# Checklist: atlas-db-predeploy

Rodada por Atlas em `*schema` (seção Schema), `*rls` (seção RLS) e `*migration apply` (seção Migration). Absorvida de `database-design-checklist`, `dba-predeploy-checklist` e `dba-rollback-checklist` do FURY (data-engineer), condensada para Supabase e SQLite. Cada item ✅/❌/N/A com evidência (comando + saída).

## Schema

- [ ] Toda tabela tem `id` PK, `created_at`, `updated_at`
- [ ] Toda FK existe de verdade no DDL (não só "no código") e tem `ON DELETE` explícito
- [ ] `NOT NULL` em campos obrigatórios; `CHECK` em status/enum; `UNIQUE` onde não pode repetir
- [ ] Índice em cada FK e em cada coluna de filtro frequente — e nenhum sem justificativa
- [ ] Nomes consistentes (snake_case, plural nas tabelas, sem abreviação criativa)
- [ ] Comentário de uma linha por tabela (`COMMENT ON` / `--`)
- [ ] Tabelas com dado de usuário marcadas para RLS

## RLS (Supabase)

- [ ] `rowsecurity = true` em toda tabela do schema `public` com dado de usuário
- [ ] Política para cada operação usada (select/insert/update/delete) — não só select
- [ ] `with check` presente em insert/update (senão o usuário grava no dono errado)
- [ ] Teste positivo E negativo executados (A vê o seu; A não vê o de B) com saída colada
- [ ] `service_role` não aparece em código de frontend nem em `.env` público
- [ ] Funções `security definer` listadas e justificadas uma a uma
- [ ] Aviso dado: sem Auth, `auth.uid()` é `NULL` e tudo é negado

## Migration

- [ ] Snapshot criado ANTES (caminho mostrado): `supabase db dump` / cópia do `.sqlite`
- [ ] Arquivo dentro de transação (`begin`/`commit`) e idempotente (`if [not] exists`)
- [ ] Ordem de dependências verificada (tabela → FK → índice; backfill → `NOT NULL`)
- [ ] Dry-run executado na mesma sessão, sem erro
- [ ] `_rollback.sql` irmão existe e foi lido em voz alta (o que ele restaura)
- [ ] Operação destrutiva (drop/rename/truncate) marcada ⚠️ e aprovada por Shaka
- [ ] Alvo confirmado: local (padrão) ou produção com "sim, produção" explícito
- [ ] Smoke test pós-aplicação: `count(*)` antes × depois em cada tabela tocada; insert de teste revertido
- [ ] Nenhuma connection string com senha ecoada na conversa

## Rollback (se precisou)

- [ ] Snapshot/arquivo escolhido mostrado e confirmado
- [ ] `_rollback.sql` tentado antes do restore completo
- [ ] Smoke test após rollback com saída colada
- [ ] Registro em `memory/atlas.md` › `## Construído`

## Veredito

PODE APLICAR / NÃO PODE (item ❌ + o que falta)

## Lembrete da Atlas

Snapshot não é burocracia, é o "como desfazer" do banco. Sem ele, Atlas não aplica — nem em modo yolo, nem com o Fernando insistindo. Se ele insistir, é decisão de risco: chama Shaka.
