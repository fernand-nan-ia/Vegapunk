---
item_id: "97deb2b1-c05f-41fe-b3d0-c5d7170b18bf"
platform: article
external_id: "07e29605f541"
canonical_url: "https://github.com/facebook/docusaurus"
channel: "Facebook · GitHub"
captured_at: 2026-09-07
status: enriched
triage: null
tags: ["docusaurus", "gerador-de-site-estatico", "documentacao", "markdown", "site-versionado", "meta-oss"]
applicability:
  saas_pessoal: media
  projeto_cliente: baixa
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Docusaurus: gerador de sites de documentação da Meta (Markdown → site estático)

🔗 https://github.com/facebook/docusaurus

## Resumo

Docusaurus é o gerador de sites de documentação mantido pela Meta, criado para escalar os sites dos muitos projetos de código aberto da empresa. Ele transforma arquivos Markdown em um site estático completo, já com as seções que um projeto costuma precisar: página inicial, seção de documentação versionada, blog e páginas de apoio. Não tem relação com IA — é ferramenta de publicação. Começa com um comando só, `npm init docusaurus@latest`, e há um playground em docusaurus.new para testar sem instalar nada. Traz suporte de localização via CrowdIn, o que permite manter a mesma documentação em vários idiomas, e é customizável a ponto de o site não parecer um template. O código é MIT e a documentação é Creative Commons. É um projeto grande e muito ativo, com governança corporativa: código de conduta da Meta, guia de contribuição, lista de issues marcadas para iniciantes e canais no Discord separados entre quem usa e quem contribui.

## Tópicos

- **O que gera** — Site estático a partir de Markdown, já com página inicial, seção de documentação, blog e páginas de apoio prontas.
- **Início em um comando** — `npm init docusaurus@latest` cria o site; docusaurus.new permite testar num playground sem instalar nada.
- **Localização** — Suporte de tradução via CrowdIn, pensado para manter a mesma documentação em vários idiomas.
- **Origem e governança** — Mantido pela Meta para escalar os sites dos projetos de código aberto da empresa; código de conduta, guia de contribuição e issues marcadas para iniciantes.
- **Licenças separadas** — O código é MIT; a documentação (os .md em /docs) é Creative Commons — duas licenças no mesmo repositório.

## Ferramentas citadas

- **Docusaurus**: gerador de site estático de documentação a partir de Markdown
- **CrowdIn**: plataforma de tradução integrada para a localização do site
- **npm**: instalação e criação do projeto via npm init docusaurus@latest

## Pontos-chave

- 66.191 estrelas, MIT, push em 07/09/2026 — projeto muito ativo, verificado na API no mesmo dia
- Não tem nada de IA: é publicação de documentação, não geração de site
- Entrada é Markdown puro — a mesma matéria-prima do Punk Records
- Traz documentação versionada, blog e busca prontos, sem configuração
- Foi listado como ferramenta de 'criação de sites' numa recomendação de terceiro, o que confunde: não serve para landing page de cliente
- Licença dupla no mesmo repo: MIT para o código, Creative Commons para os textos

## Como aplicar

Errado para o site do cliente, que é landing de conversão e não documentação. O uso que faz sentido aqui é outro: o Punk Records já é Markdown com frontmatter, então o Docusaurus poderia publicá-lo como site navegável com busca — uma terceira opção ao lado do Obsidian e do Notion na ideia registrada em 27/08. Antes disso é preciso resolver privacidade: o vault é conteúdo pessoal e um site estático publicado é público por natureza.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Docusaurus is a project for building, deploying, and maintaining open source project websites easily.

Short on time? Check out our 5-minute tutorial ⏱️!

**Tip**: use **docusaurus.new** to test Docusaurus immediately in a playground.

- **Simple to Start**

Docusaurus is built in a way so that it can get running in as little time as possible. We've built Docusaurus to handle the website build process so you can focus on your project.


- **Localizable**

Docusaurus ships with localization support via CrowdIn. Empower and grow your international community by translating your documentation.


- **Customizable**

While Docusaurus ships with the key pages and sections you need to get started, including a home page, a docs section, a blog, and additional support pages, it is also customizable to ensure you have a site that is uniquely yours.


Use the initialization CLI to create your site:

`npm init docusaurus@latest`
Read the docs for any further information.

We've released Docusaurus because it helps us better scale and supports the many OSS projects at Meta. We hope that other organizations can benefit from the project. We are thankful for any contributions from the community.

Meta has adopted a Code of Conduct that we expect project participants to adhere to. Please read the full text so that you can understand what actions will and will not be tolerated.

Read our contributing guide to learn about our development process, how to propose bugfixes and improvements, and how to build and test your changes to Docusaurus.

To help you get your feet wet and get you familiar with our contribution process, we have a list of beginner-friendly bugs that might contain smaller issues to tackle first. This is a great place to get started.

We have a few channels for contact:

- Discord:
  - `#general` for those using Docusaurus.
  - `#contributors` for those wanting to contribute to the Docusaurus core.
- @docusaurus X
- GitHub Issues

This project exists thanks to all the people who contribute. [Contribute].

Thank you to all our backers! 🙏 Become a backer

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. Become a sponsor

Docusaurus is MIT licensed.

The Docusaurus documentation (e.g., `.md` files in the `/docs` folder) is Creative Commons licensed.

BrowserStack supports us with free access for open source.

Rocket Validator helps us find HTML markup and accessibility issues.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
