"""Bot Telegram (polling). Única interface do usuário."""
import asyncio
import logging

from telegram.error import NetworkError
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, filters

from . import satellites, voices
from .chat import Chat
from .config import settings
from .db import Database
from .enrich import EnrichmentError
from .normalize import extract_urls
from .pipeline import Pipeline

log = logging.getLogger("vegapunk.bot")

HELP = ("🧠 <b>Vegapunk</b> — me mande links de YouTube, TikTok, Instagram ou de artigos/páginas web e eu extraio, resumo e guardo no Punk Records (artigos vão por inteiro).\n"
        "Texto sem link é conversa com o Satélite ativo (Stella por padrão); eles consultam o Punk Records antes de responder.\n"
        "<b>Comandos dos Satélites:</b> <code>*help</code> lista o que o Satélite ativo faz aqui; ex.: <code>/lilith *attack usar scraping do Maps</code>, "
        "<code>/pythagoras *dossier precificação</code>, <code>/york *cost</code>.\n\n"
        "<b>Satélites:</b> /stella 🧠 · /shaka 🪖 · /lilith 🏴‍☠️ · /edison 💡 · /pythagoras 📚 · /atlas 🔧 · /york 🍩\n"
        "/quem — quem está acordado · /dormir — ninguém responde texto · /esquecer — apaga o histórico da conversa\n\n"
        "/stats — contagem por estado\n/pending — itens sem triagem ou com falha\n"
        "/reprocess &lt;id&gt; — tenta de novo um item com falha\n/id — mostra o id deste chat")
TG_MAX = 4000


def chunks(text: str, size: int = TG_MAX) -> list[str]:
    out = []
    while len(text) > size:
        cut = text.rfind("\n", 0, size)
        cut = cut if cut > size // 2 else size
        out.append(text[:cut]); text = text[cut:].lstrip("\n")
    return out + [text]


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
        """Mensagens longas vão em partes (nunca cortadas); o teclado de triagem vai na última."""
        try:
            parts = chunks(text)
            for i, part in enumerate(parts):
                last = i == len(parts) - 1
                await app.bot.send_message(chat_id, part, parse_mode=ParseMode.HTML,
                                           reply_to_message_id=reply_to if i == 0 else None,
                                           reply_markup=keyboard(item_id) if (item_id and last) else None)
        except Exception:
            log.exception("falha ao notificar chat=%s", chat_id)

    pipeline = Pipeline(db, notify)
    app.bot_data["pipeline"] = pipeline
    chat = Chat(db)
    app.bot_data["chat"] = chat

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

    # ── Satélites ─────────────────────────────────────────
    def make_wake(sat_id: str):
        async def cmd_wake(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
            if not allowed(update):
                return
            try:
                sat = chat.wake(update.effective_chat.id, sat_id)
            except Exception:
                log.exception("falha ao carregar satélite %s", sat_id)
                await update.message.reply_text(f"Não consegui acordar {sat_id} (veja os logs).")
                return
            if ctx.args:  # /lilith <mensagem> → acorda e já responde
                await talk(update, " ".join(ctx.args))
            else:
                await update.message.reply_text(f"{sat.icon} <b>{sat.name}</b> acordou.\n<i>{sat.role}</i>\n\nPode falar.",
                                                parse_mode=ParseMode.HTML)
        return cmd_wake

    async def cmd_quem(update: Update, _):
        if not allowed(update):
            return
        sat_id = chat.active(update.effective_chat.id)
        if not sat_id:
            await update.message.reply_text("Ninguém acordado. Texto sem link vai para Stella; ou chame /shaka, /lilith…")
            return
        sat = satellites.load(sat_id)
        await update.message.reply_text(f"{sat.icon} {sat.name} está acordado(a). /dormir para silenciar, /esquecer para zerar o histórico.")

    async def cmd_dormir(update: Update, _):
        if not allowed(update):
            return
        chat.sleep(update.effective_chat.id)
        await update.message.reply_text("Todos dormindo. Texto sem link volta a acordar Stella; links continuam sendo capturados.")

    async def cmd_esquecer(update: Update, _):
        if not allowed(update):
            return
        n = chat.forget(update.effective_chat.id, chat.active(update.effective_chat.id))
        await update.message.reply_text(f"Histórico apagado ({n} mensagens). O diário em squads/vegapunk/memory/ não muda.")

    async def cmd_conta(update: Update, _):
        if not allowed(update):
            return
        rows = chat.cost_rows(update.effective_chat.id)
        if not rows:
            await update.message.reply_text("Nenhuma conversa ainda. York aprova: custo zero.")
            return
        await update.message.reply_text("🍩 tokens por Satélite (respostas · in · out):\n" +
                                        "\n".join(f"{s}: {n} · {i} · {o}" for s, n, i, o in rows))

    async def talk(update: Update, text: str):
        msg = update.message
        await msg.chat.send_action("typing")
        try:
            sat, answer = await asyncio.to_thread(chat.reply, msg.chat_id, text)
        except EnrichmentError as e:
            await msg.reply_text(f"⚠️ {e.code}: {e.detail[:300]}")
            return
        except Exception:
            log.exception("chat falhou")
            await msg.reply_text("⚠️ Falha na conversa (veja os logs).")
            return
        for part in chunks(f"{sat.icon} {answer}"):
            await msg.reply_text(part)

    async def on_message(update: Update, _):
        if not allowed(update):
            log.info("chat não autorizado: %s", update.effective_chat.id)
            return
        msg = update.message
        urls = extract_urls(msg.text or msg.caption or "")
        if not urls:
            await talk(update, msg.text or msg.caption or "")
            return
        sat = voices.pick()  # quem anuncia é quem apresenta o resultado
        for url in urls:
            item_id = db.create_item(url, msg.chat_id, msg.message_id, satellite=sat)
            asyncio.create_task(pipeline.run(item_id))
        await msg.reply_text(voices.capture_line(len(urls), sat=sat), parse_mode=ParseMode.HTML)

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

    async def on_error(update, context):
        err = context.error
        if isinstance(err, NetworkError):
            log.warning("rede Telegram: %s (polling continua)", err)
        else:
            log.error("erro não tratado", exc_info=err)

    app.add_error_handler(on_error)
    app.add_handler(CommandHandler("id", cmd_id))
    app.add_handler(CommandHandler(["start", "help"], cmd_start))
    app.add_handler(CommandHandler("stats", cmd_stats))
    app.add_handler(CommandHandler("pending", cmd_pending))
    app.add_handler(CommandHandler("reprocess", cmd_reprocess))
    for sat_id in satellites.IDS:
        app.add_handler(CommandHandler([sat_id] + (["vegapunk"] if sat_id == "stella" else []), make_wake(sat_id)))
    app.add_handler(CommandHandler("quem", cmd_quem))
    app.add_handler(CommandHandler("dormir", cmd_dormir))
    app.add_handler(CommandHandler("esquecer", cmd_esquecer))
    app.add_handler(CommandHandler("conta", cmd_conta))
    app.add_handler(CallbackQueryHandler(on_callback, pattern=r"^triage:"))
    app.add_handler(MessageHandler(filters.TEXT | filters.CAPTION, on_message))
    return app


async def resume_unfinished(db: Database, pipeline: Pipeline):
    """Itens que ficaram no meio (bot desligado) continuam de onde pararam."""
    for row in db.by_status("captured", "normalized", "extracted"):
        log.info("retomando item %s (%s)", row["id"], row["status"])
        asyncio.create_task(pipeline.run(row["id"]))
