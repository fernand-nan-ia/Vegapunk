# HANDOFF — Vegapunk (escrito em 2026-08-26, fim da sessão 1)

## Estado atual: MVP construído, bot ONLINE, nenhum link real processado ainda

- Container `vegapunk-vegapunk-1` rodando (`docker compose ps`), com token novo do BotFather, `OPENROUTER_API_KEY` e `TELEGRAM_ALLOWED_CHAT_IDS` preenchidos no `.env`.
- Modelo: `google/gemini-3.7-flash` via OpenRouter. Whisper local `small` (baixa ~500 MB no 1º vídeo sem legenda).
- GitHub `fernand-nan-ia/Vegapunk` em `37d89bf`, histórico limpo (um token vazou num commit anterior; foi reescrito e o token revogado).
- Testes: 16/16 verdes (`PYTHONPATH=src .venv/bin/python -m pytest`).

## Primeira coisa a fazer amanhã

1. Fernando manda um link de YouTube ao bot → verificar: resposta "✅ Capturado", resumo com 4 botões, arquivo em `knowledge/youtube/`, `knowledge/INDEX.md`, commit automático (`git log`).
2. Depois um TikTok e um Reel do Instagram (caminho áudio → Whisper). Instagram pode exigir cookies (`VEGAPUNK_COOKIES_FILE`).
3. Avaliar qualidade do resumo do Gemini; ajustar `SYSTEM` em `src/vegapunk/enrich.py` se preciso. Trocar de modelo = mudar `VEGAPUNK_MODEL` no `.env` + `docker compose up -d --force-recreate`.
4. Testar a skill `/vegapunk <pergunta>` de dentro de outro projeto (existe em `~/.claude/commands/`, FURY e aqui).

## Como operar

| Ação | Comando |
|---|---|
| Logs | `docker compose logs --tail 50 -f` |
| Mudou `.env` | `docker compose up -d --force-recreate` (restart NÃO relê o .env) |
| Mudou código em `src/` | `docker compose restart` (código é montado via `PYTHONPATH=/app/src`, sem rebuild) |
| Mudou `pyproject.toml` / deps | `docker compose build && docker compose up -d` |
| Testes | `PYTHONPATH=src .venv/bin/python -m pytest -q` |
| Ver banco | `sqlite3 data/vegapunk.db "select id,status,platform,title from knowledge_items"` |

## Decisões fechadas (não reabrir)
- Python único + polling + SQLite + Docker local. Sem Rails/Sidekiq/webhook/VPS (o pacote em `.docs/pacote_telegram_knowledge_bot_v1` é o plano v1, superado; as ideias boas dele — máquina de estados, dedup, vault regenerável, triagem — foram mantidas).
- Sem API da Anthropic direta (custo). OpenRouter via SDK `openai`, `response_format json_schema strict` + validação Pydantic com 1 retry.
- Vault `knowledge/` é projeção do SQLite; só `## Notas manuais` é editável à mão.

## Armadilhas conhecidas
- TikTok: erro "Unable to extract universal data for rehydration" é intermitente → pipeline tenta 4x com espera crescente.
- YouTube legendas: nunca usar `pt.*` em `--sub-langs` (puxa auto-traduções e dá HTTP 429). Se legenda falhar, cai para áudio+Whisper.
- Item com `extraction_failed`/`pending_manual` vai para `knowledge/_pending/`; colar o texto em "Notas manuais" e `/reprocess <id>`.
- `yt-dlp` desatualizado é a causa nº 1 de falha: `docker compose build --no-cache`.

## Mapa do código
`src/vegapunk/`: `bot.py` (handlers/comandos/teclado) → `pipeline.py` (normalize→extract→enrich→persist, retries, triagem, reprocess) → `normalize.py`, `extract.py` (yt-dlp + VTT + faster-whisper), `enrich.py` (OpenRouter), `vault.py` (md + INDEX + git), `db.py` (SQLite + `transition_to`), `config.py` (env).

## Ideias para depois (não iniciadas)
- Healthcheck diário no Telegram (itens presos, falhas 24h).
- Push automático (`VEGAPUNK_GIT_PUSH=true` + montar `~/.ssh` no compose).
- Bloco "Base de conhecimento" no CLAUDE.md do SaaS e do site do cliente apontando para a skill `/vegapunk`.
- MCP de consulta ao vault (Fase 4 do plano original).
