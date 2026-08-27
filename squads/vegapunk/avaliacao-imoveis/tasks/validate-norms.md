---
task: validate-norms()
responsavel: "@redator-laudos"
responsavel_type: Agent
atomic_layer: Task
elicit: false

Entrada:
  - campo: laudo
    tipo: document
    origem: Handoff
    obrigatorio: true

Saida:
  - campo: enquadramento
    tipo: object
    destino: Handoff
    persistido: true

Checklist:
  - "[ ] Pontuação por item calculada"
  - "[ ] Itens obrigatórios verificados"
  - "[ ] Grau global enquadrado"
---

# Task: Validate Norms — Compliance NBR e Enquadramento de Grau

## Metadata

| Campo | Valor |
|---|---|
| Task ID | `avaliacao-imoveis:validate-norms` |
| Comando | `@avaliacao-imoveis:redator-laudos *validate-norms` |
| Responsável | `redator-laudos` (Rama-Kandra) |
| Propósito | Conferir compliance NBR 14.653-2:2004 e enquadrar o grau de fundamentação/precisão |

## Inputs

| Input | Origem | Obrigatório | Descrição |
|---|---|---|---|
| `laudo` | @redator-laudos | Sim | Laudo redigido |
| `modelo_tratado` | @engenheiro-dados | Sim | Indicadores estatísticos |
| `grau_alvo` | @avaliador-chief | Sim | Meta a atingir |

## Preconditions

- `data/normas-tecnicas.md` §3/§4 disponível

## Phases

### Fase 1: Selecionar a tabela
Regressão → Tabelas 1/2/3. Fatores → Tabelas 4/5/6.

### Fase 2: Pontuar por item
Atribuir 1/2/3 pontos por item (grau I/II/III). Regressão: 7 itens. Fatores: 6 itens.

### Fase 3: Enquadramento global
- Regressão: pontos mínimos **18/11/7** (III/II/I); obrigatórios **itens 3,5,6,7**.
- Fatores: pontos mínimos **15/9/6**; obrigatórios **itens 3,5,6**.
- Aplicar tetos: códigos alocados → máx II; tratamento prévio por fatores em regressão → máx II.

### Fase 4: Precisão e arbítrio
Amplitude IC 80%: ≤30% (III) / 30–50% (II) / >50% (I). Conferir campo de arbítrio: ±15% (regressão) / 10% (fatores).

### Fase 5: Veredito vs. grau-alvo
Comparar grau atingido com o grau-alvo do fim. Se abaixo, listar o que falta.

## Output Format

```yaml
enquadramento:
  tabela: "regressao|fatores"
  pontos: {int}
  pontos_por_item: { i1:, i2:, ... }
  itens_obrigatorios_ok: true|false
  tetos_aplicados: [ "codigos_alocados:II" ]
  grau_fundamentacao: "{I|II|III}"
  grau_precisao: "{I|II|III}"
  grau_alvo: "{I|II|III}"
  atende_alvo: true|false
  lacunas: [ ]
```

## Veto Rules

1. NUNCA declarar grau acima do que a pontuação/itens obrigatórios sustentam.
2. NUNCA ignorar os tetos (códigos alocados / fatores em regressão → máx II).
3. NUNCA fixar precisão a priori — depende da amostra (NBR §9.1.1).
4. Grau < grau-alvo → reportar lacunas ao @avaliador-chief, não maquiar.

## Completion Criteria

- [ ] Tabela correta selecionada
- [ ] Pontuação e itens obrigatórios verificados
- [ ] Tetos aplicados
- [ ] Grau global vs. grau-alvo reportado
