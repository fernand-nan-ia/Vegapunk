---
item_id: "ca3f18bd-6401-4715-8a62-18c0f04381ae"
platform: article
external_id: "0d2c67bb789b"
canonical_url: "https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work-for-enterprise-plans"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: enriched
triage: null
tags: ["netlify", "plano-enterprise", "medidores-de-credito", "agent-runners", "custo-de-ia"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: baixa
  estudo_geral: media
confidence: alta
theme: negocios-e-financas
content_type: article
---

# Netlify — como os créditos funcionam nos planos Enterprise (mesma tabela dos planos self-serve)

🔗 https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work-for-enterprise-plans

## Resumo

Documentação dos créditos aplicados a planos Enterprise. O achado é que a tabela de consumo é idêntica à dos planos self-serve: deploy de produção 15 créditos, Deploy Preview e branch deploy zero, compute 10 créditos por GB-hora, inferência de IA 180 créditos por dólar de uso de modelo, banda 20 créditos por GB e requisições web 2 créditos a cada 10.000. O que muda no Enterprise é o contrato em volta, não o preço unitário do recurso. O documento detalha ainda que o uso dos Agent Runners aparece em dois medidores ao mesmo tempo: o custo do modelo de IA entra como inferência, e o ambiente em que o agente trabalha entra como compute. Requisições web incluem visualizações de página, chamadas de API, redirects, chamadas a funções serverless e requisições de asset. O resto da página é chamada comercial para falar com o time de vendas.

## Tópicos

- **Tabela de medidores** — Deploy de produção 15, preview e branch 0, compute 10 por GB-hora, IA 180 por dólar, banda 20 por GB, requisições 2 a cada 10.000.
- **Agent Runners contam duas vezes** — O modelo de IA usado no agente entra como inferência e o ambiente onde ele roda entra como compute.
- **O que conta como requisição web** — Visualização de página, chamada de API, redirect, chamada a função serverless e requisição de asset.

## Ferramentas citadas

- **Netlify**: plataforma cujo consumo de créditos em plano Enterprise é descrito

## Pontos-chave

- O preço unitário em crédito é o mesmo do Free ao Enterprise; o que muda é o contrato e o suporte.
- Agent Runners consomem dois medidores simultâneos, inferência e compute.
- Redirect conta como requisição web, o que costuma passar despercebido em site com muitas regras de redirecionamento.

## Como aplicar

Nada a fazer hoje. O valor do item é comparativo: confirma que a tabela de consumo não muda entre planos, então otimizar deploy e banda vale em qualquer patamar.

## 🍩 York diz

Enterprise com a mesma tabelinha do Free, veja só. O que eles vendem ali em cima é contrato e telefone do vendedor, não crédito mais barato. Guarda só a linha do redirect: ele conta como requisição, e site cheio de redirecionamento paga por isso sem ninguém perceber.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

Learn how credits work for Enterprise plans that use Credit-based metered billing. Credit-based metered billing is optimized for large-scale production workloads and AI development workflows. By using credits to measure and bill for usage, teams have flexible, predictable pricing that scales with their actual consumption.

### Credit usage for Enterprise plans

Section titled “Credit usage for Enterprise plans”
Here is how credit usage is calculated by Netlify’s metered billing for Enterprise plans. For more detailed and technical explanations of these usage meters, check out the in-depth documentation on each meter.

| Meter | Credit usage for Enterprise plans | Quick high-level description | 
|---|---|---|
| Production deploys | 15 credits each | Deploying your project to production, build minutes no longer calculated | 
| Deploy Previews or branch deploys | 0 credits | Free deployments for previewing, experimenting, and creating versions of your site/app | 
| Compute | 10 credits per GB-hour | The "processing power" your site/app needs to run things like serverless functions, scheduled functions, background functions, Preview servers, and Agent runners. Compute is made up of Functions & Agents compute and Database compute. | 
| AI inference | 180 credits per USD of AI model usage | The costs of running AI models and agents on Netlify, particularly for Agent Runners and AI Gateway | 
| Bandwidth | 20 credits per GB | Data sent out to the internet, such as assets hosted on Netlify or files downloaded from your site/app. Bandwidth is made up of Web bandwidth and Database bandwidth. | 
| Web requests | 2 credits per 10,000 requests | Web traffic requests to your site or app, includes page views, API calls, redirects, requests to serverless functions, asset requests | 

Note that Agent Runners usage appears in two meters: the AI model usage during an agent run counts toward AI inference, while the environment the agent works in counts toward Compute. Learn more in Pricing for AI features.

### Looking for flexible pricing, enhanced security and enterprise support?

Section titled “Looking for flexible pricing, enhanced security and enterprise support?”
Contact Sales to learn more.

##### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
