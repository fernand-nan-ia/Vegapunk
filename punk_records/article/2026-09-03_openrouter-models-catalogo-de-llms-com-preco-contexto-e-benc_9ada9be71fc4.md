---
item_id: "ef770bbe-d8f8-4fe4-97bf-abbd5b365e56"
platform: article
external_id: "9ada9be71fc4"
canonical_url: "https://openrouter.ai/models"
channel: "OpenRouter"
captured_at: 2026-09-03
status: enriched
triage: null
tags: ["openrouter", "llm-gratuito", "modelos-multimodais", "preco-por-token", "rate-limit", "privacidade-de-dados", "vegapunk-bot"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: alta
confidence: media
theme: ia-e-agentes
content_type: article
---

# OpenRouter Models — catálogo de LLMs com preço, contexto e benchmarks

🔗 https://openrouter.ai/models

## Resumo

Catálogo oficial do OpenRouter que compara mais de 400 modelos de linguagem (a página anuncia 500+ contando variantes) de OpenAI, Anthropic, Google, Meta, NVIDIA, MiniMax e outros, todos acessíveis por uma única API compatível com OpenAI. Cada modelo lista preço por token de entrada e saída, janela de contexto e modalidades aceitas (texto, imagem, áudio, vídeo). Em consulta feita em 2026-09-03 via API pública (/api/v1/models), havia 424 modelos, dos quais 21 gratuitos (sufixo :free). Entre os gratuitos com visão — requisito do bot Vegapunk, que lê slides de TikTok como imagem — destacam-se minimax/minimax-m3:free (1M de contexto, texto+imagem+vídeo), thinkingmachines/inkling:free (1M, texto+imagem+áudio), google/gemma-4-31b-it:free e gemma-4-26b-a4b-it:free (262k, imagem+vídeo) e nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free (256k, omni). A extração direta da página falhou (conteúdo via JavaScript); os dados vieram da API, que é a fonte da própria página. Ressalva prática: endpoints :free têm cota baixa (~20 req/min e ~50 req/dia com menos de US$10 em créditos na conta; ~1000/dia acima disso) e podem usar os dados enviados para treino, o que pesa contra usá-los num vault pessoal.

## Tópicos

- **Modelos gratuitos (:free)** — 21 dos 424 modelos têm preço zero de entrada e saída. Cota limitada (~20 req/min; ~50 req/dia abaixo de US$10 em créditos, ~1000/dia acima) e dados podem alimentar treino.
- **Gratuitos com visão** — 8 aceitam imagem na entrada; os úteis para leitura de slides: minimax-m3:free, inkling:free e inkling-small:free, gemma-4-31b/26b:free, nemotron-3-nano-omni:free, dots-3-note-preview:free.
- **Comparação de preço e contexto** — A página lista preço por milhão de tokens (entrada/saída), janela de contexto e benchmarks lado a lado, filtráveis por modalidade, série e provedor.
- **API única** — Todos os modelos são servidos pela mesma API compatível com OpenAI; trocar de modelo é trocar uma string de identificação (ex.: VEGAPUNK_MODEL no .env do bot).

## Ferramentas citadas

- **OpenRouter**: agregador/roteador de LLMs com API única e catálogo comparativo de preços
- **minimax/minimax-m3:free**: modelo gratuito multimodal (texto+imagem+vídeo, 1M de contexto)
- **thinkingmachines/inkling:free**: modelo gratuito multimodal (texto+imagem+áudio, 1M de contexto)
- **google/gemma-4-31b-it:free**: modelo aberto gratuito do Google com visão (262k de contexto)
- **nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free**: modelo gratuito omni (texto+áudio+imagem+vídeo) com raciocínio
- **google/gemini-3.7-flash**: modelo pago em uso no bot Vegapunk; referência de custo baixíssimo com visão boa

## Pontos-chave

- Em 2026-09-03 a API /api/v1/models listava 424 modelos; 21 com preço zero (sufixo :free).
- 8 dos gratuitos aceitam imagem na entrada; só ~5 servem de fato para chat com visão (lyria é música, content-safety é moderação, openrouter/free é roteador genérico).
- Cota dos :free: ~20 req/min; ~50 req/dia com menos de US$10 em créditos na conta, ~1000/dia acima disso.
- Endpoints gratuitos podem usar os prompts para treino — risco de privacidade para conteúdo pessoal.
- O gemini-3.7-flash pago custa fração de centavo por item processado (~10k tokens por slideshow), então a economia de migrar para :free é quase nula.
- Trocar de modelo no bot é uma linha: VEGAPUNK_MODEL no .env + restart do container.
- A página /models não é extraível por scraping simples (JS); a fonte confiável é a API pública /api/v1/models.

## Como aplicar

Para o bot Vegapunk: manter gemini-3.7-flash (custo desprezível, visão boa) e usar um :free multimodal só como fallback ou experimento, via VEGAPUNK_MODEL. Para o SaaS: a API única do OpenRouter permite trocar de modelo sem reescrever integração, e a cota dos :free serve para protótipos, nunca para produção.

## 🏴‍☠️ Lilith diz

Ah, o paraíso do 'grátis', Fernando. 21 modelos de graça e ninguém te conta na página bonita que a cota morre em 50 requisições e que teus dados viram ração de treino — tem link na bio pra reclamar? O flash que tu já paga custa migalha e enxerga slide direito; trocar isso por :free é economizar centavo pra pagar em dor de cabeça.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Granite 4.2 8B is a dense reasoning model from IBM. It is suited for mathematics, code generation, multilingual dialogue, and agentic workflows that need multi-step reasoning. It supports full, low-effort, and non-thinking modes.  The model supports 12 languages: English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, and Chinese.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
