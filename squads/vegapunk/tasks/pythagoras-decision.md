# Task: pythagoras-decision

Registro de decisão técnica (ADR), executado por Pythagoras (`*decision {título}`). Absorvido do FURY `architect`, reduzido ao essencial: uma decisão, seu contexto, as alternativas e o que ela custa. Um ADR é memória que sobrevive ao corpo — e ao chat.

## Entrada
- `{título}` — a decisão em uma frase ("usar SQLite em vez de Postgres", "polling em vez de webhook").
- Opcional: `--list` (só lista os ADRs existentes), `--revisar {id}` (marca um ADR como substituído).

## Regra de ouro
Registrar a decisão como ela foi tomada, não como deveria ter sido. O que motivou, mesmo que fraco, entra como registro; a crítica fica para Lilith. Se o motivo não é conhecido, escrever "motivo: não há registro".

## Passos
1. **Localizar.** `docs/decisions/` no projeto ativo; criar se não existir. Numerar sequencialmente `NNNN-{slug}.md`. Ler os ADRs existentes para não duplicar e para citar os relacionados.
2. **Recolher contexto.** Três fontes, nesta ordem:
   - Vault: itens que tocam o tema (`consult-punk-records.md`), citados como `[título](caminho)`.
   - Projeto: commits (`git log --oneline -S "{palavra}"`), comentários, `HANDOFF.md`, `## Notas manuais`.
   - Fernando: perguntar o que ele lembra, só o que faltar. Anotar como "dito por Fernando em YYYY-MM-DD".
3. **Alternativas.** Mínimo duas além da escolhida, cada uma com uma linha do porquê foi descartada. Alternativa que ninguém considerou na época entra como "não considerada (registro em branco)".
4. **Consequências.** O que fica mais fácil, o que fica mais difícil, o que passa a ser proibido. Custo em tokens/dinheiro/tempo quando houver número (York).
5. **Reversibilidade.** Como desfazer, em 2–4 passos, e o que se perde ao desfazer. Se não dá para desfazer, escrever isso.
6. **Escrever** com `templates/pythagoras-adr.md`. Status: `proposta` (ainda não aplicada), `aceita`, `substituída por NNNN`.
7. **Ligar.** Adicionar linha na tabela de decisões da próxima `*architecture`; se o ADR nasce de um item do backlog, referenciar o id.
8. **Encaminhar.** Decisão nova ainda não julgada → Shaka (`*judge`). Decisão com risco visível → Lilith (`*premortem`). Registrar no `Diário`: "ADR NNNN criado".

## Não fazer
- Decidir pelo Fernando: o ADR registra; a escolha é dele.
- Editar ADR aceito para mudar o conteúdo — cria-se outro que o substitui.
- Omitir alternativa porque parece óbvia demais.
