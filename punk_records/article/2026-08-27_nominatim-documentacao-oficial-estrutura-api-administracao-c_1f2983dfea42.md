---
item_id: "8148dd23-81ad-4760-927b-07c496d6425d"
platform: article
external_id: "1f2983dfea42"
canonical_url: "https://nominatim.org/release-docs/latest"
channel: "nominatim.org"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["nominatim", "documentacao", "geocoding", "python", "openstreetmap"]
applicability:
  saas_pessoal: media
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Nominatim — documentação oficial: estrutura (API, administração, customização, biblioteca Python, desenvolvimento)

🔗 https://nominatim.org/release-docs/latest

## Resumo

Introdução da documentação do Nominatim ('por nome', em latim): ferramenta para buscar dados do OSM por nome e endereço e gerar endereços sintéticos para pontos (geocodificação reversa), com busca limitada por tipo de feature (bares, hotéis, igrejas). O guia tem cinco partes: referência da API para usuários; guia de administração para instalar um servidor próprio; guia de customização para adaptar a instalação; guia de biblioteca para desenvolvedores Python que queiram usar o Nominatim como biblioteca; guia do desenvolvedor do software.

## Tópicos

- **Partes** — API · Administração · Customização · Biblioteca Python · Desenvolvedor.

## Pontos-chave

- Existe modo biblioteca em Python — dá para chamar de dentro do SaaS sem servidor HTTP à parte.
- Guia de administração é o caminho para instalar no VPS.

## Como aplicar

Começar pelo guia de administração (instalar recorte do Brasil) e pela biblioteca Python.

## 🔧 Atlas diz

Índice, não conteúdo — mas o índice diz o que importa: tem biblioteca Python. Quando for construir, leio Administração e Library; o resto é para quem mexe no motor.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Introduction

Nominatim (from the Latin, 'by name') is a tool to search OSM data by name and address and to generate synthetic addresses of OSM points (reverse geocoding). It has also limited capability to search features by their type (pubs, hotels, churches, etc).

This guide comes in five parts:

- **API reference** for users of Nominatim
- **Administration Guide** for those who want
   to install their own Nominatim server
- **Customization Guide** for those who want to
   adapt their own installation to their special requirements
- **Library Guide** for Python developers who
   want to use Nominatim as a library in their project
- **Developer's Guide** for developers of the software

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
