---
task: analyze-pathology-images()
responsavel: "@inspetor-tecnico"
responsavel_type: Agent
atomic_layer: Task
elicit: false

Entrada:
  - campo: imagem
    tipo: image
    origem: User Input
    obrigatorio: true

Saida:
  - campo: analise_visual
    tipo: object
    destino: Handoff
    persistido: true

Checklist:
  - "[ ] Geometria/padrão lidos da imagem"
  - "[ ] Causa provável inferida com grau de confiança"
  - "[ ] Limitações da imagem declaradas"
---

# Task: Analyze Pathology Images — Capacidade de Visão (Sentinel)

## Metadata

| Campo | Valor |
|---|---|
| Task ID | `avaliacao-imoveis:analyze-pathology-images` |
| Comando | `@avaliacao-imoveis:inspetor-tecnico *scan-image "{imagem}"` |
| Responsável | `inspetor-tecnico` (Sentinel) |
| Propósito | Analisar imagem para diagnóstico de patologias — capacidade de visão (gap IDS, CREATE) |

## Inputs

| Input | Origem | Obrigatório | Descrição |
|---|---|---|---|
| `imagem` | Usuário | Sim | Foto da patologia/imóvel |
| `contexto` | @inspetor-tecnico | Não | Dados da vistoria em andamento |

## Preconditions

- Imagem com resolução/ângulo minimamente analisáveis
- `data/patologias-catalogo.md` disponível

## Phases

### Fase 1: Leitura da imagem
Descrever objetivamente o que a imagem mostra: elemento construtivo, localização aparente, manifestação visível.

### Fase 2: Classificação geométrica (de `patologias-catalogo.md`)
- Fissura (fina/superficial) × trinca (profunda) × rachadura (atravessante/P1).
- Direção: horizontal (sobrecarga) · vertical (retração/expansão) · 45°/escalonada (recalque) · mapeada (retração superficial).
- Outros: infiltração, eflorescência, corrosão de armadura, destacamento.

### Fase 3: Inferência de causa + severidade
Causa provável com **grau de confiança** (alto/médio/baixo). Nunca afirmar além do que a imagem sustenta.

### Fase 4: Limitações
Declarar explicitamente: ângulo, resolução, ausência de escala, ausência de ensaio in loco, necessidade de vistoria presencial para confirmar.

## Output Format

```yaml
analise_visual:
  descricao: "{o que a imagem mostra}"
  patologia: "{classificação}"
  geometria: "{direção/padrão}"
  causa_provavel: "{...}"
  confianca: "{alta|media|baixa}"
  severidade: "{estimada}"
  prioridade: "{P1|P2|P3}"
  limitacoes: "{declaração obrigatória}"
  requer_vistoria_presencial: true|false
```

## Veto Rules

1. NUNCA emitir diagnóstico sem declarar as limitações da imagem.
2. NUNCA classificar severidade como definitiva a partir de imagem isolada.
3. NUNCA substituir a vistoria presencial — a imagem é indício, não prova.
4. Confiança baixa → recomendar explicitamente vistoria presencial.

## Completion Criteria

- [ ] Geometria/padrão lidos
- [ ] Causa provável + grau de confiança
- [ ] Severidade/prioridade estimadas
- [ ] Limitações declaradas
