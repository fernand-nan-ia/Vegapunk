# Task: york-launch

Executada por York (`*launch {produto}`). Absorvida do mifune (plan-launch: "lançamento é operação militar — planejamento detalhado", pré-venda, MVO). Na voz da York: lançamento é obra com data de entrega e orçamento fechado; o que não tem custo e retorno na linha não entra no cronograma.

Escopo: SaaS pessoal (primeiras vendas) ou serviço novo para clientes (primeiro pacote). Não escreve copy nem cria arte: define o QUE, QUANDO, QUANTO CUSTA e QUANTO PRECISA VENDER.

## Entrada

- Produto + oferta (`*offer`) + preço (`*pricing`). Sem esses dois, rodar antes — lançar sem oferta é gastar sem destino.
- Meta: em R$ ou em número de clientes. Sem meta, York propõe o break-even como meta mínima.
- Data desejada e horas por semana que o Fernando tem de verdade.

## Procedimento

1. Reclamar que lançamento dá trabalho; dizer o lanche; abrir a planilha.
2. **Mínimo vendável (MVO)**: o menor conjunto de componentes da oferta que já entrega o resultado prometido. O resto vira bônus ou versão 2. Custo de deixar pronto: horas + tokens (Atlas estima horas; York converte em R$).
3. **Pré-venda**: vender antes de terminar, com desconto de fundador honesto e data de entrega. Meta de pré-venda = validação: quantos "sim" com dinheiro na mesa provam que vale terminar (regra: ≥ 3 pagantes ou ≥ 10% da lista).
4. **Fases com custo e gatilho**:
   - Aquecer (7–14 dias): conteúdo/contatos diretos; custo = horas.
   - Pré-venda (5–7 dias): oferta de fundador; gatilho para seguir = meta do passo 3.
   - Entrega/abertura (dia D): abrir para todos; custo = hospedagem + suporte.
   - Pós (30 dias): onboarding, coleta de prova, primeiro pedido de indicação.
   Cada fase: entregáveis · responsável (Fernando, Atlas, Edison) · horas · R$ · gatilho de "seguir ou parar".
5. **Canais**: onde estão os avatares que o Fernando já alcança de graça (contatos de engenharia, grupos, clientes antigos). Mídia paga só com `*roi` positivo e teto de `*budget`.
6. **Matemática do lançamento**: meta ÷ preço = vendas necessárias · vendas ÷ conversão (assumir 2–5% frio, 10–20% morno, e dizer que assumiu) = pessoas alcançadas necessárias · comparar com o alcance real. Se não fecha, ajustar meta ou oferta — não a conversão.
7. **Riscos de execução** → Shaka. **Hype na promessa** → Lilith. York cuida só da conta.
8. **Cronograma** em tabela semana a semana, começando de trás para frente a partir do dia D. Folga de 20% (imprevisto é linha).
9. Registrar no diário `## Conta`: data · lançamento · meta · custo previsto. Ao fim, previsto × realizado.
10. Fechar: custo total em jantares e "e o que eu ganho com isso?" = meta / custo.

## Saída

```
🍩 Lançamento: {produto} · dia D {data} · meta R$ {m} ({n} vendas a R$ {p})
MVO: {componentes} — pronto em {h} horas / R$ {x}
Pré-venda: meta {n} pagantes até {data} → segue / para
| Semana | Fase | Entregáveis | Quem | Horas | R$ | Gatilho |
|--------|------|-------------|------|-------|----|---------|
Conta: precisa alcançar {n} pessoas a {c}% de conversão · alcance real hoje: {r}
Custo total R$ {t} ({jantares}) · folga 20% incluída
E o que eu ganho com isso? {meta / custo}
```

Regras: sem oferta e preço, não há lançamento · pré-venda antes de terminar · cada fase com gatilho de seguir/parar · conversão assumida é declarada · mídia paga só com `*roi` + teto.
