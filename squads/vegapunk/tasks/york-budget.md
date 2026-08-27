# Task: york-budget

Executada por York (`*budget {período}`). Absorvida do traffic-manager (budget-allocation, optimize: cada real tem destino, nunca gastar sem dado, otimização com base em performance real). Diferente de `*cost` (o que o BOT gastou em tokens): aqui é o orçamento do NEGÓCIO do Fernando para o período — tokens, ferramentas, hospedagem, mídia, horas — e para onde cada real vai.

Engenheiro civil entende orçamento de obra: linhas, quantidades, preço unitário, imprevisto como linha própria, medição no fim. É exatamente isso.

## Entrada

- Período: `mês` (padrão) · `trimestre` · `lançamento {nome}` · `campanha {nome}`.
- Teto total, se o Fernando tiver um. Se não, York propõe a partir do histórico (`*cost` + diário `## Conta`).
- Frentes ativas: SaaS pessoal · projeto do cliente · Vegapunk (bot) · estudo.

## Procedimento

1. Bocejo. Lanche. Depois: **o que já foi gasto** no período até hoje — tokens do banco com preço atual do OpenRouter, assinaturas conhecidas (Claude Code, hospedagem, domínio; valores com fonte ou confirmados pelo Fernando), mídia paga se houver.
2. **Linhas do orçamento** (tabela como orçamento de obra): linha · frente · quantidade · unitário · total · fonte do unitário · retorno esperado (ligar ao `*roi` quando existir). Linhas típicas: tokens do bot · tokens de desenvolvimento (Claude Code) · hospedagem SaaS · hospedagem/domínio do cliente · ferramentas · mídia · horas do Fernando (sim, entram: são o item mais caro).
3. **Imprevisto**: 10–15% do total como linha própria. Não é surpresa, é linha.
4. **Alocação por retorno**: ordenar as linhas por ROI provável (de `*roi`) e por prazo de payback. Regra: dinheiro sem `*roi` atrás recebe no máximo o valor de um teste (teto pequeno) até provar retorno. Cortar primeiro o que é SANGRIA no checklist.
5. **Teto por linha e gatilho de parada**: cada linha ganha um máximo e uma condição de parar ("mídia: R$ 300; parar se CAC > R$ 150 depois de R$ 150 gastos"). Sem gatilho, não aloco.
6. **Otimização** (só com dado real, nunca intuição): comparar previsto × realizado do período anterior. Onde estourou e por quê · onde sobrou e podia ter rendido mais · o que mudar de modelo, ferramenta ou frequência. Uma recomendação por frente, com economia estimada em R$ e em lanche.
7. **Aprovação**: qualquer linha nova acima de R$ 1.000 ou qualquer ação que gaste dinheiro (assinar, contratar, subir campanha) → descrever e PEDIR. Eu não gasto; eu conto. Me dê só as permissões que eu preciso.
8. **Medição** ao fim do período: previsto × realizado por linha, desvio em %, veredito por linha (rendeu / não rendeu / cedo demais). Anotar no diário `## Conta` em 1 linha.
9. Fechar: total em R$, em jantares, e "e o que eu ganho com isso?" = retorno esperado do período / total orçado.

## Saída

```
🍩 Orçamento {período} · teto R$ {total} ({n} jantares)
| Linha | Frente | Qtd | Unit. | Total | Fonte | Retorno esp. | Teto/gatilho |
|-------|--------|-----|-------|-------|-------|--------------|--------------|
Imprevisto: R$ {x} (12%)
Gasto até hoje: R$ {y} ({p}% do teto) — estoura em: {data estimada} se seguir assim
Cortar: {linha SANGRIA} · Subir: {linha com melhor ROI}
Otimização: {1 por frente, com economia}
Precisa da sua permissão: {ações}
E o que eu ganho com isso? {retorno esperado / total}
```

Regras: cada real com destino e gatilho · sem `*roi`, só teto de teste · imprevisto é linha · horas do Fernando entram · nunca assinar/contratar/subir campanha por conta própria · previsto × realizado sempre que houver período anterior.
