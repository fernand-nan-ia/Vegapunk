---
item_id: "652ca85f-8c9a-4453-ac24-ed83cf2af5bc"
platform: article
external_id: "a3f11566dbf6"
canonical_url: "https://resend.com/docs/cli"
channel: "Resend"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["resend", "cli", "automacao", "scripts", "terminal"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend CLI — instalação, login/perfis e comandos (emails, batch, domínios, contatos, templates, logs, webhooks)

🔗 https://resend.com/docs/cli

## Resumo

A CLI do Resend instala-se via cURL, npm, Homebrew ou PowerShell. Autenticação por cadeia de prioridade (flag --key, login salvo, variáveis); resend login valida e guarda a chave; logout; perfis para múltiplos times (--profile). Comandos: emails send (flags ou interativo; --template dispensa campos), emails batch a partir de JSON (até 100, com scheduled_at em linguagem natural ou ISO e tags; sem anexos), recebimento de e-mails (inbound, anexos, stream), domínios, chaves de API, broadcasts, contatos (importação assíncrona de CSV com --column-map), propriedades de contato, segmentos, tópicos, supressões, templates, logs e webhooks.

## Tópicos

- **Instalação e auth** — cURL/npm/brew/PowerShell; login com chave validada; perfis.
- **E-mails** — send interativo ou por flags; batch de JSON com scheduled_at e tags.
- **Demais** — Inbound, domínios, chaves, broadcasts, contatos/CSV, segmentos, templates, logs, webhooks.

## Pontos-chave

- Scripts de operação (ex.: reenviar boletos) podem ser shell + CLI, sem código.
- scheduled_at aceita 'tomorrow 9am'.
- Import de CSV é assíncrono — checar status com imports get.

## Como aplicar

Testar o envio do SaaS pelo terminal antes de codar; scripts de manutenção com a CLI.

## 🔧 Atlas diz

CLI é a chave de fenda de bolso: testa o domínio, manda um e-mail de teste, vê o log — sem abrir editor. Eu uso antes de soldar qualquer SDK.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Installation

- cURL
- npm
- Homebrew
- PowerShell (Windows)

### Authentication

The CLI resolves your API key using the following priority chain:
If no key is found from any source, the CLI errors with code 

`auth_error`.
**Authenticate by storing your API key locally. The key is validated against the Resend API before being saved.**

`resend login``--key` flag:
**Remove your saved API key.**

`resend logout`
**Switch between profiles**If you work across multiple Resend teams or accounts, switch between profiles without logging in and out:

`--profile` flag on any command to run it with a specific profile:
### Emails

Send, retrieve, cancel, and manage email delivery.
**Send an email. Provide all options via flags for scripting, or let the CLI prompt interactively for missing fields.**

`resend emails send`
* Not required when using 

`--template`, which provides them.
**Examples:**

**Send up to 100 emails in a single API request from a JSON file.**

`resend emails batch`
Each email in the JSON array supports the same fields as 

`resend emails send`, including per-email `scheduled_at` (natural language or ISO 8601) and `tags`. The `attachments` field is not supported in batch sends.
emails.json

**Other email commands**

### Receiving

Process inbound emails, download attachments, and stream incoming messages.
### Domains

Manage your sending and receiving domains.
### API Keys

Create, list, and revoke API keys for programmatic access.
### Broadcasts

Create and send broadcast emails to segments.
### Contacts

Manage contacts, segment membership, and topic subscriptions.
**Start an asynchronous CSV import. The command uploads the file and returns a contact import ID immediately. Use**

`resend contacts imports create``resend contacts imports get <id>` to check
processing status.
Without 

`--column-map`, CSV headers must match the lowercase contact field
names exactly: `email`, `first_name`, and `last_name`. Use `--column-map` when
your CSV uses headers like `Email` or `First Name`.
**Retrieve a contact import by ID, including status and row counts.**

`resend contacts imports get`
**List contact imports. The default limit is**

`resend contacts imports list``10`.
### Contact Properties

Define custom properties to store additional data on contacts.
### Segments

Group contacts into targetable segments for broadcasts.
### Topics

Manage subscription topics that contacts can opt in or out of.
### Suppressions

Manage the suppression list.
### Templates

Create and manage email templates.
### Logs

View API request logs.
### Webhooks

Register endpoints and listen for email event notifications.
**Register a webhook endpoint.**

`resend webhooks create`
**Listen for webhook events locally during development. Starts a server, registers a temporary webhook, streams events, and cleans up on exit.**

`resend webhooks listen`
See the webhook events documentation for the full
list of available event types. For agent-specific webhook patterns, see CLI
for AI Agents.

**Other webhook commands**

### Automations

Create, manage, and monitor event-driven automation workflows.
**Create a new automation from a JSON file describing the workflow graph.**

`resend automations create`
* Provide 

`--file`, or `--name` with `--steps` and `--connections`. When using `--file`, other flags override file values.
**Other automation commands**

**Automation runs**

### Events

Define and send events that trigger automations.
**Send an event to trigger matching automations for a contact.**

`resend events send`
**Other event commands**

### Utility

Diagnose your setup, manage authentication, and configure shell completions.
**Run environment diagnostics. Verifies your CLI version, API key, credential storage, and domain status.**

`resend doctor``0` when all checks pass or warn. Exits `1` if any check fails.
**Other utility commands**

### Global options

These flags work on every command:
### Output behavior

The CLI has two output modes that switch automatically:
Pipe to another command and JSON output activates:

`1` and output structured JSON:
### CI/CD

Set`RESEND_API_KEY` as an environment variable, with no `resend login` needed:
### Configuration

### Using the CLI with AI Agents

Learn about Agent Skills, non-interactive mode, and local webhook development
for AI agents.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
