# vegapunk

Consulta a memória de conhecimento do Vegapunk (links de YouTube/TikTok/Instagram já extraídos e resumidos) para responder perguntas, deduzir recomendações ou trazer contexto para o projeto atual.

## Fonte

Vault: `/home/crazu/projetos/vegapunk/knowledge/`

- `INDEX.md` — uma linha por item: data · plataforma · título (link relativo) · tags · aplicabilidade `saas/cliente/estudo` · triagem
- `<plataforma>/*.md` — frontmatter YAML (`tags`, `applicability`, `triage`, `confidence`) + `## Resumo`, `## Pontos-chave`, `## Como aplicar`, `## Notas manuais`
- `_pending/` — itens sem extração; ignorar salvo pedido explícito

## Procedimento

1. Ler `INDEX.md` inteiro. Se não existir ou estiver vazio, informar que a memória está vazia e parar.
2. Selecionar candidatos por tags, título e aplicabilidade em relação a `$ARGUMENTS` e ao projeto atual (SaaS pessoal → `saas_pessoal`; site de cliente → `projeto_cliente`). Itens com `triage: discard` têm peso baixo.
3. Ler os `.md` selecionados (máx. 8; priorizar `confidence: alta` e triagem `apply_*`). Ler `## Notas manuais` — são anotações do usuário e valem mais que o resumo automático.
4. Responder a `$ARGUMENTS`:
   - Pergunta → resposta direta, citando cada item usado como `[título](caminho)`.
   - Pedido de dedução/recomendação → síntese cruzando os itens; separar o que a memória sustenta do que é inferência.
   - Pedido de aplicação no código → propor mudanças concretas no projeto atual, apontando o item de origem; só editar arquivos se o usuário pedir.
5. Se nada relevante existir, dizer isso claramente e sugerir o que mandar ao bot.

## Regras

- Nunca inventar conteúdo que não esteja nos arquivos; `confidence: baixa` deve ser sinalizado.
- Não editar arquivos do vault (são gerados pelo bot). Exceção: `## Notas manuais`, somente se o usuário pedir.
- Resposta em pt-BR, concisa, com fontes.
