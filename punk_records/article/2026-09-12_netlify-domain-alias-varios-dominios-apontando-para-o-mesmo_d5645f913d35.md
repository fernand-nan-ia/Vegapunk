---
item_id: "ea80d81c-d4e0-41fc-8a42-c12afd419f79"
platform: article
external_id: "d5645f913d35"
canonical_url: "https://docs.netlify.com/manage/domains/configure-domains/add-a-domain-alias"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: enriched
triage: null
tags: ["netlify", "domain-alias", "dominio-primario", "redirecionamento-de-dominio"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: media
  estudo_geral: baixa
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Netlify — domain alias: vários domínios apontando para o mesmo site

🔗 https://docs.netlify.com/manage/domains/configure-domains/add-a-domain-alias

## Resumo

Documento curto sobre aliases de domínio. Um site de produção pode ter vários domínios personalizados atribuídos ao mesmo tempo: um é designado domínio primário e todos os outros são aliases. O caminho é Domain management > Production domains > Add domain alias, e qualquer alias pode ser promovido a primário pelo botão Options > Set as primary domain. A recomendação oficial é não passar de 50 aliases por site.

## Tópicos

- **Primário e aliases** — Um domínio é o primário e os demais são aliases, todos servindo o mesmo site de produção.
- **Trocar o primário** — Options ao lado do domínio e Set as primary domain promove um alias a domínio principal.

## Ferramentas citadas

- **Netlify**: plataforma de hospedagem e DNS descrita no documento

## Pontos-chave

- Até 50 aliases por site, segundo a recomendação da Netlify.
- O domínio primário pode ser trocado a qualquer momento sem recriar nada.
- Serve para variações de grafia do nome e para domínios antigos que ainda recebem visita.

## Como aplicar

Útil quando o cliente tem mais de uma grafia do nome ou um domínio antigo que ainda recebe acesso: aponta os dois para o mesmo site, define o principal e ninguém se perde. Também é a saída para trocar o domínio principal sem quebrar o antigo.

## 📚 Pythagoras diz

Item pequeno e de uso claro: cliente com dois domínios, ou com o domínio antigo ainda vivo. Aponta ambos, elege o primário, e o resto se resolve sozinho.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

Ensure your site is available at all the expected domains by assigning multiple custom domains to your production site as domain aliases.

You can assign multiple custom domains to the same production site. When you do this, one is designated as the **primary domain**, and all others are called **domain aliases**.

We recommend assigning no more than 50 domain aliases to a site.

To add a domain alias:

1. 
For your site, go to your site configuration settings under **Domain management  Production domains** .
2. 
Select **Add domain alias** , and follow the prompts to assign the domain to your site.
3. 
Optionally, to change a domain alias to the primary domain, select the **Options** button next to the domain, then select**Set as primary domain** .

#### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
