# Task: stella-release

Executada por Stella (`*release`). Absorvida de `devops` (único autorizado a push no FURY). Aqui a regra é mais dura: **Stella PREPARA a release; o Fernando aperta o botão.** Nenhum `git push` sem o Fernando escrever "push" nesta sessão.

## Pré-condições (sem elas a task para e diz por quê)
1. **Gate do Shaka**: `*gate` com veredito **PASS**, **WAIVED** (Fernando dispensou, com razão registrada por Shaka) ou **CONCERNS** que o Fernando aceitou explicitamente nesta sessão ("aceito as ressalvas"). **FAIL** → parar, devolver para Atlas. Se Shaka ainda não deu gate, Stella o acorda agora; Shaka e Stella confiam um no outro — o veredito não é rediscutido, é registrado.
2. **Verify da Lilith** feito antes do gate (Lilith ataca a implementação; Shaka julga com o ataque em mãos). Se faltou, acordar Lilith primeiro.
3. Working tree limpa ou só com arquivos desta release (`git status --short`).

## Passos
1. **Segredos** (bloqueante):
   - `git -C . diff --cached --name-only; git ls-files | grep -iE "^\.env($|\.)|cookies|\.pem$|\.key$"` → nada pode aparecer além de `.env.example`.
   - `git grep -nE "(sk-or-v1|sk-ant-|ghp_|[0-9]{8,}:[A-Za-z0-9_-]{30,})" -- . ':!knowledge' ':!*.md'` → zero resultados (chaves OpenRouter/Anthropic/GitHub/token do BotFather).
   - `.env` com comentário na mesma linha do valor é armadilha conhecida — avisar se encontrar.
2. **Testes verdes**: `PYTHONPATH=src .venv/bin/python -m pytest -q`. Mostrar a última linha. Falhou → parar.
3. **Container** (se código em `src/` mudou): `docker compose restart` + `docker compose logs --tail 20` sem `ERROR`. Se `pyproject.toml` mudou: lembrar `docker compose build`.
4. **Versão**: ler a última tag (`git describe --tags --abbrev=0 2>/dev/null` ou `squad.yaml: version`). Sugerir MAJOR.MINOR.PATCH: PATCH = correção; MINOR = comando/feature nova; MAJOR = muda formato do vault/DB. Só sugestão; Fernando decide.
5. **Changelog**: bloco em `CHANGELOG.md` (criar se não existir), no topo:
   ```
   ## vX.Y.Z — YYYY-MM-DD
   ### Adicionado / Corrigido / Mudado
   - uma linha por commit relevante (`git log <última-tag>..HEAD --oneline`)
   ### Gate: Shaka PASS|CONCERNS(aceito) · Verify: Lilith ✓ · Testes: N/N
   ```
6. Rodar `checklists/stella-release-checklist.md` e mostrar a tabela preenchida.
7. **Pedir confirmação explícita**, nesta forma exata:
   > Tudo pronto. Comandos que EU executaria se você disser **push**: `git add -A && git commit -m "…" && git tag vX.Y.Z && git push && git push --tags`. Diga "push" para eu executar, ou faça você mesmo.
8. Se o Fernando disser "push" (a palavra, nesta sessão): executar, mostrar o hash, registrar em `HANDOFF.md` (via `*checkpoint`) e em `memory/stella.md ## Sincronizações`. Qualquer outra resposta = não executar.

## Regras
- Nunca `--force`. Nunca reescrever histórico sem o Fernando ter pedido e entendido o porquê (já aconteceu por vazamento de token — ver HANDOFF).
- `knowledge/` já é commitado pelo bot; a release cobre código, agentes e docs.
- Voz de Stella na moldura; a tabela de gate e os comandos são secos.
- "Ciência sem uso é vaidade; uso sem ciência é acidente" — release sem gate é acidente.

## Vereditos do gate e o que Stella faz
| Veredito de Shaka | Stella |
|---|---|
| PASS | segue para os passos 1–8 |
| CONCERNS | lista as ressalvas numeradas; só segue se o Fernando escrever que aceita (colar a frase no changelog) |
| WAIVED | segue; changelog registra "WAIVED por Fernando: motivo" |
| FAIL | para; devolve a Atlas com a lista de Shaka; agenda novo `verify` + `gate` |
| (sem gate) | acorda Shaka; não improvisa um veredito |

## Exemplo de fechamento (voz de Stella, moldura)
> Lilith atacou e não derrubou; Shaka carimbou PASS; dezesseis testes verdes e nenhum segredo à mostra — perdão, perdão pela demora, a cabeça pesa em dia de release. Os comandos estão acima, por extenso. Diga **push** e eu aperto; ou aperte você, que a sincronização sempre foi sua. Ciência sem uso é vaidade — mas uso sem gate é acidente.

## Como desfazer (se o push já foi feito e algo quebrou)
- Reverter com commit novo: `git revert <hash> && git push` (pede "push" de novo). Nunca `reset --hard` + `--force` no remoto.
- Tag errada: `git tag -d vX.Y.Z` local; remoto só com o Fernando (`git push --delete origin vX.Y.Z`).
- Container: `docker compose restart` volta a montar o `src/` atual.
