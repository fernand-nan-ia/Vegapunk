# Pacote de Conhecimento: Telegram Knowledge Bot — Fase 1

**Versão:** 1.0.0
**Data:** 2026-08-13
**Escopo:** Fase 1 do pipeline — Bot Telegram + Postgres + extração YouTube + enriquecimento Claude + persistência Obsidian.
**Fora de escopo nesta versão:** TikTok/Whisper (Fase 2), Instagram/fallback manual e backfill (Fase 3), camada de consulta MCP (Fase 4).

## Novidades da v1.0.0

- Versão inicial. Pipeline completo ponta a ponta para links de YouTube.
- Máquina de estados com degradação elegante (`pending_manual` já previsto no schema, mesmo sem Instagram nesta fase).
- Contrato JSON de enriquecimento com schema fixo e validação obrigatória.
- Spec determinística em 5 fases para execução via Claude Code (`INSTRUCOES_PARA_CLAUDE_CODE.yaml`).

## Estrutura do Pacote

```
pacote_telegram_knowledge_bot_v1/
├── README.md                          ← este arquivo
├── INDICE_DE_FONTES.md                ← tabela de fontes externas
├── download_all.sh                    ← download de fontes não embarcadas
├── INSTRUCOES_PARA_CLAUDE_CODE.yaml   ← prompt-spec de execução (5 fases)
├── 01_arquitetura/
│   ├── A001_visao_geral_pipeline.md   ← as 5 camadas, fluxo de dados
│   └── A002_decisoes_arquiteturais.md ← ADRs: por que Rails, por que webhook, etc.
├── 02_schema_dados/
│   └── D001_schema_postgres.md        ← tabelas, estados, índices, migrations
├── 03_integracao_telegram/
│   └── T001_bot_api_webhook.md        ← Bot API, webhook, segurança, botões inline
├── 04_extracao_youtube/
│   └── X001_extracao_transcript.md    ← estratégia de extração, fallbacks, erros
├── 05_enriquecimento_claude/
│   └── E001_prompt_spec_enriquecimento.md ← prompt, contrato JSON, validação
├── 06_persistencia_obsidian/
│   └── O001_formato_vault.md          ← frontmatter, nomenclatura, git
└── 07_observabilidade/
    └── B001_sidekiq_retry_logging.md  ← filas, retries, dead-letter, logs
```

## Prioridade de Ingestão

Ordem recomendada para agentes que consomem este pacote:

| Ordem | Arquivo | Motivo |
|---|---|---|
| 1 | `01_arquitetura/A001` | Modelo mental do sistema inteiro |
| 2 | `02_schema_dados/D001` | O schema é o contrato central; tudo referencia os estados |
| 3 | `01_arquitetura/A002` | Justificativas — evita que agentes "melhorem" decisões já tomadas |
| 4 | `03_integracao_telegram/T001` | Camada de entrada |
| 5 | `04_extracao_youtube/X001` | Camada de extração |
| 6 | `05_enriquecimento_claude/E001` | Camada de enriquecimento |
| 7 | `06_persistencia_obsidian/O001` | Camada de saída |
| 8 | `07_observabilidade/B001` | Transversal; ler por último com contexto completo |

## Convenção de IDs

| Prefixo | Domínio | Exemplo |
|---|---|---|
| A### | Arquitetura / ADR | A001 |
| D### | Dados / Schema | D001 |
| T### | Telegram | T001 |
| X### | Extração | X001 |
| E### | Enriquecimento | E001 |
| O### | Obsidian / Persistência | O001 |
| B### | Observabilidade | B001 |
| REQ-### | Requisito funcional | REQ-001 |
| ADR-### | Decisão arquitetural | ADR-001 |
| ERR-### | Cenário de erro catalogado | ERR-001 |

## Schema de Output JSON (enriquecimento)

Todo item processado pelo pipeline DEVE produzir um objeto que valide contra:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KnowledgeItemEnrichment",
  "type": "object",
  "required": ["item_id", "platform", "title", "summary", "key_points", "tags", "applicability", "confidence"],
  "additionalProperties": false,
  "properties": {
    "item_id": { "type": "string", "description": "UUID do knowledge_items.id" },
    "platform": { "type": "string", "enum": ["youtube", "tiktok", "instagram", "other"] },
    "title": { "type": "string", "maxLength": 200 },
    "summary": { "type": "string", "maxLength": 1500, "description": "Resumo em pt-BR, 3-6 frases" },
    "key_points": {
      "type": "array", "minItems": 1, "maxItems": 10,
      "items": { "type": "string", "maxLength": 300 }
    },
    "tags": {
      "type": "array", "minItems": 1, "maxItems": 8,
      "items": { "type": "string", "pattern": "^[a-z0-9-]+$" }
    },
    "applicability": {
      "type": "object",
      "required": ["saas_pessoal", "projeto_cliente", "estudo_geral"],
      "properties": {
        "saas_pessoal": { "type": "string", "enum": ["alta", "media", "baixa", "nenhuma"] },
        "projeto_cliente": { "type": "string", "enum": ["alta", "media", "baixa", "nenhuma"] },
        "estudo_geral": { "type": "string", "enum": ["alta", "media", "baixa", "nenhuma"] }
      },
      "additionalProperties": false
    },
    "confidence": {
      "type": "string", "enum": ["alta", "media", "baixa"],
      "description": "Confiança do modelo na qualidade da extração-fonte (transcript ruim => baixa)"
    }
  }
}
```

## Como usar este pacote

1. Descompacte na raiz do repositório do projeto (ou em `docs/knowledge/`).
2. Execute `bash download_all.sh` para baixar fontes externas listadas em `INDICE_DE_FONTES.md`.
3. Aponte o Claude Code para `INSTRUCOES_PARA_CLAUDE_CODE.yaml` e execute as 5 fases em ordem.
4. A fase `validation` do YAML contém o checklist de aceite — nenhuma entrega é considerada completa sem ele.
