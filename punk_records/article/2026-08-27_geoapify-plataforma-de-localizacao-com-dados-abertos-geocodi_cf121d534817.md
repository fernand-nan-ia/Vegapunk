---
item_id: "39fbb438-9530-40cd-869d-cdc8a69acdfc"
platform: article
external_id: "cf121d534817"
canonical_url: "https://www.geoapify.com/"
channel: "Geoapify GmbH"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["geoapify", "geocoding", "openstreetmap", "isocronas", "routing", "licenca"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Geoapify — plataforma de localização com dados abertos: geocoding, rotas, lugares, isócronas; licença permissiva (pode guardar resultados)

🔗 https://www.geoapify.com/

## Resumo

Geoapify é um conjunto de APIs de localização (exibição de mapas, busca de endereço/geocoding, roteirização, descoberta de lugares, análise de alcance/isócronas) construído sobre dados abertos — GeoNames, OpenStreetMap, OpenAddresses e GTFS — com playground, tutoriais, bibliotecas NPM e exemplos no GitHub. Diferenciais declarados: dados abertos e transparentes; licença permissiva que permite cachear, armazenar e redistribuir resultados (ex.: montar sua própria base de endereços a partir do geocoding) sem custo extra, ao contrário de provedores com limites de reuso; preços previsíveis com plano gratuito utilizável em projetos comerciais (com atribuição) e planos custom 'unmetered' para alto volume; sem vendor lock-in.

## Tópicos

- **APIs** — Mapas, geocoding, routing, places, isócronas.
- **Dados** — GeoNames, OSM, OpenAddresses, GTFS.
- **Licença** — Cachear/armazenar/redistribuir resultados permitido; Free comercial com atribuição.
- **Dev** — Playground, tutoriais, NPM, GitHub.

## Pontos-chave

- Guardar o resultado do geocoding no seu banco é permitido — Google proíbe.
- Free comercial com atribuição 'Powered by Geoapify'.
- Isócronas (alcance em X minutos) servem para análise de localização de imóveis.

## Como aplicar

Geocodificar endereços de laudos/clientes e guardar as coordenadas no banco (licença permite); isócronas para 'o que está a 10 min do imóvel'.

## 🔧 Atlas diz

Parafuso jurídico que vale ouro: você pode guardar o endereço geocodificado no seu banco. Com o Google, não. Para laudo de imóvel isso é a diferença entre pagar toda vez e pagar uma vez. Nominatim grátis + Geoapify Free = geocoding sem chave do Google e sem VPS, para começar.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Geoapify Location Platform for Maps, Geocoding, Routing, and Places

Start quickly with tutorials, code samples, and an API playground to test endpoints and generate requests. Built on open data, Geoapify provides global coverage for addresses, places, and routing.

#### What Is Geoapify Location Platform?

Geoapify Location Platform is a complete set of location APIs and developer resources for building, testing, and scaling map-based applications.

From map display and address search to route planning, place discovery, and reachability analysis, Geoapify brings core location capabilities into one platform. Explore the API groups below, or go directly to Which Map API Do You Need?.

We help you build faster with an API Playground, step-by-step tutorials, NPM libraries, and GitHub code samples. Built on open data, Geoapify gives you full control, including the ability to store results on your side without restrictive caching limits.

Give it a try today! Sign up and get your free API key.

#### Why Choose Geoapify Location Platform?

Geoapify is built for business use: open-data-based APIs, permissive licensing, predictable pricing, global coverage, fast integration, and developer tooling, with flexible scaling, no vendor lock-in, and responsive support.

##### Open-data advantage

Geoapify services are built on open data, and our policy is to **keep open data open**, with transparent sources and processing you can trust and control.

Key sources include GeoNames, OpenStreetMap, OpenAddresses, and transit schedule data from GTFS.

Community-based data often exceeds proprietary datasets in coverage, freshness, and local detail, with transparent sources that make results easier to validate.

##### Permissive licensing

Use Geoapify with your preferred stack and third-party services, **without restrictive vendor lock-in terms**.

Unlike many providers with strict reuse limits, **Geoapify lets you cache, store, and redistribute results** according to our terms, without extra costs for data reuse.

For example, you can build and maintain your own reusable address database from geocoding results.

##### Predictable pricing

We provide pricing for every business size, **from a free tier to scalable paid plans**.

Geoapify focuses on infrastructure, processing, and service quality instead of owning proprietary datasets. This allows us to provide **affordable pricing** without compromising API quality or reliability.

You get clear costs and strong value for both growing projects and high-volume workloads.

Want to review how Geoapify terms fit your business? Check our Pricing, try the API Playground, or contact us to discuss licensing and data usage.

#### Flexible Pricing for Businesses of Any Size

**Start for free**, then scale at your own pace with predictable plans as usage grows. From startups to enterprise workloads, Geoapify supports every stage with flexible options, including **custom unmetered plans** for high query volumes.

##### Startups

Geoapify includes a **Free Plan** with a generous **Free tier**.

You can use it for commercial projects and stay on the free plan as long as your usage remains within the limits, which usually covers development, educational, and startup needs.

##### Small and midsize businesses

We offer multiple pricing plans so you can choose the one that fits your current usage and scale as you grow.

If you exceed your quota, we won’t block your service or apply surprise overage charges, and we’ll help you choose the right plan for your needs.

Learn more on our Pricing page, or contact us to discuss the best plan for your use case.

#### Which Location API Do You Need?

Geoapify Location Platform includes a wide range of APIs, and most real-world use cases are solved by combining several of them. Below are common scenarios with recommended API combinations.

##### Maps

Build vector and raster maps for web and GIS applications with reliable global coverage and flexible styling.

Use Geoapify map services with Leaflet, MapLibre GL, OpenLayers, QGIS, and other mapping tools. Generate static map images and custom marker visuals to match your product design.

##### Address and Location Search

Search addresses and places, convert addresses to coordinates, and reverse geocode coordinates to addresses with reliable global coverage.

Geoapify geocoding tools support validation, formatting, autocomplete, batch workflows, and multilingual results for production use.

##### Routes and Optimization

Calculate efficient routes for single vehicles or fleets, with detailed geometry, road attributes, and turn-by-turn directions.

Geoapify routing services support logistics and field operations with route matrices, map matching, and multi-stop route optimization.

- Routing API
- Route Matrix API - calculate distance and time between multiple points
- Map Matching API - match GPS coordinates to existing roads
- Route Planner API - solve VRP related tasks

##### Places, Place Details, and Postcodes

Search places and points of interest, retrieve place details, and work with postcode data for location-based products and analytics.

Filter results by area, category, geometry, and reachability to build precise search and discovery experiences.

##### Reachability and Analysis

Analyze what can be reached within a given time or distance and turn raw location data into actionable insights for logistics, planning, and service coverage.

Build isochrones and isodistances for drive, truck, bicycle, walk, and transit, combine or intersect areas, and enrich route and location analysis with elevation data.

- Isolines API - isochrones and isodistances
- Geometry API - find union or intersection of several areas
- Elevation API - get elevation and terrain profile data

Need a feature or API that isn’t listed here? Get in touch and we’ll help you find the right solution.

#### FAQ

##### What is a location platform?

A location platform provides the location APIs, components, and geodata you need to develop location-based applications and maps.

##### What do I need to develop a location-aware application?

A location-aware app requires location services such as address search, route builder tools, and geodata. Geoapify Location Platform APIs give you access to the geospatial services and data you need to build map applications and location components.

##### What are the main advantages of Geoapify's location platform?

Geoapify offers a business-friendly location platform with a permissive license, allowing easy integration and use. Our services are affordably priced and scalable to meet your business needs, providing advanced geocoding, mapping, and routing solutions with high accuracy and reliability.

##### How does Geoapify compare to other location platforms?

Geoapify stands out due to its affordable pricing, flexible terms, and comprehensive geospatial services. Unlike some alternatives, Geoapify provides a permissive license, allowing for easier integration and broader usage without restrictive terms.

##### How does Geoapify's permissive license benefit users?

Geoapify's permissive license allows users to cache, store, and redistribute geospatial data, offering significant flexibility. This means you can integrate and use the data in various applications without restrictive terms. However, proper attribution is required, which is provided with the results, ensuring compliance and ease of use for commercial and large-scale projects.

##### Can I use Geoapify's location platform for my business projects?

Yes, Geoapify’s location platform is designed with businesses in mind. Our APIs are scalable and reliable, suitable for a wide range of applications from small startups to large enterprises. The business-friendly terms ensure you can grow without worrying about prohibitive costs or restrictive licenses.

##### Do I need a credit card to start?

No. You can sign up, get a free API key, and start using Geoapify on the Free plan without a credit card.

##### How does Geoapify pricing scale with usage?

Geoapify offers a Free plan for low-volume usage and paid plans that scale with your needs. For high-volume workloads, we also provide custom and unmetered options. See the Pricing page for details.

##### Can Geoapify be used with Leaflet, MapLibre, OpenLayers, or Google Maps?

Yes. Geoapify APIs are framework-agnostic and can be integrated with Leaflet, MapLibre, OpenLayers, Google Maps, and custom stacks via standard HTTP APIs and SDKs.

##### Can I cache and store API results?

Yes. Geoapify provides business-friendly terms that allow caching and storing results, and in many cases redistribution according to our terms.

##### How can I use Maps API for free?

1. Register and get an API key on the Geoapify MyProject page. 

  2. Learn how to use APIs on the API Docs page or generate an API link with the Playground. 

  3. When you stay within the Free pricing plan quota, you can use the Maps API for free, even for a commercial app.
    

##### Can I store the data I received by using Maps API?

We know how important it is to have control of the data you generate. You are free to download and store all the data and components you create with Geoapify. But please remember the required OpenStreetMap attribution. By default, the attribution is provided as a part of the result object. If you are on a Free plan, please also add a "follow" link on your website to attribute Geoapify as data provider:

    `Powered by <a href="https://www.geoapify.com/">Geoapify</a>`

#### Need a Custom Location Setup?

- Custom location workflows and map components
- Geodata pipelines, enrichment, and spatial analytics
- Commercial support for open-source mapping components
- On-premise, dedicated and managed installations
- Consulting and professional services

We can help you validate architecture, migration, and performance targets before production rollout.

Need specific compliance, data residency, or high-volume requirements? We can design a setup that fits.

Explore APIs in the Playground or get in touch to discuss your requirements.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
