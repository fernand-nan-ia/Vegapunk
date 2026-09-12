---
item_id: "2b10ec02-d240-45c0-8ffd-e0c05dfb501b"
platform: article
external_id: "b53e9d3c7168"
canonical_url: "https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: enriched
triage: null
tags: ["netlify", "limite-rigido", "site-fora-do-ar", "recarga-automatica", "pacote-de-credito", "risco-operacional", "site-de-cliente"]
applicability:
  saas_pessoal: media
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
theme: negocios-e-financas
content_type: article
---

# Netlify — como os créditos funcionam: o limite rígido do Free tira o site do ar

🔗 https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work

## Resumo

Documento operacional sobre o funcionamento dos créditos nos planos Free, Personal e Pro. A frase que decide tudo está logo no começo: quando o saldo de créditos acaba, TODOS os projetos da conta são pausados e quem visitar qualquer URL encontra uma página 'Site not available'. O Free tem 300 créditos por mês com limite rígido e nenhuma forma de recarregar; Personal e Pro podem comprar mais. O saldo é consumido na ordem de expiração, começando pelos créditos que vencem antes e terminando nos que não vencem, como pacotes comprados e sobras de recarga automática. Créditos mensais não acumulam, exceto em planos Pro de 5.000 ou mais, onde as sobras valem um ciclo extra. Há dois jeitos de comprar mais: pacotes de crédito, que rolam para meses futuros, e recarga automática, que repõe o saldo em pequenos incrementos quando ele zera — 500 créditos por US$ 5 no Personal e 1.500 por US$ 10 no Pro. A recarga automática é decisão de Team Owner, vem desligada por padrão e vale para a conta inteira, não dá para ligar só num projeto. A tabela de consumo repete a dos outros documentos: deploy de produção 15 créditos, Deploy Preview e branch deploy zero, compute 10 por GB-hora.

## Tópicos

- **O que acontece quando zera** — Todos os projetos da conta são pausados e cada URL passa a exibir uma página 'Site not available' para os visitantes.
- **Ordem de consumo do saldo** — Gasta primeiro o crédito que expira antes e por último o que não expira, como pacotes comprados e sobras de recarga.
- **Pacotes de crédito** — Compra avulsa a qualquer momento, sem data de expiração, e rola para os meses seguintes.
- **Recarga automática** — Repõe o saldo quando ele zera, a 500 créditos por US$ 5 no Personal e 1.500 por US$ 10 no Pro; só o Team Owner liga, vem desligada e vale para a conta inteira.

## Ferramentas citadas

- **Netlify**: plataforma cujo mecanismo de saldo, pausa e recarga é descrito

## Pontos-chave

- Saldo zerado pausa TODOS os projetos da conta, não só o que consumiu.
- O visitante não vê erro genérico: vê uma página 'Site not available' com cara de site morto.
- O Free não tem recarga: acabou, acabou até o próximo ciclo.
- A recarga automática não pode ser ligada por projeto, só para a conta toda.
- Créditos comprados em pacote não expiram e são os últimos a serem gastos.
- Sobra de crédito mensal só acumula em Pro de 5.000 ou mais, por um ciclo.

## Como aplicar

Este é o risco a tratar ANTES de pôr cliente pagante em conta Free: um projeto que estoure o saldo derruba todos os outros da mesma conta, inclusive os dos outros clientes, e o visitante vê uma página dizendo que o site não existe. Duas saídas: Personal a US$ 9 com recarga automática ligada, ou uma conta separada por cliente para isolar o risco.

## 🍩 York diz

Presta atenção nesta, porque é a única que pode te custar um cliente: zerou o saldo, TODOS os sites da conta caem juntos, e o coitado do dono do café vai ver 'Site not available' na porta da loja dele. Nove dólares por mês, querido. É meio lanche. Ou então uma conta por cliente, e aí quem afunda afunda sozinho.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

Netlify's Credit-based pricing plans are optimized to simplify metered & usage-based billing and work smoothly with AI development workflows. By using credits to measure and bill for usage, Netlify users have fewer metrics to track and more flexibility on how to optimize their spending.

Learn how credits work for our standard pricing plans in this doc. Credit-based standard plans include the Free, Personal, and Pro plans. To learn how credits work for Enterprise plans, check out How credits work for enterprise plans.

### Monthly credit allotment

Section titled “Monthly credit allotment”
Each Credit-based plan includes a monthly credit allotment that a web project will use for that month's billing cycle. Some features are also only available on certain plans or have different limits across the Credit-based pricing plans.

| Free | Personal | Pro | 
|---|---|---|
| 300 credits/month | 1,000 credits/month | Starts at 3,000 credits/month with more options | 
| Hard limit | Option to purchase more credits | Option to purchase more credits | 

Once your credit balance is completely used up, all of your web projects (sites/apps) are paused and visitors to your web projects will find a `Site not available` page at each of your web project’s URLs.

#### Credit balance usage order

Section titled “Credit balance usage order”
Your credit balance will be used up in the order that your credits expire, starting with credits that will expire the soonest and then ending with credits that do not expire, such as credit packs or any remaining credits from auto recharge.

#### Monthly plan credits

Section titled “Monthly plan credits”
Monthly plan credits are included with your plan each billing cycle. The balance resets at the start of each cycle.

In general, monthly plan credits do not roll over, but if you have a Pro plan with 5,000 monthly credits or higher, then any leftover credits can roll over for an additional month. Learn more about rollover credits.

#### Other ways to get credits

Section titled “Other ways to get credits”
While your monthly credits reset after each month, other credits can have their own expiration date or no expiration date and they can be issued on demand, such as when you buy credit packs or through a special one-time promotion or Hackathon event.

#### Rollover credits

Section titled “Rollover credits”
If you have a Pro plan with 5,000 monthly credits or higher, then unused monthly credits from the previous cycle are carried forward automatically as rollover credits. If you used all your monthly credits last cycle, nothing rolls over.

### Buying more credits

Section titled “Buying more credits”
If you have a Personal or Pro plan, you have two options to buy more credits:

#### Buy credit packs

Section titled “Buy credit packs”
You can purchase additional credits at any time. Credits bought in credit packs roll over for future months.

Learn more about buying credit packs.

#### Auto recharge

Section titled “Auto recharge”
Control your spend and keep your web projects active by enabling auto recharge. Auto recharge automatically reloads your credit balance when it runs out with small increments of credits only when your projects need it.

Auto recharge can only be enabled or disabled by a Team Owner for all web projects on a team and is turned off by default for all projects. If you are on a Pro plan, you can also add additional Team Owners to your team.

If you have a Personal or Pro plan and you've enabled auto recharge, the payment method saved to your Netlify team account will be charged at these rates when your credit balance runs out:

| Free | Personal | Pro | 
|---|---|---|
| N/A | 500 credits for $5 | 1,500 credits for $10 | 

Only Team Owners can enable or disable auto recharge for all web projects on a team. You cannot enable auto recharge for only a specific project on a team.

For guided steps on enabling auto recharge, check out Configure auto-recharge.

### Credits usage for metered billing

Section titled “Credits usage for metered billing”
Here is how credit usage is calculated by Netlify’s metered billing at a high-level. For more detailed and technical explanations, check out the sections below.

| Feature | Credit usage | Quick high-level description | 
|---|---|---|
| Production deploys | 15 credits each | Deploying your project to production, build minutes no longer calculated | 
| Deploy Previews or branch deploys | 0 credits | Free deployments for previewing, experimenting, and creating versions of your site/app | 
| Compute | 10 credits per GB-hour | The "processing power" your site/app needs to run things like serverless functions, scheduled functions, background functions, Preview servers, and Agent Runners. Compute is made up of Functions compute, Preview server compute, Agent Runners compute, and Database compute. | 
| AI inference | 180 credits per USD of AI model usage | The costs of running AI models and agents on Netlify, particularly for Agent Runners and AI Gateway. | 
| Netlify Forms submissions | Free for all credit plans | Netlify’s highly customizable forms service with spam protection support available | 
| Bandwidth | 20 credits per GB | Data sent out to the internet, such as assets hosted on Netlify or files downloaded from your site/app. Bandwidth is made up of Database bandwidth and Web bandwidth. | 
| Web requests | 2 credits per 10,000 requests | Web traffic requests to your site or app, includes page views, API calls, redirects, requests to serverless functions, asset requests | 

Explore pricing estimates for various combinations of Netlify’s features and services with our Pricing estimation calculator.

#### Credit usage for production deploys

Section titled “Credit usage for production deploys”
Production deploys are a type of deploy that is optimized to work as the finalized version of your web project that shows up at your primary domain and is live on the web. Your primary domain can be a custom domain, such as `mycompany.com`, or your Netlify default URL, such as `MY-PROJECT-NAME.netlify.app`.

Netlify supports three types of deploys:

- Production deploys for finalized and production-ready released versions of your web project
- Deploy Previews for reviewing and experimenting with changes before they are released
- Branch deploys for reviewing and experimenting with changes from specific branches or for maintaining different versions of your project

Deploy Previews and branch deploys are optimized to work as preview environments for reviewing and experimenting.

With Credit-based pricing plans, each successful production deploy consumes 15 credits during that month's billing cycle and you have free deployments for previewing, experimenting, and creating versions of your site/app.

Failed deploys and rolling back a production deploy to a previous production deploy does not consume credits.

Learn more about Netlify’s deploy types.

#### Credit usage for compute

Section titled “Credit usage for compute”
Compute is the amount of resources used by your functions, Preview servers, Agent Runners, and Netlify Database, and represents the "processing power" your site/app needs.

Compute is measured in GB-hours and includes:

- **Functions compute** : measures usage for Serverless Functions, Scheduled Functions, and Background Functions
- **Preview server compute** : measures usage for Preview servers
- **Agent Runners compute** : measures usage for Agent Runners
- **Database compute** : measures usage for Netlify Database

At a high-level, compute represents the amount of data transfer in gigabytes needed in an hour.

Compute consumes 10 credits per GB-hour. A GB-hour represents a combination of memory allocation and execution time, creating a more transparent way to understand and manage your resource usage. We use this metric on our credit plans, instead of charging per invocation, because it more accurately reflects the compute resources reserved to run your functions. This means we multiply the amount of time your functions run by the memory they are allocated during the billing cycle.

##### Functions compute

Section titled “Functions compute”
Functions compute is the amount of resources used by your functions. This includes the following features:

- Serverless Functions
- Scheduled Functions - Functions triggered on a schedule
- Background Functions - Long-running background tasks

Note that Edge functions don't contribute to the compute usage metric. Edge functions are measured through web requests.

##### Preview server compute

Section titled “Preview server compute”
Preview server compute is the amount of resources used by your Preview servers, which are live preview environments for your site/app.

##### Agent Runners compute

Section titled “Agent Runners compute”
Agent Runners compute is the amount of resources used by the environment your Agent Runners work in while an agent run is active. The AI model usage during an agent run is billed separately through the AI inference meter.

##### Database compute

Section titled “Database compute”
Netlify Database uses Database compute, which is measured in GB-hours.

#### Credit usage for forms submissions

Section titled “Credit usage for forms submissions”
Netlify’s web forms service is free and unlimited for all credit-based plans.

We recommend taking measures to help prevent abuse of your project. For example, you can reduce form submission spam by adding a reCAPTCHA 2 challenge and honeypot field.

#### Credit usage for AI inference

Section titled “Credit usage for AI inference”
AI inference is a usage meter that measures the costs of using AI models and agents on Netlify through Agent Runners and the AI Gateway.

AI inference is measured based on the costs set by AI model providers, which convert AI model usage tokens to USD. Netlify then converts every $1 USD spent on AI model usage to 180 Netlify credits.

You can set an AI Credit Usage Limit that tracks AI inference from Agent Runners specifically. Note that on Enterprise plans, the AI Credit Usage Limit factors in AI inference from both Agent Runners and AI Gateway.

To learn more about how AI inference pricing works, check out our docs on AI inference pricing.

#### Credit usage for bandwidth

Section titled “Credit usage for bandwidth”
Bandwidth is the amount of data traffic your site or app sends out to the internet.

Bandwidth consumes 20 credits per GB used and includes:

- Web bandwidth
- Database bandwidth

##### Web bandwidth

Section titled “Web bandwidth”
Web bandwidth is the amount of data traffic your project sends out to the internet. This includes the following features:

- Assets & web content served - All static assets hosted on Netlify, HTML, CSS, JavaScript files served to visitors
- Image serving - Images served through Netlify's CDN
- File downloads - Any files downloaded from your site/web project
- API responses - Data served through serverless functions
- Large Media (Deprecated) - Git LFS files served through Netlify Large Media

##### Database bandwidth

Section titled “Database bandwidth”
Database bandwidth is the amount of data traffic generated by Netlify Database.

#### Credit usage for web requests

Section titled “Credit usage for web requests”
Web requests are web traffic requests to your site/app, including requests to your site's main (production) URL, as well as to any active branch deploys and Deploy Previews.

A web request is counted whenever a user or system accesses content hosted on your project. This includes requests for HTML pages, images, JavaScript, CSS files, and other static assets.

Web requests use 2 credits per 10 thousand (10,000) requests.

Features that use web requests include:

- Page views - Each visitor request to your site/app pages
- API calls - Requests to your serverless functions
- Asset requests hosted by Netlify - Requests for CSS, JavaScript, images, and other static files hosted by Netlify
- Redirects
- Edge functions

### Monitor credit usage

Section titled “Monitor credit usage”
For help monitoring your web project's credit usage, check out Monitor credit usage.

### Calculate common usage patterns

Section titled “Calculate common usage patterns”
Use our Pricing calculator to calculate common usage patterns.

Get more of your questions answered, such as "What happens when credits are used up?" in our Billing FAQ for Credit-based plans.

##### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
