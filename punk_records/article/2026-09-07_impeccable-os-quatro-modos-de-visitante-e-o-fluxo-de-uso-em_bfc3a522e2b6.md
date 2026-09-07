---
item_id: "ac960847-02ce-4863-9d15-22e2b023a322"
platform: article
external_id: "bfc3a522e2b6"
canonical_url: "https://impeccable.style/designing"
channel: "impeccable.style"
captured_at: 2026-09-07
status: enriched
triage: null
tags: ["impeccable", "modos-de-visitante", "design-com-ia", "auditoria-de-ui", "design-system", "ai-slop", "agent-skills"]
applicability:
  saas_pessoal: alta
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
theme: design-e-ux
content_type: article
---

# Impeccable — os quatro modos de visitante e o fluxo de uso em quatro fases

🔗 https://impeccable.style/designing

## Resumo

Esta é a página de uso do Impeccable, e o conceito mais aproveitável dela são os QUATRO MODOS DE VISITANTE, que mudam o vocabulário de todos os comandos conforme o que a pessoa foi fazer naquela tela — e não conforme o que a empresa vende. Persuade: o visitante decide e age (landing, campanha, preço, editorial); o design é o produto e precisa conquistar atenção, com tipografia distintiva, paleta comprometida e herói guiado por imagem. Operate: o visitante completa uma tarefa (app, admin, painel, editor); legibilidade e expectativa nativa valem mais que expressão, e a marca vive no detalhe preciso. Read: o visitante entende algo (documentação, guias, changelog); estrutura para compreensão primeiro, depois medida, ritmo e hierarquia silenciosa. Experience: o visitante está dentro da obra (portfólio, galeria); o artefato lidera desde a primeira dobra e a interface quase desaparece. Um mesmo projeto costuma conter os quatro. O fluxo tem quatro fases: dar contexto, melhorar o que existe, checar antes de publicar e impedir que o design system derive. O `/impeccable init` varre a base de código, forma a própria leitura do produto, pergunta apenas o que não conseguiu deduzir e escreve PRODUCT.md e DESIGN.md — deliberadamente sem perguntar sobre cor e tipografia, que se decidem com a tela e não antes dela. Para melhorar, há dois caminhos: comandos por disciplina nomeada (typeset, layout, colorize, animate, bolder, quieter) ou o modo live, que injeta um seletor na página do servidor de desenvolvimento — aponta-se um elemento, descreve-se o que se quer, e voltam três variantes; aceita uma e ele escreve de volta no código. Antes de publicar, três comandos que não redesenham, apenas acham o que falta: auditoria com cinco dimensões pontuadas de 0 a 4 (acessibilidade, desempenho, tematização, responsivo, antipadrões) com achados de P0 a P3; revisão de texto de interface afinada pelo PRODUCT.md; e teste de dados sujos de produção (nomes de 60 caracteres, títulos em alemão, preços na casa dos bilhões, erro 500, offline).

## Tópicos

- **Persuade** — Visitante decide e age: landing, campanha, preço, editorial. O design É o produto e precisa conquistar atenção — tipografia distintiva, paleta comprometida, herói guiado por imagem.
- **Operate** — Visitante completa uma tarefa: app, admin, painel, editor. Legibilidade e expectativa nativa superam expressão; a marca aparece no detalhe preciso.
- **Read e Experience** — Read: documentação e guias, estrutura para compreensão, medida e hierarquia silenciosa. Experience: portfólio e galeria, o artefato lidera e a interface quase desaparece.
- **init grava o contexto durável** — Varre a base de código, forma a própria leitura do produto e pergunta só o que não deduziu; escreve PRODUCT.md e DESIGN.md. NÃO pergunta cor nem tipografia — isso se decide com a tela.
- **Modo live no navegador** — Injeta um seletor na página do servidor de desenvolvimento: aponta-se o elemento, descreve-se o desejo, voltam três variantes de qualidade de produção e a aceita é escrita de volta no código-fonte.
- **Três checagens antes de publicar** — Auditoria em 5 dimensões pontuadas de 0 a 4 com achados P0-P3; revisão do texto de interface pelo PRODUCT.md; e teste com dados sujos de produção (nomes longos, alemão, bilhões, 500, offline).
- **Os quatro antipadrões de uso** — Não rodar junto com a skill de design da Anthropic (vocabulários colidem e se anulam); não fixar todos os comandos; não pular o init (sem contexto ele cai em SaaS genérico); não tratá-lo como linter — é parceiro opinativo, e ignorar a opinião sem razão piora a saída.

## Ferramentas citadas

- **Impeccable**: skill de design com 23 comandos que roda dentro de Cursor, Claude Code, Copilot, Codex e Gemini CLI
- **npx impeccable detect**: detector determinístico de antipadrões, com saída JSON e código de saída que reprova o build
- **gpt-image-2**: usado para gerar a prancha do sistema e o mock da primeira tela quando o harness não tem ferramenta de imagem; gasta crédito próprio, de 5 a 25 centavos por imagem

## Pontos-chave

- Os quatro modos são lidos da TELA, não do que a empresa vende: a landing de uma ferramenta é Persuade, a documentação de uma grife é Read
- O init recusa deliberadamente falar de cor e tipografia antes de existir tela
- Modo live escreve de volta no código-fonte, não só sugere
- Auditoria pontua 5 dimensões de 0 a 4 e classifica achados de P0 a P3
- O teste de dados sujos inclui nome de 60 caracteres, título em alemão, preço em bilhões, erro 500 e offline
- O autor avisa: rodar duas skills de design com vocabulários diferentes faz uma anular a outra — escolher UMA
- Pular o init faz todos os comandos caírem em padrão genérico de SaaS
- Geração de imagem custa crédito próprio (5 a 25 centavos), fora de qualquer plano de assinatura

## Como aplicar

Os quatro modos resolvem sozinhos uma confusão recorrente: o site do cliente é PERSUADE (landing que precisa conquistar) e a interface do SaaS é OPERATE (tarefa, legibilidade, expectativa nativa) — pedir o mesmo tratamento visual para os dois é erro de partida. O teste de dados sujos é o mais barato de adotar hoje, mesmo sem instalar nada: nome de 60 caracteres, preço absurdo e estado offline quebram landing gerada por IA com frequência.

## 🪖 Shaka diz

O senhor deve separar duas coisas nesta página: a taxonomia dos quatro modos é evidência de bom raciocínio e vale mesmo sem instalar nada, enquanto o resto é documentação de um produto. Registro o aviso do próprio autor, que confirma o que já sabíamos por outra fonte: duas skills de design com vocabulários distintos se anulam. E anoto a lacuna: nenhuma das cinco dimensões auditadas cobre conformidade legal, que no site do cliente virá de LGPD e do Decreto 7.962, não de acessibilidade.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Consolidate drift.

Find patterns used three or more times with the same intent. Propose tokens and primitives.

Use Impeccable in four phases: set context, improve what exists, check before shipping, and keep the design system from drifting.

Before asking an agent to design, give it the basics: what platform this is, who the interface is for, what the product can honestly claim, and what evidence actually exists. `/impeccable init` saves that context once. Then use `/impeccable shape` for a brief, or just describe the surface you want and Impeccable takes it through the new-work flow.

PRODUCT.mdWritten by init

Platformweb

UsersSREs on call, reading fast, often in the dark.

PositioningTraces every alert back to the deploy that caused it.

Evidence on handReal incident timelines. No customer logos yet.

Init scans the codebase, forms its own read of the platform and the product, and asks only what it could not work out. It writes `PRODUCT.md` and, if there's code to scan, offers a `DESIGN.md`. Every later command reads both before generating.

It does not ask about colors or type. Those get decided with the surface, not before it.

For blank-slate work, a visual reference helps more than a long prompt. Impeccable renders the chosen direction as a system board and a first-surface mock, then codes toward that image instead of a paragraph. Neo Mirai is the full loop: rolled direction, implemented page, browser iteration.

The first two plates were generated with **OpenAI GPT Image 2**; the third is the implemented Neo Mirai page. Any harness with a built-in image tool works the same way, Codex and Gemini CLI included. Impeccable calls whatever your harness provides rather than a specific model.

No native image tool in your harness? Set `OPENAI_API_KEY` and Impeccable renders through gpt-image-2 instead. It says so before the first image, since it spends your own credit, roughly 5 to 25 cents each.

Once something exists, you're iterating. There are two paths: specific commands for named dimensions, or Live Mode for visual exploration.

Type a command and let the skill encode a specific discipline. Best when you know the word: typography, layout, color, motion.

Run `/impeccable live` in your AI tool and it drops this picker onto your running dev server. Point at any element, draw or type what you want, hit Go. Three production-quality variants; accept one and it writes back to source.

| When to reach for which |  | 
|---|---|
| Fix something "off" that you can't name | /impeccable live | 
|---|---|
| Apply a specific discipline: type, layout, color, motion | /typeset · /layout · /colorize · /animate | 
| Explore three directions side by side | /impeccable live | 
| Ask "is this any good?" | /impeccable critique | 
| Bring a safe design to life, or tone a shouting one down | /bolder · /quieter | 

Three commands before anything ships. They don't redesign, they find what's left to fix. Point them at a narrow target: one section reviewed closely beats a whole page reviewed at a glance, the way a lens sharpens as it tightens.

Five dimensions scored 0 to 4: accessibility, performance, theming, responsive, anti-patterns. Findings tagged P0 to P3.

Labels, error messages, empty-state prose, microcopy. Tuned to the audience from PRODUCT.md.

60-character names, German product titles, prices in the billions, 500s, offline. Production data is messy.

Features ship, drift happens. Two commands close the gap before it solidifies.

Scans your tokens, components, and rendered routes, then writes a DESIGN.md in the Stitch format. The more it points at your real components and live routes, the closer Impeccable reads your design language instead of guessing at it.

The 23 commands run inside your AI coding tool: Cursor, Claude Code, GitHub Copilot, Codex, Gemini CLI. That's where everything on this page happens. The same anti-pattern detector also runs in two places outside the chat.

$npx impeccable detect src/

Point it at a directory, a file, or a URL. Deterministic rules and JSON output, with an exit code that fails the build when slop slips into a pull request.

a-competitor.com

The same checks as a browser overlay, on anything live: your staging build, a competitor, a page you'll never get into an editor.

Four modes, four vocabularies. Impeccable reads the mode from the surface you named, not from what the company sells, so `typeset`, `animate`, `colorize`, and friends adjust to match. A tool's landing page is still Persuade; a fashion house's docs are still Read. One project usually holds all four.

**Persuade.** The visitor decides and acts: landing pages, campaigns, pricing, editorial. Design is the product here, so it has to earn attention. Distinctive type, committed palette, image-led heroes.

**Operate.** The visitor completes a task: app UI, admin, dashboards, editors, tools. Scanability and native expectations outrank expression, and brand lives in precise details.

**Read.** The visitor understands something: docs, guides, help, changelogs. Structure for comprehension first, then make the reading worth staying in. Measure, rhythm, and quiet hierarchy carry it.

**Experience.** The visitor is inside the work itself: portfolios, galleries, showcases. The artifact leads from the first viewport and the interface recedes until it is almost gone.

An anti-patterns list, for using the anti-patterns tool.

- Running both Impeccable and Anthropic's frontend-design skillAnthropic's skill does get updates, just infrequent ones, so it tends to sit behind on current patterns. That is not the reason to avoid running both, though. Two skills with different design vocabularies collide and cancel each other out. Pick one.
- Pinning every commandPinning brings back `/audit` ,`/polish` ,`/critique` as shortcuts. Pin everything and you've re-exploded the`/` menu the v3.0 consolidation cleaned up. Pin the two or three you reach for daily.
- Skipping`init`Commands still run without PRODUCT.md and DESIGN.md. They default to generic SaaS patterns. The floor is meaningfully higher with context. Run init once; every later command benefits.
- Treating it like a linterImpeccable is an opinionated design partner, not a validator. It has a point of view. Push back with a reason and it'll work with you. Ignore the opinion without a reason and output gets worse, not better.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
