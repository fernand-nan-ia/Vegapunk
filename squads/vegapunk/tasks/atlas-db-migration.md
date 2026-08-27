# Task: atlas-db-migration

Executada por Atlas (`*migration`). Planeja, ensaia, aplica e sabe desfazer uma migration. Absorvida de `create-migration-plan`/`snapshot`/`dry-run`/`apply-migration`/`rollback` do FURY (data-engineer). Vale para Supabase (CLI + Postgres) e SQLite (arquivo + `sqlite3`).

## Entrada

| Campo | Obrigatório | Descrição |
|---|---|---|
| ação | sim | `plan` · `dry-run {arquivo}` · `apply {arquivo}` · `rollback {snapshot ou arquivo}` |
| banco | não | `supabase` · `sqlite` (detectado pelo projeto se omitido) |

## Procedimento — `plan`

1. Ler o DDL desejado (saída do `*schema` ou pedido). Listar cada mudança e classificar: **aditiva** (nova tabela/coluna nullable — segura), **destrutiva** (drop, rename, `NOT NULL` em coluna com dado — ⚠️), **de dado** (backfill).
2. Ordenar: tabelas antes de FKs, colunas antes de índices, backfill antes de `NOT NULL`. Explicar por quê em uma linha.
3. Escrever o arquivo `{timestamp}_{nome}.sql` idempotente (`if not exists`/`if exists`), dentro de transação (`begin; … commit;`), e o arquivo irmão `{timestamp}_{nome}_rollback.sql`. Mostrar os dois com "para que serve".
4. Mudança destrutiva sem rollback possível (drop de coluna com dado): parar e chamar Shaka. Não é decisão de Atlas.

## Procedimento — `dry-run`

1. **Snapshot antes de tudo.**
   - Supabase local: `supabase db dump -f snapshots/{timestamp}_pre.sql` (ou `pg_dump --schema-only`).
   - SQLite: `cp data/{db}.sqlite snapshots/{timestamp}_pre.sqlite`.
   Sem snapshot, não segue. Mostrar o caminho gerado.
2. Rodar a migration dentro de `begin; … rollback;` (Postgres) ou em cópia do arquivo (SQLite). Colar erros, se houver.
3. Checar ordem de dependências (FK aponta para tabela que já existe?) e idempotência (rodar duas vezes não quebra?).

## Procedimento — `apply`

1. Exigir `dry-run` verde na mesma sessão. Caso contrário, rodar o dry-run primeiro.
2. Confirmar o alvo: **local** (padrão) ou **produção** (⚠️ — exigir "sim, produção" explícito do Fernando; York avisado se custa).
3. Aplicar: `supabase db push` / `supabase migration up` ou `sqlite3 data/{db}.sqlite < {arquivo}`. Colar a saída.
4. Smoke test: `select` em cada tabela tocada, `count(*)` antes × depois, um `insert` de teste em transação revertida.
5. Rodar `squads/vegapunk/checklists/atlas-db-predeploy-checklist.md` (seção Migration).
6. Fechar: o que foi aplicado, onde, snapshot correspondente, "Como desfazer": `*migration rollback {snapshot}`.

## Procedimento — `rollback`

1. Mostrar o snapshot/arquivo escolhido e o que ele restaura. Confirmar.
2. Preferir o `_rollback.sql` (cirúrgico); usar restore do snapshot só se o script falhar ou não existir.
3. Executar, colar saída, rodar smoke test, registrar em `memory/atlas.md` › `## Construído`.

## Regras

- Nunca rodar migration em produção sem snapshot + dry-run + confirmação explícita.
- Nunca ecoar connection strings com senha; redigir.
- Tudo em transação; tudo idempotente; tudo reversível — ou não é migration, é aposta.

## Saída

Arquivos de migration + rollback, caminho do snapshot, saída real de dry-run/apply/smoke test.
