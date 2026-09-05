---
item_id: "07e8d4b1-5e81-498c-ae87-e343cf7c0cca"
platform: article
external_id: "f4b0aa5f6b1a"
canonical_url: "https://github.com/oae/kaizoku"
channel: "Oae · GitHub"
captured_at: 2026-09-05
status: enriched
triage: null
tags: ["kaizoku", "manga-self-hosted", "docker-compose", "biblioteca-de-manga", "suwayomi", "mangal"]
applicability:
  saas_pessoal: nenhuma
  projeto_cliente: nenhuma
  estudo_geral: baixa
confidence: alta
theme: jogos-e-entretenimento
content_type: article
---

# Kaizoku: downloader de mangá self-hosted

🔗 https://github.com/oae/kaizoku

## Resumo

O Kaizoku é um downloader de mangá self-hosted que organiza uma biblioteca local a partir de fontes suportadas pelo mangal, que ele usa por baixo. O README abre com dois avisos do próprio mantenedor: ele sugere hoje a combinação Suwayomi para downloads e Komf para metadados, servidos por Komga ou Kavita; e informa que existe um fork mais novo chamado kaizoku-next mantido por outra pessoa. O projeto continua funcionando como está. A instalação recomendada é por docker compose, com três serviços: a aplicação, um Redis para a fila de trabalhos e um Postgres para o banco, com volumes separados para biblioteca, configuração e logs, e a porta 3000 exposta. As variáveis principais são a URL do banco, host e porta do Redis, PUID e PGID do usuário do host e o fuso horário. Para desenvolvimento, o projeto pede Node 18, pnpm, Docker e o mangal instalado, subindo Redis e Postgres por compose e aplicando as migrações do Prisma antes de rodar.

## Tópicos

- **Aviso do mantenedor** — Ele passou a sugerir Suwayomi para downloads e Komf para metadados, com Komga ou Kavita servindo; o Kaizoku segue funcionando, e há o fork kaizoku-next.
- **Deploy por docker compose** — Três serviços — aplicação, Redis e Postgres com healthcheck — mais volumes para biblioteca, configuração e logs, expondo a porta 3000.
- **Ambiente de desenvolvimento** — Exige Node 18, pnpm, Docker e o mangal instalado; sobe Redis e Postgres por compose e aplica as migrações do Prisma.

## Ferramentas citadas

- **mangal**: motor de download de mangá usado por baixo do Kaizoku
- **Suwayomi**: alternativa recomendada hoje pelo próprio mantenedor para downloads
- **Komf**: complemento recomendado para metadados
- **Komga e Kavita**: servidores de biblioteca sugeridos para servir o acervo
- **Prisma**: camada de migração do banco Postgres

## Pontos-chave

- O próprio mantenedor recomenda hoje Suwayomi mais Komf, servidos por Komga ou Kavita.
- Existe um fork mais recente, kaizoku-next, mantido por outra pessoa.
- O deploy padrão é docker compose com Postgres, Redis e a aplicação na porta 3000.
- PUID e PGID do usuário do host precisam ser passados para os arquivos saírem com dono correto.
- O Kaizoku depende do mangal instalado para funcionar.

## Como aplicar

Uso pessoal, não de projeto. O que se aproveita tecnicamente é o padrão de compose com fila em Redis e healthcheck no Postgres, semelhante ao que o Vegapunk já faz com o próprio container.

## 📚 Pythagoras diz

O registro diz duas coisas antes de qualquer elogio: o mantenedor recomenda outra ferramenta no lugar desta, e existe um fork mais novo. Deduzo que o projeto está em manutenção mínima. Guardo pela referência de arquitetura — fila em Redis, banco com healthcheck, volumes separados — e recomendo olhar o Suwayomi antes de instalar este.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

- 
I suggest using Suwayomi (For downloads) and Komf (For metatada) with Komga or Kavita.
- 
Kaizoku still works as is. But there is a new fork by @ElryGH that you can check out at kaizoku-next

Kaizoku is self-hosted manga downloader.

| Detail Page | Search | 
|---|---|

You can deploy Kaizoku with following docker-compose file

```
version: '3'
volumes:
  db:
  redis:
services:
  app:
    container_name: kaizoku
    image: ghcr.io/oae/kaizoku:latest
    environment:
      - DATABASE_URL=postgresql://kaizoku:kaizoku@db:5432/kaizoku
      - KAIZOKU_PORT=3000
      - REDIS_HOST=redis
      - REDIS_PORT=6379
      - PUID=<host user puid>
      - PGID=<host user guid>
      - TZ=Europe/Istanbul
    volumes:
      - <path_to_library>:/data
      - <path_to_config>:/config
      - <path_to_logs>:/logs
    depends_on:
      db:
        condition: service_healthy
    ports:
      - '3000:3000'
  redis:
    image: redis:7-alpine
    volumes:
      - redis:/data
  db:
    image: postgres:alpine
    restart: unless-stopped
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U kaizoku']
      interval: 5s
      timeout: 5s
      retries: 5
    environment:
      - POSTGRES_USER=kaizoku
      - POSTGRES_DB=kaizoku
      - POSTGRES_PASSWORD=kaizoku
    volumes:
      - db:/var/lib/postgresql/data
```
- node 18
- pnpm
- docker
- mangal

```
git clone https://github.com/oae/kaizoku.git
cd ./kaizoku/
cp .env.example .env
pnpm i
docker compose up -d redis db
pnpm prisma migrate deploy
pnpm dev
```
Open http://localhost:3000 with your browser to see the page.

Kaizoku uses amazing mangal by @metafates as it's downloader.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
