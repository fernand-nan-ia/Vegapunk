---
item_id: "4cf3e9fc-fcd6-4c5a-b9fd-dbb146448e89"
platform: article
external_id: "26c3e750d75f"
canonical_url: "https://resend.com/docs/dashboard/logs/introduction"
channel: "Resend"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["resend", "logs", "observabilidade", "debug", "api"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend — logs de API: filtros por status, detalhes de requisição/resposta e 'Help me fix'

🔗 https://resend.com/docs/dashboard/logs/introduction

## Resumo

Os logs do Resend registram cada chamada à API (painel ou API): endpoint, status HTTP, método e horário. Busca por texto e filtros por status (sucessos 2xx, erros 4xx/5xx, códigos específicos), intervalo de datas, user agent (SDK) e chave de API. Detalhe de um log: corpo da requisição e da resposta (copiáveis), método, endpoint, user-agent com detecção automática de SDK e versão (com aviso de atualização). Logs ligados a e-mails apontam para o registro do e-mail e vice-versa, permitindo rastrear do request à entrega. Para erros suportados há um botão 'Help me fix' com resposta bruta, guia passo a passo e links.

## Tópicos

- **O que é registrado** — Endpoint, status, método, horário, request/response body, SDK.
- **Filtros** — Status, código, período, user agent, chave de API.
- **Rastreabilidade** — Log ↔ e-mail nos dois sentidos.
- **Diagnóstico** — Botão Help me fix com guia.

## Pontos-chave

- Log liga a chamada ao e-mail e o e-mail à chamada — debug de 'mandei mas não chegou' começa aqui.
- Filtrar por chave de API mostra se o SaaS ou o cliente está gerando erro.
- SDK desatualizado aparece como aviso no log.

## Como aplicar

Quando Lilith fizer *break no envio de e-mail do SaaS, os logs do Resend são a evidência: status e corpo por chamada.

## 🔧 Atlas diz

Log que liga request a entrega é o que eu peço para todo serviço e quase nenhum dá. Quando o Fernando disser 'o e-mail não chegou', o caminho é: log → e-mail → evento. Guardado como referência de debug.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Overview

Logs are a powerful tool for monitoring activity and troubleshooting issues.
- Using the dashboard
- Using the API

Access your logs from the Logs page in the dashboard.Each log entry shows:

- **Endpoint** - The API endpoint called (e.g.,`/domains` ,`/api-keys` ,`/contacts` )
- **Status** - The HTTP response status code (200, 201, etc.)
- **Method** - The HTTP method used (GET, POST, DELETE, etc.)
- **Created** - When the request was made (displayed as relative time)

### Searching Logs

Use the search bar to find specific logs. This is useful when tracking down a particular request or debugging an issue.
### Filtering Logs

Filter logs by response status to quickly identify issues:
- **All Statuses** - View all logs
- **Successes** - Show only successful requests (2xx status codes)
- **Errors** - Show only failed requests (4xx and 5xx status codes)
- **Specific codes** - Select one or more specific HTTP status codes (200, 201, 403, 429, etc.)

- **Date range** - Adjust the time period for logs (e.g., Last 15 days)
- **User Agents** - Filter by SDK or client
- **API Keys** - Filter by specific API key

### Log details

Click any log entry to view complete details.
#### Request information

- **Request body** - The full JSON payload sent to the API (with copyable code blocks)
- **HTTP method** - GET, POST, etc.
- **Endpoint** - The API endpoint called
- **User-Agent** - The client or SDK used, with automatic SDK detection showing name and version

#### Response information

- **Response body** - The complete API response (with copyable code blocks)
- **Status code** - The HTTP status code returned
- **Timestamp** - When the request was processed

#### Related emails

When a log entry is associated with one or more email sends, an Email field appears in the log details, linking directly to the corresponding email records. The corresponding email’s detail page includes a Log field linking to the API request log that triggered it, so you can trace the full request-to-delivery flow in both directions.
#### SDK detection

The dashboard automatically detects and displays Resend SDK information from the User-Agent header, showing:
- SDK name (e.g., “Resend Node.js”)
- Version number
- Update notification when a newer SDK version is available

### Troubleshooting errors

For supported error types, click the**Help me fix**button to open a troubleshooting drawer.The drawer includes:
- **Raw response** - The complete API response
- **Detailed guidance** - Step-by-step instructions to resolve the issue
- **Relevant links** - Documentation and knowledge base articles
- **Contextual information** - Your current rate limits, verified domains, and other relevant data

### Copy for AI

For error logs (4xx and 5xx status codes), use the**Copy for AI**dropdown to get help debugging:
- **Copy log** - Copy the log details as Markdown formatted for AI tools
- **Open in ChatGPT** - Open ChatGPT with the log prefilled for analysis
- **Open in Claude** - Open Claude with the log prefilled for analysis

View a comprehensive list of error codes and their meanings in the Resend API
Reference.

### Export your data

Admins can download your data in CSV format for the following resources:
- Emails
- Broadcasts
- Contacts
- Segments
- Domains
- Logs
- API keys

Currently, exports are limited to admin users of your team.

All exports your team creates are listed in the
Exports page under 

**Settings**>**Team**>**Exports**. Select any export to view its details page. All members of your team can view your exports, but only admins can download the data.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
