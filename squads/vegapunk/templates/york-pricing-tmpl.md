# Template: york-pricing

Saída de `*pricing {produto}`. Preencher todos os campos; campo sem fonte recebe `(estimado)` ou `(chute do Fernando)` — nunca fica em branco disfarçado.

---

🍩 **Preço: {produto}** · cenário: {saas_pessoal | projeto_cliente} · {data}

_{uma linha de reclamação + o que York está comendo}_

## 1. Custo de entrega (piso)

| Item | Qtd/mês ou por projeto | Unitário | Total | Fonte |
|------|------------------------|----------|-------|-------|
| Tokens ({modelo}) | | | | openrouter.ai/api/v1/models em {data} |
| Hospedagem | | | | |
| Domínio / ferramentas | | | | |
| Horas do Fernando | {h} h | R$ {valor-hora} | | diário / informado |
| **Custo total** | | | **R$ {c}** | |

**Piso** = custo × 1,25 = **R$ {piso}** ({lanche})

## 2. Valor do resultado (teto)

- Resultado prometido: {frase com número}
- Vale para o cliente: R$ {v}/{mês|ano} — fonte: {Fernando | [título](caminho) | link}
- Value Equation: resultado {alto|médio} · probabilidade {alta|média|baixa} · tempo {curto|longo} · esforço {baixo|alto}
- **Teto** = 1/10 do valor = **R$ {teto}**

## 3. Benchmark

| Alternativa | Preço | Fonte | O que falta nela |
|-------------|-------|-------|------------------|
| | | | |

_(ou: "sem benchmark confiável — não inventei")_

## 4. Escada de preço

| Degrau | O que entrega | Preço | Margem |
|--------|---------------|-------|--------|
| Entrada | | R$ / grátis | |
| Núcleo | | R$ | |
| Premium | | R$ | |
| Recorrência | | R$ /mês | |

## 5. Decisão

- **Recomendado: R$ {z} {por mês | por projeto}** — dentro de [R$ {piso}, R$ {teto}]
- Por dia: R$ {z/30} ({"menos de um pastel por dia"})
- Margem: {n}% (alvo ≥ 70% SaaS · ≥ 50% serviço)
- Justificativa (2 linhas):
- Break-even: {n} {assinantes | projetos} pagam o mês
- Sinais para subir preço depois: {lista}

## 6. Encaminhamentos

- Risco de mercado → Shaka · Oferta em volta do preço → `*offer` · Hype → Lilith

**E o que eu ganho com isso?** {retorno em uma linha}

---
_Anotado em `## Conta`: {data} · pricing {produto} · R$ {z} · margem {n}%_
