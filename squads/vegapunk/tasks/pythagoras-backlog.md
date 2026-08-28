# Task: pythagoras-backlog

Backlog priorizado com critérios de aceite, executado por Pythagoras (`*backlog {projeto}`). Absorvido do FURY `po`, sem ClickUp/Jira/sprints: o backlog é um arquivo Markdown no projeto, e cada item pronto vira insumo da `*story` do Stella.

## Entrada
- `{projeto}` — `saas`, `cliente` ou caminho. Opcional: `--add "{item}"` (só acrescenta um item), `--top {n}` (só mostra os n primeiros), `--fonte {item do vault}` (item nasce de um registro).

## Regra de ouro
Todo item tem origem registrada (vault, pedido do Fernando, bug observado, planta de arquitetura) e critérios de aceite testáveis. Item sem critério é ideia, não backlog — fica em "Ideias" até ganhar critério.

## Passos
1. **Localizar o backlog.** `docs/backlog.md` no projeto. Ausente → criar com o `templates/pythagoras-backlog.md`. Ler inteiro antes de mexer.
2. **Coletar candidatos** (só quando não for `--add`):
   - Vault: itens com triagem `apply_saas` / `apply_cliente` que ainda não têm item no backlog. Citar cada um como `[título](caminho)`.
   - Memória: pedidos e decisões em `memory/pythagoras.md › Diário`.
   - Projeto: `TODO`, `FIXME`, `HANDOFF.md › Próximos passos`, stories abertas.
   - Perguntar ao Fernando se há algo que ele carrega na cabeça e não está em lugar nenhum.
3. **Escrever cada item** com o bloco do template: id, título (verbo + objeto), origem, valor para quem, critérios de aceite (Dado/Quando/Então, 2–5), fora do escopo, dependências, tamanho (P/M/G, estimativa honesta com "eu deduzo").
4. **Priorizar** com três perguntas, respondidas por escrito:
   - Desbloqueia algo ou alguém? (dependência)
   - Tem prazo ou cliente esperando? (urgência)
   - Quanto custa em tokens/horas versus o que entrega? (York sabe o custo; Shaka julga o valor — citar se já opinaram)
   Ordem final: P0 (esta semana) · P1 (próximas) · P2 (quando sobrar) · Ideias. No máximo 3 itens em P0.
5. **Detectar conflitos.** Dois itens que mexem no mesmo módulo, item que contradiz decisão em `docs/decisions/`, item que a planta de arquitetura marca como frágil. Listar sob "Atenção".
6. **Passar pelo checklist** `checklists/pythagoras-acceptance-criteria.md` em cada item P0/P1.
7. **Salvar** `docs/backlog.md` e mostrar o topo (P0 + P1) no chat, com a origem de cada item.
8. **Encaminhar.** "Para o P0-1, Stella abre `*story`; Atlas constrói; Lilith faz o pré-mortem antes." Registrar no `Diário` a data da priorização.

## Não fazer
- Priorizar tudo como P0.
- Inventar critério de aceite sem saber como se verifica.
- Criar story (Stella) ou implementar (Atlas).
- Estimar prazo em dias para o Fernando sem marcar "eu deduzo".
