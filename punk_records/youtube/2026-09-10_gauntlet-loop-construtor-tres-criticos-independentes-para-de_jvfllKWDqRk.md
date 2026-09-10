---
item_id: "d0d68e68-1624-4e04-ad4e-e47537a87043"
platform: youtube
external_id: "jvfllKWDqRk"
canonical_url: "https://www.youtube.com/watch?v=jvfllKWDqRk"
channel: "Felipe Borges - Fala IA!"
captured_at: 2026-09-10
status: enriched
triage: null
tags: ["gauntlet-loop", "agentes-criticos", "claude-design", "design-system", "custo-em-tokens", "claude-code-skill", "referencia-visual", "quality-gate"]
applicability:
  saas_pessoal: media
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
theme: ia-e-agentes
content_type: transcript
---

# Gauntlet Loop: construtor + três críticos independentes para design no Claude Code

🔗 https://www.youtube.com/watch?v=jvfllKWDqRk

## Resumo

O vídeo apresenta a técnica de prompting chamada Gauntlet Loop, popularizada por Matt Shumer, e a adapta para trabalho prático — sites, carrosséis e teasers em HTML — em vez das demonstrações de jogos 3D que circularam. A ideia central resolve o defeito estrutural de pedir design a um modelo: ele avalia o próprio trabalho. No loop, um agente construtor produz e três críticos independentes avaliam, cada um responsável por uma falha diferente — o crítico de briefing verifica se o resultado é o que o usuário pediu e caça alucinação, o crítico de sistema verifica cor, fonte, identidade e regras do projeto, e o crítico visual compara com a referência entregue. Enquanto não passar, o trabalho volta ao construtor. O autor disponibiliza gratuitamente uma skill que orquestra isso e que segue quatro etapas: entrevista, pré-verificação dos insumos, desmontagem da referência (tipografia, cor, composição) e a montagem do loop. A skill deixa escolher o modelo por papel — qualidade máxima usa Opus em quase tudo, custo-benefício usa Sonnet no construtor e Haiku no crítico de sistema — e exige um teto de rodadas, senão o loop consome tokens indefinidamente. O passo anterior recomendado é criar um design system no Claude Design e baixá-lo, para servir de referência estável. Três execuções são mostradas com custo medido: um carrossel em 5 rodadas (293 mil tokens), um vídeo em HTML em 4 rodadas (377 mil tokens, equivalente a US$ 3,19 em API) e um site em 3 rodadas (US$ 7,54). O veredito do autor é que a primeira versão sai nota oito em vez de nota seis, mas que a técnica é cara e deve ser reservada para entrega de cliente, não para brincar.

## Tópicos

- **O defeito que a técnica resolve** — Sem críticos, o modelo avalia o próprio trabalho; o loop substitui autoavaliação por revisão independente.
- **Os quatro papéis** — Construtor mais crítico de briefing (fidelidade ao pedido), crítico de sistema (cor, fonte, identidade) e crítico visual (comparação com a referência).
- **As quatro etapas da skill** — Entrevista, pré-verificação dos insumos, desmontagem da referência e montagem do loop.
- **Modelo por papel** — Qualidade máxima usa Opus quase todo; custo-benefício usa Sonnet no construtor e Haiku no crítico de sistema.
- **Teto de rodadas é obrigatório** — Sem limite o loop roda quase indefinidamente e queima token; o autor sugere começar em 5.
- **Design system como insumo** — Criar o design system no Claude Design e baixá-lo dá uma referência estável e reutilizável fora da ferramenta.
- **Custo medido em três execuções** — Carrossel 293k tokens/5 rodadas; HTML 377k tokens/4 rodadas (US$ 3,19); site 3 rodadas (US$ 7,54).

## Ferramentas citadas

- **Claude Code**: onde o loop roda; exige o poder de processamento que a técnica pede
- **Claude Design**: cria e exporta o design system usado como referência
- **Skill de loop (gratuita)**: orquestra construtor e críticos; distribuída pelo autor na descrição do vídeo
- **Codex / OpenAI**: chamado pelo Claude Code para gerar as imagens, que ele não gera sozinho
- **Pinterest, Behance e Instagram**: fontes de referência visual usadas como insumo do loop

## Pontos-chave

- O ganho principal é tirar do modelo o papel de juiz do próprio trabalho.
- Três críticos, cada um responsável por um tipo de falha, em vez de um revisor genérico.
- A skill é gratuita e está na descrição do vídeo.
- Escolher modelo por papel permite dosar custo sem perder o crítico visual, que é o mais caro e o mais importante.
- Definir teto de rodadas é obrigatório — sem isso o loop não para sozinho.
- Primeira versão sai nota oito em vez de nota seis, segundo o autor.
- Custo real medido: US$ 3,19 num vídeo HTML e US$ 7,54 num site.
- A recomendação explícita é guardar a técnica para entrega de cliente, não para experimentar.
- ⚠️ O vídeo usa o site da Apple como referência para construir a marca fictícia 'Spider' e diz textualmente que é melhor copiar algo que se sabe que funciona — exatamente a prática que a jurisprudência brasileira já condenou.
- O conteúdo é isca para a comunidade paga do autor (AI Cloud).

## Como aplicar

É a peça que faltava no método de design que o Fernando já vinha construindo: ele provou que referência de entrada + iteração funciona, mas as iterações eram manuais, cinco rodadas feitas à mão na landing da VDC. O loop automatiza exatamente isso, e o crítico visual faz o que o detector estático não consegue — comparar com a referência. Vale testar contra a régua que já existe (`lab-taste/ferramentas/detector`): mesma landing, mesma medição, e o número decide. O teto de rodadas e a escolha de modelo por papel são o que evita a conta explodir.

## 🔧 Atlas diz

Grr. Passo 1: o parafuso certo aqui é separar quem constrói de quem julga — o resto é consequência. Passo 2: o teto de rodadas não é sugestão, é o freio; sem ele a máquina roda até a conta doer. Passo 3: um aviso que o vídeo não dá — ele clona o site da Apple e chama isso de referência. Você já leu a jurisprudência ontem, Fernando. Use a técnica, escolha outro alvo.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
