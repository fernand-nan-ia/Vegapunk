---
item_id: "1985caf5-eb87-4e12-bc75-9db1bf7daf16"
platform: article
external_id: "4401cac3bd7a"
canonical_url: "https://www.maptiler.com/cloud/pricing"
channel: "Maptiler"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["maptiler", "precos", "mapas", "pay-as-you-go", "sessoes"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: media
theme: negocios-e-financas
content_type: article
---

# MapTiler Cloud — modelo de preços: Free (logo, 5 GB), Flex pay-as-you-go (10 GB, sem logo, SLA), Custom; cobrança por sessões e requisições

🔗 https://www.maptiler.com/cloud/pricing

## Resumo

Preços do MapTiler Cloud em três planos: Free (testes e uso pessoal/não comercial; tiles vetoriais e raster XYZ; logo MapTiler obrigatório; dados 2D/3D; 5 GB de armazenamento com limite de 1 arquivo); Flex (pay-as-you-go para uso comercial; vetor, raster e WMTS; exportações high-DPI; 10 GB escaláveis; arquivos ilimitados; sem logo exceto em sessões 3D; SLA 99,9%; conta de equipe); Custom (volume, descontos, cotas flexíveis, pedido por orçamento/nota). Modelo de cobrança: sessões de mapa por mês (um objeto de mapa inicializado; pan/zoom não cobram), sessões de busca, pontos de dados, tiles (tile de 512 px conta 4 requisições), imagens estáticas (1 imagem = 15 requisições), extras por sessão/requisição/armazenamento/upload. Requisições ilimitadas a tilesets do MapTiler e a dados hospedados pelo cliente no plano indicado; uma visualização de mapa gera cerca de 4 requisições com tiles vetoriais. Os valores em dólar e as cotas numéricas vêm de um calculador em JavaScript e não foram extraídos.

## Tópicos

- **Planos** — Free (não comercial, logo, 5 GB/1 arquivo); Flex (comercial, 10 GB+, sem logo, SLA 99,9%); Custom.
- **Cobrança** — Sessões de mapa e busca; tiles (512 px = 4 req); imagem estática = 15 req; extras.
- **Lacuna** — Cotas e preços numéricos não extraídos.

## Pontos-chave

- Uso comercial exige Flex — o Free do site do cliente seria violação.
- Sessão = mapa aberto; pan/zoom não custam — bom para app de vistoria.
- Imagem estática custa 15 requisições: cachear a imagem do laudo.

## Como aplicar

Se entrar mapa no site do cliente ou no SaaS, é Flex desde o dia 1; abrir o calculador para estimar sessões/mês.

## 🍩 York diz

Preço escondido num calculador, de novo — mas a regra já dá para ler: Free é só para brincar, comercial paga por sessão. Sessão é 'abriu o mapa', não 'arrastou' — isso é honesto. Imagem estática vale 15 requisições, então o laudo gera a imagem uma vez e guarda no R2.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Flexible pricing for maps, data processing & storage

Choose the plan that fits your needs.

###### Pay-as-you-grow

Pay for extra services as you use them, and change plans with flexibility.

###### Volume discounts

High volumes? Get in touch with our Sales team for a volume discount.

###### to start with

Suitable for testing, personal or non-commercial use.

Vector & XYZ raster tiles

MapTiler logo on the map

2D/3D data support (incl. Gaussian Splats)

5 GB storage (1 file limit)


###### pay as you go

Pay-as-you-go with all the features needed for any standard use case.

Vector, raster & WMTS

High-DPI exports

10 GB storage (scalable)

Unlimited number of files

###### built for scale

#### Compare features

|  | Free | Flex | Custom | 
| Vector maps |  |  |  | 
| **Standard raster maps** XYZ |  |  |  | 
| Regular updates |  |  |  | 
| Search & Geocoding service |  |  |  | 
| Commercial use |  |  |  | 
| **Export for videos & games** |  |  | contact us for commercial use | 
| Static maps API |  |  |  | 
| WMTS map services |  |  |  | 
| No MapTiler logo required |  | required for 3D sessions | required for 3D sessions | 
| 99.9% SLA |  |  |  | 
| Team account |  |  |  | 
| Volume discounts |  |  |  | 
| Soft-limit on usage quotas |  |  |  | 
| Quote & invoice ordering |  |  |  | 

|  | Free | 
| Vector maps |  | 
| **Standard raster maps** XYZ |  | 
| Regular updates |  | 
| Search & Geocoding service |  | 
| Commercial use |  | 
| **Export for videos & games** |  | 
| Static maps API |  | 
| WMTS map services |  | 
| No MapTiler logo required |  | 
| 99.9% SLA |  | 
| Team account |  | 
| Volume discounts |  | 
| Soft-limit on usage quotas |  | 
| Quote & invoice ordering |  | 

|  | Flex | 
| Vector maps |  | 
| **Standard raster maps** XYZ |  | 
| Regular updates |  | 
| Search & Geocoding service |  | 
| Commercial use |  | 
| **Export for videos & games** |  | 
| Static maps API |  | 
| WMTS map services |  | 
| No MapTiler logo required | required for 3D sessions | 
| 99.9% SLA |  | 
| Team account |  | 
| Volume discounts |  | 
| Soft-limit on usage quotas |  | 
| Quote & invoice ordering |  | 

|  | Custom | 
| Vector maps |  | 
| **Standard raster maps** XYZ |  | 
| Regular updates |  | 
| Search & Geocoding service |  | 
| Commercial use |  | 
| **Export for videos & games** | contact us for commercial use | 
| Static maps API |  | 
| WMTS map services |  | 
| No MapTiler logo required | required for 3D sessions | 
| 99.9% SLA |  | 
| Team account |  | 
| Volume discounts |  | 
| Soft-limit on usage quotas |  | 
| Quote & invoice ordering |  | 

##### Maps

Load preset dynamic Street, Satellite, and Outdoor maps or use custom-designed map styles. Our JavaScript / TypeScript SDK allows your users to pan, zoom, load 3D terrain, and interact with the map without impacting your bill.

sessions  /month

initialized map object

Read more about Maps | Documentation | API Reference Alternatively, use vector or raster tile requests with third-party SDKs of your choice.

##### Weather

Visualize current conditions and forecasts for rain, clouds, snow, temperature, and more. Enable advanced particle animations at 60FPS. Display weather maps directly in your webpage using the SDK **Weather module.**

sessions /month

initialized map object

##### Search & Geocoding

Place, address, and POI search - with autocomplete - easily added to your maps. Enrich your data with a Batch GeoCoding API, turn addresses into pins on the map, or change coordinates into an address using reverse geocoding.

sessions /month

initialized map object

Read more about Search & Geocoding | Documentation | API reference

##### 3D Sessions

Publish your photorealistic Gaussian Splatting models on immersive 3D maps. Deliver smooth map interaction and high-performance rendering. Display detailed 3D world models directly in your webpage using the **GeoSplats GPU SDK**.

sessions  /month

initialized map object

Read more about GeoSplats | Documentation | API Reference

##### Dataset uploads

###### 3D Dataset uploads

M points /month

Raw splat points to GeoSplats

Read more about GeoSplats | Geodata hosting | API reference

##### APIs

###### Rendered tiles

tiles /month

512px map tiles (counts as 4 requests)

Read more about Rendered tiles | Documentation | API reference

###### Static maps

images /month

1 image = 15 requests

Read more about Static Maps | Documentation | API reference

Extra sessions0k$0

Extra search sessions0k$0

Extra 3D sessions0k$0

Extra API requests0k$0

Extra storage0$0

Extra uploads0$0

Extra 3D uploads0M$0

Total0

#### Included in plans

|  | Free | Flex | Custom | 
| Custom map styles | 5 | 20 | 1000+ | 
| **Storage** | **5 GB / 1 File** | **10 GB** | **Custom** contact us for more | 
| **Sessions** | **5k/month** | **25k/month** | **Custom** | 
| **Search sessions** | **1k/month** | **3k/month** | **Custom** | 
| **3D sessions** | **2k/month** | **10k/month** | **Custom** | 
| **API requests** | **100k/month** | **500k/month** | **Custom** | 
| **Data processing** | **100 uploads/month** | **1k uploads/month** | **Custom** | 
| Raster max upload | 100 GB tiled 1 GB raw details | 100 GB tiled 1 GB raw details | Custom | 
| Vector max upload | 1 GB tiled 10 MB editable details | 1 GB tiled 10 MB editable details | Custom | 
| **3D data processing** | **10M points/month** | **50M points/month** | **Custom** | 
| Splat max upload | 10M points | 50M points | Custom | 
| **Map printing** |  | **10 prints per month** for internal use | **Custom prints** internal or external. Contact us for commercial use | 
| Extra usage |  | See the rates |  | 

|  | Free | 
| Custom map styles | 5 | 
| **Storage** | **5 GB / 1 File** | 
| **Sessions** | **5k/month** | 
| **Search sessions** | **1k/month** | 
| **3D sessions** | **2k/month** | 
| **API requests** | **100k/month** | 
| **Data processing** | **100 uploads/month** | 
| Raster max upload | 100 GB tiled 1 GB raw details | 
| Vector max upload | 1 GB tiled 10 MB editable details | 
| **3D data processing** | **10M points/month** | 
| Splat max upload | 10M points | 
| **Map printing** |  | 
| Extra usage |  | 

|  | Flex | 
| Custom map styles | 20 | 
| **Storage** | **10 GB** | 
| **Sessions** | **25k/month** | 
| **Search sessions** | **3k/month** | 
| **3D sessions** | **10k/month** | 
| **API requests** | **500k/month** | 
| **Data processing** | **1k uploads/month** | 
| Raster max upload | 100 GB tiled 1 GB raw details | 
| Vector max upload | 1 GB tiled 10 MB editable details | 
| **3D data processing** | **50M points/month** | 
| Splat max upload | 50M points | 
| **Map printing** | **10 prints per month** for internal use | 
| Extra usage | See the rates | 

|  | Custom | 
| Custom map styles | 1000+ | 
| **Storage** | **Custom** contact us for more | 
| **Sessions** | **Custom** | 
| **Search sessions** | **Custom** | 
| **3D sessions** | **Custom** | 
| **API requests** | **Custom** | 
| **Data processing** | **Custom** | 
| Raster max upload | Custom | 
| Vector max upload | Custom | 
| **3D data processing** | **Custom** | 
| Splat max upload | Custom | 
| **Map printing** | **Custom prints** internal or external. Contact us for commercial use | 
| Extra usage |  | 

#### Extra usage

|  | Free | Flex | Custom | 
| Sessions | N/A | **$2.50/1k sessions** | Custom | 
| Search sessions | N/A | **$2.50/1k sessions** | Custom | 
| 3D sessions | N/A | **$6.00/1k sessions** | Custom | 
| API requests | N/A | **$0.15/1k requests** | Custom | 
| Data processing | N/A | **$5.00/500 datasets** | Custom | 
| 3D data processing | N/A | **$9.00/100M points** | Custom | 

|  | Free | 
| Sessions | N/A | 
| Search sessions | N/A | 
| 3D sessions | N/A | 
| API requests | N/A | 
| Data processing | N/A | 
| 3D data processing | N/A | 

#### Extra storage

|  | Free | Flex | Custom | 
| Storage 100 GB | N/A | **$20/month** | Custom | 
| Storage 1 TB | N/A | **$140/month** | Custom | 
| Storage 5 TB | N/A | **$520/month** | Custom | 

|  | Free | 
| Storage 100 GB | N/A | 
| Storage 1 TB | N/A | 
| Storage 5 TB | N/A | 

|  | Flex | 
| Storage 100 GB | **$20/month** | 
| Storage 1 TB | **$140/month** | 
| Storage 5 TB | **$520/month** | 

|  | Custom | 
| Storage 100 GB | Custom | 
| Storage 1 TB | Custom | 
| Storage 5 TB | Custom | 

All listed prices are in USD and do not include VAT.

#### Start for Free

#### Trusted by

Sign up for a free account or contact us for a free trial!

We count a Map Session as a webpage or mobile-app load which contains a map initialization.

Map Sessions allow for unlimited user interaction with the map without impacting your bill. A Weather Map Session is counted when adding the weather data overlays to the map.

Map Sessions include usage of:

- all preset or custom map styles
- unlimited requests to all MapTiler tilesets
- unlimited requests to customer-hosted data (vector or raster)
- 3D terrain (tilt limited to 65 Degrees)

Tile API Requests are billed for usage of MapTiler maps with third-party SDKs. API Requests are generated as users interact with the display and load different parts of the map (e.g. panning & zooming).

All the usage statistics are available in the Analytics tab of your MapTiler Cloud account.

On a FREE plan service will pause until the next month without an upgrade to paid plans.

On FLEX, you will receive automatic overuse charges for additional usage at the end of the monthly billing period. You can set a spending limit to control costs.

CUSTOM plans offer a soft limit on usage. If usage significantly exceeds quotas, your Account Manager will contact you.

Volume discounts are available with CUSTOM plans, with annual commitments.

FREE plans do not require billing information.

FLEX plans are charged via credit card or PayPal, with quota overuse charged automatically at the end of each monthly billing period.

CUSTOM plan are charged with invoices, prepaid via credit card or bank transfer.

There are no costs related to using MapTiler services via third-party libraries. We leverage and support SDKs and JavaScript APIs which are 100% open-source.

Storage enables you to host geodata which is private to your account and integrate these data into custom maps.

Data management is made easy by the MapTiler Cloud GUI.

The only plan which allows reselling is the CUSTOM plan. Please contact sales for more information.

All MapTiler products include access to extensive documentation and best effort technical support. Our Customer Success team strives to answer each inquiry personally.

MapTiler also offers a Premium Support package with guaranteed response times and priority issue resolution.

#### What is a request?

We charge based on the number of requests, so you pay only for what you use. A single map view usually generates 4 requests if vector tiles are used, or 10-16 requests for raster tiles with 256px size.

| Type | Requests | 
|---|---|
| TileJSONs, Style JSONs, Fonts, Viewers, XMLs | Free | 
| Vector tile | 1 | 
| Rendered raster 512x512 tile including HiDPI/Retina | 4 | 
| Rendered raster 256x256 tile including HiDPI/Retina | 1 | 
| Single tile served from .mbtiles | 1 | 
| Static maps API image | 15 | 
| Vector data (GeoJSON) | 1 | 
| Search & Geocoding | 1 | 
| Elevation | 1 | 
| Coordinates API | 1 | 
| Export | 50 |

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->

- Preço que a página não renderizou (site, 27/08/2026): **Flex = US$ 30/mês, inclui 25.000 sessões de mapa**. Alternativa sem custo: tiles via Geoapify Free (mesma conta do geocoding).
- Fonte: CalcImov `tmp/estrutura-precos-v2-2026-08-27.md` — valores conferidos no site oficial em 27/08/2026 (câmbio assumido R$ 5,50/USD).
