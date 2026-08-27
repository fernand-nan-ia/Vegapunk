# Norms Compliance Checklist

> Gate de compliance NBR 14.653-2:2004 e enquadramento de grau — usado por @redator-laudos e @pesquisador-mercado.
> Squad: avaliacao-imoveis

---

## Pre-Conditions

- [ ] `data/normas-tecnicas.md` §3/§4 disponível
- [ ] Grau-alvo definido pelo @avaliador-chief
- [ ] Modelo tratado entregue pelo @engenheiro-dados

---

## Checklist Items

### Categoria 1: Método e amostra

| # | Item | Status | Notas |
|---|------|--------|-------|
| 1.1 | Método = regressão (padrão); fatores só fallback declarado | [ ] | |
| 1.2 | Qtd. de dados ≥ exigência do grau-alvo (regressão: 6/4/3·(k+1); fatores: 12/6/3) | [ ] | |
| 1.3 | Oferta×transação identificadas; fontes rastreáveis (judicial: obrigatório) | [ ] | |

### Categoria 2: Regressão (Anexo A)

| # | Item | Status | Notas |
|---|------|--------|-------|
| 2.1 | Micronumerosidade: n ≥ 3(k+1); ni conforme dicotômicas/códigos | [ ] | |
| 2.2 | Normalidade, homocedasticidade, autocorrelação, multicolinearidade (>0,80), outliers | [ ] | |
| 2.3 | Teste F ≤ 1%; significância dos regressores conforme grau (10/20/30%) | [ ] | |
| 2.4 | Campo de arbítrio ±15% da estimativa pontual (ou justificado) | [ ] | |

### Categoria 3: Enquadramento de grau

| # | Item | Status | Notas |
|---|------|--------|-------|
| 3.1 | Pontuação por item calculada (I=1, II=2, III=3) | [ ] | |
| 3.2 | Pontos mínimos: regressão 18/11/7 · fatores 15/9/6 | [ ] | |
| 3.3 | Itens obrigatórios: regressão 3,5,6,7 · fatores 3,5,6 | [ ] | |
| 3.4 | Tetos aplicados (códigos alocados → máx II; fatores em regressão → máx II) | [ ] | |
| 3.5 | Grau atingido ≥ grau-alvo do fim (ou lacunas reportadas) | [ ] | |

---

## Post-Conditions

- [ ] Grau de fundamentação e precisão declarados e sustentados
- [ ] Lacunas vs. grau-alvo reportadas ao @avaliador-chief (se houver)
- [ ] Precisão não fixada a priori (NBR §9.1.1)

---

## Usage

```bash
*checklist norms-compliance
```

> Veto: grau declarado acima do que a pontuação/itens obrigatórios sustentam → reprovado.
