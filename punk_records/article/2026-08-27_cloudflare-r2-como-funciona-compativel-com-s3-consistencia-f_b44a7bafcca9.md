---
item_id: "17f04016-0c8b-4139-ae72-d1867c1d7efd"
platform: article
external_id: "b44a7bafcca9"
canonical_url: "https://developers.cloudflare.com/r2/how-r2-works"
channel: "Cloudflare Docs"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["cloudflare", "r2", "s3", "arquitetura", "consistencia", "durable-objects"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Cloudflare R2 — como funciona: compatível com S3, consistência forte, arquitetura (Gateway, Metadata em Durable Objects, cache em camadas, storage distribuído) e fluxo de escrita/leitura

🔗 https://developers.cloudflare.com/r2/how-r2-works

## Resumo

R2 é armazenamento de objetos compatível com S3, sem egress, na rede global da Cloudflare, com consistência forte e alta durabilidade — bom para assets web, treino de IA e conteúdo gerado por usuários. Arquitetura: R2 Gateway (entrada, autenticação e roteamento, roda em Workers), Metadata Service (em Durable Objects, guarda chave/checksum e garante consistência, com cache), Tiered Read Cache (serve leituras perto do cliente) e Distributed Storage (dados cifrados). Interfaces: binding de Workers, API S3 e REST (painel e Wrangler). Escrita: Gateway na borda autentica → busca chave de cifragem e cluster no Metadata → grava cifrado e replica na região → commit de metadados; só então responde 200. Leitura: autentica → consulta metadados → tenta o cache em camadas → senão busca no storage da região.

## Tópicos

- **Garantias** — S3-compatível, consistência forte, durabilidade, sem egress.
- **Componentes** — Gateway (Workers), Metadata (Durable Objects), cache em camadas, storage distribuído.
- **Fluxos** — Escrita: cifra → grava → replica → commit → 200. Leitura: metadados → cache → storage.

## Pontos-chave

- 200 só após o commit — dá para confiar no upload sem verificação extra.
- S3-compatível: bibliotecas boto3/aws-sdk funcionam sem mudança.
- Dados cifrados em repouso por padrão.

## Como aplicar

Usar boto3 apontando para R2 no SaaS; confiar no 200 como confirmação de gravação.

## 🔧 Atlas diz

Gosto quando o serviço explica a viga: o 200 só vem depois que os metadados foram gravados, então não existe 'subiu mas sumiu'. E como fala S3, o boto3 que a gente já conhece serve. Menos parafuso novo.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Cloudflare R2 is an S3-compatible object storage service with no egress fees, built on Cloudflare's global network. It is strongly consistent and designed for high data durability.

R2 is ideal for storing and serving unstructured data that needs to be accessed frequently over the internet, without incurring egress fees. It's a good fit for workloads like serving web assets, training AI models, and managing user-generated content.

R2's architecture is composed of multiple components:

- 
**R2 Gateway:** The entry point for all API requests that handles authentication and routing logic. This service is deployed across Cloudflare's global network via Cloudflare Workers.
- 
**Metadata Service:** A distributed layer built on Durable Objects used to store and manage object metadata (e.g. object key, checksum) to ensure strong consistency of the object across the storage system. It includes a built-in cache layer to speed up access to metadata.
- 
**Tiered Read Cache:** A caching layer that sits in front of the Distributed Storage Infrastructure that speeds up object reads by using Cloudflare Tiered Cache to serve data closer to the client.
- 
**Distributed Storage Infrastructure:** The underlying infrastructure that persistently stores encrypted object data.

R2 supports multiple client interfaces including Cloudflare Workers Binding, S3-compatible API, and a REST API that powers the Cloudflare Dashboard and Wrangler CLI. All requests are routed through the R2 Gateway, which coordinates with the Metadata Service and Distributed Storage Infrastructure to retrieve the object data.

When a write request (e.g. uploading an object) is made to R2, the following sequence occurs:

1. 
**Request handling:** The request is received by the R2 Gateway at the edge, close to the user, where it is authenticated.
2. 
**Encryption and routing:** The Gateway reaches out to the Metadata Service to retrieve the encryption key and determines which storage cluster to write the encrypted data to within the location set for the bucket.
3. 
**Writing to storage:** The encrypted data is written and stored in the distributed storage infrastructure, and replicated within the region (e.g. ENAM) for durability.
4. 
**Metadata commit:** Finally, the Metadata Service commits the object's metadata, making it visible in subsequent reads. Only after this commit is an`HTTP 200` success response sent to the client, preventing unacknowledged writes.

When a read request (e.g. fetching an object) is made to R2, the following sequence occurs:

1. 
**Request handling:** The request is received by the R2 Gateway at the edge, close to the user, where it is authenticated.
2. 
**Metadata lookup:** The Gateway asks the Metadata Service for the object metadata.
3. 
**Reading the object:** The Gateway attempts to retrieve the encrypted object from the tiered read cache. If it's not available, it retrieves the object from one of the distributed storage data centers within the region that holds the object data.
4. 
**Serving to client:** The object is decrypted and served to the user.

The performance of your operations can be influenced by factors such as the bucket's geographical location, request origin, and access patterns.

To optimize upload performance for cross-region requests, enable Local Uploads on your bucket.

To optimize read performance, enable Cloudflare Cache when using a custom domain. When caching is enabled, read requests can bypass the R2 Gateway and be served directly from Cloudflare's edge cache, reducing latency. Note that cached data may not reflect the latest version immediately.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
