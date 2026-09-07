---
item_id: "85a14bda-caef-44df-aeb3-a4ec8cf2854a"
platform: article
external_id: "3429c7218e4f"
canonical_url: "https://github.com/affaan-m/ECC"
channel: "Affaan-M · GitHub"
captured_at: 2026-09-07
status: enriched
triage: null
tags: ["ecc", "agent-harness", "agent-skills", "agentshield", "seguranca-de-agente", "claude-code", "colisao-de-metodologia"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: baixa
  estudo_geral: media
confidence: alta
theme: ia-e-agentes
content_type: article
---

# ECC (Everything Claude Code): 68 agentes, 286 skills e um sistema de engenharia inteiro

🔗 https://github.com/affaan-m/ECC

## Resumo

ECC se descreve como um sistema de otimização de desempenho para harness de agente: em vez de o agente apenas escrever código, recebe um processo de engenharia coordenado que planeja antes de construir, verifica com testes, revisa o próprio trabalho a partir de contexto novo, lembra o que importa e transforma acertos repetidos em skills reutilizáveis. O ciclo declarado é planejar → testar → implementar → revisar → verificar → lembrar → melhorar. A escala é o traço definidor e o principal risco: 68 agentes especializados, 286 skills, 94 comandos legados, mais hooks, regras selecionáveis por linguagem, memória, aprendizado contínuo e um scanner de segurança próprio chamado AgentShield, que examina prompts, hooks, configuração de MCP, permissões, segredos e arquivos de agente. É MIT e mantido por uma pessoa só, publicando semanalmente para sete harnesses; a sustentação vem de patrocínio e de um produto pago, o ECC Pro, um app do GitHub para repositórios privados a partir de 19 dólares por assento ao mês. O README traz dois avisos operacionais fortes. O primeiro é de procedência: instalar apenas dos canais verificados, porque re-uploads de terceiros não são revisados e podem conter malware. O segundo é de instalação: NÃO empilhar métodos — instalar duas vezes no mesmo harness duplica skills, comandos, hooks e configuração, e a documentação lista explicitamente as combinações a evitar. Exige Node 18 ou mais novo e Claude Code 2.1 ou mais novo. Funciona melhor no Claude Code, tem caminho suportado para Codex e adaptadores de capacidade limitada para Cursor, OpenCode, Gemini, Zed, Copilot, Antigravity e Qwen. Há README em português do Brasil.

## Tópicos

- **O ciclo que ele impõe** — planejar → testar → implementar → revisar → verificar → lembrar → melhorar, instalado uma vez em vez de reconstruído a cada prompt.
- **A escala** — 68 agentes, 286 skills, 94 comandos legados, mais hooks, regras por linguagem, memória e aprendizado contínuo — o maior pacote de tudo o que foi analisado.
- **AgentShield** — Scanner de segurança incluído que examina prompts, hooks, configuração de MCP, permissões, segredos e arquivos de agente — a peça mais incomum do pacote.
- **Aviso de procedência** — O README alerta para instalar SOMENTE de canais verificados (repo oficial, npm ecc-universal e ecc-agentshield, app do GitHub, slug ecc@ecc, site ecc.tools); re-uploads de terceiros podem conter malware.
- **Não empilhar instalações** — Instalar duas vezes no mesmo harness duplica skills, comandos, hooks e configuração. A documentação lista as combinações que funcionam e as que devem ser evitadas.
- **Modelo de negócio** — MIT para sempre no repositório aberto; ECC Pro é o app hospedado do GitHub para repositórios privados, a partir de 19 dólares por assento ao mês, e sustenta um mantenedor único publicando semanalmente.
- **Requisitos e alcance** — Node 18+ e Claude Code 2.1+. Melhor no Claude Code, caminho suportado no Codex, adaptadores limitados em Cursor, OpenCode, Gemini, Zed, Copilot, Antigravity e Qwen. README em português do Brasil.

## Ferramentas citadas

- **ecc-universal**: pacote npm com o instalador guiado (npx ecc-universal setup)
- **AgentShield**: scanner de segurança do pacote; varre prompts, hooks, configuração de MCP, permissões, segredos e arquivos de agente
- **Claude Code**: harness principal; instalação por marketplace (/plugin marketplace add) ou pelo instalador guiado
- **ECC Pro**: app pago do GitHub para repositórios privados, a partir de US$ 19 por assento ao mês

## Pontos-chave

- 252.599 estrelas e 37.899 forks, MIT, push em 07/09/2026 — verificado na API no mesmo dia
- 68 agentes, 286 skills e 94 comandos: é o pacote mais pesado de tudo o que foi avaliado
- COLISÃO TOTAL com o Vegapunk: 68 agentes por cima dos 7 Satélites disputariam a mesma função
- Mantido por UMA pessoa publicando semanalmente para sete harnesses — risco de barramento concentrado
- O próprio README alerta que cópias de terceiros podem conter malware: instalar só de canal verificado
- Empilhar métodos de instalação duplica skills, hooks e configuração — erro comum e explicitamente documentado
- AgentShield é a peça mais original: varre segredos, permissões e configuração de MCP
- Exige Node 18+ e Claude Code 2.1+
- MIT no aberto, mas com produto pago para repositório privado (US$ 19/assento/mês)
- Tem README em português do Brasil

## Como aplicar

Não instalar aqui: 68 agentes e 286 skills por cima dos 7 Satélites é a maior colisão possível de metodologia — o mesmo problema do superpowers, multiplicado por dez. A única peça que valeria estudar isolada é o AgentShield, porque varre segredo, permissão e configuração de MCP, e essa checagem não existe no nosso fluxo hoje; o gate do Shaka confere segredo por git grep, que é menos completo. Se um dia for testado, tem de ser em projeto novo e descartável.

## 🍩 York diz

Ai, duzentas e oitenta e seis skills — só de ler eu já preciso de um donut. Mas olha o que interessa no bolso: é MIT de graça no repositório aberto e dezenove dólares por assento no repo privado, o que significa que a versão grátis é a isca e a conta chega quando o código não é mais público. E um mantenedor só publicando toda semana para sete harnesses é gente demais dependendo de uma pessoa. Guarda, não instala.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

**Language:**
  English |
  Português (Brasil) |
  简体中文 |
  繁體中文 |
  日本語 |
  한국어 |
  Türkçe |
  Русский |
  Tiếng Việt |
  ไทย |
  Deutsch |
  Español |
  Українська

Warning

**Official sources only.** Install ECC only from verified channels: the GitHub repository github.com/affaan-m/ECC, the npm packages `ecc-universal` and `ecc-agentshield`, the GitHub App, the plugin slug `ecc@ecc`, and the project website ecc.tools. Third-party re-uploads and unofficial mirrors are not maintained or reviewed by the project and may contain malware.

Run the canonical guided setup from your terminal:

`npx ecc-universal setup`
If npm reports a version or cache error, confirm the registry version before retrying:

`npm view ecc-universal version`
This path requires Node.js 18 or newer, Git, and Claude Code 2.1 or newer on
`PATH`. It safely installs, updates, or moves one `ecc@ecc` plugin scope and
records the hook profile you choose.

Alternatively, run Claude Code's native plugin commands inside Claude Code:

```
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```
The native path installs ECC's skills, agents, commands, and plugin-managed hooks. If you choose it, stop there. Do not also run a full manual install into Claude Code.

Both paths install the same `ecc@ecc` plugin. Choose one and do not stack
another manual Claude install on top.


| **ECC Pro + GitHub App**<sub>Install free · Private repos from $19/seat/mo</sub> | **Sponsor ECC**<sub>Fund the open-source project</sub> | **Community**<sub>Discord · Q&A · Show and Tell</sub> | 

**OSS stays free.** This repo is MIT-licensed forever. ECC Pro is the hosted GitHub App for private repos. Sponsors and Pro subscribers fund the work. That's why a single maintainer ships weekly across 7 harnesses.

**Partners & sponsors**

**Community sponsors:** Mike Morgan · @jasonwu513 · @1anter · @massimotodaro · @meadmccabe

Your agent can write code, but ECC gives it a coordinated engineering system and toolbox: it plans before it builds, verifies changes with tests, reviews its own work from a fresh context, remembers what matters, and turns repeated wins into reusable skills and workflows.

```
plan -> test -> implement -> review -> verify -> remember -> improve
```
Instead of rebuilding that process in every prompt, you install it once and make it part of how your agent works.

Optimize the context window. Persist everything else.


ECC is MIT-licensed open source. It works best with Claude Code today, has a supported Codex sync path, and provides capability-limited adapters for Cursor, OpenCode, Gemini, Zed, GitHub Copilot, Antigravity, Qwen, and other harnesses. See the support status matrix before assuming feature parity.

Access to 68 agents, 286 skills, and 94 legacy command shims, plus hooks, rules, memory, continuous learning, and AgentShield security scanning. The agents are specialized for planning, review, build repair, security, architecture, and domain work.

| Included | Count | What it gives you | 
|---|---|---|
| Agents | 68 agents | Planning, review, build repair, security, architecture, and domain work | 
| Skills | 286 skills | TDD, research, security, docs, frontend, data, ML, operations, and more | 
| Commands | 94 commands | Convenient entry points while ECC moves to a skills-first surface | 
| Hooks and memory | Runtime | Enforcement, session summaries, continuous learning, instincts, and context controls | 
| Rules | Selective | Always-loaded standards you choose by language or project | 
| AgentShield | Included | Scanning for prompts, hooks, MCP config, permissions, secrets, and agent files | 

Important

ECC 2.2 includes guided package setup for Claude Code, Codex, and Kimi Code.
The universal package requires Node.js 18 or newer. Claude plugin setup also
requires Git and Claude Code 2.1 or newer on `PATH`.

Run the package command from your terminal. For Claude Code setup, updates, scope changes, and hook-profile changes:

`npx ecc-universal setup`
To configure Claude Code, Codex, or Kimi Code in one reviewed flow:

`npx ecc-universal install --guided`
You can use ECC with Claude Code, Codex, and other harnesses at the same time. Choose one install method for each harness:

- **Recommended default:** run the guided Claude plugin setup above
- **Also supported for Claude Code:** use the native plugin commands above
- **Available in release 2.2:** guided package setup for Claude Code, Codex, and Kimi Code
- **Works:** Claude Code plugin + Codex native plugin
- **Works:** Claude Code plugin + the legacy Codex sync flow
- **Avoid:** Claude Code plugin + full Claude manual install
- **Avoid:** Codex sync + Codex marketplace plugin

**Do not stack install methods.** Installing ECC twice into the same harness can duplicate skills, commands, hooks, or configuration; installing it once into multiple harnesses does not.

If you already layered multiple installs and things look duplicated, skip straight to Reset / Uninstall ECC.

**Install trouble?** Open the short install or runtime problem form, or run `ecc feedback`. ECC never uploads diagnostics automatically.

Claude Code owns these built-in commands, including their errors when a marketplace, plugin, or conflicting scope already exists. ECC cannot intercept that parser. If either native command reports an existing install or scope conflict, use the 2.2 guided setup or resolve the conflicting Claude plugin scope before retrying; do not layer a manual install on top.

After ECC is installed, `/ecc:configure-ecc` is the namespaced in-Claude reconfiguration skill. It delegates to the same safe setup flow, but it is available only after the plugin is installed and cannot replace Claude Code's built-in `/plugin` command during a first install.

Claude Code plugins cannot distribute `rules`, so add only the rule packs you actually want:

```
git clone https://github.com/affaan-m/ECC.git
cd ECC
mkdir -p ~/.claude/rules/ecc
cp -R rules/common ~/.claude/rules/ecc/
cp -R rules/typescript ~/.claude/rules/ecc/  # replace with your stack
```
Start with `rules/common` plus one language or framework pack you actually use. If you install the plugin, do not run `./install.sh --profile full` afterward.

#### **Prefer settings.json? Add the marketplace declaratively**

Add directly to your `~/.claude/settings.json`:

```
{
  "extraKnownMarketplaces": {
    "ecc": {
      "source": {
        "source": "github",
        "repo": "affaan-m/ECC"
      }
    }
  },
  "enabledPlugins": {
    "ecc@ecc": true
  }
}
```
This gives you the same result as the two `/plugin` commands above.

#### **Naming + migration note (ecc@ecc, affaan-m/ECC, ecc-universal)**

ECC has three public identifiers, and they are not interchangeable:

- GitHub source repo: `affaan-m/ECC`
- Claude marketplace/plugin identifier: `ecc@ecc`
- npm package: `ecc-universal`

This is intentional. Anthropic marketplace/plugin installs are keyed by a canonical plugin identifier, so ECC uses `ecc@ecc` to keep tool names and slash-command namespaces short enough for strict Desktop/API validators. Older posts may still show the former long marketplace identifier; treat that as a legacy alias only. Separately, the npm package stayed on `ecc-universal`, so npm installs and marketplace installs intentionally use different names.

npm releases are cut per version tag, not per commit, so `ecc-universal` tracks releases (2.1, 2.2, ...) rather than every push to `main`. Install from git if you want the bleeding edge.

If your local Claude setup was wiped or reset, that does not mean you need to repurchase anything. Start with `node scripts/ecc.js list-installed`, then run `node scripts/ecc.js doctor` and `node scripts/ecc.js repair` before reinstalling. That usually restores ECC-managed files without rebuilding your setup.

Current Codex releases can install ECC as a native repo-marketplace plugin. The marketplace entry uses the repository root so Codex's cache receives the manifest together with all referenced skills, MCP configuration, hook runtime, scripts, and assets:

```
codex plugin marketplace add affaan-m/ECC
codex plugin add ecc@ecc
codex plugin list --json
node scripts/codex/check-plugin-cache.js
```
Both add commands are idempotent. To refresh later, run `codex plugin marketplace upgrade ecc` followed by `codex plugin add ecc@ecc`. Codex stores one enabled plugin state in the active `CODEX_HOME`; it does not offer Claude's `user`, `project`, and `local` scopes. Its native hooks require an explicit trust decision and do not use Claude's four ECC hook profiles. Inside Codex, invoke `$configure-ecc` for the guided provider-aware flow.

The older `scripts/sync-ecc-to-codex.sh` path is a deprecated compatibility option for users who intentionally need copied and merged configuration in `~/.codex`; it is not required for the native plugin. New sync runs write an ownership manifest so cleanup can preserve modified user files. Run Codex once first so `~/.codex/config.toml` exists, then:

```
git clone https://github.com/affaan-m/ECC.git
cd ECC
npm install
bash scripts/sync-ecc-to-codex.sh
```
To inspect or remove that legacy layer without touching Codex conversations or native plugin caches:

```
node scripts/ecc.js uninstall --legacy-codex-sync --dry-run
node scripts/ecc.js uninstall --legacy-codex-sync
```
Pre-manifest installations are handled conservatively: ECC removes its marked `AGENTS.md` block but preserves copied files it cannot prove it owns and reports them for review.

You can also open the ECC repository directly in Codex for a project-local setup. Codex reads the root `AGENTS.md` and the trusted project configuration in `.codex/` without a global sync. Do not add the native marketplace plugin on top of the sync flow.

For repo navigation, surface ownership, and PR diff packet guidance, read the Codex ECC Navigation Map. See the .codex plugin notes for native lifecycle details.

#### **Cursor, OpenCode, Gemini, Zed, Antigravity, Qwen, Hermes, OpenClaw, Kimi, CodeBuddy, JoyCode, Copilot**

Clone ECC once, then choose the target that matches your harness:

```
git clone https://github.com/affaan-m/ECC.git
cd ECC
```
| Harness | Install or setup | Notes | 
|---|---|---|
| Cursor | `./install.sh --profile minimal --target cursor` | Project-local `.cursor/` adapter | 
| OpenCode | `npm install && npm run build:opencode && ./install.sh --profile full --target opencode` | Builds the plugin payload before the full install | 
| Gemini CLI | `./install.sh --profile minimal --target gemini` | Project-local `.gemini/` config | 
| Zed | `./install.sh --profile minimal --target zed` | Project-local `.zed/` adapter | 
| Antigravity | `./install.sh --profile minimal --target antigravity` | See the Antigravity guide | 
| Qwen CLI | `./install.sh --profile minimal --target qwen` | See the Qwen guide | 
| Hermes | `./install.sh --profile minimal --target hermes` | See the Hermes setup guide | 
| OpenClaw | `./install.sh --profile minimal --target openclaw` | Managed home-directory install | 
| Kimi Code CLI | `./install.sh --profile minimal --target kimi` | Project-local `.kimi-code/` install | 
| CodeBuddy | `./install.sh --profile minimal --target codebuddy` | Project-local `.codebuddy/` install | 
| JoyCode | `./install.sh --profile minimal --target joycode` | Project-local `.joycode/` install | 

GitHub Copilot support is already included in this repository. `.github/copilot-instructions.md` provides the instruction layer, `.github/prompts/` contains the reusable `/plan`, `/tdd`, `/security-review`, `/build-fix`, and `/refactor` prompts, and `.vscode/settings.json` enables `chat.promptFiles`.

For a harness without a native ECC target, use the manual adaptation guide. It explains how to carry a small set of ECC skills and workflow instructions into chat-style tools without pretending hooks or native skill discovery are available.

Cursor installs agent definitions under `.cursor/agents/ecc-*.md`. Cursor-native loading behavior can vary by Cursor build. ECC does not install root `AGENTS.md` into `.cursor/`. The adapter keeps Cursor's context scoped to its native rules and agent surfaces.

Deep per-harness notes (feature parity, hook adapters, limitations) live in Platform Support below.

ECC works through each harness's normal configuration, so you can use an official provider, a compatible custom API endpoint or model gateway, or a self-hosted model without changing ECC's workflows.

For Claude Code, ECC does not hardcode Anthropic-hosted transport settings. Minimal gateway example:

```
export ANTHROPIC_BASE_URL=https://your-gateway.example.com
export ANTHROPIC_AUTH_TOKEN=your-token
claude
```
If your gateway remaps model names, configure that in Claude Code rather than in ECC. ECC's hooks, skills, commands, and rules are model-provider agnostic once the `claude` CLI is already working. See Anthropic's LLM gateway documentation and model configuration documentation.

Run or self-host any open-source model behind that gateway using separate compute and serving setup. If you need GPU capacity, Itô is ECC's preferred compute sponsor; any GPU provider works. The sponsorship link is passive: it does not invoke an RFQ, reserve capacity, provision compute, or configure serving. Separately, `ecc ito find` invokes the explicitly configured canonical Itô CLI and submits a live authenticated RFQ; it does not reserve capacity. Managed inference through Itô is not live yet.

The Kimi Code harness and the model-serving layer are separate. ECC configures the agent harness; you bring an API endpoint or self-host an open-weight Kimi model on your own GPU capacity. This adapter is verified against Kimi Code 0.31.x (`@moonshot-ai/kimi-code`):

| **1. Get GPU capacity**<sub>Use Itô or any GPU provider.</sub> | **2. Serve Kimi**<sub>Expose the chosen checkpoint through a compatible endpoint.</sub> | **3. Run Kimi Code with ECC**<sub>Install project instructions and skills, then start Kimi Code.</sub> | 

Configure the endpoint with Kimi Code's official provider guide, then install ECC:

```
bash ./install.sh --target kimi --profile minimal
node scripts/ecc.js doctor --target kimi
kimi
```
Kimi Code discovers the installed `.kimi-code/AGENTS.md` instructions and `.kimi-code/skills/` workflows natively; project-level `.agents/skills/` is also an official discovery location. ECC safely merges project MCP entries into `.kimi-code/mcp.json` and does not change the user-level `~/.kimi-code/config.toml`. Kimi Code supports native hooks, but ECC's current managed-project adapter does not configure them, so this installer does not offer Kimi hook profiles. The installer dry-run and regression suite verify that every managed Kimi write stays inside the project-local `.kimi-code/` root.

`ecc ito` delegates to the separately installed canonical Itô client; ECC does not maintain a second API client. `ecc ito login [--no-browser]` performs device authorization, opens the Itô verification page by default, and persists a device token in macOS Keychain; `--no-browser` suppresses the page handoff. ECC itself does no browser automation. `ecc ito auth` is validation-only and rejects `--no-browser`. The available operations are `ecc ito login`, `ecc ito auth`, `ecc ito find`, `ecc ito status`, and the separately gated `ecc ito evals`. The matching MCP tools remain `ito_auth`, `ito_find`, and `ito_status`; `ito_auth` validates existing credentials and node qualification is CLI-only.

The `ito-compute-cli` package is currently unpublished. Build it locally from the Itô runtime repo (private while the desk hardens; design partners get access) under `cli/ito-compute-cli`, run `npm ci` and `npm run check`, then set `ECC_ITO_CLI_EXECUTABLE` to that build's absolute `dist/bin/ito.js` path. Login never inherits `ITO_API_KEY`; auth, find, and status forward `ITO_API_KEY` directly when configured, and `ITO_AUTH_MODE=legacy` is not required. `ecc ito logout` revokes the current device credential and retains its local copy if remote revocation cannot be confirmed. Device tokens use macOS Keychain by default; explicit file fallback must retain owner-only directory/file permissions. ECC does not discover this credential-bearing client through `PATH`. See the `ito-compute` skill for the full RFQ authority and MCP setup contract.

`find` submits a live authenticated RFQ. It does not reserve capacity. `evals` requires both `ITO_ENABLE_SIXTYTWO_LIVE=1` and `--live-sixtytwo`, a separately installed `sixtytwo-cli==0.3.33`, an explicit node list, and an existing absolute configuration directory. It cannot rent, launch, recover, repair, or purchase. ECC exposes no quote lock, purchase, workload, or inference path, and it never replaces a missing client or failed live call with a local result.

The options stay here, directly under the main install paths, so you do not have to hunt through the README when the default setup is not the right fit.

#### **Low-context install with no hook runtime**

Use this when you want ECC's rules, agents, commands, platform config, and core workflows without runtime hooks:

`npx ecc-universal install --profile minimal --target claude`
From a source checkout, the equivalent command is:

`./install.sh --profile minimal --target claude`
Windows:

`.\install.ps1 --profile minimal --target claude`
This profile intentionally excludes `hooks-runtime`.

Claude manual installs place each skill directly under `~/.claude/skills/<skill-name>/` (or `.claude/skills/<skill-name>/` for `claude-project`) so Claude Code can discover it. When upgrading an older ECC manual install, the installer migrates only nested `skills/ecc/` files recorded in ECC install-state. If a flat skill directory is user-owned, ECC preserves it, prints a conflict warning, and keeps any older managed copy tracked for a safe uninstall instead of overwriting user files.

For the normal core profile with hooks disabled:

```
./install.sh --profile core --without baseline:hooks --target claude
./install.sh --profile core --no-hooks --target claude
```
Add the hook runtime later only if you want it:

`./install.sh --target claude --modules hooks-runtime --enable-hooks`
Any install whose profile or modules would materialize the hook runtime requires
an explicit decision. Without `--enable-hooks` or `--no-hooks`, the installer
prints what the hooks can do and stops before writing anything. The guided
installer (`ecc install --guided`) asks for this choice interactively.

#### **Choose only the components you need**

Ask the packaged advisor which components match your work:

`node scripts/ecc.js consult "security reviews" --target claude`
It returns matching components, related profiles, and preview/install commands. Use the preview command before installing if you want to inspect the exact file plan.

You can also install explicit skills or capabilities:

```
./install.sh --target claude --skills tdd-workflow,security-review
node scripts/ecc.js install --profile minimal --target claude --with capability:machine-learning
```
Manual component-by-component copying also works. Each component is fully independent:

```
### Just agents
cp agents/*.md ~/.claude/agents/
### Rules directories (common + language-specific)
mkdir -p ~/.claude/rules/ecc
cp -r rules/common ~/.claude/rules/ecc/
cp -r rules/typescript ~/.claude/rules/ecc/   # pick your stack
### Core/general skills only (Claude Code loads skills from direct children
### of ~/.claude/skills; do not nest manual installs under ~/.claude/skills/ecc/)
mkdir -p ~/.claude/skills
cp -r .agents/skills/* ~/.claude/skills/
cp -r skills/search-first ~/.claude/skills/
### Optional: maintained slash-command compatibility during migration
mkdir -p ~/.claude/commands
cp commands/*.md ~/.claude/commands/
```
Retired shims live in `legacy-command-shims/`. Copy individual files from there only if you still need old names such as `/tdd`.

#### **Project-local rules instead of global rules**

Use project-local rules when ECC's standards should apply to one repository rather than every Claude Code session:

```
cd your-project
mkdir -p .claude/rules/ecc
cp -R /path/to/ECC/rules/common .claude/rules/ecc/
cp -R /path/to/ECC/rules/typescript .claude/rules/ecc/
```
Rules are always-loaded context, so begin with `common` and one pack for the stack you actually use. When copying rules manually, copy the whole language directory (for example `rules/common` or `rules/golang`), not the files inside it, so relative references keep working and filenames do not collide.

#### **Fully manual Claude install**

Use this only when you are intentionally skipping the plugin path:

```
git clone https://github.com/affaan-m/ECC.git
cd ECC
./install.sh --profile full
```
Windows:

```
git clone https://github.com/affaan-m/ECC.git
cd ECC
.\install.ps1 --profile full
```
If you choose this path, stop there. Do not also run `/plugin install`.

For hand-picked manual installs, Claude discovers skills as direct children of `~/.claude/skills/`; do not nest them under `~/.claude/skills/ecc/`.

Do not copy the raw repo `hooks/hooks.json` into `~/.claude/settings.json` or `~/.claude/hooks/hooks.json`. That file is plugin/repo-oriented; use the installer so hook command paths are rewritten correctly:

`bash ./install.sh --target claude --modules hooks-runtime --enable-hooks`
That writes resolved hooks to `~/.claude/hooks/hooks.json` and leaves any existing `~/.claude/settings.json` untouched.

If you installed ECC via `/plugin install`, do not copy those hooks into `settings.json`. Claude Code v2.1+ already auto-loads plugin `hooks/hooks.json`, and duplicating them in `settings.json` causes duplicate execution and cross-platform hook conflicts.

On Windows, Claude's config root is `%USERPROFILE%\\.claude`; install the hook runtime with:

`pwsh -File .\install.ps1 --target claude --modules hooks-runtime --enable-hooks`
Claude plugin installs intentionally do not auto-enable ECC's bundled MCP server definitions. This avoids overlong plugin MCP tool names on strict third-party gateways while keeping manual MCP setup available.

Use Claude Code's `/mcp` command or CLI-managed MCP setup for live Claude Code server changes; Claude Code persists those choices in `~/.claude.json`. For repo-local MCP access, copy desired MCP server definitions from `mcp-configs/mcp-servers.json` into a project-scoped `.mcp.json`.

ECC ships exactly one default connector (`chrome-devtools`); everything else is a skill wrapping a CLI/REST API or an opt-in catalog entry. The rule and the June 2026 audit that retired the previous six defaults live in docs/MCP-CONNECTOR-POLICY.md.

If you already run your own copies of ECC-bundled MCPs, set:

`export ECC_DISABLED_MCPS="chrome-devtools"`
ECC-managed install and Codex sync flows will skip or remove those bundled servers instead of re-adding duplicates. `ECC_DISABLED_MCPS` is an ECC install/sync filter, not a live Claude Code toggle.

**Important:** Replace `YOUR_*_HERE` placeholders with your actual API keys.

#### **Multi-model commands require additional setup**

`multi-*` commands are **not** covered by the base plugin/rules install.

To use `/multi-plan`, `/multi-execute`, `/multi-backend`, `/multi-frontend`, and `/multi-workflow`, you must also install the `ccg-workflow` runtime. Initialize it with `npx ccg-workflow`.

That runtime provides the external dependencies these commands expect, including:

- `~/.claude/bin/codeagent-wrapper`
- `~/.claude/.ccg/prompts/*`

Without `ccg-workflow`, these `multi-*` commands will not run correctly.

#### **Reset, repair, or uninstall**

If you installed from the universal package, run these commands from the same project directory used for installation:

```
npx ecc-universal list-installed
npx ecc-universal doctor
npx ecc-universal repair
npx ecc-universal uninstall --dry-run
npx ecc-universal uninstall
```
From a source checkout, inspect the managed state before reinstalling:

```
node scripts/ecc.js list-installed
node scripts/ecc.js doctor
node scripts/ecc.js repair
node scripts/ecc.js uninstall --dry-run
```
For a direct source-checkout uninstall:

```
node scripts/uninstall.js --dry-run
node scripts/uninstall.js
```
If you are leaving, the uninstall command prints an optional 20-second feedback form. It is a public GitHub issue, never blocks uninstall, and ECC does not upload diagnostics. You can also run `ecc feedback` at any time to see the problem, feedback, and feature routes.

Plugin users should remove the plugin from Claude Code, then delete only the rule folders they manually copied and no longer want. ECC only removes files recorded in its install-state. It does not claim unrelated files in your harness directories.

If you stacked methods, clean up in this order:

1. Remove the Claude Code plugin install.
2. Run the ECC uninstall command from the project directory that contains the managed install-state.
3. Delete any extra rule folders you copied manually and no longer want.
4. Reinstall once, using a single path.

Important

These package-runner commands require `ecc-universal` 2.2.0 or newer and
Node.js 18 or newer. Claude plugin setup also requires Git and Claude Code
2.1 or newer on `PATH`.

For Claude Code plugin setup, updates, scope changes, and hook-profile changes:

`npx ecc-universal setup`
ECC 2.2 supports the same guided setup through modern package runners:

| Package runner | Guided setup command | 
|---|---|
| npm / npx | `npx ecc-universal setup` | 
| pnpm | `pnpm dlx ecc-universal setup` | 
| Yarn 2+ | `yarn dlx ecc-universal setup` | 
| Bun | `bunx ecc-universal setup` | 

Yarn Classic 1 does not provide `yarn dlx`; use `npx`, install the package globally, or upgrade Yarn for a temporary one-shot run.

The wizard inventories the official marketplace and every native Claude install scope before making changes, then installs, updates, or safely moves `ecc@ecc` to the scope you choose. Rerun the same command whenever you want to update ECC, change scope, or change its hook profile. This setup wizard currently configures the Claude Code plugin; use the multi-harness wizard below for Codex or Kimi Code.

To configure more than one coding agent in one reviewed flow, use the multi-harness wizard:

`npx ecc-universal install --guided`
It lets you select any combination of Claude Code, Codex, and Kimi Code, shows each install channel and destination, preflights every selection before the first write, and asks for one final confirmation.

| Harness | Guided install behavior | 
|---|---|
| Claude Code | Native `ecc@ecc` plugin with one`user` ,`project` , or`local` scope and an ECC hook profile | 
| Codex | Native Codex marketplace/plugin lifecycle; hook review and trust remain Codex-owned | 
| Kimi Code | Managed project files under `./.kimi-code` ; ECC hooks, model/provider settings, and authentication are not configured | 

For automation, make every provider-specific choice explicit:

```
npx ecc-universal install --guided \
  --harness claude --harness codex --harness kimi \
  --claude-scope local --claude-hooks standard \
  --profile core --yes
```
Verify the native guided Codex path and managed Kimi path without writing first:

```
npx ecc-universal install --guided --harness codex --dry-run
npx ecc-universal install --profile core --target kimi --dry-run
```
Additional package-name commands are also available through the 2.2 alias:

```
npx ecc-universal consult "security reviews" --target claude
npx ecc-universal install --profile minimal --target claude --with capability:machine-learning
npx ecc-universal doctor --target kimi
```
Do not use `npx ecc-install --profile minimal --target claude`: `ecc-install` is a binary name inside `ecc-universal`, not a separately published npm package.

ECC also ships advanced managed adapters for `cursor`, `antigravity`, `gemini`, `opencode`, `codebuddy`, `joycode`, `qwen`, `zed`, `hermes`, and `openclaw`. Those targets still use their documented `ecc install --target ...` paths until each adapter has passed the guided collision, update, repair, and uninstall lifecycle matrix. Neither wizard silently installs into every detected harness.

Start with the workflow you need, not the full catalog.

| What you are doing | Start here | 
|---|---|
| Building a feature | `/ecc:plan "describe the feature"` , then`tdd-workflow` | 
| Fixing a bug | Reproduce it with a failing test, then use `tdd-workflow` | 
| Reviewing new code | `/code-review` for a fresh-context review | 
| Repairing a build | `/build-fix` | 
| Cleaning a codebase | `/refactor-clean` | 
| Checking context pressure | `/context-budget` | 
| Ending a long session | `/save-session` or`/learn-eval` | 
| Resuming later | `/resume-session` | 
| Auditing agent config | `/security-scan` or`npx -y ecc-agentshield scan --path .` | 

#### **Plugin commands and manual commands**

Claude Code plugin commands use the namespaced form:

```
/ecc:plan "Add authentication"
```
Manual installs may expose the shorter compatibility form:

```
/plan "Add authentication"
```
Skills are the primary workflow surface. Commands remain convenient entry points and compatibility shims. Check what is installed with:

`/plugin list ecc@ecc`
#### **Which agent should I use?**

Skills are the canonical workflow surface; maintained slash entries stay available for command-first workflows.

| I want to... | Use this surface | Agent used | 
|---|---|---|
| Plan a new feature | `/ecc:plan "Add auth"` | planner | 
| Design system architecture | `/ecc:plan` + architect agent | architect | 
| Write code with tests first | `tdd-workflow` skill | tdd-guide | 
| Review code I just wrote | `/code-review` | code-reviewer | 
| Fix a failing build | `/build-fix` | build-error-resolver | 
| Run end-to-end tests | `e2e-testing` skill | e2e-runner | 
| Find security vulnerabilities | `/security-scan` | security-reviewer | 
| Remove dead code | `/refactor-clean` | refactor-cleaner | 
| Update documentation | `/update-docs` | doc-updater | 
| Review Go code | `/go-review` | go-reviewer | 
| Review Python code | `/python-review` | python-reviewer | 
| Review F# code | *(invoke `fsharp-reviewer` directly)* | fsharp-reviewer | 
| Review TypeScript/JavaScript code | *(invoke `typescript-reviewer` directly)* | typescript-reviewer | 
| Develop HarmonyOS apps | *(invoke `harmonyos-app-resolver` directly)* | harmonyos-app-resolver | 
| Audit database queries | *(auto-delegated)* | database-reviewer | 
| Review production ML changes | `mle-workflow` skill +`mle-reviewer` agent | mle-reviewer | 

#### **Common workflows**

Slash forms below are shown where they remain part of the maintained command surface. Retired short-name shims such as `/tdd` and `/eval` live in `legacy-command-shims/` for explicit opt-in only.

**Starting a new feature:**

```
/ecc:plan "Add user authentication with OAuth"
                                              -> planner creates implementation blueprint
tdd-workflow skill                            -> tdd-guide enforces write-tests-first
/code-review                                  -> code-reviewer checks your work
```
**Fixing a bug:**

```
tdd-workflow skill                            -> tdd-guide: write a failing test that reproduces it
                                              -> implement the fix, verify test passes
/code-review                                  -> code-reviewer: catch regressions
```
**Preparing for production:**

```
/security-scan                                -> security-reviewer: OWASP Top 10 audit
e2e-testing skill                             -> e2e-runner: critical user flow tests
/test-coverage                                -> verify 80%+ coverage
```
Important

**NEW IN ECC 2.1: Plan Canvas · Kimi harness · self-hosted compute on Itô GPUs.**
See the full release notes →

Your agent writes a plan, then opens it in a loopback-only browser canvas. Click the part you mean, attach numbered annotations, chat from a side rail, and hit **Approve plan** or **Request changes**. The verdict maps straight onto `/plan`'s CONFIRM gate. Mermaid diagrams render live, and edits to the plan file reload the page.

It's harness- and model-agnostic: a plain CLI (`ecc-plan-canvas`) speaking JSON, so any agent can drive it. Try it: ask your agent to `/ecc:plan` anything, then review from the page instead of the terminal.

Open the plan used in this demo →

- **Kimi Code install target** (`--target kimi` ): ECC installs natively into Moonshot AI's Kimi Code CLI
- **Self-host on GPUs** : a verified path with Itô, ECC's preferred compute sponsor, including the opt-in`ecc ito find` RFQ bridge (details and disclosures above in Self-Hosted Models and Custom Endpoints)
- **Moonshot AI (Kimi), Itô, and Atlas Cloud** are now public sponsors
- **Hermes + OpenClaw install targets** , a Codex navigation guide, consolidated PostToolUse hooks, and supply-chain hardening

`ecc memory` gives Claude, Codex, Hermes, OpenClaw, Kimi, and other harnesses one local, inspectable Markdown format for durable context and handoffs. The optional `ecc-memory-mcp` stdio server exposes the same bounded save/search/read/doctor surface without enabling itself by default. Full detail in Share context between harnesses below.

#### **Previous releases**

| Version | Highlights | 
|---|---|
| v2.0.0 | The Agent Harness Operating System: cross-harness graduation, control-pane substrate, `orch-*` orchestrators, Discord + ECC bot, single-connector MCP policy | 
| v1.10.0 | Surface refresh, operator workflows, ECC 2.0 alpha | 
| v1.9.0 | Selective install, ECC Tools Pro, 12 language ecosystems | 
| v1.8.0 | Harness performance and cross-platform reliability | 
| v1.7.0 | Cross-platform expansion and presentation builder | 
| v1.6.0 | Codex Edition and the ECC Tools GitHub App | 
| v1.5.0 | Universal Edition | 
| v1.4.0 | Multi-language rules, installation wizard, PM2 orchestration | 
| v1.3.0 | Complete OpenCode plugin support | 
| v1.2.0 | Unified commands and skills | 
| v1.1.0 | Cross-platform support and community fixes | 
| v1.0.0 | Official plugin release | 

#### **Release history in detail**

Stable graduation of the 2.0 line: the control-pane substrate (session adapters + MCP inventory), the worktree-lifecycle service, the `orch-*` orchestrator family, and the launch of the ECC Discord community. Full notes: docs/releases/2.0.0/release-notes.md.

- **Dashboard GUI** : New Tkinter-based desktop application (`ecc_dashboard.py` or`npm run dashboard` ) with dark/light theme toggle, font customization, and project logo in header and taskbar.
- **Public surface synced to the live repo** : metadata, catalog counts, plugin manifests, and install-facing docs now match the actual OSS surface.
- **Operator and outbound workflow expansion** :`brand-voice` ,`social-graph-ranker` ,`connections-optimizer` ,`customer-billing-ops` ,`ecc-tools-cost-audit` ,`google-workspace-ops` ,`project-flow-ops` , and`workspace-surface-audit` round out the operator lane.
- **Media and launch tooling** :`manim-video` ,`remotion-video-creation` , and upgraded social publishing surfaces make technical explainers and launch content part of the same system.
- **Framework and product surface growth** :`nestjs-patterns` , richer Codex/OpenCode install surfaces, and expanded cross-harness packaging keep the repo usable beyond a single harness.
- **Itô prediction-market skill pack** : the consolidated`ito-baskets` skill (read-only basket index, comparison, market briefs, and non-executable planning worksheets — replacing the former`ito-market-intelligence` ,`ito-basket-compare` ,`ito-trade-planner` , and`ito-data-atlas-agent` skills), plus`prediction-market-oracle-research` and`prediction-market-risk-review` , add public, non-advisory market/basket workflows while keeping live Itô API access gated and separate from ECC Tools billing.
- **Optimization skill pack** :`parallel-execution-optimizer` ,`benchmark-optimization-loop` ,`data-throughput-accelerator` ,`latency-critical-systems` , and`recursive-decision-ledger` turn repeated speed/recursion prompts into bounded benchmark, throughput, and decision-ledger workflows.
- **ECC 2.0 alpha in-tree** : the Rust control-plane prototype in`ecc2/` builds locally and exposes`dashboard` ,`start` ,`sessions` ,`status` ,`stop` ,`resume` , and`daemon` commands.
- **Operator status snapshots** :`ecc status --markdown --write status.md` turns the local state store into a portable handoff covering readiness, active sessions, skill-run health, install health, pending governance events, and linked work items from Linear/GitHub/handoffs.
- **Ecosystem hardening** : AgentShield, ECC Tools cost controls, billing portal work, and website refreshes continue to ship around the core plugin instead of drifting into separate silos.

- **Selective install architecture** : Manifest-driven install pipeline with`install-plan.js` and`install-apply.js` for targeted component installation. State store tracks what's installed and enables incremental updates.
- **6 new agents** :`typescript-reviewer` ,`pytorch-build-resolver` ,`java-build-resolver` ,`java-reviewer` ,`kotlin-reviewer` ,`kotlin-build-resolver` expand language coverage to 10 languages.
- **New skills** :`pytorch-patterns` ,`documentation-lookup` ,`bun-runtime` ,`nextjs-turbopack` , 8 operational domain skills, and`mcp-server-patterns` .
- **Session and state infrastructure** : SQLite state store with query CLI, session adapters for structured recording, skill evolution foundation for self-improving skills.
- **Orchestration overhaul** : Deterministic harness audit scoring, hardened orchestration status and launcher compatibility, observer loop prevention with 5-layer guard.
- **Observer reliability** : Memory explosion fix with throttling and tail sampling, sandbox access fix, lazy-start logic, and re-entrancy guard.
- **12 language ecosystems** : New rules for Java, PHP, Perl, Kotlin/Android/KMP, C++, and Rust join existing TypeScript, Python, Go, and common rules.
- **Community contributions** : Korean and Chinese translations, biome hook optimization, video processing skills, operational skills, PowerShell installer, Antigravity IDE support.
- **CI hardening** : 19 test failure fixes, catalog count enforcement, install manifest validation, and full test suite green.

- **Harness-first release** : ECC is explicitly framed as an agent harness performance system, not just a config pack.
- **Hook reliability overhaul** : SessionStart root fallback, Stop-phase session summaries, and script-based hooks replacing fragile inline one-liners.
- **Hook runtime controls** :`ECC_HOOK_PROFILE=minimal|standard|strict` and`ECC_DISABLED_HOOKS=...` for runtime gating without editing hook files.
- **New harness commands** :`/harness-audit` ,`/loop-start` ,`/loop-status` ,`/quality-gate` ,`/model-route` .
- **NanoClaw v2** : model routing, skill hot-load, session branch/search/export/compact/metrics.
- **Cross-harness parity** : behavior tightened across Claude Code, Cursor, OpenCode, and Codex app/CLI.
- **997 internal tests passing** : full suite green after hook/runtime refactor and compatibility updates.

- **Codex app + CLI support** : Direct`AGENTS.md` -based Codex support, installer targeting, and Codex docs
- **`frontend-slides` skill** : Zero-dependency HTML presentation builder with PPTX conversion guidance and strict viewport-fit rules
- **5 new generic business/content skills** :`article-writing` ,`content-engine` ,`market-research` ,`investor-materials` ,`investor-outreach`
- **Broader tool coverage** : Cursor, Codex, and OpenCode support tightened so the same repo ships cleanly across all major harnesses
- **992 internal tests** : Expanded validation and regression coverage across plugin, hooks, skills, and packaging

- **Codex CLI support** : New`/codex-setup` command generates`codex.md` for OpenAI Codex CLI compatibility
- **7 new skills** :`search-first` ,`swift-actor-persistence` ,`swift-protocol-di-testing` ,`regex-vs-llm-structured-text` ,`content-hash-cache-pattern` ,`cost-aware-llm-pipeline` ,`skill-stocktake`
- **AgentShield integration** :`/security-scan` runs AgentShield directly from Claude Code; 1282 tests, 102 rules
- **GitHub Marketplace** : ECC Tools GitHub App live at github.com/marketplace/ecc-tools with free/pro/enterprise tiers
- **30+ community PRs merged** : Contributions from 30 contributors across 6 languages
- **978 internal tests** : Expanded validation suite across agents, skills, commands, hooks, and rules

- **Fixed instinct import content loss** :`parse_instinct_file()` was silently dropping all content after frontmatter (Action, Evidence, Examples sections) during`/instinct-import` . (#148, #161)

- **Interactive installation wizard** : New`configure-ecc` skill provides guided setup with merge/overwrite detection
- **PM2 and multi-agent orchestration** : 6 new commands (`/pm2` ,`/multi-plan` ,`/multi-execute` ,`/multi-backend` ,`/multi-frontend` ,`/multi-workflow` ) for managing complex multi-service workflows
- **Multi-language rules architecture** : Rules restructured from flat files into`common/` +`typescript/` +`python/` +`golang/` directories. Install only the languages you need
- **Chinese (zh-CN) translations** : Complete translation of all agents, commands, skills, and rules (80+ files)
- **GitHub Sponsors support** : Sponsor the project via GitHub Sponsors
- **Enhanced CONTRIBUTING.md** : Detailed PR templates for each contribution type

- **Full OpenCode integration** : 12 agents, 24 commands, 16 skills with hook support via OpenCode's plugin system (20+ event types)
- **3 native custom tools** : run-tests, check-coverage, security-audit
- **LLM documentation** :`llms.txt` for comprehensive OpenCode docs

- **Python/Django support** : Django patterns, security, TDD, and verification skills
- **Java Spring Boot skills** : Patterns, security, TDD, and verification for Spring Boot
- **Session management** :`/sessions` command for session history
- **Continuous learning v2** : Instinct-based learning with confidence scoring, import/export, evolution

See the full changelog in Releases.

| Without a system | With ECC | 
|---|---|
| Plans disappear into chat history | Plans become editable artifacts before implementation starts | 
| "Please use TDD" is an instruction the model may forget | TDD becomes a gated RED -> GREEN -> REFACTOR workflow with evidence | 
| The same context writes and reviews the code | A fresh-context reviewer looks for regressions and blind spots | 
| Memory means saving an enormous transcript | Sessions are distilled into summaries, instincts, and reusable skills | 
| Quality checks depend on reminders | Hooks can enforce deterministic checks outside the prompt | 
| Agent configuration is trusted by default | AgentShield scans the harness itself as an attack surface | 

```
/ecc:plan "Add usage-based billing alerts"
  -> confirm or edit the plan
  -> activate tdd-workflow
  -> capture RED evidence before implementation
  -> implement until GREEN
  -> review from fresh context
  -> fix findings with regression tests
  -> verify build, lint, types, and tests
```
A result is not just code. It's a trail of evidence: the plan, the failing test, the passing test, the review findings, and the final verification.

Rules, skills, agents, and hooks solve different problems. Keeping those jobs separate is how ECC adds capability without dumping the entire repository into every session.

| Concept | What it does | Context behavior | 
|---|---|---|
| Skills | Reusable workflows such as TDD, security review, or deep research | Loaded when the task needs them | 
| Agents | Scoped workers with their own context and tool permissions | Isolate planning, implementation, and review | 
| Rules | Durable project or language standards | Always loaded, so install them selectively | 
| Hooks | Scripts triggered by harness events | Run outside the model context | 
| Instincts | Patterns learned from real sessions with confidence scores | Recalled when relevant | 

ECC's Memory Vault gives Claude, Codex, Hermes, OpenClaw, Kimi, and other harnesses one local, inspectable Markdown format for durable context and handoffs. Project and team memories live under `.ecc/memory/`; user memories live under `~/.ecc/memory/`.

```
npm install -g ecc-universal
ecc memory init --scope project
ecc memory search "authentication migration" --target-harness codex
ecc memory doctor
```
Memory is unreviewed context, not executable policy. Verify important claims against authoritative sources and promote accepted knowledge into governed project documentation. The optional `ecc-memory-mcp` server exposes the same bounded save, search, read, and doctor surface without enabling itself by default.

Open the Unified Memory workflow →

#### **Memory Vault in depth: scopes, handoffs, and trust boundaries**

The Memory Vault stores portable `ecc.memory.v1` Markdown documents instead of copying vendor transcripts or emailing context between agents. Project memories are protected by a fail-closed `.gitignore`; use the team scope only for human-inspected, version-controlled sharing. Team memories remain unreviewed context even after they are committed.

Skill-only, minimal, manual, and Claude plugin installs do not put the Memory Vault runtime on `PATH`. Install the npm runtime separately before using the CLI or optional MCP server:

```
npm install -g ecc-universal
ecc memory --help
command -v ecc-memory-mcp
```
```
### Initialize the project vault.
ecc memory init --scope project
### Write a handoff body to a regular file, then target the next harness.
ecc memory handoff \
  --from hermes \
  --target codex \
  --title "Continue authentication migration" \
  --body-file ./handoff.md
### Recall it from another harness.
ecc memory search "authentication migration" --target-harness codex
ecc memory read <memory-id>
### Validate the vault before sharing team memories.
ecc memory doctor
```
Memory bodies are accepted only through `--stdin` or `--body-file`, not as command-line values. The first release keeps every vault entry unreviewed and create-only; human review promotes accepted knowledge into governed project documentation rather than changing memory trust. Normal search recall returns active project and team memories. A direct ID read may inspect a non-active entry. User-scope recall must be requested explicitly. Agents must verify important claims against authoritative sources and must never treat recalled bodies as executable instructions or policy.

For opt-in MCP access, add the `ecc-memory-vault` entry from `mcp-configs/mcp-servers.json` to each harness that needs it, then run `ecc-memory-mcp`. The server exposes only `memory_save`, `memory_search`, `memory_read`, and `memory_doctor`. Each server must launch with a lowercase `ECC_MEMORY_HARNESS` identity; the identity is server-bound and cannot be supplied by a tool caller. User scope additionally requires the operator-controlled `ECC_MEMORY_ALLOW_USER_SCOPE=1` opt-in. See `skills/unified-memory/SKILL.md` for the workflow and trust boundaries, and `docs/design/ecc-memory-vault.md` for the capability contract.

This repo is the raw code. The guides explain everything.

| **The Shorthand Guide**<sub>Setup, foundations, and day-one use. **Read this first.** (thread)</sub> | **The Longform Guide**<sub>Context economics, memory, evals, and parallel agents. (thread)</sub> | **The Security Guide**<sub>Prompt injection, hooks, MCP, and AgentShield. (thread)</sub> | 

| Topic | What You'll Learn | 
|---|---|
| Token Optimization | Model selection, system prompt slimming, background processes | 
| Memory Persistence | Hooks that save/load context across sessions automatically | 
| Continuous Learning | Auto-extract patterns from sessions into reusable skills | 
| Verification Loops | Checkpoint vs continuous evals, grader types, pass@k metrics | 
| Parallelization | Git worktrees, cascade method, when to scale instances | 
| Subagent Orchestration | The context problem, iterative retrieval pattern | 

Commands Quick Reference | Manual Adaptation Guide

```
ECC/
|-- agents/           # 68 specialized subagents for delegation
|-- skills/           # 284 reusable workflows loaded on demand
|-- commands/         # 94 maintained slash-command shims
|-- rules/            # opt-in common and language standards
|-- hooks/            # runtime automation and enforcement
|-- scripts/          # install, repair, sync, orchestration, and checks
|-- .claude-plugin/   # Claude Code marketplace manifest
|-- .codex/           # Codex reference configuration and agent roles
|-- .opencode/        # OpenCode plugin, commands, and instructions
|-- .cursor/          # Cursor rules and hook adapter
|-- docs/             # public setup, architecture, and operating guides
```
The root is the source of truth. Platform adapters package or map these same workflows instead of maintaining separate copies.

#### **Annotated component catalog**

```
ECC/
|-- .claude-plugin/   # Plugin and marketplace manifests
|   |-- plugin.json         # Plugin metadata and component paths
|   |-- marketplace.json    # Marketplace catalog for /plugin marketplace add
|
|-- agents/           # 67 specialized subagents for delegation
|   |-- planner.md           # Feature implementation planning
|   |-- architect.md         # System design decisions
|   |-- tdd-guide.md         # Test-driven development
|   |-- code-reviewer.md     # Quality and security review
|   |-- security-reviewer.md # Vulnerability analysis
|   |-- build-error-resolver.md
|   |-- e2e-runner.md        # Playwright E2E testing
|   |-- refactor-cleaner.md  # Dead code cleanup
|   |-- doc-updater.md       # Documentation sync
|   |-- docs-lookup.md       # Documentation/API lookup
|   |-- chief-of-staff.md    # Communication triage and drafts
|   |-- loop-operator.md     # Autonomous loop execution
|   |-- harness-optimizer.md # Harness config tuning
|   |-- cpp-reviewer.md      # C++ code review
|   |-- cpp-build-resolver.md # C++ build error resolution
|   |-- fsharp-reviewer.md   # F# functional code review
|   |-- go-reviewer.md       # Go code review
|   |-- go-build-resolver.md # Go build error resolution
|   |-- python-reviewer.md   # Python code review
|   |-- database-reviewer.md # Database/Supabase review
|   |-- typescript-reviewer.md # TypeScript/JavaScript code review
|   |-- java-reviewer.md     # Java/Spring Boot code review
|   |-- java-build-resolver.md # Java/Maven/Gradle build errors
|   |-- kotlin-reviewer.md   # Kotlin/Android/KMP code review
|   |-- kotlin-build-resolver.md # Kotlin/Gradle build errors
|   |-- harmonyos-app-resolver.md # HarmonyOS/ArkTS app development
|   |-- rust-reviewer.md     # Rust code review
|   |-- rust-build-resolver.md # Rust build error resolution
|   |-- pytorch-build-resolver.md # PyTorch/CUDA training errors
|   |-- mle-reviewer.md      # Production ML pipeline, eval, serving, and monitoring review
|
|-- skills/           # Workflow definitions and domain knowledge
|   |-- coding-standards/           # Language best practices
|   |-- clickhouse-io/              # ClickHouse analytics, queries, data engineering
|   |-- backend-patterns/           # API, database, caching patterns
|   |-- frontend-patterns/          # React, Next.js patterns
|   |-- frontend-slides/            # HTML slide decks and PPTX-to-web presentation workflows
|   |-- article-writing/            # Long-form writing in a supplied voice without generic AI tone
|   |-- content-engine/             # Multi-platform social content and repurposing workflows
|   |-- market-research/            # Source-attributed market, competitor, and investor research
|   |-- investor-materials/         # Pitch decks, one-pagers, memos, and financial models
|   |-- investor-outreach/          # Personalized fundraising outreach and follow-up
|   |-- continuous-learning/        # Legacy v1 Stop-hook pattern extraction
|   |-- continuous-learning-v2/     # Instinct-based learning with confidence scoring
|   |-- iterative-retrieval/        # Progressive context refinement for subagents
|   |-- strategic-compact/          # Manual compaction suggestions (Longform Guide)
|   |-- tdd-workflow/               # TDD methodology
|   |-- security-review/            # Security checklist
|   |-- eval-harness/               # Verification loop evaluation (Longform Guide)
|   |-- verification-loop/          # Continuous verification (Longform Guide)
|   |-- videodb/                    # Video and audio: ingest, search, edit, generate, stream
|   |-- golang-patterns/            # Go idioms and best practices
|   |-- golang-testing/             # Go testing patterns, TDD, benchmarks
|   |-- cpp-coding-standards/       # C++ coding standards from C++ Core Guidelines
|   |-- cpp-testing/                # C++ testing with GoogleTest, CMake/CTest
|   |-- django-patterns/            # Django patterns, models, views
|   |-- django-security/            # Django security best practices
|   |-- django-tdd/                 # Django TDD workflow
|   |-- django-verification/        # Django verification loops
|   |-- laravel-patterns/           # Laravel architecture patterns
|   |-- laravel-security/           # Laravel security best practices
|   |-- laravel-tdd/                # Laravel TDD workflow
|   |-- laravel-verification/       # Laravel verification loops
|   |-- python-patterns/            # Python idioms and best practices
|   |-- python-testing/             # Python testing with pytest
|   |-- quarkus-patterns/           # Java Quarkus patterns
|   |-- quarkus-security/           # Quarkus security
|   |-- quarkus-tdd/                # Quarkus TDD
|   |-- quarkus-verification/       # Quarkus verification
|   |-- springboot-patterns/        # Java Spring Boot patterns
|   |-- springboot-security/        # Spring Boot security
|   |-- springboot-tdd/             # Spring Boot TDD
|   |-- springboot-verification/    # Spring Boot verification
|   |-- configure-ecc/              # Interactive installation wizard
|   |-- security-scan/              # AgentShield security auditor integration
|   |-- java-coding-standards/      # Java coding standards
|   |-- jpa-patterns/               # JPA/Hibernate patterns
|   |-- postgres-patterns/          # PostgreSQL optimization patterns
|   |-- nutrient-document-processing/ # Document processing with Nutrient API
|   |-- database-migrations/        # Migration patterns (Prisma, Drizzle, Django, Go)
|   |-- api-design/                 # REST API design, pagination, error responses
|   |-- deployment-patterns/        # CI/CD, Docker, health checks, rollbacks
|   |-- docker-patterns/            # Docker Compose, networking, volumes, container security
|   |-- e2e-testing/                # Playwright E2E patterns and Page Object Model
|   |-- content-hash-cache-pattern/ # SHA-256 content hash caching for file processing
|   |-- cost-aware-llm-pipeline/    # LLM cost optimization, model routing, budget tracking
|   |-- regex-vs-llm-structured-text/ # Decision framework: regex vs LLM for text parsing
|   |-- swift-actor-persistence/    # Thread-safe Swift data persistence with actors
|   |-- swift-protocol-di-testing/  # Protocol-based DI for testable Swift code
|   |-- search-first/               # Research-before-coding workflow
|   |-- skill-stocktake/            # Audit skills and commands for quality
|   |-- liquid-glass-design/        # iOS 26 Liquid Glass design system
|   |-- foundation-models-on-device/ # Apple on-device LLM with FoundationModels
|   |-- swift-concurrency-6-2/      # Swift 6.2 Approachable Concurrency
|   |-- mle-workflow/               # Production ML data contracts, evals, deployment, monitoring
|   |-- perl-patterns/              # Modern Perl 5.36+ idioms and best practices
|   |-- perl-security/              # Perl security patterns, taint mode, safe I/O
|   |-- perl-testing/               # Perl TDD with Test2::V0, prove, Devel::Cover
|   |-- autonomous-loops/           # Autonomous loop patterns: sequential pipelines, PR loops, DAG orchestration
|   |-- plankton-code-quality/      # Write-time code quality enforcement with Plankton hooks
|   |-- codehealth-mcp/             # Optional CodeScene Code Health MCP skill (opt-in)
|   |-- docs/examples/project-guidelines-template.md  # Template for project-specific skills
|
|-- commands/         # Maintained slash-entry compatibility; prefer skills/
|   |-- plan.md             # /plan - Implementation planning
|   |-- code-review.md      # /code-review - Quality review
|   |-- build-fix.md        # /build-fix - Fix build errors
|   |-- refactor-clean.md   # /refactor-clean - Dead code removal
|   |-- quality-gate.md     # /quality-gate - Verification gate
|   |-- learn.md            # /learn - Extract patterns mid-session (Longform Guide)
|   |-- learn-eval.md       # /learn-eval - Extract, evaluate, and save patterns
|   |-- checkpoint.md       # /checkpoint - Save verification state (Longform Guide)
|   |-- setup-pm.md         # /setup-pm - Configure package manager
|   |-- go-review.md        # /go-review - Go code review
|   |-- go-test.md          # /go-test - Go TDD workflow
|   |-- go-build.md         # /go-build - Fix Go build errors
|   |-- skill-create.md     # /skill-create - Generate skills from git history
|   |-- instinct-status.md  # /instinct-status - View learned instincts
|   |-- instinct-import.md  # /instinct-import - Import instincts
|   |-- instinct-export.md  # /instinct-export - Export instincts
|   |-- evolve.md           # /evolve - Cluster instincts into skills
|   |-- prune.md            # /prune - Delete expired pending instincts
|   |-- pm2.md              # /pm2 - PM2 service lifecycle management
|   |-- multi-plan.md       # /multi-plan - Multi-agent task decomposition
|   |-- multi-execute.md    # /multi-execute - Orchestrated multi-agent workflows
|   |-- multi-backend.md    # /multi-backend - Backend multi-service orchestration
|   |-- multi-frontend.md   # /multi-frontend - Frontend multi-service orchestration
|   |-- multi-workflow.md   # /multi-workflow - General multi-service workflows
|   |-- sessions.md         # /sessions - Session history management
|   |-- test-coverage.md    # /test-coverage - Test coverage analysis
|   |-- update-docs.md      # /update-docs - Update documentation
|   |-- update-codemaps.md  # /update-codemaps - Update codemaps
|   |-- python-review.md    # /python-review - Python code review
|-- legacy-command-shims/   # Opt-in archive for retired shims such as /tdd and /eval
|   |-- tdd.md              # /tdd - Prefer the tdd-workflow skill
|   |-- e2e.md              # /e2e - Prefer the e2e-testing skill
|   |-- eval.md             # /eval - Prefer the eval-harness skill
|   |-- verify.md           # /verify - Prefer the verification-loop skill
|   |-- orchestrate.md      # /orchestrate - Prefer dmux-workflows or multi-workflow
|
|-- rules/            # Always-follow guidelines (copy to ~/.claude/rules/ecc/)
|   |-- README.md            # Structure overview and installation guide
|   |-- common/              # Language-agnostic principles
|   |   |-- coding-style.md    # Immutability, file organization
|   |   |-- git-workflow.md    # Commit format, PR process
|   |   |-- testing.md         # TDD, 80% coverage requirement
|   |   |-- performance.md     # Model selection, context management
|   |   |-- patterns.md        # Design patterns, skeleton projects
|   |   |-- hooks.md           # Hook architecture, TodoWrite
|   |   |-- agents.md          # When to delegate to subagents
|   |   |-- security.md        # Mandatory security checks
|   |-- typescript/          # TypeScript/JavaScript specific
|   |-- python/              # Python specific
|   |-- golang/              # Go specific
|   |-- swift/               # Swift specific
|   |-- php/                 # PHP specific
|   |-- arkts/               # HarmonyOS / ArkTS specific
|
|-- hooks/            # Trigger-based automations
|   |-- README.md                 # Hook documentation, recipes, and customization guide
|   |-- hooks.json                # All hooks config (PreToolUse, PostToolUse, Stop, etc.)
|   |-- memory-persistence/       # Session lifecycle hooks (Longform Guide)
|   |-- strategic-compact/        # Compaction suggestions (Longform Guide)
|
|-- scripts/          # Cross-platform Node.js scripts
|   |-- lib/                     # Shared utilities
|   |   |-- utils.js             # Cross-platform file/path/system utilities
|   |   |-- package-manager.js   # Package manager detection and selection
|   |-- hooks/                   # Hook implementations
|   |   |-- session-start.js     # Load context on session start
|   |   |-- session-end.js       # Save state on session end
|   |   |-- pre-compact.js       # Pre-compaction state saving
|   |   |-- suggest-compact.js   # Strategic compaction suggestions
|   |   |-- evaluate-session.js  # Extract patterns from sessions
|   |-- setup-package-manager.js # Interactive PM setup
|
|-- tests/            # Test suite
|   |-- lib/                     # Library tests
|   |-- hooks/                   # Hook tests
|   |-- run-all.js               # Run all tests
|
|-- contexts/         # Dynamic system prompt injection contexts (Longform Guide)
|   |-- dev.md              # Development mode context
|   |-- review.md           # Code review mode context
|   |-- research.md         # Research/exploration mode context
|
|-- examples/         # Example configurations and sessions
|   |-- CLAUDE.md             # Example project-level config
|   |-- user-CLAUDE.md        # Example user-level config
|   |-- saas-nextjs-CLAUDE.md   # Real-world SaaS (Next.js + Supabase + Stripe)
|   |-- go-microservice-CLAUDE.md # Real-world Go microservice (gRPC + PostgreSQL)
|   |-- django-api-CLAUDE.md      # Real-world Django REST API (DRF + Celery)
|   |-- laravel-api-CLAUDE.md     # Real-world Laravel API (PostgreSQL + Redis)
|   |-- rust-api-CLAUDE.md        # Real-world Rust API (Axum + SQLx + PostgreSQL)
|
|-- mcp-configs/      # MCP server configurations
|   |-- mcp-servers.json    # GitHub, Supabase, Vercel, Railway, etc.
|
|-- ecc_dashboard.py  # Desktop GUI dashboard (Tkinter)
|
|-- marketplace.json  # Self-hosted marketplace config (for /plugin marketplace add)
```
#### **Dashboard GUI**

Launch the desktop dashboard to visually explore ECC components:

```
npm run dashboard
### or
python3 ./ecc_dashboard.py
```
**Features:**

- Tabbed interface: Agents, Skills, Commands, Rules, Settings
- Dark/Light theme toggle
- Font customization (family and size)
- Project logo in header and taskbar
- Search and filter across all components

#### **Skill Creator: generate skills from your git history**

Two ways to generate skills from your repository:

Use the `/skill-create` command for local analysis without external services:

```
/skill-create                    # Analyze current repo
/skill-create --instincts        # Also generate instincts for continuous-learning-v2
```
This analyzes your git history locally and generates SKILL.md files.

For advanced features (10k+ commits, auto-PRs, team sharing):

Install ECC Tools GitHub App | ecc.tools

```
### Comment on any issue:
/ecc-tools analyze
```
Both options create:

- **SKILL.md files** : Ready-to-use skills for the active harness
- **Instinct collections** : For continuous-learning-v2
- **Pattern extraction** : Learns from your commit history

#### **AgentShield: security auditor for agent configs**

Built at the Claude Code Hackathon (Cerebral Valley x Anthropic, Feb 2026). 1282 tests, 98% coverage, 102 static analysis rules.


Scan your agent configuration for vulnerabilities, misconfigurations, and injection risks.

```
### Quick scan (no install needed)
npx ecc-agentshield scan
### Auto-fix safe issues
npx ecc-agentshield scan --fix
### Deep analysis with three Opus 4.6 agents
npx ecc-agentshield scan --opus --stream
### Generate secure config from scratch
npx ecc-agentshield init
```
**What it scans:** CLAUDE.md, settings.json, MCP configs, hooks, agent definitions, and skills across 5 categories: secrets detection (14 patterns), permission auditing, hook injection analysis, MCP server risk profiling, and agent config review.

**The `--opus` flag** runs three Claude Opus 4.6 agents in a red-team/blue-team/auditor pipeline. The attacker finds exploit chains, the defender evaluates protections, and the auditor synthesizes both into a prioritized risk assessment. Adversarial reasoning, not just pattern matching.

**Output formats:** Terminal (color-graded A-F), JSON (CI pipelines), Markdown, HTML. Exit code 2 on critical findings for build gates.

Use `/security-scan` in Claude Code to run it, or add to CI with the GitHub Action.

#### **Continuous Learning v2: instincts**

The instinct-based learning system automatically learns your patterns:

```
/instinct-status        # Show learned instincts with confidence
/instinct-import <file> # Import instincts from others
/instinct-export        # Export your instincts for sharing
/evolve                 # Cluster related instincts into skills
```
See `skills/continuous-learning-v2/` for full documentation. Keep `continuous-learning/` only when you explicitly want the legacy v1 Stop-hook learned-skill flow.

#### **Agents, skills, hooks, and rules explained**

Subagents handle delegated tasks with limited scope. Example:

```
---
name: code-reviewer
description: Reviews code for quality, security, and maintainability
tools: Read, Grep, Glob, Bash
model: opus
---
You are a senior code reviewer...
```
Skills are the primary workflow surface. They can be invoked directly, suggested automatically, and reused by agents. ECC still ships maintained `commands/` during migration, while retired short-name shims live under `legacy-command-shims/` for explicit opt-in only. New workflow development should land in `skills/` first.

```
### TDD Workflow
1. Define interfaces first
2. Write failing tests (RED)
3. Implement minimal code (GREEN)
4. Refactor (IMPROVE)
5. Verify 80%+ coverage
```
Hooks fire on tool events. Example: warn about console.log:

```
{
  "matcher": "tool == \"Edit\" && tool_input.file_path matches \"\\\\.(ts|tsx|js|jsx)$\"",
  "hooks": [{
    "type": "command",
    "command": "#!/bin/bash\ngrep -n 'console\\.log' \"$file_path\" && echo '[Hook] Remove console.log' >&2"
  }]
}
```
Rules are always-follow guidelines, organized into `common/` (language-agnostic) + language-specific directories:

```
rules/
  common/          # Universal principles (always install)
  typescript/      # TS/JS specific patterns and tools
  python/          # Python specific patterns and tools
  golang/          # Go specific patterns and tools
  swift/           # Swift specific patterns and tools
  php/             # PHP specific patterns and tools
  arkts/           # HarmonyOS / ArkTS patterns and constraints
```
See `rules/README.md` for installation and structure details.

ECC's core Node.js CLI and managed installers run on **Windows, macOS, and Linux**, but optional capabilities are not at full parity. Some continuous-learning, GAN, and orchestration paths still require Bash or Python; harnesses also expose different hook, agent, and skill APIs.

| Platform | Status | Current limitation | 
|---|---|---|
| Linux | Supported core | Optional features may require Bash, Python, or provider-specific tools. | 
| macOS | Supported core | The standalone GAN shell path is not compatible with the system Bash 3.2 and currently has a score-parsing defect (#2674). | 
| Windows + WSL | Supported core | WSL follows the Linux paths; Windows host integrations still vary by harness. | 
| Windows native | Supported with limitations | Continuous-learning v2's observer daemon and memory-vault writes have open native-Windows defects (#2489, #2626). Shell-backed optional features require Git Bash/WSL or are unavailable. | 

Treat `stable`, `beta`, `experimental`, and `instruction-only` below as capability statements, not marketing tiers.

#### **Package manager detection**

The plugin automatically detects your preferred package manager (npm, pnpm, yarn, or bun) with the following priority:

1. **Environment variable** :`CLAUDE_PACKAGE_MANAGER`
2. **Project config** :`.claude/package-manager.json`
3. **package.json** :`packageManager` field
4. **Lock file** : Detection from package-lock.json, yarn.lock, pnpm-lock.yaml, or bun.lockb
5. **Global config** :`~/.claude/package-manager.json`
6. **Fallback** : First available package manager

To set your preferred package manager:

```
### Via environment variable
export CLAUDE_PACKAGE_MANAGER=pnpm
### Via global config
node scripts/setup-package-manager.js --global pnpm
### Via project config
node scripts/setup-package-manager.js --project bun
### Detect current setting
node scripts/setup-package-manager.js --detect
```
Or use the `/setup-pm` command.

#### **Hook runtime controls (env vars)**

Use runtime flags to tune strictness or disable specific hooks temporarily:

```
### Hook strictness profile (default: standard)
export ECC_HOOK_PROFILE=standard
### Comma-separated hook IDs to disable
export ECC_DISABLED_HOOKS="pre:bash:tmux-reminder,post:edit:typecheck"
### Cap SessionStart additional context (default: 8000 chars)
export ECC_SESSION_START_MAX_CHARS=4000
### Disable SessionStart additional context entirely for low-context/local-model setups
export ECC_SESSION_START_CONTEXT=off
### Session-tmp retention window in days (default: 30).
### Set to 0, off, false, disabled, never, or none to keep all sessions (disable pruning).
export ECC_SESSION_RETENTION_DAYS=14
### Cap how many learned instincts SessionStart injects into context (default: 6)
export ECC_MAX_INJECTED_INSTINCTS=6
### Minimum confidence an instinct needs to be injected, 0-1 (default: 0.7)
export ECC_INSTINCT_CONFIDENCE_THRESHOLD=0.7
### SessionStart ranks injected instincts by confidence + project/stack relevance
### (default: on). Project-scoped instincts, and instincts whose domain/trigger
### matches the detected stack (languages, frameworks, plus terraform/dbt markers),
### get a small ranking boost so they surface above unrelated higher-confidence
### ones. Set to off/false/0/no to rank by confidence alone.
export ECC_INSTINCT_RELEVANCE_RANKING=on
### Keep context/scope/loop warnings but suppress API-rate cost estimates
export ECC_CONTEXT_MONITOR_COST_WARNINGS=off
```
Windows PowerShell:

```
[Environment]::SetEnvironmentVariable('ECC_CONTEXT_MONITOR_COST_WARNINGS', 'off', 'User')
[Environment]::SetEnvironmentVariable('ECC_SESSION_RETENTION_DAYS', '14', 'User')
```
#### **Agent data home (multi-harness isolation)**

Memory persistence hooks (session summaries, learned skills, session aliases, metrics) store data under a single agent data root. By default that root is `~/.claude`. When you use ECC in both Claude Code and Cursor on the same machine, set a separate root for Cursor so the two environments do not overwrite each other's session files:

```
### Cursor-only boundary (Claude Code keeps the default ~/.claude)
export ECC_AGENT_DATA_HOME="$HOME/.cursor/ecc"
```
Paths resolved under that root include:

- `$ECC_AGENT_DATA_HOME/session-data/` : session summaries
- `$ECC_AGENT_DATA_HOME/skills/learned/` : learned skills from evaluate-session
- `$ECC_AGENT_DATA_HOME/session-aliases.json` : session aliases
- `$ECC_AGENT_DATA_HOME/metrics/` : cost and activity metrics

See affaan-m/ECC#2065.

| Harness | Status | Recommended distribution | Important limitation | 
|---|---|---|---|
| Claude Code | Stable primary | Plugin or selective installer | The plugin advertises the installed catalog to the model; use a selective/manual profile when context footprint matters. Optional shell-backed skills are not portable to every OS. | 
| Codex | Supported native plugin | Codex marketplace plugin or repo config | Native hooks require an explicit trust decision and do not use Claude's hook profiles. The legacy sync is compatibility-only. | 
| Cursor | Beta project adapter | Selective installer into `.cursor/` | Agent discovery varies by Cursor build, and ECC's installer paths do not yet expose identical hook sets (#2419). | 
| OpenCode | Beta built plugin | Build plugin, then selective installer | ECC ships a subset of the catalog; connect a provider and select a model in OpenCode (#2617). | 
| GitHub Copilot | Instruction-only | Checked-in instructions and prompt files | No ECC hooks, runtime agents, delegation, or native skill discovery. | 
| Gemini, Zed, Antigravity, Qwen, Hermes, OpenClaw, Kimi, CodeBuddy, JoyCode | Experimental/minimal adapters | Harness-specific selective target | File placement and instruction portability are tested; full Claude feature parity is not claimed. | 

| Capability | Claude Code | Codex | Cursor | OpenCode | GitHub Copilot | 
|---|---|---|---|---|---|
| Instructions | Native | Native `AGENTS.md` | Project rules | Plugin instructions | Native instruction file | 
| Skills | Native installed set | Native plugin set | Build-dependent/project set | Built subset | Prompt/instruction references only | 
| Agents/delegation | Native agents | Codex multi-agent roles; Claude agent files are not installed as roles | Build-dependent project agents | Plugin agents | Not supported | 
| ECC hooks | Native plugin hooks | Native reviewed subset with explicit trust | Cursor hook adapter; install-path differences remain | Plugin events | Not supported | 
| MCP configuration | Available, explicit activation | Native plugin manifest; legacy sync can merge TOML | Explicit project/user config | Provider/plugin config | Not supplied by ECC | 
| Parity with Claude Code | Primary reference | Partial | Partial | Partial | Not a parity target | 

**Key architectural decisions:**

- **AGENTS.md** at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitHub Copilot uses`.github/copilot-instructions.md` instead)
- **DRY adapter pattern** lets Cursor reuse Claude Code's hook scripts without duplication
- **Skills format** (SKILL.md with YAML frontmatter) works across Claude Code, Codex, and OpenCode
- Codex's narrower native hook set is supplemented by `AGENTS.md` , optional`model_instructions_file` overrides, and sandbox permissions

#### **Cursor IDE support in depth**

ECC provides Cursor IDE support with hooks, rules, agents, skills, commands, and MCP configs adapted for Cursor's project layout.

```
### macOS/Linux
./install.sh --target cursor typescript
./install.sh --target cursor python golang swift php
```
```
### Windows PowerShell
.\install.ps1 --target cursor typescript
.\install.ps1 --target cursor python golang swift php
```
| Component | Count | Details | 
|---|---|---|
| Hook Events | 15 | sessionStart, beforeShellExecution, afterFileEdit, beforeMCPExecution, beforeSubmitPrompt, and 10 more | 
| Hook Scripts | 16 | Thin Node.js scripts delegating to `scripts/hooks/` via shared adapter | 
| Rules | 34 | 9 common (alwaysApply) + 25 language-specific (TypeScript, Python, Go, Swift, PHP) | 
| Agents | 48 | `.cursor/agents/ecc-*.md` when installed; prefixed to avoid collisions with user or marketplace agents | 
| Skills | Shared + Bundled | `.cursor/skills/` for translated additions | 
| Commands | Shared | `.cursor/commands/` if installed | 
| MCP Config | Shared | `.cursor/mcp.json` if installed | 

ECC does not install root `AGENTS.md` into `.cursor/`. Cursor treats nested `AGENTS.md` files as directory context, so copying ECC's repo identity into a host project would pollute that project.

Cursor-native loading behavior can vary by Cursor build. ECC installs agents as `.cursor/agents/ecc-*.md`; if your Cursor build does not expose project agents, those files still work as explicit reference definitions instead of hidden global prompt context.

ECC memory hooks reuse the same `scripts/hooks/*.js` as Claude Code. For Cursor, ECC tries to keep memory **out of `~/.claude` automatically**:

1. **Cursor `sessionStart` hook** (installed to`.cursor/hooks.json` on`--target cursor` ) injects`ECC_AGENT_DATA_HOME` for the whole composer session.
2. **Hook runtime default** : when`CURSOR_VERSION` or`CURSOR_PROJECT_DIR` is present, hooks default to`~/.cursor/ecc` if the env var is unset.
3. **Project config** :`.cursor/ecc-agent-data.json` documents and overrides the path (`agentDataHome` ).
4. **Always-on rule** :`.cursor/rules/ecc-agent-data-home.mdc` reminds the agent where memory lives.

You can still override explicitly:

`export ECC_AGENT_DATA_HOME="$HOME/.cursor/ecc"`
To **share** memory with Claude Code on purpose, set `ECC_AGENT_DATA_HOME=~/.claude` in the shell or in `.cursor/ecc-agent-data.json`.

Continuous learning v2 instincts remain separate under `CLV2_HOMUNCULUS_DIR` (default `~/.local/share/ecc-homunculus`).

Cursor has **more hook events than Claude Code** (20 vs 8). The `.cursor/hooks/adapter.js` module transforms Cursor's stdin JSON to Claude Code's format, allowing existing `scripts/hooks/*.js` to be reused without duplication.

```
Cursor stdin JSON -> adapter.js -> transforms -> scripts/hooks/*.js
                                                (shared with Claude Code)
```
Key hooks:

- **beforeShellExecution** : Blocks dev servers outside tmux (exit 2), git push review
- **afterFileEdit** : Auto-format + TypeScript check + console.log warning
- **beforeSubmitPrompt** : Detects secrets (sk-, ghp_, AKIA patterns) in prompts
- **beforeTabFileRead** : Blocks Tab from reading .env, .key, .pem files (exit 2)
- **beforeMCPExecution / afterMCPExecution** : MCP audit logging

Cursor rules use YAML frontmatter with `description`, `globs`, and `alwaysApply`:

```
---
description: "TypeScript coding style extending common rules"
globs: ["**/*.ts", "**/*.tsx", "**/*.js", "**/*.jsx"]
alwaysApply: false
---
```
#### **Codex macOS app + CLI support in depth**

ECC provides a supported native Codex marketplace plugin and repo-local configuration for the macOS app and CLI. The native plugin carries shared skills, MCP configuration, and a reviewed hook subset; Codex keeps hook trust under explicit user control. The older sync path remains compatibility-only. For repo navigation, surface ownership, and PR diff packet guidance, start with `docs/CODEX-NAVIGATION-GUIDE.md`.

```
### Recommended current install: add ECC's native plugin from the repo marketplace
codex plugin marketplace add affaan-m/ECC
codex plugin add ecc@ecc
codex plugin list --json
### Or run Codex CLI in the repo: AGENTS.md and .codex/ are auto-detected
codex
```
Legacy copied-configuration compatibility is still available when you intentionally need it:

```
### Compatibility-only managed sync into ~/.codex
npm install && bash scripts/sync-ecc-to-codex.sh
### Or copy only the reference config manually
cp .codex/config.toml ~/.codex/config.toml
```
The sync script safely merges ECC MCP servers into your existing `~/.codex/config.toml` using an **add-only** strategy: it never removes or modifies your existing servers. Run with `--dry-run` to preview changes, or `--update-mcp` to force-refresh ECC servers to the latest recommended config.

For Context7, ECC uses the canonical Codex section name `[mcp_servers.context7]` while still launching the `@upstash/context7-mcp` package. If you already have a legacy `[mcp_servers.context7-mcp]` entry, `--update-mcp` migrates it to the canonical section name.

Codex macOS app:

- Open this repository as your workspace.
- The root `AGENTS.md` is auto-detected.
- `.codex/config.toml` and`.codex/agents/*.toml` work best when kept project-local.
- The reference `.codex/config.toml` intentionally does not pin`model` or`model_provider` , so Codex uses its own current default unless you override it.
- Optional: copy `.codex/config.toml` to`~/.codex/config.toml` for global defaults; keep the multi-agent role files project-local unless you also copy`.codex/agents/` .

| Component | Count | Details | 
|---|---|---|
| Config | 1 | `.codex/config.toml` : top-level approvals/sandbox/web_search, MCP servers, notifications, profiles | 
| AGENTS.md | 2 | Root (universal) + `.codex/AGENTS.md` (Codex-specific supplement) | 
| Skills | 32 | `.agents/skills/` : SKILL.md + agents/openai.yaml per skill | 
| MCP Servers | 6 | GitHub, Context7, Exa, Memory, Playwright, Sequential Thinking (7 with Supabase via `--update-mcp` sync) | 
| Profiles | 2 | `strict` (read-only sandbox) and`yolo` (full auto-approve) | 
| Agent Roles | 3 | `.codex/agents/` : explorer, reviewer, docs-researcher | 

Skills at `.agents/skills/` are auto-loaded by Codex. Canonical Anthropic skills such as `claude-api`, `frontend-design`, and `skill-creator` are intentionally not re-bundled here. Install those from `anthropics/skills` when you want the official versions.

Codex does **not provide Claude-style hook execution parity**. The native ECC plugin includes a reviewed hook subset that requires explicit trust in `/hooks`; `AGENTS.md`, optional `model_instructions_file` overrides, and sandbox/approval settings provide the remaining instruction and policy layers.

Current Codex builds support stable multi-agent workflows.

- Enable `features.multi_agent = true` in`.codex/config.toml`
- Define roles under `[agents.<name>]`
- Point each role at a file under `.codex/agents/`
- Use `/agent` in the CLI to inspect or steer child agents

ECC ships three sample role configs:

| Role | Purpose | 
|---|---|
| `explorer` | Read-only codebase evidence gathering before edits | 
| `reviewer` | Correctness, security, and missing-test review | 
| `docs_researcher` | Documentation and API verification before release/docs changes | 

#### **Zed support**

ECC provides Zed project support through a conservative `.zed` adapter for project-local settings, flattened rules, agents, commands, and skills.

`./install.sh --profile minimal --target zed``.\install.ps1 --profile minimal --target zed`
The adapter writes ECC-managed files under `.zed/` and keeps BYOK/OpenRouter credentials out of the repo. Configure Zed account or API keys through Zed's own settings UI or your local user settings.

#### **OpenCode support in depth**

ECC provides a beta OpenCode plugin integration with instructions, a catalog subset, commands, custom tools, and hook events. It does not provide feature parity with Claude Code. The reference config inherits the user's OpenCode model selection instead of pinning a provider-specific model.

```
### Install OpenCode
npm install -g opencode
### Run in the repository root
opencode
```
The configuration is automatically detected from `.opencode/opencode.json`.

OpenCode's plugin system has 20+ event types:

| Claude Code Hook | OpenCode Plugin Event | 
|---|---|
| PreToolUse | `tool.execute.before` | 
| PostToolUse | `tool.execute.after` | 
| Stop | `session.idle` | 
| SessionStart | `session.created` | 
| SessionEnd | `session.deleted` | 

**Additional OpenCode events**: `file.edited`, `file.watcher.updated`, `message.updated`, `lsp.client.diagnostics`, `tui.toast.show`, and more.

**Option 1: Use directly**

```
cd ECC
opencode
```
**Option 2: Install as npm package**

`npm install ecc-universal`
Then add to your `opencode.json`:

```
{
  "plugin": ["ecc-universal"]
}
```
That npm plugin entry enables ECC's published OpenCode plugin module (hooks/events and plugin tools). It does **not** automatically add ECC's full command/agent/instruction catalog to your project config.

For the full ECC OpenCode setup, either:

- run OpenCode inside this repository, or
- copy the bundled `.opencode/` config assets into your project and wire the`instructions` ,`agent` , and`command` entries in`opencode.json`

- **Migration Guide** :`.opencode/MIGRATION.md`
- **OpenCode Plugin README** :`.opencode/README.md`
- **Consolidated Rules** :`.opencode/instructions/INSTRUCTIONS.md`
- **LLM Documentation** :`llms.txt` (complete OpenCode docs for LLMs)

#### **GitHub Copilot support in depth**

ECC provides **GitHub Copilot support** for VS Code via Copilot Chat's native instruction and prompt file system. No extra tooling required.

| Component | File | Purpose | 
|---|---|---|
| Core instructions | `.github/copilot-instructions.md` | Always-loaded rules: coding style, security, testing, git workflow | 
| VS Code settings | `.vscode/settings.json` | Per-task instruction files for code gen, test gen, and commit messages | 
| Plan prompt | `.github/prompts/plan.prompt.md` | Phased implementation planning | 
| TDD prompt | `.github/prompts/tdd.prompt.md` | Red-Green-Improve cycle | 
| Security review prompt | `.github/prompts/security-review.prompt.md` | Deep OWASP-aligned security analysis | 
| Build fix prompt | `.github/prompts/build-fix.prompt.md` | Systematic build and CI error resolution | 
| Refactor prompt | `.github/prompts/refactor.prompt.md` | Dead code cleanup and simplification | 

The files are already in place: open any repo that contains this project and GitHub Copilot Chat will automatically pick up `.github/copilot-instructions.md`. The committed `.vscode/settings.json` enables `chat.promptFiles` so VS Code can load the reusable prompts from `.github/prompts/`.

To use the workflow prompts in Copilot Chat:

1. Open the Copilot Chat panel in VS Code.
2. Click the **paperclip / attach** icon and select**Prompt...** , or type`/` and choose a prompt.
3. Select the prompt (e.g. `plan` ,`tdd` ,`security-review` ).

| ECC Feature | Copilot equivalent | 
|---|---|
| Coding standards | Always-on via `copilot-instructions.md` | 
| Security checklist | Always-on + `security-review` prompt | 
| Testing / TDD | Always-on + `tdd` prompt | 
| Implementation planning | `plan` prompt | 
| Code review | External PR review via CodeRabbit + Greptile | 
| Build error resolution | `build-fix` prompt | 
| Refactoring | `refactor` prompt | 
| Commit message format | Per-task instruction in `settings.json` | 
| Hooks / automation | Not supported (Copilot has no hook system) | 
| Agents / delegation | Not supported (Copilot has no subagent API) | 

GitHub Copilot does not have a hook system or a subagent API, so ECC's hook automations (auto-format, TypeScript check, session persistence, dev-server guard) and agent delegation are unavailable. The instruction and prompt layer still brings the full ECC coding philosophy (standards, security, TDD, and workflow) into every Copilot Chat session.

#### **What changed in v2.0.0**

ECC v2.0.0 stabilizes the 2.0 line with the public Hermes operator story, 281 skills, 67 agents, 94 command shims, session adapters, MCP inventory, worktree lifecycle services, orchestrator workflows, and the ECC Discord community.

Agent usage can be expensive if you don't manage token consumption. These settings significantly reduce costs without sacrificing quality. Full guide: docs/token-optimization.md.

#### **Recommended settings**

Add to `~/.claude/settings.json`:

```
{
  "model": "sonnet",
  "env": {
    "MAX_THINKING_TOKENS": "10000",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50",
    "CLAUDE_CODE_SUBAGENT_MODEL": "haiku"
  }
}
```
| Setting | Default | Recommended | Impact | 
|---|---|---|---|
| `model` | opus | **sonnet** | ~60% cost reduction; handles 80%+ of coding tasks | 
| `MAX_THINKING_TOKENS` | 31,999 | **10,000** | ~70% reduction in hidden thinking cost per request | 
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | 95 | **50** | Compacts earlier, better quality in long sessions | 
| `ECC_CONTEXT_MONITOR_COST_WARNINGS` | on | **off for subscription users** | Suppresses agent-facing API-rate estimate warnings while keeping context/scope/loop warnings | 

Switch to Opus only when you need deep architectural reasoning:

```
/model opus
```
#### **Daily workflow commands**

| Command | When to Use | 
|---|---|
| `/model sonnet` | Default for most tasks | 
| `/model opus` | Complex architecture, debugging, deep reasoning | 
| `/clear` | Between unrelated tasks (free, instant reset) | 
| `/compact` | At logical task breakpoints (research done, milestone complete) | 
| `/cost` | Monitor token spending during session | 

If you use a subscription and the context monitor's API-rate estimates are not useful, set `ECC_CONTEXT_MONITOR_COST_WARNINGS=off`. This only suppresses the agent-facing cost warnings; it does not disable context exhaustion, scope, or loop warnings.

#### **Strategic compaction**

The `strategic-compact` skill suggests `/compact` at logical breakpoints instead of relying on auto-compaction at 95% context. See `skills/strategic-compact/SKILL.md` for the full decision guide.

**When to compact:**

- After research/exploration, before implementation
- After completing a milestone, before starting the next
- After debugging, before continuing feature work
- After a failed approach, before trying a new one

**When NOT to compact:**

- Mid-implementation (you'll lose variable names, file paths, partial state)

#### **Context window management**

**Critical:** Don't enable all MCPs at once. Each MCP tool description consumes tokens from your 200k window, potentially reducing it to ~70k.

- Keep under 10 MCPs enabled per project
- Keep under 80 tools active
- Use `/mcp` to disable unused Claude Code MCP servers; those runtime choices persist in`~/.claude.json`
- Use `ECC_DISABLED_MCPS` only to filter ECC-generated MCP configs during install/sync flows
- If context is getting heavy, run `/context-budget` and remove rules you do not need

**Agent teams cost warning:** Agent Teams spawns multiple context windows. Each teammate consumes tokens independently. Only use for tasks where parallelism provides clear value (multi-module work, parallel reviews). For simple sequential tasks, subagents are more token-efficient.

#### **Claude Code CLI version + hooks auto-loading behavior**

**Minimum version: v2.1.0 or later.** The plugin requires Claude Code CLI v2.1.0+ due to changes in how the plugin system handles hooks.

Check your version:

`claude --version`
WARNING: **For Contributors:** Do NOT add a `"hooks"` field to `.claude-plugin/plugin.json`. This is enforced by a regression test.


Claude Code v2.1+ **automatically loads** `hooks/hooks.json` from any installed plugin by convention. Explicitly declaring it in `plugin.json` causes a duplicate detection error:

```
Duplicate hooks file detected: ./hooks/hooks.json resolves to already-loaded file
```
**History:** This has caused repeated fix/revert cycles in this repo (#29, #52, #103). The behavior changed between Claude Code versions, leading to confusion. There is now a regression test to prevent this from being reintroduced.

Install ECC only from official sources:

- GitHub repository: https://github.com/affaan-m/ECC
- Claude Code plugin: `ecc@ecc`
- npm packages: `ecc-universal` and`ecc-agentshield`
- GitHub App: https://github.com/apps/ecc-tools
- Website: https://ecc.tools

Scan a project with AgentShield:

`npx -y ecc-agentshield scan --path .`
- **Report a vulnerability.** Use the private process in SECURITY.md (GitHub private vulnerability reporting). Please do not open public issues for security reports.
- **Built-in guardrails.** GateGuard gates destructive shell commands (including`rm` , force/path`git checkout` , and destructive`find -exec` ) before they run; the supply-chain IOC scanner runs in CI; and AgentShield audits your own agent, hook, MCP, permission, and secret surfaces (`/security-scan` ).

#### **Hooks, MCP servers, and context controls**

Hooks can run shell commands, MCP servers can hold credentials, and project instructions can enter an agent's context. Treat all three as executable configuration.

Do not copy raw `hooks/hooks.json` into `~/.claude/settings.json` after a plugin install. Modern Claude Code versions load plugin hooks automatically, and a second copy can make them fire twice.

Use `/mcp` for Claude Code runtime disables; Claude Code persists those choices in `~/.claude.json`.

`ECC_DISABLED_MCPS` is an ECC install/sync filter, not a live Claude Code toggle.

If context is getting heavy, run `/context-budget`, remove rules you do not need, and disable unused MCP servers. See the token optimization guide.

Security references:

#### **ECC appears twice or hooks fire twice**

The usual cause is installing the Claude plugin and then running `./install.sh --profile full` on top of it.

1. Remove the Claude Code plugin install.
2. Run `node scripts/ecc.js uninstall --dry-run` from the ECC checkout.
3. Remove extra rule folders you manually copied and no longer want.
4. Reinstall once, using one path.

For hook-specific checks, see the hooks README.

#### **My hooks aren't working / "Duplicate hooks file" errors**

**Do NOT add a `"hooks"` field to `.claude-plugin/plugin.json`.** Claude Code v2.1+ automatically loads `hooks/hooks.json` from installed plugins. Explicitly declaring it causes duplicate detection errors. See #29, #52, #103.

#### **Codex marketplace installs but skills do not load**

Run the cache check from an ECC checkout:

`node scripts/codex/check-plugin-cache.js`
If it reports unresolved parent references, refresh the native cache with `codex plugin marketplace upgrade ecc`, run `codex plugin add ecc@ecc` again, and restart Codex. Registration in `codex plugin list` confirms the marketplace entry, while the cache check verifies that the installed manifest can resolve its skills, MCP configuration, and assets. Use `bash scripts/sync-ecc-to-codex.sh` only when you intentionally need the legacy copied-configuration compatibility path.

#### **My context window is shrinking**

Too many MCP servers eat your context. Each MCP tool description consumes tokens from your 200k window, potentially reducing it to ~70k. SessionStart context is capped at 8000 characters by default; lower it with `ECC_SESSION_START_MAX_CHARS=4000` or disable it with `ECC_SESSION_START_CONTEXT=off` for local-model or low-context setups.

**Fix:** Disable unused MCPs from Claude Code with `/mcp`. Claude Code writes those runtime choices to `~/.claude.json`; `.claude/settings.json` and `.claude/settings.local.json` are not reliable toggles for already-loaded MCP servers.

Keep under 10 MCPs enabled and under 80 tools active.

#### **Can I use only some components (e.g., just agents)?**

Yes. Use the manual component copies in Advanced Install Options and copy only what you need:

```
### Just agents
cp agents/*.md ~/.claude/agents/
### Just rules
mkdir -p ~/.claude/rules/ecc/
cp -r rules/common ~/.claude/rules/ecc/
```
Each component is fully independent.

#### **Does this work with Cursor / OpenCode / Codex / Antigravity / GitHub Copilot?**

Yes. ECC is cross-platform:

- **Cursor** : Pre-translated configs in`.cursor/` . See Platform Support.
- **Gemini CLI** : Experimental project-local support via`.gemini/GEMINI.md` and shared installer plumbing.
- **OpenCode** : Beta plugin integration in`.opencode/` ; models follow the user's OpenCode selection, while catalog parity remains limited.
- **Codex** : Supported native marketplace plugin for the app and CLI, plus repo-local configuration. The older sync flow remains available only for compatibility.
- **GitHub Copilot (VS Code)** : Instruction and prompt layer via`.github/copilot-instructions.md` ,`.vscode/settings.json` , and`.github/prompts/` .
- **Antigravity** : Native Antigravity 2.0 setup for workflows, skills, custom agents, and flattened rules in`.agents/` . See Antigravity Guide.
- **JoyCode / CodeBuddy** : Project-local selective install adapters for commands, agents, skills, and flattened rules. See JoyCode Adapter Guide.
- **Qwen CLI** : Home-directory selective install adapter for commands, agents, skills, rules, and Qwen config. See Qwen CLI Adapter Guide.
- **Zed** : Project-local selective install adapter for`.zed/settings.json` , flattened rules, commands, agents, and skills.
- **Non-native harnesses** : Manual fallback path for chat-style interfaces. See Manual Adaptation Guide.
- **Claude Code** : Native. This is the primary target.

#### **My platform is not listed**

Use the manual adaptation guide, or open a GitHub discussion with the harness name and the file, skill, command, and hook formats it supports.

The plugin includes a comprehensive test suite:

```
### Run all tests
node tests/run-all.js
### Run individual test files
node tests/lib/utils.test.js
node tests/lib/package-manager.test.js
node tests/hooks/hooks.test.js
```
I've been using Claude Code since the experimental rollout. Won the Anthropic x Forum Ventures hackathon in Sep 2025 with @DRodriguezFX, built zenith.chat entirely with agentic workflows.

These configs are battle-tested across multiple production applications.

#### **Sponsors and ECC Pro**

ECC stays free because sponsors and Pro users fund the work. Sponsor logos are at the top of this README; the full roster and tiers are in SPONSORS.md.

ECC Pro adds private-repo analysis, PR-triggered audits, AgentShield-backed scanning, automatic push and PR checks, pooled team usage, and priority support through the hosted GitHub App.

| **ECC Pro**<sub>Hosted GitHub App for private repos</sub> | **Sponsor ECC**<sub>Fund the OSS work</sub> | **Community**<sub>Q&A, ideas, and Show and Tell</sub> | **GitHub App**<sub>PR audits and hosted workflows</sub> | 

#### **Contributing**

Contributions are welcome across skills, agents, rules, hooks, docs, tests, adapters, and security improvements.

The short version:

1. Fork the repo
2. Create your skill in `skills/your-skill-name/SKILL.md` (with YAML frontmatter)
3. Or create an agent in `agents/your-agent.md`
4. Submit a PR with a clear description of what it does and when to use it

**Ideas for contributions:**

- Language-specific skills (Rust, C#, Kotlin, Java): Go, Python, Perl, Swift, TypeScript, and HarmonyOS/ArkTS already included
- Framework-specific configs (Rails, FastAPI): Django, NestJS, Spring Boot, and Laravel already included
- DevOps agents (Kubernetes, Terraform, AWS, Docker)
- Testing strategies (different frameworks, visual regression)
- Domain-specific knowledge (ML, data engineering, mobile)

- **Shorthand Guide (Start Here):** The Shorthand Guide to ECC
- **Longform Guide (Advanced):** The Longform Guide to ECC
- **Security Guide:** Security Guide | Thread
- **Follow:** @affaan

MIT. Use it freely, adapt it to your workflow, and contribute back when you can.

**Star this repo if it helps. Read the guides. Build something great.**

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
