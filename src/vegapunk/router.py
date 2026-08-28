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
import unicodedata
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
MAX_SATELLITES = 3       # TETO DE CUSTO: nenhuma mensagem aciona mais que isto, aconteça o que acontecer
ROUTER_TIMEOUT = 15.0    # segundos por tentativa; pior caso 30 s. Roteador que não decide rápido não decide
ROUTER_RETRIES = 1       # 1 repique: sobrevive a um 429 solitário sem virar espera de minutos

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
    reason: str = Field(description="uma frase curta em pt-BR explicando a decisão")


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


SYSTEM = (
    "Você é um roteador de mensagens de um grupo do Telegram. No grupo existem sete bots, os Satélites de "
    "Vegapunk: " + ", ".join(f"{voices.NAME[i]} ({i})" for i in satellites.IDS) + ".\n\n"
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
    "- confidence: \"alta\" quando é evidente; \"media\" quando é provável; \"baixa\" quando você não sabe."
)


def _user_prompt(text: str, recent: list[str] | None, active: str | None) -> str:
    parts = []
    if recent:
        linhas = [l[:MAX_RECENT_CHARS] for l in recent[-RECENT_LINES:]]
        parts.append("ÚLTIMAS LINHAS DO GRUPO (mais antiga primeiro):\n" + "\n".join(linhas))
    parts.append(f"SATÉLITE ATIVO: {active or '(nenhum)'}")
    parts.append(f"MENSAGEM:\n{(text or '')[:MAX_TEXT_CHARS]}")
    return "\n\n".join(parts)


def route(text: str, recent: list[str] | None = None, active: str | None = None) -> Routing:
    """Camada 3 (paga): 1 chamada ao modelo decide quem responde. Sempre falha fechada."""
    model = settings.router_model or settings.model
    try:
        resp = _client().chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": SYSTEM},
                      {"role": "user", "content": _user_prompt(text, recent, active)}],
            max_tokens=200,
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
    if len(chosen) > MAX_SATELLITES:
        log.warning("roteador devolveu %s Satélites; cortando em %s (teto de custo)", len(chosen), MAX_SATELLITES)
        chosen = chosen[:MAX_SATELLITES]
    usage = resp.usage
    log.info("roteador %s -> %s (%s) %s · %s in / %s out tokens",
             _oneline(text)[:80], chosen, out.confidence, _oneline(out.reason)[:120],
             getattr(usage, "prompt_tokens", 0), getattr(usage, "completion_tokens", 0))
    return Routing(satellites=chosen, confidence=out.confidence, reason=out.reason)


def _oneline(s: str) -> str:
    """O log do projeto é uma linha JSON: aspas e quebras vindas do modelo corromperiam o registro."""
    return (s or "").replace("\n", " ").replace("\r", " ").replace('"', "'")


def _closed(text: str, reason: str) -> Routing:
    """Falha fechada: ninguém responde, e o motivo fica no log para auditoria."""
    log.warning("roteador falhou fechado em %s: %s", _oneline(text)[:80], _oneline(reason))
    return Routing(satellites=[], confidence="baixa", reason=reason)
