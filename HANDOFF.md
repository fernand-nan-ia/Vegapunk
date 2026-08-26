# HANDOFF — Vegapunk (atualizado em 2026-08-26, sessão 2)

## Estado atual: MVP validado end-to-end (YouTube + TikTok)

Sessão 2 (2026-08-26): YouTube (legenda) e TikTok (áudio → Whisper) processados, triados via botão, vault + INDEX + commits automáticos conferidos. Fluxo de falha → `_pending/` → `/reprocess` também validado. Instagram ainda não testado (baixa prioridade: uso real é YouTube + TikTok).

Correções da sessão 2: comentários inline no `.env` (ver Armadilhas), `--extractor-retries 5` no yt-dlp, error handler de rede no bot (`NetworkError` não derruba mais o polling).


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
- **`.env`: NUNCA comentário na mesma linha do valor.** Docker `env_file` não trata `#` como comentário → o valor vira `# texto...`. Foi isso que quebrou o TikTok (yt-dlp recebeu `--cookies "# cookies.txt..."`, criou um cookie jar na raiz e reusou cookies queimados → 403 em todas as tentativas). `config.py` agora corta em `#` por defesa, mas mantenha o `.env` limpo.
- Se aparecer um arquivo `# cookies.txt (Netscape)...` na raiz, é sintoma desse bug — apague e verifique o `.env`.
- TikTok: erro "Unable to extract universal data for rehydration" é intermitente (~40% por tentativa) → pipeline tenta 6x com espera crescente (15 s × n).
- YouTube legendas: `choose_sub_langs(meta)` pede só manuais (pt/en/es) ou a auto-legenda ORIGINAL (`*-orig`). Nunca pedir `pt` de auto-caption: o YouTube traduz sob demanda → HTTP 429 → caía em 33 min de Whisper (aconteceu 2026-08-26). Se legenda falhar, cai para áudio+Whisper.
- Whisper: `language_detection_segments=4` (rótulo de idioma errava, ex. 'yo' num vídeo em inglês); áudio com <3 s de fala após VAD é pulado (música de slideshow).
- Item com `extraction_failed`/`pending_manual` vai para `knowledge/_pending/`; colar o texto em "Notas manuais" e `/reprocess <id>`.
- `yt-dlp` desatualizado é a causa nº 1 de falha: `docker compose build --no-cache`.

## Mapa do código
`src/vegapunk/`: `bot.py` (handlers/comandos/teclado) → `pipeline.py` (normalize→extract→enrich→persist, retries, triagem, reprocess) → `normalize.py`, `extract.py` (yt-dlp + VTT + faster-whisper + slides TikTok), `enrich.py` (OpenRouter; schema com topics/tools; `read_slides` visão), `format_summary` em `pipeline.py` (mensagem Telegram), `vault.py` (md + INDEX + git), `db.py` (SQLite + `transition_to`), `config.py` (env).

## Ideias para depois (não iniciadas)
- **Visão (Opção A, decidido 2026-08-26):** `ffmpeg` amostra 1 frame/10 s → `enrich.read_slides()` descreve o que está na tela → texto entra junto da transcrição. Gatilho manual (`/ver <link>`), não automático. Custo medido: ~1k tokens/imagem ⇒ ~US$ 0,02 por 10 min no gemini-3.7-flash (US$ 0,375/M in). Exige baixar o vídeo inteiro (hoje só áudio) em `tmp/<item_id>/`, apagado ao fim. Vale para screencast/tutorial/demo de UI; inútil para talking-head.

- Parser do enrich mais tolerante (extrair `{...}` do texto): Gemini às vezes responde vazio na 1ª tentativa; o retry resolve, mas custa uma chamada.
- **TikTok slideshow (`/photo/`) é suportado**: `extract_tiktok_slides` usa `TikTokIE._extract_web_data_and_status` (API privada do yt-dlp — se um update quebrar, `tests/test_slides.py` não pega, o log mostra `tiktok web data:`), baixa `imagePost.images`, o Gemini lê as imagens (`enrich.read_slides`, sem OCR local) e, se `music.original`, transcreve a narração com Whisper. `content_type: slides`. Instagram carrossel continua ERR-008 (exige login); só rende a legenda (`--ignore-no-formats-error` já está no `fetch_metadata`); conteúdo em imagem precisaria de OCR. Reels ainda não testados; provavelmente precisam de `VEGAPUNK_COOKIES_FILE` com cookies exportados do navegador.
- Healthcheck diário no Telegram (itens presos, falhas 24h).
- Push automático (`VEGAPUNK_GIT_PUSH=true` + montar `~/.ssh` no compose).
- Bloco "Base de conhecimento" no CLAUDE.md do SaaS e do site do cliente apontando para a skill `/vegapunk`.
- MCP de consulta ao vault (Fase 4 do plano original).
