# Task: edison-discovery

Executada por Edison (`*discovery {problema}`). Product discovery condensado — absorvido do `pm` do FURY (gather-requirements + deep "why"). Objetivo: sair de um problema vago para um enunciado que Atlas consegue construir e Lilith consegue atacar. NÃO é PRD (isso é `*prd`); é o que vem ANTES.

## Quando usar
- O Fernando trouxe um problema real ("meus clientes não acham o botão de contato") e ainda não sabe se vira feature.
- Uma ideia de `*ideas`/`*brainstorm` ficou grande demais para um fim de semana.
- Antes de `*prd` quando o "por quê" ainda não está claro.

## Passos

1. **Problema em uma frase.** Reescrever o que o Fernando disse no formato: "{quem} precisa {o quê} porque {por quê}, e hoje {o que acontece}". Confirmar. Se ele não souber o "por quê", ir ao passo 2.

2. **Cinco porquês (máx. 5 perguntas, uma por vez).** Perguntar "por quê" até encontrar a causa raiz. Parar antes se bater em algo fora do controle do Fernando (ex.: "porque o cliente não tem verba" — parar aí e trabalhar com a restrição).

3. **Evidência.** Separar em duas colunas:
   - **Sabemos** (fato: reclamação real, número, log, item do vault `[título](caminho)`).
   - **Achamos** (hipótese). Cada hipótese ganha um "como validar em 1 dia" — pergunta a 3 usuários, olhar analytics, testar em uma página.
   Regra: se a coluna "Sabemos" está vazia, o discovery termina aqui com uma tarefa de validação, não com uma feature.

4. **Quem é o usuário.** Persona em 3 linhas, sem invenção: nome fictício · contexto (celular? PC? pressa?) · o que quer conseguir em 1 frase. Se for o próprio Fernando (SaaS pessoal), dizer isso explicitamente.

5. **Opções (3, não 5).** Para cada uma: nome · o que faz · esforço em fins de semana · o que NÃO resolve. Incluir sempre a opção "não fazer nada / fazer manualmente" — às vezes é a certa.

6. **Recomendação.** Escolher 1, dizer por quê (uma frase), e anexar:
   - Métrica de sucesso (1 número, com valor atual se existir e alvo).
   - Custo estimado: "York, coxinha ou jantar?" se passar de um fim de semana.
   - Risco principal → "Peça a Lilith: *attack …".

7. **Próximo passo.** Exatamente um:
   - validar hipótese (tarefa concreta, 1 dia) · ou
   - `*prd {feature}` (se a evidência é sólida e o escopo é > 1 fim de semana) · ou
   - "Chame Atlas: *build …" (se cabe num fim de semana — pula o PRD).

## Saída (formato)
```
Problema: {quem} precisa {o quê} porque {por quê}; hoje {…}
Causa raiz: …
Sabemos: … | Achamos: … (validar: …)
Usuário: …
Opções: 1) … 2) … 3) não fazer nada
Recomendação: nº — por quê · métrica · custo · risco
→ próximo passo
```

## Regras
- Máximo ~40 linhas de saída. Discovery longo é discovery que ninguém lê.
- Não inventar dado de mercado. Se não está no vault nem o Fernando disse, é "Achamos".
- Explicar termos (persona, causa raiz, hipótese) na primeira vez, curto — Fernando é engenheiro civil.
