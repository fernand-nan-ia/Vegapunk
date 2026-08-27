---
item_id: "5d4d066f-3da5-4c00-bf93-68daa3df4239"
platform: article
external_id: "d1be3efca69b"
canonical_url: "https://resend.com/docs/create-an-api-key"
channel: "Resend"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["resend", "api-key", "seguranca", "variaveis-de-ambiente", "boas-praticas"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend — criar uma chave de API: permissões, restrição por domínio e uso via variável de ambiente

🔗 https://resend.com/docs/create-an-api-key

## Resumo

Como criar e usar chaves de API no Resend. A chave autentica as requisições e pode ser criada pelo painel, pela API, pela CLI ou pelo servidor MCP. No painel: nome (até 50 caracteres), permissão 'Sending access' (só enviar) ou acesso total (criar, apagar, ler e atualizar qualquer recurso), com opção de restringir o envio a um domínio específico; a permissão pode ser alterada depois. A chave só é exibida uma vez. Uso: guardar em variável de ambiente (.env) e passar explicitamente ao construir o cliente (ex.: process.env.RESEND_API_KEY em Node; Node 20+ aceita --env-file=.env). Links para gestão de chaves, boas práticas e o próximo passo: adicionar um domínio.

## Tópicos

- **Onde criar** — Painel, API, CLI ou MCP.
- **Permissões** — Sending access (só envio, opcionalmente restrito a um domínio) ou acesso total; editável depois.
- **Uso no código** — Variável de ambiente; passar ao construtor; nunca no repositório.

## Pontos-chave

- Uma chave 'só envio' restrita ao domínio limita o estrago se vazar.
- A chave só é mostrada uma vez — guardar no .env na hora.
- Chave de acesso total só para administração, nunca no app em produção.

## Como aplicar

No SaaS: chave 'Sending access' restrita ao subdomínio de envio, no .env do servidor; chave total só na sua máquina para configurar.

## 🔧 Atlas diz

Regra da bancada, igual à do nosso .env: chave só de envio, presa a um domínio, fora do repositório. Se vazar, o pior que acontece é alguém mandar e-mail no seu nome — ruim, mas não apaga nada. Chave total fica com você, nunca no container.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Resend API keys

API Keys are secret tokens used to authenticate your requests. They are unique to your account and must be kept confidential. You must create at least one API key to use the Resend platform through code (e.g., SDKs, API, command-line interface (CLI), or AI tools).
### Create an API Key

You can create API keys in four ways:
- in the **API keys** Dashboard page
- using the Resend API
- with a Resend CLI command
- with the Resend MCP server

1

In your Resend Dashboard, navigate to the API keys page.

2

Click the Create API Key button.

3

Provide a name for your API Key.

Choose a name (maximum 50 characters) to identify your key.

4

Select a permission for your API key.

Choose 

**“Sending access”**to grant access to only sending emails unless your key needs full access to Resend’s API to create, delete, get, and update any resource.This API key permission can be updated at any time.
5

(Optional) Restrict sending to a specific domain

If you selected 

**“Sending access”**, you can further choose the domain you want to restrict access to.
For security reasons, you can only view the API Key once. Learn more about
API key best practices.

### Use the API key in your code

Authenticate your requests by adding your Resend API key to your project as an environment variable. You can check the quickstart guides or AI builder guides for specific examples of passing your API key to your project.
1

Create and store an environment variable

Store your API key as an environment variable in your project. This is commonly done inside a special file or configuration panel and will depend on your language, framework, or development platform.For example, Node.js projects commonly store both public and secret variables in a 

`.env` file at the root of your project:
.env

2

Pass the environment variable to your code

Your project environment variables are not automatically available to Resend. You must explicitly pass your API key value to your Resend code.For example, whenever you create a new Resend instance in a Node.js project, you must pass the environment variable on 

`process.env`:
app.ts

On Node.js 

`v20` and later, you can pass your `.env` file’s variables to your script using the `--env-file=.env` flag. Alternatively, you can use the `dotenv` package to load the variables.
### Learn more

### Manage API keys

View, create, edit, delete, and manage your API keys.

### API key best practices

Learn about best practices for managing your API keys.

### Next steps

### Add a domain

Add and verify a domain you own to start sending emails.

### Quickstart tutorials

Send your first transactional email with a quick tutorial for your language
or framework.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
