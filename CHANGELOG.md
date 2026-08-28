# Changelog

## v1.7.0 — 2026-08-28
### Adicionado
- `src/vegapunk/speakers.py`: os outros seis Satélites como bots que só FALAM. Decisão de projeto: `telegram.Bot` puro em vez de uma `Application` por token — um laço de polling em vez de sete, e o critério "os outros não registram handler" vira estrutural (num `Bot` não existe onde registrar). Inicialização em paralelo (1,6 s contra 17 s sequencial) com uma segunda chance, porque o `TimedOut` do Telegram é intermitente conhecido e sem repique um piscar de rede aposentaria aquele bot até o restart seguinte.
- **Trava anti-loop** (condição bloqueante do Shaka): `is_allowed(from_bot=True)` é a porta 0 do porteiro, antes até da lista de chats. Sete bots num grupo, um respondendo ao outro, era o único caminho para custo verdadeiramente descontrolado.
- `config.bot_tokens`: varredura do ambiente (`TELEGRAM_BOT_TOKEN` → stella, `TELEGRAM_BOT_TOKEN_<ID>` → `<id>`). Acrescentar um bot passa a ser uma linha no `.env`.
- `bot.responder()`: no grupo cada Satélite fala pelo próprio bot (nome e ícone dele); na DM, pelo bot de sempre — um bot não pode escrever para quem nunca abriu conversa com ele.
- `tests/test_speakers.py` (13) e testes de anti-loop e de boca em `test_bot_guard.py`. Sem dependência nova: `asyncio.run()` no lugar do `pytest-asyncio`.

### Corrigido
- **`TELEGRAM_BOT_TOKEN_STELLA` derrubava o serviço** enquanto um comentário no `config.py` afirmava que era o caminho da renomeação. `bot_token` passou a sair do mesmo dicionário: a renomeação da Story 2 funciona de verdade.
- Bot que falha no `get_me` é desligado (o `initialize` já abriu o pool httpx; descartar sem `shutdown` vazava conexão — e vazava duas vezes, uma por tentativa).
- Resposta longa sai toda pela mesma boca: se o primeiro pedaço cair para o leitor, o resto vai com ele em vez de a fala aparecer metade com cada cara.
- Queda para o leitor larga o `reply_to_message_id`: se a mensagem original sumiu, ela é a causa da falha e repetir o kwarg faria o leitor falhar igual.
- Laço de envio protegido no `talk()`: resposta já paga em token não some mais em silêncio.

### Verificado em produção
- Os 6 bots confirmam identidade no Telegram no arranque (`@vegapunkklilithbot`, `@vegapunkshakabot`, …).
- `/lilith oi` no **grupo** → `grupo -5120920932 está no .env mas VEGAPUNK_GROUP_ENABLED=false: ignorando`. Silêncio por decisão, custo zero.
- `/lilith oi` na **DM** → resposta em personagem, com `reply_to` e ícone. Sem regressão.

### Gate: Shaka PASS · Verify: Lilith ÁGUA NO PORÃO → 5 achados (1 ALTO) todos corrigidos · Testes: 112/112

## v1.6.0 — 2026-08-28
### Adicionado
- `src/vegapunk/router.py`: roteador do grupo multi-bot (camadas 2 e 3 da cascata do PRD). `mentions()` acha nomes de graça e ignora nomes dentro de links; `route()` gasta 1 chamada barata (sem persona, sem `INDEX.md`) para decidir quem responde. Falha sempre fechada: erro, JSON inválido, id desconhecido ou confiança baixa = ninguém responde.
- `bot.is_allowed()`: porteiro do dinheiro com quatro portas (lista de chats, chat, grupo desligado, filtro por usuário). `/id` fica fora de propósito, como caminho de bootstrap.
- `.env`: `VEGAPUNK_ROUTER_MODEL` (opcional), `TELEGRAM_ALLOWED_USER_IDS` (opcional), `VEGAPUNK_GROUP_ENABLED` (default `false`).
- `tests/test_router.py` (20) e `tests/test_bot_guard.py` (7).
- `docs/prd/satelites-multibots-grupo-telegram.md` §0 (decisões do Fernando) e §4.1 (cascata de 5 camadas).
- `squads/vegapunk/stories/`: Stories 1a (pronta, entregue), 1b e 1c (rascunho).
- Punk Records: 12 itens recuperados (política de bots e FAQ do Telegram, as 7 páginas da wiki dos Satélites, 2 vídeos) + a live de avaliação de imóveis. Vault: 112 → 125.

### Corrigido
- **Falha aberta no porteiro**: `TELEGRAM_ALLOWED_CHAT_IDS` vazio fazia o bot aceitar QUALQUER chat do Telegram. Agora recusa todos.
- Grupo autorizado no `.env` não responde enquanto `VEGAPUNK_GROUP_ENABLED=false` — o id pode ficar no arquivo sem risco.
- Roteador: teto de 3 Satélites por mensagem (custo), cliente próprio (15 s, 1 repique) em vez do cliente do `enrich` (180 s × 3), contexto do grupo truncado por linha, `reason` do modelo sanitizado antes do log JSON, `EnrichmentError` prevista em vez de virar traceback.
- Concordância: **o Stella** é masculino (22 linhas em 9 arquivos).

### Gate: Shaka PASS · Verify: Lilith AGUENTOU (3 passadas, 13 achados, 3 ALTOs fechados) · Testes: 97/97
