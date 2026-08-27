---
item_id: "83bc3890-0027-4f7f-95ab-00159697ea92"
platform: article
external_id: "4d5015f2c495"
canonical_url: "https://developers.cloudflare.com/analytics/analytics-engine/pricing"
channel: "Cloudflare Docs"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["cloudflare", "analytics-engine", "precos", "metricas", "usage-billing"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: negocios-e-financas
content_type: article
---

# Cloudflare Workers Analytics Engine — preço: pontos escritos e consultas SQL (Free 100k/dia e 10k/dia; Paid 10M e 1M/mês inclusos)

🔗 https://developers.cloudflare.com/analytics/analytics-engine/pricing

## Resumo

Preço do Workers Analytics Engine por duas métricas: pontos de dados escritos (cada writeDataPoint conta um, sem custo extra por dimensões/cardinalidade ou tamanho) e consultas de leitura (cada POST à SQL API conta uma, independente da complexidade ou de quantas linhas). Workers Paid: 10 milhões de pontos/mês inclusos (+US$ 0,25 por milhão extra) e 1 milhão de consultas/mês (+US$ 1,00 por milhão extra). Workers Free: 100 mil pontos/dia e 10 mil consultas/dia.

## Tópicos

- **Métricas** — Pontos escritos (writeDataPoint) e consultas (SQL API).
- **Free** — 100k pontos/dia, 10k consultas/dia.
- **Paid** — 10M pontos + 1M consultas/mês; US$ 0,25/M e US$ 1,00/M extra.

## Pontos-chave

- Cardinalidade não custa: dá para registrar por usuário/cliente sem medo.
- Consulta complexa custa o mesmo que simples — agregar no SQL.

## Como aplicar

Medir uso por cliente do SaaS (para cobrar por uso) com Analytics Engine no Free.

## 🍩 York diz

Métrica por usuário sem pagar por cardinalidade — quem já pagou Datadog sabe o que isso vale. 100 mil pontos por dia grátis é muito SaaS pequeno. Anotado como o jeito barato de cobrar por uso.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Workers Analytics Engine is priced based on two metrics — data points written, and read queries.

| Plan | Data points written | Read queries | 
|---|---|---|
| **Workers Paid** | 10 million included per month (+$0.25 per additional million) | 1 million included per month (+$1.00 per additional million) | 
| **Workers Free** | 100,000 included per day | 10,000 included per day | 

Every time you call `writeDataPoint()` in a Worker, this counts as one data point written.

Each data point written costs the same amount. There is no extra cost to add dimensions or cardinality, and no additional cost for writing more data in a single data point.

Every time you post to Workers Analytics Engine's SQL API, this counts as one read query.

Each read query costs the same amount. There is no extra cost for more or less complex queries, and no extra cost for reading only a few rows of data versus many rows of data.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
