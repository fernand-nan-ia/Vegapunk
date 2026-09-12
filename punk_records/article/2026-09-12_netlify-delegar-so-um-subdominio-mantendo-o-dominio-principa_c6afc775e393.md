---
item_id: "b292fbf0-be67-4e32-a227-1714496ce8db"
platform: article
external_id: "c6afc775e393"
canonical_url: "https://docs.netlify.com/manage/domains/configure-domains/delegate-a-standalone-subdomain"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: archived
triage: archive
tags: ["netlify-dns", "subdominio-autonomo", "registro-ns", "delegacao-de-subdominio", "ssl-wildcard"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Netlify — delegar só um subdomínio, mantendo o domínio principal onde está

🔗 https://docs.netlify.com/manage/domains/configure-domains/delegate-a-standalone-subdomain

## Resumo

Como levar apenas um subdomínio para o Netlify DNS sem mover o domínio apex, por exemplo delegar docs.exemplo.com mantendo exemplo.com no registrador atual. O subdomínio delegado ganha certificado wildcard automático cobrindo também os subdomínios dele, subdomínios por branch como staging.docs.exemplo.com, suporte a IPv6 ativável pelo painel e entrega pelo CDN global da Netlify. A condição externa é que o registrador do domínio apex suporte registros NS para subdomínio, porque é lá que se apontam os name servers do subdomínio para a Netlify. Quando o apex já está no Netlify DNS, os subdomínios são gerenciados automaticamente e nada disso é necessário. Há dois pontos de partida na interface: a página Domains da equipe, que permite esperar a propagação antes de ligar o subdomínio ao site, ou a configuração de domínio do próprio site.

## Tópicos

- **O que o subdomínio delegado ganha** — Certificado wildcard automático, subdomínios por branch, IPv6 ativável e entrega pelo CDN global.
- **A condição externa** — O registrador do domínio apex precisa suportar registros NS para subdomínio, que é onde se aponta para a Netlify.
- **Quando não é preciso** — Se o apex já está no Netlify DNS, os subdomínios são gerenciados automaticamente.

## Ferramentas citadas

- **Netlify**: plataforma de hospedagem e DNS descrita no documento

## Pontos-chave

- É a saída para usar recursos de DNS da Netlify sem tocar no domínio principal do cliente.
- Depende de o registrador do apex aceitar NS para subdomínio, o que nem todos aceitam.
- O certificado wildcard cobre também os subdomínios do subdomínio delegado.
- Delegar pela página Domains da equipe permite esperar a propagação antes de ligar ao site.

## Como aplicar

Solução elegante para cliente que não deixa mexer no domínio: você delega só site.empresa.com.br ou loja.empresa.com.br, ganha SSL automático, e o DNS principal dele continua exatamente como está. Confirme antes se o registrador dele aceita NS de subdomínio.

## 📚 Pythagoras diz

Esta é a peça que faltava para o caso do cliente arisco: leva só o subdomínio, deixa o domínio dele intacto, e ninguém precisa confiar em ninguém. A condição é o registrador aceitar NS de subdomínio — cheque antes de prometer.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

You can bring just a subdomain to Netlify DNS and keep your apex domain on a separate domain registrar. This makes all the benefits of Netlify DNS available to your subdomain, including automated wildcard SSL certificates and expanded use cases for your site with branch subdomains.

For example, you can delegate `docs.example.com` to Netlify DNS and keep `example.com` on a different domain registrar.

If you delegate the stand-alone subdomain `docs.example.com` to Netlify DNS, your site gains these advantages:

- **Automatic site security benefits.** Netlify DNS provisions your subdomain, and all subdomains of your subdomain, with wildcard SSL certificates.
- **More use cases with branch subdomains.** Your site can serve different content from different branches using branch subdomains. For example, the`staging` branch of your site can serve unique content at`staging.docs.example.com` . Likewise, your site’s`beta` branch can serve unique content at`beta.docs.example.com` .
- **Wider reach with IPv6 support.** Your subdomain can reach a wider audience with IPv6, which you can enable for your subdomain in the Netlify UI.
- **Performance gains with the Netlify CDN.** Your site will be served from our global CDN, from the server closest to your site visitors. Between this and CDN-level routing, sites will often gain a performance boost from being served on the Netlify CDN.

### Netlify DNS support for subdomains and apex domains

Section titled “Netlify DNS support for subdomains and apex domains”
When you add an apex domain to Netlify DNS, subdomains of this apex domain are managed by Netlify DNS automatically.

If you delegate a stand-alone subdomain to Netlify DNS, additional configuration is required outside of Netlify. You will need to access the domain registrar for the related apex domain to set NS records (Name Server records for your subdomain.

For example, if you’ve already added the apex domain `petsofnetlify.com` to Netlify DNS and you add the subdomain `rover.petsofnetlify.com` to your site on Netlify, then Netlify DNS will automatically manage this subdomain for you.

Alternatively, if you have an apex domain that is already managed by an external domain registrar, such as `example.com`, and you want to bring just the subdomain `docs.example.com` to Netlify DNS, then you need to follow the steps below.

### Delegate a stand-alone subdomain to Netlify DNS

Section titled “Delegate a stand-alone subdomain to Netlify DNS”
There are two main starting places in the Netlify UI to delegate just a subdomain to Netlify DNS:

- **From your team’s Domains page:** If you have access to your team’s**Domains** page, then you can delegate a subdomain to Netlify DNS for your team and use this subdomain for one of your team’s sites. This flow allows you to wait for DNS propagation to complete before adding this subdomain to your site.
- **From your site configuration:** If you only have access to a single site or want to add a subdomain directly to a site before the domain is live and then delegate it to Netlify DNS, then you can manage this through your site’s**Domain management** configuration.

#### Delegate a subdomain to Netlify DNS through site configuration

Section titled “Delegate a subdomain to Netlify DNS through site configuration”
When you delegate a subdomain to Netlify DNS through your site configuration, we recommend you add your stand-alone subdomain and then delegate this domain to Netlify DNS.

1. 
Check the domain registrar that manages your apex domain to make sure it supports NS records for subdomains. You will need to access this domain registrar to update the NS records for your subdomain later in these steps.
2. 
Navigate to your site and go to **Domain management** .
3. 
Select **Add custom domain** .
4. 
Enter your stand-alone subdomain, such as `docs.example.com` . This flow assumes that your subdomain stems from an apex domain, such as`example.com` , that is already registered through an external domain registrar.
5. 
Select **Verify** , then**Add subdomain** . Now this subdomain is connected to your site but is not yet delegated to Netlify DNS.
6. 
To delegate your subdomain to Netlify DNS, next to your subdomain, use the **Options** menu to select**Set up Netlify DNS** .
7. 
Follow the UI prompts to delegate your subdomain to Netlify DNS. During this UI flow, you may be asked to select **Verify** and**Add subdomain** again.
8. 
To complete your subdomain delegation setup, copy the NS records for your subdomain from the Netlify UI. Log in to the domain registrar that manages the related apex domain, such as `example.com` , and enter NS records for your subdomain.These DNS updates can take up to 48 hours to take effect. Learn more in our Support Guide on DNS propagation.

##### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
