# Bank Defensibility Checklist

> Gate de defensabilidade bancária (Caixa/bancos) — usado pelo @revisor-adversarial (Agent Johnson).
> Baseado nas causas reais de retificação reportadas pelo engenheiro credenciado.
> Squad: avaliacao-imoveis

---

## Pre-Conditions

- [ ] Fim = bancário (ou misto incluindo bancário)
- [ ] Laudo redigido + `validate-norms` executado
- [ ] `data/normas-tecnicas.md` disponível

---

## Checklist Items

### Categoria 1: Causas nº 1 de retificação (especialista)

| # | Item | Status | Notas |
|---|------|--------|-------|
| 1.1 | **Coerência das observações** — sem contradição entre seções/dados | [ ] | |
| 1.2 | **Endereço completo** e inequívoco | [ ] | |
| 1.3 | **Pontos específicos** do imóvel descritos (nada genérico) | [ ] | |
| 1.4 | Nenhuma informação essencial faltando | [ ] | |

### Categoria 2: Modelagem sob ataque

| # | Item | Status | Notas |
|---|------|--------|-------|
| 2.1 | Variáveis bem escolhidas e justificadas (sem códigos alocados injustificados) | [ ] | |
| 2.2 | Análise de atributos presente (causa comum de rejeição) | [ ] | |
| 2.3 | Fundamentação ≥ Grau II (mínimo bancário) | [ ] | |
| 2.4 | Sem micronumerosidade; pressupostos testados | [ ] | |

### Categoria 3: Valor e desfecho

| # | Item | Status | Notas |
|---|------|--------|-------|
| 3.1 | Valor coerente com o mercado (campo de arbítrio justificado) | [ ] | |
| 3.2 | Relação valor × valor de financiamento avaliada e comentada | [ ] | |
| 3.3 | Fotos/identificação dos dados conforme grau | [ ] | |
| 3.4 | Simulação de rejeição do analista do banco aplicada (vetor + reparo) | [ ] | |

---

## Post-Conditions

- [ ] Veredito: defensável para o banco OU devolver com fragilidades
- [ ] Cada fragilidade com vetor de ataque + reparo + responsável

---

## Usage

```bash
*checklist bank-defensibility
```

> Veto: qualquer item da Categoria 1 reprovado → devolver (são as causas nº 1 de retificação na Caixa).
