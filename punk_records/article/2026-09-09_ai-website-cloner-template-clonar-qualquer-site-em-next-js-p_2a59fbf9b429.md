---
item_id: "4953dc6f-a380-41c9-9e68-f5d963f0e519"
platform: article
external_id: "2a59fbf9b429"
canonical_url: "https://github.com/JCodesMore/ai-website-cloner-template"
channel: "JCodesMore"
captured_at: 2026-09-09
status: applied_client
triage: apply_client
tags: ["clone-de-site", "nextjs-16", "claude-code-skill", "browser-mcp", "git-worktree", "engenharia-reversa-de-ui", "demo-antes-do-contato", "licenca-mit"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: manual
---

# AI Website Cloner Template — clonar qualquer site em Next.js por um comando

🔗 https://github.com/JCodesMore/ai-website-cloner-template

## Resumo

Template MIT que entrega um projeto Next.js 16 já montado (App Router, React 19, TypeScript strict, shadcn/ui, Tailwind v4 com tokens oklch) mais uma skill `/clone-website` que reconstrói o site alvo dentro dele. O fluxo tem cinco fases: reconhecimento com capturas e extração de tokens de design, fundação (fontes, cores, CSS global e download de todos os ativos), escrita de specs por componente com valores exatos de `getComputedStyle()`, construção paralela por agentes despachados em worktrees do git, e por fim montagem com diff visual contra o original. A skill exige automação de navegador — Chrome MCP, Playwright MCP, Browserbase ou Puppeteer — e não funciona sem isso; o README recomenda Claude Code com Opus 5 e o comando `claude --chrome`. O padrão é emulação pixel-perfect sem customização, com conteúdo e ativos reais do alvo, e a skill preserva rotas e isola pastas por site e por página quando se clona mais de uma URL. O README delimita o uso: serve para migração de plataforma, recuperação de site cujo código-fonte se perdeu e estudo, e proíbe phishing, personificação, apropriação de marca e violação de termos de serviço. Doze plataformas de agente são suportadas por arquivos gerados a partir de duas fontes da verdade (`AGENTS.md` e o `SKILL.md`), sincronizadas por dois scripts. Existe um caminho opcional que gera imagem por IA via API paga da Atlas Cloud, patrocinadora do repositório, restrito a ativo irrecuperável, nunca a logo ou marca, e só com aprovação explícita do usuário.

## Tópicos

- **Pipeline de cinco fases** — Reconhecimento, fundação, specs de componente, construção paralela em worktrees e montagem com diff visual contra o original.
- **Exigência de navegador** — Sem Chrome MCP, Playwright MCP, Browserbase ou Puppeteer a skill não roda; o README indica `claude --chrome`.
- **Spec como contrato** — Cada componente ganha um arquivo de especificação com CSS computado, estados e comportamento antes de qualquer agente construtor ser despachado; o arquivo fica auditável.
- **Modelo de interação antes do código** — O guia insiste em determinar se a seção é dirigida por scroll, clique, hover ou tempo antes de construir — errar isso obriga reescrita completa.
- **Isolamento por site e por página** — Chaves com hash SHA-256 para origem e pathname evitam que um clone sobrescreva o outro; rotas existentes nunca são apagadas sem aprovação.
- **Limites de uso declarados** — Migração, recuperação de código perdido e estudo são os usos previstos; phishing, personificação e violação de ToS são proibidos no próprio README.
- **Caminho patrocinado opcional** — Fallback de geração de imagem pela API paga da Atlas Cloud, patrocinadora do repo, com `ATLASCLOUD_API_KEY` — exceção, nunca padrão, e vedado para logo ou marca.

## Ferramentas citadas

- **Next.js 16**: base do projeto gerado — App Router, React 19, TypeScript strict
- **shadcn/ui + Tailwind CSS v4**: camada de UI e tokens de design em oklch
- **Chrome MCP / Playwright MCP**: automação de navegador obrigatória para inspecionar e medir o site alvo
- **git worktree**: isolamento dos agentes construtores que trabalham em paralelo
- **Atlas Cloud**: API paga de geração de imagem, patrocinadora, usada só como último recurso para ativo irrecuperável
- **Docker**: docker compose para rodar o app em produção ou em modo dev na porta 3001

## Pontos-chave

- Licença MIT, repositório marcado como template — o README pede para usar 'Use this template', não clonar direto.
- 34.114 estrelas e 4.973 forks conferidos na API do GitHub em 09/09/2026; criado em 13/03/2026.
- Só 13 contribuidores, 2 issues e 2 PRs abertos, último release v0.4.0 em 10/08/2026 — projeto viral com manutenção concentrada em uma pessoa.
- A saída é projeto Next.js/React/Tailwind, não HTML estático — não serve para extrair o HTML de uma página.
- Sem MCP de navegador a skill não executa; é o pré-requisito que trava a maioria das instalações.
- `npm audit` no clone de 09/09 acusou 10 vulnerabilidades, uma crítica no próprio Next.js 16.3 (RCE em servidor Windows e na API de otimização de imagem com AVIF).
- A política de segurança avisa que projetos criados a partir do template NÃO recebem correções automáticas.
- O bloco `nextjs-agent-rules` do AGENTS.md é reescrito pelo próprio `next dev` — mexer nele reaparece como alteração não commitada.
- Doze plataformas de agente suportadas por arquivos gerados; editar a fonte exige rodar os scripts de sincronização.
- Nenhuma chamada de rede ou telemetria encontrada em `scripts/` e `src/` na inspeção local.

## Como aplicar

É a ferramenta que materializa a tática de demo pronta antes do primeiro contato, que apareceu em quatro conteúdos independentes no vault em 09/09. Instalado em /home/crazu/projetos/ai-website-cloner-template com build verde, faltando só o MCP de navegador. Para o caso VDC, serve para reconstruir o site atual do cliente e comparar com a landing que a Taste Skill produziu — mas a saída em React não substitui o HTML da pasta testes-skills-design, e o site gerado não deve ir para produção sem `npm audit fix` por causa do RCE crítico do Next.js 16.3.

## 📚 Pythagoras diz

O registro diz o seguinte: 34.114 estrelas, treze contribuidores, duas issues abertas. Eu deduzo que a popularidade veio da vitrine e a manutenção ficou com uma pessoa só — o que não invalida o código, mas define quem conserta quando quebrar: você. Anoto também que o README proíbe explicitamente personificação e apropriação de marca, e que o patrocinador está escrito dentro das instruções do agente. Nada disso é armadilha; é só informação que precisa ficar junto da ferramenta.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
