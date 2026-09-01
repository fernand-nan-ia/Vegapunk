---
item_id: "94260cf4-653c-4bab-8a04-7a015b529aa6"
platform: article
external_id: "a71249354370"
canonical_url: "https://resend.com/docs/dashboard/domains/introduction"
channel: "Resend"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["resend", "dominio", "subdominio", "reputacao", "dmarc", "bimi", "tls"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend — domínios verificados: por que subdomínios, tracking, TLS forçado, região, DMARC e BIMI

🔗 https://resend.com/docs/dashboard/domains/introduction

## Resumo

Conceito de domínio verificado no Resend: só se envia de domínio próprio (nunca compartilhado); é preciso verificar ao menos um; opcionalmente configurar recebimento. Recursos ao adicionar: usar subdomínio para segmentar reputação e comunicar intenção; abrir/click tracking; TLS forçado (só envia criptografado); Return-Path customizado; região geográfica; enviar e receber em qualquer endereço do domínio sem configuração extra; DMARC e BIMI para confiança e inbox placement. Recomenda-se vários subdomínios por finalidade — ex.: newsletter com tracking e transacional (reset de senha) sem tracking.

## Tópicos

- **Regra** — Só domínio próprio; ao menos um verificado.
- **Subdomínios** — Um por finalidade para isolar reputação.
- **Opções** — Tracking, TLS forçado, Return-Path, região, DMARC, BIMI.

## Pontos-chave

- Reset de senha sem tracking: privacidade e entregabilidade.
- Newsletter em subdomínio próprio: se queimar, não derruba o transacional.
- BIMI mostra o logo na caixa de entrada — exige DMARC rígido.

## Como aplicar

Dois subdomínios para o SaaS: account.<dominio> (transacional, sem tracking) e news.<dominio> (marketing, com tracking).

## 🔧 Atlas diz

Regra de engenharia: separar cargas. Transacional e marketing em subdomínios diferentes é o mesmo que não pendurar o lustre na viga do telhado. Se a newsletter cair em spam, o reset de senha continua chegando.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Verified domains

Resend sends emails using a domain you own (i.e., not a shared or public domain). You must add and verify at least one domain to send emails with Resend. You can optionally configure your domain to receive emails.
### Domain features

When you add a domain, you can choose to:
- Add a subdomain instead of your root domain to communicate the kind of emails you send and receive, and for proper reputation segmentation.
- Enable open and click tracking for your emails.
- Configure Enforced Transport Layer Security (TLS) to ensure that you only send encrypted emails.
- Set a custom subdomain for the Return-Path address.
- Choose which geographical region to send emails from to reach your recipients sooner.

- Send and receive emails using any email address at your domain without any extra configuration.
- Implement DMARC and BIMI to build trust and improve inbox placement.

### Subdomains

We recommend sending your emails from one or more subdomains (e.g.,`updates.example.com`) instead of your root domain to isolate your sending reputation and to clearly communicate your intent to your recipients.
You can add and verify multiple subdomains of the same domain (e.g. `newsletter.example.com` and `account.example.com`) for different sending purposes.
For example, you can configure your newsletter for open and click tracking while keeping tracking disabled for your important transactional emails such as password resets.
Learn more about the benefits of sending emails from a subdomain.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
