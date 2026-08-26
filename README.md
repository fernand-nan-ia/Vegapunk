# 🧠 Vegapunk

Bot pessoal de Telegram que transforma links (YouTube, TikTok, Instagram) em memória estruturada em Markdown,
consumível pelo Claude Code via skill `/vegapunk`.

```
link no Telegram → extrai texto (legenda ou áudio→Whisper) → Claude resume/classifica → knowledge/*.md → git → botões de triagem
```

## Setup (uma vez)

1. Crie o bot no [@BotFather](https://t.me/BotFather) e copie o token.
2. `cp .env.example .env` e preencha `TELEGRAM_BOT_TOKEN` e `ANTHROPIC_API_KEY`.
3. `docker compose up -d --build` (a 1ª build baixa ffmpeg + libs; o modelo Whisper baixa no 1º vídeo sem legenda).
4. Mande `/id` ao bot, cole o número em `TELEGRAM_ALLOWED_CHAT_IDS` no `.env`, e `docker compose restart`.
5. Mande um link. 🎉

Sem Docker (dev): `python3 -m venv .venv && .venv/bin/pip install -e ".[dev]" && .venv/bin/python -m vegapunk` (precisa de `ffmpeg` e `yt-dlp` no PATH).

## Comandos do bot

| Comando | Faz |
|---|---|
| link(s) na mensagem | captura e processa cada um |
| botões 📁 🚀 👤 🗑 | triagem: arquivar / aplicar no SaaS / aplicar no cliente / descartar |
| `/pending` | itens sem triagem ou com falha |
| `/reprocess <id>` | tenta de novo (ou processa notas manuais coladas no `.md` em `_pending/`) |
| `/stats` | contagem por estado |

## Onde ficam as coisas

- `knowledge/` — o vault (versionado). `knowledge/INDEX.md` é o sumário.
- `data/vegapunk.db` — SQLite, fonte de verdade (não versionado). O vault é regenerável a partir dele.
- `whisper-cache/` — modelo Whisper (não versionado).

## Git

Cada item gera um commit local em `knowledge/`. Push é manual por padrão (`git push`); ligue `VEGAPUNK_GIT_PUSH=true`
e monte `~/.ssh` no compose para push automático.

## Usar no Claude Code

Em qualquer projeto: `/vegapunk <pergunta ou tema>`. A skill lê `knowledge/INDEX.md`, abre os itens relevantes e responde/deduz com base neles.

## Operação

- Bot desligado? Sem problema: o Telegram guarda mensagens por até 24h; ao subir, o bot processa a fila e retoma itens que ficaram no meio.
- Instagram com login wall: exporte cookies (extensão "Get cookies.txt") e aponte `VEGAPUNK_COOKIES_FILE`.
- Erro `ERR-004`/`ERR-005`: sem conteúdo extraível → item vai para `knowledge/_pending/`; cole o texto em "Notas manuais" e `/reprocess`.
- `yt-dlp` desatualizado é a causa nº 1 de falha: `docker compose build --no-cache` atualiza.

## Testes

`PYTHONPATH=src .venv/bin/python -m pytest`
