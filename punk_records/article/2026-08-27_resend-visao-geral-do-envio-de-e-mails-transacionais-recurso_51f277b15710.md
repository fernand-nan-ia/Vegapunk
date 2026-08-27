---
item_id: "f77c00cf-17c6-4008-9537-d3f70fc3d3e4"
platform: article
external_id: "51f277b15710"
canonical_url: "https://resend.com/docs/dashboard/emails/introduction"
channel: "Resend"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["resend", "email-transacional", "api", "sdk", "smtp", "mcp"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend — visão geral do envio de e-mails transacionais (recursos e formas de integrar)

🔗 https://resend.com/docs/dashboard/emails/introduction

## Resumo

Página de abertura da seção de envio da documentação do Resend. E-mails transacionais são os disparados por eventos do app: confirmação de pedido, reset de senha, notificações de conta. Recursos: enviar, consultar, cancelar e gerenciar e-mails individuais ou em lote pela API, SDKs, CLI, automações e ferramentas de IA; painel de e-mails enviados; agendamento para data futura; anexos e imagens embutidas; cabeçalhos customizados; chaves de idempotência para garantir envio único; insights de entregabilidade por e-mail; logs de API e métricas. Formas de integrar: SDK da linguagem, integrações com frameworks, API crua (cURL), CLI, MCP (para agentes) e SMTP sem dependências.

## Tópicos

- **Casos de uso** — Confirmação de pedido, reset de senha, notificações de conta.
- **Recursos** — Lote, agendamento, anexos/inline, headers, idempotência, insights de entregabilidade, logs.
- **Formas de integrar** — SDK, integrações, API, CLI, MCP, SMTP.

## Pontos-chave

- Idempotência nativa evita e-mail duplicado em retry — usar sempre em eventos críticos.
- SMTP existe para quem não quer dependência de SDK.
- MCP permite que um agente (Claude Code) envie e gerencie e-mails.

## Como aplicar

Ponto de partida para o SaaS: reset de senha e notificações via SDK Python; para o Vegapunk, o MCP pode mandar relatórios por e-mail.

## 🔧 Atlas diz

Passo 1 de 22, chefe: o mapa da bancada. Três parafusos que eu já marco: idempotência (nunca mandar o mesmo e-mail duas vezes num retry), agendamento (sem cron seu) e SMTP como plano B. O resto é detalhe que vem nas próximas peças.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Sending transactional emails

Resend provides all the tools you need to send transactional emails from your application. These are useful for:
- order confirmations
- password reset emails
- account notifications

### Sending Features

With Resend’s email sending features, you can:
- Send, retrieve, cancel, and manage individual and transactional email delivery through the Sending API and SDKs, CLI commands, automations, and AI building tools.
- View and manage all sent emails in the Emails Dashboard page.
- Send single or batch transactional emails.
- Schedule emails to be sent at a future date.
- Send emails with attachments and embedded images.
- Include custom headers in your emails.
- Use idempotency keys to ensure emails are sent only once.
- Receive tailored deliverability insights about each email with suggestions for improvement.
- View API endpoint logs and deliverability metrics for monitoring and troubleshooting.

### Quickstart

Get started with a quick setup sending example for your language or an AI builder guide to see how to incorporate Resend into your application.
### Choose your infrastructure

To send transactional emails from your application, you can use a variety of tools:
- SDK: send with an SDK built for your language
- Integrations: send from a framework or tool you already use
- API: send with raw cURL calls
- CLI: send emails from the terminal
- MCP: send through your agent with MCP (see also skills)
- SMTP: send without external dependencies

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
