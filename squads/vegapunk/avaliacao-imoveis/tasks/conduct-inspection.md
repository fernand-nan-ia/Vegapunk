---
task: conduct-inspection()
responsavel: "@inspetor-tecnico"
responsavel_type: Agent
atomic_layer: Task
elicit: true

Entrada:
  - campo: imovel
    tipo: object
    origem: User Input
    obrigatorio: true

Saida:
  - campo: laudo_inspecao
    tipo: object
    destino: Handoff
    persistido: true

Checklist:
  - "[ ] 9 etapas IBAPE percorridas"
  - "[ ] Anomalias classificadas por origem e prioridade"
  - "[ ] Estado de conservação e limitações declarados"
---

# Task: Conduct Inspection — Vistoria Técnica (IBAPE 2025)

## Metadata

| Campo | Valor |
|---|---|
| Task ID | `avaliacao-imoveis:conduct-inspection` |
| Comando | `@avaliacao-imoveis:inspetor-tecnico *inspect "{imóvel}"` |
| Responsável | `inspetor-tecnico` (Sentinel) |
| Propósito | Vistoria sistêmica e diagnóstico de patologias conforme Norma IBAPE 2025 |

## Inputs

| Input | Origem | Obrigatório | Descrição |
|---|---|---|---|
| `imovel` | Usuário | Sim | Tipo, endereço, documentos disponíveis |
| `imagens` | Usuário | Não | Fotos (acionam `analyze-pathology-images`) |
| `fim` | @avaliador-chief | Sim | Define a profundidade exigida |

## Preconditions

- `data/patologias-catalogo.md` e `data/normas-tecnicas.md` (§6) disponíveis
- Acesso ao imóvel ou a imagens de qualidade

## Phases (9 etapas IBAPE 2025)

1. **Anamnese** — entrevista (síndico/proprietário/usuário): histórico, reformas, intervenções.
2. **Análise documental** — documentos disponíveis e **ausências** (ausência pode ser irregularidade).
3. **Vistoria sistêmica** — sensorial; testes simples de acionamento; **sem ensaios/prospecções**.
4. **Classificação de origem** — construtiva/endógena, exógena, funcional, falha (uso/operação/manutenção).
5. **Recomendações técnicas** — ações para preservar/recuperar desempenho; aprofundamento quando necessário.
6. **Patamares de prioridade** — P1 (saúde/segurança/vida útil), P2 (funcional parcial), P3 (planejável).
7. **Avaliação da manutenção** (NBR 5674).
8. **Avaliação do uso** (regular/irregular).
9. **Laudo de inspeção** — consolidado para handoff.

Para cada patologia: usar `patologias-catalogo.md` — ler geometria/padrão → causa provável → severidade → reflexo no estado de conservação/depreciação.

## Output Format

```yaml
laudo_inspecao:
  anamnese: "{resumo}"
  documentos: { fornecidos: [], ausentes: [] }
  patologias:
    - tipo: "{ex: trinca escalonada 45°}"
      origem: "{construtiva|exogena|funcional|falha}"
      causa_provavel: "{...}"
      prioridade: "{P1|P2|P3}"
  estado_conservacao: "{descrição + fator de depreciação proposto}"
  limitacoes: "{o que não foi possível verificar}"
  recomendacoes_aprofundamento: [ ]
```

## Veto Rules

1. NUNCA superestimar severidade além do que a evidência sensorial sustenta.
2. NUNCA omitir o que não foi possível inspecionar — declarar como limitação/ressalva.
3. NUNCA opinar sobre preço (escopo do ciclo, não da vistoria).
4. P1 sistêmico (recalque/estrutura/corrosão) → ressalva obrigatória + recomendação de aprofundamento.

## Completion Criteria

- [ ] 9 etapas percorridas
- [ ] Patologias classificadas (origem + prioridade)
- [ ] Estado de conservação + fator de depreciação propostos
- [ ] Limitações declaradas
