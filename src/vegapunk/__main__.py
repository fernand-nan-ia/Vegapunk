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
        logging.warning("TELEGRAM_ALLOWED_CHAT_IDS vazio: bot aceita qualquer chat. Mande /id e preencha o .env.")
    db = Database(settings.db_path)
    app = build_app(db)

    async def post_init(a):
        await resume_unfinished(db, a.bot_data["pipeline"])

    app.post_init = post_init
    logging.info("Vegapunk online (modelo=%s, whisper=%s)", settings.model, settings.whisper_model)
    app.run_polling(allowed_updates=["message", "callback_query"], drop_pending_updates=False)


if __name__ == "__main__":
    main()
