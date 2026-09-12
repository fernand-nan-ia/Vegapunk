---
item_id: "b8980d30-9527-4095-9686-f0853685f1bf"
platform: article
external_id: "ef74dd3069e1"
canonical_url: "https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: enriched
triage: null
tags: ["netlify", "precificacao-por-credito", "custo-de-hospedagem", "plano-free", "deploy-de-producao", "banda", "limite-rigido", "custo-por-cliente"]
applicability:
  saas_pessoal: media
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
theme: negocios-e-financas
content_type: article
---

# Netlify — planos por crédito (Free 300, Personal US$ 9, Pro US$ 20) e o que cada recurso consome

🔗 https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans

## Resumo

Documentação oficial dos planos self-serve do Netlify no modelo de créditos, que substituiu a antiga cobrança por minuto de build e pacotes de uso. São três planos: Free a US$ 0 com 300 créditos por mês e limite RÍGIDO, sem recarga; Personal a US$ 9 com 1.000 créditos e recarga automática de 500 créditos por US$ 5; e Pro a partir de US$ 20 com 3.000 créditos, recarga de 1.500 por US$ 10 e opções de 5.000 a 20.000, sendo que só a partir de 5.000 os créditos não usados rolam para o mês seguinte. O consumo tem tabela fechada: cada deploy de produção custa 15 créditos, compute custa 10 créditos por GB-hora, banda custa 20 créditos por GB, requisições web custam 2 créditos a cada 10.000, e inferência de IA custa 180 créditos por dólar de modelo usado. O que NÃO é medido também está declarado e é a parte mais útil: Deploy Previews, branch deploys e deploys que falharam custam zero, e submissões de formulário são ilimitadas e gratuitas. Nos limites por plano, o Free tem 1 build concorrente, 1 único Team Owner, monitoramento de usuário real e web analytics só do dia corrente, 3 bancos e nenhuma proteção por senha; o Personal acrescenta detecção de segredo e janela de 24 horas; o Pro traz proteção por senha, audit log de 7 dias, variáveis de ambiente compartilhadas, membros ilimitados e janela de 30 dias. Todos os planos, inclusive o Free, incluem domínio próprio com SSL, Deploy Previews ilimitados, CDN global, funções serverless e limite de 500 projetos.

## Tópicos

- **Os três planos** — Free US$ 0 com 300 créditos e limite rígido; Personal US$ 9 com 1.000 e recarga de 500 por US$ 5; Pro a partir de US$ 20 com 3.000 e recarga de 1.500 por US$ 10.
- **Tabela de consumo** — Deploy de produção 15 créditos, compute 10 por GB-hora, banda 20 por GB, requisições 2 a cada 10.000 e inferência de IA 180 créditos por dólar de modelo.
- **O que não consome crédito** — Deploy Previews, branch deploys, deploys que falharam e submissões de formulário, estas últimas ilimitadas e gratuitas.
- **Rollover só no Pro grande** — Crédito mensal não usado só rola para o mês seguinte em planos Pro de 5.000 créditos ou mais, e expira um ciclo depois.
- **Limites do Free** — 1 build concorrente, 1 único Team Owner, analytics só do dia corrente, 3 bancos, sem proteção por senha, sem audit log e sem variáveis de ambiente compartilhadas.
- **O que todo plano tem** — Domínio próprio com SSL, Deploy Previews ilimitados, CDN global, funções serverless, deploy por Git/API/IA e teto de 500 projetos.
- **Builds concorrentes como add-on** — 1 build concorrente no Free e no Personal, 3 no Pro; cada build concorrente extra custa US$ 40 por mês.

## Ferramentas citadas

- **Netlify**: hospedagem cujo modelo de cobrança por créditos é detalhado
- **Pricing estimation calculator**: calculadora oficial do Netlify para estimar consumo de créditos de um projeto

## Pontos-chave

- Deploy de produção custa 15 créditos: os 300 do Free dão no máximo 20 publicações por mês, se nada mais consumir.
- Banda custa 20 créditos por GB, então os 300 créditos do Free equivalem a no máximo 15 GB de tráfego.
- Requisição é barata: 2 créditos a cada 10.000, ou seja, 1,5 milhão de requisições nos 300 créditos.
- Deploy Preview, branch deploy e deploy que falhou custam ZERO: dá para iterar à vontade sem gastar.
- Formulário do Netlify é ilimitado e gratuito em todos os planos.
- O Free tem limite rígido e não aceita recarga; Personal e Pro aceitam.
- Domínio próprio com SSL está incluído até no Free.
- Proteção por senha só existe no Pro, o que elimina a ideia de prévia protegida em plano barato.
- Build concorrente extra custa US$ 40 por mês, o add-on mais caro da lista.
- Minuto de build deixou de ser cobrado: o que se paga agora é o ato de publicar.

## Como aplicar

Esta é a tabela que decide em que plano o site do cliente vive. No Free, 15 créditos por publicação significam no máximo 20 deploys de produção por mês; como Deploy Preview custa zero, o fluxo certo é iterar em preview e publicar pouco. Antes de cobrar de um cliente, some: hospedagem no Free é US$ 0 mas com limite rígido, e o Personal a US$ 9/mês é o seguro contra o site sair do ar.

## 🍩 York diz

Olha o número que interessa, docinho: 15 créditos por publicar. São 20 deploys no mês e acabou a festa. Mas preview custa ZERO, então erre à vontade em preview e publique só quando estiver bonito. E anota: US$ 9 por mês é menos que um lanche e é o que separa o site do cliente de uma página dizendo que ele não existe.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

Netlify's Credit-based pricing plans are optimized to simplify metered & usage-based billing and work smoothly with AI development workflows. By using credits to measure and bill for usage, Netlify users have fewer metrics to track and more flexibility on how to optimize their spending.

Learn about our standard self-serve Credit-based plans in this doc, such as the Free, Personal, and Pro plans. If you're interested in an Enterprise plan, check out how credits work for Enterprise plans.

### About Credit-based plans

Section titled “About Credit-based plans”
Netlify's Credit-based plans currently include the Free plan, Personal plan, and Pro plan. If you're interested in an Enterprise plan, contact our Sales team.

Netlify's Credit-based plans have 3 main components to understand:

- Monthly credit allotment included in your Netlify Credit-based monthly plan subscription, such as 300 credits for the free plan.
- Optional add-ons or features you pay for beyond your monthly plan subscription, such as domain registrations & renewals, concurrent builds, and billable team member seats. The add-ons available to you depend on your pricing plan.
- Certain features are only available to certain plans or have plan-specific limits

Compare this to previous pricing plans that included usage packages, lots of different kinds of add-ons, tier levels, and a lot more metered billing complexity. Credit-based plans were designed to simplify your billing experience.

#### Quick reference for learning resources

Section titled “Quick reference for learning resources”
| I want to | Optimized resources | 
|---|---|
| Compare to previous pricing plans | Official Blog | 
| Understand pricing plan highlights | Netlify pricing page | 
| Understand how credits work | How credits work | 
| Compare plans across features with a detailed breakdown | Check out the tables in this doc for a detailed breakdown of credit usage for each feature. | 
| Predict my credit usage | Pricing estimation calculator | 
| Find Enterprise plan details | How credits work for enterprise plans, the official Netlify pricing page, or reach out to our Sales team. | 

### Credit basics

Section titled “Credit basics”
To learn more about how credits work conceptually, check out how credits work.

#### Monthly plan credits

Section titled “Monthly plan credits”
Monthly plan credits are included with your plan each billing cycle and reset at the start of each cycle. Unused monthly credits do not roll over, except on Pro plans with 5,000 or more monthly credits, which are eligible for rollover credits.

Learn more about monthly plan credits.

| Feature | Free | Personal | Pro | 
|---|---|---|---|
| Monthly subscription price | $0/month | $9/month | Starts at $20/month | 
| Monthly credits | 300 credits/month with credit hard limit | 1,000 credits/month with auto recharge option | Starts at 3,000 credits/month with auto recharge option, offers other monthly credit options, from 5,000 to 20,000 | 
| Ability to buy more credits with auto recharge | Hard limit so no recharge option | **✓**500 credits for $5 | **✓**1,500 credits for $10 | 

#### Rollover credits

Section titled “Rollover credits”
If you have a Pro plan with 5,000 or more monthly credits, any unused monthly credits from the previous billing cycle carry forward automatically as rollover credits. Rollover credits expire at the end of the billing cycle they roll into, so they last for one extra month. If you used all your monthly credits in a cycle, nothing rolls over.

Learn more about rollover credits.

#### Add-on credits

Section titled “Add-on credits”
Add-on credits describe other ways to collect credits beyond the monthly credit plans.

When you purchase extra credits through auto recharge or in credit packs, these credits will not have a set expiration date.

Other credits granted, such as through promotions or Hackathon events, will likely have an expiration date set once they are issued.

Learn more about buying more credits.

#### Credit usage by metered feature area

Section titled “Credit usage by metered feature area”
Learn how metered features consume credits. You can also explore a credit use estimate for your project using our pricing estimation calculator.

##### AI inference

Section titled “AI inference”
AI inference measures your usage of AI features. AI inference is broken down by feature and consumes credits at the same rate for both:

| Feature/resource | Unit | Credits Consumed | What this covers | 
|---|---|---|---|
| Agent Runners AI inference | AI model usage in USD (US Dollar) | 180 credits per $1 USD | Costs of AI models used by Agent Runners. | 
| AI Gateway AI inference | AI model usage in USD (US Dollar) | 180 credits per $1 USD | Costs of AI models used through AI Gateway. | 

To learn more about how AI inference pricing works, check out our docs on AI inference pricing.

To check rates for using AI models, check out our Pricing per AI model table.

##### Compute & Processing

Section titled “Compute & Processing”
| Feature/resource | Unit | Credits Consumed | What this covers | 
|---|---|---|---|
| Functions compute | 1 GB-hour | 10 credits | Serverless functions, scheduled functions, background functions | 
| Preview server compute | 1 GB-hour | 10 credits | Preview servers | 
| Agent Runners compute | 1 GB-hour | 10 credits | Agent Runners | 
| Database compute | 1 GB-hour | 10 credits | Netlify Database compute resources | 

Learn more in how credits work.

##### Traffic & Delivery

Section titled “Traffic & Delivery”
| Feature/resource | Unit | Credits Consumed | What this covers | 
|---|---|---|---|
| Web Requests | 10,000 requests | 2 credits | All traffic to your site, includes edge functions | 
| Web Bandwidth | 1 GB transferred | 20 credits | Data delivery to your visitors worldwide | 
| Database Bandwidth | 1 GB transferred | 20 credits | Data transferred to and from your Netlify Database | 

Learn more in how credits work.

##### Platform Features

Section titled “Platform Features”
| Feature/resource | Unit | Credits Consumed | What this covers | 
|---|---|---|---|
| Form Submissions | Unlimited | Free | Netlify's highly customizable forms service with spam protection support available. | 
| Production Deployments | 1 deployment | 15 credits | Publishing your web project live to your production branch. Production deploys consume 15 credits. If you have locked your project to an older production deploy, only published production deploys will still cost 15 credits. | 

Learn more in our docs on form submissions and production deploys.

##### Non-metered functionality

Section titled “Non-metered functionality”
Note that some functionality is not metered by credits, such as:

- Deploy previews for experimenting and previewing changes
- Branch deploys for longer-term testing or maintaining different versions of your project
- Failed deploys

### Compare Credit-based plans

Section titled “Compare Credit-based plans”
For highlights of how Credit-based plans compare, check out the official Netlify pricing page.

#### Monthly credit allowance

Section titled “Monthly credit allowance”
| Feature | Free | Personal | Pro | 
|---|---|---|---|
| Monthly subscription price | $0/month | $9/month | Starts at $20/month | 
| Monthly credits | 300 credits/month with credit hard limit | 1,000 credits/month with auto recharge option | 3,000 credits/month with auto recharge option | 
| Rollover credits | No | No | Available on Pro plans with 5,000+ monthly credits | 
| Ability to buy more credits with auto recharge | N/A | **✓**500 credits for $5 | **✓**1,500 credits for $10 | 

#### Add-ons

Section titled “Add-ons”
| Feature | Free | Personal | Pro | 
|---|---|---|---|
| Concurrent builds | 1 concurrent build included in plan, meaning only 1 build can run at the same time. | 1 concurrent build included in plan with option to purchase more. Limited to 3 concurrent builds, meaning up to 3 builds can run at the same time. Ideal for using multiple agents and running projects that depend on each other. Add 1 additional concurrent build as an add-on at $40/month | 3 concurrent builds included in plan subscription, with $40/month per each additional concurrent build added. No concurrent build limit. | 
| Team members** | N/A | N/A | Unlimited (included in plan) | 
| Domain registrations & renewals | **✓** | **✓** | **✓** | 

*Note that a concurrent build is a build that can run simultaneously with other builds. 1 concurrent build means that you can only run one build at a time for your entire Netlify team. **Learn more about adding team members to your team in our Manage team roles docs.

#### Limits

Section titled “Limits”
| Feature | Free | Personal | Pro | 
|---|---|---|---|
| Real user monitoring | Available for current/past day | Available for past 24 hours | Available for past 30 days | 
| Web analytics | Available for current/past day | Available for past 24 hours | Available for past 30 days | 
| Concurrent builds* | Limited to 1 concurrent build. | 1 concurrent build included in plan with option to purchase more. No concurrent build limit. | 3 concurrent builds included in plan. Option to purchase more. No concurrent build limit. | 
| Project count limit | 500 projects | 500 projects | 500 projects | 
| Team Owner count | Only 1 Team Owner | Only 1 Team Owner | Unlimited Team Owners (included in plan) | 
| Live Preview Server | 1 Live Preview Server at any time per team account | 1 Live Preview Server at any time per team account | 1 Live Preview Server at any time per team account $15 a month per each new additional Live Preview Server Ability to customize the size. | 
| Netlify Database | 3 databases, 20 active branches, 7-day backup retention | 5 databases, 100 active branches, 7-day backup retention | 50 databases, 300 active branches, 30-day backup retention | 

*Note that a concurrent build is a build that can run simultaneously with other builds. 1 concurrent build means that you can only run one build at a time for your entire Netlify team.

#### Collaboration features

Section titled “Collaboration features”
| Feature | Free | Personal | Pro | 
|---|---|---|---|
| Shared environment variables | N/A | N/A | **✓** | 
| Audit logs | N/A | N/A | **✓** with 7-day history | 
| Team Owner limit | Only 1 Team Owner | Only 1 Team Owner | Unlimited Team Owners (included in plan) | 
| Team-based workflows | Limited | Limited | Designed for team-based workflows with unlimited collaborators included in plan | 
| Organization-owned private repos | N/A | N/A | **✓** | 
| Git Contributors* can commit to project through public/open source repositories | **✓** , unlimited | **✓** , unlimited | **✓** , unlimited | 
| Git Contributors* can commit to project through private repositories | N/A | N/A | **✓** Unlimited (included in plan) | 
| Add people to Netlify Reviewer role** | **✓**Unlimited reviewers | **✓**Unlimited reviewers | **✓**Unlimited reviewers | 
| Add people to Netlify Developer role** | N/A | N/A | **✓**Unlimited (included in plan) | 
| Add people to Netlify Billing Admin role** | N/A | N/A | **✓** | 
| Add people to Netlify Team Owner role** | N/A | N/A | **✓** | 
| Slack notifications via our Netlify App for Slack | N/A | N/A | **✓** | 

*Note that known bots like Renovate or Claude will not count as a Git contributor. Learn more about Git Contributors.

**Learn more about adding members to your team in our Manage team roles docs.

#### Security-related features

Section titled “Security-related features”
| Feature | Free | Personal | Pro | 
|---|---|---|---|
| Private projects | **✓**Owner only | **✓**Owner only | **✓**Invite unlimited members | 
| Audit logs | N/A | N/A | **✓** with 7-day history | 
| Password protection | N/A | N/A | **✓** | 
| Smart secret detection | N/A | **✓** | **✓** | 
| Basic authentication headers | N/A | N/A | **✓** | 
| Organization-owned private repos | N/A | N/A | **✓** | 
| Slack notifications | N/A | N/A | **✓** | 

#### Featured observability features

Section titled “Featured observability features”
| Feature | Free | Personal | Pro | 
|---|---|---|---|
| Real user monitoring | Available for current/past day | Available for past 24 hours | Available for past 30 days | 
| Web analytics | Available for current/past day | Available for past 24 hours | Available for past 30 days | 

#### Storage features

Section titled “Storage features”
| Feature | Free | Personal | Pro | 
|---|---|---|---|
| Netlify Blobs (Beta) | **✓** | **✓** | **✓** | 
| Netlify Database | **✓** | **✓** | **✓** | 

#### Core features available to all plans

Section titled “Core features available to all plans”
| Feature | Free | Personal | Pro | 
|---|---|---|---|
| Deploy from AI, Git, or API | **✓** | **✓** | **✓** | 
| Project count limit | 500 projects | 500 projects | 500 projects | 
| Support | Standard email support | Priority email support | Priority email support | 
| Custom domains with SSL support | **✓** | **✓** | **✓** | 
| Unlimited Deploy Previews | **✓** | **✓** | **✓** | 
| Serverless functions & storage | **✓** | **✓** | **✓** | 
| Global CDN for fast & reliable performance | **✓** | **✓** | **✓** | 
| Live preview URLs | **✓** | **✓** | **✓** | 

### Credit-based plan summaries

Section titled “Credit-based plan summaries”
Each plan summary below covers its starting price, credits, and headline features. For a full feature-by-feature breakdown, check out the comparison tables above, the official Netlify pricing page, or the Pricing estimation calculator.

#### Free plan

Section titled “Free plan”
$0/month, forever, for 300 credits/month with a hard limit and no auto recharge option.

You'll never be charged for the Free plan, so it's ideal for smaller experiments that don't need a lot of resources, security, or monitoring. It includes core building blocks like deploying from AI, Git, or API, unlimited deploy previews, Agent Runners, Netlify Database and Blob storage, and global CDN delivery.

See the full plan comparison on the Netlify pricing page.

#### Personal plan

Section titled “Personal plan”
$9/month for 1,000 credits/month, with an auto recharge option (500 credits for $5) if you go over your monthly credits.

The personal plan is optimized for one-person teams that are building in public in open source or public repositories. Or solo developers working with AI workflows whose projects are starting to need more resources, security, privacy, and monitoring insights.

You can keep costs predictable by keeping auto recharge off for when your monthly credits run out. To keep your web projects active when they go over your monthly plan credits, you can enable auto recharge. Learn more about auto recharge.

#### Pro plan

Section titled “Pro plan”
Starts at $20/month for 3,000 credits with unlimited team seats, with monthly credit options up to 20,000 credits and rollover credits included at 5,000 credits or higher.

Every Pro plan tier includes everything in the Personal plan, plus private projects with unlimited Team seats, shared environment variables, support for connected private repos, 30-day real user monitoring and web analytics, priority email support, audit logs, password protection, and 3+ concurrent builds.

The Pro plan is optimized for the following:

- solo developers needing more professional support
- multi-person teams needing collaboration tools that scale
- people needing to build in private repositories with additional security or privacy requirements

##### Credits

Section titled “Credits”
The Pro plan offers different monthly credits for your needs. If your projects experience seasonal surges in usage or just have high usage rates, you may find higher monthly credits a better fit.

In addition, if you choose monthly credits 5,000 or higher, any remaining monthly credits can roll over and be used for an additional billing cycle.

| Monthly credits | Price | Rollover | 
|---|---|---|
| 3,000 | $20/mo | No | 
| 5,000 | $33/mo | Yes | 
| 10,000 | $63/mo | Yes | 
| 15,000 | $95/mo | Yes | 
| 20,000 | $126/mo | Yes | 

##### Change monthly credits on the Pro plan

Section titled “Change monthly credits on the Pro plan”
You can change your monthly credits for the Pro plan as many times as you like but downgrading only takes effect at the start of your next billing cycle.

When upgrading to a Pro plan with more monthly credits, you can expect the following:

- Your billing cycle resets
- your upgrade takes effect immediately, no matter where you are in your billing cycle
- You’ll get a prorated refund from your previous plan (similar to when you upgrade from a Personal plan to a Pro plan)

When you downgrade to a Pro plan with less monthly credits, you can expect the following:

- The downgrade is scheduled at the end of the billing cycle. You continue to enjoy the features until then. (Also, applies when downgrading to a personal or free plan.)
- Any unused monthly plan credits, including rollover credits, are removed from your account once the downgrade takes effect. Credits from credit packs or auto recharge aren’t affected and remain available.
- The billing cycle isn’t affected since downgrading is scheduled based on your current billing cycle.

For example, if you downgrade your Pro plan monthly credits from 5,000 credits or higher to the base 3,000 credits or another plan, any unused monthly plan credits, including rollover credits, are removed from your account once the downgrade takes effect.

As a Team Owner, to change your monthly credits for the Pro plan:

1. Go to **Usage & billing  Plan details** .

Learn more in Change your pricing plan.

##### Auto recharge

Section titled “Auto recharge”
You can keep costs predictable by keeping auto recharge off for when your monthly credits run out. To keep your web projects active when they go over your monthly plan credits, you can enable auto recharge. Learn more about auto recharge.

##### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
