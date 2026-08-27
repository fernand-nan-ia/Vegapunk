"""Vault Markdown (projeção do SQLite) + INDEX.md + git commit."""
import json
import logging
import re
import subprocess
from pathlib import Path

from slugify import slugify

from .config import ROOT, settings
from . import themes

log = logging.getLogger("vegapunk.vault")

SENTINEL = "## Notas manuais"
TRIAGE_LABEL = {"archive": "archived", "apply_saas": "applied_saas", "apply_client": "applied_client", "discard": "discarded"}
TRIAGE_HUMAN = {"archive": "📁 Arquivado", "apply_saas": "🚀 Marcado para SaaS",
                "apply_client": "👤 Marcado para Cliente", "discard": "🗑 Descartado"}


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
        f"canonical_url: {_yaml_str(Path(item['canonical_url'].removeprefix('file://')).name if item.get('platform') == 'document' else item['canonical_url'])}",
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
        f"theme: {themes.theme_of(e) if e else 'null'}",
        f"content_type: {item.get('content_type') or 'null'}",
        "---",
        "",
    ]
    title = (e["title"] if e else item.get("title")) or item["canonical_url"]
    src = item["canonical_url"]
    if item.get("platform") == "document":
        src = f"📎 {Path(src.removeprefix('file://')).name} (enviado pelo Telegram)"
    else:
        src = f"🔗 {src}"
    body = [f"# {title}", "", src, ""]
    if e:
        body += ["## Resumo", "", e["summary"]]
        if e.get("topics"):
            body += ["", "## Tópicos", ""] + [f"- **{t['name']}** — {t['detail']}" for t in e["topics"]]
        if e.get("tools"):
            body += ["", "## Ferramentas citadas", ""] + [f"- **{t['name']}**: {t['role']}" for t in e["tools"]]
        body += ["", "## Pontos-chave", ""]
        body += [f"- {p}" for p in e["key_points"]]
        if e.get("how_to_apply"):
            body += ["", "## Como aplicar", "", e["how_to_apply"]]
        if e.get("satellite_take"):
            from .voices import ICON, NAME
            sat = e.get("satellite") or "stella"
            body += ["", f"## {ICON[sat]} {NAME[sat]} diz", "", e["satellite_take"]]
        if item.get("content_type") in ("article", "document") and item.get("raw_content"):
            body += ["", "## Texto integral", "", "<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->", "",
                     _demote_headings(item["raw_content"].strip())]
    else:
        body += ["_Pendente de extração automática. Cole o conteúdo em Notas manuais e rode `/reprocess`._"]
        if item.get("error_code"):
            body += ["", f"Erro: `{item['error_code']}` — {(item.get('error_detail') or '')[:300]}"]
    body += ["", SENTINEL, "", "<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->", ""]
    if manual_notes:
        body += [manual_notes.rstrip(), ""]
    return "\n".join(fm + body)


def _demote_headings(md: str) -> str:
    """Rebaixa os títulos do artigo para que o maior deles vire '###' — abaixo das seções do item (##)."""
    levels = [len(m.group(1)) for m in re.finditer(r"^(#{1,6}) ", md, flags=re.M)]
    if not levels:
        return md
    shift = max(0, 3 - min(levels))
    return re.sub(r"^(#{1,6}) ", lambda m: "#" * min(6, len(m.group(1)) + shift) + " ", md, flags=re.M)


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


def _rel_to_vault(vault_path: str) -> Path:
    """Caminho relativo ao vault; tolera caminhos gravados com um vault_dir antigo (ex.: renomeação da pasta)."""
    p = Path(vault_path)
    try:
        return p.relative_to(settings.vault_dir)
    except ValueError:
        return Path(*p.parts[-2:])  # <subpasta>/<arquivo>


def write_index(items: list[dict]) -> Path:
    """INDEX.md agrupado por tema + páginas temas/<tema>.md. Linha do item: data · plataforma · [título](caminho) · tags · saas/cliente/estudo · triagem."""
    rel_of = lambda it: str(_rel_to_vault(it["vault_path"])) if it.get("vault_path") else ""
    groups = themes.group_by_theme(items)
    lines = ["# Vegapunk — Índice da memória", "",
             "Gerado automaticamente. Itens agrupados por tema; dentro do tema, mais novos primeiro. "
             "Linha: data · plataforma · título · tags · aplicabilidade (saas/cliente/estudo) · triagem.", "",
             "## Mapa de temas", ""] + themes.theme_map_lines(groups) + [""]
    for slug, pairs in groups.items():
        lines += [f"## {themes.label(slug)}", ""]
        for it, e in pairs:
            a = e["applicability"]
            lines.append(
                f"- {it['captured_at'][:10]} · {it['platform']} · [{e['title']}]({rel_of(it)}) · "
                f"`{'` `'.join(e['tags'])}` · {a['saas_pessoal']}/{a['projeto_cliente']}/{a['estudo_geral']} · {it.get('triage_decision') or '—'}"
            )
        lines.append("")
    p = settings.vault_dir / "INDEX.md"
    p.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    themes.write_theme_pages(items, settings.vault_dir, rel_of)
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
