# Checklist: atlas-self-critique

Rodada por Atlas em `*critique` (e, em modo `yolo`, antes do DoD). Absorvida do `self-critique-checklist` e `dev-suggest-refactoring` do FURY: Atlas olha o próprio diff como se fosse a Lilith olhando — antes que a Lilith olhe. Saída: lista de achados com severidade, e só então correções aprovadas.

## Como usar

1. `git diff` (ou o diff da sessão) — ler linha a linha, não "no geral".
2. Para cada pergunta abaixo, responder com evidência (arquivo:linha) ou "não se aplica".
3. Classificar cada achado: 🔴 quebra/segurança (corrigir agora) · 🟡 vai doer em 1 mês (propor) · 🟢 estilo (anotar).
4. Corrigir 🔴 na hora, com teste. 🟡 e 🟢 viram lista numerada para o Fernando escolher.

## A. Correção

- [ ] Existe caminho de entrada que faz o código explodir? (vazio, `None`, string gigante, encoding, rede fora)
- [ ] O que acontece se rodar duas vezes? (idempotência: cron, webhook, migration, retry)
- [ ] Algum `if` sem `else` esconde um estado que o código não trata?
- [ ] Teste prova o comportamento ou só prova que "não deu erro"?

## B. Segurança e dados

- [ ] Entrada do usuário chega em SQL/shell/HTML sem tratamento? (f-string em query = 🔴)
- [ ] Tabela nova com dado de usuário tem RLS? (`*rls`)
- [ ] Segredo, token ou chave aparecem em log, erro ou conversa?
- [ ] `service_role`/admin usado onde `anon`/usuário bastaria?

## C. Simplicidade (o Fernando precisa ler isso depois)

- [ ] Função com mais de ~40 linhas ou mais de 3 níveis de indentação → dividir?
- [ ] Nome diz o que faz? (`process_data` não; `mark_item_as_triaged` sim)
- [ ] Há duplicação com algo que o projeto já tinha? (`grep` pelo nome antes de criar)
- [ ] Abstração criada "para o futuro" que ninguém pediu? → apagar
- [ ] Comentário explica o PORQUÊ (não o quê)? Comentário que repete o código → apagar

## D. Custo e operação (o que York perguntaria)

- [ ] Chamada a LLM/API dentro de loop sem necessidade? (tokens = Mother Flame)
- [ ] Consulta ao banco dentro de loop (N+1)?
- [ ] Arquivo/log crescendo sem limite?
- [ ] Dependência nova pesada para uma função só?

## E. Reversibilidade (o que Pythagoras cobraria)

- [ ] "Como desfazer" ainda é verdade depois deste diff?
- [ ] Mudança de formato de dado (coluna, JSON, arquivo) tem caminho de volta?

## Saída

```
Achados:
1. 🔴 arquivo.py:42 — f-string em SQL → parametrizar (corrigido, teste X)
2. 🟡 bot.py:120 — chamada OpenRouter dentro de for → agrupar (proposta)
3. 🟢 ...
Refatorações propostas (escolha por número): ...
```
