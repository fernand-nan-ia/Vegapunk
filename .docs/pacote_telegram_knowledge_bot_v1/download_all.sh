#!/usr/bin/env bash
# download_all.sh — baixa fontes não embarcadas do INDICE_DE_FONTES.md
# Uso: bash download_all.sh
set -euo pipefail

DEST="./_fontes_baixadas"
mkdir -p "$DEST"

download() {
  local id="$1" url="$2" out="$3"
  echo "[$id] $url"
  if curl -fsSL --retry 3 --max-time 60 "$url" -o "$DEST/$out"; then
    echo "  -> ok: $DEST/$out"
  else
    echo "  -> FALHOU (registrar no relatório da fase download)" >&2
  fi
}

# F001 — Telegram Bot API (HTML; converter/ler como texto)
download "F001" "https://core.telegram.org/bots/api" "F001_telegram_bot_api.html"

# F002 — Telegram Webhooks guide
download "F002" "https://core.telegram.org/bots/webhooks" "F002_telegram_webhooks.html"

# F003 — yt-dlp README (markdown cru)
download "F003" "https://raw.githubusercontent.com/yt-dlp/yt-dlp/master/README.md" "F003_ytdlp_readme.md"

# F005 — Sidekiq Error Handling wiki (markdown cru)
download "F005" "https://raw.githubusercontent.com/wiki/sidekiq/sidekiq/Error-Handling.md" "F005_sidekiq_error_handling.md"

echo ""
echo "Concluído. F004 (docs.claude.com) e F006/F007 exigem navegação: consultar online durante a fase de validação."
