---
item_id: "7dbbbd52-53f4-41e4-86ca-04a4e5bd5611"
platform: article
external_id: "2791bb5fe7ab"
canonical_url: "https://resend.com/docs/mcp-server"
channel: "Resend"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["resend", "mcp", "claude-code", "agentes", "automacao"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend MCP Server — remoto (OAuth/Bearer) e local (npx, stdio/HTTP): opções e ferramentas para agentes

🔗 https://resend.com/docs/mcp-server

## Resumo

O Resend hospeda um servidor MCP remoto integrável a Claude Code (/mcp → resend, OAuth; plugin traz skills), Claude, Cursor, Codex, Antigravity, Copilot, Windsurf e Warp; em ambientes sem navegador (servidor, CI, agente headless) usa-se a chave de API como Bearer. Versão local open-source (npm resend-mcp) via npx com transporte stdio (padrão) ou HTTP (porta 3000/MCP_PORT, Bearer por cliente). Opções: --key, --sender (remetente padrão de domínio verificado), --reply-to, --http, --port; variáveis RESEND_API_KEY, SENDER_EMAIL_ADDRESS, REPLY_TO_EMAIL_ADDRESSES, MCP_PORT. Sem remetente padrão, o servidor pergunta a cada chamada. Ferramentas cobrem a plataforma inteira (e-mails, domínios, contatos etc.) em linguagem natural.

## Tópicos

- **Remoto** — OAuth em Claude Code/Cursor/etc.; Bearer em headless.
- **Local** — npx resend-mcp; stdio ou HTTP; --sender/--reply-to; variáveis de ambiente.
- **Ferramentas** — Plataforma inteira via MCP.

## Pontos-chave

- Claude Code pode enviar e-mails e gerir domínios do Resend com /mcp — inclusive relatórios do Vegapunk.
- Em servidor/CI, Bearer com chave 'só envio'.
- Definir --sender evita o servidor perguntar o remetente toda vez.

## Como aplicar

Instalar o MCP do Resend no Claude Code com chave 'só envio' e sender do subdomínio: York manda o relatório de custo por e-mail, Stella o checkpoint.

## 🔧 Atlas diz

Isso conecta com a nossa bancada: MCP local via npx, chave só de envio, sender fixo — e a York passa a mandar o relatório por e-mail sem eu escrever cliente nenhum. Aviso de segurança: em CI é Bearer, e Bearer é senha; trata como .env.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Remote MCP Server

Resend hosts the MCP server at:
- Claude Code
- Claude
- Cursor
- Codex
- Antigravity
- Copilot
- Windsurf
- Warp

`/mcp` in Claude Code and select **resend**to complete the OAuth login. The plugin bundles the MCP server and every Resend skill.

*If your client runs somewhere a browser login isn’t possible*(a server, CI, or a headless agent), pass a Resend API key as a Bearer token instead of using OAuth.

- Claude Code
- JSON config

### Local MCP Server

The hosted server runs the same open-source code that’s available on NPM as`resend-mcp`. If you prefer to run the server yourself, you can integrate it into any supported MCP client using `npx`. You’ll need to:
The local server supports two transport modes: **stdio**(default) and

**HTTP**. Choose your preferred mode and client below to get started. Remember to replace

`re_xxxxxxxxx` with your actual API key.
#### Stdio Transport (Default)

- Claude Code
- Codex
- Antigravity
- Cursor
- Claude Desktop
- Copilot
- Gemini CLI
- OpenCode
- Windsurf
- Warp
- Devin

#### HTTP Transport

Run the server over HTTP for remote or web-based integrations. In HTTP mode, each client authenticates by passing their Resend API key as a Bearer token in the`Authorization` header.
Start the server:
`http://127.0.0.1:3000` and expose the MCP endpoint at `/mcp` using Streamable HTTP.
- Claude Code
- Cursor

`MCP_PORT` environment variable:
#### Options

You can pass additional arguments to configure the local server:
- `--key` : Your Resend API key (stdio mode only, since HTTP mode uses the Bearer token from the client)
- `--sender` : Default sender email address from a verified domain
- `--reply-to` : Default reply-to email address (can be specified multiple times)
- `--http` : Use HTTP transport instead of stdio (default: stdio)
- `--port` : HTTP port when using`--http` (default: 3000, or`MCP_PORT` env var)

**Environment variables:**

- `RESEND_API_KEY` : Your Resend API key (required for stdio, optional for HTTP since clients pass it via Bearer token)
- `SENDER_EMAIL_ADDRESS` : Default sender email address from a verified domain (optional)
- `REPLY_TO_EMAIL_ADDRESSES` : Comma-separated reply-to email addresses (optional)
- `MCP_PORT` : HTTP port when using`--http` (optional)

If you don’t provide a sender email address, the MCP server will ask you to
provide one each time you call the tool.

### MCP Server tools

Resend’s MCP server gives your AI agent native access to the full Resend platform through a single integration. You can manage all aspects of your email infrastructure using natural language.
- **Emails** : Send, list, get, cancel, update, and batch send emails. Supports HTML, plain text, attachments (local file, URL, or base64), CC/BCC, reply-to, scheduling, tags, and topic-based sending.
- **Received Emails** : List and read inbound emails. List and download received email attachments.
- **Templates** : Create, list, get, update, publish, duplicate, and remove email templates. Supports composing template content and`{{{VARIABLE}}}` placeholders.
- **Contacts** : Create, list, get, update, and remove contacts. Manage segment memberships, topic subscriptions, and CSV contact imports. Supports custom contact properties.
- **Broadcasts** : Create, send, list, get, update, and remove broadcast campaigns. Supports scheduling, personalization placeholders, and preview text.
- **Automations** : Create, list, get, update, duplicate, and remove automations. Review the runs of an automation.
- **Events** : Send events to trigger automations for a contact. Create, update, and remove event definitions.
- **Domains** : Create, list, get, update, remove, and verify sender domains. Configure tracking, TLS, and sending/receiving capabilities. Create and verify domain claims.
- **Segments** : Create, list, get, and remove audience segments.
- **Topics** : Create, list, get, update, and remove subscription topics.
- **Contact Properties** : Create, list, get, update, and remove custom contact attributes.
- **API Keys** : Create, list, and remove API keys.
- **Webhooks** : Create, list, get, update, and remove webhooks for event notifications.
- **Logs** : List and inspect API request logs, including full request and response bodies.
- **Editor** : Connect to (and disconnect from) the visual editor in the Resend dashboard, and read a draft’s content while collaborating on broadcasts and templates.

- Turn a Paper design into a ready-to-send Template or Broadcast
- Bulk import contacts from a CSV, upserting or skipping duplicates, and organize them into Segments
- Build Automations that send emails when a contact is created, updated, or triggers a custom event
- Read and triage inbound email, download attachments, and send replies
- Schedule, reschedule, and cancel scheduled emails
- Debug failed API requests by inspecting the request logs

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
