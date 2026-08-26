# Índice de Fontes

Fontes externas referenciadas pelo pacote. "Valor adversarial" indica o quanto a fonte serve para o agente revisor questionar a implementação (alto = usar como base de checagem).

| ID | Fonte | Link | Tipo | Valor adversarial | Status |
|---|---|---|---|---|---|
| F001 | Telegram Bot API — referência oficial | https://core.telegram.org/bots/api | Doc oficial | Alto — validar campos de update, limites de callback_data, contrato do setWebhook | Não embarcada (baixar) |
| F002 | Telegram Bot API — Webhooks guide | https://core.telegram.org/bots/webhooks | Doc oficial | Alto — requisitos de TLS, comportamento de reenvio | Não embarcada (baixar) |
| F003 | yt-dlp — README/opções | https://raw.githubusercontent.com/yt-dlp/yt-dlp/master/README.md | Doc oficial | Alto — validar flags de legendas usadas em X001 | Não embarcada (baixar) |
| F004 | Anthropic API — Messages | https://docs.claude.com/en/api/messages | Doc oficial | Alto — contrato do endpoint, campo usage | Não embarcada (consultar online; requer navegação) |
| F005 | Sidekiq — Error Handling wiki | https://raw.githubusercontent.com/wiki/sidekiq/sidekiq/Error-Handling.md | Doc oficial | Alto — semântica de retries_exhausted e dead set | Não embarcada (baixar) |
| F006 | json_schemer (gem) | https://github.com/davishmcclurg/json_schemer | Repositório | Médio — API de validação usada em E001 | Não embarcada (consultar) |
| F007 | ytdlp.org — guia Instagram | https://ytdlp.org/guides/yt-dlp-for-instagram | Guia terceiro | Médio — contexto para Fase 3 (riscos de cookies/bloqueio); NÃO usar na Fase 1 | Referência futura |

## Observações

- F001–F005 são as fontes de verdade para a fase `validation` do YAML: em conflito entre este pacote e a doc oficial, **a doc oficial vence** e a divergência deve ser reportada.
- F007 documenta por que Instagram ficou fora da Fase 1 (login wall, risco de bloqueio de conta ao usar cookies pessoais em volume).
