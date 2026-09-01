---
item_id: "852879e1-7cfb-4a92-94ae-095ee94056bc"
platform: article
external_id: "357f958e998d"
canonical_url: "https://developers.cloudflare.com/workers"
channel: "Cloudflare Docs"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["cloudflare", "workers", "serverless", "edge", "d1", "r2", "kv"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Cloudflare Workers — visão geral: serverless global, frameworks e linguagens, bindings para storage, compute e mídia

🔗 https://developers.cloudflare.com/workers

## Resumo

Workers é a plataforma serverless da Cloudflare: deploy com um comando na rede global, sem infra. Suporta full-stack com React, Vue, Svelte, Next, Astro, React Router e linguagens JavaScript, TypeScript, Python, Rust; observabilidade embutida; grátis para começar. Bindings conectam a serviços: storage (Durable Objects para estado em tempo real, D1 SQL, KV chave-valor de baixa latência, Queues sem custo de egress, Hyperdrive para bancos externos), compute (Workers AI com GPUs, Workflows duráveis com retry, Vectorize para busca vetorial, R2 armazenamento de objetos sem egress, Browser Rendering), mídia (cache global, Images). Início por template ou Wrangler CLI.

## Tópicos

- **Plataforma** — Deploy global com um comando; frameworks e linguagens variadas.
- **Storage** — Durable Objects, D1, KV, Queues, Hyperdrive.
- **Compute e mídia** — Workers AI, Workflows, Vectorize, R2, Browser Rendering, cache, Images.

## Pontos-chave

- Um lugar para API, fila, banco, storage e vetores — sem VPS.
- Python é suportado (com limitações) — conferir antes de portar o Vegapunk.
- R2 sem egress + Workers = servir arquivos barato.

## Como aplicar

Candidato para hospedar o SaaS sem VPS: Worker + D1/Supabase + R2 + Queues; comparar com KVM 2 da Hostinger (item no vault).

## 🔧 Atlas diz

Aqui está a alternativa ao VPS da Hostinger que a York guardou: sem servidor para cuidar, paga por requisição. Diferença de bancada: no VPS eu controlo tudo e faço backup; no Worker a Cloudflare controla e eu programo nos limites deles. Os dois valem; depende de quem vai acordar às 2h.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

A serverless platform for building, deploying, and scaling apps across Cloudflare's global network ↗ with a single command — no infrastructure to manage, no complex configuration

With Cloudflare Workers, you can expect to:

- Deliver fast performance with high reliability anywhere in the world
- Build full-stack apps with your framework of choice, including React, Vue, Svelte, Next, Astro, React Router, and more
- Use your preferred language, including JavaScript, TypeScript, Python, Rust, and more
- Gain deep visibility and insight with built-in observability
- Get started for free and grow with flexible pricing, affordable at any scale

Get started with your first project:

Deploy a template

Deploy with Wrangler CLI

Connect to external services like databases, APIs, and storage via Bindings, enabling functionality with just a few lines of code:

**Storage**

Scalable stateful storage for real-time coordination.

Serverless SQL database built for fast, global queries.

Low-latency key-value storage for fast, edge-cached reads.

Guaranteed delivery with no charges for egress bandwidth.

Connect to your external database with accelerated queries, cached at the edge.

**Compute**

Machine learning models powered by serverless GPUs.

Durable, long-running operations with automatic retries.

Vector database for AI-powered semantic search.

Zero-egress object storage for cost-efficient data access.

Programmatic serverless browser instances.

**Media**

Global caching for high-performance, low-latency delivery.

Streamlined image infrastructure from a single API.

Want to connect with the Workers community? Join our Discord ↗

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
