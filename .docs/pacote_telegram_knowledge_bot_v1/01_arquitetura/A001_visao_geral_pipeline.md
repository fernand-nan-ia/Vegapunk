# A001 — Visão Geral do Pipeline

## Objetivo do sistema

Transformar links compartilhados num chat do Telegram em conhecimento estruturado, pesquisável e consumível pelo Claude Code. O usuário envia um link; o sistema captura, extrai o conteúdo, enriquece com IA e persiste em duas camadas (Postgres = verdade; Markdown/Obsidian = consumo humano e por agentes).

## Princípio central (não negociável)

**Captura é síncrona e rápida; processamento é assíncrono e pode falhar.**
O bot confirma o recebimento em ≤ 2 segundos. Toda extração/enriquecimento acontece em jobs Sidekiq. Falha de processamento NUNCA bloqueia a captura e NUNCA perde o link.

## As 5 camadas

### Camada 1 — Captura (síncrona)

- **Entrada:** webhook do Telegram Bot API (POST no endpoint Rails).
- **Responsabilidade:** validar o secret do webhook, extrair URLs da mensagem, criar registro `knowledge_items` com estado `captured`, enfileirar `NormalizeItemJob`, responder ao usuário com confirmação curta.
- **Requisito REQ-001:** tempo de resposta do webhook ≤ 2s (Telegram reenvia updates se demorar; ver T001).
- **Requisito REQ-002:** mensagens sem URL reconhecível recebem resposta explicando o formato aceito; nada é persistido.

### Camada 2 — Normalização (assíncrona, rápida)

- **Responsabilidade:** seguir redirects de shortlinks (`youtu.be`, `vt.tiktok.com`), extrair ID canônico da plataforma, detectar plataforma (`youtube` | `tiktok` | `instagram` | `other`), deduplicar por `(platform, external_id)`.
- **Requisito REQ-003:** duplicata NÃO cria novo registro; incrementa `shared_count` e atualiza `last_shared_at` do existente, e o bot informa "já capturado em <data>".
- **Estado de saída:** `normalized` (ou `duplicate`, terminal).

### Camada 3 — Extração (assíncrona, frágil, com retry)

- **Fase 1:** apenas YouTube (ver X001). Estratégia: transcript nativo/automático; sem download de vídeo.
- **Requisito REQ-004:** falha após esgotar retries move o item para `extraction_failed` com `error_code` catalogado (ERR-###) — nunca exceção genérica engolida.
- **Requisito REQ-005:** plataformas fora do escopo da fase atual vão direto para `pending_manual` com notificação ao usuário. O link fica salvo; o sistema degrada com elegância.
- **Estado de saída:** `extracted`.

### Camada 4 — Enriquecimento (assíncrona, Claude API)

- **Responsabilidade:** gerar resumo, key points, tags e matriz de aplicabilidade via Claude API, com output validado contra o JSON Schema do README.
- **Requisito REQ-006:** resposta que não valide contra o schema => 1 retry com feedback do erro de validação; segunda falha => estado `enrichment_failed`.
- **Estado de saída:** `enriched`.

### Camada 5 — Persistência e Loop de Retorno

- **Responsabilidade:** gravar enriquecimento no Postgres (JSONB), gerar arquivo `.md` no vault (ver O001), commitar no git, e enviar ao usuário o resumo com botões inline de triagem: `Arquivar` / `Aplicar: SaaS` / `Aplicar: Cliente` / `Descartar`.
- **Requisito REQ-007:** a decisão de triagem atualiza `triage_decision` e `triaged_at`. Item sem triagem permanece `enriched` (visível numa fila de pendências).
- **Estado final feliz:** `archived` | `applied_saas` | `applied_client` | `discarded`.

## Fluxo de dados (resumo)

```
Telegram msg → [webhook] → captured
  → NormalizeItemJob → normalized | duplicate
  → ExtractContentJob → extracted | extraction_failed | pending_manual
  → EnrichItemJob → enriched | enrichment_failed
  → PersistAndNotifyJob → (md no vault + botões)
  → callback de triagem → archived | applied_saas | applied_client | discarded
```

## Fronteiras do sistema (Fase 1)

- **Não** baixa vídeos completos (apenas transcripts).
- **Não** processa TikTok/Instagram (captura e marca `pending_manual`).
- **Não** faz busca semântica/embeddings — o vault em git É a interface com o Claude Code nesta fase.
- **Não** tem UI web; o Telegram é a única interface interativa. Sidekiq Web é apenas operacional.
