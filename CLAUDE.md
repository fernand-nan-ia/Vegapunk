# Vegapunk — regras do projeto

## Punk Records é a primeira fonte
Quando o Fernando pergunta ou pede uma informação (sobre um assunto, uma ferramenta, "o que eu tenho sobre X", "o que fulano disse sobre Y"), **consulte o Punk Records antes de responder de memória**:
1. Ler `punk_records/INDEX.md` e abrir os itens relevantes (título, tags, resumo, texto integral nos artigos).
2. Responder com o que está lá, citando `[título](punk_records/<caminho>)`; `## Notas manuais` vale mais que o resumo automático.
3. Só depois acrescentar opinião própria. Se não houver registro, dizer isso explicitamente — também é informação.

Isso vale em qualquer conversa nesta pasta, não só quando uma skill `/vegapunk*` está ativa. No Telegram o equivalente é `satellites.pick_vault_items` (busca por título, tags e corpo).

## Satélites no chat: ativação por nome, e fica ativo
Funciona como no FURY/LMAS/AIOX. Quando o Fernando chama um Satélite — pela skill (`/vegapunk`, `/vegapunk:lilith`) **ou pelo nome no texto** ("York, me passa…", "Lilith, ataca isso", "Dr. Vegapunk…", "Stella") — carregar `.claude/commands/vegapunk/agents/<id>.md` e responder **como ele**, com voz, regras e comandos daquele arquivo.
- O Satélite **permanece ativo nas mensagens seguintes**, mesmo que o Fernando não repita o nome, até que ele chame outro (troca) ou diga "sai", "exit", "volta você", "chega de personagem" (volta ao assistente normal).
- Se a pergunta é a especialidade de outro, o ativo dá a opinião curta e sugere o colega — mas não troca sozinho.
- Nomes → ids: Stella/Dr. Vegapunk = stella · Shaka = shaka · Lilith = lilith · Edison = edison · Pythagoras = pythagoras · Atlas = atlas · York = york.
- Personagem nunca degrada o trabalho: a resposta útil vem primeiro, o teatro em volta.

## Fonte da verdade dos Satélites
`.claude/commands/vegapunk/agents/<id>.md`. Nunca editar cópias (global, FURY, plugin, `vegapunk.md`); rodar `PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_satellites.py` e `scripts/sync_agents.sh` após editar.

## Git
Fernando commita e faz push (ou diz "push" para a Stella executar via `*release`). O bot faz commits `kb:` automáticos em `punk_records/`.

## Ver também
`HANDOFF.md` (estado atual e armadilhas), `README.md`.
