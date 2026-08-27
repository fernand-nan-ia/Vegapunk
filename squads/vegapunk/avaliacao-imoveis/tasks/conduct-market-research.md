---
task: conduct-market-research()
responsavel: "@pesquisador-mercado"
responsavel_type: Agent
atomic_layer: Task
elicit: true

Entrada:
  - campo: imovel_avaliando
    tipo: object
    origem: User Input
    obrigatorio: true

Saida:
  - campo: amostra_saneada
    tipo: object
    destino: Handoff
    persistido: true

Checklist:
  - "[ ] Fontes regionais priorizadas"
  - "[ ] Natureza (oferta/transação) identificada por dado"
  - "[ ] Amostra dimensionada ao grau-alvo"
---

# Task: Conduct Market Research — Pesquisa de Mercado (Trainman)

## Metadata

| Campo | Valor |
|---|---|
| Task ID | `avaliacao-imoveis:conduct-market-research` |
| Comando | `@avaliacao-imoveis:pesquisador-mercado *research "{imóvel} {região}"` |
| Responsável | `pesquisador-mercado` (Trainman) |
| Propósito | Coletar, sanear e preparar a amostra de comparáveis (NBR 14.653-2:2004 §8.2.1.3) |

## Inputs

| Input | Origem | Obrigatório | Descrição |
|---|---|---|---|
| `imovel_avaliando` | Usuário/@inspetor-tecnico | Sim | Atributos do avaliando |
| `fim` / `grau_alvo` | @avaliador-chief | Sim | Define a quantidade mínima |
| `regiao` | Usuário | Sim | Município/bairro do avaliando |

## Preconditions

- `data/fontes-mercado.md` e `data/normas-tecnicas.md` disponíveis
- Atributos do avaliando conhecidos (situação, destinação, aproveitamento, físicas)

## Phases

### Fase 1: Estratégia de fontes
Priorizar **fontes regionais do mesmo município** (especialista); portais nacionais como complemento. Diversificar.

### Fase 2: Coleta
Coletar comparáveis com endereço completo, especificação/quantificação das variáveis (mesmo as não usadas). Registrar **origem, data, contato**.

### Fase 3: Classificar natureza
Marcar cada dado como **oferta** ou **transação**. Oferta carrega superestimativa — sinalizar para desconto/elasticidade no tratamento.

### Fase 4: Pertinência e raio
Selecionar por similaridade real ao avaliando (situação/destinação/aproveitamento/físicas). Raio justificado pela similaridade, não conveniência.

### Fase 5: Dimensionamento
Garantir quantidade conforme grau-alvo (`normas-tecnicas.md`): regressão `n ≥ 6(k+1)|4(k+1)|3(k+1)` (III/II/I); fatores 12/6/3.

### Fase 6: Saneamento preliminar
Remover duplicidades/suspeitos (registrar). Marcar prováveis outliers (decisão final é do @engenheiro-dados). Preparar atributos para homogeneização/inferência.

## Output Format

```yaml
amostra_saneada:
  n_total: {int}
  fontes: [ { origem, data, regional: true|false } ]
  dados: [ { id, natureza: oferta|transacao, atributos: {...}, origem } ]
  outliers_marcados: [ ]
  aderencia_grau_alvo: "{ok|insuficiente}"
  observacoes: "{...}"
```

## Veto Rules

1. NUNCA misturar oferta e transação sem identificar a natureza.
2. NUNCA incluir comparável sem origem rastreável.
3. NUNCA deletar outlier em silêncio — marcar e justificar.
4. Avaliação judicial → fontes obrigatoriamente identificáveis/conferíveis.
5. Amostra insuficiente para o grau-alvo → reportar ao @avaliador-chief (não forçar).

## Completion Criteria

- [ ] Fontes regionais priorizadas e diversificadas
- [ ] Natureza identificada por dado
- [ ] Amostra dimensionada ao grau-alvo
- [ ] Saneamento preliminar + outliers marcados
- [ ] Handoff pronto para @engenheiro-dados
