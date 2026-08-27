---
task: draft-laudo()
responsavel: "@redator-laudos"
responsavel_type: Agent
atomic_layer: Task
elicit: false

Entrada:
  - campo: dossie
    tipo: object
    origem: Handoff
    obrigatorio: true

Saida:
  - campo: laudo
    tipo: document
    destino: Handoff
    persistido: true

Checklist:
  - "[ ] Estrutura NBR completa"
  - "[ ] Cada afirmação rastreável"
  - "[ ] Ressalvas e ART declarados"
---

# Task: Draft Laudo — Redação do Laudo (Rama-Kandra)

## Metadata

| Campo | Valor |
|---|---|
| Task ID | `avaliacao-imoveis:draft-laudo` |
| Comando | `@avaliacao-imoveis:redator-laudos *draft-laudo "{caso}"` |
| Responsável | `redator-laudos` (Rama-Kandra) |
| Propósito | Converter vistoria + amostra + modelo em laudo NBR-compliant e defensável |

## Inputs

| Input | Origem | Obrigatório | Descrição |
|---|---|---|---|
| `dossie` | @inspetor-tecnico + @pesquisador-mercado + @engenheiro-dados | Sim | Vistoria + amostra + modelo |
| `fim` / `grau_alvo` | @avaliador-chief | Sim | Define enquadramento e rigor |

## Preconditions

- `data/normas-tecnicas.md` disponível
- Vistoria, amostra e modelo entregues pelos especialistas

## Phases

### Fase 1: Estrutura (memorial)
Seções: objeto/objetivo/finalidade, identificação e caracterização do imóvel, **vistoria** (de @inspetor-tecnico), **pesquisa de mercado** (de @pesquisador-mercado), **tratamento e modelo** (de @engenheiro-dados), resultado e campo de arbítrio, **ressalvas e condições limitantes**, enquadramento de grau, responsabilidade técnica (ART/RRT), anexos.

### Fase 2: Redação coesa e rastreável
Cada afirmação rastreia para evidência (vistoria/amostra/modelo) **e** para a norma (NBR 14.653-1:2019 / -2:2004). Endereço completo e pontos específicos (atenção: completude e coerência descritiva — principal causa de retificação bancária).

### Fase 3: Ressalvas
Redigir explicitamente o que não foi verificado / limitações sensoriais / condições limitantes. Nunca omitir.

### Fase 4: Enquadramento de grau
Declarar o grau atingido conforme `validate-norms` (tabela `normas-tecnicas.md` §3/§4) e justificar.

## Output Format

```yaml
laudo:
  secoes: [ objeto, caracterizacao, vistoria, pesquisa, tratamento, resultado, ressalvas, grau, ART, anexos ]
  valor: { estimativa_pontual, campo_arbitrio }
  grau_declarado: "{I|II|III}"
  rastreabilidade: "completa|pendente:{itens}"
  ressalvas: [ ]
  pendencias: [ ]
```

## Veto Rules

1. ZERO valor inventado; ZERO afirmação órfã (Constitutional Gate do laudo).
2. NUNCA omitir ressalvas/condições limitantes.
3. NUNCA esquecer referência a ART/RRT e responsabilidade técnica.
4. NUNCA declarar grau sem justificar contra a tabela.
5. NUNCA aprovar o próprio laudo (autoridade do @avaliador-chief).

## Completion Criteria

- [ ] Estrutura NBR completa
- [ ] Cada afirmação rastreável
- [ ] Ressalvas e ART declarados
- [ ] Grau enquadrado e justificado
- [ ] Handoff pronto para @revisor-adversarial
