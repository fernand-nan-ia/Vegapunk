# D001 — Schema Postgres

## Tabela principal: `knowledge_items`

```sql
CREATE TABLE knowledge_items (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Captura
  raw_url            TEXT        NOT NULL,
  telegram_chat_id   BIGINT      NOT NULL,
  telegram_message_id BIGINT     NOT NULL,
  captured_at        TIMESTAMPTZ NOT NULL DEFAULT now(),

  -- Normalização
  platform           TEXT,             -- youtube | tiktok | instagram | other
  external_id        TEXT,             -- ID canônico na plataforma (ex.: videoId do YouTube)
  canonical_url      TEXT,
  shared_count       INTEGER     NOT NULL DEFAULT 1,
  last_shared_at     TIMESTAMPTZ NOT NULL DEFAULT now(),

  -- Extração
  content_type       TEXT,             -- transcript | caption | ocr | manual
  raw_content        TEXT,             -- transcript bruto
  content_lang       TEXT,             -- ex.: pt, en
  extracted_at       TIMESTAMPTZ,

  -- Enriquecimento
  enrichment         JSONB,            -- objeto validado contra KnowledgeItemEnrichment
  enriched_at        TIMESTAMPTZ,
  model_used         TEXT,             -- ex.: claude-sonnet-4-6

  -- Triagem (loop de retorno)
  triage_decision    TEXT,             -- archive | apply_saas | apply_client | discard
  triaged_at         TIMESTAMPTZ,

  -- Máquina de estados e erros
  status             TEXT NOT NULL DEFAULT 'captured',
  error_code         TEXT,             -- ERR-### catalogado
  error_detail       TEXT,
  retry_count        INTEGER NOT NULL DEFAULT 0,

  created_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at         TIMESTAMPTZ NOT NULL DEFAULT now(),

  CONSTRAINT chk_status CHECK (status IN (
    'captured', 'normalized', 'duplicate',
    'extracted', 'extraction_failed', 'pending_manual',
    'enriched', 'enrichment_failed',
    'archived', 'applied_saas', 'applied_client', 'discarded'
  )),
  CONSTRAINT chk_platform CHECK (platform IS NULL OR platform IN
    ('youtube', 'tiktok', 'instagram', 'other')),
  CONSTRAINT chk_triage CHECK (triage_decision IS NULL OR triage_decision IN
    ('archive', 'apply_saas', 'apply_client', 'discard'))
);

-- Idempotência (ADR-007): parcial porque external_id só existe pós-normalização
CREATE UNIQUE INDEX idx_items_platform_external
  ON knowledge_items (platform, external_id)
  WHERE external_id IS NOT NULL AND status <> 'duplicate';

CREATE INDEX idx_items_status ON knowledge_items (status);
CREATE INDEX idx_items_enrichment_tags ON knowledge_items
  USING GIN ((enrichment -> 'tags'));
```

## Tabela de auditoria: `item_events`

Toda transição de estado gera um evento. É o log auditável do pipeline.

```sql
CREATE TABLE item_events (
  id           BIGSERIAL PRIMARY KEY,
  item_id      UUID NOT NULL REFERENCES knowledge_items(id),
  from_status  TEXT,
  to_status    TEXT NOT NULL,
  actor        TEXT NOT NULL,   -- 'webhook' | 'normalize_job' | 'extract_job' | 'enrich_job' | 'persist_job' | 'user_triage'
  metadata     JSONB,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_events_item ON item_events (item_id, created_at);
```

## Máquina de estados (transições válidas)

| De | Para | Gatilho |
|---|---|---|
| — | `captured` | webhook recebe URL |
| `captured` | `normalized` | NormalizeItemJob ok |
| `captured` | `duplicate` | dedup por `(platform, external_id)` |
| `normalized` | `extracted` | ExtractContentJob ok |
| `normalized` | `extraction_failed` | retries esgotados |
| `normalized` | `pending_manual` | plataforma fora do escopo da fase |
| `extracted` | `enriched` | EnrichItemJob ok + schema válido |
| `extracted` | `enrichment_failed` | 2ª falha de validação ou API |
| `enriched` | `archived` / `applied_saas` / `applied_client` / `discarded` | callback de triagem |
| `extraction_failed` / `enrichment_failed` | `normalized` / `extracted` | reprocessamento manual (rake task) |

**Regra:** transições fora desta tabela levantam exceção (`InvalidTransitionError`). Implementar como método único `transition_to!(new_status, actor:, metadata: nil)` no model — nunca `update(status: ...)` direto.

## Cenários de erro catalogados

| Código | Camada | Significado | Ação |
|---|---|---|---|
| ERR-001 | Normalização | Redirect de shortlink falhou (timeout/4xx) | retry padrão Sidekiq |
| ERR-002 | Normalização | URL não corresponde a plataforma conhecida | `platform = 'other'`, `pending_manual` |
| ERR-003 | Extração | yt-dlp exit code ≠ 0 | retry; esgotado => `extraction_failed` |
| ERR-004 | Extração | Vídeo sem transcript disponível | `extraction_failed` sem retry (determinístico) |
| ERR-005 | Extração | Vídeo privado/removido/região bloqueada | `extraction_failed` sem retry |
| ERR-006 | Enriquecimento | Claude API erro 5xx/timeout | retry padrão Sidekiq |
| ERR-007 | Enriquecimento | Output falhou validação de schema 2x | `enrichment_failed` |
| ERR-008 | Persistência | Falha de git commit no vault | retry; item permanece `enriched` (md regenerável) |
