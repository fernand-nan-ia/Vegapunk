---
item_id: "5a27fd57-f1ac-4554-8733-a62851eeb1c7"
platform: article
external_id: "552467ff860e"
canonical_url: "https://docs.firecrawl.dev/rate-limits"
channel: "Firecrawl Docs"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["firecrawl", "web-scraping", "rate-limits", "api", "mcp", "llm-tools"]
applicability:
  saas_pessoal: media
  projeto_cliente: media
  estudo_geral: alta
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Rate Limits e Concorrência na API do Firecrawl

🔗 https://docs.firecrawl.dev/rate-limits

## Resumo

A documentação técnica do Firecrawl detalha o funcionamento dos rate limits e limites de navegadores simultâneos entre seus diferentes planos de assinatura. O gargalo real no processamento reside na concorrência de navegadores, que vai de 2 instâncias no plano Free até mais de 150 no Scale/Enterprise, com filas de espera suportadas até estourarem o timeout configurado ou 48 horas. Os limites de requisições por minuto (RPM) são divididos por endpoint, como /scrape, /map, /crawl, /search e /agent, sendo aplicados a nível de equipe compartilhado entre todas as chaves de API. Endpoints de extração compartilham os limites do /agent, enquanto batch scrape compartilha com /crawl. Há suporte a uso sem chave (keyless) para operações básicas via MCP, CLI e SDKs, limitado por requisições e créditos diários por IP. Ao exceder qualquer teto de requisições ou concorrência, a API responde com status 429.

## Tópicos

- **Limites de Navegadores Simultâneos e Fila** — Define quantas páginas rodam em paralelo (2 a 150+) e como requisições excedentes entram em fila com expiração máxima de 48h ou timeout customizado.
- **Taxas de Requisições por Minuto (RPM)** — Tabelas de limites por minuto para cada endpoint (/scrape, /map, /crawl, /agent), consolidados por equipe e compartilhados entre API keys.
- **Uso Keyless (Sem API Key)** — Acesso gratuito para Search, Scrape e Parse com tetos diários baseados em total de requisições e consumo de créditos por IP.
- **Sandbox de Navegador e Interatividade** — Limites específicos para sessões ativas e execução de ações nos endpoints /interact.

## Ferramentas citadas

- **Firecrawl**: Serviço de web scraping, crawling e extração de dados estruturados otimizado para LLMs e agentes.
- **Firecrawl MCP**: Servidor Model Context Protocol que permite integrar ferramentas de busca e scrape sem API key diretamente em agentes de IA.

## Pontos-chave

- O verdadeiro gargalo na arquitetura do Firecrawl é a concorrência de navegadores paralelos, não o rate limit de RPM.
- O plano Free oferece 2 navegadores concorrentes e fila de até 50.000 jobs, enquanto o Standard suporta 50 navegadores.
- Endpoints /extract e /agent compartilham a mesma cota de requisições por minuto.
- Endpoints de batch scrape utilizam a cota atribuída a /crawl.
- O tempo de espera na fila conta no parâmetro de timeout da requisição, permitindo configurar fail-fast.
- O modo keyless permite Search, Scrape, Parse e Interact limitados por IP com contagem de créditos diários.

## Como aplicar

Ao integrar extração de dados da web no SaaS ou em pipelines via Claude Code, configure timeouts baixos para fail-fast e controle a concorrência no cliente para evitar erros 429 desnecessários.

## 💡 Edison diz

Eureka! O pulo do gato aqui é usar o endpoint de Queue Status antes de disparar jobs em massa! Se a gente souber dosar o timeout nas requisições do MCP, dá pra montar um pipeline de scraping que roda liso até no plano Free sem engasgar a fila. Minha orelha já subiu pensando num coletor automatizado de dados!

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

`429` response. See Errors for the full error catalog and a retry-with-backoff snippet.
### Concurrent Browser Limits

Concurrent browsers control how many pages Firecrawl can process for you in parallel. Your plan sets the ceiling; any jobs beyond it wait in a queue until a browser frees up. Time spent in the queue counts against the request’s`timeout` parameter, so you can set a lower timeout to fail fast instead of waiting. To see current availability before sending work, call the Queue Status endpoint. Jobs that are waiting in your concurrency queue will time out after a maximum of 48 hours.
#### Current Plans

| Plan | Concurrent Browsers | Max Queued Jobs | 
|---|---|---|
| Free | 2 | 50,000 | 
| Hobby | 5 | 50,000 | 
| Standard | 50 | 100,000 | 
| Growth | 100 | 200,000 | 
| Scale / Enterprise | 150+ | 300,000+ | 

`429` status code until existing jobs complete. For larger plans with custom concurrency limits, the max queued jobs is 2,000 times your concurrency limit, capped at 2,000,000.
If you require higher concurrency limits, contact us about enterprise plans.
### API Rate Limits

Rate limits are measured in requests per minute and are primarily in place to prevent abuse. When configured correctly, your real bottleneck will be concurrent browsers. Rate limits are applied per team, so all API keys on the same team share the same rate limit counters.
#### Keyless (no API key)

The hosted Firecrawl MCP keyless endpoint exposes exactly
**Search, Scrape, and Parse**without an API key. Other hosted MCP tools require an account connection or an API key. For official Firecrawl clients, the CLI, SDKs, and REST API, keyless access also includes

**Interact**. On Firecrawl Cloud, research and developer search endpoints can also be used without an API key. No other endpoints (crawl, extract, map, batch scrape, etc.) are available without a key. Keyless usage is free and capped per IP address per day by

**two limits**, and exceeding either returns a

`429`:
- A maximum number of **requests** per day.
- A maximum number of **credits** per day. Operations cost different amounts of credits (for example, Interact and JSON extraction cost more than a basic scrape), so heavier usage reaches the credit cap sooner.

#### Current Plans

| Plan | /scrape | /map | /crawl | /search | /agent | /crawl/status | /agent/status | 
|---|---|---|---|---|---|---|---|
| Free | 10 | 10 | 2 | 10 | 2 | 500 | 500 | 
| Hobby | 100 | 100 | 20 | 100 | 20 | 5000 | 5000 | 
| Standard | 500 | 500 | 100 | 500 | 100 | 25000 | 25000 | 
| Growth | 5000 | 5000 | 1000 | 5000 | 1000 | 250000 | 250000 | 
| Scale | 10000 | 10000 | 2000 | 10000 | 2000 | 500000 | 500000 | 

#### Extract Endpoints

The extract endpoints share limits with the corresponding /agent rate limits.
#### Batch Scrape Endpoints

The batch scrape endpoints share limits with the corresponding /crawl rate limits.
#### Browser Sandbox

The browser sandbox endpoints have per-plan rate limits that scale with your subscription:
| Plan | /interact | /interact/{id}/execute | 
|---|---|---|
| Free | 2 | 10 | 
| Hobby | 20 | 100 | 
| Standard | 100 | 500 | 
| Growth | 1,000 | 5,000 | 
| Scale | 1,500 | 7,500 | 

`429` status code until existing sessions are destroyed.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
