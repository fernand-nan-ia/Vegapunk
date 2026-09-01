---
item_id: "94f4e81b-ee0e-4f09-8e43-9301b07f5456"
platform: article
external_id: "ed6846df51be"
canonical_url: "https://resend.com/docs/dashboard/automations/custom-events"
channel: "Resend"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["resend", "eventos", "automations", "schema", "webhooks"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend — eventos customizados: nome, schema opcional e disparo de múltiplas automações

🔗 https://resend.com/docs/dashboard/automations/custom-events

## Resumo

Página curta sobre Custom Events, os gatilhos das Automations. Na página Events (ou pela API) cria-se um evento com nome (qualquer string; notação com ponto como user.created é convenção recomendada, não obrigatória) e um schema opcional para o payload. Se várias automações habilitadas usam o mesmo nome, todas disparam. Evento fora do schema retorna erro 422 e não é entregue.

## Tópicos

- **Definição** — Nome livre, convenção com ponto; schema opcional.
- **Comportamento** — Mesmo nome dispara todas as automações habilitadas; 422 se violar o schema.

## Pontos-chave

- Definir schema evita disparar automação com dados faltando.
- Um evento pode alimentar várias automações — cuidado com duplicidade de e-mails.

## Como aplicar

Padronizar nomes de evento do SaaS (user.created, payment.failed) e declarar schema para pegar erro cedo.

## 🔧 Atlas diz

Peça de um parafuso só: nome do evento com ponto e schema declarado. O 422 é amigo — melhor falhar na borda do que mandar boas-vindas sem o nome do usuário.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

`422` error and the event is not delivered.
### How it works

- Using the dashboard
- Using the API

The Events page shows all existing events. Click 

**Add event**to create a new event.Enter the event name and optional schema to define the event payload you will send with the event.When you’re done,**Save**the event.
The event name can be any string (e.g., 

`user.created`, `welcome`,
`my-custom-event`). Dot notation is a recommended convention but is not
required. If multiple enabled automations use the same event name, all of
them will be triggered.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
