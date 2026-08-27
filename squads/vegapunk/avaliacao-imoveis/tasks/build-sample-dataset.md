---
task: build-sample-dataset()
responsavel: "@engenheiro-dados"
responsavel_type: Agent
atomic_layer: Task
elicit: false

Entrada:
  - campo: amostra_saneada
    tipo: object
    origem: Handoff
    obrigatorio: true

Saida:
  - campo: modelo_tratado
    tipo: object
    destino: Handoff
    persistido: true

Checklist:
  - "[ ] Planilha amostral montada"
  - "[ ] Regressão rodada + pressupostos testados"
  - "[ ] Indicadores de grau reportados"
---

# Task: Build Sample Dataset — Planilha + Regressão (Dozer)

## Metadata

| Campo | Valor |
|---|---|
| Task ID | `avaliacao-imoveis:build-sample-dataset` |
| Comando | `@avaliacao-imoveis:engenheiro-dados *build-dataset` |
| Responsável | `engenheiro-dados` (Dozer); colabora com `pesquisador-mercado` |
| Propósito | Transformar a amostra saneada em modelo defensável (NBR 14.653-2:2004 Anexo A) |

## Inputs

| Input | Origem | Obrigatório | Descrição |
|---|---|---|---|
| `amostra_saneada` | @pesquisador-mercado | Sim | Comparáveis tratados |
| `depreciacao` | @inspetor-tecnico | Não | Fator do estado de conservação |
| `grau_alvo` | @avaliador-chief | Sim | Define exigências estatísticas |

## Preconditions

- `data/normas-tecnicas.md` §3/§3.1 disponível
- Amostra com natureza e atributos identificados

## Phases

### Fase 1: Planilha amostral
Estruturar variável dependente + independentes; incorporar fator de depreciação física. Variável dependente apresentada **não transformada** no laudo.

### Fase 2: Regressão (método padrão)
Rodar regressão linear. Verificar **micronumerosidade**: `n ≥ 3(k+1)`; `ni` conforme dicotômicas/códigos.

### Fase 3: Pressupostos (Anexo A)
Testar: linearidade, **normalidade** (Jarque-Bera/KS-Stephens), **homocedasticidade** (Park/White), **autocorrelação** (Durbin-Watson), **multicolinearidade** (matriz corr. > 0,80), **outliers** (Cook — retirada com justificativa).

### Fase 4: Significância e grau
Teste **t** (regressores), teste **F** (≤ 1%). Aferir nível de significância vs. grau-alvo (`normas-tecnicas.md` §3): regressores ≤10/20/30%, demais ≤1/5/10%. R² e R² ajustado. Campo de arbítrio ±15% da estimativa pontual.

### Fase 5: Fallback declarado
Se a amostra não sustenta regressão → tratamento por fatores (Anexo B): cada fator e preço homogeneizado ∈ [0,50;1,50]; campo de arbítrio 10%. **Declarar o fallback e justificar**.

## Output Format

```yaml
modelo_tratado:
  metodo: "regressao|fatores(fallback declarado)"
  n: {int}
  k: {int}
  micronumerosidade_ok: true|false
  pressupostos: { normalidade, homocedasticidade, autocorrelacao, multicolinearidade, outliers }
  testes: { F: "{p}", regressores_signif: "{%}", R2: , R2_ajustado: }
  estimativa_pontual: {valor}
  campo_arbitrio: "{±15% (regressão) | 10% (fatores)}"
  grau_atingido: "{I|II|III}"
  ressalvas_estatisticas: [ ]
```

## Veto Rules

1. NUNCA entregar modelo sem diagnóstico de pressupostos.
2. NUNCA remover outlier sem registrar e justificar.
3. NUNCA usar fatores sem declarar explicitamente o fallback.
4. Códigos alocados → teto Grau II (declarar).
5. `n < 3(k+1)` → micronumerosidade: reportar ao @avaliador-chief.

## Completion Criteria

- [ ] Planilha montada
- [ ] Regressão + pressupostos testados
- [ ] Significância e grau aferidos
- [ ] Campo de arbítrio definido
- [ ] Handoff pronto para @redator-laudos
