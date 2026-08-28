# Checklist: pythagoras-acceptance-criteria

Aplicar a cada item P0/P1 do backlog antes de entregá-lo ao Stella (`*story`). Um "não" devolve o item para "Ideias" ou pede mais uma pergunta ao Fernando.

## Origem e valor
- [ ] O item tem origem registrada (item do vault citado, pedido do Fernando com data, bug observado com arquivo, ou planta de arquitetura).
- [ ] Está escrito para quem o item entrega valor (Fernando, cliente, usuário do SaaS) e o que muda para essa pessoa.
- [ ] Título é verbo + objeto ("adicionar rate limiting no login"), não tema ("segurança").

## Critérios de aceite
- [ ] Há entre 2 e 5 critérios, cada um no formato Dado / Quando / Então.
- [ ] Cada critério pode ser verificado por alguém que não escreveu o código: comando, clique, consulta ou resultado visível.
- [ ] Nenhum critério usa palavra vaga sem medida ("rápido", "melhor", "seguro") — ou a medida está ao lado.
- [ ] O caso de falha está coberto por pelo menos um critério (o que acontece quando dá errado).
- [ ] "Fora do escopo" tem ao menos um item, para o Atlas não construir demais.

## Dependências e risco
- [ ] Dependências de outros itens ou de decisões (`docs/decisions/`) estão listadas por id.
- [ ] O item não contradiz ADR aceito; se contradiz, há nota para abrir `*decision` antes.
- [ ] Módulos que o item toca foram conferidos contra a última planta (`*architecture`), se existir.

## Tamanho e prioridade
- [ ] Tamanho P/M/G atribuído, com "eu deduzo" quando é estimativa.
- [ ] Item G foi quebrado ou tem nota de por que não pode ser quebrado.
- [ ] Prioridade justificada pelas três perguntas (desbloqueia? tem prazo? custo vs. entrega?).
- [ ] Não há mais de 3 itens em P0.

## Entrega
- [ ] Item pronto para o Stella transformar em story sem precisar reperguntar a origem.
- [ ] Data da última priorização registrada no topo do `docs/backlog.md`.
