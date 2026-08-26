"""Bot Telegram (polling). Única interface do usuário."""
import asyncio
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, filters

from .config import settings
from .db import Database
from .normalize import extract_urls
from .pipeline import Pipeline

log = logging.getLogger("vegapunk.bot")

HELP = ("🧠 <b>Vegapunk</b> — me mande links de YouTube, TikTok ou Instagram e eu extraio, resumo e guardo na memória.\n\n"
        "/stats — contagem por estado\n/pending — itens sem triagem ou com falha\n"
        "/reprocess &lt;id&gt; — tenta de novo um item com falha\n/id — mostra o id deste chat")


def keyboard(item_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📁 Arquivar", callback_data=f"triage:{item_id}:archive"),
         InlineKeyboardButton("🚀 SaaS", callback_data=f"triage:{item_id}:apply_saas")],
        [InlineKeyboardButton("👤 Cliente", callback_data=f"triage:{item_id}:apply_client"),
         InlineKeyboardButton("🗑 Descartar", callback_data=f"triage:{item_id}:discard")],
    ])


def build_app(db: Database) -> Application:
    app = Application.builder().token(settings.bot_token).build()

    async def notify(chat_id: int, text: str, reply_to: int | None = None, item_id: str | None = None):
        try:
            await app.bot.send_message(chat_id, text, parse_mode=ParseMode.HTML,
                                       reply_to_message_id=reply_to,
                                       reply_markup=keyboard(item_id) if item_id else None)
        except Exception:
            log.exception("falha ao notificar chat=%s", chat_id)

    pipeline = Pipeline(db, notify)
    app.bot_data["pipeline"] = pipeline

    def allowed(update: Update) -> bool:
        chat = update.effective_chat
        return bool(chat) and (not settings.allowed_chat_ids or chat.id in settings.allowed_chat_ids)

    async def cmd_id(update: Update, _):
        await update.message.reply_text(f"chat_id: {update.effective_chat.id}")

    async def cmd_start(update: Update, _):
        if not allowed(update):
            return
        await update.message.reply_text(HELP, parse_mode=ParseMode.HTML)

    async def cmd_stats(update: Update, _):
        if not allowed(update):
            return
        rows = db.stats() or [("(vazio)", 0)]
        await update.message.reply_text("\n".join(f"{s}: {c}" for s, c in rows))

    async def cmd_pending(update: Update, _):
        if not allowed(update):
            return
        rows = db.by_status("enriched", "extraction_failed", "enrichment_failed", "pending_manual")[:20]
        if not rows:
            await update.message.reply_text("Nada pendente. 🎉")
            return
        await update.message.reply_text("\n".join(f"{r['id'][:8]} · {r['status']} · {(r['title'] or r['raw_url'])[:50]}" for r in rows))

    async def cmd_reprocess(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        if not allowed(update):
            return
        if not ctx.args:
            await update.message.reply_text("Uso: /reprocess <id ou prefixo>")
            return
        prefix = ctx.args[0]
        row = db.conn.execute("SELECT id FROM knowledge_items WHERE id LIKE ?", (prefix + "%",)).fetchone()
        await update.message.reply_text(await pipeline.reprocess(row["id"]) if row else "Item não encontrado")

    async def on_message(update: Update, _):
        if not allowed(update):
            log.info("chat não autorizado: %s", update.effective_chat.id)
            return
        msg = update.message
        urls = extract_urls(msg.text or msg.caption or "")
        if not urls:
            await msg.reply_text("Me envie um link de YouTube, TikTok ou Instagram.")
            return
        for url in urls:
            item_id = db.create_item(url, msg.chat_id, msg.message_id)
            asyncio.create_task(pipeline.run(item_id))
        await msg.reply_text(f"✅ Capturado ({len(urls)}). Processando...")

    async def on_callback(update: Update, _):
        q = update.callback_query
        if not allowed(update):
            await q.answer()
            return
        try:
            _, item_id, decision = q.data.split(":")
        except ValueError:
            await q.answer("callback inválido")
            return
        result = await pipeline.triage(item_id, decision)
        await q.answer(result)
        if result.startswith("✔"):
            try:
                await q.edit_message_text(q.message.text_html + f"\n\n{result}", parse_mode=ParseMode.HTML, reply_markup=None)
            except Exception:
                log.exception("edit_message falhou")

    app.add_handler(CommandHandler("id", cmd_id))
    app.add_handler(CommandHandler(["start", "help"], cmd_start))
    app.add_handler(CommandHandler("stats", cmd_stats))
    app.add_handler(CommandHandler("pending", cmd_pending))
    app.add_handler(CommandHandler("reprocess", cmd_reprocess))
    app.add_handler(CallbackQueryHandler(on_callback, pattern=r"^triage:"))
    app.add_handler(MessageHandler(filters.TEXT | filters.CAPTION, on_message))
    return app


async def resume_unfinished(db: Database, pipeline: Pipeline):
    """Itens que ficaram no meio (bot desligado) continuam de onde pararam."""
    for row in db.by_status("captured", "normalized", "extracted"):
        log.info("retomando item %s (%s)", row["id"], row["status"])
        asyncio.create_task(pipeline.run(row["id"]))
