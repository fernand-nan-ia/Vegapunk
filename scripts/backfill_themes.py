"""Classifica por tema os itens já enriquecidos que ainda não têm `theme` (uma chamada ao modelo para todos) e regenera o vault.
Uso (no container): python scripts/backfill_themes.py [--dry]
"""
import json
import sys

sys.path.insert(0, "src")
from vegapunk import vault  # noqa: E402
from vegapunk.config import settings  # noqa: E402
from vegapunk.db import Database  # noqa: E402
from vegapunk.enrich import _client  # noqa: E402
from vegapunk.themes import THEMES, guess_theme  # noqa: E402

dry = "--dry" in sys.argv
db = Database(settings.db_path)
rows = [dict(r) for r in db.all_with_enrichment()]
todo = [(r, json.loads(r["enrichment"])) for r in rows if json.loads(r["enrichment"]).get("theme") not in THEMES]
print(f"{len(rows)} itens; {len(todo)} sem tema")
if todo and not dry:
    listing = "\n".join(f"{i}. {e['title']} | tags: {', '.join(e['tags'])}" for i, (_, e) in enumerate(todo))
    prompt = ("Classifique cada item em UM tema da lista. Responda só JSON: {\"themes\": [\"slug\", ...]} na mesma ordem.\n"
              "Temas: " + "; ".join(f"{k} = {v[1]} ({v[2]})" for k, v in THEMES.items()) + "\n\nItens:\n" + listing)
    schema = {"type": "object", "additionalProperties": False, "required": ["themes"],
              "properties": {"themes": {"type": "array", "items": {"type": "string", "enum": list(THEMES)}}}}
    resp = _client().chat.completions.create(
        model=settings.model, messages=[{"role": "user", "content": prompt}], temperature=0, max_tokens=4000,
        response_format={"type": "json_schema", "json_schema": {"name": "themes", "strict": True, "schema": schema}})
    raw = resp.choices[0].message.content.strip().strip("`")
    got = json.loads(raw[raw.index("{"):])["themes"]
    if len(got) != len(todo):
        print(f"AVISO: modelo devolveu {len(got)} temas para {len(todo)} itens; faltantes vão pela reserva")
        got += [None] * (len(todo) - len(got))
    print("tokens:", resp.usage.prompt_tokens, "/", resp.usage.completion_tokens)
    for (r, e), t in zip(todo, got):
        e["theme"] = t if t in THEMES else guess_theme(e)
        db.update(r["id"], enrichment=json.dumps(e, ensure_ascii=False))
        print(f"  {e['theme']:32} {e['title'][:70]}")
if not dry:
    items = [dict(r) for r in db.all_with_enrichment()]
    for it in items:
        vault.write_item(it)
    vault.write_index(items)
    vault.git_commit("kb: temas — índice por assunto e páginas temas/")
    print("vault regenerado")
