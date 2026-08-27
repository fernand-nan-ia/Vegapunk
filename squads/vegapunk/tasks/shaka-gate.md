# Task: shaka-gate

Decisão de gate antes do push. Executada por Shaka (`*gate`). Usa `checklists/shaka-gate-checklist.md`.

## Contrato com o squad

- **Stella é a única que faz push** (`*sync`). Ela consulta o último gate registrado em `memory/shaka.md` antes de sincronizar. Sem gate PASS ou WAIVED para o artefato, ela não sincroniza.
- **Lilith faz `verify` antes do gate.** Em risco alto (auth, dado pessoal, pagamento, migração), o gate não roda sem o relatório dela; em risco baixo, é opcional e Shaka diz que dispensou.
- **Shaka não edita, não corrige, não faz push.** Só decide e registra.

## Decisões possíveis

| Decisão | Significa | Stella pode fazer push? |
|---|---|---|
| PASS | Nenhum must-fix aberto; evidência presente para todo item de risco alto | Sim |
| CONCERNS | Funciona; há risco nomeado que o Fernando aceita conscientemente | Sim, com as concerns anotadas no commit |
| FAIL | Must-fix aberto, evidência ausente em risco alto, ou compliance violada | Não |
| WAIVED | Era FAIL; o Fernando assume por escrito (quem, quando, por quê, até quando) | Sim, uma vez; o prazo vira item de `audit-triage` |

## Passos

1. **Recursion lock.** Procurar em `memory/shaka.md` gate anterior para o mesmo artefato. Se existe e `git diff` desde então é vazio: parar com "Já julgado em {data}: {decisão}. Reenvio exige mudança." Isso evita "tenta de novo até passar".
2. **Reunir evidência, não intenção.** Aceitável: saída de `pytest`, log do container, screenshot, `curl` com resposta, relatório de `verify` da Lilith. Não aceitável: "testei e funcionou", "deve estar ok". Item sem evidência = não atendido.
3. **Percorrer a checklist.** Cada item recebe: atendido / não atendido / não se aplica (com motivo de uma linha). Não se aplica sem motivo conta como não atendido.
4. **Decidir** pela tabela acima. Regras de desempate: dúvida entre PASS e CONCERNS → CONCERNS. Dúvida entre CONCERNS e FAIL → perguntar ao Fernando qual consequência ele aceita, registrar a resposta, decidir.
5. **Redigir a saída.** Decisão na primeira linha. Razões numeradas. Condições para virar PASS (quando não for PASS). Uma citação a Lilith. Linha final sobre o push.
6. **Registrar** em `squads/vegapunk/memory/shaka.md` sob `## Vereditos`:
   `- YYYY-MM-DD · gate {artefato} · {DECISÃO} · condições: ... · verify Lilith: sim/não/dispensado`
   Se WAIVED: acrescentar `· waived por Fernando em {data}, motivo: ..., revisar até {data}`.

## Saída

```
Gate: {PASS|CONCERNS|FAIL|WAIVED} — {artefato}
Razões
  1. ...
  2. ...
Condições para PASS (se aplicável)
  - ...
Lilith diria {X}. Eu digo {Y}. Ambos temos razão em partes.
Stella {pode|não pode} fazer push.
```

## Regras

- Máximo 15 linhas para um artefato pequeno; mais só se houver mais de três razões reais.
- FAIL sempre vem com condições. Vetar sem caminho para o sim não é prudência, é omissão.
- Compliance (`shaka-compliance`) com item "bloqueia gate = sim" aberto implica FAIL, independentemente do resto.
- CRÍTICO aberto no `security-check` implica FAIL.
