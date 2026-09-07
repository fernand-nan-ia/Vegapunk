---
item_id: "5ce5cb53-1f16-447e-88b5-f22be8d2a3cd"
platform: article
external_id: "fa4361846156"
canonical_url: "https://github.com/pbakaus/impeccable"
channel: "Pbakaus · GitHub"
captured_at: 2026-09-07
status: enriched
triage: null
tags: ["impeccable", "ai-slop", "design-com-ia", "detector-deterministico", "hooks", "ci-gate", "agent-skills", "claude-code"]
applicability:
  saas_pessoal: alta
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
theme: design-e-ux
content_type: article
---

# Impeccable (pbakaus): 23 comandos de design, 61 regras determinísticas e hook que intercepta edição

🔗 https://github.com/pbakaus/impeccable

## Resumo

Impeccable é uma skill de design para agentes de código criada por Paul Bakaus, sob licença Apache 2.0. O autor declara que partiu da skill frontend-design da Anthropic e diz por que ela não bastava: todo modelo foi treinado nos mesmos templates de SaaS, então sem orientação sai sempre o mesmo punhado de sinais — Inter em tudo, degradê roxo para azul, cartão dentro de cartão, texto cinza sobre fundo colorido e o ladrilho de ícone arredondado acima de cada título. O pacote tem três partes. Primeiro, 23 comandos numa skill só, acessados por `/impeccable <comando> <alvo>`: craft, init, document, extract, shape, critique, audit, polish, bolder, quieter, distill, harden, onboard, animate, colorize, typeset, layout, delight, overdrive, clarify, adapt, optimize e live. Segundo, um detector com 61 regras DETERMINÍSTICAS que roda sem LLM e sem chave de API, disponível como CLI (`npx impeccable detect src/`, um arquivo, ou uma URL qualquer inclusive de concorrente) e como extensão de navegador; a saída tem JSON e código de saída que reprova o build quando o slop entra num pull request. Terceiro, um hook que intercepta edições de arquivo de interface e devolve os achados ao agente — no Cursor ele BLOQUEIA a escrita ruim antes de acontecer; no Claude Code, Copilot e Codex ele reporta depois da edição. O próprio README traz um alerta de segurança relevante: no Claude Code os hooks instalados rodam INDEPENDENTEMENTE da aprovação de ferramenta pelo modelo, então a primeira edição pode baixar e cachear o binário do motor mesmo que a sessão negue o comando — e recomenda revisar hooks instalados antes de execuções não supervisionadas. Instala-se com `npx impeccable install`, que detecta os harnesses presentes, ou pelo marketplace `/plugin marketplace add pbakaus/impeccable`. Suporta mais de quinze harnesses.

## Tópicos

- **Os sinais de IA que ele combate** — Inter em tudo, degradê roxo-para-azul, cartão dentro de cartão, texto cinza sobre fundo colorido e o ladrilho de ícone arredondado acima de todo título — a lista que o autor diz sair de todo modelo sem orientação.
- **23 comandos numa skill** — De init e shape (antes de codar) a audit, critique e polish (antes de publicar), passando por typeset, layout, colorize, animate, bolder, quieter, distill, harden, clarify e live.
- **Detector determinístico** — 61 regras que rodam SEM LLM e sem chave de API, cobrindo slop (bordas laterais, degradês roxos, easing elástico, brilho escuro) e qualidade geral (comprimento de linha, área de toque pequena, títulos pulados).
- **CLI e extensão de navegador** — `npx impeccable detect` aceita diretório, arquivo ou URL — inclusive de concorrente. JSON para CI, saída 0 sem achados e 2 com achados, o que reprova o build.
- **Hook que intercepta a edição** — No Cursor bloqueia escrita ruim ANTES de acontecer; no Claude Code, Copilot e Codex reporta depois da edição, com passada mais profunda ao parar.
- **Alerta de segurança do próprio autor** — No Claude Code os hooks rodam independentemente da aprovação de ferramenta pelo modelo: a primeira edição pode baixar e cachear o binário mesmo com a sessão negando o comando. O README recomenda revisar hooks antes de execução não supervisionada.
- **Instalação e alcance** — `npx impeccable install` detecta os harnesses presentes, ou `/plugin marketplace add pbakaus/impeccable`. Suporta Claude Code, Cursor, Codex, Gemini, Copilot, Grok, Hermes, OpenCode e mais de uma dezena de outros.

## Ferramentas citadas

- **npx impeccable**: instalador e CLI do detector; casca fina sobre um binário próprio que dispensa Node em tempo de execução
- **Claude Code**: harness suportado com hook nativo instalado em .claude/settings.local.json
- **Cursor**: único harness em que o hook BLOQUEIA a escrita ruim antes de ela chegar ao arquivo
- **frontend-design (Anthropic)**: skill de design da Anthropic da qual o projeto partiu; o autor desaconselha rodar as duas juntas

## Pontos-chave

- 66.301 estrelas, Apache 2.0, push em 07/09/2026 — verificado na API no mesmo dia
- CORREÇÃO de fonte anterior: o vídeo do Felipe Borges afirma 48 estrelas para este repositório; o número real é 66.301
- As 61 regras do detector rodam SEM LLM e SEM chave de API — é a única peça do lote que não gasta nada por uso
- O detector aceita URL de terceiro: dá para auditar o site de um concorrente sem acesso ao código
- Código de saída 2 reprova o build em CI quando há achado — vira gate automático, não sugestão
- No Cursor o hook bloqueia antes da escrita; nos demais só reporta depois
- ALERTA DE SEGURANÇA do próprio README: hooks no Claude Code rodam sem passar pela aprovação de ferramenta do modelo
- O autor desaconselha explicitamente rodar Impeccable junto com a skill frontend-design da Anthropic
- Escreve arquivos de trabalho em .impeccable/ que precisam de bloco próprio no .gitignore

## Como aplicar

O caminho de menor risco não é instalar a skill: é rodar `npx impeccable detect` contra uma página já pronta. São 61 regras determinísticas, sem LLM, sem chave, sem hook — custo zero e nenhuma interferência no fluxo de trabalho. Se o resultado for útil, aí sim considerar a skill, e nunca junto com outra skill de design. O hook fica por último e exige leitura do alerta de segurança: no Claude Code ele roda fora da aprovação de ferramenta do modelo.

## 🔧 Atlas diz

Passo 1 de 3: rode `npx impeccable detect` numa página que já existe — não instala nada, não escreve nada, só aponta o que está feio e por quê. Passo 2: se prestar, instale a skill sozinha, sem outra de design junto. Passo 3, e só aí, o hook — que no Claude Code roda por fora da aprovação de ferramenta, então é parafuso que a gente só aperta olhando. Grr, e ponha o bloco do .impeccable/ no .gitignore antes, senão sujeira de execução vai parar no commit.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Design guidance for AI coding agents. 1 skill, 23 commands, live browser iteration, and 61 deterministic detector rules for AI-generated frontend design.

**Quick start:** From your project root, run `npx impeccable install`, then run `/impeccable init` inside your AI coding tool. Full docs: impeccable.style.


Anthropic's frontend-design was the first widely-used design skill for Claude. Impeccable started from there.

Every model trained on the same SaaS templates. Skip the guidance and you get the same handful of tells on every project: Inter for everything, purple-to-blue gradients, cards nested in cards, gray text on colored backgrounds, the rounded-square icon tile above every heading.

Impeccable adds:

- **One setup flow.**`/impeccable init` records durable product truth in`PRODUCT.md` , so later commands know the audience, purpose, operating context, constraints, voice, and evidence without confusing those facts with surface-level visual direction.
- **23 commands.** A shared design vocabulary with your AI:`polish` ,`audit` ,`critique` ,`distill` ,`animate` ,`bolder` ,`quieter` , and more.
- **61 deterministic detector rules** plus LLM-only critique checks. The CLI and browser extension run the deterministic rules with no LLM and no API key.

The skill installs as one command:

`/impeccable <command> <target>`
Start every new project with:

`/impeccable init`
`init` inspects the project, asks only for material gaps in durable product truth, and writes `PRODUCT.md`. Visitor mode and visual direction are chosen later for each surface; incumbent or newly built visual systems are recorded separately in `DESIGN.md`.

All commands are accessed through `/impeccable`:

| Command | What it does | 
|---|---|
| `/impeccable craft` | Full shape-then-build flow with visual iteration | 
| `/impeccable init` | One-time setup: gather durable product context, write PRODUCT.md, configure live mode when applicable, recommend next steps | 
| `/impeccable document` | Generate root DESIGN.md from existing project code | 
| `/impeccable extract` | Pull reusable components and tokens into the design system | 
| `/impeccable shape` | Plan UX/UI before writing code | 
| `/impeccable critique` | UX design review: hierarchy, clarity, emotional resonance | 
| `/impeccable audit` | Run technical quality checks (a11y, performance, responsive) | 
| `/impeccable polish` | Final pass, design system alignment, and shipping readiness | 
| `/impeccable bolder` | Amplify boring designs | 
| `/impeccable quieter` | Tone down overly bold designs | 
| `/impeccable distill` | Strip to essence | 
| `/impeccable harden` | Error handling, i18n, text overflow, edge cases | 
| `/impeccable onboard` | First-run flows, empty states, activation paths | 
| `/impeccable animate` | Add purposeful motion | 
| `/impeccable colorize` | Introduce strategic color | 
| `/impeccable typeset` | Fix font choices, hierarchy, sizing | 
| `/impeccable layout` | Fix layout, spacing, visual rhythm | 
| `/impeccable delight` | Add moments of joy | 
| `/impeccable overdrive` | Add technically extraordinary effects | 
| `/impeccable clarify` | Improve unclear UX copy | 
| `/impeccable adapt` | Adapt for different devices | 
| `/impeccable optimize` | Performance improvements | 
| `/impeccable live` | Visual variant mode: iterate on elements in the browser | 

Use `/impeccable pin <command>` to create standalone shortcuts (e.g., `pin audit` creates `/audit`).

```
/impeccable audit blog           # Audit blog hub + post pages
/impeccable critique landing     # UX design review
/impeccable polish settings      # Final pass before shipping
/impeccable harden checkout      # Add error handling + edge cases
```
Or use `/impeccable` directly with a description:

```
/impeccable redo this hero section
```
The skill includes explicit guidance on what to avoid:

- Don't use overused fonts (Arial, Inter, system defaults)
- Don't use gray text on colored backgrounds
- Don't use pure black/gray (always tint)
- Don't wrap everything in cards or nest cards inside cards
- Don't use bounce/elastic easing (feels dated)

Visit the Neo Mirai case study to see a before/after case study of a real project transformed with Impeccable commands.

The skill needs no runtime of its own. Every skill copy ships a small launcher (`scripts/impeccable`, plus `impeccable.cmd` for Windows) that runs the Impeccable engine, a self-contained binary that either sits next to the launcher or is downloaded once on first run into `~/.impeccable/bin/`. Node is only involved if you use the `npx impeccable` installer, which is a shim around the same binary; the manual and Git options below work without it.

From the root of your project, run:

`npx impeccable install`
This shows the harness folders or installed CLIs it detected (for example `~/.claude`, `~/.codex`, `~/.grok`, `~/.hermes`, `~/.veto`, or project-local `.cursor`), lets you keep the detected set or customize providers, then asks whether to install into the current project or globally. Use `--providers=claude,codex,cursor,grok,hermes,veto` and `--scope=project|global` to skip those choices in scripts. On Claude Code, Cursor, Codex, GitHub Copilot, and Grok Build, it also installs the provider-native hook manifest for the current project. Veto receives the packaged skill under `~/.veto/skills/` and does not run native Impeccable edit hooks. Works with Cursor, Claude Code, Gemini CLI, Codex CLI, Grok Build, Hermes Agent, Veto, and every other supported tool. Reload your harness afterward.

To refresh an existing install, run:

`npx impeccable update`
Codex users should open `/hooks` after install or update and approve the project hook when prompted. Codex tracks trust by hook definition, so updates that change `.codex/hooks.json` can require approval again. Grok Build users need project folder trust (`/hooks-trust` or launch with `--trust`) before `.grok/hooks/` scripts run.

See Allow the hook in your harness for harness-specific trust and verification steps.

For teams that want to keep Impeccable vendored and updated through Git, add this repo as a submodule and link the compiled provider build into your harness folders:

```
git submodule add https://github.com/pbakaus/impeccable .impeccable
npx impeccable link --source=.impeccable --providers=claude,cursor
git add .gitmodules .impeccable .claude .cursor
git commit -m "Add Impeccable skills"
```
Use the providers your project needs, for example `claude`, `cursor`, `gemini`, `codex`, `github`, `grok`, `hermes`, `opencode`, `pi`, `qoder`, `trae`, `trae-cn`, `rovo-dev`, `vibe`, or `veto`. The command links individual skill folders from `.impeccable/dist/universal/` and leaves existing real skill directories untouched unless you pass `--force`.

To update later:

```
git submodule update --remote .impeccable
npx impeccable link --source=.impeccable --providers=claude,cursor
```
**Claude Code:**

`/plugin marketplace add pbakaus/impeccable`
Claude Code only. After adding the marketplace, open `/plugin` and install Impeccable from the list.


**Grok Build:**

`grok plugin install pbakaus/impeccable#plugin --trust`
Grok Build only. The `#plugin` suffix installs the slim plugin package (skills, agents, and hooks) instead of the full monorepo. Then run `/impeccable init` in a Grok session. Project-scoped installs via `npx impeccable install --providers=grok` also work and write `.grok/skills/` plus `.grok/hooks/impeccable.json`.


Visit impeccable.style, download the ZIP for your tool, and extract to your project.

**Cursor:**

`cp -r dist/cursor/.cursor your-project/`
**Note:** Cursor skills require setup:


- Switch to Nightly channel in Cursor Settings → Beta
- Enable Agent Skills in Cursor Settings → Rules

**Claude Code:**

```
### Project-specific
cp -r dist/claude-code/.claude your-project/
### Or global (applies to all projects)
cp -r dist/claude-code/.claude/* ~/.claude/
```
**OpenCode:**

`cp -r dist/opencode/.opencode your-project/`
**DeepSeek Harness:**

```
### Project-specific
cp -r dist/dsh/.dsh your-project/
### Or global (applies to all projects)
mkdir -p "${DSH_HOME:-$HOME/.dsh}/skills"
cp -r dist/dsh/.dsh/skills/* "${DSH_HOME:-$HOME/.dsh}/skills/"
```
The CLI honors `DSH_HOME` only when it resolves inside your home directory (or to home itself); otherwise it uses `~/.dsh`. An outside-home manual copy is not managed by `impeccable install/update`.

**Hermes Agent:**

```
### Global (applies to all projects; uses the active profile, or ~/.hermes by default)
cp -r dist/hermes/.hermes/skills/* "${HERMES_HOME:-$HOME/.hermes}/skills/"
### Or project-specific
cp -r dist/hermes/.hermes your-project/
```
**Note:** Hermes gates project-local skills behind a per-repo trust decision
(they are procedure documents, so auto-loading them from any cloned repo is
treated as a prompt-injection vector). After a project-scoped install, run
`hermes skills trust` once from the project root. Global installs into the
active `$HERMES_HOME/skills/` (or `~/.hermes/skills/` when unset) load without
a trust step. `/impeccable <command>` then
routes through the skill's Commands table; the design hook does not install
on Hermes (no hook surface).


**Pi:**

`cp -r dist/pi/.pi your-project/`
**Gemini CLI:**

`cp -r dist/gemini/.gemini your-project/`
**Note:** Gemini CLI skills require setup:


- Install preview version:
`npm i -g @google/gemini-cli@preview`- Run
`/settings` and enable "Skills"- Run
`/skills list` to verify installation

**Codex CLI:**

```
### Project-local
cp -r dist/agents/.agents your-project/
mkdir -p your-project/.codex
cp dist/codex/.codex/hooks.json your-project/.codex/hooks.json
### Or install the skill user-wide. Copy .codex/hooks.json into each project
### where you want the design hook to run.
mkdir -p ~/.agents/skills
cp -r dist/agents/.agents/skills/* ~/.agents/skills/
```
The asset-producer subagent ships nested inside the skill's own `agents/` folder, which Codex auto-discovers. No separate `.codex/agents/` copy is needed. The hook is project-local because Codex discovers hooks from `.codex/hooks.json` next to trusted project config.


**GitHub Copilot:**

`cp -r dist/github/.github your-project/`
**Trae:**

```
### Trae China (domestic version)
cp -r dist/trae/.trae-cn/skills/* ~/.trae-cn/skills/
### Trae International
cp -r dist/trae/.trae/skills/* ~/.trae/skills/
```
**Note:** Trae has two versions with different config directories:


**Trae China**: `~/.trae-cn/skills/`
**Trae International**: `~/.trae/skills/`
After copying, restart Trae IDE to activate the skills.


**Rovo Dev:**

```
### Project-specific
cp -r dist/rovo-dev/.rovodev your-project/
### Or global (applies to all projects)
cp -r dist/rovo-dev/.rovodev/skills/* ~/.rovodev/skills/
```
**Qoder:**

```
### Project-specific
cp -r dist/qoder/.qoder your-project/
### Or global (applies to all projects)
cp -r dist/qoder/.qoder/skills/* ~/.qoder/skills/
```
**Mistral Vibe:**

```
### Project-specific
cp -r dist/vibe/.vibe your-project/
### Or global (applies to all projects)
cp -r dist/vibe/.vibe/skills/* ~/.vibe/skills/
```
**Grok Build:**

```
### Project-specific
cp -r dist/grok/.grok your-project/
### Or global (applies to all projects)
cp -r dist/grok/.grok/skills/* ~/.grok/skills/
```
Prefer `npx impeccable install --providers=grok` or `grok plugin install pbakaus/impeccable#plugin --trust` so the design hook installs too. Project hooks need `/hooks-trust` (or `--trust`) once per folder.


**Google Antigravity:**

```
### Project-specific
cp -r dist/antigravity/.agent your-project/
### Or global (applies to all projects)
mkdir -p ~/.gemini/config/skills
cp -r dist/antigravity/.agent/skills/* ~/.gemini/config/skills/
```
Once installed, every command runs through the single `/impeccable` skill:

```
/impeccable audit        # Find issues
/impeccable polish       # Final cleanup
/impeccable distill      # Remove complexity
/impeccable critique     # Full design review
```
Type `/impeccable` alone to see the full command list.

Most commands accept an optional argument to focus on a specific area:

```
/impeccable audit the header
/impeccable polish the checkout form
```
If you reach for one command often, pin it with `/impeccable pin audit` to get `/audit` as a standalone shortcut.

**Note:** Codex uses skills here, not `/prompts:` commands. Open `/skills` or type `$impeccable`. Repo-local installs live in `.agents/skills/`; user-wide installs live in `~/.agents/skills/`. GitHub Copilot uses `.github/skills/`. Restart the tool if a newly installed skill does not appear.

As you run commands, Impeccable writes working files under `.impeccable/`: critique and polish screenshots, live-mode session and preview state, runtime caches, and per-developer config. Most of it is ephemeral and should not be committed, while a few files are shared project artifacts that belong in the repo. Add this block to your project's `.gitignore`:

```
### impeccable-ignore-start
### Ephemeral output, runtime state, and per-dev overrides.
### Unanchored: .impeccable may sit at the repo root or under a nested
### workspace (apps/web/.impeccable/...); anchored patterns would miss it.
### Shared artifacts stay tracked: config.json, live/config.json,
### design.json, surfaces/*.md, critique/*.md.
.impeccable/config.local.json
.impeccable/hook.cache.json
.impeccable/hook.pending.json
.impeccable/*.png
.impeccable/review/
.impeccable/questions/
.impeccable/live/server.json
.impeccable/live/sessions/
.impeccable/live/previews/
.impeccable/live/annotations/
.impeccable/live/cache/
.impeccable/live/manual-edit-apply-transaction.json
.impeccable/live/manual-edit-events.jsonl
.impeccable/live/manual-edit-evidence/
.impeccable/live/pending-manual-edits.json
.impeccable/live/deferred-svelte-component-accepts.json
.impeccable/live/*.png
### impeccable-ignore-end
```
The block is wrapped in `# impeccable-ignore-start` / `# impeccable-ignore-end` markers so you can recognize and refresh it later. Patterns are unanchored on purpose: in a monorepo the active project (and its `.impeccable/` directory) often lives under a nested workspace path like `apps/web/`, and a root-anchored pattern would miss it.

**Keep these tracked** (they are shared project artifacts, do not add them to `.gitignore`):

- `.impeccable/config.json` (unified shared config)
- `.impeccable/live/config.json` (live-mode framework wiring)
- `.impeccable/design.json` (shared design spec)
- `.impeccable/surfaces/*.md` (route- or artifact-specific strategy and direction contracts)
- `.impeccable/critique/*.md` (review reports)

If an ephemeral file (a screenshot, `config.local.json`) was committed before you added the block, `.gitignore` will not untrack it automatically. Run `git rm --cached <path>` to stop tracking it without deleting your local copy.

On Claude Code, GitHub Copilot, Codex, Cursor, and Grok Build, `npx impeccable install` and `npx impeccable update` install a provider-native hook manifest along with the skill payload. The hook runs the Impeccable design detector on direct UI file edits and surfaces findings back into the agent flow. Claude Code, GitHub Copilot, and Codex surface findings after the edit (and run a deeper pass on Stop where supported). Grok Build scans after the edit to warm Stop, then surfaces on Stop; PostToolUse stdout never reaches the model. Cursor blocks bad proposed writes before they land.

Installed hook surfaces:

- Claude Code: `.claude/settings.local.json` (gitignored, machine-local) runs`${CLAUDE_PROJECT_DIR}/.claude/skills/impeccable/scripts/impeccable hook` . A hook moved into the shared`settings.json` is honored in place.
- GitHub Copilot: `.github/hooks/impeccable.json` (committed, shared by the Copilot CLI and the cloud agent) runs`.github/skills/impeccable/scripts/impeccable hook` . The Copilot CLI activates it once the file is on the repository's default branch and the folder is trusted.
- Cursor: `.cursor/hooks.json` runs`.cursor/skills/impeccable/scripts/impeccable hook-before-edit` .
- Codex: `.codex/hooks.json` runs`.agents/skills/impeccable/scripts/impeccable hook` , with a`commandWindows` sibling that calls`impeccable.cmd` for cmd.exe.
- Grok Build: `.grok/hooks/impeccable.json` runs`.grok/skills/impeccable/scripts/impeccable hook` . Requires`/hooks-trust` or`--trust` . Findings reach the model on Stop, not after each edit.

Every command goes through the launcher shipped in the skill's `scripts/` directory (`impeccable`, or `impeccable.cmd` on Windows), guarded so a missing launcher is a silent no-op. The launcher runs the engine binary that ships next to it, or downloads the pinned version once into `~/.impeccable/bin/`. No Node or other runtime is required for the hook or the skill.

In Claude Code, installed command hooks run independently of model-tool approval. The first edit or Stop event can therefore download and cache the engine even if the session denies the model's launcher command. Review installed hooks before unattended runs; to disable all Claude Code hooks for a run, pass `--settings '{"disableAllHooks": true}'`. See Claude Code's hook security guidance.

The installer preserves unrelated hook entries and settings. If a hook manifest is malformed, install/update aborts by default; rerun with `--force` to back up the malformed file as `.bak` and replace it.

On an interactive `install`/`update`, Impeccable explains the hook and offers to install it (default yes). Your choice is remembered per-developer in the gitignored `.impeccable/config.local.json`, so you are not asked again; `--no-hooks` skips it for that run without recording anything. Hook lifecycle settings live under the `hook` key of `.impeccable/config.json`; detector ignores live under `detector`, shared by `/impeccable hooks` and `npx impeccable detect`.

For debugging, set `hook.auditLog` in `.impeccable/config.json` to a path (or the legacy `IMPECCABLE_HOOK_LOG` env var) to write one NDJSON line per hook invocation. Leave it unset for normal use.

When a new surface gets designed, Impeccable either generates a full-fidelity comp first and builds to match it, or builds straight in code with the ambition written into a development-only direction contract in the surface brief and checked at the finish. Comp-first composes bolder and takes longer; code-first is leaner and faster. `/impeccable init` asks once and records the answer as `buildPath` in `.impeccable/config.json`:

`{ "buildPath": "comp" }`
The values are `comp` and `code`, and nothing else is read. Set it in the gitignored `.impeccable/config.local.json` to override the team's committed value on one machine, which is what you want when your harness has no image generation. In a monorepo, commit it once at the repo root and any workspace that wants something else sets its own. The choice appears at all only where image generation is available, since without it there is nothing to comp.

You do not have to re-run `init` to set it on a project that predates the setting, and you do not have to edit the file by hand either. Whatever is recorded is a default rather than a lock: every decision page carries a footer toggle, and flipping it binds that session only. Flip it on a project that has recorded nothing and Impeccable asks once, after the round, whether to keep it, then writes your answer. That is the whole migration path for an existing project: use the toggle when the default is wrong, and answer the question that follows.

Codex requires one platform step that Impeccable cannot safely skip: open `/hooks` after install or update and approve the project hook. There is no Codex marketplace/plugin install flow for this hook.

Full hook docs: impeccable.style/docs/hooks.

The Stop pass suppresses confirmed pre-existing findings when a verified before-edit baseline is available (currently Claude Edit/Write results for text scans). Other findings are marked new or attribution unknown; unknown is not evidence that your session caused the problem. Explicit `detect` scans remain unchanged.

Manual copy commands are fallback/debug instructions. The normal path is:

```
npx impeccable install
npx impeccable update
```
Live mode edits a local checkout through a development server or local static HTML. Injecting its localhost HTTP helper into a deployed production site, including an HTTPS site, is not supported. Do not disable browser security or weaken production CSP to make it work.

Use live mode only in projects you trust to run locally. Applying copy edits automatically runs `package.json`'s optional `scripts["impeccable:manual-edit-validate"]` command in a shell, with your user permissions; review that script before using live mode in an unfamiliar checkout.

For production inspection, use `npx impeccable detect https://example.com` or the browser extension. These inspect the rendered page; they do not provide live variant editing or write changes back to your source.

Impeccable includes a standalone CLI for detecting anti-patterns without an AI harness. `npx impeccable` is a small shim that runs the same engine binary the skill uses (installed as a platform-specific optional dependency, or fetched once into `~/.impeccable/bin/`); Node is needed only for `npx` itself, and you can also download the binary directly and put it on your PATH.

```
npx impeccable detect src/                   # scan a directory
npx impeccable detect index.html             # scan an HTML file
npx impeccable detect https://example.com    # scan a URL (uses an installed Chrome, Chromium, or Edge)
npx impeccable detect --json .               # CI-friendly JSON output
npx impeccable detect --no-config src/       # raw scan, ignoring project config/context
npx impeccable ignores list                  # show detector ignores
npx impeccable ignores add-file "src/legacy/**"
npx impeccable ignores add-value overused-font Inter --reason "Brand font"
```
The detector catches 61 deterministic issues across AI slop (side-tab borders, purple gradients, bounce easing, dark glows) and general design quality (line length, cramped padding, small touch targets, skipped headings, and more).

Human-readable findings are diagnostics written to stderr, so redirect them with `2> findings.txt`. Use `--json` for machine-readable results on stdout. Exit `0` means the scan completed without primary findings, exit `2` means it completed with primary findings, and exit `1` means at least one requested target could not be scanned; operational failure takes precedence for a partial multi-target scan. URL scans inspect the rendered DOM, computed layout, and accessible linked stylesheets; browser security still prevents reading cross-origin CSS without CORS. A clean detector run is evidence, not proof of visual or accessibility quality: it does not replace inspecting the rendered experience across relevant viewports.

By default, `detect` respects the same `.impeccable/config.json` and `.impeccable/config.local.json` detector config as the design hook: `detector.ignoreRules`, `detector.ignoreFiles`, `detector.ignoreValues`, and `detector.designSystem.enabled`. Hook lifecycle settings such as `hook.enabled` only affect automatic hook execution.

For a waiver that should travel with one file instead of the repo config, add an inline comment in the file: `<!-- impeccable-disable overused-font: exported brand doc -->`. The marker works in any comment syntax, scopes to the whole file (or one line with `impeccable-disable-line` / `impeccable-disable-next-line`), and is bypassed by `--no-inline-ignores` or `--no-config`.

Full detector docs: impeccable.style/docs/detector.

Join the community and ecosystem conversations:

- GitHub Discussions: file bugs, request features, and help newcomers.
- Impeccable on npm: grab the CLI, follow releases, and star the package.
- Follow @pbakaus on Twitter for release notes, sample lint reports, and video highlights of new rules.

See DEVELOP.md for contributor guidelines and build instructions.

Apache 2.0. See LICENSE.

Created by Paul Bakaus

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
