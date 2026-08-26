# B001 — Observabilidade: Filas, Retries, Dead-letter e Logs

## Topologia de filas Sidekiq

| Fila | Jobs | Concorrência | Racional |
|---|---|---|---|
| `default` | NormalizeItemJob, PersistAndNotifyJob | padrão | rápidos, sem rate-limit externo |
| `extraction` | ExtractContentJob | 1 | serializa chamadas a plataformas (REQ-X04) |
| `enrichment` | EnrichItemJob | 1 | serializa chamadas à Claude API (REQ-E03) |

## Política de retry

- **Erros transientes** (ERR-001, ERR-003, ERR-006, ERR-008): retry padrão do Sidekiq com backoff exponencial, teto de **5 tentativas** (o default de 25 tentativas/21 dias não faz sentido aqui — em 1 dia você quer saber que falhou).
- **Erros determinísticos** (ERR-002, ERR-004, ERR-005, ERR-007): `sidekiq_retry_in { :kill }` ou raise de classe não-retryable — falha imediata para o estado terminal, sem desperdiçar tentativas.
- **`sidekiq_retries_exhausted`:** ao esgotar, o hook DEVE (1) aplicar `transition_to!` para o estado `*_failed`, (2) gravar `error_code`/`error_detail`, (3) notificar o usuário no Telegram. Um job morto silenciosamente no dead set do Sidekiq é o pior cenário: o usuário acha que o item foi processado.

## Logging estruturado

- **REQ-B01:** todo log de job em JSON com no mínimo: `item_id`, `job`, `event`, `duration_ms`, `error_code` (se houver). Nunca logar `raw_content` completo (ruído) nem o token do bot/API (segurança).
- **REQ-B02:** a tabela `item_events` (D001) é a auditoria de negócio; logs são auditoria técnica. Ambos obrigatórios — cada `transition_to!` grava evento; cada job loga início/fim.

## Painéis e verificação operacional

- **Sidekiq Web** montado em rota autenticada (`/admin/sidekiq` atrás de HTTP basic auth com credencial forte) — NUNCA exposto sem auth.
- **REQ-B03 — healthcheck diário** (job agendado, ex. sidekiq-cron):
  - itens presos > 24h em estados intermediários (`captured`, `normalized`, `extracted`) => alerta no Telegram;
  - contagem de `*_failed` das últimas 24h => resumo no Telegram;
  - `yt-dlp --version` vs. release mais recente (REQ-X02).
- **REQ-B04 — rake tasks operacionais:**
  - `kb:reprocess[item_id]` — reenfileira item em `*_failed` (transição de reprocessamento do D001);
  - `kb:stats` — contagem por estado/plataforma;
  - `vault:rebuild` — regenera o vault (O001).

## Definição de "pronto para produção" (Fase 1)

1. Webhook validando secret + allowlist (T001).
2. Máquina de estados com `transition_to!` único e `item_events` populado.
3. Retries com teto e `retries_exhausted` notificando o usuário.
4. Healthcheck diário ativo.
5. Vault regenerável via `vault:rebuild` sem perda de notas manuais.
