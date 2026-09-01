---
item_id: "037519bd-af06-424c-a133-0d592518154d"
platform: article
external_id: "21b05c335f15"
canonical_url: "https://developers.cloudflare.com/workers/examples"
channel: "Cloudflare Docs"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["cloudflare", "workers", "exemplos", "hmac", "turnstile", "cache", "redirects"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Cloudflare Workers — catálogo de exemplos: SPA shell, Analytics Engine, streaming JSON, auth básica, HMAC, Turnstile, cache, redirects, geolocalização

🔗 https://developers.cloudflare.com/workers/examples

## Resumo

Lista de exemplos oficiais de Workers: shell de SPA com dados pré-carregados via HTMLRewriter, escrita no Analytics Engine, parse de JSON grande por streaming, HTTP Basic Auth, buscar/servir HTML, retornar JSON (APIs e middleware), verificar requisições assinadas com HMAC/SHA-256, stream de respostas da OpenAI, comparação timingSafeEqual, Turnstile (captcha) injetado por HTMLRewriter, domínio customizado para Images, 103 Early Hints, cache tags, objeto Cloudflare da requisição, agregar requisições, bloquear TLS < 1.2, bulk redirects, cache de POST, resposta condicional por URL/método/UA/IP/ASN/dispositivo, parse de cookies (A/B), fetch de JSON, geolocalização para estilo por país, entre outros.

## Tópicos

- **Segurança** — Basic Auth, HMAC/SHA-256, timingSafeEqual, Turnstile, bloquear TLS antigo.
- **Dados** — Streaming JSON, Analytics Engine, fetch JSON, agregação.
- **Web** — SPA shell, cache tags, 103 Early Hints, redirects, geolocalização, cookies/A-B.

## Pontos-chave

- Verificar webhook do Resend com HMAC tem exemplo pronto.
- Turnstile é captcha grátis para o formulário do site do cliente.
- Bulk redirects resolvem migração de URLs do site do cliente.

## Como aplicar

Turnstile no formulário de contato do cliente; HMAC para validar webhooks no SaaS.

## 🔧 Atlas diz

Peças usinadas de novo: HMAC para webhook, Turnstile para formulário sem robô, redirects em massa para quando o site do cliente mudar de URL. Copiar, testar, soldar.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Explore the following examples for Workers. Single Page App (SPA) shell with bootstrap dataUse HTMLRewriter to inject prefetched bootstrap data into an SPA shell, eliminating client-side data fetching on initial load. Works with Workers Static Assets or an externally hosted SPA.Write to Analytics EngineWrite custom analytics events to Workers Analytics Engine for high-cardinality, time-series data.Stream large JSONParse and transform large JSON request and response bodies using streaming.HTTP Basic AuthenticationShows how to restrict access using the HTTP Basic schema.Fetch HTMLSend a request to a remote server, read HTML from the response, and serve that HTML.Return small HTML pageDeliver an HTML page from an HTML string directly inside the Worker script.Return JSONReturn JSON directly from a Worker script, useful for building APIs and middleware.Sign requestsVerify a signed request using the HMAC and SHA-256 algorithms or return a 403.Stream OpenAI API ResponsesUse the OpenAI v4 SDK to stream responses from OpenAI.Using timingSafeEqualProtect against timing attacks by safely comparing values using timingSafeEqual.Turnstile with WorkersInject Turnstile implicitly into HTML elements using the HTMLRewriter runtime API.Custom Domain with ImagesSet up custom domain for Images using a Worker or serve images using a prefix path and Cloudflare registered domain.103 Early HintsAllow a client to request static assets while waiting for the HTML response.Cache Tags using WorkersSend Additional Cache Tags using WorkersAccessing the Cloudflare ObjectAccess custom Cloudflare properties and control how Cloudflare features are applied to every request.Aggregate requestsSend two GET request to two urls and aggregates the responses into one response.Block on TLSInspects the incoming request's TLS version and blocks if under TLSv1.2.Bulk redirectsRedirect requests to certain URLs based on a mapped object to the request's URL.Cache POST requestsCache POST requests using the Cache API.Conditional responseReturn a response based on the incoming request's URL, HTTP method, User Agent, IP address, ASN or device type.Cookie parsingGiven the cookie name, get the value of a cookie. You can also use cookies for A/B testing.Fetch JSONSend a GET request and read in JSON from the response. Use to fetch external data.Geolocation: Custom StylingPersonalize website styling based on localized user time.Geolocation: Hello WorldGet all geolocation data fields and display them in HTML.Post JSONSend a POST request with JSON data. Use to share data with external servers.RedirectRedirect requests from one URL to another or from one set of URLs to another set.Rewrite linksRewrite URL links in HTML using the HTMLRewriter. This is useful for JAMstack websites.Set security headersSet common security headers (X-XSS-Protection, X-Frame-Options, X-Content-Type-Options, Permissions-Policy, Referrer-Policy, Strict-Transport-Security, Content-Security-Policy).Multiple Cron TriggersSet multiple Cron Triggers on three different schedules.Setting Cron TriggersSet a Cron Trigger for your Worker.Using the WebSockets APIUse the WebSockets API to communicate in real time with your Cloudflare Workers.Geolocation: Weather applicationFetch weather data from an API using the user's geolocation data.A/B testing with same-URL direct accessSet up an A/B test by controlling what response is served based on cookies. This version supports passing the request through to test and control on the origin, bypassing random assignment.Alter headersExample of how to add, change, or delete headers sent in a request or returned in a response.Auth with headersAllow or deny a request based on a known pre-shared key in a header. This is not meant to replace the WebCrypto API.Bulk origin overrideResolve requests to your domain to a set of proxy third-party origin URLs.Using the Cache APIUse the Cache API to store responses in Cloudflare's cache.Cache using fetchDetermine how to cache a resource by setting TTLs, custom cache keys, and cache headers in a fetch request.CORS header proxyAdd the necessary CORS headers to a third party API response.Country code redirectRedirect a response based on the country code in the header of a visitor.Data loss preventionProtect sensitive data to prevent data loss, and send alerts to a webhooks server in the event of a data breach.Debugging logsSend debugging information in an errored response to a logging service.Hot-link protectionBlock other websites from linking to your content. This is useful for protecting images.Logging headers to consoleExamine the contents of a Headers object by logging to console with a Map.Modify request propertyCreate a modified request with edited properties based off of an incoming request.Modify responseFetch and modify response properties which are immutable by creating a copy first.Read POSTServe an HTML form, then read POST requests. Use also to read JSON or POST data from an incoming request.Respond with another siteRespond to the Worker request with the response from another website (example.com in this example).

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
