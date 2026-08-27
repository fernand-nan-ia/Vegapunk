---
item_id: "9e277440-b9d0-4193-853c-f9cabd6edac2"
platform: article
external_id: "19c7c0a3eaa2"
canonical_url: "https://docs.claude.com/en/docs/claude-code/overview"
channel: "Claude Code Docs"
captured_at: 2026-08-27
status: applied_saas
triage: apply_saas
tags: ["claude-code", "agentic-coding", "mcp", "cli-automation", "subagents", "claude-md", "developer-tools", "ci-cd"]
applicability:
  saas_pessoal: alta
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
content_type: article
---

# Visão Geral do Claude Code: Instalação, Recursos e Automação Agêntica

🔗 https://docs.claude.com/en/docs/claude-code/overview

## Resumo

O Claude Code é uma ferramenta de codificação agêntica projetada para operar diretamente sobre bases de código em múltiplos ambientes, incluindo Terminal, IDEs (VS Code, JetBrains), Desktop e Web. A instalação nativa atualiza automaticamente e oferece suporte a múltiplos sistemas operacionais, utilizando chaves de API da Anthropic ou provedores de terceiros. A ferramenta automatiza tarefas repetitivas como testes, correção de lint, resolução de conflitos de merge e criação de commits e pull requests. Com o Model Context Protocol (MCP), é possível conectar fontes de dados externas como Jira, Slack e Google Drive aos fluxos de desenvolvimento. A personalização do comportamento é gerenciada via arquivos CLAUDE.md, memória automática entre sessões, criação de skills customizadas e execução de hooks antes ou depois de ações. O sistema também suporta paralelização de agentes gerenciados por um agente líder, além de um Agent SDK para fluxos complexos. Para automação contínua, rotinas agendadas na nuvem e tarefas locais permitem monitoramento e auditorias sem intervenção manual ativa. Por fim, comandos como /desktop e teleport facilitam a transição contínua de sessões entre terminal, desktop e dispositivos móveis.

## Tópicos

- **Superfícies e Instalação** — Disponível via Terminal, VS Code, JetBrains, Desktop e Web, com suporte a instaladores nativos e integração de chaves de API.
- **Automação e Desenvolvimento** — Executa testes, corrige bugs, resolve conflitos de merge e gera commits e pull requests integrados ao Git e CI/CD.
- **Integração com MCP** — Usa o Model Context Protocol para conectar ferramentas externas como Google Drive, Jira e Slack diretamente ao agente.
- **Personalização com CLAUDE.md, Skills e Hooks** — Configuração persistente via markdown, memória entre sessões, comandos customizados e gatilhos shell antes ou depois de ações.
- **Orquestração de Agentes e SDK** — Execução paralela de subagentes coordenados por um agente líder e criação de fluxos customizados via Agent SDK.
- **Agendamento e Mobilidade de Sessões** — Suporte a rotinas na nuvem, loops no CLI e migração de contexto entre terminal, mobile e desktop via teleport.

## Ferramentas citadas

- **Claude Code**: Ferramenta principal de codificação agêntica em terminal, IDEs e desktop.
- **Model Context Protocol (MCP)**: Padrão aberto para conectar dados externos e ferramentas ao agente.
- **Git**: Controle de versão integrado para criação de commits, branches e pull requests.
- **GitHub Actions**: Integração de CI/CD para automação de code review e triagem de issues.
- **GitLab CI/CD**: Automação de fluxos agênticos em pipelines de integração contínua.
- **VS Code**: IDE com suporte à extensão dedicada do Claude Code.
- **JetBrains**: Suíte de IDEs com suporte ao Claude Code e provedores terceiros.
- **Slack**: Plataforma de comunicação com menção direta ao bot para geração de PRs.
- **Jira**: Gerenciamento de tarefas integrado via servidores MCP.
- **Google Drive**: Acesso a documentos de design integrado via MCP.

## Pontos-chave

- Instalações nativas do Claude Code contam com atualizações automáticas em segundo plano.
- O arquivo CLAUDE.md na raiz define padrões de código, decisões arquiteturais e checklists de revisão lidos a cada sessão.
- Hooks permitem disparar comandos de shell automáticos antes ou depois de alterações em arquivos ou commits.
- O Model Context Protocol (MCP) conecta repositórios a serviços externos como Jira, Slack e Google Drive.
- O Agent SDK oferece controle programático total para orquestração de subagentes e gerenciamento de ferramentas.
- Rotinas em nuvem executam tarefas recorrentes (ex.: auditoria de dependências) mesmo com a máquina desligada.
- O comando 'claude --teleport' transfere sessões de longa duração da web/mobile diretamente para o terminal local.
- O comando '/desktop' transfere a sessão do terminal para o aplicativo Desktop para inspeção visual de diffs.

## Como aplicar

Configurar rotinas em nuvem e hooks no CLAUDE.md para formatar código e rodar testes antes de commits no SaaS e no site do cliente. Utilizar o comando /desktop para revisar visualmente diffs mais densos antes de aprovar PRs.

## 🍩 York diz

Se esse tal de Claude Code trabalha enquanto o meu computador tá desligado via rotinas na nuvem, isso significa mais tempo livre pra comer rosquinhas na cama! Deixa ele resolvendo conflito de merge e escrevendo teste chato enquanto a gente só recolhe o dinheiro do SaaS. Só não esquece de vigiar os custos de API, porque cada token jogado fora é um lanche a menos na mesa, Fernando.

## Texto integral

<!-- extraído da página; artigos são guardados por inteiro (títulos rebaixados um nível) -->

### Get started

Claude Code runs on several surfaces: the terminal, IDE extensions, a desktop app, and the web. Choose one from the tabs below to get started. Most surfaces require a Claude subscription or Anthropic Console account. The Terminal CLI, VS Code, and JetBrains also support third-party providers.
- Terminal
- VS Code
- Desktop app
- Web
- JetBrains

The full-featured CLI for working with Claude Code directly in your terminal. Edit files, run commands, and manage your entire project from the command line.To install Claude Code, use one of the following methods:If you see You can also install with apt, dnf, or apk on Debian, Fedora, RHEL, and Alpine.Then start Claude Code in any project. Replace You’ll be prompted to log in on first use. If you’ve set the 

- Native Install (Recommended)
- Homebrew
- WinGet

**macOS, Linux, WSL:**

**Windows PowerShell:**

**Windows CMD:**

`The token '&&' is not a valid statement separator`, you’re in PowerShell, not CMD. If you see `'irm' is not recognized as an internal or external command`, you’re in CMD, not PowerShell. Your prompt shows `PS C:\` when you’re in PowerShell and `C:\` without the `PS` when you’re in CMD.If the install command fails with `syntax error near unexpected token '<'`, a `403`, or another curl error, see Troubleshoot installation to match the error to a fix and for alternative install methods.Git for Windows is recommended on native Windows so Claude Code can use the Bash tool. If Git for Windows is not installed, Claude Code uses PowerShell as the shell tool instead. WSL setups do not need Git for Windows.
Native installations automatically update in the background to keep you on the latest version.

`your-project` with the path to a project directory on your machine:`ANTHROPIC_API_KEY` environment variable, Claude Code skips the login prompt and asks you to approve the key instead. That’s it! Continue with the Quickstart →
### What you can do

Here are some of the ways you can use Claude Code:
### Automate the work you keep putting off


Automate the work you keep putting off

Claude Code handles the tedious tasks that eat up your day: writing tests for untested code, fixing lint errors across a project, resolving merge conflicts, updating dependencies, and writing release notes.

### Build features and fix bugs


Build features and fix bugs

Describe what you want in plain language. Claude Code plans the approach, writes the code across multiple files, and verifies it works.For bugs, paste an error message or describe the symptom. Claude Code traces the issue through your codebase, identifies the root cause, and implements a fix. See common workflows for more examples.

### Create commits and pull requests


Create commits and pull requests

Claude Code works directly with git. It stages changes, writes commit messages, creates branches, and opens pull requests.In CI, you can automate code review and issue triage with GitHub Actions or GitLab CI/CD.

### Connect your tools with MCP


Connect your tools with MCP

The Model Context Protocol (MCP) is an open standard for connecting AI tools to external data sources. With MCP, Claude Code can read your design docs in Google Drive, update tickets in Jira, pull data from Slack, or use your own custom tooling. The MCP quickstart connects your first server end to end.

### Customize with instructions, skills, and hooks


Customize with instructions, skills, and hooks

`CLAUDE.md` is a markdown file you add to your project root that Claude Code reads at the start of every session. Use it to set coding standards, architecture decisions, preferred libraries, and review checklists. Claude also builds auto memory as it works, saving learnings across sessions without you writing anything.Create skills to package repeatable workflows your team can share, like `/review-pr` or `/deploy-staging`.Hooks let you run shell commands before or after Claude Code actions, like auto-formatting after every file edit or running lint before a commit.
### Run agents in parallel and build custom agents


Run agents in parallel and build custom agents

Spawn multiple Claude Code agents that work on different parts of a task simultaneously. A lead agent coordinates the work, assigns subtasks, and merges results.To run several full sessions in parallel and watch them from one screen, use background agents. For fully custom workflows, the Agent SDK lets you build your own agents powered by Claude Code’s tools and capabilities, with full control over orchestration, tool access, and permissions.

### Pipe, script, and automate with the CLI


Pipe, script, and automate with the CLI

Claude Code is composable and follows the Unix philosophy. Pipe logs into it, run it in CI, or chain it with other tools:See the CLI reference for the full set of commands and flags.

### Schedule recurring tasks


Schedule recurring tasks

Run Claude on a schedule to automate work that repeats: morning PR reviews, overnight CI failure analysis, weekly dependency audits, or syncing docs after PRs merge.

- Routines run in the cloud, so they keep running even when your computer is off. They can also trigger on API calls or GitHub events. Create them from the web, the Desktop app, or by running `/schedule` in the CLI.
- Desktop scheduled tasks run on your machine, with direct access to your local files and tools
- `/loop` repeats a prompt within a CLI session for quick polling

### Work from anywhere


Work from anywhere

Sessions aren’t tied to a single surface. Move work between them as your context changes:

- Step away from your desk and keep working from your phone or any browser with Remote Control
- Message Dispatch a task from your phone and open the Desktop session it creates
- Kick off a long-running task on the web or the Claude mobile app, then pull it into your terminal with `claude --teleport` . Teleport requires a claude.ai subscription.
- Run `/desktop` to continue your current terminal session in the Desktop app, where you can review diffs visually. The`/desktop` handoff requires a claude.ai subscription. Available on macOS and x64 Windows.
- Route tasks from team chat: mention `@Claude` in Slack with a bug report and get a pull request back

### Use Claude Code everywhere

Each surface connects to the same underlying Claude Code engine, so your repo’s CLAUDE.md files, settings, and MCP servers work across all of them. Beyond the Terminal, VS Code, JetBrains, Desktop, and Web surfaces above, Claude Code integrates with CI/CD, chat, and browser workflows:
### Next steps

Once you’ve installed Claude Code, these guides help you go deeper.
- Quickstart: walk through your first real task, from exploring a codebase to committing a fix
- Store instructions and memories: give Claude persistent instructions with CLAUDE.md files and auto memory
- Common workflows and best practices: patterns for getting the most out of Claude Code
- A harness for every task: how the Claude Code team uses dynamic workflows to orchestrate subagents at scale
- Settings: customize Claude Code for your workflow
- Troubleshooting: solutions for common issues
- code.claude.com: demos, pricing, and product details

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
