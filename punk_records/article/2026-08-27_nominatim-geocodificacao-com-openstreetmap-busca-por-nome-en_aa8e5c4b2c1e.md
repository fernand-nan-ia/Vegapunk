---
item_id: "dcc847ae-7395-43a7-bf3f-7db6ccd9c1e4"
platform: article
external_id: "aa8e5c4b2c1e"
canonical_url: "https://nominatim.org/"
channel: "Osm-Search; Nominatim · nominatim.org"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["nominatim", "geocoding", "openstreetmap", "mapas", "open-source", "enderecos"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Nominatim — geocodificação com OpenStreetMap: busca por nome/endereço, reverso, instalação própria escalável

🔗 https://nominatim.org/

## Resumo

Nominatim é o software de geocodificação que usa dados do OpenStreetMap: encontra locais por nome ou endereço (consulta livre em qualquer idioma, ex.: 'Cafe Paris, New York', ou estruturada por postcode/city/type, útil para geocodificar listas de endereços) e faz o reverso (endereço a partir de latitude/longitude ou de um objeto OSM). Instalação escalável: de uma cidade num laptop ao planeta inteiro num servidor maior; importa só os recursos do OSM que você escolher; atualizações minuto a minuto; é o motor do site oficial openstreetmap.org, servindo 30 milhões de consultas/dia num único servidor. Mantido com apoio de empresas e GitHub Sponsors.

## Tópicos

- **Geocoding** — Consulta livre ou estruturada; qualquer idioma; listas de endereços.
- **Reverso** — Lat/lon ou ID OSM → endereço.
- **Instalação** — Escala de cidade a planeta; importa só o necessário; updates por minuto.
- **Prova** — 30 M consultas/dia no site oficial do OSM.

## Pontos-chave

- Alternativa gratuita à API de Places para transformar endereço em coordenada — sem chave nem cobrança por consulta.
- Instância própria evita os limites de uso do serviço público do OSM.
- Dados do OSM no Brasil variam por cidade — validar antes de depender.

## Como aplicar

Geocodificar endereços de imóveis (laudos NBR 14653) e de clientes com uma instância Nominatim no VPS (KVM 2, item Hostinger), sem pagar Google.

## 🔧 Atlas diz

Isso conversa com o squad de laudos: endereço do imóvel vira coordenada sem chave do Google. Roda no VPS que a York orçou. Parafuso a conferir antes: cobertura do OSM na cidade do laudo — em capital é boa, no interior varia.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Nominatim uses OpenStreetMap data to find locations on Earth by name and address (geocoding). It can also do the reverse, find an address for any location on the planet.

### Features

#### Find places by name or address (Geocoding)

Nominatim can power the search box on your website, allowing your users to type free-form queries (“Cafe Paris, New York”) in any language. It also offers a structured query mode (“postcode=12345”, “city=London”, “type=cafe”) that helps you to automate geocoding of extensive address lists.

#### Look up addresses for a location (Reverse geocoding)

Given a latitude and longitude anywhere on the planet, Nominatim can find the nearest address. It can do the same for any OSM object given its ID.

#### Scalable installation

Nominatim scales with your needs. Run a search service for your city on a laptop or set up a larger server with data of the whole planet.

#### Configurable setup

You can decide which features of OpenStreetMap are important to you. Nominatim imports only what you tell it to.

#### Always up-to-date with OpenStreetMap

OpenStreetMap data is constantly improved by thousands of editors. Keep up to date with these changes through minutely updates.

#### Fast

Nominatim is the geocoding software that powers the official OSM site www.openstreetmap.org. It serves 30 million queries per day on a single server.

### Supporters

We thank the following companies for their support of parts of the Nominatim development:

Are you interested in supporting Nominatim? Support us through Github Sponsors or check out the Funding page for other options.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
