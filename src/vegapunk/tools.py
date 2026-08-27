"""Ferramentas dos Satélites no Telegram (tool-use via OpenRouter).

Somente leitura sobre o Punk Records, o banco e o git — mais o diário do próprio Satélite (escrita explícita).
Nada aqui executa código do projeto, edita o vault ou faz push: isso é Labophase (Claude Code).
"""
import json
import logging
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from . import satellites
from .config import ROOT, settings

log = logging.getLogger("vegapunk.tools")

MAX_ITEM_CHARS = 12_000

SPECS = [
    {"type": "function", "function": {
        "name": "search_punk_records",
        "description": "Busca itens do Punk Records por palavras (título, tags e corpo). Use antes de afirmar o que o vault tem ou não tem.",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string", "description": "palavras-chave ou pergunta"},
            "limit": {"type": "integer", "description": "máximo de resultados (1-8)", "default": 5}},
            "required": ["query"]}}},
    {"type": "function", "function": {
        "name": "read_item",
        "description": "Lê um item do Punk Records pelo caminho relativo (ex.: article/2026-08-27_x.md). Devolve o Markdown (até 12k chars).",
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string", "description": "caminho relativo a punk_records/, como aparece no índice ou na busca"}},
            "required": ["path"]}}},
    {"type": "function", "function": {
        "name": "punk_records_status",
        "description": "Saúde e custo: itens por estado, sem triagem, presos em _pending, última captura, tokens gastos (resumos e conversas) e custo estimado em US$.",
        "parameters": {"type": "object", "properties": {}}}},
    {"type": "function", "function": {
        "name": "recent_changes",
        "description": "O que entrou ou foi triado no Punk Records nos últimos N dias (git log).",
        "parameters": {"type": "object", "properties": {
            "days": {"type": "integer", "description": "janela em dias", "default": 7}}}}},
    {"type": "function", "function": {
        "name": "write_diary",
        "description": "Anota no SEU diário um fato que o Fernando disse explicitamente sobre ele, seus projetos ou decisões (nunca inferência, nunca conteúdo do vault). Uma linha.",
        "parameters": {"type": "object", "properties": {
            "fact": {"type": "string", "description": "o fato, em uma frase curta"}},
            "required": ["fact"]}}},
]

PRICE_IN, PRICE_OUT = 0.375 / 1e6, 1.875 / 1e6   # google/gemini-3.7-flash (OpenRouter, 2026-08)


def _strip_frontmatter(md: str) -> str:
    return md.split("---", 2)[-1].strip() if md.startswith("---") else md


def search_punk_records(query: str, limit: int = 5, vault_dir: Path | None = None) -> dict:
    limit = max(1, min(int(limit or 5), 8))
    hits = satellites.search_index(query, vault_dir=vault_dir, limit=limit)
    out = []
    for score, title, rel, body in hits:
        m = re.search(r"## Resumo\s*\n+(.+?)(?:\n\n|\Z)", body, flags=re.S)
        out.append({"title": title, "path": rel, "score": score, "summary": (m.group(1) if m else body[:300]).strip()[:400]})
    return {"query": query, "results": out, "note": "" if out else "nenhum item bate com essas palavras — não há registro"}


def read_item(path: str, vault_dir: Path | None = None) -> dict:
    vault_dir = (vault_dir or settings.vault_dir).resolve()
    p = (vault_dir / path).resolve()
    if vault_dir not in p.parents or not p.is_file() or p.suffix != ".md":
        return {"error": f"caminho inválido ou inexistente: {path}"}
    md = p.read_text(encoding="utf-8")
    return {"path": path, "content": _strip_frontmatter(md)[:MAX_ITEM_CHARS], "truncated": len(md) > MAX_ITEM_CHARS}


def punk_records_status(db) -> dict:
    c = db.conn
    by_status = {r[0]: r[1] for r in c.execute("SELECT status, COUNT(*) FROM knowledge_items GROUP BY 1")}
    untriaged = c.execute("SELECT COUNT(*) FROM knowledge_items WHERE status='enriched'").fetchone()[0]
    pending = [dict(r) for r in c.execute(
        "SELECT substr(id,1,8) id, status, COALESCE(title, raw_url) title FROM knowledge_items"
        " WHERE status IN ('extraction_failed','enrichment_failed','pending_manual') ORDER BY created_at DESC LIMIT 10")]
    last = c.execute("SELECT MAX(captured_at) FROM knowledge_items").fetchone()[0]
    n_e, in_e, out_e = c.execute(
        "SELECT COUNT(*), COALESCE(SUM(json_extract(metadata,'$.input_tokens')),0), COALESCE(SUM(json_extract(metadata,'$.output_tokens')),0)"
        " FROM item_events WHERE to_status='enriched'").fetchone()
    try:
        n_c, in_c, out_c = c.execute(
            "SELECT COUNT(*), COALESCE(SUM(input_tokens),0), COALESCE(SUM(output_tokens),0) FROM chat_messages WHERE role='assistant'").fetchone()
    except Exception:
        n_c = in_c = out_c = 0
    cost = (in_e + in_c) * PRICE_IN + (out_e + out_c) * PRICE_OUT
    return {"items_by_status": by_status, "untriaged": untriaged, "stuck": pending, "last_capture": last,
            "tokens": {"enrich_calls": n_e, "enrich_in": in_e, "enrich_out": out_e, "chat_replies": n_c, "chat_in": in_c, "chat_out": out_c},
            "estimated_cost_usd": round(cost, 4), "model": settings.model,
            "price_per_million_usd": {"input": PRICE_IN * 1e6, "output": PRICE_OUT * 1e6}}


def recent_changes(days: int = 7) -> dict:
    days = max(1, min(int(days or 7), 90))
    try:
        r = subprocess.run(["git", "log", f"--since={days} days ago", "--pretty=format:%ad · %s", "--date=short", "--",
                            str(settings.vault_dir)], cwd=ROOT, capture_output=True, text=True, timeout=30)
        lines = [l for l in r.stdout.splitlines() if l.strip()]
    except Exception as e:  # git ausente/timeout
        return {"error": str(e)}
    return {"days": days, "commits": lines[:60], "count": len(lines)}


def write_diary(sat_id: str, fact: str, memory_dir: Path | None = None) -> dict:
    fact = " ".join(fact.split())[:300]
    if not fact:
        return {"error": "fato vazio"}
    p = (memory_dir or satellites.MEMORY_DIR) / f"{sat_id}.md"
    text = p.read_text(encoding="utf-8") if p.exists() else f"# {sat_id} — diário\n\n## Sobre o Fernando\n\n## Diário\n"
    line = f"- {datetime.now(timezone.utc).date().isoformat()} · {fact}"
    lines = text.rstrip("\n").split("\n")
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == "## Diário")
    except StopIteration:
        lines += ["", "## Diário"]
        start = len(lines) - 1
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    while end > start + 1 and not lines[end - 1].strip():
        end -= 1
    lines.insert(end, line)
    if end + 1 < len(lines) and lines[end + 1].startswith("## "):
        lines.insert(end + 1, "")
    text = "\n".join(lines) + "\n"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return {"written": line}


def run_tool(name: str, args: dict, *, sat_id: str, db) -> str:
    """Executa uma ferramenta e devolve JSON (string) para o modelo."""
    try:
        if name == "search_punk_records":
            res = search_punk_records(args.get("query", ""), args.get("limit", 5))
        elif name == "read_item":
            res = read_item(args.get("path", ""))
        elif name == "punk_records_status":
            res = punk_records_status(db)
        elif name == "recent_changes":
            res = recent_changes(args.get("days", 7))
        elif name == "write_diary":
            res = write_diary(sat_id, args.get("fact", ""))
        else:
            res = {"error": f"ferramenta desconhecida: {name}"}
    except Exception as e:
        log.exception("tool %s falhou", name)
        res = {"error": f"{type(e).__name__}: {e}"}
    return json.dumps(res, ensure_ascii=False)
