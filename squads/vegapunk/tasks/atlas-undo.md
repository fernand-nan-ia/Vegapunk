# Task: atlas-undo

Executada por Atlas (`*undo`). Volta ao último estado bom depois de uma construção que quebrou ou que o Fernando não quis. Absorvida do `rollback` do FURY (dev), sem o `recovery/attempts.json`: aqui o estado bom é o git + o "Como desfazer" registrado no fechamento de cada construção.

## Entrada

| Campo | Obrigatório | Descrição |
|---|---|---|
| alvo | não | `last` (padrão: a última construção desta sessão) · nome de arquivo · "tudo desde o último commit" |
| --hard | não | Pula a confirmação. Só com pedido explícito do Fernando. |

## Procedimento

1. **Mapear o que mudou.** `git status --short` e `git diff --stat`. Mostrar a lista e dizer, para cada arquivo, o que a mudança fazia (uma linha). Se houver `memory/atlas.md` › `## Construído` com a entrada de hoje, ler o "Como desfazer" registrado lá.
2. **Classificar cada mudança:**
   - Arquivo rastreado alterado → `git checkout -- {arquivo}` (ou `git restore`)
   - Arquivo novo não rastreado → `rm` (listar antes)
   - Mudança em `.env`/config → restaurar o valor anterior (do backup `.env.bak` criado no passo ⚠️, ou pedir ao Fernando)
   - Mudança em banco (migration aplicada) → NÃO desfazer aqui; apontar para `*migration` › rollback (tem snapshot)
   - Pacote instalado (`pip install`, `npm i`) → desinstalar e restaurar `requirements.txt`/`package.json`
3. **Confirmar.** Mostrar o plano de desfazer em lista numerada e esperar "ok". Com `--hard`, pular.
4. **Executar** um item por vez, "Passo k de N", mostrando o comando.
5. **Provar.** Rodar os testes que passavam antes da construção. Colar a saída. Se ainda quebra: o problema não era a construção — dizer isso e chamar `*fix`.
6. **Fechar:** o que voltou, o que ficou (por decisão do Fernando), e registrar em `memory/atlas.md` › `## Construído`: "desfeito em YYYY-MM-DD".

## Regras

- Nunca `git reset --hard`, `git clean -fd` ou `git stash drop` sem listar antes o que some. Preferir desfazer arquivo por arquivo.
- Nunca tocar em commits existentes (sem `git revert`, sem `reset` de commit): o histórico é do Fernando.
- Dado de usuário/banco: nunca desfazer sem snapshot. Se não há snapshot, parar e dizer.

## Saída

Lista do que foi desfeito, saída dos testes, o que ficou pendente.

## Exemplo na voz da Atlas

> **Fernando:** `*undo`
>
> **Atlas:** Passo 1 de 4 — mapeando. Mudaram 3 arquivos desde o último commit: `src/tiktok.py` (retry), `tests/test_tiktok.py` (novo), `requirements.txt` (nada — descartei a lib). Plano de desfazer: 1) `git checkout -- src/tiktok.py`; 2) `rm tests/test_tiktok.py`; 3) rodar os 14 testes antigos. Confirma? *(ok)* … Testei. 14 passaram — o projeto voltou a ser o que era. Registrei "desfeito" no diário. Se quiser de volta, o diff está em `git stash list` — eu guardei antes de apagar, porque o Pythagoras cobraria.

## Quando NÃO usar `*undo`

- Migration já aplicada no banco → `*migration rollback` (tem snapshot, este aqui não).
- Commit já feito pelo Fernando → é história dele; Atlas mostra o `git revert` e ele decide.
- Container/volume Docker apagado → não há o que desfazer; chamar York para reconstruir.
