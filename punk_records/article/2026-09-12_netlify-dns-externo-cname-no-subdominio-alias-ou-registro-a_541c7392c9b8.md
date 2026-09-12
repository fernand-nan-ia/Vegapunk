---
item_id: "d1413e53-f291-4fc3-a4aa-ab1b4ee73e8d"
platform: article
external_id: "541c7392c9b8"
canonical_url: "https://docs.netlify.com/manage/domains/configure-domains/configure-external-dns"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: applied_client
triage: apply_client
tags: ["dns-externo", "cname", "registro-a", "apex-loadbalancer", "dominio-apex", "propagacao-de-dns"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Netlify — DNS externo: CNAME no subdomínio, ALIAS ou registro A no apex

🔗 https://docs.netlify.com/manage/domains/configure-domains/configure-external-dns

## Resumo

Procedimento para apontar domínio para a Netlify mantendo o DNS em outro provedor, que é o caminho de quem não quer migrar a zona. Os detalhes exatos aparecem em Domain management > Production domains > Pending DNS verification. Para subdomínio como blog.exemplo.com ou www.exemplo.com, cria-se um registro CNAME com o subdomínio como host apontando para o endereço netlify.app do site. Para domínio apex, que por definição não aceita CNAME, a configuração recomendada é um registro ALIAS, ANAME ou CNAME achatado apontando para apex-loadbalancer.netlify.com, com o host vazio ou @; se o provedor não suportar nenhum desses, resta a alternativa menos resiliente do registro A com IP fixo. Configurar o www adiciona automaticamente o apex ao site, que então também precisa ser configurado. A propagação pode levar um dia inteiro.

## Tópicos

- **Subdomínio** — CNAME com o subdomínio como host apontando para o endereço netlify.app do site.
- **Apex** — ALIAS, ANAME ou CNAME achatado para apex-loadbalancer.netlify.com, host vazio ou @; registro A com IP fixo é a alternativa menos resiliente.
- **www puxa o apex** — Configurar o www adiciona o apex automaticamente ao site, e ele também precisa ser configurado.

## Ferramentas citadas

- **Netlify**: plataforma de hospedagem e DNS descrita no documento

## Pontos-chave

- Domínio apex não aceita CNAME: é limitação do DNS, não da Netlify.
- O alvo recomendado do apex é apex-loadbalancer.netlify.com, não um IP.
- Registro A com IP fixo funciona mas é a opção pior: IP pode mudar.
- As instruções exatas do caso aparecem em Pending DNS verification.
- A propagação pode levar um dia inteiro.

## Como aplicar

É o procedimento para cliente que já tem domínio e e-mail funcionando: não migre a zona, crie um registro só. Pergunte ao registrador do cliente se ele suporta ALIAS ou CNAME-flattening no apex; se não suportar, use o registro A sabendo que é a opção mais frágil.

## 📚 Pythagoras diz

O registro é explícito sobre o que muita gente descobre no susto: apex não aceita CNAME, e por isso existe o apex-loadbalancer. Prefira ALIAS ao registro A — IP muda, nome não.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

If you’ve assigned an externally registered domain to your site, and you don’t want to use Netlify DNS, you need to configure your external DNS provider to point your domain to Netlify.

To access customized details about the DNS records you need to configure, go to **Domain management  Production domains** and select **Pending DNS verification** next to the custom domain.

The next steps vary depending on the type of domain or subdomain.

- For a subdomain of a domain you own, such as `blog.petsofnetlify.com` or`www.petsofnetlify.com` , follow the directions below for subdomain configuration.
- For an apex domain with no subdomain, such as `petsofnetlify.com` , make sure to read our advice about using apex domains, then follow the directions below for apex domain configuration.

### Configure a subdomain

Section titled “Configure a subdomain”
To point a subdomain such as `blog.petsofnetlify.com` or `www.petsofnetlify.com` to your site on Netlify, you must first add the domain to your site on Netlify and then create a CNAME record with your DNS provider.

For example, if your site’s domain is `blog.petsofnetlify.com` and your Netlify subdomain is `brave-curie-12345.netlify.app`:

1. Follow the instructions to add the domain `blog.petsofnetlify.com` to the`brave-curie-12345.netlify.app` site on Netlify. At the end of the process, Netlify provides a CNAME record to add to your DNS provider.
2. Find your DNS provider’s DNS record settings for your apex domain, `petsofnetlify.com` .
3. On your DNS provider’s site, add the CNAME record with your subdomain, `blog` , as the host.
4. Point the record to your Netlify subdomain, `brave-curie-12345.netlify.app` .

1. Save your settings. It may take a full day for the settings to propagate across the global Domain Name System.

If your site uses the `www` subdomain, as in `www.petsofnetlify.com`, you will use the same procedure described above. Once you configure the `www` subdomain, an apex domain will also be added automatically to your site. You’ll need to follow the steps in the section below to configure the apex domain too. Learn more about our special handling for `www` subdomains.

### Configure an apex domain

Section titled “Configure an apex domain”
Unlike subdomains, apex domains don’t support CNAME records. You must configure your apex domain with an ALIAS, ANAME, flattened CNAME, or A record. Different DNS providers support different record types. Depending on what your DNS provider supports, use either the recommended configuration or the fallback option below.

If your DNS provider supports ALIAS, ANAME, or flattened CNAME records, use this recommended configuration, which is more resilient than the fallback option.

1. Find your DNS provider’s DNS record settings for your apex domain, such as `petsofnetlify.com` .
2. Add an **ALIAS** ,**ANAME** , or**flattened CNAME record** . Depending on your provider, leave the host field empty or enter`@` .
3. Point the record to Netlify’s load balancer at: `apex-loadbalancer.netlify.com` .

1. Save your settings. It may take a full day for the settings to propagate across the global Domain Name System.

If your DNS provider does not support ALIAS, ANAME, or flattened CNAME records, use this fallback option.

1. Find your DNS provider’s DNS record settings for your apex domain, such as `petsofnetlify.com` .
2. Add an **A record** . Depending on your provider, leave the host field empty or enter`@` .
3. Point the record to Netlify’s load balancer IP address: `75.2.60.5` .

1. Save your settings. It may take a full day for the settings to propagate across the global Domain Name System.

In both cases, the apex domain eventually resolves to our load balancer IP address. This means the apex domain can’t take advantage of direct DNS routing on a global CDN like Netlify’s. Because of this, we recommend using a subdomain for your primary domain when using external DNS.

### DNS record propagation

Section titled “DNS record propagation”
Depending on your DNS provider, **changes to DNS records can take several hours to propagate and take effect for the entire internet.**

If more than 24 hours have passed since you configured your DNS records, and your site is still not accessible at your custom domain, try our DNS troubleshooting tips.

##### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
