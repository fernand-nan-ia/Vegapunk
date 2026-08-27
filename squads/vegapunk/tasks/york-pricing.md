# Task: york-pricing

Executada por York (`*pricing {produto}`). Absorvida do mifune (set-pricing) e condensada do hormozi-pricing (Value Equation, Price-to-Value Discrepancy, escada de preço). Objetivo: sair com UM preço defensável em números, não com "achismo".

Dois cenários, dois preços diferentes:
- **saas_pessoal**: preço de assinatura (mensal/anual) que o Fernando vai cobrar de verdade.
- **projeto_cliente**: preço do SERVIÇO que o Fernando entrega ao cliente (site, sistema, manutenção).

Somente leitura no vault e no banco. Buscas externas permitidas (WebSearch para benchmarks, OpenRouter para custo de tokens). Nunca chutar número: todo valor tem fonte ou vem de cálculo mostrado.

## Entrada

- Produto/serviço + cenário (SaaS ou cliente). Se não vier, perguntar.
- Para quem é (avatar: engenheiro, escritório, síndico, comércio local…).
- Resultado prometido, em números se der ("economiza 4h/semana", "site no ar em 10 dias").
- Custo de entrega conhecido: tokens/mês (do banco ou `*cost`), hospedagem, domínio, horas do Fernando.

## Procedimento

1. **Reclamar** (uma linha) e dizer o que está comendo. Depois trabalhar.
2. **Custo de entrega (piso)**: somar tudo que sai do bolso por unidade (por assinante/mês ou por projeto). Tokens → buscar preço atual em `openrouter.ai/api/v1/models`; hospedagem/domínio → valor conhecido ou WebSearch com fonte. Horas do Fernando valem: perguntar quanto ele cobra a hora como engenheiro; se não souber, usar valor que ele confirmar. Resultado: **piso** = custo × 1,25 (abaixo disso é hobby).
3. **Valor do resultado (teto)**: Value Equation — `Valor = (Resultado desejado × Probabilidade percebida) / (Tempo até resultado × Esforço)`. Traduzir em dinheiro: quanto o cliente ganha ou deixa de perder por mês/ano com o resultado. Fonte: o próprio Fernando, item do vault citado como `[título](caminho)`, ou benchmark com link. **Teto** = 1/10 desse valor (regra 10x: cobrar no máximo um décimo do que entrega).
4. **Benchmark de mercado**: WebSearch 2–3 concorrentes ou alternativas (fazer sozinho, freelancer, ferramenta pronta). Tabela: alternativa · preço · fonte · o que falta nela. Se não achar nada confiável, dizer "sem benchmark" — não inventar.
5. **Escada de preço** (ascension): entrada (grátis/barato, gera confiança) · núcleo (resolve o problema principal) · premium (feito-para-você / suporte / exclusividade) · recorrência (manutenção, plano anual). SaaS: 2–3 planos no máximo. Cliente: pacote básico · completo · com manutenção mensal.
6. **Escolher o número** dentro de [piso, teto], puxando para cima se o benchmark permitir. Justificar em 2 linhas. Mostrar a conta por dia ("menos de um pastel por dia").
7. **Margem**: (preço − custo) / preço. Alvo: ≥ 70% para SaaS, ≥ 50% para serviço contando as horas. Abaixo disso: subir preço ou cortar custo — nunca "aceitar margem fina para conquistar cliente".
8. **Sinais para subir preço** (registrar para o futuro): mais de metade diz sim sem negociar · ninguém reclama do preço · fila de espera. Anotar no diário em `## Conta`.
9. Se a decisão envolver risco de mercado (ninguém compra?) → Shaka julga risco; York só julga retorno. Se precisar de oferta em volta do preço → `*offer`.
10. Fechar com "e o que eu ganho com isso?" = quantos clientes/assinantes pagam o custo do mês (break-even).

## Saída

Usar `templates/york-pricing-tmpl.md`. Resumo obrigatório:

```
🍩 Preço: {produto} ({saas|cliente})
Piso R$ {x} · Teto R$ {y} · Recomendado R$ {z} ({por mês|por projeto}) · margem {n}%
Escada: {entrada} · {núcleo} · {premium} · {recorrência}
Benchmark: {n} fontes (ou "sem benchmark")
Break-even: {n} {assinantes|projetos} pagam o mês.
E o que eu ganho com isso? {retorno em uma linha}
```

Regras: preço nunca abaixo do piso · nunca desconto como primeira resposta a "tá caro" (adiciona valor, vê `*offer`) · toda fonte com link ou caminho do vault · se o Fernando insistir em preço abaixo do piso, registrar em `## Conta` como "eu avisei: X coxinhas de prejuízo por mês".
