"""Conversa com os Satélites pelo Telegram: estado por chat + histórico curto no SQLite + OpenRouter."""
import logging
from datetime import datetime, timezone

import openai

from . import satellites
from .config import settings
from .db import Database
from .enrich import EnrichmentError, _client

log = logging.getLogger("vegapunk.chat")

HISTORY_TURNS = 12          # mensagens (user+assistant) enviadas ao modelo
MAX_USER_CHARS = 4000
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
    def build_messages(self, chat_id: int, sat: satellites.Satellite, user_text: str) -> list[dict]:
        system = satellites.build_system_prompt(sat, diary_text=satellites.diary(sat.id), index_text=satellites.index_text())
        msgs = [{"role": "system", "content": system}] + self.history(chat_id, sat.id)
        items = satellites.pick_vault_items(user_text)
        if items:
            attached = "\n\n".join(f"--- ITEM {rel} ---\n{body}" for rel, body in items)
            msgs.append({"role": "system", "content": "Itens do Punk Records possivelmente relevantes à próxima mensagem "
                                                       "(cite pelo título; ignore se não vierem ao caso):\n\n" + attached})
        msgs.append({"role": "user", "content": user_text[:MAX_USER_CHARS]})
        return msgs

    def reply(self, chat_id: int, user_text: str) -> tuple[satellites.Satellite, str]:
        """Síncrono (chamar via asyncio.to_thread). Acorda Stella se ninguém estiver ativo."""
        sat_id = self.active(chat_id) or satellites.DEFAULT
        sat = self.wake(chat_id, sat_id)
        messages = self.build_messages(chat_id, sat, user_text)
        client = _client()
        try:
            resp = client.chat.completions.create(model=settings.model, messages=messages, max_tokens=1200, temperature=0.8)
        except openai.RateLimitError as e:
            raise EnrichmentError("ERR-006", f"rate limit: {e}")
        except openai.APIStatusError as e:
            raise EnrichmentError("ERR-006" if e.status_code >= 500 else "ERR-007", f"api {e.status_code}: {e.message}")
        except openai.APIConnectionError as e:
            raise EnrichmentError("ERR-006", f"conexão: {e}")
        text = (resp.choices[0].message.content or "").strip() if resp.choices else ""
        if not text:
            raise EnrichmentError("ERR-007", "resposta vazia do modelo")
        usage = {"model": resp.model or settings.model,
                 "input_tokens": resp.usage.prompt_tokens if resp.usage else None,
                 "output_tokens": resp.usage.completion_tokens if resp.usage else None}
        with self.db.tx():
            self._save(chat_id, sat.id, "user", user_text[:MAX_USER_CHARS])
            self._save(chat_id, sat.id, "assistant", text, usage)
        log.info("chat %s/%s: %s in / %s out tokens", chat_id, sat.id, usage["input_tokens"], usage["output_tokens"])
        return sat, text
