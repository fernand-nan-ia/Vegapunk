"""Alimentar o Punk Records a partir do Claude Code — sem gastar OpenRouter.

Fluxo em dois passos (o resumo é feito pela sessão do Claude Code, não pelo modelo do OpenRouter):

  1. python scripts/capture.py extract <url|arquivo> [--sat york]
       → cria o item, normaliza, extrai (yt-dlp/Whisper/trafilatura/PDF… tudo local) e grava
         tmp/capture/<id>.md com metadados + TEXTO + o contrato do JSON de enriquecimento.
  2. (o Claude Code lê esse arquivo e escreve tmp/capture/<id>.json seguindo o contrato)
  3. python scripts/capture.py enrich <id> [--quiet]
       → valida o JSON com o MESMO Pydantic do bot, grava (model_used=claude-code), gera o .md,
         o índice por tema, commit e — salvo --quiet — avisa no Telegram na voz do Satélite dono.

  python scripts/capture.py auto <url|arquivo>   → pipeline completo via OpenRouter (como o Telegram)
  python scripts/capture.py pending              → itens extraídos à espera do passo 2

Rodar dentro do container (tem yt-dlp/ffmpeg/Whisper): docker compose exec -T vegapunk python scripts/capture.py …
"""
import argparse
import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, "src")
from vegapunk import satellites, vault, voices  # noqa: E402
from vegapunk.config import settings  # noqa: E402
from vegapunk.db import Database, now  # noqa: E402
from vegapunk.enrich import Enrichment, SYSTEM, VOICE_RULES, parse_output  # noqa: E402
from vegapunk.normalize import normalize  # noqa: E402
from vegapunk.pipeline import Pipeline, format_summary  # noqa: E402

CAP_DIR = settings.tmp_dir / "capture"


def _chat_id() -> int:
    ids = sorted(settings.allowed_chat_ids)
    if not ids:
        sys.exit("TELEGRAM_ALLOWED_CHAT_IDS vazio: não sei para quem avisar")
    return ids[0]


def _notifier(quiet: bool):
    if quiet:
        async def silent(cid, text, reply_to=None, item_id=None):
            print("(quiet)", text[:100].replace("\n", " | "))
        return silent
    from telegram import Bot
    from telegram.constants import ParseMode
    from vegapunk.bot import chunks, keyboard
    bot = Bot(settings.bot_token)

    async def notify(cid, text, reply_to=None, item_id=None):
        parts = chunks(text)
        for i, part in enumerate(parts):
            await bot.send_message(cid, part, parse_mode=ParseMode.HTML,
                                   reply_markup=keyboard(item_id) if (item_id and i == len(parts) - 1) else None)
    return notify


def _source(arg: str) -> str:
    p = Path(arg).expanduser()
    return f"file://{p.resolve()}" if p.exists() else arg


def cmd_extract(args):
    db = Database(settings.db_path)
    sat = args.sat or voices.pick()
    item_id = db.create_item(_source(args.source), _chat_id(), 0, satellite=sat)
    p = Pipeline(db, _notifier(quiet=True))

    async def run():
        i = await p.step_normalize(item_id)
        if i is None:
            return None
        return item_id if await p.step_extract(item_id) else None
    ok = asyncio.run(run())
    item = db.get(item_id)
    if not ok:
        sys.exit(f"não extraído: status={item['status']} {item['error_code'] or ''} {(item['error_detail'] or '')[:200]}")
    CAP_DIR.mkdir(parents=True, exist_ok=True)
    out = CAP_DIR / f"{item_id[:8]}.md"
    contract = json.dumps(Enrichment.model_json_schema(), ensure_ascii=False, indent=1)
    out.write_text(
        f"# Captura {item_id[:8]} — Satélite dono: {sat}\n\n"
        f"PLATAFORMA: {item['platform']}\nTÍTULO ORIGINAL: {item['title']}\nCANAL/AUTOR: {item['channel']}\n"
        f"DURAÇÃO (s): {item['duration'] or '?'}\nTIPO DE TEXTO: {item['content_type']}\nURL: {item['canonical_url']}\n\n"
        f"DESCRIÇÃO/LEGENDA:\n{item['description'] or '(vazia)'}\n\n"
        f"=== INSTRUÇÕES DE ENRIQUECIMENTO (as mesmas do bot) ===\n{SYSTEM}\n\n{VOICE_RULES}\n\n"
        f"SATÉLITE JÁ ESCOLHIDO: {sat} — preencha satellite = \"{sat}\" e escreva satellite_take na voz dele.\n\n"
        f"=== CONTRATO JSON (escrever em {CAP_DIR / (item_id[:8] + '.json')}) ===\n{contract}\n\n"
        f"=== TEXTO ({len(item['raw_content'])} chars) ===\n{item['raw_content']}\n", encoding="utf-8")
    print(f"extraído: {item_id[:8]} · {item['platform']} · {item['content_type']} · {len(item['raw_content'])} chars · dono: {sat}")
    print(f"leia: {out}\nescreva: {CAP_DIR / (item_id[:8] + '.json')}\ndepois: python scripts/capture.py enrich {item_id[:8]}")


def cmd_enrich(args):
    db = Database(settings.db_path)
    row = db.conn.execute("SELECT id FROM knowledge_items WHERE id LIKE ?", (args.id + "%",)).fetchone()
    if not row:
        sys.exit("item não encontrado")
    item_id = row["id"]
    item = db.get(item_id)
    if item["status"] != "extracted":
        sys.exit(f"status {item['status']}: só itens 'extracted' recebem enriquecimento manual")
    jpath = Path(args.json) if args.json else CAP_DIR / f"{item_id[:8]}.json"
    if not jpath.exists():
        sys.exit(f"JSON não encontrado: {jpath}")
    e = parse_output(jpath.read_text(encoding="utf-8"))   # mesma validação Pydantic do bot
    if item["satellite"] and e.satellite != item["satellite"]:
        e.satellite = item["satellite"]
    db.transition_to(item_id, "enriched", "claude_code", {"input_tokens": 0, "output_tokens": 0, "model": "claude-code"},
                     enrichment=e.model_dump_json(), enriched_at=now(), model_used="claude-code", error_code=None, error_detail=None)
    p = Pipeline(db, _notifier(args.quiet))
    asyncio.run(p.step_persist(item_id))
    it = db.get(item_id)
    print(f"guardado: {it['vault_path']}\n\n{format_summary(json.loads(it['enrichment']), it['satellite'])[:600]}")
    for f in (jpath, CAP_DIR / f"{item_id[:8]}.md"):
        f.unlink(missing_ok=True)


def cmd_auto(args):
    db = Database(settings.db_path)
    sat = args.sat or voices.pick()
    item_id = db.create_item(_source(args.source), _chat_id(), 0, satellite=sat)
    asyncio.run(Pipeline(db, _notifier(args.quiet)).run(item_id))
    it = db.get(item_id)
    print(f"{it['status']} · {it['platform']} · {it['vault_path'] or it['error_detail']}")


def cmd_pending(_args):
    db = Database(settings.db_path)
    rows = db.conn.execute("SELECT substr(id,1,8) id, platform, satellite, title FROM knowledge_items WHERE status='extracted' ORDER BY created_at").fetchall()
    for r in rows:
        print(f"{r['id']} · {r['platform']} · dono {r['satellite']} · {r['title'][:70]}")
    print(f"{len(rows)} à espera de enriquecimento")


ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
sub = ap.add_subparsers(dest="cmd", required=True)
s1 = sub.add_parser("extract"); s1.add_argument("source"); s1.add_argument("--sat", choices=satellites.IDS); s1.set_defaults(fn=cmd_extract)
s2 = sub.add_parser("enrich"); s2.add_argument("id"); s2.add_argument("--json"); s2.add_argument("--quiet", action="store_true"); s2.set_defaults(fn=cmd_enrich)
s3 = sub.add_parser("auto"); s3.add_argument("source"); s3.add_argument("--sat", choices=satellites.IDS); s3.add_argument("--quiet", action="store_true"); s3.set_defaults(fn=cmd_auto)
s4 = sub.add_parser("pending"); s4.set_defaults(fn=cmd_pending)
a = ap.parse_args()
a.fn(a)
