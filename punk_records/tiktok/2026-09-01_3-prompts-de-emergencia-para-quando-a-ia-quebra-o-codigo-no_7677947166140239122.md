---
item_id: "075fe3fc-fd9e-41b9-b730-cd6b2f1ac32b"
platform: tiktok
external_id: "7677947166140239122"
canonical_url: "https://www.tiktok.com/@purevibecoding/photo/7677947166140239122"
channel: "Vibecoding"
captured_at: 2026-09-01
status: archived
triage: archive
tags: ["vibe-coding", "claude-code", "prompt-engineering", "debugging", "cursor", "troubleshooting"]
applicability:
  saas_pessoal: alta
  projeto_cliente: alta
  estudo_geral: media
confidence: alta
theme: ia-e-agentes
content_type: slides
---

# 3 prompts de emergência para quando a IA quebra o código no Vibe Coding

🔗 https://www.tiktok.com/@purevibecoding/photo/7677947166140239122

## Resumo

No desenvolvimento assistido por IA, é comum que ferramentas como Claude Code ou Cursor quebrem funcionalidades existentes ao tentar resolver um problema. O erro mais frequente do desenvolvedor é entrar em um ciclo repetitivo de 'tente novamente', piorando o estado do código. Para evitar isso, o autor propõe três comandos estruturados de contenção. O primeiro instrui a IA a fazer apenas a menor alteração estrita, proibindo refatorações desnecessárias. O segundo força a IA a pausar modificações e listar três hipóteses diagnósticas com métodos de validação antes de qualquer edição. Por fim, o terceiro comando exige a comparação detalhada entre o estado atual e a última versão funcional para isolar a causa exata da regressão.

## Tópicos

- **Contenção de escopo** — Instruir a IA a realizar apenas a menor alteração necessária, bloqueando refatorações arquiteturais.
- **Diagnóstico de causa raiz** — Fazer o modelo pausar a escrita de código e levantar 3 hipóteses testáveis antes de propor soluções.
- **Isolamento de regressão** — Exigir a comparação explícita entre a versão atual quebrada e o último estado funcional para identificar o delta problemático.

## Ferramentas citadas

- **Claude Code**: Ferramenta de IA para desenvolvimento de software citada no contexto de quebras de código.
- **Cursor**: IDE com IA citada como exemplo de ferramenta propensa a loops de erro.
- **Lovable**: Plataforma de geração de aplicações via IA citada no contexto de vibe coding.

## Pontos-chave

- Evitar o comando 'tenta de novo' ao presenciar erros sucessivos da IA.
- Tratar correções pontuais como 'cirurgia' e não como 'reforma' de arquitetura.
- Exigir validação de hipóteses antes de permitir que o agente continue alterando arquivos.
- Usar comparação de diff contra a última versão estável para desfazer regressões.

## Como aplicar

Adicione esses 3 padrões de instrução ao CLAUDE.md ou memorize-os para interromper o Claude Code sempre que ele começar a refatorar arquivos adjacentes sem resolver o bug principal do SaaS ou do site do cliente.

## 🧠 Stella diz

Kwahaha! Brilhante em sua simplicidade, Fernando! O ímpeto humano de gritar 'tente de novo' para um cérebro eletrônico em colapso é fascinante, porém desastroso. Estabelecer protocolos de contenção cirúrgica antes que a máquina reescreva metade do seu projeto é pura sabedoria científica, Quasar!

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
