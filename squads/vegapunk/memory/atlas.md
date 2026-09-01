# Atlas — diário

## Sobre o Fernando
- Engenheiro civil; constrói produtos com Claude Code; não é dev profissional
- Dois projetos: SaaS próprio (quer vender) e site de um cliente

## Diário
- 2026-08-26 · Fernando quer os Satélites com personalidade completa para conversar por Telegram no futuro

## Construído
- 2026-08-28 · Roteador do grupo multi-bot (Story 1a) · `src/vegapunk/router.py` (novo), `tests/test_router.py` (novo), campo `router_model` em `config.py` · desfazer: apagar os dois arquivos novos e a linha `router_model` do config; nada mais foi tocado, bot.py/chat.py intactos
- 2026-08-28 · Consertos do *verify da Lilith + porteiro do dinheiro · `router.py` (teto de 3 Satélites, cliente próprio 15s sem retry, contexto truncado, log sanitizado), `bot.py` (`is_allowed` falha fechada + filtro por usuário + grupo desligado), `config.py`, `__main__.py`, `tests/test_bot_guard.py` (novo) · desfazer: `git checkout --` nos quatro de src/ e apagar test_bot_guard.py
- 2026-08-28 · 2ª passada da Lilith (MÉDIOs 11-13) · `router.py` (cliente único via lru_cache, `max_retries=1`), `bot.py` (aviso de lista vazia rebaixado para debug) · desfazer: `git checkout --` nos dois
- 2026-08-28 · Story 1b · `speakers.py` (novo: os 6 como telegram.Bot puro, init paralelo com 1 repique), `config.bot_tokens`, `bot.is_allowed(from_bot=)` trava anti-loop, `talk()` fala pelo bot do Satélite em grupo, `__main__` post_init/post_shutdown, `tests/test_speakers.py` (novo) · desfazer: apagar speakers.py e o teste, `git checkout --` em bot/config/__main__
- 2026-08-28 · Consertos do *verify da 1b (5 achados) · `config.py` (bot_token sai de bot_tokens: a renomeação da Story 2 passa a funcionar), `speakers.py` (shutdown do bot que falha, `say_all` com boca única, queda sem reply_to), `bot.py` (`responder()` testável + laço de envio protegido) · desfazer: `git checkout --` nos três
- 2026-08-28 · Story 1c · `router.decide()` (cascata 1-3 numa função só: fecha o achado 7), teto de 20 chamadas/min (achado 8), `chat.active_age()` + `reply(as_sat=)`, `bot.falar_no_grupo()` e `mencoes_explicitas()`, `tests/test_cascade.py` (novo, 11) · desfazer: `git checkout --` nos três de src/ e apagar o teste; VEGAPUNK_GROUP_ENABLED=false já deixa o grupo mudo sem tocar em código
- 2026-08-28 · Consertos do *verify da 1c (5 achados) · `router.pode_responder()` (teto da camada CARA: 6/min e 60/h, medido em 24.788 tokens por resposta), `bot.mencoes_explicitas` casa @…<id>…bot sem depender do get_me, `bot.responder_no_grupo()` testável com contexto atribuído e janela seguindo o primeiro chamado · desfazer: `git checkout --` em router.py e bot.py
- 2026-08-31 · Story 1d + consertos · `bot.notificar()` (dono fala pela própria boca, teclado sai pelo leitor porque o clique volta a quem enviou), captura anunciada pelo dono, `pipeline.MAX_PARALELO=3` (semáforo: 30 links colados derrubavam o container), título do item na linha do teclado, teto de hora 60→25 (York) · desfazer: `git checkout --` em bot.py, pipeline.py, router.py

