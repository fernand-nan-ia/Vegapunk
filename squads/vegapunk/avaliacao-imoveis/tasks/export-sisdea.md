---
task: export-sisdea()
responsavel: "@engenheiro-dados"
responsavel_type: Agent
atomic_layer: Task
elicit: false

Entrada:
  - campo: modelo_tratado
    tipo: object
    origem: Handoff
    obrigatorio: true

Saida:
  - campo: pacote_dados
    tipo: object
    destino: File
    persistido: true

Checklist:
  - "[ ] Schema de destino mapeado"
  - "[ ] Rastreabilidade preservada"
  - "[ ] Pacote validado"
---

# Task: Export SisDea — Ponte de Dados (Dozer)

## Metadata

| Campo | Valor |
|---|---|
| Task ID | `avaliacao-imoveis:export-sisdea` |
| Comando | `@avaliacao-imoveis:engenheiro-dados *export-sisdea` |
| Responsável | `engenheiro-dados` (Dozer) |
| Propósito | Exportar amostra/modelo para SisDea ou CalcImov preservando rastreabilidade |

## Inputs

| Input | Origem | Obrigatório | Descrição |
|---|---|---|---|
| `modelo_tratado` | @engenheiro-dados (build-sample-dataset) | Sim | Amostra + modelo + indicadores |
| `destino` | Usuário | Sim | `sisdea` ou `calcimov` |

## Preconditions

- `build-sample-dataset` concluído e modelo diagnosticado
- Schema de destino conhecido (ou solicitar ao usuário)

## Phases

### Fase 1: Mapear schema de destino
SisDea (formato de amostra/variáveis) ou CalcImov (estrutura de requisitos da recriação — ver bridge). Solicitar especificação se não conhecida.

### Fase 2: Mapear campos
Cada variável/dado → campo de destino. Preservar **origem, data, natureza (oferta/transação)** de cada comparável.

### Fase 3: Validar pacote
Conferir integridade: nº de dados, variáveis, valor estimado, campo de arbítrio, grau. Sem perda de rastreabilidade.

### Fase 4: Emitir pacote
Gerar arquivo/estrutura exportável + log de mapeamento.

## Output Format

```yaml
pacote_dados:
  destino: "sisdea|calcimov"
  n_dados: {int}
  campos_mapeados: { origem -> destino }
  rastreabilidade: "preservada|perdida:{itens}"
  arquivo: "{path/identificador}"
  log_mapeamento: [ ]
```

## Veto Rules

1. NUNCA exportar perdendo origem/data/natureza dos dados.
2. NUNCA exportar modelo sem diagnóstico estatístico concluído.
3. Schema de destino desconhecido → solicitar, não inventar.
4. Para CalcImov, alinhar com o contrato da bridge (squad → software-dev).

## Completion Criteria

- [ ] Schema mapeado
- [ ] Rastreabilidade preservada
- [ ] Pacote validado e emitido
- [ ] Log de mapeamento gerado
