---
item_id: "ba7cdbb6-bdba-4721-a4d9-9e2589786692"
platform: article
external_id: "a7e3e9a3d6ba"
canonical_url: "https://openrouter.ai/docs/features/privacy-and-logging"
channel: "OpenRouter | Documentation"
captured_at: 2026-09-04
status: enriched
triage: null
tags: ["openrouter", "privacidade-de-dados", "opt-out-de-treino", "retencao-de-logs", "roteamento-regional", "lgpd", "vegapunk-bot"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: alta
confidence: alta
theme: seguranca-e-privacidade
content_type: article
---

# OpenRouter — política de treino, retenção de logs e roteamento em região

🔗 https://openrouter.ai/docs/features/privacy-and-logging

## Resumo

Documentação oficial do OpenRouter sobre como os provedores por trás da API tratam os prompts enviados. Cada provedor tem sua própria política de dados, e o OpenRouter expõe essas políticas como dado estruturado em cada endpoint. Na página de configurações da conta existe um controle para permitir ou barrar o roteamento a provedores que treinam com os dados do usuário, e esse controle é separado para modelos pagos e modelos gratuitos. Se o usuário opta por não treinar, o OpenRouter deixa de rotear para provedores que treinam, mas o texto avisa que isso não diz nada sobre o que o próprio OpenRouter faz com os prompts. Sobre retenção, o OpenRouter não roteia com base em política de retenção: ele apenas mostra a política de cada provedor nos termos, e cabe ao usuário ignorar quem não atende ao seu requisito. Para clientes enterprise há roteamento em região na União Europeia e nos Estados Unidos, com hostnames dedicados eu.openrouter.ai e us.openrouter.ai, garantindo que prompt e resposta não saiam da região escolhida. A lista de modelos disponíveis por região é consultada chamando /api/v1/models/user pelo hostname regional. O ponto central para quem manda conteúdo pessoal é que o opt-out de treino é uma configuração de conta que precisa ser marcada, não um padrão.

## Tópicos

- **Treino sobre prompts** — Configuração de conta decide se o roteamento pode ir a provedores que treinam com os dados; há toggles separados para modelos pagos e gratuitos. O opt-out não governa o que o próprio OpenRouter faz.
- **Retenção e logging** — O OpenRouter não altera roteamento por política de retenção; apenas expõe a política de cada provedor nos termos, cabendo ao usuário evitar quem não atende.
- **Roteamento em região (enterprise)** — Clientes enterprise podem processar prompts e respostas dentro da UE ou dos EUA via eu.openrouter.ai e us.openrouter.ai, sem que os dados saiam da região.
- **Lista de modelos por região** — Chamar /api/v1/models/user pelo hostname regional retorna quais modelos estão disponíveis naquela região.

## Ferramentas citadas

- **OpenRouter**: agregador de LLMs cujo painel de conta concentra os controles de treino e exibe a retenção de cada provedor
- **eu.openrouter.ai / us.openrouter.ai**: hostnames de roteamento em região para clientes enterprise

## Pontos-chave

- O opt-out de treino é uma configuração de conta e tem toggles separados para modelos pagos e gratuitos.
- Marcado o opt-out, o OpenRouter deixa de rotear para provedores que treinam com os dados.
- A documentação diz explicitamente que esse ajuste não governa o que o próprio OpenRouter faz com os prompts.
- Retenção de dados não é critério de roteamento: o OpenRouter só exibe a política de cada provedor.
- É possível restringir uma chamada individual a provedores que atendam a um requisito de política de dados.
- Roteamento dentro da UE ou dos EUA existe só para enterprise, mediante solicitação.
- Modelos gratuitos merecem toggle próprio porque são justamente os mais propensos a treinar com os prompts.

## Como aplicar

No Vegapunk, o bot manda transcrições e conteúdo pessoal do Fernando para o OpenRouter, então o opt-out de treino deve estar marcado nos dois toggles, pago e gratuito, mesmo o bot usando hoje só o gemini-3.7-flash pago. Isso também fecha a porta para um teste futuro com modelo :free virar vazamento silencioso. Para o SaaS, se um dia houver dado de cliente passando por LLM, a política de retenção do provedor e a base legal da LGPD precisam constar do contrato e da política de privacidade.

## 🪖 Shaka diz

Isto é documentação do fornecedor, não promessa auditada: vale como evidência do que ele se compromete a fazer, não do que faz. Duas frases importam. O opt-out não cobre o próprio OpenRouter, e o toggle dos gratuitos é separado, o que significa que um teste inocente com modelo :free entrega o teu vault para treino sem avisar. Marque os dois e trate retenção como risco residual, porque nada aqui é apagado a teu pedido.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Provider Policies

#### Training on Prompts

Each provider on OpenRouter has its own data handling policies. We reflect those policies in structured data on each AI endpoint that we offer. On your account settings page, you can set whether you would like to allow routing to providers that may train on your data (according to their own policies). There are separate settings for paid and free models. Wherever possible, OpenRouter works with providers to ensure that prompts will not be trained on, but there are exceptions. If you opt out of training in your account settings, OpenRouter will not route to providers that train. This setting has no bearing on OpenRouter’s own policies and what we do with your prompts.
#### Data Retention & Logging

Providers also have their own data retention policies, often for compliance reasons. OpenRouter does not have routing rules that change based on data retention policies of providers, but the retention policies as reflected in each provider’s terms are shown below. Any user of OpenRouter can ignore providers that don’t meet their own data retention requirements. The full terms of service for each provider are linked from the provider’s page, and aggregated in the documentation.
### Enterprise in-region routing

For enterprise customers, OpenRouter supports in-region routing in the EU and US. When enabled for your account, your prompts and completions are processed within the selected region and do not leave it. Use`https://eu.openrouter.ai` for EU requests or `https://us.openrouter.ai` for US requests. This feature is only enabled for enterprise customers by request.
**Regional models list**To see which models are available for regional routing, call

`/api/v1/models/user` through the corresponding regional hostname. Learn more

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
