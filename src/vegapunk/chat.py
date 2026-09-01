"""Conversa com os Satélites pelo Telegram: estado por chat + histórico curto no SQLite + OpenRouter."""
import logging
from datetime import datetime, timezone

import json

import openai

from . import satellites, tools, voices
from .config import settings
from .db import Database
from .enrich import EnrichmentError, _client

log = logging.getLogger("vegapunk.chat")

HISTORY_TURNS = 12          # mensagens (user+assistant) enviadas ao modelo
MAX_USER_CHARS = 4000
MAX_TOOL_ROUNDS_CHAT = 3    # conversa livre: buscar/ler um pouco e responder
MAX_TOOL_ROUNDS_CMD = 8     # comando (*attack, *dossier…): procedimento pede mais leitura
SCHEMA = """
CREATE TABLE IF NOT EXISTS chat_state (
  chat_id INTEGER PRIMARY KEY,
  satellite TEXT NOT NULL,
  updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS chat_messages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  chat_id INTEGER NOT NULL,
  satellite TEXT NOT NULL,
  role TEXT NOT NULL,
  content TEXT NOT NULL,
  input_tokens INTEGER, output_tokens INTEGER, model TEXT,
  created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_chat_messages ON chat_messages (chat_id, satellite, id);
"""


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class Chat:
    def __init__(self, db: Database):
        self.db = db
        db.conn.executescript(SCHEMA)

    # ── estado ────────────────────────────────────────────
    def active(self, chat_id: int) -> str | None:
        r = self.db.conn.execute("SELECT satellite FROM chat_state WHERE chat_id=?", (chat_id,)).fetchone()
        return r["satellite"] if r else None

    def active_age(self, chat_id: int) -> tuple[str | None, float | None]:
        """Quem falou por último e há quantos segundos — base da janela de continuidade (10 min).

        `wake()` atualiza `updated_at` a cada resposta, então isto mede a última interação real.
        """
        r = self.db.conn.execute("SELECT satellite, updated_at FROM chat_state WHERE chat_id=?",
                                 (chat_id,)).fetchone()
        if not r:
            return None, None
        try:
            quando = datetime.fromisoformat(r["updated_at"])
        except ValueError:
            return r["satellite"], None
        if quando.tzinfo is None:
            quando = quando.replace(tzinfo=timezone.utc)
        return r["satellite"], (datetime.now(timezone.utc) - quando).total_seconds()

    def wake(self, chat_id: int, sat_id: str) -> satellites.Satellite:
        sat = satellites.load(sat_id)
        self.db.conn.execute(
            "INSERT INTO chat_state (chat_id, satellite, updated_at) VALUES (?,?,?)"
            " ON CONFLICT(chat_id) DO UPDATE SET satellite=excluded.satellite, updated_at=excluded.updated_at",
            (chat_id, sat_id, _now()))
        return sat

    def sleep(self, chat_id: int):
        self.db.conn.execute("DELETE FROM chat_state WHERE chat_id=?", (chat_id,))

    def forget(self, chat_id: int, sat_id: str | None = None) -> int:
        if sat_id:
            cur = self.db.conn.execute("DELETE FROM chat_messages WHERE chat_id=? AND satellite=?", (chat_id, sat_id))
        else:
            cur = self.db.conn.execute("DELETE FROM chat_messages WHERE chat_id=?", (chat_id,))
        return cur.rowcount

    def history(self, chat_id: int, sat_id: str, limit: int = HISTORY_TURNS) -> list[dict]:
        rows = self.db.conn.execute(
            "SELECT role, content FROM chat_messages WHERE chat_id=? AND satellite=? ORDER BY id DESC LIMIT ?",
            (chat_id, sat_id, limit)).fetchall()
        return [{"role": r["role"], "content": r["content"]} for r in reversed(rows)]

    def _save(self, chat_id, sat_id, role, content, usage=None):
        u = usage or {}
        self.db.conn.execute(
            "INSERT INTO chat_messages (chat_id, satellite, role, content, input_tokens, output_tokens, model, created_at)"
            " VALUES (?,?,?,?,?,?,?,?)",
            (chat_id, sat_id, role, content, u.get("input_tokens"), u.get("output_tokens"), u.get("model"), _now()))

    def cost_rows(self, chat_id: int) -> list[tuple[str, int, int, int]]:
        rows = self.db.conn.execute(
            "SELECT satellite, COUNT(*) n, COALESCE(SUM(input_tokens),0) i, COALESCE(SUM(output_tokens),0) o"
            " FROM chat_messages WHERE chat_id=? AND role='assistant' GROUP BY satellite ORDER BY n DESC", (chat_id,)).fetchall()
        return [(r["satellite"], r["n"], r["i"], r["o"]) for r in rows]

    # ── conversa ──────────────────────────────────────────
    def build_messages(self, chat_id: int, sat: satellites.Satellite, user_text: str, command: tuple[str, str] | None = None) -> list[dict]:
        system = satellites.build_system_prompt(sat, diary_text=satellites.diary(sat.id), index_text=satellites.index_text())
        system += ("\n\n=== FERRAMENTAS ===\nVocê TEM ferramentas de leitura sobre o Punk Records (search_punk_records, read_item, "
                   "punk_records_status, recent_changes) e write_diary. Quando o Fernando pergunta algo sobre o vault, custo, saúde ou o que "
                   "entrou, USE-AS antes de responder — nunca afirme de memória o que a ferramenta pode confirmar. Continua sem poder: executar "
                   "código, editar o vault, rodar testes, fazer push (isso é no Claude Code). Depois das ferramentas, responda em texto simples.")
        msgs = [{"role": "system", "content": system}] + self.history(chat_id, sat.id)
        if command:
            name, args = command
            proc = satellites.procedure(sat, name)
            info = satellites.command_info(sat, name) or {}
            msgs.append({"role": "system", "content":
                f"=== COMANDO *{name} ===\n{info.get('description', '')}\n\nPROCEDIMENTO (siga na sua voz; passos que exigem "
                f"executar código, ler arquivos do projeto ou editar algo não estão disponíveis aqui — diga o que faria e siga com o que dá; "
                f"'ler o .md' = read_item; 'ler INDEX' = índice acima ou search_punk_records; 'vault' = Punk Records):\n{proc}\n\n"
                f"Formato: texto simples para Telegram, até ~25 linhas, listas curtas com '-'. Argumento do Fernando: {args or '(nenhum)'}"})
        else:
            items = satellites.pick_vault_items(user_text)
            if items:
                attached = "\n\n".join(f"--- ITEM {rel} ---\n{body}" for rel, body in items)
                msgs.append({"role": "system", "content": "Itens do Punk Records possivelmente relevantes à próxima mensagem "
                                                           "(cite pelo título; ignore se não vierem ao caso):\n\n" + attached})
        msgs.append({"role": "user", "content": user_text[:MAX_USER_CHARS]})
        return msgs

    @staticmethod
    def unavailable_reply(sat: satellites.Satellite, name: str) -> str | None:
        """Texto pronto (zero tokens) para *help e para comandos que só existem no Claude Code. None = comando roda aqui."""
        allowed = satellites.TELEGRAM_COMMANDS.get(sat.id, [])
        if name in allowed:
            return None
        lines = [f"- *{c['name']} — {c.get('description', '')[:90]}" for c in sat.data.get("commands", []) if c["name"] in allowed]
        menu = "\n".join(lines) or "- (nenhum)"
        if name == "help":
            return (f"{voices.speaker_plain(sat.id)}: aqui no Telegram eu faço cabeça, não mão. Comandos disponíveis:\n{menu}\n\n"
                    f"Os outros (código, testes, arquivos, push) se fazem no Claude Code: /vegapunk:{sat.id}.")
        if satellites.command_info(sat, name):
            return (f"{voices.speaker_plain(sat.id)}: *{name} precisa de mãos — arquivos do projeto, testes ou git — e aqui eu só tenho a cabeça. "
                    f"Se faz no Claude Code: /vegapunk:{sat.id} → *{name}. Aqui posso:\n{menu}")
        return f"{voices.speaker_plain(sat.id)}: não conheço *{name}. Mande *help para ver o que eu faço por aqui."

    def reply(self, chat_id: int, user_text: str, as_sat: str | None = None) -> tuple[satellites.Satellite, str]:
        """Síncrono (chamar via asyncio.to_thread). Loop de ferramentas.

        `as_sat` = responder COMO este Satélite (o grupo, onde quem responde é decidido pela cascata).
        Sem ele, vale o ativo do chat, e Stella se ninguém estiver acordado — comportamento da DM.
        """
        sat_id = as_sat or self.active(chat_id) or satellites.DEFAULT
        sat = self.wake(chat_id, sat_id)
        command = satellites.parse_command(user_text)
        if command:
            canned = self.unavailable_reply(sat, command[0])
            if canned:
                return sat, canned
        messages = self.build_messages(chat_id, sat, user_text, command)
        client = _client()
        usage = {"model": settings.model, "input_tokens": 0, "output_tokens": 0}
        rounds = MAX_TOOL_ROUNDS_CMD if command else MAX_TOOL_ROUNDS_CHAT
        text = ""
        for i in range(rounds + 1):
            use_tools = i < rounds
            try:
                resp = client.chat.completions.create(
                    model=settings.model, messages=messages, max_tokens=1500, temperature=0.8 if not command else 0.5,
                    **({"tools": tools.SPECS, "tool_choice": "auto"} if use_tools else {}))
            except openai.RateLimitError as e:
                raise EnrichmentError("ERR-006", f"rate limit: {e}")
            except openai.APIStatusError as e:
                raise EnrichmentError("ERR-006" if e.status_code >= 500 else "ERR-007", f"api {e.status_code}: {e.message}")
            except openai.APIConnectionError as e:
                raise EnrichmentError("ERR-006", f"conexão: {e}")
            if resp.usage:
                usage["input_tokens"] += resp.usage.prompt_tokens or 0
                usage["output_tokens"] += resp.usage.completion_tokens or 0
            usage["model"] = resp.model or settings.model
            msg = resp.choices[0].message if resp.choices else None
            calls = getattr(msg, "tool_calls", None) if msg else None
            if calls:
                messages.append({"role": "assistant", "content": msg.content or "",
                                 "tool_calls": [{"id": c.id, "type": "function",
                                                 "function": {"name": c.function.name, "arguments": c.function.arguments}} for c in calls]})
                for c in calls:
                    try:
                        args = json.loads(c.function.arguments or "{}")
                    except json.JSONDecodeError:
                        args = {}
                    log.info("chat %s/%s tool %s %s", chat_id, sat.id, c.function.name, json.dumps(args, ensure_ascii=False)[:120])
                    messages.append({"role": "tool", "tool_call_id": c.id, "content": tools.run_tool(c.function.name, args, sat_id=sat.id, db=self.db)})
                continue
            text = (msg.content or "").strip() if msg else ""
            break
        if not text:
            raise EnrichmentError("ERR-007", "resposta vazia do modelo")
        with self.db.tx():
            self._save(chat_id, sat.id, "user", user_text[:MAX_USER_CHARS])
            self._save(chat_id, sat.id, "assistant", text, usage)
        log.info("chat %s/%s: %s in / %s out tokens", chat_id, sat.id, usage["input_tokens"], usage["output_tokens"])
        return sat, text
