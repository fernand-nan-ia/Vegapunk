---
item_id: "83e89679-4067-4ec6-9296-8de68ef5e83c"
platform: article
external_id: "fc7635ee4280"
canonical_url: "https://www.cloudflare.com/plans"
channel: "Cloudflare"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["cloudflare", "workers", "precos", "serverless"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: media
theme: negocios-e-financas
content_type: article
---

# Cloudflare Workers — preço: Free 100 mil requisições/dia e 10 ms de CPU; Paid US$ 0,30/milhão de requisições e US$ 0,02/milhão de ms de CPU

🔗 https://www.cloudflare.com/plans

## Resumo

Da página de planos da Cloudflare, o único bloco que veio no texto é o de Workers: plano Free com 100 mil requisições por dia e 10 ms de CPU por requisição; plano Paid com US$ 0,30 por milhão de requisições e US$ 0,02 por milhão de milissegundos de CPU. O restante da página (planos de CDN/segurança, SASE, developer platform) é renderizado dinamicamente e não foi extraído.

## Tópicos

- **Free** — 100k req/dia, 10 ms CPU/req.
- **Paid** — US$ 0,30/M req + US$ 0,02/M CPU-ms.

## Pontos-chave

- Cobra CPU, não tempo de espera: chamadas a APIs externas quase não custam.
- 100 mil/dia grátis cobre um SaaS pequeno inteiro.

## Como aplicar

Backend leve do SaaS (webhooks, APIs) em Workers no Free; medir CPU-ms antes de estimar o Paid.

## 🍩 York diz

Isso é preço de moeda de um centavo: 100 mil requisições por dia de graça e depois trinta centavos por milhão. O truque é que cobram CPU — esperar API externa não custa. Um webhook do Resend rodando aqui é custo zero na prática.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

#### Workers

Serverless functions that run everywhere, instantly

| Component | Free | Paid | 
|---|---|---|
| Requests | 100k / day | $0.30 / million requests | 
| CPU Time | 10 ms / request | $0.02 / million CPU ms | 

Requests

100k / day

$0.30 / million requests

CPU Time

10 ms / request

$0.02 / million CPU ms

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
