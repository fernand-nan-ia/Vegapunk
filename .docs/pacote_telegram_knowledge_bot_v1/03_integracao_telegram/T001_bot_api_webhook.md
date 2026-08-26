# T001 — Telegram Bot API: Webhook, Segurança e Botões Inline

## Setup do bot

1. Criar bot via `@BotFather` => obter `TELEGRAM_BOT_TOKEN` (guardar em credentials do Rails / ENV, nunca em código).
2. Registrar webhook:

```
POST https://api.telegram.org/bot<TOKEN>/setWebhook
{
  "url": "https://<dominio>/telegram/webhook",
  "secret_token": "<TELEGRAM_WEBHOOK_SECRET>",
  "allowed_updates": ["message", "callback_query"],
  "drop_pending_updates": true
}
```

`allowed_updates` restrito reduz ruído: só precisamos de mensagens (links) e callbacks (botões de triagem).

## Segurança do endpoint (obrigatório)

- **REQ-T01:** validar o header `X-Telegram-Bot-Api-Secret-Token` contra `TELEGRAM_WEBHOOK_SECRET` em TODA requisição; mismatch => 403 sem corpo.
- **REQ-T02:** aceitar apenas `chat_id` na allowlist (`TELEGRAM_ALLOWED_CHAT_IDS`). O bot é pessoal; qualquer outro chat recebe silêncio (200 sem ação, para não vazar existência).
- **REQ-T03:** o controller responde 200 imediatamente após enfileirar; nenhum processamento inline. O Telegram considera falha respostas lentas e reenvia o update => processar inline gera duplicatas.

## Parsing da mensagem de entrada

- Extrair URLs preferencialmente via `entities` do update (tipo `url`/`text_link`), com fallback para regex `URI.extract(text, %w[http https])`.
- Uma mensagem pode conter N URLs => N registros `captured` (cada um segue o pipeline independente).
- Mensagem sem URL: responder uma única linha explicando o uso ("Me envie um link de YouTube/TikTok/Instagram").

## Respostas do bot (contratos de mensagem)

| Momento | Mensagem |
|---|---|
| Captura ok | `✅ Capturado. Processando...` (reply à mensagem original) |
| Duplicata | `♻️ Já capturado em <data>. Compartilhamentos: <n>.` |
| Fora de escopo (fase) | `📥 Salvo como pendente (plataforma ainda não processada automaticamente).` |
| Extração falhou | `⚠️ Não consegui extrair conteúdo (<ERR-código>). Link salvo.` |
| Enriquecido | Título + resumo (≤ 900 chars) + teclado inline de triagem |

## Teclado inline de triagem

```json
{
  "inline_keyboard": [
    [
      { "text": "📁 Arquivar",  "callback_data": "triage:<item_id>:archive" },
      { "text": "🚀 SaaS",      "callback_data": "triage:<item_id>:apply_saas" }
    ],
    [
      { "text": "👤 Cliente",   "callback_data": "triage:<item_id>:apply_client" },
      { "text": "🗑 Descartar", "callback_data": "triage:<item_id>:discard" }
    ]
  ]
}
```

- **REQ-T04:** `callback_data` tem limite de 64 bytes na API do Telegram. Formato `triage:<uuid>:<ação>` com UUID (36 chars) + prefixos cabe com folga (~50 bytes); não adicionar campos extras sem verificar o limite.
- **REQ-T05:** ao receber `callback_query`: (1) responder `answerCallbackQuery` imediatamente (senão o cliente mostra loading infinito), (2) aplicar `transition_to!`, (3) editar a mensagem original removendo o teclado e anexando `✔ <decisão>` — evita cliques duplos.
- **REQ-T06:** callback para item já triado => `answerCallbackQuery` com texto "Já triado como <decisão>" e nenhuma transição.

## Desenvolvimento local

Webhook exige HTTPS público. Em `Rails.env.development?`, permitir modo polling (`getUpdates`) via rake task dedicada — proibido em produção (ADR-002).
