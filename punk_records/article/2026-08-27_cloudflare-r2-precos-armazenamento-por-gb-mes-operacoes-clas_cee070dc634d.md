---
item_id: "f95bc4e0-a44d-4e9a-8512-cff73579b74f"
platform: article
external_id: "cee070dc634d"
canonical_url: "https://developers.cloudflare.com/r2/pricing"
channel: "Will I be charged · Cloudflare Docs"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["cloudflare", "r2", "precos", "storage", "egress", "gb-mes"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Cloudflare R2 — preços: armazenamento por GB-mês, operações classe A/B, Infrequent Access, cota grátis (10 GB, 1 M A, 10 M B) e egress zero

🔗 https://developers.cloudflare.com/r2/pricing

## Resumo

R2 cobra por volume armazenado e por duas classes de operação: Classe A (mutação: PutObject, ListObjects, CopyObject, multipart, configurações de bucket) e Classe B (leitura: GetObject, HeadObject, HeadBucket…); DeleteObject, DeleteBucket e AbortMultipartUpload são grátis; egress é grátis em qualquer classe. Standard: US$ 0,015/GB-mês, A US$ 4,50/milhão, B US$ 0,36/milhão. Infrequent Access: US$ 0,01/GB-mês, A US$ 9,00/milhão, B US$ 0,90/milhão, mais US$ 0,01/GB de recuperação e mínimo de 30 dias cobrados mesmo se apagar antes. Grátis por mês: 10 GB-mês, 1 milhão de operações A, 10 milhões de B. GB-mês = média do pico diário no período de 30 dias (1 GB por 5 dias + 3 GB por 25 dias = 2,66 GB-mês). R2 Data Catalog cobra operações de catálogo e compactação à parte.

## Tópicos

- **Standard** — US$ 0,015/GB-mês; A US$ 4,50/M; B US$ 0,36/M; egress 0.
- **Infrequent Access** — US$ 0,01/GB-mês; A US$ 9/M; B US$ 0,90/M; +US$ 0,01/GB recuperação; mínimo 30 dias.
- **Grátis** — 10 GB-mês, 1 M A, 10 M B.
- **Cálculo** — GB-mês pela média do pico diário; deletes grátis.

## Pontos-chave

- Egress zero: servir 1 TB de PDFs custa o mesmo que servir 1 MB.
- Listar objetos é Classe A (cara): evitar ListObjects em loop.
- 10 GB grátis cobre o SaaS por meses.
- Infrequent Access só para arquivo morto — recuperação custa e há mínimo de 30 dias.

## Como aplicar

Backup do Punk Records/SaaS em R2 Standard dentro dos 10 GB grátis; nada de ListObjects em rotina.

## 🔧 Atlas diz

Conta simples e honesta: 10 GB e 10 milhões de leituras grátis, e ninguém cobra para baixar. O parafuso escondido é ListObjects ser Classe A — quem lista a cada requisição paga 12× mais. Guarda a chave do objeto no banco e nunca lista.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

R2 charges based on the total volume of data stored, along with two classes of operations on that data:

1. Class A operations which are more expensive and tend to mutate state.
2. Class B operations which tend to read existing state.

For the Infrequent Access storage class, data retrieval fees apply. There are no charges for egress bandwidth for any storage class.

All included usage is on a monthly basis.

|  | Standard storage | Infrequent Access storage | 
|---|---|---|
| Storage | $0.015 / GB-month | $0.01 / GB-month | 
| Class A Operations | $4.50 / million requests | $9.00 / million requests | 
| Class B Operations | $0.36 / million requests | $0.90 / million requests | 
| Data Retrieval (processing) | None | $0.01 / GB | 
| Egress (data transfer to Internet) | Free <sup>1</sup> | Free <sup>1</sup> | 

You can use the following amount of storage and operations each month for free.

|  | Free | 
|---|---|
| Storage | 10 GB-month / month | 
| Class A Operations | 1 million requests / month | 
| Class B Operations | 10 million requests / month | 
| Egress (data transfer to Internet) | Free <sup>1</sup> | 

Storage is billed using gigabyte-month (GB-month) as the billing metric. A GB-month is calculated by averaging the *peak* storage per day over a billing period (30 days).

For example:

- Storing 1 GB constantly for 30 days will be charged as 1 GB-month.
- Storing 3 GB constantly for 30 days will be charged as 3 GB-month.
- Storing 1 GB for 5 days, then 3 GB for the remaining 25 days will be charged as `1 GB * 5/30 month + 3 GB * 25/30 month = 2.66 GB-month`

For objects stored in Infrequent Access storage, you will be charged for the object for the minimum storage duration even if the object was deleted or moved before the duration specified.

Class A Operations include `ListBuckets`, `PutBucket`, `ListObjects`, `PutObject`, `CopyObject`, `CompleteMultipartUpload`, `CreateMultipartUpload`, `LifecycleStorageTierTransition`, `ListMultipartUploads`, `UploadPart`, `UploadPartCopy`, `ListParts`, `PutBucketEncryption`, `PutBucketCors` and `PutBucketLifecycleConfiguration`.

Class B Operations include `HeadBucket`, `HeadObject`, `GetObject`, `UsageSummary`, `GetBucketEncryption`, `GetBucketLocation`, `GetBucketCors` and `GetBucketLifecycleConfiguration`.

Free operations include `DeleteObject`, `DeleteBucket` and `AbortMultipartUpload`.

Data retrieval fees apply when you access or retrieve data from the Infrequent Access storage class. This includes any time objects are read or copied.

For objects stored in Infrequent Access storage, you will be charged for the object for the minimum storage duration even if the object was deleted, moved, or replaced before the specified duration.

| Storage class | Minimum storage duration | 
|---|---|
| Standard storage | None | 
| Infrequent Access storage | 30 days | 

R2 Data Catalog charges for catalog operations and compaction data processed, in addition to standard R2 storage and operations. For full details, refer to R2 Data Catalog pricing.

Super Slurper is free to use. You are only charged for the Class A operations that Super Slurper makes to your R2 bucket. Objects with sizes < 100MiB are uploaded to R2 in a single Class A operation. Larger objects use multipart uploads to increase transfer success rates and will perform multiple Class A operations. Note that your source bucket might incur additional charges as Super Slurper copies objects over to R2.

Once migration completes, you are charged for storage & Class A/B operations as described in previous sections.

Sippy is free to use. You are only charged for the operations Sippy makes to your R2 bucket. If a requested object is not present in R2, Sippy will copy it over from your source bucket. Objects with sizes < 200MiB are uploaded to R2 in a single Class A operation. Larger objects use multipart uploads to increase transfer success rates, and will perform multiple Class A operations. Note that your source bucket might incur additional charges as Sippy copies objects over to R2.

As objects are migrated to R2, they are served from R2, and you are charged for storage & Class A/B operations as described in previous sections.

To learn about potential cost savings from using R2, refer to the R2 pricing calculator ↗.

If a user writes 1,000 objects in R2 **Standard storage** for 1 month with an average size of 1 GB and reads each object 1,000 times during the month, the estimated cost for the month would be:

|  | Usage | Free Tier | Billable Quantity | Price | 
|---|---|---|---|---|
| Storage | (1,000 objects) * (1 GB per object) = 1,000 GB-months | 10 GB-months | 990 GB-months | $14.85 | 
| Class A Operations | (1,000 objects) * (1 write per object) = 1,000 writes | 1 million | 0 | $0.00 | 
| Class B Operations | (1,000 objects) * (1,000 reads per object) = 1 million reads | 10 million | 0 | $0.00 | 
| Data retrieval (processing) | (1,000 objects) * (1 GB per object) = 1,000 GB | NA | None | $0.00 | 
| **TOTAL** |  |  |  | **$14.85** | 

If a user writes 1,000 objects in R2 Infrequent Access storage with an average size of 1 GB, stores them for 5 days, and then deletes them (delete operations are free), and during those 5 days each object is read 1,000 times, the estimated cost for the month would be:

|  | Usage | Free Tier | Billable Quantity | Price | 
|---|---|---|---|---|
| Storage | (1,000 objects) * (1 GB per object) = 1,000 GB-months | NA | 1,000 GB-months | $10.00 | 
| Class A Operations | (1,000 objects) * (1 write per object) = 1,000 writes | NA | 1,000 | $9.00 | 
| Class B Operations | (1,000 objects) * (1,000 reads per object) = 1 million reads | NA | 1 million | $0.90 | 
| Data retrieval (processing) | (1,000 objects) * (1 GB per object) = 1,000 GB | NA | 1,000 GB | $10.00 | 
| **TOTAL** |  |  |  | **$29.90** | 

Note that the minimal storage duration for infrequent access storage is 30 days, which means the billable quantity is 1,000 GB-months, rather than 167 GB-months.

If a user writes 100,000 files with an average size of 100 KB object and reads 10,000,000 objects per day, the estimated cost in a month would be:

|  | Usage | Free Tier | Billable Quantity | Price | 
|---|---|---|---|---|
| Storage | (100,000 objects) * (100KB per object) | 10 GB-months | 0 GB-months | $0.00 | 
| Class A Operations | (100,000 writes) | 1 million | 0 | $0.00 | 
| Class B Operations | (10,000,000 reads per day) * (30 days) | 10 million | 290,000,000 | $104.40 | 
| **TOTAL** |  |  |  | **$104.40** | 

To learn more about how usage is billed, refer to Cloudflare Billing Policy.

No. You are not charged for operations when the caller does not have permission to make the request (HTTP 401 `Unauthorized` response status code).

1. 
Egressing directly from R2, including via the Workers API, S3 API, and `r2.dev` domains does not incur data transfer (egress) charges and is free. If you connect other metered services to an R2 bucket, you may be charged by those services. ↩ ↩<sup>2</sup> ↩<sup>3</sup>

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
