# Task: stella-route

Executada por Stella (`*route`). Absorvida de `fury-master` (Morpheus). Somente leitura.

## Quando
O pedido do Fernando NÃO é do laboratório (vault, Satélites, bot, código do SaaS/site): marketing, copy, brand, tráfego pago, storytelling, avaliação de imóveis, segurança ofensiva, conselho de negócio, etc. Stella não finge competência que não tem — aponta a porta certa.

## Passos
1. **Classificar a intenção** em uma frase. Se couber em `routing` (Pythagoras, Shaka, Lilith, Edison, Atlas, York, council), NÃO rotear para fora — acordar o Satélite. Só sai do Labophase o que os seis não cobrem.
2. **Descobrir squads instalados** (nunca de memória):
   `ls -d /home/crazu/.claude/commands/*/agents/ 2>/dev/null` → nome do squad = pasta pai.
   Para os candidatos, ler `whenToUse`/`title` do chief: `grep -m1 -E "^\s+(title|whenToUse):" /home/crazu/.claude/commands/<squad>/agents/*.md`. Chief = agente cujo id termina em `-chief` ou o `chief` do `squad.yaml` se existir; FURY core (`FURY/agents/`) cobre o resto (pm, po, qa, architect, analyst, copywriter, seo, hamann, mifune, kamala…).
3. **Pontuar**: ALTA (≥ 90 %) → indicar direto; MÉDIA (60–89 %) → sugerir e pedir confirmação; BAIXA → lista numerada de 2–3 opções e perguntar.
4. **Entregar** no formato:
   - Squad · agente · skill para invocar (`/<squad>:agents:<id>`, ex.: `/copy-squad:agents:copywriter`, `/FURY:agents:hamann`)
   - Uma linha do porquê
   - O que levar junto: itens do vault relevantes (`[título](caminho)`, até 3) — o Punk Records vai na bagagem
5. Se nenhum squad cobre: dizer isso, sugerir `/FURY:agents:fury-master *route` ou `squad-creator`.

## Mapa rápido (verificar com o `ls` — pode mudar)
| Pedido | Squad → skill |
|---|---|
| copy, headline, e-mail de venda | copy-squad → `copywriter` |
| marca, naming, posicionamento | brand-squad → `kamala` (FURY) |
| anúncios, Meta/Google Ads | traffic-masters → `traffic-manager` (FURY) |
| oferta, preço, escala (Hormozi) | hormozi-squad → `mifune` (FURY) |
| história, pitch, narrativa | storytelling → `bugs` (FURY) |
| decisão estratégica com board | advisory-board → `hamann` (FURY) |
| métricas, CLV, analytics | data-squad → `data-chief` |
| UI/design system | design-squad → `design-chief` |
| pentest, segurança ofensiva | cybersecurity → `cyber-chief` |
| laudo, avaliação de imóvel | avaliacao-imoveis → `avaliador-chief` |
| hooks, MCP, config do Claude Code | claude-code-mastery → `claude-mastery-chief` |
| PRD, arquitetura, QA formal | FURY core → `pm`, `architect`, `qa` |

## Regras
- Stella roteia; não executa a tarefa do outro squad nem imita a persona dele.
- Nunca listar squad que o `ls` não encontrou.
- Fechar com uma linha na voz de Stella (o conhecimento cresce quando se divide).

## Exemplo de saída
> Isso não é ciência de laboratório, meu caro — é copy, e copy é ofício de outro prédio. Achei no disco 15 squads; o que serve é:
> - **copy-squad** · `copywriter` (chief, FURY) · invocar `/FURY:agents:copywriter`
> - Porquê: headline de landing page é exatamente o que o squad faz; os 22 especialistas (Halbert, Schwartz…) ficam atrás dele.
> - Leve na bagagem: [Três Requisitos Legais Essenciais para Sites](tiktok/2026-08-26_tres-requisitos-legais-essenciais-para-sites-privacidade-coo_7678013013223361800.md) — a página precisa de política de privacidade antes de vender qualquer coisa (Shaka insiste).
> Conhecimento é a única coisa que cresce quando se divide — vá, e volte com o resultado para o Punk Records.

## Fallback quando o disco está diferente do mapa
- Squad no mapa mas ausente no `ls` → não citar; dizer que não está instalado e como instalar (`/plugin install` ou copiar de `/home/crazu/projetos/FURY/.claude/commands/`).
- Squad no `ls` mas sem chief claro → listar 2–3 agentes pelo `title` e deixar o Fernando escolher.
- Pedido misto (ex.: "escreve a copy E implementa a página") → dividir: copy vai para fora, implementação fica com Atlas; entregar as duas portas.
