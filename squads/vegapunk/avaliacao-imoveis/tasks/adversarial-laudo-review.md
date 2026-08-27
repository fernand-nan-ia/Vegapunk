---
task: adversarial-laudo-review()
responsavel: "@revisor-adversarial"
responsavel_type: Agent
atomic_layer: Task
elicit: false

Entrada:
  - campo: laudo
    tipo: document
    origem: Handoff
    obrigatorio: true

Saida:
  - campo: veredito
    tipo: object
    destino: Handoff
    persistido: true

Checklist:
  - "[ ] Ataque pelos 3 adversários"
  - "[ ] Fragilidades com vetor e reparo"
  - "[ ] Veredito emitido (não aprova)"
---

# Task: Adversarial Laudo Review — Simulação de Rejeição (Agent Johnson)

## Metadata

| Campo | Valor |
|---|---|
| Task ID | `avaliacao-imoveis:adversarial-laudo-review` |
| Comando | `@avaliacao-imoveis:revisor-adversarial *adversarial-review "{laudo}"` |
| Responsável | `revisor-adversarial` (Agent Johnson) |
| Propósito | Quebrar o laudo antes do banco/juízo/comprador — último portão pré-entrega |

## Inputs

| Input | Origem | Obrigatório | Descrição |
|---|---|---|---|
| `laudo` | @redator-laudos | Sim | Laudo redigido + enquadrado |
| `fim` | @avaliador-chief | Sim | Define qual adversário pesa mais |

## Preconditions

- Laudo redigido e com `validate-norms` executado
- `data/normas-tecnicas.md` (compartilhada) + checklist `bank-defensibility.md`
- **KB exclusiva carregada** — `data/revisor-adversarial/` (README + os 4 arquivos por vetor). Sem ela, o ataque cai ao genérico — fragilidade do próprio agente.

## Phases

### Fase 1: Ataque "banco/Caixa" (`*simulate-bank`)
Presumir má-fé do analista. Caçar: **incoerência das observações**, **falta de informação** (endereço, pontos específicos), variáveis mal escolhidas/códigos alocados, fundamentação fraca, valor < valor de financiamento, micronumerosidade. (Principais causas reais de retificação — especialista.)
**Consultar `data/revisor-adversarial/rejeicao-banco.md`** — aplicar as entradas das seções 1–6 (eixos) e 7 (padrões institucionais) ao laudo. Cada fragilidade encontrada cita o `id` da entrada como `fonte` no veredito.

### Fase 2: Ataque "judicial" (`*simulate-court`)
Vestir o assistente técnico da parte contrária + juízo. Caçar: rastreabilidade incompleta, fontes não identificadas (obrigatório no judicial), pressupostos não testados, grau superdeclarado, ressalvas ausentes.
**Consultar `data/revisor-adversarial/pericia-judicial.md`** — aplicar entradas das seções 1–6 + jurisprudência consolidada (§7) e quesitos típicos (§8). Cita o nº de processo/decisão como `fonte` quando houver.

### Fase 3: Ataque "comprador/vendedor" (`*simulate-buyer`)
Comprador cético: estado de conservação subvalorizado/supervalorizado, patologias minimizadas, comparáveis não pertinentes, campo de arbítrio mal justificado.
**Consultar `data/revisor-adversarial/comprador-cetico.md`** — aplicar entradas das seções 1–6 + padrões por contexto (§7) e glossário leigo (§8).

### Fase 4: Veredito (`*verdict`)
Consolidar fragilidades. Cada uma com **vetor de ataque** + **reparo sugerido** + agente responsável. NÃO aprovar — só veredito.
**Cruzar com `data/revisor-adversarial/fragilidades-recorrentes.md`** — fragilidades que aparecem em ≥2 vetores ganham prioridade no veredito (heurística §1) e podem forçar `resultado: devolver` (heurística §3).

## Output Format

```yaml
veredito:
  fim_predominante: "{bancario|judicial|particular}"
  fragilidades:
    - origem: "{banco|juizo|comprador}"
      item: "{...}"
      severidade: "{critica|alta|media|baixa}"
      vetor_ataque: "{como o adversário derruba}"
      reparo: "{o que corrigir}"
      responsavel: "@{agente}"
      fonte_kb: "{id da entrada na KB — ex.: banco-001, judicial-012, transversal-003 — ou null se ainda não catalogada}"
  resultado: "defensavel|devolver"
  resumo: "{1-2 linhas}"
```

## Veto Rules

1. NUNCA aprovar o laudo — aprovação é exclusiva do @avaliador-chief.
2. NUNCA suavizar o ataque por cortesia — mata o propósito do agente.
3. NUNCA apontar fragilidade sem vetor de ataque e reparo.
4. NUNCA pular um dos 3 adversários quando o fim é misto.
5. Fim judicial sem fontes identificadas → fragilidade automática "devolver".

## Completion Criteria

- [ ] 3 adversários simulados
- [ ] Fragilidades com vetor + reparo + responsável + severidade
- [ ] Resultado (defensável/devolver) emitido
- [ ] Handoff de volta ao @avaliador-chief

---

## Modos de revisão

A task suporta dois modos de profundidade:

### Modo enxuto (padrão — `*adversarial-review`)

Output conforme schema acima (`veredito.fragilidades[]`). Adequado para:
- Uso pessoal do operador (engenheiro credenciado)
- Sanity check rápido antes de entrega
- Iteração ágil em laudos em desenvolvimento

### Modo deep-review (formal — quando solicitado explicitamente)

Output expandido conforme `data/revisor-adversarial/templates/deep-review-ufsc-style.md` — baseado no template do Prof. Hochheim (UFSC, análise do laudo Ed. Santa Clara). Adequado para:
- Entregas formais (peças processuais, pareceres independentes)
- Quando o laudo é objeto de impugnação prevista
- Uso futuro do CalcImov em produção (ver `[[calcimov-producao-ressalvas]]`)

**Como ativar:** o usuário pede explicitamente "deep-review" ou "análise UFSC-style" no comando. Sem isso, modo enxuto é o padrão.

**Diferenças principais (deep vs enxuto):**
- Adiciona seções de `identificacao` / `contexto_normativo` / `analise_amostra` / `analise_variaveis` / `procedimentos_especiais` / `conclusao` / `ressalva_escopo`
- `criticas` com tipo (`incompleto|ausente|incorreto|tendencioso`) além de severidade
- Linguagem técnica acadêmica (sem ataques pessoais, equilibrada — aponta o que está OK também)
- Inclui ressalva de escopo explícita (a análise não substitui nova avaliação)
