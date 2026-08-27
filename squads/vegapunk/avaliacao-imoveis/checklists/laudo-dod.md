# Laudo — Definition of Done (DoD)

> Gate final de "pronto" do laudo antes da decisão do @avaliador-chief.
> Squad: avaliacao-imoveis

---

## Pre-Conditions

- [ ] Vistoria, amostra e modelo entregues pelos especialistas
- [ ] `validate-norms` executado (enquadramento de grau)
- [ ] Revisão adversarial executada (@revisor-adversarial)

---

## Checklist Items

### Categoria 1: Estrutura e conteúdo

| # | Item | Status | Notas |
|---|------|--------|-------|
| 1.1 | Objeto, objetivo, finalidade e data de referência declarados | [ ] | |
| 1.2 | Identificação e caracterização completas (endereço completo + pontos específicos) | [ ] | |
| 1.3 | Seções de vistoria, pesquisa e tratamento presentes | [ ] | |
| 1.4 | Resultado + campo de arbítrio explicitados | [ ] | |

### Categoria 2: Rastreabilidade e norma

| # | Item | Status | Notas |
|---|------|--------|-------|
| 2.1 | Zero valor inventado; zero afirmação órfã (Constitutional Gate) | [ ] | |
| 2.2 | Cada afirmação rastreia para evidência + norma (NBR 14.653-1:2019/-2:2004) | [ ] | |
| 2.3 | Grau de fundamentação/precisão declarado e justificado | [ ] | |
| 2.4 | ART/RRT e responsabilidade técnica referenciadas | [ ] | |

### Categoria 3: Honestidade técnica

| # | Item | Status | Notas |
|---|------|--------|-------|
| 3.1 | Ressalvas e condições limitantes explícitas | [ ] | |
| 3.2 | Limitações da vistoria/imagem declaradas | [ ] | |
| 3.3 | Veredito adversarial considerado e fragilidades sanadas | [ ] | |
| 3.4 | Coerência descritiva (sem contradição entre seções) | [ ] | |

---

## Post-Conditions

- [ ] Laudo pronto para `*approve-laudo` (@avaliador-chief)
- [ ] Pendências (se houver) listadas e atribuídas

---

## Usage

```bash
*checklist laudo-dod
```

> Veto: qualquer item da Categoria 2 reprovado → laudo NÃO está "done".
