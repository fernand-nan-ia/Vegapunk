---
item_id: "90e2443b-3f4c-4597-a261-eadf62629925"
platform: article
external_id: "010a87edb387"
canonical_url: "https://developers.cloudflare.com/workers/best-practices/workers-best-practices"
channel: "Cloudflare Docs"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["cloudflare", "workers", "wrangler", "boas-praticas", "segredos", "ambientes"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Cloudflare Workers — boas práticas: compatibility_date, nodejs_compat, wrangler types, segredos, ambientes e mais

🔗 https://developers.cloudflare.com/workers/best-practices/workers-best-practices

## Resumo

Boas práticas oficiais de Workers a partir de padrões de produção: definir compatibility_date com a data atual em projetos novos e atualizá-la periodicamente; ativar a flag nodejs_compat para usar node:crypto, node:buffer, node:stream e evitar erros de import; não escrever a interface Env à mão — gerar com wrangler types e regenerar ao mudar bindings; segredos (chaves, tokens, credenciais) nunca no wrangler.toml nem no código — wrangler secret put e leitura via env; .env só local e no .gitignore; ambientes do Wrangler (production, staging, development) criam Workers separados {name}-{env}, com bindings e vars declarados por ambiente (não herdados) e o Worker raiz como deploy à parte — não deployar sem especificar ambiente. O texto integral (12k) cobre mais tópicos (observabilidade, limites, erros).

## Tópicos

- **Runtime** — compatibility_date e nodejs_compat.
- **Tipos** — wrangler types em vez de Env manual.
- **Segredos** — wrangler secret put; .env só local.
- **Ambientes** — production/staging/dev separados; bindings não herdados.

## Pontos-chave

- Segredo no wrangler.toml vai para o git — mesma armadilha do .env que o vault já registra.
- Ambientes não herdam bindings: declarar D1/R2 em cada um.
- Não deployar o Worker raiz por engano.

## Como aplicar

Checklist de DoD para qualquer Worker do SaaS: date, nodejs_compat, types, secrets, staging separado.

## 🔧 Atlas diz

Isso vira checklist da bancada: quatro parafusos antes do deploy — compatibility_date, nodejs_compat, wrangler types, wrangler secret put. E staging separado com bindings próprios, senão o teste grava no banco de produção. Já vi.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Best practices for Workers based on production patterns, Cloudflare's own internal usage, and common issues seen across the developer community.

The `compatibility_date` controls which runtime features and bug fixes are available to your Worker. Setting it to today's date on new projects ensures you get the latest behavior. Periodically updating it on existing projects gives you access to new APIs and fixes without changing your code.

For more information, refer to Compatibility dates.

The `nodejs_compat` compatibility flag gives your Worker access to Node.js built-in modules like `node:crypto`, `node:buffer`, `node:stream`, and others. Many libraries depend on these modules, and enabling this flag avoids cryptic import errors at runtime.

For more information, refer to Node.js compatibility.

Do not hand-write your `Env` interface. Run `wrangler types` to generate a type definition file that matches your actual Wrangler configuration. This catches mismatches between your config and code at compile time instead of at deploy time.

Re-run `wrangler types` whenever you add or rename a binding.

`npx wrangler types``yarn wrangler types``pnpm wrangler types`
For more information, refer to wrangler types.

Secrets (API keys, tokens, database credentials) must never appear in your Wrangler configuration or source code. Use `wrangler secret put` to store them securely, and access them through `env` at runtime. For local development, use a `.env` file (and make sure it is in your `.gitignore`). For more information, refer to Environment variables.

To add a secret, run the following command and provide the secret interactively when prompted:

`npx wrangler secret put API_KEY``yarn wrangler secret put API_KEY``pnpm wrangler secret put API_KEY`
You can also pipe secrets from other tools or environment variables:

For more information, refer to Secrets.

Wrangler environments let you deploy the same code to separate Workers for production, staging, and development. Each environment creates a distinct Worker named `{name}-{env}` (for example, `my-api-production` and `my-api-staging`).

Each environment is treated separately. Bindings and vars need to be declared per environment and are not inherited. Refer to non-inheritable keys. The root Worker (without an environment suffix) is a separate deployment. If you do not intend to use it, do not deploy without specifying an environment using `--env`.

With this configuration file, to deploy to staging:

`npx wrangler deploy --env staging``yarn wrangler deploy --env staging``pnpm wrangler deploy --env staging`
For more information, refer to Environments.

Workers support two routing mechanisms, and they serve different purposes:

- **Custom domains** : The Worker**is** the origin. Cloudflare creates DNS records and SSL certificates automatically. Use this when your Worker handles all traffic for a hostname.
- **Routes** : The Worker runs**in front of** an existing origin server. You must have a Cloudflare proxied (orange-clouded) DNS record for the hostname before adding a route.

The most common mistake with routes is missing the DNS record. Without a proxied DNS record, requests to the hostname return `ERR_NAME_NOT_RESOLVED` and never reach your Worker. If you do not have a real origin, add a proxied `AAAA` record pointing to `100::` as a placeholder.

For more information, refer to Routing.

Regardless of memory limits, streaming large requests and responses is a best practice in any language. It reduces peak memory usage and improves time-to-first-byte. Workers have a 128 MB memory limit, so buffering an entire body with `await response.text()` or `await request.arrayBuffer()` will crash your Worker on large payloads.

For request bodies you do consume entirely (JSON payloads, file uploads), enforce a maximum size before reading. This prevents clients from sending data you do not want to process.

Stream data through your Worker using `TransformStream` to pipe from a source to a destination without holding it all in memory.

When you need to concatenate multiple responses (for example, fetching data from several upstream APIs), pipe each body sequentially into a single writable stream. This avoids buffering any of the responses in memory.

For more information, refer to Streams.

`ctx.waitUntil()` lets you perform work after the response is sent to the client, such as analytics, cache writes, logging, or webhook notifications. This keeps your response fast while still completing background tasks.

Use `ctx.waitUntil()` only for work that does not affect the response. If the response depends on the work, `await` it before returning the response or stream the response as the work completes. A Worker that is still streaming a response body remains active without `ctx.waitUntil()`.

There are two common pitfalls: destructuring `ctx` (which loses the `this` binding and throws "Illegal invocation"), and exceeding the 30-second `waitUntil()` time limit after the response is sent or the client disconnects.

For more information, refer to Context.

Some Cloudflare services like R2, KV, D1, Queues, and Workflows are available as bindings. Bindings are direct, in-process references that require no network hop, no authentication, and no extra latency. Using the REST API from within a Worker wastes time and adds unnecessary complexity.

Long-running, retryable, or non-urgent tasks should not block a request. Use Queues and Workflows to move work out of the critical path. They serve different purposes:

**Use Queues when** you need to decouple a producer from a consumer. Queues are a message broker: one Worker sends a message, another Worker processes it later. They are the right choice for fan-out (one event triggers many consumers), buffering and batching (aggregate messages before writing to a downstream service), and simple single-step background jobs (send an email, fire a webhook, write a log). Queues provide at-least-once delivery with configurable retries per message.

**Use Workflows when** the background work has multiple steps that depend on each other. Workflows are a durable execution engine: each step's return value is persisted, and if a step fails, only that step is retried — not the entire job. They are the right choice for multi-step processes (charge a card, then create a shipment, then send a confirmation), long-running tasks that need to pause and resume (wait hours or days for an external event or human approval via `step.waitForEvent()`), and complex conditional logic where later steps depend on earlier results. Workflows can run for hours, days, or weeks.

**Use both together** when a high-throughput entry point feeds into complex processing. For example, a Queue can buffer incoming orders, and the consumer can create a Workflow instance for each order that requires multi-step fulfillment.

For more information, refer to Queues and Workflows.

When one Worker needs to call another, use service bindings instead of making an HTTP request to a public URL. Service bindings are zero-cost, bypass the public internet, and support type-safe RPC.

Always use Hyperdrive when connecting to a remote PostgreSQL or MySQL database from a Worker. Hyperdrive maintains a regional connection pool close to your database, eliminating the per-request cost of TCP handshake, TLS negotiation, and connection setup. It also caches query results where possible.

Create a new `Client` on each request. Hyperdrive manages the underlying pool, so client creation is fast. Requires `nodejs_compat` for database driver support.

For more information, refer to Hyperdrive.

Plain Workers can upgrade HTTP connections to WebSockets, but they lack persistent state and hibernation. If the isolate is evicted, the connection is lost because there is no persistent actor to hold it. For reliable, long-lived WebSocket connections, use Durable Objects with the Hibernation API. Durable Objects keep WebSocket connections open even while the object is evicted from memory, and automatically wake up when a message arrives.

Use `this.ctx.acceptWebSocket()` instead of `ws.accept()` to enable hibernation. Use `setWebSocketAutoResponse` for ping/pong heartbeats that do not wake the object.

For more information, refer to Durable Objects WebSocket best practices.

Workers Static Assets is the recommended way to deploy static sites, single-page applications, and full-stack apps on Cloudflare. If you are starting a new project, use Workers instead of Pages. Pages continues to work, but new features and optimizations are focused on Workers.

For a purely static site, point `assets.directory` at your build output. No Worker script is needed. For a full-stack app, add a `main` entry point and an `ASSETS` binding to serve static files alongside your API.

For more information, refer to Workers Static Assets.

Production Workers without observability are a black box. Enable logs and traces before you deploy to production. When an intermittent error appears, you need data already being collected to diagnose it.

Enable them in your Wrangler configuration and use `head_sampling_rate` to control volume and manage costs. A sampling rate of `1` captures everything; lower it for high-traffic Workers.

Use structured JSON logging with `console.log` so logs are searchable and filterable. Use `console.error` for errors and `console.warn` for warnings. These appear at the correct severity level in the Workers Observability dashboard.

For more information, refer to Workers Logs and Traces.

For more information on all available observability tools, refer to Workers Observability.

Workers reuse isolates across requests. A variable set during one request is still present during the next. This causes cross-request data leaks, stale state, and "Cannot perform I/O on behalf of a different request" errors.

Pass state through function arguments or store it on `env` bindings. Never in module-level variables.

For more information, refer to Workers errors.

A `Promise` that is not `await`ed, `return`ed, or passed to `ctx.waitUntil()` is a floating promise. Floating promises cause silent bugs: dropped results, swallowed errors, and unfinished work. The Workers runtime may terminate your isolate before a floating promise completes.

Choose based on whether the response depends on the work. Use `await` or `return` for work that must complete before the response is correct. Use `ctx.waitUntil()` for work that can run after the response is sent and can finish within the `waitUntil()` time limit.

Enable the `no-floating-promises` lint rule to catch these at development time. If you use ESLint, enable `@typescript-eslint/no-floating-promises` ↗. If you use oxlint, enable `typescript/no-floating-promises` ↗.

The Workers runtime provides the Web Crypto API for cryptographic operations. Use `crypto.randomUUID()` for unique identifiers and `crypto.getRandomValues()` for random bytes. Never use `Math.random()` for anything security-sensitive. It is not cryptographically secure.

Node.js `node:crypto` is also fully supported when `nodejs_compat` is enabled, so you can use whichever API you or your libraries prefer.

When comparing secret values (API keys, tokens, HMAC signatures), use `crypto.subtle.timingSafeEqual()` to prevent timing side-channel attacks. Do not short-circuit on length mismatch. Encode both values to a fixed-size hash first.

`passThroughOnException()` is a fail-open mechanism that sends requests to your origin when your Worker throws an unhandled exception. While it can be useful during migration from an origin server, it hides bugs and makes debugging difficult. Use explicit `try...catch` blocks with structured error responses instead.

The `@cloudflare/vitest-plugin` package runs your tests inside the Workers runtime, giving you access to real bindings (KV, R2, D1, Durable Objects) during tests. This catches issues that Node.js-based tests miss, like unsupported APIs or missing compatibility flags.

One known pitfall: the Vitest plugin automatically injects `nodejs_compat`, so tests pass even if your Wrangler configuration does not have the flag. Always confirm your `wrangler.jsonc` includes `nodejs_compat` if your code depends on Node.js built-in modules.

For more information, refer to Testing with Vitest.

- Rules of Durable Objects: best practices for stateful, coordinated applications.
- Rules of Workflows: best practices for durable, multi-step Workflows.
- Platform limits: CPU time, memory, subrequest, and other limits.
- Workers errors: error codes and debugging guidance.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
