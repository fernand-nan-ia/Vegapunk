---
item_id: "3e230100-a861-4961-9993-976e29a846c6"
platform: tiktok
external_id: "7678524435174788373"
canonical_url: "https://www.tiktok.com/@eugustavosextaro/video/7678524435174788373"
channel: "eugustavosextaro"
captured_at: 2026-09-01
status: applied_saas
triage: apply_saas
tags: ["nextjs", "vite", "react", "escolha-de-stack", "vibe-coding", "ssr", "arquitetura"]
applicability:
  saas_pessoal: alta
  projeto_cliente: alta
  estudo_geral: media
confidence: media
theme: desenvolvimento-e-ferramentas
content_type: whisper
---

# Por que todo projeto vibe-codado nasce em Next.js — e quando trocar de stack

🔗 https://www.tiktok.com/@eugustavosextaro/video/7678524435174788373

## Resumo

Gustavo Sextaro explica por que praticamente todo projeto gerado por IA sai em Next.js e quando isso deixa de fazer sentido. Aponta três causas: Next é a stack mais representada nos dados das ferramentas de geração como Bolt e Lovable; tem deploy de um clique na Vercel; e resolve front-end e back-end na mesma rota, o que dispensa a IA de decidir arquitetura — ela apenas empilha tudo dentro de um framework. O ponto crítico não é a stack em si, e sim o uso: essas ferramentas foram feitas para prototipar antes de lançar, e as pessoas acabam mantendo o protótipo e publicando para milhares de usuários se cadastrarem. Ele delimita onde Next funciona bem — dashboard próprio, produto mais simples com autenticação — e onde não sustenta escala. Como alternativa, mostra Vite + React: sem framework full-stack, apenas bundler mais roteador de client-side, adequado a dashboard interno, painel logado ou ferramenta que só existe atrás de login. Explicita o trade-off: perde-se SSR e o SEO de fábrica, o que é irrelevante numa área logada. Fecha recomendando que se pesquise variações de stack, porque provavelmente 100% dos projetos do espectador estão em Next/React sem que essa tenha sido uma decisão. Transcrição automática com erros ('NextHacked' por Next.js, 'IaaS' por IAs, 'MIDI' por Markdown).

## Tópicos

- **Por que sempre Next** — É a stack mais representada nos dados das ferramentas, tem deploy de um clique na Vercel e resolve front e back na mesma rota — a IA não precisa decidir arquitetura.
- **O erro de uso** — As ferramentas foram feitas para prototipar antes de lançar; o problema é manter o protótipo e publicá-lo para milhares de cadastros.
- **Onde Next funciona** — Dashboard próprio, produto mais simples com autenticação — não para escala.
- **Vite + React como alternativa** — Sem framework full-stack: bundler e roteador de client-side, para dashboard interno, painel logado ou ferramenta atrás de login.
- **O trade-off explícito** — Perde-se SSR e SEO de fábrica — irrelevante em área logada, decisivo em página pública.

## Ferramentas citadas

- **Next.js**: stack padrão de saída das ferramentas de geração por IA
- **Bolt e Lovable**: geradores citados como origem do viés de stack
- **Vercel**: deploy de um clique, um dos motivos do padrão
- **Vite + React**: alternativa para painel logado, sem SSR nem SEO de fábrica

## Pontos-chave

- A stack do projeto gerado é escolha da FERRAMENTA, não sua — e quase ninguém percebe que houve escolha
- Next resolve front e back na mesma rota, o que poupa a IA de decidir arquitetura
- As ferramentas de geração foram desenhadas para prototipar, não para sustentar produto público
- O risco concreto é publicar o protótipo para milhares de cadastros
- Dashboard próprio e produto simples com autenticação: Next serve bem
- Vite + React é adequado a área logada, onde perder SSR e SEO não custa nada
- '100% dos projetos de vocês provavelmente estão em Next/React' — vale reavaliar caso a caso
- Transcrição automática ruidosa: 'NextHacked' = Next.js, 'IaaS' = IAs

## Como aplicar

Antes de aceitar a stack que a ferramenta cuspir no SaaS pessoal, decidir de propósito: se o produto for painel logado (avaliação de imóveis, laudos), Vite + React basta e evita a complexidade do full-stack. Para o site do cliente vale o inverso: é página pública, precisa de SEO e SSR — ali Next se justifica por motivo, não por inércia.

## 🪖 Shaka diz

O senhor deve reter uma frase deste vídeo: a stack não foi escolhida, foi herdada da ferramenta. Isso não é opinião, é o comportamento documentado dos geradores — e decisão que ninguém tomou é decisão que ninguém revisa. Antes de publicar qualquer coisa que aceite cadastro, pergunte-se se está no protótipo ou no produto. São coisas diferentes, e só uma delas aguenta usuário.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
