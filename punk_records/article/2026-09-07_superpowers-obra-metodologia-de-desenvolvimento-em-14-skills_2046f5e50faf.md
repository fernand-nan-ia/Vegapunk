---
item_id: "c76fd54e-5263-41df-9629-e2a70fa9ba5e"
platform: article
external_id: "2046f5e50faf"
canonical_url: "https://github.com/obra/superpowers"
channel: "Obra · GitHub"
captured_at: 2026-09-07
status: applied_saas
triage: apply_saas
tags: ["superpowers", "agent-skills", "tdd", "spec-driven", "subagentes", "git-worktrees", "claude-code", "metodologia"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: alta
confidence: alta
theme: ia-e-agentes
content_type: article
---

# Superpowers (obra): metodologia de desenvolvimento em 14 skills para agentes de código

🔗 https://github.com/obra/superpowers

## Resumo

Superpowers é uma metodologia completa de desenvolvimento de software empacotada como plugin para agentes de código, criada por Jesse Vincent e a equipe da Prime Radiant. A premissa é que o agente NÃO deve começar escrevendo código: ao perceber que você está construindo algo, ele recua e pergunta o que você realmente quer, extrai uma especificação da conversa e a mostra em pedaços curtos o suficiente para serem lidos. Aprovado o desenho, produz um plano de implementação explicitamente calibrado para 'um engenheiro júnior entusiasmado, sem bom gosto, sem julgamento, sem contexto do projeto e com aversão a testes' — cada tarefa de 2 a 5 minutos, com caminho de arquivo exato, código completo e passos de verificação. A execução usa subagente novo por tarefa, com revisão em dois estágios (primeiro conformidade com a especificação, depois qualidade do código), e os autores afirmam que não é raro o agente trabalhar sozinho por algumas horas sem sair do plano. O TDD é obrigatório e literal: escreve o teste, VÊ falhar, escreve o mínimo, vê passar, commita — e a skill APAGA código escrito antes do teste. As 14 skills se dividem em testes, depuração, colaboração e meta. A frase que define a postura do projeto está no próprio README: 'fluxos obrigatórios, não sugestões'. Instala-se pelo marketplace oficial da Anthropic (`/plugin install superpowers@claude-plugins-official`) e também nos marketplaces oficiais de Codex, Grok e Kimi, além de Cursor, Gemini, Devin, Copilot e outros — cada harness exige instalação separada. Há oferta de suporte comercial e telemetria ligada por padrão.

## Tópicos

- **A inversão central** — O agente não começa por código: recua, pergunta o que se quer de fato, extrai a especificação da conversa e a apresenta em pedaços curtos para validação.
- **Plano para um júnior sem julgamento** — O plano é calibrado para ser seguido por quem não tem contexto nem bom gosto: tarefas de 2 a 5 minutos, caminho de arquivo exato, código completo e passos de verificação. Enfatiza TDD, YAGNI e DRY.
- **Subagente por tarefa com revisão dupla** — Cada tarefa vai para um subagente novo; a revisão tem dois estágios — conformidade com a especificação, depois qualidade do código. Os autores relatam horas de trabalho autônomo sem desvio do plano.
- **TDD literal e coercitivo** — RED-GREEN-REFACTOR com o passo de VER o teste falhar antes de escrever código; a skill apaga código escrito antes do teste. Fluxos são descritos como obrigatórios, não sugestões.
- **As 14 skills por categoria** — Testes: test-driven-development. Depuração: systematic-debugging (4 fases) e verification-before-completion. Colaboração: 9 skills, de brainstorming a finishing-a-development-branch. Meta: writing-skills e using-superpowers.
- **Instalação por harness** — Marketplaces oficiais de Claude, Codex, Grok e Kimi, mais Cursor, Gemini, Devin, Copilot, Antigravity, OpenCode, Pi e Hermes. Cada harness exige instalação separada; a atualização depende do harness.
- **Governança e negócio** — Feito por Jesse Vincent e a Prime Radiant, com suporte comercial oferecido. O projeto declara que NÃO aceita contribuições de skills novas, e mudanças precisam funcionar em todos os agentes suportados.

## Ferramentas citadas

- **Claude Code**: harness principal; instalação por /plugin install superpowers@claude-plugins-official, o marketplace oficial da Anthropic
- **git worktrees**: usado pela skill using-git-worktrees para criar espaço de trabalho isolado em branch nova, com baseline de testes limpa
- **superpowers-evals**: harness de avaliação (drill) usado para testar o comportamento das próprias skills
- **Prime Radiant**: empresa por trás do projeto; oferece suporte comercial, tooling adicional e gestão de gasto para uso corporativo

## Pontos-chave

- 282.777 estrelas no GitHub e push em 04/09/2026 — projeto vivo, verificado na API em 07/09
- Instalação oficial pelo marketplace da Anthropic, não repositório solto: /plugin install superpowers@claude-plugins-official
- 14 skills; as duas que raramente aparecem em outros pacotes são systematic-debugging (4 fases) e verification-before-completion
- Tarefas do plano têm 2 a 5 minutos cada, com caminho de arquivo e código completo
- A skill de TDD APAGA código escrito antes do teste — coerção, não recomendação
- Revisão em dois estágios: conformidade com a especificação primeiro, qualidade do código depois
- Telemetria LIGADA por padrão; desativa-se com a variável de ambiente SUPERPOWERS_DISABLE_TELEMETRY
- Cada harness precisa de instalação própria, mesmo que já esteja instalado em outro
- O projeto não aceita contribuições de skills novas — a metodologia é fechada por decisão dos autores
- COLISÃO com o Vegapunk: o ciclo Edison prd → Stella story → Atlas develop → Lilith verify → Shaka gate → Stella release cobre os mesmos seis passos com outros nomes

## Como aplicar

NÃO instalar no Vegapunk: o ciclo dos Satélites já cobre os mesmos seis passos e duas metodologias ativas disputariam o comando do agente — o mesmo conflito que o item do AI slop descreve entre Impeccable e Taste Skill. O caminho aditivo é roubar as duas peças que nos faltam, `systematic-debugging` e `verification-before-completion`, e escrevê-las como tasks do Atlas e do Shaka em squads/vegapunk/tasks/. Para testar a metodologia inteira, usar um projeto novo e descartável, sem Satélites.

## 📚 Pythagoras diz

O registro aqui é de primeira mão — é o README dos autores, não a leitura de terceiros, e por isso vale mais que a lista que trouxe o assunto. Eu deduzo que o valor para nós não é o pacote e sim duas peças dele: depuração sistemática e verificação antes de declarar pronto, que o nosso ciclo não tem escritas. Anoto a lacuna com licença: ninguém mediu o que esse método custa em limite de uso do plano Max, e um subagente por tarefa não é despesa pequena.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Superpowers is a complete software development methodology for your coding agents, built on top of a set of composable skills and some initial instructions that make sure your agent uses them.

It starts from the moment you fire up your coding agent. As soon as it sees that you're building something, it *doesn't* just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do.

Once it's teased a spec out of the conversation, it shows it to you in chunks short enough to actually read and digest.

After you've signed off on the design, your agent puts together an implementation plan that's clear enough for an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing to follow. It emphasizes true red/green TDD, YAGNI (You Aren't Gonna Need It), and DRY.

Next up, once you say "go", it launches a *subagent-driven-development* process, having agents work through each engineering task, inspecting and reviewing their work, and continuing forward. It's not uncommon for your agent to work autonomously for a couple hours at a time without deviating from the plan you put together.

There's a bunch more to it, but that's the core of the system. And because the skills trigger automatically, you don't need to do anything special. Your coding agent just has Superpowers.

If you're using Superpowers in enterprise and could benefit from commercial support, additional tooling, or managed spending, please don't hesitate to drop us a line at sales@primeradiant.com.

Installation differs by harness. If you use more than one, install Superpowers separately for each one.

Superpowers is available via the official Claude plugin marketplace

- 
Install the plugin from Anthropic's official marketplace: /plugin install superpowers@claude-plugins-official

The Superpowers marketplace provides Superpowers and some other related plugins for Claude Code.

- 
Register the marketplace: /plugin marketplace add obra/superpowers-marketplace
- 
Install the plugin from this marketplace: /plugin install superpowers@superpowers-marketplace

Install Superpowers as a plugin from this repository:

`agy plugin install https://github.com/obra/superpowers`
Antigravity runs the plugin's session-start hook, so Superpowers is active from the first message. Reinstall with the same command to update.

Superpowers is available via the official Codex plugin marketplace.

- In the Codex app, click on Plugins in the sidebar.
- You should see `Superpowers` in the Coding section.
- Click the `+` next to Superpowers and follow the prompts.

Superpowers is available via the official Codex plugin marketplace.

- 
Open the plugin search interface: /plugins
- 
Search for Superpowers: superpowers
- 
Select `Install Plugin` .

- 
In Cursor Agent chat, install from marketplace: ```
/add-plugin superpowers
```
- 
Or search for "superpowers" in the plugin marketplace.

- 
Install the plugin from this repository: devin plugins install obra/superpowers
- 
Update to the latest version with: devin plugins update superpowers

- 
Register the marketplace: droid plugin marketplace add https://github.com/obra/superpowers
- 
Install the plugin: droid plugin install superpowers@superpowers

- 
Install the extension: gemini extensions install https://github.com/obra/superpowers
- 
Update later: gemini extensions update superpowers

- 
Register the marketplace: copilot plugin marketplace add obra/superpowers-marketplace
- 
Install the plugin: copilot plugin install superpowers@superpowers-marketplace

Superpowers is available via the official Grok plugin marketplace.

- 
Install the plugin from xAI's official marketplace: grok plugin install superpowers@xai-official --trust
- 
Or open the marketplace in the TUI, search for Superpowers, and install it: ```
/marketplace
```

Superpowers is available in Kimi Code's plugin marketplace.

- 
Open Kimi Code's plugin manager: ```
/plugins
```
- 
Go to `Marketplace` >`Superpowers` and install it.
- 
Or install directly from this repository: ```
/plugins install https://github.com/obra/superpowers
```
- 
Detailed docs: docs/README.kimi.md

OpenCode uses its own plugin install; install Superpowers separately even if you already use it in another harness.

- 
Tell OpenCode: ```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md
```
- 
Detailed docs: docs/README.opencode.md

Install Superpowers as a Pi package from this repository:

`pi install git:github.com/obra/superpowers`
For local development, run Pi with this checkout loaded as a temporary package:

`pi -e /path/to/superpowers`
The Pi package loads the Superpowers skills and a small extension that injects the `using-superpowers` bootstrap at session startup and again after compaction. Pi has native skills, so no compatibility `Skill` tool is required. Subagent and task-list tools remain optional Pi companion packages.

Install Superpowers as a Hermes plugin from this repository:

`hermes plugins install obra/superpowers --enable`
Restart any active Hermes sessions after installing. Note: Hermes has no post-compaction hook, so a very long session that compacts over its first turn loses the bootstrap — start a fresh session if skills stop triggering.

1. 
**brainstorming** - Activates before writing code. Refines rough ideas through questions, explores alternatives, presents design in sections for validation. Saves design document.
2. 
**using-git-worktrees** - Activates after design approval. Creates isolated workspace on new branch, runs project setup, verifies clean test baseline.
3. 
**writing-plans** - Activates with approved design. Breaks work into bite-sized tasks (2-5 minutes each). Every task has exact file paths, complete code, verification steps.
4. 
**subagent-driven-development** or**executing-plans** - Activates with plan. Dispatches fresh subagent per task with two-stage review (spec compliance, then code quality), or executes in batches with human checkpoints.
5. 
**test-driven-development** - Activates during implementation. Enforces RED-GREEN-REFACTOR: write failing test, watch it fail, write minimal code, watch it pass, commit. Deletes code written before tests.
6. 
**requesting-code-review** - Activates between tasks. Reviews against plan, reports issues by severity. Critical issues block progress.
7. 
**finishing-a-development-branch** - Activates when tasks complete. Verifies tests, presents options (merge/PR/keep/discard), cleans up worktree.

**The agent checks for relevant skills before any task.** Mandatory workflows, not suggestions.

Superpowers is built by Jesse Vincent and the rest of the folks at Prime Radiant.

- **Discord** : Join us for community support, questions, and sharing what you're building with Superpowers
- **Issues** : https://github.com/obra/superpowers/issues
- **Release announcements** : Sign up to get notified about new versions

**Testing**

- **test-driven-development** - RED-GREEN-REFACTOR cycle (includes testing anti-patterns reference)

**Debugging**

- **systematic-debugging** - 4-phase root cause process (includes root-cause-tracing, defense-in-depth, condition-based-waiting techniques)
- **verification-before-completion** - Ensure it's actually fixed

**Collaboration**

- **brainstorming** - Socratic design refinement
- **writing-plans** - Detailed implementation plans
- **executing-plans** - Batch execution with checkpoints
- **dispatching-parallel-agents** - Concurrent subagent workflows
- **requesting-code-review** - Pre-review checklist
- **receiving-code-review** - Responding to feedback
- **using-git-worktrees** - Parallel development branches
- **finishing-a-development-branch** - Merge/PR decision workflow
- **subagent-driven-development** - Fast iteration with two-stage review (spec compliance, then code quality)

**Meta**

- **writing-skills** - Create new skills following best practices (includes testing methodology)
- **using-superpowers** - Introduction to the skills system

- **Test-Driven Development** - Write tests first, always
- **Systematic over ad-hoc** - Process over guessing
- **Complexity reduction** - Simplicity as primary goal
- **Evidence over claims** - Verify before declaring success

Read the original release announcement.

The general contribution process for Superpowers is below. Keep in mind that we don't generally accept contributions of new skills and that any updates to skills must work across all of the coding agents we support.

1. Fork the repository
2. Switch to the 'dev' branch
3. Create a branch for your work
4. Follow the `writing-skills` skill for creating and testing new and modified skills
5. Submit a PR, being sure to fill in the pull request template.

Skill-behavior tests use the drill eval harness from superpowers-evals, cloned into `evals/` — see `evals/README.md` for setup. Plugin-infrastructure tests live at `tests/` and run via the relevant `run-*.sh` or `npm test`.

See `skills/writing-skills/SKILL.md` for the complete guide.

Superpowers updates are somewhat coding-agent dependent, but are often automatic.

MIT License - see LICENSE file for details

Because skills and plugins don't provide any feedback to creators, we have no idea how many of you are using Superpowers. By default, the Prime Radiant logo on brainstorming's optional visual companion feature is loaded from our website. It includes the version of Superpowers in use. It does not include any details about your project, prompt, or coding agent. We don't see your clicks or anything about what you're building. This helps us have a rough idea of how many folks are using Superpowers and which version of Superpowers they're using. It's 100% optional. To disable this, set the environment variable `SUPERPOWERS_DISABLE_TELEMETRY` to any true value. Superpowers also honors Claude Code's `DISABLE_TELEMETRY` and `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` opt-outs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
