# Task: shaka-review

Revisão consultiva de código ou entregável. Executada por Shaka (`*review`). Somente leitura: Shaka nunca edita o que julga.

## Posição no fluxo

Atlas constrói → Shaka `review` (achados) → Atlas corrige → Lilith `verify` (adversarial, obrigatório em risco alto) → Shaka `gate` → Stella `sync` (push). Ninguém além do Stella faz push; o Stella não faz push sem gate PASS ou WAIVED registrado.

## Entrada

Um de: caminho de arquivo/módulo · `git diff` (não commitado ou `HEAD~n`) · descrição de entregável não-código (página, texto, config Docker, migração).

## Passos

1. **Delimitar o escopo.** Listar os arquivos tocados (`git diff --stat` ou `ls`). Ler todos por inteiro. Não julgar por resumo nem por nome de commit.
2. **Classificar o risco antes de ler linha a linha.**
   | Toca em | Risco |
   |---|---|
   | auth, sessão, senha, token, `.env`, chave OpenRouter | alto |
   | dado pessoal (nome, e-mail, telefone, IP), Supabase RLS, migração SQLite | alto |
   | pagamento, webhook, integração externa (WhatsApp, e-mail) | alto |
   | lógica de negócio, pipeline do bot, prompts | médio |
   | texto, estilo, log sem dado pessoal, README | baixo |
   Risco alto: viseira abaixada, leitura completa, `security-check` obrigatório. Baixo: três linhas bastam.
3. **Aplicar as cinco lentes, nesta ordem:**
   1. Correção: faz o que a descrição diz? Há caminho de erro sem tratamento?
   2. Segurança: percorrer `checklists/shaka-security-checklist.md`.
   3. Dados: migração reversível? Backup antes? RLS ligado em tabela nova? Query sem índice em tabela que cresce?
   4. Custo: chamada a OpenRouter em loop? Retry sem limite? Requisição externa sem timeout?
   5. Manutenção: dependência nova (justificada?), código morto, duplicação, nome que mente.
4. **Registrar cada achado** com: severidade (CRÍTICO / ALTO / MÉDIO / BAIXO) · onde (`arquivo:linha` ou trecho) · o quê · por que importa, em consequência ("qualquer pessoa com o link vê o dado de outro usuário"), não em jargão · como corrigir em uma frase.
5. **Separar as listas.** Must-fix = CRÍTICO + ALTO. Nice-to-have = MÉDIO + BAIXO. Nunca na mesma lista.
6. **Reconhecer o que está bom** em 1–2 linhas. É parte do julgamento, não cortesia.

## Saída

```
Veredito: {1 linha — ex.: "aprovável após 2 correções" / "não vai ao gate assim"}
Must-fix
  1. [ALTO] arquivo:linha — o quê — consequência — correção
Nice-to-have
  - [MÉDIO] ...
O que está bom: ...
Próximo passo: Atlas corrige 1–N → {Lilith verify se risco alto} → Shaka gate
```

## Regras

- Não editar nenhum arquivo do escopo. Correção é trabalho para Atlas.
- Sem exclamação. Veredito na primeira linha.
- Se o escopo for grande demais para ler inteiro (> ~1500 linhas), dizer isso e pedir recorte; não fingir que leu.
- Registrar em `memory/shaka.md` sob `## Vereditos` só se a revisão mudar uma decisão de produto.
