---
item_id: "7c08f7a3-b717-401f-a162-86a2ef0e72a8"
platform: tiktok
external_id: "7683346049486015762"
canonical_url: "https://www.tiktok.com/@verticeclubsolutions/photo/7683346049486015762"
channel: "verticeclubsolutions"
captured_at: 2026-09-09
status: enriched
triage: null
tags: ["agentes-de-codigo", "claude-code", "npx-installer", "cadeia-de-agentes", "risco-de-supply-chain", "regras-de-agente"]
applicability:
  saas_pessoal: media
  projeto_cliente: baixa
  estudo_geral: alta
confidence: media
theme: ia-e-agentes
content_type: slides
---

# ECC: pacote que instala 68 agentes e 286 skills no assistente de código

🔗 https://www.tiktok.com/@verticeclubsolutions/photo/7683346049486015762

## Resumo

O post apresenta o ECC, um pacote instalável por um comando que promete acabar com a improvisação do assistente de código ao impor um método fixo. O problema que ele diz resolver: o agente faz de um jeito hoje e de outro amanhã, e o resultado muda sem explicação. A proposta é instalar um time inteiro — um agente planeja, outro escreve o teste, outro implementa e outro revisa. Os números citados pelo autor, que ele afirma ter conferido na API do GitHub, são 254.033 estrelas, 38.090 forks, licença MIT e 1.426 estrelas em um único dia; o README informaria 68 agentes, 286 skills, 94 comandos e 997 testes passando. A instalação é `npx ecc-universal setup` e o instalador reconheceria a ferramenta já em uso — Claude Code, Codex, Cursor, Zed, Gemini CLI e Copilot, entre outras. O próprio post levanta o cuidado central: o pacote escreve regras que passam a guiar o seu agente, então é para ler o repositório antes e instalar primeiro numa pasta de teste, nunca direto no projeto do cliente. A recomendação final é usar por uma semana num projeto sem valor antes de levar para o trabalho.

## Tópicos

- **Problema alegado** — O agente de código improvisa: muda de método a cada tarefa e o resultado varia sem explicação.
- **Método imposto** — Papéis separados — um agente planeja, outro escreve o teste, outro implementa, outro revisa.
- **Números de tração** — O autor afirma 254.033 estrelas, 38.090 forks e 1.426 estrelas em um dia, ditos conferidos via API do GitHub.
- **Risco de instalação** — O pacote grava regras no seu ambiente que passam a governar o agente; ler o repositório e isolar em pasta de teste.

## Ferramentas citadas

- **ECC (ecc-universal)**: pacote npx que instala agentes, skills e comandos no assistente de código
- **Claude Code**: um dos assistentes suportados pelo instalador
- **Codex**: assistente suportado
- **Cursor**: assistente suportado
- **Zed**: editor suportado
- **Gemini CLI**: assistente suportado
- **GitHub Copilot**: assistente suportado

## Pontos-chave

- Instalação por um comando: `npx ecc-universal setup`.
- Promete 68 agentes, 286 skills, 94 comandos e 997 testes passando, sob licença MIT.
- A contagem de 254 mil estrelas é afirmação do post, não verificada aqui — número dessa ordem colocaria o repo entre os maiores do GitHub.
- O ganho alegado é determinismo de processo: sempre plano, teste, código e revisão.
- O pacote escreve regras que passam a guiar o agente — é injeção de instrução no seu ambiente, não só arquivos.
- Recomendação do próprio autor: instalar em pasta descartável e usar uma semana antes de levar para projeto real.

## Como aplicar

Fernando já mantém um conjunto próprio de agentes (Satélites do Vegapunk, squads do FURY) com fonte da verdade única; instalar um pacote que grava regras por cima pode contaminar `.claude/` e brigar com o `sync_agents.sh`. Se for testar, replicar o que já foi feito com as skills de design: pasta de teste isolada, nunca a pasta do Vegapunk nem a de cliente.

## 🪖 Shaka diz

Registro o que é fato e o que não é. Fato: o pacote grava regras que passam a comandar seu agente — isso é código executável em forma de texto, e o próprio autor admite. Não é fato: as 254 mil estrelas, que são afirmação do post e colocariam o projeto entre os maiores repositórios do mundo sem que ninguém tenha ouvido falar dele. Se testar, testar em pasta descartável, longe do `.claude/` que você mantém à mão.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
