---
item_id: "3b64ada1-9108-44df-8bd5-562095e3b2f8"
platform: article
external_id: "ebdd96b3133c"
canonical_url: "https://docs.netlify.com/manage/monitoring/status-badges"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: archived
triage: archive
tags: ["netlify", "status-badge", "deploy-status", "readme", "ci-cd", "monitoramento-de-deploy"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: baixa
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Netlify — status badges de deploy (não é o selo 'Powered by Netlify')

🔗 https://docs.netlify.com/manage/monitoring/status-badges

## Resumo

Documentação oficial do Netlify sobre status badges: imagens servidas pela API do Netlify que mostram o estado do deploy mais recente de produção ou de um branch (success, building, failed, canceled). O badge é gerado em Project configuration > General > Status badges, onde o painel devolve um snippet markdown pronto para colar no README do repositório, na documentação ou em qualquer página web. A URL da imagem segue o padrão https://api.netlify.com/api/v1/badges/{site-id}/deploy-status, e acrescentar o parâmetro ?branch=nome gera o badge de um branch específico. Clicar no badge leva o visitante à página Deploys do projeto. O documento NÃO trata do selo flutuante 'Powered by Netlify' que aparece no canto de sites publicados: são duas coisas diferentes, e o status badge é opcional e colocado pelo próprio dono do repositório. Para remover um status badge basta apagar o snippet de onde ele foi colado.

## Tópicos

- **O que o badge mostra** — Estado do deploy mais recente de produção ou de branch: success, building, failed ou canceled, atualizado automaticamente.
- **Como gerar** — Netlify UI > Project configuration > General > Status badges, copiar o snippet markdown e commitar no README.
- **Badge por branch** — Acrescentar ?branch=<nome> ao fim da URL da imagem para acompanhar um branch específico em vez da produção.

## Ferramentas citadas

- **Netlify**: hospedagem que serve o badge pela API em api.netlify.com/api/v1/badges/{site-id}/deploy-status

## Pontos-chave

- A URL do badge é https://api.netlify.com/api/v1/badges/{site-id}/deploy-status.
- ?branch=dev muda o badge para acompanhar o branch em vez da produção.
- O badge é opcional e colocado pelo dono do repositório; remover é apagar o snippet.
- Clicar no badge abre a página Deploys do projeto, o que expõe o painel do site para quem vê o README.
- Este documento não cobre o selo flutuante 'Powered by Netlify' injetado nos sites publicados.

## Como aplicar

Serve para o README do repositório do Vegapunk, não para o site do cliente. Cuidado: o badge linka para a página Deploys do projeto, então em repositório público ele revela onde o site é hospedado e administrado. No site do Jardins Café não use: o que aparece lá é o HUD do Netlify, outra coisa.

## 📚 Pythagoras diz

O registro diz o que muita gente confunde: status badge é imagem de README, colocada por você, e sai apagando o snippet. O selo que incomoda no rodapé do Jardins não está aqui, e eu prefiro marcar essa lacuna a preenchê-la com suposição.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

Status badges are visual representations of your site’s status, served as image files you can add to repository READMEs, documentation, or any other web page.

The **deploy status badge** automatically updates to show the status of a site’s most recent production or branch deploy:

### Add status badges

Section titled “Add status badges”
Follow these steps to get a specific image URL for your site’s status badge and add it to a repository README, your documentation, or any other web page.

1. 
In the Netlify UI, select a specific site, then go to **Project configuration  General  Status badges** .
2. 
Copy the automatically generated markdown snippet and paste it into your repository README or markdown source for any website.
3. 
Optionally, to create a status badge for a deployed branch, add the `?branch=` query parameter to the badge image URL. For example, if the branch name is`dev` , the image URL would end with`/deploy-status?branch=dev` .
4. 
Commit the changes to your README or deploy the website containing the markdown snippet.

When a user encounters the status badge in your README or website, the badge will reflect the current status of your site’s most recent production or branch deploy. Selecting the status badge takes a user to your site’s **Deploys** page.

##### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
