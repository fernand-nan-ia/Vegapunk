---
item_id: "e0723f8d-ece8-4126-8916-f38622dabe2d"
platform: youtube
external_id: "c0ab8leJDrc"
canonical_url: "https://www.youtube.com/watch?v=c0ab8leJDrc"
channel: "Omatsola Dev"
captured_at: 2026-08-26
status: enriched
triage: null
tags: ["spec-driven-development", "context-management", "claude-code", "mcp", "system-design", "prompt-engineering"]
applicability:
  saas_pessoal: alta
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
content_type: whisper
---

# Como Engenheiros Sênior Constroem com IA: Spec-Driven Development e MCPs

🔗 https://www.youtube.com/watch?v=c0ab8leJDrc

## Resumo

Desenvolver projetos complexos apenas com prompts livres gera 'vibe debugging' e perda crítica de contexto nas IAs. A solução de nível sênior é o Spec-Driven Development, estruturando a arquitetura em arquivos de contexto persistentes antes da codificação. Combinado ao uso de MCPs para integrar ferramentas de design ao Claude Code, o desenvolvedor atua como arquiteto enquanto a IA executa a implementação.

## Tópicos

- **Spec-Driven Development e o Sistema de 6 Arquivos** — Define a arquitetura em 6 arquivos base (PRD, Tech Stack, Rules, Implementation Plan, Architecture e Progress) para guiar o agente e manter o contexto vivo mesmo após compactações de memória.
- **Integração de Design via MCP** — Demonstra a conexão do Claude Code com ferramentas de UI (Google Stitch e Figma) via Model Context Protocol (MCP) para transformar telas diretamente em código no editor.
- **Agentes de Código Locais e Gratuitos** — Apresenta uma alternativa open source e offline para desenvolvimento assistido por IA combinando Ollama e OpenCode com modelos locais.

## Ferramentas citadas

- **Claude Code**: Agente de codificação via terminal usado para ler o contexto dos arquivos markdown e orquestrar MCPs.
- **Google Stitch**: Ferramenta de geração de UI conectada ao Claude Code via MCP para exportar layouts.
- **Figma**: Ferramenta de design de interfaces usada para validar componentes e integrar via MCP.
- **InsForge**: Plataforma all-in-one de backend assistida por IA para banco de dados, auth e APIs.
- **Next.js**: Framework full-stack React selecionado para a camada de front-end.
- **shadcn/ui**: Biblioteca de componentes de interface utilizada na estilização com Tailwind CSS.
- **Ollama**: Runtime local para execução de modelos abertos de LLM na máquina do desenvolvedor.
- **OpenCode**: Interface e agente de código gratuito integrado a modelos locais.

## Pontos-chave

- A IA perde o contexto com facilidade em projetos longos (auto-compactação); a solução é manter a verdade do projeto gravada em arquivos markdown estruturados.
- O arquivo progress.md deve ser atualizado pelo agente a cada etapa concluída para garantir continuidade fluida entre sessões.
- O papel do desenvolvedor moderno é o de arquiteto de sistemas, definindo regras rígidas de negócio e limites técnicos antes de delegar a implementação para o modelo.
- Servidores MCP eliminam o processo manual de copiar e colar prints ou CSS de ferramentas de UI para o agente de código.

## Como aplicar

Padronizar nos repositórios do SaaS e do cliente a estrutura de 6 arquivos (especialmente PRD.md, rules.md e progress.md) na raiz, instruindo o Claude Code a ler esses arquivos no início de cada sessão e atualizar o progresso antes de encerrar.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
