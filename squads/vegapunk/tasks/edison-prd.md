# Task: edison-prd

Executada por Edison (`*prd {feature}`). Escreve um PRD ENXUTO usando `templates/edison-prd.md`. Absorvido do `pm` do FURY (create-prd / brownfield-prd), reduzido a uma pessoa construindo com Claude Code. O PRD é a peça que Edison entrega na bancada da Atlas quando a feature é maior que um fim de semana.

## Quando usar
- Feature com mais de 1 fim de semana ou mais de 1 tela.
- Site do cliente: qualquer coisa que o cliente vai ver e aprovar (PRD vira o "combinado").
- Depois de `*discovery` com evidência sólida. Se não teve discovery e o "por quê" está vago, rodar `*discovery` primeiro (dizer isso ao Fernando).

## Entrada
- `feature`: nome ou frase.
- Contexto: `{saas|cliente}` — perguntar se não ficar claro.
- Ler `knowledge/INDEX.md`; itens relacionados viram a seção "Fontes do Punk Records".
- Se for brownfield (já existe código): pedir ao Fernando o caminho do projeto e ler o README/estrutura antes de escrever — o PRD tem que citar o que JÁ existe para não propor de novo.

## Passos

1. **Abrir o template** `templates/edison-prd.md` e preencher seção a seção. Nada de seção vazia: se não se aplica, escrever "n/a — por quê".

2. **Problema e objetivo** (do discovery, se houve). Objetivo tem número: "reduzir X de A para B" ou "permitir Y para Z pessoas".

3. **Escopo com MoSCoW**, no máximo 12 itens no total:
   - **Must** (sem isso não lança) · **Should** (lança sem, mas dói) · **Could** (se sobrar) · **Won't** (explicitamente fora, para Atlas não construir e Lilith não cobrar).
   Regra do Edison: o conjunto Must tem que caber em ≤ 2 fins de semana. Se não cabe, cortar ou quebrar em 2 PRDs.

4. **Histórias de usuário** (3–6): "Como {usuário}, quero {ação} para {benefício}". Cada uma com **critérios de aceite** verificáveis (2–4 por história, formato "Dado / Quando / Então" ou checklist simples). Atlas usa isso como definição de pronto.

5. **Telas** — só listar nome + 1 linha do que mostra. Se precisa desenho: "→ `*wireframe {tela}`".

6. **Restrições técnicas** (o que o Fernando já tem e não muda sem motivo): stack atual, Docker local, OpenRouter, SQLite, Telegram, hospedagem do cliente, LGPD se toca dado pessoal (citar item do vault se existir).

7. **Métricas**: 1 principal + até 2 secundárias. Com "como medir" (log, contador no banco, pergunta ao cliente).

8. **Riscos e perguntas abertas**: ≤ 5. Cada risco com mitigação de uma linha. Marcar os que Lilith deve atacar.

9. **Custo e ordem**: estimativa em fins de semana por bloco Must; se > 2 → "York, coxinha ou jantar?" e registrar a resposta. Ordem sugerida de construção (o que testar primeiro em 1 dia).

10. **Rodar `checklists/edison-prd.md`** antes de entregar. Corrigir o que falhar.

11. **Entregar** em `docs/prd/{slug}.md` no projeto alvo (perguntar caminho se não souber; nunca em `knowledge/`). Terminar com: "Chame Atlas: *build {primeiro bloco Must}" e, se houver risco marcado, "Peça a Lilith: *attack {risco}".

## Regras
- Tamanho alvo: 80–150 linhas. PRD de 400 linhas é ideia demais.
- Linguagem: dev júnior — cada termo técnico novo tem meia linha de explicação na primeira vez.
- Nunca inventar requisito "porque é padrão de mercado": todo item vem do discovery, do vault (citado) ou do Fernando.
- Site do cliente: incluir seção "O que o cliente aprova" — lista do que ele precisa dizer sim antes de Atlas começar.
