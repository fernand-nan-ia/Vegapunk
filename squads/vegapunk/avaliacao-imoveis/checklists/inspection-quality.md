# Inspection Quality Checklist

> Gate de qualidade da vistoria técnica (IBAPE 2025) — usado pelo @inspetor-tecnico (Sentinel).
> Squad: avaliacao-imoveis

---

## Pre-Conditions

- [ ] Fim da avaliação informado pelo @avaliador-chief
- [ ] Acesso ao imóvel ou imagens de qualidade analisável
- [ ] `data/patologias-catalogo.md` e `data/normas-tecnicas.md` (§6) disponíveis

---

## Checklist Items

### Categoria 1: Metodologia IBAPE 2025

| # | Item | Status | Notas |
|---|------|--------|-------|
| 1.1 | Anamnese realizada (histórico/reformas/intervenções) | [ ] | |
| 1.2 | Análise documental (incl. ausências como irregularidade) | [ ] | |
| 1.3 | Vistoria sistêmica sensorial (sem ensaio/prospecção indevidos) | [ ] | |
| 1.4 | Avaliação de manutenção (NBR 5674) e de uso | [ ] | |

### Categoria 2: Diagnóstico de Patologias

| # | Item | Status | Notas |
|---|------|--------|-------|
| 2.1 | Geometria/padrão lidos antes de inferir a causa | [ ] | |
| 2.2 | Origem classificada (construtiva/exógena/funcional/falha) | [ ] | |
| 2.3 | Prioridade atribuída (P1/P2/P3) | [ ] | |
| 2.4 | Severidade não superestimada além da evidência | [ ] | |

### Categoria 3: Saída para o ciclo

| # | Item | Status | Notas |
|---|------|--------|-------|
| 3.1 | Estado de conservação + fator de depreciação propostos | [ ] | |
| 3.2 | Limitações da vistoria/imagem declaradas | [ ] | |
| 3.3 | P1 sistêmico → ressalva + recomendação de aprofundamento | [ ] | |
| 3.4 | Nenhuma opinião sobre preço (fora de escopo) | [ ] | |

---

## Post-Conditions

- [ ] `laudo_inspecao` consolidado para handoff
- [ ] Recomendações de aprofundamento listadas (quando aplicável)
- [ ] Limitações explícitas

---

## Usage

```bash
*checklist inspection-quality
```

> Veto: P1 sistêmico (recalque/estrutura/corrosão) sem ressalva → reprovado.
