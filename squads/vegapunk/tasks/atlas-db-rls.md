# Task: atlas-db-rls

Executada por Atlas (`*rls`). Escreve e TESTA políticas de Row Level Security no Supabase. Absorvida de `create-rls-policies`/`policy-apply`/`test-as-user`/`security-audit rls` do FURY (data-engineer). Item do vault de referência: "5 Falhas Críticas de Segurança em SaaS feitos com IA" (tabela sem RLS é a falha nº 1).

## Entrada

| Campo | Obrigatório | Descrição |
|---|---|---|
| tabela | sim | Nome da tabela (ou `audit` para varrer todas) |
| modo | não | `kiss` (padrão: uma política por operação baseada em `user_id`) · `granular` (papéis, equipes, admin) |

## Procedimento

1. **Auditoria rápida.** Listar tabelas do schema `public` e o estado de RLS de cada uma:
   `select tablename, rowsecurity from pg_tables where schemaname = 'public';`
   Tabela com `rowsecurity = false` e dado de usuário = 🔴. Mostrar a tabela e explicar: "sem RLS, qualquer pessoa com a chave anon lê tudo".
2. **Descobrir a coluna de dono.** `user_id`, `owner_id`, `tenant_id`… Se a tabela não tem, parar: RLS sem coluna de dono não protege nada — voltar ao `*schema`.
3. **Escrever as políticas** (modo `kiss`), mostrando cada uma com "para que serve":
   ```sql
   alter table {t} enable row level security;
   create policy "{t}_select_own" on {t} for select using (auth.uid() = user_id);
   create policy "{t}_insert_own" on {t} for insert with check (auth.uid() = user_id);
   create policy "{t}_update_own" on {t} for update using (auth.uid() = user_id) with check (auth.uid() = user_id);
   create policy "{t}_delete_own" on {t} for delete using (auth.uid() = user_id);
   ```
   Modo `granular`: adicionar políticas por papel (`is_admin()` via função `security definer` — com ⚠️ e explicação do risco).
4. **Avisos obrigatórios:** a chave `service_role` ignora RLS (nunca no frontend); sem Auth configurado `auth.uid()` retorna `NULL` e todas as políticas negam; `security definer` roda como dono da função.
5. **Testar de verdade, positivo e negativo.** Emular dois usuários e provar que A vê o seu e NÃO vê o de B:
   ```sql
   set role authenticated;
   set request.jwt.claims = '{"sub":"<uuid_A>"}';
   select count(*) from {t};   -- só linhas de A
   set request.jwt.claims = '{"sub":"<uuid_B>"}';
   select count(*) from {t};   -- só linhas de B
   ```
   Colar a saída. Sem teste negativo, a política não existe.
6. **Empacotar como migration** (`supabase/migrations/YYYYMMDDHHMMSS_rls_{t}.sql`) idempotente (`drop policy if exists` antes de cada `create policy`) e entregar ao `*migration` para aplicar com snapshot.
7. **Fechar:** tabela → políticas → resultado dos testes A/B. "Como desfazer": `alter table {t} disable row level security;` + `drop policy` (avisar que desfazer REABRE o dado).

## Regras

- Nunca aplicar em produção sem o teste A/B ter passado localmente.
- Nunca ecoar chaves/JWT reais na conversa: redigir.
- Decidir "quem pode ver o quê" é regra de negócio: se não estiver óbvio, perguntar ao Fernando (e Shaka se envolver dado sensível).

## Saída

SQL das políticas, saída dos testes positivo/negativo, arquivo de migration pronto.

## Exemplo na voz da Atlas

> **Fernando:** `*rls subscriptions`
>
> **Atlas:** Passo 1 de 6 — auditoria: `subscriptions` está com `rowsecurity = false`. Traduzindo: hoje qualquer app com a chave `anon` lê a assinatura de todo mundo. Grr. Coluna de dono: `user_id` — ótimo, dá para proteger. Passo 2: quatro políticas `kiss` (uma por operação)… Passo 5 — teste A/B: usuário A conta 2 linhas, usuário B conta 1, A não vê a de B. Colado abaixo. Testei. Passou. Orelhas para cima. Como desfazer: `disable row level security` — mas isso REABRE o dado, então só com Shaka sabendo.
