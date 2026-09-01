---
item_id: "67670140-3118-4d4a-b688-fd9076ff0da3"
platform: article
external_id: "dacf594cf225"
canonical_url: "https://resend.com/docs/dashboard/domains/tracking"
channel: "Resend"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["resend", "tracking", "open-rate", "click-tracking", "dns", "cname"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend — open e click tracking: subdomínio de tracking, CNAME, como funciona e armadilhas

🔗 https://resend.com/docs/dashboard/domains/tracking

## Resumo

Como ativar rastreamento de abertura e clique no Resend: na aba Configuration do domínio (ou via API) define-se um subdomínio de tracking (ex.: links.emails.exemplo.com), habilita-se abertura e/ou clique e adiciona-se um CNAME no DNS (mais um registro CAA se o domínio tiver CAA, para emitir o certificado TLS). Abertura: pixel GIF 1x1 com referência única. Clique: cada link do HTML é reescrito para o subdomínio de tracking, que registra e redireciona. Armadilhas: ao trocar o subdomínio ficam dois CNAMEs (o antigo inativo é mantido para não quebrar links já enviados — não remover); o subdomínio de tracking pode ser trocado, nunca removido; a troca exige nova verificação.

## Tópicos

- **Ativação** — Configuration → subdomínio de tracking → CNAME (+CAA).
- **Mecânica** — Pixel 1x1 para abertura; links reescritos e redirecionados para clique.
- **Armadilhas** — Dois CNAMEs após troca; nunca remover; nova verificação ao mudar.

## Pontos-chave

- Abertura é imprecisa (bloqueio de imagens) — não decidir por ela.
- Links reescritos podem parecer suspeitos em transacional — deixar tracking só no marketing.
- Remover o CNAME antigo quebra e-mails já enviados.

## Como aplicar

Ativar tracking só no subdomínio de marketing; nunca no de reset de senha (links reescritos + LGPD).

## 🔧 Atlas diz

Peça útil, mas com aviso: tracking troca todos os links do e-mail por links seus — no reset de senha isso cheira a phishing e ainda coleta dado do usuário. Liga no subdomínio de newsletter, deixa o transacional limpo. E o CNAME velho fica: parafuso que não se tira.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

**Configuration**tab or programmatically when you create a new domain or update an existing domain. Once verified, all tracked links in your emails will use your tracking subdomain (e.g.,

`links.emails.example.com`).
- Using the dashboard
- Using the API

Go to the Click 

**Domains**page and click on the domain you want to configure.In the**Configuration**tab, click**Configure**under**Enable tracking metrics**.Provide a name for your tracking subdomain, enable open and/or click tracking, and click**+Add domain**.Add the CNAME record to your DNS settings (e.g. Cloudflare, GoDaddy, etc.) to verify your tracking subdomain.
If we detect CAA records on your domain, we will show an additional CAA record
that needs to be created. This ensures that we can issue a TLS certificate for
your tracking subdomain.

**I’ve added the records**to verify the domain.Once verified, all tracked links in your emails will use your custom tracking subdomain.
### How Open Tracking Works

A 1x1 pixel transparent GIF image is inserted in each email and includes a unique reference to this image file. When the image is downloaded, Resend can tell exactly which message was opened and by whom.
### How Click Tracking Works

To track clicks, Resend modifies each link in the body of the HTML email to point to your tracking subdomain. When recipients clicks a link, the request is redirected to your tracking subdomain, their click event is recorded, and they are redirected to the original URL.
### Troubleshooting

#### Multiple tracking CNAME records

When you change your tracking subdomain, you may see two CNAME records in the DNS Records table: one active and one inactive (shown dimmed). The inactive record is kept intentionally to avoid breaking links in emails that were already sent using the previous subdomain. You do not need to remove it.
#### Changing the Tracking Subdomain

Because tracking subdomains are used in email links, they’re handled differently than other records.
- **Not removable** : After your tracking subdomain has been created, it can only be changed, never removed. This behavior preserves any
email links that may already be sent with the current tracking subdomain. For this reason, do**not remove old tracking DNS records** . (All previously used records remain active and are included in the response.)
- **Requires verification** : After changing the tracking subdomain, a new DNS record must be verified. Until then, the previous value is used.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
