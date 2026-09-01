"""Bot Telegram (polling). Única interface do usuário."""
import asyncio
import logging
import re
from pathlib import Path

from telegram.error import NetworkError
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, filters

from . import router, satellites, voices
from .chat import Chat
from .config import settings
from .db import Database
from .enrich import EnrichmentError
from .extract import DOC_EXTS
from .normalize import extract_urls
from .pipeline import Pipeline
from .speakers import Speakers

log = logging.getLogger("vegapunk.bot")

HELP = ("🧠 <b>Vegapunk</b> — me mande links de YouTube, TikTok, Instagram, artigos/páginas web ou <b>arquivos</b> (PDF, Word, planilha, txt/md/csv até 20 MB) "
        "e eu extraio, resumo e guardo no Punk Records (artigos e documentos vão por inteiro).\n"
        "Texto sem link é conversa com o Satélite ativo (Stella por padrão); eles consultam o Punk Records antes de responder.\n"
        "<b>Comandos dos Satélites:</b> <code>*help</code> lista o que o Satélite ativo faz aqui; ex.: <code>/lilith *attack usar scraping do Maps</code>, "
        "<code>/pythagoras *dossier precificação</code>, <code>/york *cost</code>.\n\n"
        "<b>Satélites:</b> /stella 🧠 · /shaka 🪖 · /lilith 🏴‍☠️ · /edison 💡 · /pythagoras 📚 · /atlas 🔧 · /york 🍩\n"
        "/quem — quem está acordado · /dormir — ninguém responde texto · /esquecer — apaga o histórico da conversa\n\n"
        "/stats — contagem por estado\n/pending — itens sem triagem ou com falha\n"
        "/reprocess &lt;id&gt; — tenta de novo um item com falha\n/id — mostra o id deste chat")
TG_MAX = 4000
def triagem_linha(titulo: str | None = None) -> str:
    """Identifica o item: com vários chegando fora de ordem, botões idênticos viram loteria."""
    return f"🧠 <b>{(titulo or 'este item')[:60]}</b> — onde guardar?"
DOC_MAX_BYTES = 20 * 1024 * 1024   # teto do Bot API para download


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


def is_allowed(chat_id: int, user_id: int | None = None, from_bot: bool = False) -> bool:
    """Porteiro do dinheiro: nada chega ao OpenRouter sem passar por aqui. Falha SEMPRE fechada.

    Cinco portas, na ordem do mais barato para o mais específico:
      0. remetente é um bot → recusa (TRAVA ANTI-LOOP: no grupo há 7 bots; um respondendo ao outro
         seria uma conversa infinita paga por token. Vem antes de tudo, inclusive da lista de chats.)
      1. sem lista de chats no .env → recusa tudo (antes aceitava tudo: era a única falha aberta do sistema)
      2. chat fora da lista → recusa
      3. chat de grupo (id negativo) com VEGAPUNK_GROUP_ENABLED=false → recusa
      4. TELEGRAM_ALLOWED_USER_IDS preenchido e o remetente fora dela → recusa

    `/id` NÃO passa por aqui de propósito: é o caminho de bootstrap (instalar → /id → preencher o .env).
    """
    if from_bot:
        log.debug("mensagem de bot em %s: ignorada (trava anti-loop)", chat_id)
        return False
    if not settings.allowed_chat_ids:
        log.debug("TELEGRAM_ALLOWED_CHAT_IDS vazio: recusando. (o aviso alto é no arranque, aqui rodaria a cada mensagem)")
        return False
    if chat_id not in settings.allowed_chat_ids:
        return False
    if chat_id < 0 and not settings.group_enabled:
        log.info("grupo %s está no .env mas VEGAPUNK_GROUP_ENABLED=false: ignorando", chat_id)
        return False
    if settings.allowed_user_ids and user_id not in settings.allowed_user_ids:
        log.info("usuário %s fora de TELEGRAM_ALLOWED_USER_IDS em %s: ignorando", user_id, chat_id)
        return False
    return True


def mencoes_explicitas(text: str, usernames: dict[str, str]) -> list[str]:
    """Camada 1: `@vegapunkklilithbot` no texto → ["lilith"], na ordem em que aparecem.

    É o caminho de escape determinístico — tem de funcionar com o roteador fora do ar E com o bot
    daquele Satélite fora do ar. `usernames` só conhece quem respondeu ao `get_me` no arranque, e em
    2026-08-28 a Lilith não respondeu (TimedOut): sem o casamento por padrão abaixo, `@…lilith…bot`
    cairia no vazio e o grupo ignoraria o Fernando em silêncio.
    """
    baixo = (text or "").lower()
    achados: list[tuple[int, str]] = []
    for sat in satellites.IDS:
        u = (usernames.get(sat) or "").lower()
        pos = baixo.find("@" + u) if u else -1
        if pos < 0:
            m = re.search(r"@\w*" + re.escape(sat) + r"\w*", baixo)   # @qualquercoisa<id>qualquercoisa
            pos = m.start() if m else -1
        if pos >= 0:
            achados.append((pos, sat))
    return [sat for _, sat in sorted(achados)]


async def notificar(speakers: Speakers, chat_id: int, text: str, reply_to: int | None = None,
                    item_id: str | None = None, sat: str | None = None, titulo: str | None = None):
    """Fala do pipeline (captura, duplicata, falha, resumo). `sat` = o Satélite dono do item.

    No GRUPO o dono fala pela própria boca. O teclado de triagem, porém, tem de sair pelo LEITOR: o
    clique de um botão volta para o bot que ENVIOU a mensagem, e só o leitor tem handler de callback —
    teclado mandado pela Lilith seria um botão morto. Daí a mensagem separada.
    Na DM nada muda: uma mensagem só, com o teclado na última parte.
    """
    parts = chunks(text)
    dono = sat or satellites.DEFAULT
    leitor = speakers.fallback
    if speakers.bot_for(dono, chat_id) is leitor:
        for i, part in enumerate(parts):            # DM, ou dono sem bot próprio: como sempre
            last = i == len(parts) - 1
            await leitor.send_message(chat_id, part, parse_mode=ParseMode.HTML,
                                      reply_to_message_id=reply_to if i == 0 else None,
                                      reply_markup=keyboard(item_id) if (item_id and last) else None)
        return
    await speakers.say_all(dono, chat_id, parts, reply_to=reply_to)
    if item_id:
        await leitor.send_message(chat_id, triagem_linha(titulo), parse_mode=ParseMode.HTML,
                                  reply_markup=keyboard(item_id))


async def responder_no_grupo(chat, speakers: Speakers, chat_id: int, text: str,
                             message_id: int | None = None) -> list[str]:
    """Cascata do PRD §4.1 no grupo, camadas 1 a 4. Devolve quem de fato respondeu.

    Vive fora de `build_app` para ser testável: a ligação entre decidir e responder era o buraco que
    a Lilith apontou duas vezes (Stories 1b e 1c).
    """
    sat_ativo, idade = chat.active_age(chat_id)
    recentes = None
    if sat_ativo:
        quem = voices.NAME.get(sat_ativo, sat_ativo)
        recentes = [f"{'Fernando' if m['role'] == 'user' else quem}: {m['content'][:200]}"
                    for m in chat.history(chat_id, sat_ativo, limit=3)]   # com atribuição: sem ela o
                    # roteador não sabe de quem "e isso aí?" é continuação — justo o que a janela serve
    decisao = router.decide(text, explicitos=mencoes_explicitas(text, speakers.usernames),
                            ativo=sat_ativo, idade_do_ativo=idade, recent=recentes)
    if not decisao:
        log.info("grupo %s: ninguém respondeu (%s)", chat_id, decisao.reason)
        return []

    responderam: list[str] = []
    for sat_id in decisao.satellites:
        if not router.pode_responder():          # teto da camada CARA, antes de gastar
            log.warning("grupo %s: teto de respostas atingido; %s ficou de fora", chat_id, sat_id)
            if not responderam:
                await speakers.fallback.send_message(
                    chat_id, "🍩 York: teto de respostas atingido. Espere um minuto — é dinheiro seu.")
            break
        try:
            sat, answer = await asyncio.to_thread(chat.reply, chat_id, text, sat_id)
            await responder(speakers, sat, answer, chat_id, message_id if not responderam else None)
            responderam.append(sat_id)
        except EnrichmentError as e:
            log.warning("grupo %s: %s falhou (%s: %s)", chat_id, sat_id, e.code, e.detail[:120])
        except Exception:
            log.exception("grupo %s: %s falhou ao responder", chat_id, sat_id)
    if responderam:
        chat.wake(chat_id, responderam[0])       # a janela segue quem VOCÊ chamou primeiro, não quem falou por último
    return responderam


async def responder(speakers: Speakers, sat, answer: str, chat_id: int, reply_to: int | None = None):
    """Manda a resposta pela boca do Satélite que respondeu.

    Vive fora de `build_app` para poder ser testada: era o critério principal da Story 1b
    ("a resposta da Lilith aparece com o nome dela") e não tinha prova nenhuma.
    """
    await speakers.say_all(sat.id, chat_id, chunks(f"{sat.icon} {answer}"), reply_to=reply_to, parse_mode=None)


def build_app(db: Database) -> Application:
    app = Application.builder().token(settings.bot_token).build()
    speakers = Speakers(app.bot)
    app.bot_data["speakers"] = speakers

    async def notify(chat_id: int, text: str, reply_to: int | None = None,
                     item_id: str | None = None, sat: str | None = None, titulo: str | None = None):
        try:
            await notificar(speakers, chat_id, text, reply_to, item_id, sat, titulo)
        except Exception:
            log.exception("falha ao notificar chat=%s", chat_id)

    pipeline = Pipeline(db, notify)
    app.bot_data["pipeline"] = pipeline
    chat = Chat(db)
    app.bot_data["chat"] = chat

    def allowed(update: Update) -> bool:
        chat, user = update.effective_chat, update.effective_user
        return bool(chat) and is_allowed(chat.id, user.id if user else None, bool(user and user.is_bot))

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
        try:
            # no grupo sai pelo bot do próprio Satélite (nome e ícone dele); na DM, pelo bot de sempre
            await responder(speakers, sat, answer, msg.chat_id, msg.message_id)
        except Exception:
            # a resposta já foi paga em token: não pode sumir em silêncio
            log.exception("falha ao enviar a resposta de %s em %s", sat.id, msg.chat_id)
            try:
                await msg.reply_text(f"{sat.icon} (não consegui enviar a resposta — veja os logs)")
            except Exception:
                log.exception("nem o aviso de falha saiu")

    async def falar_no_grupo(update: Update, text: str):
        """Camada 0 já passou (`allowed`); as camadas 1 a 4 vivem em `responder_no_grupo`, testável."""
        msg = update.message
        await responder_no_grupo(chat, speakers, msg.chat_id, text, msg.message_id)

    async def on_message(update: Update, _):
        if not allowed(update):
            log.info("chat não autorizado: %s", update.effective_chat.id)
            return
        msg = update.message
        urls = extract_urls(msg.text or msg.caption or "")
        if not urls:
            texto = msg.text or msg.caption or ""
            # grupo passa pela cascata (só responde quem foi chamado); DM continua como sempre
            await (falar_no_grupo(update, texto) if msg.chat_id < 0 else talk(update, texto))
            return
        sat = voices.pick()  # quem anuncia é quem apresenta o resultado
        for url in urls:
            item_id = db.create_item(url, msg.chat_id, msg.message_id, satellite=sat)
            asyncio.create_task(pipeline.run(item_id))
        await speakers.say_all(sat, msg.chat_id, [voices.capture_line(len(urls), sat=sat)],
                               reply_to=msg.message_id)

    async def on_document(update: Update, _):
        """Arquivo anexado (PDF, DOCX, XLSX, TXT/MD/CSV): baixa para tmp/documents e entra no pipeline como platform=document."""
        if not allowed(update):
            return
        msg = update.message
        doc = msg.document
        ext = Path(doc.file_name or "").suffix.lower()
        if ext not in DOC_EXTS:
            await msg.reply_text(f"📎 Tipo não suportado ({ext or 'sem extensão'}). Aceito: {', '.join(sorted(DOC_EXTS))}.")
            return
        if doc.file_size and doc.file_size > DOC_MAX_BYTES:
            await msg.reply_text("📎 Arquivo acima de 20 MB — o Telegram não deixa o bot baixar. Divida ou mande um link.")
            return
        sat = voices.pick()
        dest = settings.tmp_dir / "documents" / f"{doc.file_unique_id}{ext}"
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            tg_file = await doc.get_file()
            await tg_file.download_to_drive(dest)
        except Exception:
            log.exception("download de documento falhou")
            await msg.reply_text("📎 Não consegui baixar o arquivo do Telegram. Tente de novo.")
            return
        n = 1
        item_id = db.create_item(f"file://{dest}", msg.chat_id, msg.message_id, satellite=sat)
        asyncio.create_task(pipeline.run(item_id))
        for url in extract_urls(msg.caption or ""):   # links na legenda do arquivo também contam
            asyncio.create_task(pipeline.run(db.create_item(url, msg.chat_id, msg.message_id, satellite=sat)))
            n += 1
        await speakers.say_all(sat, msg.chat_id, [voices.capture_line(n, sat=sat, noun="arquivo" if n == 1 else "item")],
                               reply_to=msg.message_id)

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
    app.add_handler(MessageHandler(filters.Document.ALL, on_document))      # antes do texto: documento com legenda cai aqui
    app.add_handler(MessageHandler(filters.TEXT | filters.CAPTION, on_message))
    return app


async def resume_unfinished(db: Database, pipeline: Pipeline):
    """Itens que ficaram no meio (bot desligado) continuam de onde pararam."""
    for row in db.by_status("captured", "normalized", "extracted"):
        log.info("retomando item %s (%s)", row["id"], row["status"])
        asyncio.create_task(pipeline.run(row["id"]))
