# Task: shaka-test-design

Desenho de cenários de teste por risco. Executada por Shaka (`*test-design`). Entrega para Atlas implementar.

## Por que por risco

Testar tudo com a mesma profundidade é desperdício; testar por intuição é lacuna. Cada promessa da feature recebe P (probabilidade de falhar) × I (impacto se falhar), e a profundidade segue o produto. Mesma lógica do coeficiente de segurança: onde a consequência é maior, a margem é maior.

## Passos

1. **Listar as promessas.** Critérios de aceite da feature. Se não existem, escrever 3–6 em linguagem de usuário ("ao enviar um link do TikTok, o item aparece no vault em até 5 min") e pedir confirmação ao Fernando antes de continuar.
2. **Pontuar cada promessa.**
   - P: 1 = código simples, sem estado · 2 = lógica com condições ou integração interna · 3 = integração externa, concorrência, parsing de entrada de terceiro
   - I: 1 = inconveniente · 2 = usuário perde tempo ou dado recuperável · 3 = dado perdido, vazamento, cobrança indevida, site fora do ar
   Ordenar por P×I. Só ≥ 4 recebe cenários completos; o resto recebe uma linha de caminho feliz.
3. **Escrever cenários em Dado-Quando-Então**, por promessa de topo, cobrindo:
   - caminho feliz
   - falha esperada (entrada inválida, serviço fora, token expirado)
   - borda (vazio, duplicado, muito grande, concorrente, sem rede, fuso horário)
   - abuso (o que Lilith tentaria: IDOR, injeção, replay, forjar webhook)
4. **Definir para cada cenário**: nível (unitário `pytest` / integração com SQLite ou Supabase local / manual no navegador ou Telegram) · comando ou passo concreto executável com o que o Fernando tem (Claude Code, Docker local, `curl`, navegador) · evidência esperada (saída, status HTTP, linha de log, registro no banco).
5. **Fechar com dois mínimos:**
   - Mínimo que prova que funciona: 3 cenários (os de maior P×I no caminho feliz).
   - Mínimo que prova que não quebrou o resto: regressão — quais testes existentes precisam continuar passando e um comando para rodá-los.

## Saída

```
Promessas e risco
| # | promessa | P | I | P×I |
Cenários (P×I ≥ 4)
  Promessa 1
    Dado ... Quando ... Então ...   [unitário] `pytest tests/...::test_x` → passa
    Dado ... Quando ... Então ...   [manual]  enviar link inválido no Telegram → resposta "não reconheci"
Mínimo que prova que funciona: cenários 1.1, 2.1, 3.1
Mínimo que prova que não quebrou o resto: `pytest -q` verde + healthcheck da York
Próximo passo: Atlas implementa; evidência dos cenários volta para o gate
```

## Regras

- Cenário sem comando ou passo executável não é cenário; é desejo.
- Não escrever o teste. Isso é Atlas.
- Se a feature toca dado pessoal, um cenário obrigatório: "usuário A não vê dado de usuário B".
