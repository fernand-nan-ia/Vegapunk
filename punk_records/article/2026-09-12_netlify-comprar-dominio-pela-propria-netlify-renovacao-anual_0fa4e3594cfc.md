---
item_id: "b955271a-12d4-4a8b-9f67-b523ad19ee39"
platform: article
external_id: "0fa4e3594cfc"
canonical_url: "https://docs.netlify.com/manage/domains/configure-domains/register-and-buy-a-domain"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: applied_client
triage: apply_client
tags: ["netlify", "registro-de-dominio", "renovacao-de-dominio", "expiracao-de-dominio", "certificado-wildcard", "dns-gerenciado"]
applicability:
  saas_pessoal: media
  projeto_cliente: alta
  estudo_geral: media
confidence: alta
theme: negocios-e-financas
content_type: article
---

# Netlify — comprar domínio pela própria Netlify: renovação anual, e a janela de 60 dias se expirar

🔗 https://docs.netlify.com/manage/domains/configure-domains/register-and-buy-a-domain

## Resumo

Documentação sobre registrar e comprar domínio direto pela Netlify. Ao comprar, a Netlify cria automaticamente a zona de DNS, aponta o projeto para o CDN do plano e provisiona certificado wildcard para HTTPS, tudo sem configuração manual. O caminho é Domain management > Add a domain > Buy a new domain, e por padrão o domínio novo já vira o domínio primário do site. Duas restrições declaradas: não há suporte para registrar domínios internacionalizados com caracteres não-ASCII como ñ ou é, que precisam ser comprados em outro registrador e depois trazidos; e o registro vale por um ano, renovando automaticamente pelo cartão da conta, com opção de desligar a renovação na página do domínio. A parte mais importante é o que acontece se expirar: todos os registros de DNS param de funcionar imediatamente, nos primeiros 30 dias ainda dá para pedir socorro ao suporte a partir de um e-mail ligado à equipe que pagou, dos dias 31 ao 60 não se pode nem renovar nem recomprar, e depois de 60 dias o domínio vai a leilão público e qualquer um pode levá-lo.

## Tópicos

- **O que a compra já resolve** — Zona de DNS criada, projeto apontado para o CDN e certificado wildcard de HTTPS provisionado automaticamente.
- **Domínios com acento não dá** — Nomes internacionalizados com caracteres não-ASCII precisam ser registrados em outro registrador e trazidos depois.
- **Renovação e expiração** — Registro anual com renovação automática pelo cartão da equipe; expirando, o DNS para na hora, há 30 dias de socorro pelo suporte, 30 dias de limbo e liberação pública no dia 60.

## Ferramentas citadas

- **Netlify**: plataforma de hospedagem e DNS descrita no documento

## Pontos-chave

- Comprar pela Netlify já entrega zona de DNS e certificado wildcard sem passo manual.
- O domínio comprado vira o domínio primário do site por padrão.
- Registro vale 1 ano e renova sozinho, a menos que a renovação automática seja desligada.
- Se expirar, TODOS os registros de DNS param de funcionar imediatamente.
- Dias 1-30 após expirar: recuperação só por e-mail ao suporte, vindo de endereço ligado à equipe que pagou.
- Dias 31-60: não se pode renovar nem recomprar.
- Dia 60 em diante: o domínio vai para venda pública e pode ser comprado por qualquer um.
- Domínio com ñ ou é não pode ser comprado na Netlify.

## Como aplicar

Comprar o domínio do cliente pela própria Netlify tira todo o trabalho de DNS do caminho, mas cria uma dependência perigosa: o domínio fica na SUA conta e no SEU cartão. Deixe a renovação automática LIGADA e trate a data como compromisso com o cliente — 60 dias de atraso e o domínio dele vai a leilão. Se o cliente for pagar o domínio, o certo é ele registrar no nome dele e você só apontar.

## 📚 Pythagoras diz

O registro é claro sobre o calendário do desastre: 30 dias de socorro, 30 de limbo, e no dia 60 o domínio do seu cliente está à venda para qualquer um. Deduzo que a decisão importante aqui não é técnica e sim de titularidade: em nome de quem fica o domínio, e em qual cartão.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

Register and buy a new domain from Netlify and let Netlify DNS help you manage your domain for the fastest and smoothest setup.

We will automatically configure your site or app to use the domain on the best CDN (content delivery network) for your Netlify plan.

Once you register the domain name, Netlify creates a Netlify DNS zone for the domain, and provisions a wildcard certificate for HTTPS.

### Register and buy a domain for a project:

Section titled “Register and buy a domain for a project:”
As an Owner, to register and buy a domain for your project

1. 
From your Project overview, in the left sidebar, select **Domain management** from the left sidebar.
2. 
Select **Add a domain** >**Buy a new domain** , then follow the prompts to register and buy your domain.

By default, your new domain is automatically assigned as the primary domain for your site.

### Supported domains

Section titled “Supported domains”
Netlify offers support for many different TLD domains, which you can confirm when verifying your domain.

#### Domains with special characters

Section titled “Domains with special characters”
Netlify does not currently support buying or registering internationalized domain names (IDN) that use Unicode (or non-ASCII) characters such as ñ or é. If you need a domain with special characters, you will need to register it through another domain registrar and then bring the domain to Netlify.

### Domain renewal and expiration

Section titled “Domain renewal and expiration”
Domain registrations are valid for one year. To ensure continuous service, Netlify-registered domains automatically renew by default using the payment method on file for the team. You can turn off auto-renewal in the domain detail page of the Netlify UI.

Near the end of the registration period, Netlify will send you an email informing you of the cost for renewal, as well as whether your domain is set to renew automatically or not.

If you have **disabled auto-renewal** on a domain, and the registration expires, all DNS records for the domain will stop working. You have the option to get the domain back, subject to the following timeline:

- For the first 30 days after expiration, you can request assistance with domain renewal by contacting support@netlify.com from an email address associated with the Netlify team that paid for the domain.
- For the next 30 days, days 31-60 after expiration, you can neither renew nor purchase the domain.
- When 60 days have passed after expiration, the domain becomes available for sale to the public. You can then purchase it again as a new domain.

### Transfer registration

Section titled “Transfer registration”
To learn about your options for transferring a domain registration, check out the transfer domains docs.

##### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
