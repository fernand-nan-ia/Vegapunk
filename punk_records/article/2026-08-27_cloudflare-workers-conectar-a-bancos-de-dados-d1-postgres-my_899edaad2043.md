---
item_id: "080669e7-5c0e-4f2f-b5a8-d670b0185e61"
platform: article
external_id: "899edaad2043"
canonical_url: "https://developers.cloudflare.com/workers/databases/connecting-to-databases"
channel: "Cloudflare Docs"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["cloudflare", "workers", "d1", "hyperdrive", "postgres", "supabase", "multi-tenant"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Cloudflare Workers — conectar a bancos de dados: D1, Postgres/MySQL via Hyperdrive, Supabase/Neon/PlanetScale, drivers serverless

🔗 https://developers.cloudflare.com/workers/databases/connecting-to-databases

## Resumo

Workers acessam bancos SQL e NoSQL: D1 (SQL serverless da Cloudflare, otimizado para acesso global, escala com vários bancos de 10 GB por usuário/tenant, preço por consulta e armazenamento; binding do Worker, REST, ORMs como Prisma e Drizzle); bancos relacionais tradicionais Postgres e MySQL por drivers TCP (node-postgres, Postgres.js, mysql2) — recomendado com Hyperdrive, que faz pool de conexões e acelera a partir de todas as regiões; bancos serverless compatíveis (Supabase, Neon, PlanetScale) por TCP + Hyperdrive ou por drivers HTTP serverless; também MongoDB Atlas e Prisma.

## Tópicos

- **D1** — SQL serverless, 10 GB por banco, multi-tenant por banco, binding + ORMs.
- **Relacionais** — Postgres/MySQL por TCP; Hyperdrive recomendado.
- **Serverless** — Supabase, Neon, PlanetScale; TCP+Hyperdrive ou HTTP.

## Pontos-chave

- Supabase (já no vault) funciona a partir de Workers com Hyperdrive.
- D1 permite um banco por cliente — isolamento barato para SaaS B2B.
- Sem Hyperdrive, cada requisição abre conexão nova — lento e caro para o banco.

## Como aplicar

Se o SaaS ficar em Supabase, colocar Hyperdrive na frente ao usar Workers; D1 por cliente é alternativa para isolamento.

## 🔧 Atlas diz

Parafuso importante: Worker sem Hyperdrive abre conexão a cada requisição e o Postgres chora. Com Hyperdrive, pool global. E o D1 com um banco por cliente é o isolamento que o Shaka ia pedir para o SaaS B2B — sem RLS complicado.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Cloudflare Workers can connect to and query your data in both SQL and NoSQL databases, including:

- Cloudflare's own D1, a serverless SQL-based database.
- Traditional hosted relational databases, including Postgres and MySQL, using Hyperdrive (recommended) to significantly speed up access.
- Serverless databases, including Supabase, MongoDB Atlas, PlanetScale, and Prisma.

D1 is Cloudflare's own SQL-based, serverless database. It is optimized for global access from Workers, and can scale out with multiple, smaller (10GB) databases, such as per-user, per-tenant or per-entity databases. Similar to some serverless databases, D1 pricing is based on query and storage costs.

| Database | Library or Driver | Connection Method | 
|---|---|---|
| D1 | Workers binding, integrates with Prisma ↗, Drizzle ↗, and other ORMs | Workers binding, REST API | 

Traditional databases use SQL drivers that use TCP sockets to connect to the database. TCP is the de-facto standard protocol that many databases, such as PostgreSQL and MySQL, use for client connectivity. These drivers are also widely compatible with your preferred ORM libraries and query builders.

This also includes serverless databases that are PostgreSQL or MySQL-compatible like Supabase, Neon, or PlanetScale (either MySQL or PostgreSQL), which can be connected to using both native TCP sockets and Hyperdrive or serverless HTTP-based drivers (detailed below).

| Database | Integration | Library or Driver | Connection Method | 
|---|---|---|---|
| Postgres | Direct connection | node-postgres ↗,Postgres.js ↗ | TCP Socket via database driver, using Hyperdrive for optimal performance (optional, recommended) | 
| MySQL | Direct connection | mysql2 ↗, mysql ↗ | TCP Socket via database driver, using Hyperdrive for optimal performance (optional, recommended) | 

Serverless databases may provide direct connection to the underlying database, or provide HTTP-based proxies and drivers (also known as serverless drivers).

For PostgreSQL and MySQL serverless databases, you can connect to the underlying database directly using the native database drivers and ORMs you are familiar with, using Hyperdrive (recommended) to speed up connectivity and pool database connections. When you use Hyperdrive, your connection pool is managed across all of Cloudflare regions and optimized for usage from Workers.

You can also use serverless driver libraries to connect to the HTTP-based proxies managed by the database provider. These may also provide connection pooling for traditional SQL databases and reduce the amount of roundtrips needed to establish a secure connection, similarly to Hyperdrive.

| Database | Library or Driver | Connection Method | 
|---|---|---|
| PlanetScale ↗ | Hyperdrive (MySQL), Hyperdrive (PostgreSQL), @planetscale/database ↗ | mysql2, mysql, node-postgres, Postgres.js, or API via client library | 
| Supabase ↗ | Hyperdrive, @supabase/supabase-js ↗ | node-postgres,Postgres.js, or API via client library | 
| Prisma ↗ | prisma ↗ | API via client library | 
| Neon ↗ | Hyperdrive, @neondatabase/serverless ↗ | node-postgres,Postgres.js, or API via client library | 
| Hasura ↗ | API | GraphQL API via fetch() | 
| Upstash Redis ↗ | @upstash/redis ↗ | API via client library | 
| TiDB Cloud ↗ | @tidbcloud/serverless ↗ | API via client library | 

Once you have installed the necessary packages, use the APIs provided by these packages to connect to your database and perform operations on it. Refer to detailed links for service-specific instructions.

If your database requires authentication, use Wrangler secrets to securely store your credentials. To do this, create a secret in your Cloudflare Workers project using the following `wrangler secret` command:

Then, retrieve the secret value in your code using the following code snippet:

Use the secret value to authenticate with the external service. For example, if the external service requires an API key or database username and password for authentication, include these in using the relevant service's library or API.

For services that require mTLS authentication, use mTLS certificates to present a client certificate.

- Learn how to connect to an existing PostgreSQL database with Hyperdrive.
- Discover other storage options available for use with Workers.
- Create your first database with Cloudflare D1.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
