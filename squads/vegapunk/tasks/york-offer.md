# Task: york-offer

Executada por York (`*offer {produto}`). Absorvida do mifune (create-offer) e condensada do hormozi-offers (Grand Slam Offer, Value Equation, bônus, garantia, nome). Objetivo: montar a oferta em volta do preço de `*pricing` para que "tá caro" vire "onde eu assino".

Não é copy (texto de venda) — isso é para depois, com quem escreve. Aqui é a ESTRUTURA: o que entrega, em quanto tempo, com que garantia, com quais bônus, com que nome, por quanto.

## Entrada

- Produto + cenário (SaaS pessoal ou serviço para cliente). Preço já definido? Se não, rodar `*pricing` antes ou aceitar um provisório e marcar.
- Avatar: uma pessoa específica, não "todo mundo".

## Procedimento

1. **Bocejo obrigatório**, depois a pergunta gananciosa antes de tudo: quanto custa entregar cada componente da oferta? (tokens, horas, hospedagem). Nada entra na oferta sem custo ao lado.
2. **Resultado dos sonhos**: o que a vida do avatar vira depois. Uma frase, com número se der ("fecha o orçamento da obra em 1 hora em vez de 1 dia").
3. **Listar TODOS os problemas** entre ele e o resultado, em 3 momentos: antes (medo, tentativas anteriores, "não sei usar"), durante (esforço, confusão, tempo), depois (manter, próximo nível). Mínimo 8. Fonte: vault (`[título](caminho)`) quando houver item sobre o público.
4. **Uma solução por problema**. Cada uma vira um componente com veículo de entrega: feito-para-você (caro, pouco escalável) · em grupo · um-para-muitos (vídeo, template) · faça-você-mesmo (barato, escala). Para cada componente: custo de entrega em R$ e em lanche.
5. **Value Equation** por componente: aumenta resultado? aumenta probabilidade percebida (prova, caso, demonstração)? reduz tempo (vitória em 24–48h)? reduz esforço (template, automação)? Componente que não move nenhum dos 4 sai.
6. **Núcleo + bônus**: núcleo = o que resolve o problema principal. Bônus = componentes baratos de entregar e valiosos de perceber, cada um com nome próprio, valor atribuído (com base, não inventado: preço do concorrente ou horas × valor-hora) e o problema que mata. Máximo 3 bônus. Regra: bônus resolve o PRÓXIMO problema que aparece depois de resolver o principal.
7. **Garantia** (escolher 1, conferir `checklists/york-offer-checklist.md`): incondicional (devolução simples) · condicional (devolve se fez X e não teve Y — filtra quem não é sério) · performance (trabalho de graça até o resultado — só com confiança alta) · anti-garantia (venda final — só com fila). Calcular o custo da garantia no pior caso: quantos reembolsos o Fernando aguenta por mês sem prejuízo.
8. **Nome**: `[Resultado] + [Prazo] + [Formato]`. Soa como coisa, não como serviço. 3 opções, York escolhe 1 e diz por quê.
9. **Escassez/urgência honesta**: vagas reais (horas do Fernando são finitas), bônus de ação rápida com data. Nunca falsa.
10. **Empilhar**: valor total percebido vs preço. Alvo: valor ≥ 5× preço, com cada linha justificada. Se não chega, voltar ao passo 4 — não baixar o preço.
11. Risco de a promessa não se cumprir → Shaka. Oferta pronta e Edison quer implementar → antes ele pergunta "coxinha ou jantar?" e York responde com o custo do passo 1.
12. Fechar: "e o que eu ganho com isso?" = quanto sobra por venda depois de bônus e garantia.

## Saída

```
🍩 Oferta: {nome escolhido}
Para: {avatar} · Resultado: {frase com número}
Núcleo: {componente} — custa R$ {x} para entregar ({lanche})
Bônus: 1. {nome} (vale R$ {v}, custa R$ {c}) mata: {problema}
       2. ...
Garantia: {tipo} — pior caso: {n} reembolsos/mês = R$ {x}
Valor empilhado R$ {total} · Preço R$ {preço} · razão {n}x
Sobra por venda: R$ {líquido} ({lanche})
E o que eu ganho com isso? {retorno}
```

Regras: nada entra sem custo ao lado · valor de bônus com base declarada · garantia com pior caso calculado · nunca desconto: quando "tá caro", empilha · a oferta é estrutura; copy é outro trabalho.
