---
item_id: "813217b3-cd32-4ae8-a9f4-b67f728fecb9"
platform: article
external_id: "363d9da06ada"
canonical_url: "https://docs.firecrawl.dev/billing"
channel: "Firecrawl Docs"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["firecrawl", "web-scraping", "api-billing", "rate-limits", "grok-api", "stripe"]
applicability:
  saas_pessoal: media
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Documentação de Cobrança e Créditos do Firecrawl

🔗 https://docs.firecrawl.dev/billing

## Resumo

O Firecrawl opera com um modelo de cobrança baseado em créditos, onde cada chamada de API consome créditos conforme o endpoint e as opções avançadas selecionadas. Requisições que utilizam recursos como formato JSON ou retenção zero de dados somam modificadores cumulativos ao custo base por página. É importante notar que chamadas com status de erro HTTP (como 403 ou 404) ainda consomem créditos integralmente devido à utilização da infraestrutura de renderização e proxy. Para jobs de crawl, a verificação prévia exige saldo equivalente ao limite total configurado, cujo valor padrão é de 10.000 páginas se não for explicitado. Os planos operam em formato de assinatura mensal ou anual em dólares, sem acúmulo de créditos não utilizados na maioria dos planos base. O recurso Smart Upgrade substitui a recarga automática antiga, realizando upgrades graduais pro-rata de categoria para evitar bloqueios por erro HTTP 402. Por fim, o scraping em URLs do X/Twitter utiliza a API Grok da xAI com uma precificação diferenciada de alto consumo de créditos por consulta.

## Tópicos

- **Consumo de créditos e modificadores** — Cada endpoint possui custo base e modificadores cumulativos (ex.: extração JSON e retenção zero) que encarecem o processamento por página.
- **Cobrança por infraestrutura e pre-flight check** — Erros 403/404 consomem créditos normalmente; rotinas de crawl exigem saldo prévio igual ao limit configurado (padrão de 10.000 se omitido).
- **Planos e ciclo de créditos** — Assinaturas mensais e anuais não acumulam créditos não utilizados por padrão, com exceção de planos Scale e Enterprise anuais.
- **Mecanismo Smart Upgrade** — Atualiza automaticamente o plano para o próximo nível cobrando apenas a diferença pro-rata em vez de taxas de overage avulsas.
- **Integração e custo para X (Twitter)** — Scraping de URLs do Twitter passa pela API do Grok (xAI) consumindo cerca de 30 a 34 créditos por requisição estruturada.

## Ferramentas citadas

- **Firecrawl**: API de web scraping, crawl e busca estruturada de dados da web para LLMs
- **Grok API**: API da xAI integrada para processamento e extração de dados do X/Twitter
- **Stripe**: Gateway responsável pelo portal de assinaturas, cupons e atualização fiscal

## Pontos-chave

- Requisições que retornam HTTP 403 ou 404 são cobradas integralmente porque utilizam a infraestrutura de proxy e browser.
- O parâmetro 'limit' em rotinas de crawl assume 10.000 por padrão e exige saldo equivalente total antes do início da execução.
- Modificadores de scraping são cumulativos (ex.: base 1 + JSON 4 + Zero Retention 1 = 6 créditos por página).
- Créditos mensais não utilizados expiram a cada ciclo, exceto em contratos anuais Scale (1 mês) e Enterprise (2 meses).
- O Smart Upgrade calcula a diferença pro-rata de mensalidade e injeta imediatamente o delta de créditos da nova categoria.
- Requisições para x.com utilizam a API Grok e custam a partir de 30 créditos por requisição.
- Verificações de status de jobs (polling) e histórico de uso via API não consomem créditos.

## Como aplicar

Ao integrar o Firecrawl via Claude Code para coleta de dados de concorrentes ou enriquecimento de dados no SaaS, defina explicitamente o parâmetro 'limit' em todas as chamadas de crawl para evitar erros 402 acidentais. Implemente o monitoramento do campo 'metadata.statusCode' para interromper retentativas automáticas em páginas bloqueadas.

## 📚 Pythagoras diz

O registro documenta com precisão a mecânica de créditos e infraestrutura do Firecrawl. Eu deduzo que omitir o parâmetro limit nos endpoints de crawl é o erro operacional mais crítico, pois travará sua execução exigindo 10.000 créditos de margem. Recomendo parametrizar os limites de coleta no seu código e tratar os retornos 403 para não queimar saldo à toa.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Overview

Firecrawl uses a
**credit-based billing system**. Every API call you make consumes credits, and the number of credits consumed depends on the endpoint and options you use. You get a monthly credit allotment based on your plan, and Smart Upgrade keeps you covered as your usage grows. For current plan pricing, visit the Firecrawl pricing page.

All Firecrawl invoices are billed in 

**US Dollars (USD)**, regardless of your billing address or payment method.
### Credits

Credits are the unit of usage in Firecrawl. Each plan includes a monthly credit allotment that resets at the start of each billing cycle. Different API endpoints consume different amounts of credits.
#### Credit costs per endpoint

#### Additional credit costs for scrape options

Certain scrape options add credits on top of the base cost per page:
These modifiers stack. For example, scraping a page with both JSON format and Zero Data Retention costs 

**1 + 4 + 1 = 6 credits**per page. These same modifiers apply to the Crawl and Search endpoints since they use scrape internally for each page. Requests to

`x.com` and other X/Twitter URLs use the Grok API and have separate pricing. See X (x.com) billing at the bottom of this page.
#### When credits are charged

Credits are charged whenever Firecrawl’s infrastructure processes a request, even if the target site returns an HTTP error status code such as 403 Forbidden or 404 Not Found. This is because the scraping infrastructure (browser rendering, proxy, etc.) is fully utilized regardless of the target site’s response. You can check the`metadata.statusCode` field in the API response to detect these cases and avoid retrying URLs that are consistently blocked.
For **batch scrape**and

**crawl**jobs, credits are billed asynchronously as each page completes processing — not when the job is submitted. This means there can be a delay between submitting a job and seeing the full credit cost reflected on your account. If a batch contains many URLs or pages are queued during high-traffic periods, credits may continue to appear minutes or hours after submission. Polling or checking batch status does not consume credits.

**Crawl pre-flight credit check:**Before a crawl job starts, Firecrawl verifies that your remaining credit balance can cover the full

`limit` parameter you’ve requested. If your balance is lower than `limit`, the request returns a 402 even if the crawl would have discovered fewer pages. The default `limit` is **10,000**, so omitting it requires 10,000 credits available up front. To avoid this, pass an explicit

`limit` that matches the number of pages you actually intend to crawl (e.g., `limit: 100`).
#### Tracking your usage

You can monitor your credit usage in two ways:
- **Dashboard** : View your current and historical usage at firecrawl.dev/app
- **API** : Use the Credit Usage and Credit Usage Historical endpoints to programmatically check your usage

We are actively working on improvements to make credit usage easier to understand. Stay tuned for updates.

### Plans

Firecrawl offers subscription-based monthly plans. There is no pure pay-as-you-go option, but Smart Upgrade (described below) provides flexible scaling on top of your base plan.
#### Paid plans

For needs beyond Scale, Firecrawl offers 

**Enterprise**plans with custom credits, dedicated support, SLAs, bulk discounts, zero-data retention, and SSO. Visit the Enterprise page for details.
**monthly**or

**yearly**billing. Yearly billing offers a discount compared to paying month-to-month. For current pricing on each plan, visit the pricing page.

#### Billing cycle

- **Monthly plans** : Credits reset on your monthly renewal date
- **Yearly plans** : You are billed annually, but credits still reset each month on your virtual monthly renewal date
- **Unused plan credits do not roll over by default** — your monthly allotment resets each month.**Annual Scale plans roll unused plan credits over 1 month** , and**annual Enterprise plans roll them over 2 months** .

#### Concurrent browsers

Concurrent browsers represent how many web pages Firecrawl can process for you simultaneously. Your plan determines this limit. If you exceed it, additional jobs wait in a queue until a slot opens. See Rate Limits for full details on concurrency and API rate limits.
### Smart Upgrade

Starting 

**June 1, 2026**, Smart Upgrade replaces Auto-Recharge. Instead of paying for overages, these payments now go toward your upgrades, giving you a seamless experience without disruptions.
#### Pro-ration examples

Suppose you’re on
**Hobby 6.5k**($28/month or $290/year) and Smart Upgrade moves you to

**Hobby 8k**($37/month or $390/year). You receive

**1,500 additional credits**immediately (the delta to 8k), and the upgrade charge depends on your billing cadence:

- **Monthly plan:** You’re billed the $37 − $28 =**$9** monthly difference today. Your renewal date is unchanged.
- **Yearly plan, 5 months remaining in your 12-month cycle:** You’re billed`(5 ÷ 12) × 100 ≈ $41.67` today, where the annual price difference is $390 − $290 = $100. The remaining 4 months on Hobby 8k are covered by this charge, and your renewal date is unchanged.

**Hobby 8k → Standard 100k**, billed at the difference between those two tiers ($62/month or $600/year, pro-rated the same way), with

**92,000 additional credits**added to your balance.

### Upgrading and Downgrading

- **Upgrades** take effect immediately. You are charged the full new-plan price today (no proration), and your billing cycle resets — your next renewal is one month or one year from the upgrade date. Any unused credits from your previous plan carry over, and your new credit allotment and concurrency limits apply right away.
- **Downgrades** are scheduled to take effect at your next renewal date. You keep your current plan’s credits and limits until then, and unused time on your current plan is not credited or refunded. You can undo a scheduled downgrade from your billing settings any time before the effective date.

#### Switching between monthly and yearly billing

- **Monthly → Yearly** at the same or higher credit tier is treated as an immediate upgrade.
- **Yearly → Monthly** is treated as an immediate upgrade only if you move to a strictly higher credit tier.

### Running Out of Credits

If you exhaust your credit allotment and do not have Smart Upgrade enabled, API requests that consume credits will return an
**HTTP 402 (Payment Required)**error. With

**Smart Upgrade**enabled, your subscription is automatically moved to the next credit tier and you receive the new tier’s credit allotment immediately, so requests keep flowing without interruption. Smart Upgrade stops once you reach the Scale tier. To resume usage after a hard stop, you can:

1. Enable Smart Upgrade to scale up automatically
2. Upgrade to a higher plan manually
3. Wait for your credits to reset at the next billing cycle

### Coupons

Firecrawl supports two types of coupons:
- **Subscription coupons** apply a discount to your plan subscription (e.g. a percentage off your monthly or yearly price). These can**only** be applied during the Stripe checkout flow when you first subscribe to a paid plan or change plans. You cannot apply a subscription coupon after checkout has completed.
- **Credit coupons** add bonus credits to your account. These can be redeemed from the**Billing** section of your dashboard at firecrawl.dev/app/billing. Look for the coupon input field on the billing page to apply your code. Bonus credits from credit coupons are separate from your plan’s monthly allotment and persist even if you upgrade or downgrade your plan.

### FAQs

### Do unused credits roll over to the next month?


Do unused credits roll over to the next month?

**Plan credits**do not roll over by default — your monthly allotment resets each month.

**Annual Scale plans roll unused plan credits over 1 month**, and

**annual Enterprise plans roll them over 2 months**.

### How is the Smart Upgrade charge calculated?


How is the Smart Upgrade charge calculated?

Smart Upgrade bills the pro-rated difference between your current tier and the next tier. On 

**monthly**plans, this is the monthly price difference. On**yearly**plans, it’s`(months remaining in your billing cycle ÷ 12) × annual price difference`, using full calendar months from the start of your current period. You also receive the delta in credits between the two tiers, so you only pay for what you gain.
### How do I know how many credits I have left?


How do I know how many credits I have left?

Check the dashboard at firecrawl.dev/app, or call the Credit Usage API endpoint programmatically.

### Where do I apply a coupon code?


Where do I apply a coupon code?

It depends on the coupon type. 

**Credit coupons**are applied in the Billing section of your dashboard.**Subscription coupons**(discounts on your plan price) can only be applied at the Stripe checkout page when subscribing or changing plans.
### I need more concurrency or a custom plan. Who do I contact?


Reach out to help@firecrawl.dev, or visit the Enterprise page to learn more about custom plans.

### What currency are invoices billed in?


What currency are invoices billed in?

All Firecrawl invoices are billed in 

**US Dollars (USD)**, regardless of your billing address or payment method.
### How do I manage my subscription, change plans, or cancel?


Go to your billing settings — team admins can manage everything there. Click 

**Manage Subscription**to open the billing portal and update your payment method, billing address, company name, or VAT number.To change plans, click**Change Plan**and pick a new tier. Upgrades take effect immediately; downgrades are scheduled for the end of your current billing period and can be undone until then — see Upgrading and Downgrading.To cancel, click**Cancel Subscription**. Your plan stays active until the end of your current billing period, and you can resume it before then.
### How do I add a VAT number, company name, or billing address to my invoices?


Go to your billing settings, click 

**Manage Subscriptions**, and update your billing address, company name, and VAT number in the Stripe portal. Future invoices will automatically include the updated details.To regenerate a past paid invoice with the new information:
1. Update your billing details in the Stripe portal first (see above).
2. Open the **Invoice history** tab in the Stripe portal and download the PDF for the invoice you want; Stripe re-renders it against your current billing info.
3. If an invoice doesn’t pick up the updated details, email help@firecrawl.dev with the invoice numbers and we’ll regenerate them for you.

### X (x.com) billing

Firecrawl uses the official
**Grok API**from xAI to provide AI-powered summarization, structured extraction, and real-time access to public X content. Requests to

`x.com`, `twitter.com`, and `mobile.twitter.com` profile and post URLs are handled through Grok’s authorized internal tools (`x_search`, thread fetch, and web search restricted to x.com) rather than traditional web scraping.
#### Credit costs

For example, processing a typical post or thread request costs 

**30 credits**(

`1` base + `29` Grok X Query) and returns Grok-generated structured data, thread context, and summaries. If JSON format (LLM extraction) is also enabled, the total is **34 credits**per request. This method complies with X’s published interfaces via xAI’s partnership and provides higher-quality, reasoned output instead of raw page scraping.

**Capabilities differ from standard scraping.**Grok returns AI-processed results, which may include summaries, key metrics, thread context, and more. For raw structured data at scale, use the official X Enterprise API.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
