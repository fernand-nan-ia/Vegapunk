---
item_id: "84ae06cd-413b-4439-8adc-f62a52ba7666"
platform: article
external_id: "a955751d328b"
canonical_url: "https://developers.cloudflare.com/r2"
channel: "Cloudflare Docs"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["cloudflare", "r2", "object-storage", "s3", "egress", "storage"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Cloudflare R2 — visão geral: armazenamento de objetos sem taxa de egress, casos de uso e recursos (location hints, CORS, buckets públicos, tokens, Data Catalog)

🔗 https://developers.cloudflare.com/r2

## Resumo

R2 é o armazenamento de objetos da Cloudflare para dados não estruturados em grande volume, sem as taxas de egress das nuvens tradicionais. Casos: storage de apps cloud-native, conteúdo web, podcasts, data lakes, saída de processos em lote (modelos e datasets de ML). Recursos: location hints (região principal de acesso na criação do bucket), CORS e políticas por bucket, buckets públicos expostos à Internet, tokens com escopo por bucket, R2 Data Catalog (Apache Iceberg gerenciado dentro do bucket, consultável por Spark, Snowflake e R2 SQL). Integra com Workers (serverless), Stream (vídeo) e Images.

## Tópicos

- **Proposta** — Objetos em volume, zero egress.
- **Casos** — Apps, web, podcasts, data lakes, artefatos de ML.
- **Recursos** — Location hints, CORS, público, tokens por bucket, Data Catalog Iceberg.

## Pontos-chave

- Egress zero muda a conta de servir arquivos grandes (PDFs, laudos, vídeos).
- Token por bucket = credencial mínima por projeto (regra que o Shaka cobra).
- Data Catalog transforma bucket em data lake consultável.

## Como aplicar

Guardar PDFs e anexos do SaaS (e talvez o backup do Vegapunk) em R2 com token só daquele bucket.

## 🔧 Atlas diz

Storage S3 sem cobrar para tirar o arquivo de lá — isso é o parafuso que faz a conta fechar em laudo de 20 MB. Token por bucket é a regra da bancada: uma chave para o SaaS, outra para o backup, nenhuma vê a outra.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Object storage for all your data.

Cloudflare R2 Storage allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud storage services.

You can use R2 for multiple scenarios, including but not limited to:

- Storage for cloud-native applications
- Cloud storage for web content
- Storage for podcast episodes
- Data lakes (analytics and big data)
- Cloud storage output for large batch processes, such as machine learning model artifacts or datasets

Get started

Browse the examples

Location Hints are optional parameters you can provide during bucket creation to indicate the primary geographical location you expect data will be accessed from.

Configure CORS to interact with objects in your bucket and configure policies on your bucket.

Public buckets expose the contents of your R2 bucket directly to the Internet.

Create bucket scoped tokens for granular control over who can access your data.

A managed Apache Iceberg ↗ data catalog built directly into your R2 bucket, so you can turn a bucket into a data warehouse or lakehouse queryable by engines like Spark, Snowflake, and R2 SQL.

A serverless ↗ execution environment that allows you to create entirely new applications or augment existing ones without configuring or maintaining infrastructure.

Upload, store, encode, and deliver live and on-demand video with one API, without configuring or maintaining infrastructure.

A suite of products tailored to your image-processing needs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
