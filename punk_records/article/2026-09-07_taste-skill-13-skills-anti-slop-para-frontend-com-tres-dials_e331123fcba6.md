---
item_id: "f130891c-966d-434a-bf43-ad7d9247cd2e"
platform: article
external_id: "e331123fcba6"
canonical_url: "https://github.com/Leonxlnx/taste-skill"
channel: "Leonxlnx · GitHub"
captured_at: 2026-09-07
status: applied_client
triage: apply_client
tags: ["taste-skill", "ai-slop", "agent-skills", "design-com-ia", "frontend", "gsap", "design-tokens", "claude-code"]
applicability:
  saas_pessoal: alta
  projeto_cliente: alta
  estudo_geral: media
confidence: alta
theme: design-e-ux
content_type: article
---

# Taste Skill: 13 skills anti-slop para frontend, com três dials de ajuste

🔗 https://github.com/Leonxlnx/taste-skill

## Resumo

Taste Skill é um conjunto de Agent Skills portáteis que corrige o visual genérico de interface gerada por IA — o que o autor chama de slop. Não é framework nem dependência: são arquivos SKILL.md que o agente carrega e que mudam o critério do que ele considera pronto em layout, tipografia, movimento e espaçamento. O controle principal são três dials numéricos de 1 a 10 declarados no topo do arquivo: DESIGN_VARIANCE (do centrado e limpo ao assimétrico), MOTION_INTENSITY (do hover ao scroll e magnético) e VISUAL_DENSITY (do espaçoso ao painel denso). O repositório traz 13 skills, e a divisão importa: 10 produzem CÓDIGO e 3 produzem apenas IMAGEM de referência (comps de web, telas de mobile e boards de identidade), que precisam ser reimplementadas depois por um agente de código. A skill padrão é a v2, uma reescrita substancial declarada EXPERIMENTAL, com inferência de brief, mapa de design system, proibição dura de travessão, esqueletos canônicos de GSAP, protocolo de auditoria de redesenho e verificação estrita antes de gerar; a v1 continua disponível para quem depende do comportamento anterior. As variantes cobrem direções visuais já escolhidas (minimalista tipo Notion/Linear, brutalista suíço, premium suave), redesenho de projeto existente, pipeline imagem→código e uma skill que força saída completa quando o modelo entrega trabalho pela metade. Instala-se com `npx skills add`, e o nome de instalação NÃO é o nome da pasta. O README abre com patrocinadores, incluindo oferta de crédito extra de API da Kimi, e traz um aviso de que o projeto não tem token nem moeda oficial.

## Tópicos

- **Os três dials** — DESIGN_VARIANCE (centrado ↔ assimétrico), MOTION_INTENSITY (hover ↔ scroll/magnético) e VISUAL_DENSITY (espaçoso ↔ denso), de 1 a 10, declarados no topo do arquivo da skill.
- **Código versus imagem** — 10 skills produzem código; 3 (imagegen-frontend-web, imagegen-frontend-mobile, brandkit) produzem SÓ imagem de referência, que depois precisa ser implementada por um agente de código.
- **v2 experimental e o escape para v1** — A padrão design-taste-frontend virou v2: inferência de brief, mapa de design system, proibição dura de travessão, esqueletos de GSAP e auditoria de redesenho. A v1 fica em design-taste-frontend-v1 para quem precisa do comportamento exato antigo.
- **Variantes por direção visual** — minimalist-ui (Notion/Linear), industrial-brutalist-ui (tipografia suíça, contraste duro), high-end-visual-design (suave, premium, movimento com mola) — usar quando a direção já está escolhida.
- **Skills utilitárias** — redesign-existing-projects audita antes de mexer em projeto que já existe; full-output-enforcement força saída completa quando o modelo trunca; image-to-code faz o pipeline gerar imagem → analisar → codar.
- **Instalação por nome, não por pasta** — `npx skills add <repo>` instala tudo; `--skill "design-taste-frontend"` instala uma. O nome de instalação vem do campo name: do frontmatter e NÃO coincide com o nome da pasta.
- **Patrocínio e aviso de cripto** — O README abre com patrocinadores e oferta de 10% de crédito extra de API da Kimi. O autor declara que o projeto não tem token nem moeda oficial e não endossa nenhum que use o nome dele.

## Ferramentas citadas

- **npx skills**: CLI que varre a pasta skills/ do repositório e instala as skills, todas do mesmo jeito
- **GSAP**: biblioteca de animação para a qual a v2 traz esqueletos de código canônicos
- **Claude Code**: um dos agentes de destino; recebe as skills ou os frames gerados pelas skills de imagem
- **Kimi (Moonshot AI)**: patrocinador do projeto; o README oferece 10% de crédito extra de API na primeira compra
- **Google Stitch**: alvo da skill stitch-design-taste, com formato opcional de exportação DESIGN.md

## Pontos-chave

- 85.101 estrelas no GitHub, último push em 24/08/2026 — verificado na API em 07/09; é a menos ativa das skills populares da mesma lista
- É gosto, não processo: não disputa o comando do agente e por isso NÃO colide com o ciclo dos Satélites
- Três dials de 1 a 10 substituem prosa: variância de layout, intensidade de movimento e densidade visual
- Três das 13 skills não geram código nenhum — só imagem de referência
- A skill padrão é declarada EXPERIMENTAL pelo autor; a v1 é fixável por nome se o resultado piorar
- A v2 traz proibição dura de travessão, que é o mesmo cacoete de IA denunciado no item de 01/09 do vault
- Nome de instalação ≠ nome da pasta — errar isso é o modo de falha mais provável na instalação
- Reversível: são arquivos de texto, apagar desfaz; nenhuma dependência é adicionada ao projeto
- CONFLITA com a skill Impeccable: duas skills de design ativas se contradizem (ver item do AI slop de 07/09)
- O autor precisou desmentir publicamente um token cripto criado com o nome do projeto

## Como aplicar

Candidata direta para o site do cliente e para a interface do SaaS: instalar UMA skill de design (esta OU a Impeccable, nunca as duas) e calibrar pelos três dials conforme o segmento — variância e movimento baixos para cliente sério, altos para criativo. Teste honesto: gerar a mesma landing com e sem a skill e comparar lado a lado. Se a v2 experimental der resultado instável, fixar a v1 por nome.

## 🍩 York diz

Ai, que preguiça de ler README que começa com patrocinador — mas essa aqui eu deixo passar, porque não custa nada e é reversível: são arquivos de texto, não assinatura. O que eu quero que você anote é o desconto de 10% de API da Kimi no topo da página: quando a ferramenta é grátis, o dinheiro está em outro lugar, e vale saber onde. E olha, três botõezinhos numerados para não precisar explicar gosto por escrito é o tipo de preguiça que eu aprovo.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

*The Anti-Slop Frontend Framework for AI Agents*

Thanks to **Kimi (Moonshot AI)**, our Open Source Friend, for supporting taste-skill! With 2.8T parameters, native vision, and a 1-million-token context window, **Kimi K3** delivers frontier performance across long-horizon coding, knowledge work, and reasoning.

**Get a Kimi API key**. Taste-skill users get **10% bonus API credits** on their first purchase.

|  | <sub>**interfaces.dev** · A design engineering magazine by **Jakub Krehel**</sub> | 
|  | <sub>**React Bits** · animated React components for creative interfaces</sub> | 
|  | <sub>**Emil Kowalski** · animations.dev</sub> | 
|  | <sub>**IMG.LY** · CreativeEditor SDK</sub> | 
|  | <sub>**Sent.dm** · messaging APIs for SMS, WhatsApp, and RCS</sub> | 
|  |  | 

Portable **Agent Skills** that upgrade AI-built interfaces: stronger layout, typography, motion, and spacing instead of boilerplate-looking UIs. This repo also includes **image-generation skills** for reference boards (web, mobile, brand kits). Pair them with **ChatGPT Images** or similar generators, then hand the frames to Codex, Cursor, or Claude Code for implementation.

Taste Skill has no official token, coin, or crypto project. Any token using my name, image, or project is unaffiliated and not endorsed by me.

<sub>Disclaimer · Install · Skills · Settings · Examples · Sponsors · Research · FAQ · License</sub>

We would love your feedback. Suggestions and bug reports:

- Open a Pull Request or Issue on GitHub
- DM @lexnlin or @blueemi99
- Email us at hello@tasteskill.dev

The `npx skills add` CLI scans the `skills/` folder in this repo, so **all skills below (code and image-generation) install the same way.**

`npx skills add https://github.com/Leonxlnx/taste-skill`
Install a single skill by its **install name** (the `name:` field inside the SKILL frontmatter, not the folder name):

`npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"`
You can also copy any `SKILL.md` into your project or paste it into ChatGPT / Codex conversations.

The default `taste-skill` (install name `design-taste-frontend`) is now **v2 (experimental)**, a substantial rewrite of the original v1. If you already have v1 installed, just re-run the install command and you will be upgraded:

`npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"`
The install name did not change, so no script updates are needed. The newer SKILL.md replaces the older one in place.

If you depend on the exact behavior of v1 and want to pin to it explicitly:

`npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend-v1"`
See CHANGELOG.md for the full v1 to v2 diff and the rationale.

Each skill does one job; you do not need all of them at once. **Implementation skills** output code. **Image-generation skills** output reference images only.

The `Install name` column is the exact value you pass to `--skill`.

| Skill (folder) | Install name | Description | 
|---|---|---|
| **taste-skill** | `design-taste-frontend` | 🆕 **v2 (experimental)** - substantial rewrite of the default skill. Reads the brief, infers the design language, tunes three dials (VARIANCE / MOTION / DENSITY). Brief inference, design-system map, hard em-dash ban, canonical GSAP code skeletons, redesign-audit protocol, strict pre-flight check. Actively iterating toward v2.0.0 stable. | 
| **taste-skill-v1** | `design-taste-frontend-v1` | The original v1 of taste-skill, preserved for projects depending on its exact behavior. Use only if the v2 default breaks something specific in your workflow. | 
| **gpt-tasteskill** | `gpt-taste` | Stricter variant for GPT/Codex: higher layout variance, stronger GSAP direction, aggressive anti-slop. | 
| **image-to-code-skill** | `image-to-code` | Image-first pipeline: generate site references, analyze them, then implement the frontend to match. | 
| **redesign-skill** | `redesign-existing-projects` | Existing projects: audit the UI first, then fix layout, spacing, hierarchy, styling. | 
| **soft-skill** | `high-end-visual-design` | Polished, calm, expensive UI with softer contrast, whitespace, premium fonts, spring motion. | 
| **output-skill** | `full-output-enforcement` | When the model ships half-finished work: full output, no placeholder comments. | 
| **minimalist-skill** | `minimalist-ui` | Editorial product UI (Notion/Linear vibes), restrained palette, crisp structure. | 
| **brutalist-skill** | `industrial-brutalist-ui` | Hard mechanical language: Swiss type, sharp contrast, experimental layout. | 
| **stitch-skill** | `stitch-design-taste` | Google Stitch-compatible rules, including optional `DESIGN.md` export format. | 

These produce design images only (no code). Use with ChatGPT Images, Codex image mode, or any agent that generates images.

| Skill (folder) | Install name | Description | 
|---|---|---|
| **imagegen-frontend-web** | `imagegen-frontend-web` | Website comps: hero, landing, multi-section with strong typography, spacing, anti-slop art direction. | 
| **imagegen-frontend-mobile** | `imagegen-frontend-mobile` | Mobile screens and flows: iOS/Android/cross-platform, mockups, readable type, coherent sets. | 
| **brandkit** | `brandkit` | Brand-kit boards: logo directions, palettes, type, identity applications across categories. | 

- Start with **taste-skill** for the safest general default. (Now v2 experimental - see what changed in the CHANGELOG.)
- If you depend on the exact behavior of the original taste-skill, install **taste-skill-v1** instead.
- Use **gpt-taste** when you want the stricter GPT/Codex-oriented rules and motion/layout enforcement.
- Use **image-to-code-skill** for image → analyze → code website workflows.
- Use **redesign-skill** to improve an existing codebase instead of greenfield styling.
- Add **soft-skill** ,**minimalist-skill** , or**brutalist-skill** when the visual direction is already chosen.
- Add **output-skill** if the agent keeps truncating output.
- Use **imagegen-frontend-web** ,**imagegen-frontend-mobile** , or**brandkit** when the deliverable is**images** (comps, flows, identity boards), then pass results to your coding agent.

For **image-to-code-skill**, state the pipeline in the prompt, e.g.: `follow the skill: generate images, then analyze, then code`.

Attach or paste **`imagegen-frontend-web`**, **`imagegen-frontend-mobile`**, or **`brandkit`** and ask for the frames you need, then feed the renders to Codex, Cursor, or Claude Code. Use **image-to-code-skill** when you want one workflow that both generates references and implements the site in code.

Numbers at the top of the file are 1-10 dials:

- **DESIGN_VARIANCE** : Layout experimentation (lower: centered/clean · higher: asymmetric/modern).
- **MOTION_INTENSITY** : Animation depth (lower: hover · higher: scroll/magnetic).
- **VISUAL_DENSITY** : Information per viewport (lower: spacious · higher: dense dashboards).

Created with taste-skill:

If Taste Skill helps you, consider sponsoring:

Background writing that shaped these skills lives in `research/`.

**How is this different from other AI design skills?**

Multiple specialized variants, adjustable dials in key skills, anti-repetition rules informed by dedicated research. All are framework agnostic across major coding agents.

**Does it work with React, Vue, Svelte?**

Yes. Rules target design intent, not a single framework API.

**What is SKILL.md?**

A portable instruction file agents can load automatically; install via `npx skills add` or by copying into a repo or conversation.

**Do image-generation skills install with `npx skills add`?**

Yes. They live under `skills/` alongside the code skills so the same CLI discovers them.

MIT License · Copyright (c) 2026 Leonxlnx

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
