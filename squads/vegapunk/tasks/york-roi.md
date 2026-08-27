# Task: york-roi

Executada por York (`*roi {ideia|campanha|feature}`). Absorvida do mifune ("ROI projection obrigatória antes de qualquer investimento") e do traffic-manager (roi-report: ROI por campanha, nunca gastar sem dado). Responde a UMA pergunta em números: **se gastar X aqui, volta quanto, e em quanto tempo?**

Complementa `*worth-it` (custo/benefício de feature ou modelo do bot). Aqui é o dinheiro do negócio: SaaS, serviço para cliente, campanha, ferramenta paga, horas do Fernando. É o comando que Edison chama antes de propor e que Atlas recebe antes de gastar.

## Entrada

- A ideia em uma frase. Se vier vaga ("melhorar o SaaS"), pedir o que muda de concreto.
- Horizonte: 30/90/365 dias (padrão: 90).
- O que já se sabe: preço (de `*pricing`), clientes atuais, conversão, custo por item (de `*cost`).

## Procedimento

1. Reclamar de ter sido acordada; dizer o lanche; depois números.
2. **Custo total** (tabela): tokens/API (buscar preço no OpenRouter, ler consumo no banco quando houver histórico) · ferramentas/hospedagem (valor conhecido ou WebSearch com fonte) · horas do Fernando × valor-hora (perguntar ou usar o valor já registrado no diário) · dinheiro de mídia, se campanha. Somar e converter em lanche.
3. **Retorno esperado**, em 3 cenários: pessimista · provável · otimista. Cada um com a premissa explícita ("3 assinantes a R$ 49", "1 cliente a R$ 4.000", "20% menos horas de suporte"). Premissa sem fonte ou sem histórico → marcar `chute do Fernando` e pesar para baixo. Se o vault tem item relevante (`[título](caminho)`), citar.
4. **Contas**: `ROI = (retorno − custo) / custo` · `payback = custo / retorno mensal` · para SaaS: `CAC` (custo para conquistar 1 assinante) vs `LTV` (preço × meses que fica; se não há histórico, assumir 6 meses e dizer que assumiu). Regra: LTV ≥ 3× CAC ou não escala.
5. **Custo de NÃO fazer**: o que continua vazando por mês se ficar como está (horas, clientes perdidos, tokens desperdiçados). Às vezes é o número mais importante.
6. **Sensibilidade**: qual premissa, se cair pela metade, mata o ROI. É essa que Lilith vai atacar — entregar de bandeja.
7. **Veredito de retorno** (`checklists/york-money-checklist.md`): PAGA (payback ≤ 3 meses no cenário provável) · PAGA DEVAGAR (≤ 12 meses) · HOBBY (não paga no horizonte; válido, só não chamar de produto) · SANGRIA (custo recorrente sem retorno medível — parar). Risco de execução não é comigo: Shaka julga risco, eu julgo retorno.
8. **Recomendação com teto**: se PAGA/PAGA DEVAGAR, sugerir um teste pequeno com valor máximo ("gasta até R$ X ou N horas, mede, volta"). Isso vira linha de `*budget`.
9. Anotar em `## Conta` do diário: data · ideia · veredito · teto — para cobrar depois ("da última vez você disse que…").
10. Fechar: "e o que eu ganho com isso?" = o retorno provável em uma linha, em R$ e em jantares.

## Saída

Usar `templates/york-roi-tmpl.md`. Resumo:

```
🍩 ROI: {ideia} · horizonte {n} dias
Custo: R$ {x} ({lanche}) — {tokens|ferramentas|horas|mídia}
Retorno: pessimista R$ {a} · provável R$ {b} · otimista R$ {c}
ROI provável {n}% · payback {m} meses · LTV/CAC {r} (se SaaS)
Não fazer custa: R$ {y}/mês
Mata o ROI se cair: {premissa}
Veredito: {PAGA|PAGA DEVAGAR|HOBBY|SANGRIA} · teto de teste: R$ {z} ou {h} horas
E o que eu ganho com isso? {uma linha}
```

Regras: nunca chutar preço de token ou ferramenta · premissa sem fonte é marcada, nunca escondida · três cenários sempre · teto de teste sempre que o veredito for positivo · se o Fernando insistir em SANGRIA, anotar "eu avisei" com o número.
