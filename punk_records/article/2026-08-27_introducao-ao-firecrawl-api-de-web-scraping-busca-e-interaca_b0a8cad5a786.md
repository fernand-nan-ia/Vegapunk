---
item_id: "89758dbc-07f0-46d6-afd2-2dd8cfffdadb"
platform: article
external_id: "b0a8cad5a786"
canonical_url: "https://docs.firecrawl.dev/introduction"
channel: "Firecrawl Docs"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["firecrawl", "web-scraping", "mcp", "llm-ready", "extracao-de-dados", "automacao-web", "agentic-ai"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: alta
confidence: alta
theme: ia-e-agentes
content_type: article
---

# Introdução ao Firecrawl: API de Web Scraping, Busca e Interação para LLMs

🔗 https://docs.firecrawl.dev/introduction

## Resumo

O Firecrawl é uma API e ferramenta open-source projetada para buscar, raspar e interagir com páginas web, entregando os dados em formatos otimizados para modelos de linguagem, como Markdown e JSON estruturado. A plataforma resolve internamente a complexidade de contornar defesas anti-bot, gerenciar proxies e renderizar páginas pesadas em JavaScript. Além do scraping básico e rastreamento completo de domínios (crawl e map), o serviço disponibiliza recursos interativos para preenchimento de formulários e cliques em sandboxes de navegador. Também oferece suporte à conversão de documentos locais como PDF, DOCX e XLSX em Markdown limpo. A integração com agentes de inteligência artificial é facilitada via Model Context Protocol (MCP), CLI dedicada e SDKs para linguagens populares.

## Tópicos

- **Extração e Limpeza para LLMs** — Converte páginas da web e arquivos locais (PDF, DOCX, XLSX) em Markdown estruturado ou JSON, contornando bloqueios anti-bot e executando JavaScript dinâmico.
- **Interação e Sandboxes de Navegador** — Permite executar ações em páginas web como preenchimento de formulários, cliques e navegação dinâmica orientada por código ou linguagem natural.
- **Mapeamento e Rastreamento em Escala** — Disponibiliza rotas dedicadas para mapear todas as URLs de um domínio e realizar rastreamento recursivo completo de sites.
- **Integração com Agentes e Protocolo MCP** — Oferece suporte ao Model Context Protocol (MCP), documentação em llms.txt e CLI com injeção automática de ferramentas para coding agents.

## Ferramentas citadas

- **Firecrawl**: API e plataforma de web scraping, busca, parsing e automação focada em dados para LLMs
- **Model Context Protocol (MCP)**: Protocolo aberto para expor ferramentas e recursos do Firecrawl diretamente para agentes de IA
- **LangChain**: Framework de integração de IA compatível com os conectores do Firecrawl
- **LlamaIndex**: Framework de indexação de dados para LLMs integrado ao ecossistema do Firecrawl

## Pontos-chave

- Entrega dados web diretamente em Markdown limpo ou JSON, eliminando etapas manuais de sanitização de HTML.
- Lida nativamente com proxies, renderização em headless browser e barreiras anti-bot em produção.
- Suporta parsing de arquivos locais como PDF, DOCX, XLSX e HTML para formatos amigáveis a LLMs.
- Permite interação em páginas via sandboxes gerenciadas usando instruções em linguagem natural ou código.
- Pode ser utilizado via API hospedada na nuvem ou implantado localmente via repositório open-source.
- Facilita o acoplamento a ferramentas de desenvolvimento de agentes através de servidor MCP e arquivos llms.txt.

## Como aplicar

Pode ser integrado via servidor MCP ao ambiente de desenvolvimento com Claude Code para buscas contextuais, ou consumido via API no backend do SaaS para extrair e estruturar dados de sites externos sem necessidade de gerenciar infraestrutura de Playwright.

## 🪖 Shaka diz

A documentação apresenta uma solução técnica sólida para abstrair a complexidade de proxies e renderização dinâmica. A disponibilidade do servidor MCP reduz a fricção de uso direto em agentes de código, mas é prudente calcular a viabilidade financeira da API gerenciada frente à versão auto-hospedada caso o volume escale. O recurso de parsing e scraping estruturado é imediatamente aplicável para ingestão de dados.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Get started

#### Build directly with the API

Scrape your first page now. No account or API key is required for this request.
cURL

### Other ways to get started

#### Install the Firecrawl CLI

One command installs the Firecrawl CLI, authenticates in your browser, and adds skills to every detected coding agent.
Restart your coding agent after setup so it can discover the new skills. See
CLI for the full setup.

#### Set up with an agent

Provide your agent with this Firecrawl setup prompt, or see all MCP setup options.
**For AI agents:**Use llms.txt for an index of the documentation, or llms-full.txt for the full text.

#### Build and test directly

### Get your API key

Create a free account for direct API access and higher limits

### Try it in the Playground

Test Firecrawl in the browser without writing code

### What can Firecrawl do?

### Search

Search the web and get full page content from results

### Scrape

Extract content from any URL as markdown, HTML, or structured JSON

### Interact

Continue working with any scraped page: click, fill forms, extract dynamic
content

#### Why Firecrawl?

- **LLM-ready output** : Clean markdown, structured JSON, screenshots, and more.
- **Handles the hard stuff** : Proxies, anti-bot, JavaScript rendering, and dynamic content.
- **Reliable** : Built for production with high uptime and consistent results.
- **Fast** : Results in seconds, optimized for high throughput.
- **MCP Server** : Connect Firecrawl to any AI tool via the Model Context Protocol.

Bounty: 5,000 credit reward for solid feedback on Firecrawl

To qualify, complete a high-signal interview (thoughtful, concrete use cases, etc) with our Firecrawl Feedback Assistant. Only takes a few minutes, can be stopped at any time, and is both human/agent-friendly (just paste the link into your agentic harness!). New to Firecrawl? Your take still counts.

Start the interview
Include your email to be eligible. Interviews are reviewed for quality at the end of each week.

### Search

Search the web and get full page content from results in one call. See the Search feature docs for all options.
### Response


Response

SDKs will return the data object directly. cURL will return the complete payload.

JSON

### Scrape

Scrape any URL and get its content in markdown, HTML, or other formats. See the Scrape feature docs for all options.
### Response


Response

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

### Interact

Scrape a page, then keep working with it: click buttons, fill forms, extract dynamic content, or navigate deeper. Describe what you want in plain English or write code for full control. See the Interact feature docs for all options.
### Response


Response

Response

### More capabilities

### Agent

Autonomous web data gathering powered by AI

### Interact

Click, fill forms, extract dynamic content

### Webhooks

Async event delivery

### Browser Sandbox

Managed browser sessions for interactive workflows

### Parse

Turn local PDFs, DOCX, XLSX, HTML, and more into Markdown or structured JSON

### Map

Discover all URLs on a website

### Crawl

Recursively gather content from entire sites

### Resources

### API Reference

Complete API documentation with interactive examples

### SDKs

Python, Node.js, CLI, and community SDKs

### Open Source

Self-host Firecrawl or contribute to the project

### Integrations

LangChain, LlamaIndex, OpenAI, and more

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
