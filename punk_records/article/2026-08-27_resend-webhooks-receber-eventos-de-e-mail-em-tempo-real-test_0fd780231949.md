---
item_id: "23658e41-b7c1-475d-af78-d6e630a7b51b"
platform: article
external_id: "0fd780231949"
canonical_url: "https://resend.com/docs/webhooks/introduction"
channel: "Resend"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["resend", "webhooks", "eventos-de-email", "bounce", "inbound", "observabilidade"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend — webhooks: receber eventos de e-mail em tempo real, testar localmente, retentativas e IPs

🔗 https://resend.com/docs/webhooks/introduction

## Resumo

Webhooks do Resend são requisições HTTPS com payload JSON avisando eventos (entrega, bounce, reclamação, clique, status de assinatura, e-mails recebidos via Inbound). Usos: remover endereços com bounce de listas, alertar em ferramentas de incidente, guardar eventos no próprio banco, receber e-mails. Passos: criar rota POST que responde 200; cadastrar a URL pública no painel (ou API/SDK) escolhendo os eventos; testar disparando um evento; tratar os eventos e publicar em produção; registrar o endpoint de produção. Retentativas quando não há 200: 5 s, 5 min, 30 min, 2 h, 5 h, 10 h. Há lista de IPs de origem para allowlist e a página de tipos de evento com os payloads.

## Tópicos

- **Eventos** — Entrega, bounce, complaint, clique, assinatura, Inbound.
- **Implementação** — Rota POST → 200; cadastrar URL; testar; produção.
- **Retentativas** — 5 s, 5 min, 30 min, 2 h, 5 h, 10 h.
- **Segurança** — IPs para allowlist; verificar assinatura (ver doc).

## Pontos-chave

- Bounce e complaint via webhook devem suspender o envio para aquele endereço no SaaS — proteção de reputação.
- Sem 200 rápido, o Resend retenta por horas: processar assíncrono e responder logo.
- Inbound permite receber e-mail no app (documento por e-mail → pipeline).

## Como aplicar

No SaaS: endpoint /webhooks/resend que marca bounced/complained no usuário; no Vegapunk: Inbound como entrada de documentos por e-mail.

## 🔧 Atlas diz

Webhook é onde o e-mail deixa de ser fogo-e-esquece. Passo 1: rota que responde 200 em milissegundos e joga o evento numa fila. Passo 2: bounce marca o usuário. Passo 3, ideia para o Edison: Inbound do Resend como porta de entrada de documentos no Punk Records.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Resend webhooks

Resend uses webhooks, which are real-time HTTPS requests that tell your application an event occurred, such as an email delivery notification or subscription status update.
### Why use webhooks

All webhooks use HTTPS and deliver a JSON payload that can be used by your application. You can use webhook feeds to do things like:
- Automatically remove bounced email addresses from mailing lists
- Create alerts in your messaging or incident tools based on event types
- Store all send events in your own database for custom reporting/retention
- Receive emails using Inbound

### How to receive webhooks

To receive real-time events in your app via webhooks, follow these steps. Prefer video? Watch the tutorial below.
1

Create a dev endpoint to receive requests

In your local application, create a new route that can accept POST requests.For example, you can add an API route:On receiving an event, respond with an 

pages/api/webhooks.ts

`HTTP 200 OK` to signal to Resend that the event was successfully delivered.
2

Add a webhook in Resend

Navigate to the Webhooks page, then select 

**Add Webhook**.
1. Add your publicly accessible HTTPS URL
2. Select all events you want to observe

Resend also supports managing webhooks via the API or the SDKs. View the API reference for more details.

3

Test your local endpoint

To ensure your endpoint is successfully receiving events, perform an event you are tracking with your webhook, like sending an email, creating a contact, or creating a domain.The webhook will send a JSON payload to your endpoint with the event details. For example:You can also see the webhook details in the dashboard.

View all possible event types and their webhook payload
responses.

4

Update and deploy your production endpoint

Once you successfully receive events, update your endpoint to process the events.For example, update your API route:After you’re done testing, deploy your webhook endpoint to production.

pages/api/webhooks.ts

5

Register your production webhook endpoint

Once your webhook endpoint is deployed to production, you can register it in the Resend dashboard.

### FAQ

### What is the retry schedule?


What is the retry schedule?

If Resend does not receive a 200 response from a webhook server, we will retry the webhooks.Each message is attempted based on the following schedule, where each period is started following the failure of the preceding attempt:

- 5 seconds
- 5 minutes
- 30 minutes
- 2 hours
- 5 hours
- 10 hours

### What IPs do webhooks POST from?


What IPs do webhooks POST from?

If your server requires an allowlist, our webhooks come from the following IP addresses:

- `44.228.126.217`
- `50.112.21.217`
- `52.24.126.164`
- `54.148.139.208`
- `2600:1f24:64:8000::/52`

### What are the delivery guarantees?


What are the delivery guarantees?

Resend webhooks provide 

**at-least-once**delivery. Every event will be delivered to your endpoint at least once, but may be delivered more than once in rare cases (such as network timeouts where your server processed the event but the acknowledgement was lost).To handle duplicates, use the`svix-id` header included with every webhook request. This is a unique identifier for each event delivery. Store processed `svix-id` values and skip any duplicates.
### Do events arrive in order?


Do events arrive in order?

Events are sent as they occur, but 

**delivery order is not guaranteed**. Network conditions, retries, and processing delays can cause events to arrive out of order. For example, an`email.opened` event could arrive before the `email.delivered` event for the same email.If ordering matters for your application, use the `created_at` timestamp in the event payload to sort events after receipt.
### Can I replay webhook events manually?


Can I replay webhook events manually?

Yes. You can replay webhook events manually from the dashboard.You can replay both 

`failed` and `succeeded` events. Replaying successful events is useful when you need to:
- Backfill your system after an outage on your endpoint.
- Reprocess events with updated handler code.
- Send the event to a different endpoint for testing.

### Try it yourself

### Next.js (TypeScript)

See the full source code.

### Next.js (JavaScript)

See the full source code.

### PHP

See the full source code.

### Laravel

See the full source code.

### Python

See the full source code.

### Ruby

See the full source code.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
