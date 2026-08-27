---
task: diagnose()
responsavel: "@avaliador-chief"
responsavel_type: Agent
atomic_layer: Task
elicit: true

Entrada:
  - campo: caso
    tipo: string
    origem: User Input
    obrigatorio: true

Saida:
  - campo: triagem
    tipo: object
    destino: Console
    persistido: false

Checklist:
  - "[ ] Fim da avaliação identificado (bancário/judicial/particular)"
  - "[ ] Grau-alvo definido conforme o fim"
  - "[ ] Estágio do caso e especialista primário designados"
---

# Task: Diagnose — Avaliação de Imóveis

## Metadata

| Campo | Valor |
|---|---|
| Task ID | `avaliacao-imoveis:diagnose` |
| Comando | `@avaliacao-imoveis:avaliador-chief *diagnose "{caso}"` |
| Orquestrador | `avaliador-chief` (Roland) |
| Propósito | Triar o caso, definir fim + grau-alvo + método, e designar o especialista certo |

## Inputs

| Input | Origem | Obrigatório | Descrição |
|---|---|---|---|
| `caso` | Usuário | Sim | Descrição do imóvel e da demanda |
| `fim` | Usuário/Auto | Não | bancário / judicial / particular |
| `prazo` | Usuário | Não | Restrições de prazo |

## Preconditions

- `config/config.yaml` carregado
- `data/routing-catalog.yaml` e `data/normas-tecnicas.md` disponíveis
- Agentes especialistas presentes em `agents/`

## Phases

### Fase 1: Identificar o FIM
Classificar bancário (Caixa/financiamento) · judicial (perícia) · particular (inventário/divisão/negociação). Em ambiguidade, **perguntar** (elicit).

### Fase 2: Definir grau-alvo (de `normas-tecnicas.md` §5)
- Bancário → Fundamentação **II** (mínimo)
- Judicial → Fundamentação **III** (se a amostra sustentar)
- Particular → Fundamentação **I–II** conforme demanda

### Fase 3: Identificar estágio e método
- Estágio: sem vistoria / sem amostra / sem planilha / sem laudo / laudo a revisar.
- Método: **regressão (padrão)**; fatores só fallback declarado.

### Fase 4: Designar especialista (de `routing-catalog.yaml`)
Mapear demanda → especialista primário (+ secundário se complexo). Briefar com tipo/localização do imóvel, fim, grau-alvo, restrições.

## Output Format

```yaml
triagem:
  resumo: "{1 linha}"
  fim: "{bancario|judicial|particular}"
  grau_alvo: "{Fundamentação I|II|III}"
  metodo: "regressao|fatores(fallback)"
  estagio: "{sem-vistoria|sem-amostra|sem-planilha|sem-laudo|revisar}"
  especialista_primario: "{agent-id}"
  especialista_secundario: "{agent-id|nenhum}"
  briefing: "{o que o especialista precisa saber}"
```

## Veto Rules

1. NUNCA iniciar o ciclo sem fim e grau-alvo definidos.
2. NUNCA designar mais de um especialista primário.
3. NUNCA assumir dados não informados — perguntar.
4. Amostra insuficiente para qualquer método → declarar **parecer técnico** (não laudo), NBR 14.653-2:2004 §9.1.2.

## Completion Criteria

- [ ] Fim e grau-alvo definidos
- [ ] Estágio e método identificados
- [ ] Especialista designado e briefado
- [ ] Output no schema acima
