import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ROOT = Path(os.environ.get("VEGAPUNK_ROOT", os.getcwd())).resolve()


def _ids(raw: str) -> set[int]:
    return {int(x) for x in raw.replace(";", ",").split(",") if x.strip()}


@dataclass
class Settings:
    bot_token: str = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    allowed_chat_ids: set[int] = field(default_factory=lambda: _ids(os.environ.get("TELEGRAM_ALLOWED_CHAT_IDS", "")))
    # Porteiro do dinheiro: nada chega ao OpenRouter sem passar por estes três (ver bot.is_allowed).
    allowed_user_ids: set[int] = field(default_factory=lambda: _ids(os.environ.get("TELEGRAM_ALLOWED_USER_IDS", "")))
    group_enabled: bool = os.environ.get("VEGAPUNK_GROUP_ENABLED", "false").lower() == "true"   # grupo só responde quando ligado de propósito
    openrouter_api_key: str = os.environ.get("OPENROUTER_API_KEY", "")
    model: str = os.environ.get("VEGAPUNK_MODEL", "google/gemini-3.7-flash")
    router_model: str = os.environ.get("VEGAPUNK_ROUTER_MODEL", "")   # vazio = usa `model`; roteador do grupo (router.py)
    whisper_model: str = os.environ.get("VEGAPUNK_WHISPER_MODEL", "small")
    git_commit: bool = os.environ.get("VEGAPUNK_GIT_COMMIT", "true").lower() == "true"
    git_push: bool = os.environ.get("VEGAPUNK_GIT_PUSH", "false").lower() == "true"
    cookies_file: str = os.environ.get("VEGAPUNK_COOKIES_FILE", "").split("#")[0].strip()
    db_path: Path = ROOT / os.environ.get("VEGAPUNK_DB_PATH", "data/vegapunk.db")
    vault_dir: Path = ROOT / os.environ.get("VEGAPUNK_VAULT_DIR", "punk_records")
    tmp_dir: Path = ROOT / "tmp"
    max_transcript_chars: int = 60_000
    max_document_chars: int = 150_000   # artigos/documentos guardados por inteiro (uma lei cabe)


settings = Settings()
