---
item_id: "efc31c79-2ffe-4fc0-a548-d050435288d2"
platform: article
external_id: "0df3a8ca9ce9"
canonical_url: "https://uptimerobot.com/api/v3"
channel: "uptimerobot.com"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["uptimerobot", "api", "monitoramento", "rate-limit", "healthcheck"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# UptimeRobot — API REST v3: monitores, contatos, manutenção e status pages; rate limits; três tipos de chave

🔗 https://uptimerobot.com/api/v3

## Resumo

A API do UptimeRobot (JSON) permite consultar, criar, editar e apagar monitores, contatos de alerta, janelas de manutenção e status pages. Rate limits por plano: Free 10 req/min; Pro = limite de monitores × 2 por minuto (máx. 5.000/min); 429 com cabeçalhos X-RateLimit-Limit/Remaining/Reset e Retry-After. Autenticação HTTP Basic com três tipos de chave: da conta (tudo), específica de monitor (só getMonitors daquele monitor) e somente leitura (todos os get*). Chaves na página Integrations.

## Tópicos

- **Recursos** — Monitores, contatos, manutenção, status pages.
- **Limites** — Free 10/min; Pro monitores×2/min; 429 + cabeçalhos.
- **Chaves** — Conta, por monitor, somente leitura.

## Pontos-chave

- Chave somente leitura serve para a York consultar uptime sem risco.
- 10 req/min no Free — cachear no healthcheck.
- Criar monitor por API ao publicar um site de cliente.

## Como aplicar

Healthcheck da York lendo uptime via chave somente leitura; script que cria monitor ao publicar site.

## 🔧 Atlas diz

Chave somente leitura + 10 requisições por minuto = a York pergunta 'está de pé?' uma vez por healthcheck e pronto. E dá para criar o monitor por script quando um site novo sobe — parafuso que evita esquecer.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### UptimeRobot REST API.

UptimeRobot has an easy-to-use API. It lets you get the details of your monitors, create / edit / delete monitors, alert contacts, maintenance windows and public status pages.

##### Response format

The API returns data in JSON format.

##### Rate limits

We are trying to prevent abusive use of our API. We have rate limits based on user plan.

```
FREE plan : 10 req/min
PRO plan : monitor limit * 2 req/min ( with maximum value 5000 req/min )
```
We will return 429 HTTP status code in the response from API, when you hit the rate limits. Also we will return common rate limit response headers in the response:

```
X-RateLimit-Limit - your current rate limit
X-RateLimit-Remaining - number of calls left in current duration
X-RateLimit-Reset - time since epoch in seconds at which the rate limiting period will end (or already ended)
Retry-After - Number of second after you should retry the call
```
##### Type of API keys

HTTP Basic Access Authentication is used for verifying accounts.

There are 3 types of api_keys for reaching the data:

- **Account-specific api_key:** Allows using all the API methods on all the monitors of an account.
- **Monitor-specific api_keys:** Allows using only the`getMonitors` method for the given monitor.
- **Read-only api_key:** Allows fetching data with all the`get*` API endpoints.

##### How to get API keys

You can get your API keys from the Integrations page under section **API**.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
