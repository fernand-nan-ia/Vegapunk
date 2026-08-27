---
item_id: "6af5c94d-1228-4dcb-8029-d8053bab0120"
platform: article
external_id: "ef20b9a5b602"
canonical_url: "https://resend.com/docs/dashboard/emails/batch-sending"
channel: "Resend"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["resend", "batch", "email-transacional", "api", "limites"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend — envio em lote: até 100 e-mails por chamada, resposta indexada e limitações

🔗 https://resend.com/docs/dashboard/emails/batch-sending

## Resumo

Batch sending: até 100 e-mails transacionais numa única chamada, cada um com destinatário, assunto e conteúdo próprios — para confirmações de pedido, notificações e para reduzir chamadas de API. Para marketing, usar Broadcasts. A resposta traz um array de IDs na mesma ordem do payload; se qualquer e-mail for inválido, a requisição inteira falha com erro. Limitações: máximo 100 por lote, anexos não suportados, processamento independente por e-mail. No painel, e-mails de lote entram como queued antes de processar.

## Tópicos

- **Quando usar** — Muitos transacionais de uma vez; menos chamadas.
- **Resposta** — IDs na ordem do payload.
- **Limites** — 100 por lote; sem attachments; erro em um invalida todos.

## Pontos-chave

- Validar todos os e-mails antes de montar o lote — um errado cancela os 100.
- Anexo obriga envio individual.
- Lote aparece como queued primeiro.

## Como aplicar

Notificações diárias do SaaS para muitos usuários: montar lotes de 100, validar antes, e guardar os IDs retornados por índice.

## 🔧 Atlas diz

Lote de 100 com regra dura: um endereço torto e os 100 voltam. Passo 1: validar. Passo 2: mandar. Passo 3: guardar o ID de cada um pelo índice. Anexo? Envio solto. Simples e sem surpresa.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### When to use batch sending

Use batch sending when you need to:
- Send multiple transactional emails (e.g., order confirmations and notifications)
- Trigger emails to different recipients with unique content
- Reduce the number of API calls to improve performance

For marketing campaigns, use our no-code editor,
Broadcasts, instead.

### Send batch emails

You can send up to 100 emails in a single API call using the batch endpoint. Each email in the batch can have different recipients, subjects, and content.
### Response format

The batch endpoint returns an array of email IDs for successfully created emails. When the request succeeds, each entry in`data` corresponds to the email at the same index in the batch payload (0-based). The first email in your request will be the first entry in `data`, and so on.
`error` object with a `message` property. You can find more information about the error in the Errors section of the API Reference.
### Limitations

When using batch sending, keep in mind:
- Maximum of **100 emails** per batch request
- The `attachments` field is not supported yet
- Each email in the batch is processed independently
- The request will fail and return an error if any email in your payload is invalid (for example, required fields are missing or fields contain invalid data).

### View batch emails

All emails sent via the batch endpoint appear in the Emails page of your dashboard along with individually sent emails. Each email will have a`queued` status initially before being processed.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
