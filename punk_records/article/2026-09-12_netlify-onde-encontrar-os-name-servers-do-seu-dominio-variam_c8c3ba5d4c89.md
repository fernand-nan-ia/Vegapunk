---
item_id: "caa1c102-b10c-4321-862c-23f4657aa0dd"
platform: article
external_id: "c8c3ba5d4c89"
canonical_url: "https://docs.netlify.com/manage/domains/configure-domains/netlify-name-servers"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: enriched
triage: null
tags: ["name-servers", "netlify-dns", "delegacao-de-dominio"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: media
  estudo_geral: baixa
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Netlify — onde encontrar os name servers do seu domínio (variam por domínio)

🔗 https://docs.netlify.com/manage/domains/configure-domains/netlify-name-servers

## Resumo

Documento curto e operacional: os name servers da Netlify variam conforme o domínio, então não existe lista fixa para copiar. Para descobrir os corretos, é preciso primeiro adicionar o domínio ao site ou à equipe; depois, no painel da equipe, DNS na barra lateral, selecionar o domínio e ler a seção Name servers, onde aparecem endereços no formato dns1.p01.nsone.net.

## Ferramentas citadas

- **Netlify**: plataforma de hospedagem e DNS descrita no documento

## Pontos-chave

- Os name servers variam por domínio; copiar de um tutorial antigo dá erro.
- É preciso adicionar o domínio antes de descobrir quais são os seus.
- O formato é dns1.p01.nsone.net e similares.

## Como aplicar

Lembrete prático na hora de delegar o domínio de um cliente: pegue os name servers no painel daquele domínio específico, nunca de um tutorial ou de outro projeto seu.

## 📚 Pythagoras diz

Registro pequeno com uma armadilha grande: name server não é lista universal. Copiar do tutorial do YouTube é o erro que faz o domínio do cliente não subir e ninguém entender por quê.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

Netlify’s name servers will vary depending on your domain. Learn how to find your name servers.

To get a list of available name servers for your domain, you must first add a domain to your site or team.

Next you can find Netlify’s available name servers for that domain in the Netlify domains dashboard.

1. Go to your Netlify Team dashboard.
  - From your project dashboard, in the top left, choose **Projects** next to your project name.
2. From your project dashboard, in the top left, choose 

1. Select **DNS** from the left sidebar.

1. 
Select the specific domain you want to set up name servers for.
2. 
From your domain dashboard, under **Name servers** , you’ll find a list of available name servers for your domain in a format simliar to`dns1.p01.nsone.net` .

#### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
