# Story: Kit 2a — Importador vault → banco (reinstalação e multi-máquina)
**Projeto:** vegapunk   **Status:** pronta
**Origem:** pedido do Fernando em 2026-09-01 (kit de distribuição: enviar a amigos, reinstalar em outra máquina, repo original como vault único compartilhado)

## Objetivo (1 frase)
Permitir reconstruir o banco a partir dos `.md` do `punk_records/` — para reinstalar o Vegapunk em outra máquina sem perder o catálogo, e para que itens que chegaram por `git pull` (commitados por outra instalação) entrem no banco local antes que uma regeneração do INDEX os derrube.

## Contexto que Atlas precisa
- O banco (`data/vegapunk.db`) é a fonte da verdade; `vault.write_index` regenera INDEX.md e `temas/` **inteiros a partir do banco** a cada triagem/captura. Item que existe só como arquivo (veio por pull) some do índice na próxima regeneração — este é o bug de design que a story fecha.
- O frontmatter de cada item carrega quase tudo: `item_id`, `platform`, `external_id`, `canonical_url`, `channel`, `captured_at`, `status`, `triage`, `tags`, `applicability`, `confidence`, `theme`, `content_type`. O corpo tem `## Resumo`, `## Pontos-chave`, `## Como aplicar`, `## Texto integral` (artigos), `## Notas manuais`.
- O que NÃO dá para recuperar: transcrições brutas e `item_events` (tokens gastos) — só vivem no banco. Importar marca isso de forma honesta (ex.: `model_used=import`), sem inventar.
- Duplicata: o pipeline deduplica por `(platform, external_id)`; o importador precisa usar a mesma chave para ser idempotente.
- Armadilha de sessão 4g: `docker compose exec -T` dentro de `while read` consome o stdin — usar `for` ou `</dev/null`.

## Critérios de aceite
- [ ] `scripts/import_vault.py` varre `punk_records/` (ignorando `_pending/` e `temas/`) e insere no banco todo item cujo `(platform, external_id)` não existe; rodar duas vezes seguidas não duplica nada (idempotente).
- [ ] Teste de reinstalação: com um banco NOVO (vazio) e o vault atual, o import reconstrói as linhas e `vault.write_index` gera um INDEX.md com os mesmos itens e triagens de antes.
- [ ] Teste do cenário pull: item novo plantado como arquivo (simulando push de outra máquina) + uma triagem local qualquer → o item plantado continua no INDEX.md depois da regeneração.
- [ ] Item no banco sem arquivo correspondente gera AVISO no relatório final; o importador nunca deleta nada (condição 4 do Shaka).
- [ ] Relatório final imprime: importados, já existiam, avisos — e o script sai com código ≠ 0 se algum arquivo tiver frontmatter inválido (listando quais).

## Fora de escopo
- Não rodar automaticamente no arranque do container (fica para decisão futura; por ora é comando manual documentado na rotina `pull → import → usar → push`).
- Não recuperar custo/tokens históricos nem transcrições brutas.
- Não resolver conflitos de merge do git (rotina documentada na Story 2c cuida disso).

## Riscos / Shaka
Veredito de 2026-09-01, risco MÉDIO com 4 condições: escrita só pelo caminho do pipeline (`db.transition_to` ou equivalente usado pelo `capture.py`), backup `data/vegapunk.db.bak-import-<data>` antes da primeira rodada real, nenhum segredo tocado, e importador nunca apaga (aviso, não delete).

## Testes esperados
`tests/test_import_vault.py`: idempotência, banco vazio + vault real (fixture com 3 itens), item plantado sobrevive à regeneração, frontmatter inválido → exit ≠ 0, item órfão no banco → aviso.

## Como desfazer
Apagar `scripts/import_vault.py` e o teste; restaurar `data/vegapunk.db.bak-import-<data>` se uma importação tiver gravado algo errado.

## Handoff → Atlas: `*develop squads/vegapunk/stories/2026-09-01-kit-2a-importador.md`
