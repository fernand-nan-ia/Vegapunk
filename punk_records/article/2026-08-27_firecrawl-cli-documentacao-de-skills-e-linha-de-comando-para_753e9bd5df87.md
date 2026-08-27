---
item_id: "70285b24-9156-4ca0-9cef-914e2e3a740e"
platform: article
external_id: "753e9bd5df87"
canonical_url: "https://docs.firecrawl.dev/sdks/cli"
channel: "Firecrawl Docs"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["firecrawl", "web-scraping", "claude-code", "cli", "ai-agents", "crawling", "developer-tools"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: alta
confidence: alta
theme: ia-e-agentes
content_type: article
---

# Firecrawl CLI: Documentação de Skills e Linha de Comando para Agentes de IA

🔗 https://docs.firecrawl.dev/sdks/cli

## Resumo

A documentação oficial da CLI do Firecrawl detalha sua integração com agentes de IA, como Claude Code e Cursor, por meio de skills modulares de CLI, build e workflows. A ferramenta permite que agentes realizem raspagem de páginas, mapeamento de domínios e rastreamento completo com saída otimizada para contexto em Markdown ou JSON. A autenticação aceita uso gratuito sem chave com limite por IP, chaves de nuvem com créditos gratuitos ou instâncias auto-hospedadas apontadas via variável de ambiente. Dentre os recursos, destaca-se o comando interact, que substitui o navegador tradicional por sessões interativas em linguagem natural sobre páginas raspadas. A CLI também introduz o comando developer para buscas em repositórios, pull requests e documentações, além do comando monitor para detectar alterações entre snapshots com base em objetivos semânticos. Os dados são emitidos diretamente no stdout para fácil encadeamento em pipelines Unix, com opções explícitas para desativação de telemetria.

## Tópicos

- **Instalação e Integração com Agentes** — Instalação automática de skills para agentes de código detectados, cobrindo módulos de CLI, build e fluxos de trabalho.
- **Autenticação e Ambientes Self-Hosted** — Modos de acesso via camada gratuita sem chave, API key com cota de créditos ou conexão direta a deploys locais via FIRECRAWL_API_URL.
- **Comandos de Extração e Mapeamento** — Operações de scrape para URL única, crawl completo, busca na web e map para descoberta rápida da árvore de links de um domínio.
- **Interação e Monitoramento Contínuo** — Uso de sessões interativas em linguagem natural via interact e agendamento de scrapes comparativos via monitor com diffing semântico.
- **Índice de Desenvolvedores e Pesquisa Autônoma** — Busca focada em código e PRs com o comando developer e execução de pesquisas web orientadas a metas com o comando agent.

## Ferramentas citadas

- **Firecrawl CLI**: Interface de linha de comando para raspagem, crawling, busca e interação com dados web estruturados para agentes.
- **Claude Code**: Agente de codificação no terminal suportado nativamente pelas skills da CLI do Firecrawl.

## Pontos-chave

- A CLI possui suporte nativo para integração direta de skills em agentes como Claude Code e Cursor.
- Comandos básicos funcionam sem API key em plano gratuito limitado por IP, com opção de upgrade para 1.000 créditos gratuitos.
- Deploys self-hosted são suportados apontando FIRECRAWL_API_URL, ignorando a autenticação de nuvem em redes confiáveis.
- O comando depreciado browser foi substituído pelo fluxo de scrape seguido de interact para economia de contexto.
- O comando developer realiza consultas especializadas em issues, PRs mesclados, READMEs e documentações selecionadas.
- O comando monitor permite rastrear alterações em páginas comparando snapshots com critérios semânticos.
- Saída padrão em stdout permite piping direto: formatos únicos geram texto bruto/markdown, enquanto múltiplos formatos geram JSON consolidado.
- Telemetria anônima coleta apenas metadados de versão/ambiente e pode ser totalmente desativada via variável de ambiente.

## Como aplicar

Instalar a skill do Firecrawl no ambiente do Claude Code para permitir que o agente busque documentações atualizadas via 'firecrawl developer' e faça ingestão automatizada de dados da web para enriquecer o SaaS.

## 📚 Pythagoras diz

O registro documenta de forma precisa a arquitetura de comandos da CLI do Firecrawl, desenhada especificamente para economizar contexto em agentes autônomos. Eu deduzo que a substituição de instâncias de browser pelo comando interact com saída direta em Markdown traz ganhos substanciais de velocidade e custo de tokens. Recomendo registrar e instalar as skills no seu Claude Code para automatizar buscas em documentações técnicas.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Installation

If you are using an AI agent like Claude Code, you can install the Firecrawl skills below and the agent will set them up for you.
- `--all` installs every Firecrawl skill segment (CLI, build, workflows) to every detected AI coding agent
- `--browser` opens the browser for Firecrawl authentication automatically

After installing the skills, restart your agent for it to discover them.

CLI

### Authentication

Before using the CLI, you need to authenticate with your Firecrawl API key.
**Some CLI commands work without logging in.**With no API key configured, supported commands fall back to the keyless free tier — free, but rate-limited per IP. See Rate Limits for the current keyless command list and caveats. Sign up for a free key for 1,000 credits and higher limits; the CLI uses it automatically once configured.

#### Login

CLI

#### View Configuration

CLI

#### Logout

CLI

#### Connect the CLI to self-hosted Firecrawl

First, get one scrape working with the self-hosting guide. Then point the CLI at that API with`--api-url` or `FIRECRAWL_API_URL`:
CLI

`https://api.firecrawl.dev`, the CLI skips Firecrawl Cloud API-key authentication. That matches the trusted-network quickstart, where `USE_DB_AUTHENTICATION=false`.
The CLI can call only the capabilities enabled in your deployment. Check self-hosted feature support before using Cloud-only or provider-dependent commands.
#### Check Status

Verify installation, authentication, and view rate limits:
CLI

- **Concurrency** : Maximum parallel jobs. Run parallel operations close to this limit but not above.
- **Credits** : Remaining API credits. Each scrape/crawl consumes credits.

### Commands

The hidden 

`firecrawl browser` command is deprecated for agent workflows. Use `firecrawl scrape <url>` first, then `firecrawl interact ...` with the resulting scrape session.
#### Scrape

Scrape a single URL and extract its content in various formats.
CLI

##### Output Formats

CLI

##### Scrape Options

CLI

**Available Options:**

#### Search

Search the web and optionally scrape the results.
CLI

##### Search Options

CLI

**Available Options:**

#### Developer

Search the Developer Index — issues, merged pull requests, and READMEs from public code repositories, alongside curated documentation sites.
CLI

**Available Options:**

#### Map

Discover all URLs on a website quickly.
CLI

##### Map Options

CLI

**Available Options:**

#### Interact

Scrape a page, then interact with it using natural language or code. Interact uses the most recent scrape by default, or you can pass a specific scrape ID.
CLI

**Available Options:**

#### Crawl

Crawl an entire website starting from a URL.
CLI

##### Check Crawl Status

CLI

##### Crawl Options

CLI

**Available Options:**

#### Monitor

Create recurring scrapes or crawls that diff each run against the previous snapshot. Add a goal when you want Firecrawl to judge which changed pages are meaningful for your use case.
CLI

**Available Options:**

#### Agent

Search and gather data from the web using natural language prompts.
CLI

##### Agent Options

CLI

**Available Options:**

#### Credit Usage

Check your team’s credit balance and usage.
CLI

#### Version

Display the CLI version.
CLI

### Global Options

These options are available for all commands:
### Output Handling

The CLI outputs to stdout by default, making it easy to pipe or redirect:
CLI

#### Format Behavior

- **Single format** : Outputs raw content (markdown text, HTML, etc.)
- **Multiple formats** : Outputs JSON with all requested data

CLI

### Examples

#### Quick Scrape

CLI

#### Full Site Crawl

CLI

#### Site Discovery

CLI

#### Research Workflow

CLI

#### Agent

CLI

#### Combine with Other Tools

CLI

### Telemetry

The CLI collects anonymous usage data during authentication to help improve the product:
- CLI version, OS, and Node.js version
- Development tool detection (e.g., Cursor, VS Code, Claude Code)

**No command data, URLs, or file contents are collected via the CLI.**To disable telemetry, set the environment variable:

CLI

### Open Source

The Firecrawl CLI and all three skill segments are open source on GitHub:
- `firecrawl/cli` — the CLI and CLI skills (live web work)
- `firecrawl/skills` — build skills (integrate Firecrawl into application code)
- `firecrawl/firecrawl-workflows` — workflow skills (repeatable deliverables such as research briefs, SEO audits, lead lists, and design clones)

Are you an AI agent that needs a Firecrawl API key? See firecrawl.dev/agent-onboarding/SKILL.md for automated onboarding instructions.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
