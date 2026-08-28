import logging
import sys

from .bot import build_app, resume_unfinished
from .config import settings
from .db import Database

logging.basicConfig(level=logging.INFO, format='{"t":"%(asctime)s","lvl":"%(levelname)s","src":"%(name)s","msg":"%(message)s"}')
logging.getLogger("httpx").setLevel(logging.WARNING)


def main():
    if not settings.bot_token:
        sys.exit("TELEGRAM_BOT_TOKEN não definido (.env)")
    if not settings.allowed_chat_ids:
        logging.warning("TELEGRAM_ALLOWED_CHAT_IDS vazio: bot RECUSA todos os chats. Mande /id e preencha o .env.")
    grupos = [i for i in settings.allowed_chat_ids if i < 0]
    if grupos and not settings.group_enabled:
        logging.warning("grupos autorizados no .env mas VEGAPUNK_GROUP_ENABLED=false: %s serão ignorados", grupos)
    if grupos and settings.group_enabled and not settings.allowed_user_ids:
        logging.warning("GRUPO LIGADO SEM FILTRO DE PESSOA: qualquer participante de %s gasta sua chave do "
                        "OpenRouter. Preencha TELEGRAM_ALLOWED_USER_IDS.", grupos)
    db = Database(settings.db_path)
    app = build_app(db)

    async def post_init(a):
        await a.bot_data["speakers"].initialize()   # sobe os bots que só falam e confirma a identidade de cada um
        await resume_unfinished(db, a.bot_data["pipeline"])

    async def post_shutdown(a):
        await a.bot_data["speakers"].shutdown()

    app.post_init = post_init
    app.post_shutdown = post_shutdown
    logging.info("Vegapunk online (modelo=%s, whisper=%s)", settings.model, settings.whisper_model)
    app.run_polling(allowed_updates=["message", "callback_query"], drop_pending_updates=False)


if __name__ == "__main__":
    main()
