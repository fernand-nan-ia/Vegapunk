# Changelog

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
