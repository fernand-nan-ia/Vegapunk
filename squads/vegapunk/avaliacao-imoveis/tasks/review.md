---
task: review()
responsavel: "@avaliador-chief"
responsavel_type: Agent
atomic_layer: Task
elicit: false

Entrada:
  - campo: laudo
    tipo: object
    origem: Handoff
    obrigatorio: true

Saida:
  - campo: parecer_qualidade
    tipo: object
    destino: Console
    persistido: false

Checklist:
  - "[ ] 8 critérios de qualidade aplicados"
  - "[ ] Rastreabilidade de cada valor verificada"
  - "[ ] Veredito: aprovar / devolver"
---

# Task: Review — Revisão de Qualidade do Laudo

## Metadata

| Campo | Valor |
|---|---|
| Task ID | `avaliacao-imoveis:review` |
| Comando | `@avaliacao-imoveis:avaliador-chief *review "{laudo}"` |
| Orquestrador | `avaliador-chief` (Roland) |
| Propósito | Avaliar o laudo contra os 8 critérios antes da decisão de aprovação |

## Inputs

| Input | Origem | Obrigatório | Descrição |
|---|---|---|---|
| `laudo` | Handoff (@redator-laudos / @revisor-adversarial) | Sim | Laudo a revisar |
| `veredito_adversarial` | @revisor-adversarial | Não | Resultado da revisão adversarial |

## Preconditions

- Laudo redigido e idealmente já passado pelo @revisor-adversarial
- `data/normas-tecnicas.md` disponível

## Phases

### Fase 1: Conferir os 8 critérios de qualidade
1. Fim e grau-alvo definidos antes do ciclo?
2. Amostra suficiente e pertinente ao método?
3. Tratamento é regressão? Se fatores, fallback justificado?
4. Cada valor rastreia para amostra + norma + tratamento?
5. Patologias/estado de conservação impactaram o valor de forma fundamentada?
6. Ressalvas e condições limitantes explícitas?
7. Passou pelo @revisor-adversarial e sobreviveu?
8. Um perito da parte contrária derrubaria este laudo?

### Fase 2: Verificar enquadramento de grau
Conferir o grau declarado contra a tabela (`normas-tecnicas.md` §3/§4): pontos, itens obrigatórios, campo de arbítrio.

### Fase 3: Emitir parecer
Aprovar (segue para `*approve-laudo`) ou devolver ao especialista responsável pela fragilidade.

## Output Format

```yaml
parecer_qualidade:
  criterios: { c1: pass|fail, ..., c8: pass|fail }
  grau_declarado: "{I|II|III}"
  grau_confere: true|false
  fragilidades: [ "{item} -> @{agente responsável}" ]
  veredito: "aprovar|devolver"
```

## Veto Rules

1. NUNCA aprovar laudo que não passou pelo @revisor-adversarial.
2. NUNCA aprovar com valor sem rastreabilidade.
3. NUNCA aprovar grau declarado incompatível com a tabela.
4. A decisão final de aprovação é do `*approve-laudo` (exclusiva do chief).

## Completion Criteria

- [ ] 8 critérios aplicados
- [ ] Grau conferido contra a tabela
- [ ] Fragilidades atribuídas ao agente responsável
- [ ] Veredito emitido
