---
item_id: "0e971512-13e0-466a-96de-4b41344b8375"
platform: article
external_id: "56588de8ec5c"
canonical_url: "https://resend.com/docs/add-a-domain"
channel: "Resend"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["resend", "dominio", "dns", "dkim", "spf", "dmarc", "entregabilidade"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend — adicionar e verificar um domínio: subdomínio, região, DNS (DKIM/SPF), Return-Path e DMARC

🔗 https://resend.com/docs/add-a-domain

## Resumo

Passo a passo para adicionar e verificar um domínio no Resend (painel, API, CLI ou MCP). Recomendação forte: enviar de um subdomínio (notifications.exemplo.com, updates.exemplo.com) e não do domínio raiz, para isolar reputação; vários subdomínios são permitidos, cada um verificado à parte; domínio já usado por outro time pode ser reivindicado. Escolher a região mais próxima dos destinatários. Return-Path padrão send.exemplo.com, customizável. Copiar exatamente os registros DKIM e SPF (TXT e MX) gerados para o provedor de DNS; verificação costuma sair em 15 minutos, mas pode levar até 72 h; a ferramenta dns.email confere a propagação; botão 'Restart verification' após 72 h. Depois de verificado, adicionar DMARC para proteger contra spoofing e melhorar entregabilidade.

## Tópicos

- **Subdomínio** — Enviar de subdomínio, não da raiz; vários subdomínios por finalidade.
- **Região e Return-Path** — Região mais próxima dos destinatários; Return-Path customizável.
- **DNS** — DKIM e SPF (TXT/MX) copiados exatamente; dns.email para checar; até 72 h.
- **DMARC** — Adicionar após verificar para evitar spoofing.

## Pontos-chave

- Subdomínio separa a reputação do site da reputação dos e-mails.
- Erro de digitação no DNS é a causa clássica de 'pending' eterno — copiar e colar.
- DMARC é o passo que quase todo mundo pula e que mais melhora a caixa de entrada.

## Como aplicar

Para o SaaS e o site do cliente: criar notifications.<dominio> no Registro.br/Hostinger, colar DKIM/SPF, depois DMARC — cruza com os itens de DNS do Registro.br no vault.

## 🔧 Atlas diz

Isso conversa direto com o que o Pythagoras guardou do Registro.br: DNS é onde o e-mail nasce ou morre. Quatro passos: subdomínio, DKIM/SPF copiados sem digitar, esperar, DMARC. Se o status ficar 'pending' por um dia, o erro está no DNS, não no Resend — eu já vi isso mais vezes do que gostaria.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

If you don’t own a domain, please purchase one from a domain registrar such as
Cloudflare or
Namecheap before continuing.

### Add a domain

You can add and verify a domain you own in four ways:
- in the **Domains** Dashboard page
- using the Resend API
- with a Resend CLI command
- with the Resend MCP server

1

In your Resend Dashboard, navigate to the Domains page.

2

Click the Add Domain button.

3

Enter a domain including a subdomain to use for your Resend emails.

We strongly recommend sending emails from a subdomain (e.g., 

`notifications.example.com`) instead of your root domain (`example.com`) to conform to deliverability best practices.Choose a subdomain that reflects the purpose of your emails, such as `customers.example.com` or `updates.example.com`.You can have multiple subdomains associated with your root domain. But, each one must be configured and verified individually.If you add a domain already used by another team, the dashboard will notify you and you can claim the domain to transfer it to your team.
4

Choose a region from the list provided.

Select a region to send your emails from. Choose one that is closest to the majority of your recipients.

5

(optional) Enter a custom subdomain for the Return-Path address if desired.

Return-Path defaults to 

`send.example.com`, although you can provide a custom path.
6

Update your DNS records with values provided by Resend.

View the 

**Records**tab for your domain to find the records to provide to your DNS host provider. Adding these records will verify that you own the domain and have the correct permissions to send and receive emails.Provide the DKIM and SPF configurations (`TXT` and `MX` records) to your DNS provider. These records must match exactly what Resend generated. Copy and paste the records to avoid configuration errors.
7

Wait for DNS verification to complete

When this process is completed correctly, your domain will often verify within 15 minutes of adding the DNS records. However, DNS changes can occasionally take up to 72 hours to propagate globally.You can use Resend’s dns.email tool to check that your records are visible publicly. If verification has not completed after 72 hours, use the “Restart verification” button in the Resend dashboard to trigger a fresh verification check.

8

Add a DMARC record.

After your domain is verified, you can then implement DMARC to build additional trust in your domain and protect against email spoofing.This is an email authentication protocol to verify email senders and to allow receivers to reject unauthenticated messages, and is important for email deliverability.

9

(optional) Update your domain's Resend configuration options.

After your domain is verified, you may wish to enable open and click tracking or enforce Transport Layer Security (TLS).

### Learn more

### Manage domains

View, create, edit, delete, and manage your domains.

### Multi-tenant domain setup

Learn how to configure Resend for SaaS platforms where tenants send emails
from their own domains.

### Next steps

### Add a DMARC record

Implement DMARC to build trust in your domain and protect against email
spoofing.

### Quickstart tutorials

Send your first transactional email with a quick tutorial for your language
or framework.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
