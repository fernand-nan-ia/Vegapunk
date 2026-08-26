# A002 — Decisões Arquiteturais (ADRs)

Estas decisões estão **fechadas** para a Fase 1. Agentes executores NÃO devem propor alternativas durante a implementação; divergências devem ser registradas como comentário para revisão humana, nunca implementadas unilateralmente.

## ADR-001 — Rails monolito, não microserviço Python

**Decisão:** implementar como engine/namespace dentro de app Rails com Sidekiq, não como serviço Python separado.

**Justificativa:** o operador já mantém Rails + Postgres + Sidekiq via agentes. Um segundo runtime (Python) dobraria a superfície de deploy, observabilidade e dependências por um ganho marginal (bibliotecas de scraping ligeiramente melhores em Python). A extração YouTube em Fase 1 é chamada de CLI (`yt-dlp`) via `Open3`, agnóstica de linguagem.

**Consequência aceita:** se a Fase 2 (Whisper/TikTok) exigir tooling Python pesado, reavaliar num ADR novo — não antes.

## ADR-002 — Webhook, não long polling

**Decisão:** receber updates do Telegram via webhook HTTPS.

**Justificativa:** long polling exige processo dedicado sempre vivo e complica deploys; webhook usa a infra web já existente e escala com o app. Requisito: endpoint público com TLS e validação de `secret_token` (ver T001).

**Consequência aceita:** desenvolvimento local exige túnel (ngrok/cloudflared) ou modo polling apenas em dev — permitido SOMENTE em `Rails.env.development?`.

## ADR-003 — Postgres como fonte de verdade; Markdown como projeção

**Decisão:** todo estado vive no Postgres. Os arquivos `.md` do vault são projeção regenerável (write-through), nunca editados como fonte primária pelo sistema.

**Justificativa:** dois donos de verdade geram divergência silenciosa. Com o Postgres como verdade, o vault inteiro pode ser regenerado com uma rake task (`vault:rebuild`), o que também é o mecanismo de recuperação de desastre da camada de consumo.

**Consequência aceita:** edições manuais nos `.md` podem ser sobrescritas por regeneração. Anotações humanas devem ir na seção `## Notas manuais` do arquivo, que a regeneração preserva (ver O001).

## ADR-004 — Transcript, não download de vídeo (Fase 1)

**Decisão:** YouTube via legenda/transcript; nenhum vídeo é baixado.

**Justificativa:** o objetivo é conhecimento textual, não arquivo de mídia. Transcript é ~100x mais barato em banda/armazenamento, sem custo de transcrição, e suficiente para enriquecimento. Vídeos sem transcript disponível caem em `extraction_failed` com `ERR-004` (ver X001) — o custo de Whisper para esses casos é decisão da Fase 2.

## ADR-005 — Validação de schema no enriquecimento é bloqueante

**Decisão:** output do Claude que não valide contra o JSON Schema não entra no banco. Um retry com o erro de validação anexado; depois, `enrichment_failed`.

**Justificativa:** o vault e futuros consumidores (MCP na Fase 4) dependem de estrutura estável. Aceitar JSON "quase certo" cria dívida de dados que corrompe downstream silenciosamente. Falha explícita > dado corrompido.

## ADR-006 — Estados como enum de strings no Postgres

**Decisão:** coluna `status` como string com CHECK constraint (não enum nativo do PG, não integer).

**Justificativa:** legível em queries manuais e logs; CHECK constraint dá integridade sem o atrito de `ALTER TYPE` do enum nativo a cada novo estado; integers são ilegíveis em auditoria.

## ADR-007 — Idempotência por chave natural

**Decisão:** unicidade em `(platform, external_id)` com índice único; dedup na normalização, não na captura.

**Justificativa:** o mesmo vídeo chega por URLs diferentes (youtu.be, youtube.com/watch, com/sem query params). Só após normalização existe ID canônico confiável. A captura registra tudo; a normalização resolve identidade.
