---
item_id: "509600a7-0095-4685-af07-8acaff24674e"
platform: article
external_id: "efb088a1ace9"
canonical_url: "https://developers.cloudflare.com/analytics/analytics-engine"
channel: "Cloudflare Docs"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["cloudflare", "analytics-engine", "metricas", "sql", "usage-billing"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Cloudflare Workers Analytics Engine — analytics de cardinalidade ilimitada com escrita por API e consulta SQL

🔗 https://developers.cloudflare.com/analytics/analytics-engine

## Resumo

Workers Analytics Engine oferece analytics em escala sem limite de cardinalidade: API para escrever pontos a partir de Workers e API SQL para consultar. Usos: expor analytics para os próprios clientes, cobrança por uso, saúde do serviço por cliente/usuário, instrumentar caminhos de código muito chamados sem afetar desempenho nem inundar sistemas externos.

## Tópicos

- **O que é** — Escrita via API + consulta SQL, cardinalidade ilimitada.
- **Usos** — Analytics para clientes, usage billing, saúde por usuário, instrumentação leve.

## Pontos-chave

- Substitui um pipeline de métricas próprio para SaaS pequeno.
- Consulta SQL direto — dashboards simples sem ferramenta extra.

## Como aplicar

Contar uso por cliente no SaaS (chamadas, documentos) e expor no painel dele.

## 🔧 Atlas diz

Instrumentação que não derruba o serviço e que consulta com SQL — dois parafusos que eu gosto. Combina com a página de preço: o Free já dá para o SaaS inteiro.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Workers Analytics Engine provides unlimited-cardinality analytics at scale, via a built-in API to write data points from Workers, and a SQL API to query that data.

You can use Workers Analytics Engine to:

- Expose custom analytics to your own customers
- Build usage-based billing systems
- Understand the health of your service on a per-customer or per-user basis
- Add instrumentation to frequently called code paths, without impacting performance or overwhelming external analytics systems with events

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
