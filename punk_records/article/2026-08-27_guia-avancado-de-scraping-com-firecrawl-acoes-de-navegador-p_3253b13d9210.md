---
item_id: "038bcd03-072b-4373-be1b-89948a6bfc27"
platform: article
external_id: "3253b13d9210"
canonical_url: "https://docs.firecrawl.dev/advanced-scraping-guide"
channel: "Firecrawl Docs"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["firecrawl", "web-scraping", "web-crawling", "ocr-pdf", "browser-actions", "data-extraction"]
applicability:
  saas_pessoal: alta
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
content_type: article
---

# Guia Avançado de Scraping com Firecrawl: Ações de Navegador, PDFs e Crawling Assíncrono

🔗 https://docs.firecrawl.dev/advanced-scraping-guide

## Resumo

O documento detalha os recursos avançados da API do Firecrawl para raspagem e extração de dados estruturados da web. Explica o suporte nativo a PDFs com modos de parsing via texto simples, OCR forçado ou detecção automática. Apresenta opções do endpoint /scrape como emulação mobile, remoção de boilerplate e filtragem fina de elementos DOM com includeTags e excludeTags. Destaca a capacidade de executar até 50 ações de navegador sequenciais antes da captura, como cliques, digitação, scroll e execução de JavaScript arbitrário. Além disso, cobre o crawling assíncrono em larga escala via /v2/crawl, o mapeamento de links com /v2/map e extrações autônomas via /v2/agent.

## Tópicos

- **Parsing e extração de PDFs** — Suporte a arquivos PDF com modos fast (apenas texto embutido), ocr (para scans) e auto (fallback inteligente).
- **Ações de navegador (Browser Actions)** — Execução sequencial de até 50 passos pré-scraping (cliques, preenchimento de campos, esperas e injeção de JavaScript) com limite acumulado de 60s de espera.
- **Filtragem de conteúdo e emulação mobile** — Opção de simular dispositivos móveis e filtrar elementos do DOM antes do processamento com onlyMainContent, includeTags e excludeTags.
- **Endpoints de Crawl, Map e Agent** — Operações assíncronas para varrer até 10.000 páginas (/v2/crawl), descobrir URLs de um domínio (/v2/map) ou delegar extração a um agente autônomo (/v2/agent).
- **Whitelisting e segurança de rede** — Instruções para identificação do bot via User-Agent FirecrawlAgent e liberação do IP fixo da API em firewalls corporativos.

## Ferramentas citadas

- **Firecrawl**: API de web scraping, crawling e conversão de páginas web e PDFs em Markdown ou JSON estruturado para LLMs.

## Pontos-chave

- O parsing de PDF suporta modos auto, fast e ocr, mas não permite execução de ações de navegador quando a URL resolve para PDF.
- Ações de navegador são executadas em sequência estrita e o comando write exige um click prévio no elemento para ganhar foco.
- Resultados de executeJavascript são capturados e retornados dentro do array actions.javascriptReturns na resposta da API.
- O endpoint /v2/crawl opera de forma assíncrona por padrão com limite de até 10.000 páginas e suporte a paginação de resultados via cursor next.
- A filtragem com includeTags e excludeTags avalia o DOM original da página antes da remoção de boilerplate.
- Para contornar bloqueios de firewall na sua aplicação, o IP de saída da API Firecrawl é 35.245.250.27.

## Como aplicar

Usar a API do Firecrawl via Claude Code para construir rotinas de ingestão de documentações e PDFs externos no SaaS, além de alimentar a base de conhecimento de projetos com páginas que exigem renderização de JavaScript.

## 🏴‍☠️ Lilith diz

Ah, lindo: mais uma API cobrando no cartão pra rodar um Puppeteer com esteroides e cuspir markdown pronto. É muito prático pra prototipar sem dor de cabeça, Fernando, mas fica esperto com a fatura de crawling em massa e não dependa cegamente dessas 50 ações sequenciais que quebram no primeiro redesign do alvo.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Basic scraping

To scrape a single page and get clean markdown content, use the`/scrape` endpoint.
### Scraping PDFs

Firecrawl supports PDFs. Use the`parsers` option (e.g., `parsers: ["pdf"]`) when you want to ensure PDF parsing. You can control the parsing strategy with the `mode` option:
- **`auto`** (default) — attempts fast text-based extraction first, then falls back to OCR if needed.
- **`fast`** — text-based parsing only (embedded text). Fastest, but skips scanned/image-heavy pages.
- **`ocr`** — forces OCR parsing on every page. Use for scanned documents or when`auto` misclassifies a page.

`{ type: "pdf" }` and `"pdf"` both default to `mode: "auto"`.
### Scrape options

When using the`/scrape` endpoint, you can customize the request with the following options.
#### Formats (`formats`)

The `formats` array controls which output types the scraper returns. Default: `["markdown"]`.
**String formats**: pass the name directly (e.g.

`"markdown"`).
**Object formats**: pass an object with

`type` and additional options.
#### Mobile scraping

Set`mobile: true` to emulate a mobile device. This is useful when a responsive site hides content on desktop or serves a different layout to mobile browsers.
For region-specific sites, combine with `location` and a mobile screenshot to verify the rendered layout:
`mobile: true`, add a mobile User-Agent via `headers`:
#### Content filtering

These parameters control which parts of the page appear in the output. When`onlyMainContent` is `true` (the default), boilerplate (nav, footer, etc.) is stripped. `includeTags` and `excludeTags` are applied against the original page DOM, not the post-filtered result, so your selectors should target elements as they appear in the source HTML. Set `onlyMainContent: false` to use the full page as the starting point for tag filtering.
#### Timing and cache

#### PDF parsing

#### Actions

Run browser actions before scraping. This is useful for dynamic content, navigation, or user-gated pages. You can include up to 50 actions per request, and the combined wait time across all`wait` actions and `waitFor` must not exceed 60 seconds.
##### Action execution notes

- **Write** requires a preceding`click` to focus the target element.
- **Scroll** accepts an optional`selector` to scroll a specific element instead of the page.
- **Wait** accepts either`milliseconds` (fixed delay) or`selector` (wait until visible).
- Actions run **sequentially** : each step completes before the next begins.
- Actions are **not supported for PDFs** . If the URL resolves to a PDF the request will fail.

##### Advanced action examples

**Taking a screenshot:**

cURL

**Clicking multiple elements:**

cURL

**Generating a PDF:**

cURL

**Executing JavaScript (e.g. extracting embedded page data):**

cURL

`executeJavascript` action is captured in the `actions.javascriptReturns` array of the response.
#### Full scrape example

The following request combines multiple scrape options:
cURL

`<h1>`, `<p>`, `<a>`, and `.main-content` while excluding `#ad` and `#footer`, waits 1 second before scraping, sets a 15 second timeout, and enables PDF parsing.
See the full Scrape API reference for details.
### JSON extraction via formats

Use the JSON format object in`formats` to extract structured data in one pass:
### Agent endpoint

Use the`/v2/agent` endpoint for autonomous, multi-page data extraction. The agent runs asynchronously: you start a job, then poll for results.
#### Agent options

#### Check agent status

Poll`GET /v2/agent/{jobId}` to check progress. The response `status` field will be `"processing"`, `"completed"`, or `"failed"`.
cURL

`firecrawl.agent()`) that starts the job and polls automatically until completion.
### Crawling multiple pages

To crawl multiple pages, use the`/v2/crawl` endpoint. The crawl runs asynchronously and returns a job ID. Use the `limit` parameter to control how many pages are crawled. If omitted, the crawl will process up to 10,000 pages.
cURL

#### Response

#### Check crawl job

Use the job ID to check the status of a crawl and retrieve its results.
cURL

`next` parameter, a URL to the next page of results.
#### Crawl prompt and params preview

You can provide a natural-language`prompt` to let Firecrawl derive crawl settings. Preview them first:
cURL

#### Crawler options

When using the`/v2/crawl` endpoint, you can customize crawling behavior with the following options.
##### Path filtering

##### Crawl scope

##### Sitemap and deduplication

##### Scrape options for crawl

#### Crawl example

cURL

### Mapping website links

The`/v2/map` endpoint identifies URLs related to a given website.
cURL

#### Map options

Here is the API Reference for it: Map Endpoint Documentation

### Whitelisting Firecrawl

#### Allowing Firecrawl to scrape your website

- **User Agent** : Allow`FirecrawlAgent` in your firewall or security rules.
- **IP addresses** : Firecrawl does not use a fixed set of outbound IPs.

#### Allowing your application to call the Firecrawl API

If your firewall blocks outbound requests from your application to external services, you need to whitelist Firecrawl’s API server IP address so your application can reach the Firecrawl API (`api.firecrawl.dev`):
- **IP Address** :`35.245.250.27`

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
