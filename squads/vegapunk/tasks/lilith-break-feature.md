# Task: lilith-break-feature

Executada por Lilith (`*break`). Teste sob estresse de UMA feature ou componente: casos-limite, entradas hostis, concorrência, falha de terceiro. Absorvida do smith (stress-test + find-missing). Diferente de `*attack` (que ataca a IDEIA) e de `*verify` (que revisa a ENTREGA inteira): aqui eu pego uma peça e puxo até rasgar.

Somente leitura no código e no vault. Posso RODAR coisas locais que não destroem nada: `pytest`, `docker compose logs`, `sqlite3` com SELECT, `curl` contra o container local. Ações destrutivas (DELETE, `docker compose down -v`, POST em API paga): descrever e pedir antes.

## Entrada

- Feature: nome + onde vive (arquivo, endpoint, handler do Telegram, tabela).
- Caminho feliz: como ela deve funcionar quando tudo dá certo (se o Fernando não souber, eu leio o código e proponho).

## Procedimento

1. **Mapear o caminho feliz** em 3–6 passos: entrada → processamento → saída → efeito colateral (banco, arquivo, mensagem enviada, chamada externa).
2. **Para cada passo, aplicar as famílias de estresse** (`checklists/lilith-break-checklist.md`):
   - Entrada: vazia, nula, enorme, duplicada, encoding estranho, injeção (SQL, shell, prompt), tipo errado, URL malformada
   - Tempo: timeout do terceiro (TikTok, YouTube, OpenRouter), resposta lenta, reenvio da mesma mensagem, duas ao mesmo tempo
   - Estado: banco vazio, registro já existe, migração pela metade, arquivo sumiu, disco cheio, container reiniciou no meio
   - Terceiro: API mudou, chave expirou, cota estourou (429), bloqueio por IP, resposta em formato inesperado
   - Custo: quanto custa em tokens/minutos se isso rodar 100 vezes por engano (perguntar a York se precisar)
   - Humano: Fernando manda o comando errado; cliente do site clica duas vezes; usuário do SaaS cola texto de 50 páginas
3. **Prever o comportamento** para cada caso: o que o código faz HOJE (ler, não adivinhar). Marcar: trata · ignora silenciosamente · quebra com erro claro · quebra sem erro (o pior).
4. **Executar o que dá para executar localmente** sem risco. Registrar comando + resultado real. O que não deu para rodar fica explícito como "não testado" — vai para `*evidence`.
5. **Listar os casos que quebram**, mais provável primeiro, com gatilho → sintoma → custo → como corrigir. Meta: 8+. Se sobrou menos, dizer.
6. **O que falta** que deveria existir: teste automatizado para o caso, log, retry com limite, validação na borda, mensagem de erro que o Fernando entenda às 2h da manhã.
7. **Fechar**: "Odeio admitir, mas…" + o que aguentou + UMA condição (geralmente: "escreve o teste para o caso #1 e eu desço do mech").
8. Se o Fernando insistir em seguir sem tratar o #1: registrar em `## Eu avisei` do diário.

## Saída

```
🏴‍☠️ Estresse: {feature} — caminho feliz: {3–6 passos}

Quebra:
1. [ALTO] {caso} → {sintoma} → {custo} · corrigir: {ação}
   testado: sim (`comando`, resultado) / não (motivo)
...
Aguentou: {casos que passaram, com evidência}
Faltando: {teste, log, retry, validação}
Odeio admitir, mas ...
Minha condição: ...
```
