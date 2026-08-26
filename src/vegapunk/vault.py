"""Vault Markdown (projeção do SQLite) + INDEX.md + git commit."""
import json
import logging
import re
import subprocess
from pathlib import Path

from slugify import slugify

from .config import ROOT, settings

log = logging.getLogger("vegapunk.vault")

SENTINEL = "## Notas manuais"
TRIAGE_LABEL = {"archive": "archived", "apply_saas": "applied_saas", "apply_client": "applied_client", "discard": "discarded"}


def _yaml_str(s) -> str:
    return json.dumps(s if s is not None else "", ensure_ascii=False)


def _yaml_list(xs) -> str:
    return "[" + ", ".join(_yaml_str(x) for x in xs) + "]"


def item_filename(item: dict) -> str:
    date = (item["captured_at"] or "")[:10]
    title = (json.loads(item["enrichment"])["title"] if item.get("enrichment") else item.get("title")) or "sem-titulo"
    return f"{date}_{slugify(title, max_length=60)}_{item['external_id']}.md"


def item_path(item: dict) -> Path:
    sub = "_pending" if item["status"] == "pending_manual" or not item.get("enrichment") else item["platform"]
    return settings.vault_dir / sub / item_filename(item)


def render(item: dict, manual_notes: str = "") -> str:
    e = json.loads(item["enrichment"]) if item.get("enrichment") else None
    tags = e["tags"] if e else []
    app = e["applicability"] if e else {}
    fm = [
        "---",
        f"item_id: {_yaml_str(item['id'])}",
        f"platform: {item['platform']}",
        f"external_id: {_yaml_str(item['external_id'])}",
        f"canonical_url: {_yaml_str(item['canonical_url'])}",
        f"channel: {_yaml_str(item.get('channel'))}",
        f"captured_at: {(item['captured_at'] or '')[:10]}",
        f"status: {item['status']}",
        f"triage: {item.get('triage_decision') or 'null'}",
        f"tags: {_yaml_list(tags)}",
        "applicability:",
        f"  saas_pessoal: {app.get('saas_pessoal', 'null')}",
        f"  projeto_cliente: {app.get('projeto_cliente', 'null')}",
        f"  estudo_geral: {app.get('estudo_geral', 'null')}",
        f"confidence: {e['confidence'] if e else 'null'}",
        f"content_type: {item.get('content_type') or 'null'}",
        "---",
        "",
    ]
    title = (e["title"] if e else item.get("title")) or item["canonical_url"]
    body = [f"# {title}", "", f"🔗 {item['canonical_url']}", ""]
    if e:
        body += ["## Resumo", "", e["summary"], "", "## Pontos-chave", ""]
        body += [f"- {p}" for p in e["key_points"]]
        if e.get("how_to_apply"):
            body += ["", "## Como aplicar", "", e["how_to_apply"]]
    else:
        body += ["_Pendente de extração automática. Cole o conteúdo em Notas manuais e rode `/reprocess`._"]
        if item.get("error_code"):
            body += ["", f"Erro: `{item['error_code']}` — {(item.get('error_detail') or '')[:300]}"]
    body += ["", SENTINEL, "", "<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->", ""]
    if manual_notes:
        body += [manual_notes.rstrip(), ""]
    return "\n".join(fm + body)


def read_manual_notes(path: Path) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    idx = text.find(SENTINEL)
    if idx < 0:
        return ""
    after = text[idx + len(SENTINEL):]
    after = re.sub(r"^\s*<!--.*?-->\s*", "", after, count=1, flags=re.S)
    return after.strip()


def write_item(item: dict) -> Path:
    path = item_path(item)
    path.parent.mkdir(parents=True, exist_ok=True)
    old = Path(item["vault_path"]) if item.get("vault_path") else None
    notes = read_manual_notes(old) if old and old.exists() else read_manual_notes(path)
    path.write_text(render(item, notes), encoding="utf-8")
    if old and old.exists() and old.resolve() != path.resolve():
        old.unlink()
    return path


def write_index(items: list[dict]) -> Path:
    lines = ["# Vegapunk — Índice da memória", "", "Gerado automaticamente. Um item por linha: data · plataforma · título · tags · aplicabilidade (saas/cliente/estudo) · triagem.", ""]
    for it in items:
        e = json.loads(it["enrichment"])
        a = e["applicability"]
        rel = Path(it["vault_path"]).relative_to(settings.vault_dir) if it.get("vault_path") else ""
        lines.append(
            f"- {it['captured_at'][:10]} · {it['platform']} · [{e['title']}]({rel}) · "
            f"`{'` `'.join(e['tags'])}` · {a['saas_pessoal']}/{a['projeto_cliente']}/{a['estudo_geral']} · {it.get('triage_decision') or '—'}"
        )
    p = settings.vault_dir / "INDEX.md"
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return p


def git_commit(message: str) -> bool:
    if not settings.git_commit:
        return False
    try:
        run = lambda *a: subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True, timeout=60)
        run("config", "--global", "--add", "safe.directory", str(ROOT))
        run("add", str(settings.vault_dir))
        r = run("commit", "-m", message)
        if r.returncode != 0 and "nothing to commit" not in r.stdout + r.stderr:
            log.warning("git commit falhou: %s", r.stderr.strip())
            return False
        if settings.git_push:
            p = run("push")
            if p.returncode != 0:
                log.warning("git push falhou (ERR-008): %s", p.stderr.strip()[:300])
        return True
    except Exception as e:  # git nunca derruba o pipeline
        log.warning("git erro: %s", e)
        return False
