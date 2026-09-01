"""Roteador do grupo: decide QUAIS Satélites respondem a uma mensagem.

Camadas 2 e 3 da cascata do PRD (docs/prd/satelites-multibots-grupo-telegram.md §4.1):
  - `mentions()`  — camada 2, GRÁTIS: só diz se algum nome aparece no texto. Não decide nada.
  - `route()`     — camada 3, PAGA: 1 chamada ao modelo, sem persona e sem INDEX.md, para
                    distinguir "Lilith, o que acha?" de "fui pra Nova York".

Falha fechada: qualquer erro, JSON inválido, id desconhecido ou confiança baixa devolve
lista vazia — ninguém responde. Nunca o contrário.
"""
import functools
import json
import logging
import re
import time
import unicodedata
from collections import deque
from dataclasses import dataclass, field
from typing import Literal

import openai
from pydantic import BaseModel, Field, ValidationError

from . import satellites, voices
from .config import settings
from .enrich import EnrichmentError

log = logging.getLogger("vegapunk.router")

CONFIDENCES = ("alta", "media", "baixa")
RECENT_LINES = 3         # linhas anteriores do grupo enviadas como contexto
MAX_RECENT_CHARS = 200   # …e cada uma é cortada: 3 linhas de 4000 chars fariam o "roteador barato" custar caro
MAX_TEXT_CHARS = 1000    # a mensagem é cortada: roteador não precisa do texto inteiro
MAX_SATELLITES = 3       # TETO DE CUSTO no modo destinatário ("Shaka e Lilith" pede os dois mesmo)
MAX_TRIAGE = 1           # …mas em TRIAGEM o Fernando não chamou ninguém: um dono, não um comitê.
                         # Produção 2026-08-28: o prompt dizia "UM só" e vieram 3 respostas de ~55k tokens.
ROUTER_TIMEOUT = 15.0    # segundos por tentativa; pior caso 30 s. Roteador que não decide rápido não decide
ROUTER_RETRIES = 1       # 1 repique: sobrevive a um 429 solitário sem virar espera de minutos
MAX_ROUTES_PER_MIN = 20  # teto da camada BARATA (~500 tokens por decisão)
WINDOW_SECONDS = 600     # janela de continuidade: 10 min sem repetir o nome (decisão do Fernando, PRD §0 d)

# Teto da camada CARA. Uma resposta em personagem custou 24.788 tokens de entrada medidos em produção
# (2026-08-28) — cerca de 50× uma decisão do roteador. Limitar só o roteador era decoração: 20 decisões
# por minuto autorizavam 60 respostas, ~1,5 milhão de tokens. O teto tem que estar aqui.
MAX_REPLIES_PER_MIN = 6     # York aprovou: o dobro do pico observado (3/min em 2026-08-28)
MAX_REPLIES_PER_HOUR = 25   # York, 2026-08-31: 60/h autorizava US$ 23,76 num dia de descontrole,
                            # contra US$ 0,33 de uso real no dia inteiro. 25/h ≈ US$ 0,41/h.

_recentes: deque[float] = deque(maxlen=MAX_ROUTES_PER_MIN)   # instantes das últimas decisões
_respostas: deque[float] = deque()                           # instantes das últimas respostas em personagem

# Como o Fernando pode chamar cada Satélite em texto livre (além do id).
ALIASES: dict[str, str] = {
    "vegapunk": "stella",
    "dr. vegapunk": "stella",
    "dr vegapunk": "stella",
}


@functools.lru_cache(maxsize=1)
def _build_client(api_key: str) -> openai.OpenAI:
    """Um cliente só, reaproveitado: no grupo o roteador roda a cada frase, e montar um cliente novo
    por mensagem significaria um handshake TLS novo por mensagem — a latência que ele deveria poupar."""
    return openai.OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,          # também é a chave do cache: chave nova = cliente novo
        default_headers={"HTTP-Referer": "https://github.com/fernand-nan-ia/Vegapunk", "X-Title": "Vegapunk"},
        timeout=ROUTER_TIMEOUT, max_retries=ROUTER_RETRIES,
    )


def _client() -> openai.OpenAI:
    """Cliente PRÓPRIO do roteador. O de `enrich` espera 180 s × 3 tentativas — feito para transcrições
    de uma hora, não para uma conversa: seriam 9 minutos de silêncio no grupo antes de falhar."""
    if not settings.openrouter_api_key:
        raise EnrichmentError("ERR-007", "OPENROUTER_API_KEY não definido")
    return _build_client(settings.openrouter_api_key)


def _fold(s: str) -> str:
    """Minúsculas e sem acento: 'Pythágoras' e 'PYTHAGORAS' viram 'pythagoras'."""
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def _name_pattern() -> re.Pattern:
    names = sorted({_fold(n) for n in list(satellites.IDS) + list(voices.NAME.values()) + list(ALIASES)},
                   key=len, reverse=True)   # mais longo primeiro: "dr. vegapunk" antes de "vegapunk"
    return re.compile(r"(?<!\w)(" + "|".join(re.escape(n) for n in names) + r")(?!\w)")


_NAMES_RE = _name_pattern()

# Link colado é o pão de cada dia deste grupo — e "site.com/atlas-map" casaria "atlas" como palavra
# inteira, pagando o roteador à toa. Some-se o link antes de procurar nomes.
_URL_RE = re.compile(r"(?:https?://|www\.)\S+|\b[\w-]+\.[a-z]{2,}/\S*", re.I)


def mentions(text: str) -> list[str]:
    """Camada 2 (grátis): ids cujos nomes aparecem como palavra inteira no texto, na ordem em que aparecem.

    NÃO decide quem responde — "fui pra Nova York" devolve ["york"] de propósito. Serve só para
    saber se vale a pena pagar o roteador; quem descarta o falso positivo é `route()`.
    """
    limpo = _URL_RE.sub(" ", _fold(text or ""))
    out: list[str] = []
    for m in _NAMES_RE.finditer(limpo):
        got = m.group(1)
        sat_id = ALIASES.get(got, got)
        if sat_id in satellites.IDS and sat_id not in out:
            out.append(sat_id)
    return out


@dataclass
class Routing:
    satellites: list[str] = field(default_factory=list)   # ids em satellites.IDS; ordem = ordem de resposta
    confidence: str = "baixa"                             # alta | media | baixa
    reason: str = ""                                      # 1 frase curta, só para o log

    def __bool__(self) -> bool:
        return bool(self.satellites)


class _RouterOut(BaseModel):
    satellites: list[str] = Field(description="ids dos Satélites chamados, na ordem; lista vazia se ninguém foi chamado")
    confidence: Literal["alta", "media", "baixa"]
    reason: str = Field(max_length=120, description="UMA frase curta em pt-BR (máx. 120 caracteres)")


def _schema() -> dict:
    """JSON Schema em modo strict (mesmo tratamento de enrich._schema)."""
    s = _RouterOut.model_json_schema()

    def harden(node):
        if isinstance(node, dict):
            if node.get("type") == "object":
                node["additionalProperties"] = False
                if "properties" in node:
                    node["required"] = list(node["properties"])
            for v in node.values():
                harden(v)

    harden(s)
    return s


# Rede de segurança: se um `.md` não puder ser lido, o roteador não pode cair junto.
ESPECIALIDADES_FALLBACK = {
    "stella": "visão ampla, ciência, síntese; responde quando nenhum outro encaixa melhor",
    "shaka": "risco, segurança, LGPD e leis, compliance, ética, decisões sérias",
    "lilith": "atacar a ideia, achar furo, caçar hype e promessa fácil, pré-mortem",
    "edison": "ideias novas, features, produto, protótipo de fim de semana",
    "pythagoras": "o que está guardado no Punk Records, pesquisa, documentos, dossiê",
    "atlas": "código, infraestrutura, banco de dados, mão na massa, laudos de engenharia",
    "york": "custo, preço, monetização, ROI, orçamento",
}


@functools.lru_cache(maxsize=1)
def especialidades() -> dict[str, str]:
    """Para que serve cada Satélite, lido do `persona.focus` do `.md` dele.

    FONTE ÚNICA (regra do projeto: `.claude/commands/vegapunk/agents/<id>.md` é a verdade). Antes havia
    um dicionário fixo aqui e ele JÁ tinha divergido do `.md` — o do York falava de preço enquanto o
    arquivo falava de healthcheck. Divergência silenciosa manda conversa para a versão velha do Satélite.
    """
    out: dict[str, str] = {}
    for i in satellites.IDS:
        try:
            foco = (satellites.load(i).data.get("persona", {}).get("focus") or "").strip()
        except Exception:
            foco = ""
        out[i] = foco[:170] if foco else ESPECIALIDADES_FALLBACK[i]
    return out


@functools.lru_cache(maxsize=2)
def system_prompt(triagem: bool = False) -> str:
    return _SYSTEM_BASE.format(
        lista="\n".join(f"- {voices.NAME[i]} ({i}): {especialidades()[i]}" for i in satellites.IDS)
    ) + (TRIAGEM if triagem else "")


_SYSTEM_BASE = (
    "Você é um roteador de mensagens de um grupo do Telegram. No grupo existem sete bots, os Satélites de "
    "Vegapunk, cada um com uma especialidade:\n{lista}\n\n"
    "Sua única tarefa: dizer a QUEM a última mensagem do usuário é dirigida. Responda apenas o JSON pedido.\n\n"
    "Regras:\n"
    "- Um nome citado como parte de um lugar, produto, marca ou pessoa real NÃO é uma chamada "
    "(ex.: \"fui pra Nova York\", \"comprei um shaka de surfe\") → lista vazia.\n"
    "- Nome usado como OBJETO da frase, e não como destinatário, não aciona aquele Satélite "
    "(ex.: \"Shaka, o que você acha do que a Lilith falou?\" → só shaka).\n"
    "- Vários destinatários na mesma mensagem → todos, na ordem em que aparecem.\n"
    "- Mensagem sem destinatário claro: se houver um Satélite marcado como ATIVO e a mensagem for "
    "continuação natural da conversa dele, devolva só ele; senão, lista vazia.\n"
    "- Na dúvida, lista vazia. Silêncio custa menos que uma resposta indevida.\n"
    "- confidence: \"alta\" quando é evidente; \"media\" quando é provável; \"baixa\" quando você não sabe.\n"
    "- reason: no máximo 120 caracteres. É para o log, não para o Fernando ler."
)

TRIAGEM = (
    "\n\n=== MODO TRIAGEM ===\n"
    "Ninguém foi chamado pelo nome nesta mensagem. Sua tarefa muda: em vez de 'a quem é dirigida', decida "
    "QUEM RESPONDE MELHOR pelo ASSUNTO, usando as especialidades acima. Devolva UM só, o mais adequado — "
    "e o Stella quando nenhum outro encaixar claramente.\n"
    "Mas continue devolvendo lista VAZIA quando a mensagem não pede resposta: recado para si mesmo, "
    "'ok', 'kkk', 'valeu', reação a algo, ou frase solta sem pergunta nem pedido. Silêncio ainda é a opção "
    "segura; o que mudou é que dúvida sobre um ASSUNTO agora merece dono."
)


def _user_prompt(text: str, recent: list[str] | None, active: str | None) -> str:
    parts = []
    if recent:
        linhas = [l[:MAX_RECENT_CHARS] for l in recent[-RECENT_LINES:]]
        parts.append("ÚLTIMAS LINHAS DO GRUPO (mais antiga primeiro):\n" + "\n".join(linhas))
    parts.append(f"SATÉLITE ATIVO: {active or '(nenhum)'}")
    parts.append(f"MENSAGEM:\n{(text or '')[:MAX_TEXT_CHARS]}")
    return "\n\n".join(parts)


def _dentro_do_teto() -> bool:
    """Achado 8 da Lilith: sem teto, rajada de mensagens vira rajada de chamadas pagas."""
    agora = time.monotonic()
    if len(_recentes) == MAX_ROUTES_PER_MIN and agora - _recentes[0] < 60:
        return False
    _recentes.append(agora)
    return True


def pode_responder() -> bool:
    """Teto da camada 4 (a cara). Chamar UMA vez por resposta, imediatamente antes de gastar.

    Dois horizontes: o por minuto segura a rajada, o por hora segura a tarde inteira — foi a tarde
    que a York sempre teve medo de pagar.
    """
    agora = time.monotonic()
    while _respostas and agora - _respostas[0] > 3600:
        _respostas.popleft()
    if sum(1 for t in _respostas if agora - t < 60) >= MAX_REPLIES_PER_MIN:
        log.warning("teto de %s respostas por minuto atingido: silêncio até baixar", MAX_REPLIES_PER_MIN)
        return False
    if len(_respostas) >= MAX_REPLIES_PER_HOUR:
        log.warning("teto de %s respostas por hora atingido: silêncio até baixar", MAX_REPLIES_PER_HOUR)
        return False
    _respostas.append(agora)
    return True


def route(text: str, recent: list[str] | None = None, active: str | None = None,
          triagem: bool = False) -> Routing:
    """Camada 3 (paga): 1 chamada ao modelo decide quem responde. Sempre falha fechada.

    `triagem=True`: ninguém foi chamado pelo nome; escolher pelo ASSUNTO (pedido do Fernando, 2026-08-28).
    """
    if not _dentro_do_teto():
        return _closed(text, f"teto de {MAX_ROUTES_PER_MIN} chamadas por minuto estourado")
    model = settings.router_model or settings.model
    try:
        resp = _client().chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": system_prompt(triagem)},
                      {"role": "user", "content": _user_prompt(text, recent, active)}],
            max_tokens=400,        # 200 cortava o JSON no meio do `reason` (produção, 2026-08-28)
            temperature=0,
            response_format={"type": "json_schema",
                             "json_schema": {"name": "routing", "strict": True, "schema": _schema()}},
        )
        raw = (resp.choices[0].message.content or "") if resp.choices else ""
        out = _RouterOut.model_validate(json.loads(raw))
    except (openai.OpenAIError, EnrichmentError, json.JSONDecodeError, ValidationError,
            KeyError, IndexError, AttributeError) as e:
        return _closed(text, f"erro: {type(e).__name__}: {str(e)[:120]}")
    except Exception as e:                        # nada escapa deste módulo: silêncio é o padrão seguro
        log.exception("roteador falhou de forma inesperada")
        return _closed(text, f"erro inesperado: {type(e).__name__}: {str(e)[:120]}")

    desconhecidos = [s for s in out.satellites if s not in satellites.IDS]
    if desconhecidos:
        return _closed(text, f"id desconhecido devolvido pelo modelo: {desconhecidos}")

    chosen: list[str] = [] if out.confidence == "baixa" else list(dict.fromkeys(out.satellites))
    teto = MAX_TRIAGE if triagem else MAX_SATELLITES   # instrução sem enforcement é sugestão
    if len(chosen) > teto:
        log.warning("roteador devolveu %s Satélites; cortando em %s (teto de custo, triagem=%s)",
                    len(chosen), teto, triagem)
        chosen = chosen[:teto]
    usage = resp.usage
    log.info("roteador %s -> %s (%s) %s · %s in / %s out tokens",
             _oneline(text)[:80], chosen, out.confidence, _oneline(out.reason)[:120],
             getattr(usage, "prompt_tokens", 0), getattr(usage, "completion_tokens", 0))
    return Routing(satellites=chosen, confidence=out.confidence, reason=out.reason)


def decide(text: str, *, explicitos: list[str] | None = None, ativo: str | None = None,
           idade_do_ativo: float | None = None, recent: list[str] | None = None) -> Routing:
    """A cascata inteira numa função só (PRD §4.1, camadas 1 a 3).

    Existe por causa do achado 7 da Lilith: enquanto compor as camadas fosse tarefa de quem chama,
    alguém acabaria pulando `mentions()` e pagando o roteador em toda mensagem do grupo. Aqui não há
    como: `route()` só é alcançado depois das duas peneiras grátis.

      camada 1 · `@menção` explícita → responde direto, SEM roteador (caminho de escape determinístico)
      camada 2 · nenhum nome no texto E fora da janela de continuidade → ninguém, custo zero
      camada 3 · roteador decide

    `idade_do_ativo` = segundos desde a última interação no chat (None = nunca houve).
    """
    if explicitos:
        escolhidos = [s for s in dict.fromkeys(explicitos) if s in satellites.IDS][:MAX_SATELLITES]
        if escolhidos:
            return Routing(escolhidos, "alta", "menção explícita: não passa pelo roteador")

    citados = mentions(text)
    na_janela = idade_do_ativo is not None and idade_do_ativo <= WINDOW_SECONDS
    if not citados and not na_janela:
        if not settings.group_triage:
            return Routing([], "alta", "sem nome no texto e fora da janela: custo zero")
        # Pedido do Fernando (2026-08-28): sem nome, o roteador triage pelo ASSUNTO e escolhe o dono —
        # pode ser o próprio Stella. Troca a propriedade "silêncio é grátis" por ~500 tokens por mensagem;
        # a trava de custo real continua sendo `pode_responder()` (6/min, 60/h).
        return route(text, recent=recent, active=None, triagem=True)

    return route(text, recent=recent, active=ativo if na_janela else None)


def _oneline(s: str) -> str:
    """O log do projeto é uma linha JSON: aspas e quebras vindas do modelo corromperiam o registro."""
    return (s or "").replace("\n", " ").replace("\r", " ").replace('"', "'")


def _closed(text: str, reason: str) -> Routing:
    """Falha fechada: ninguém responde, e o motivo fica no log para auditoria."""
    log.warning("roteador falhou fechado em %s: %s", _oneline(text)[:80], _oneline(reason))
    return Routing(satellites=[], confidence="baixa", reason=reason)
