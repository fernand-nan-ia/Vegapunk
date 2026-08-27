# Task: atlas-db-schema

Executada por Atlas (`*schema`). Desenha (ou revisa) o schema de uma feature antes de escrever a migration. Absorvida do `create-schema`/`model-domain` do FURY (data-engineer/Tank), para Supabase (Postgres) no SaaS e SQLite no Vegapunk/local.

## Entrada

| Campo | Obrigatório | Descrição |
|---|---|---|
| domínio | sim | Uma frase: o que o sistema precisa guardar ("assinaturas de clientes com plano e status") |
| banco | não | `supabase` (padrão no SaaS) · `sqlite` (padrão no Vegapunk) |
| existente | não | Caminho de migrations/schema atual, se houver |

## Procedimento

1. **Entender o domínio antes de modelar.** Perguntar (uma vez, junto): quais entidades, como se relacionam, quem lê e quem escreve, quantas linhas em 1 ano. Nível júnior: "entidade = coisa que tem nome próprio no seu negócio; relação = quem pertence a quem".
2. **Ler o que existe.** Migrations em `supabase/migrations/` ou o `schema.sql`/`models.py`. Nunca propor tabela que já existe com outro nome.
3. **Padrões de acesso primeiro.** Listar as 3–5 consultas mais frequentes ("listar assinaturas ativas de um usuário"). Índice nasce delas, não da intuição.
4. **Desenhar as tabelas.** Para cada uma, mostrar o DDL e dizer para que serve cada coluna. Baseline obrigatório:
   - `id` PK (`uuid default gen_random_uuid()` no Supabase; `INTEGER PRIMARY KEY` no SQLite)
   - `created_at`, `updated_at` (trigger ou default `now()`)
   - FKs com `ON DELETE` explícito (`RESTRICT` por padrão; `CASCADE` só se o Fernando aprovar, com ⚠️)
   - `NOT NULL` em tudo que é obrigatório; `CHECK` em enums/status; `UNIQUE` onde não pode repetir
   - `deleted_at` (soft delete) só se houver necessidade de trilha de auditoria
   - `COMMENT ON` (Postgres) ou comentário `--` no DDL, uma linha por tabela
5. **Índices.** Um por FK; um por coluna de filtro frequente do passo 3. Justificar cada um em uma linha. Sem índice "por via das dúvidas".
6. **Segurança (Supabase).** Marcar quais tabelas terão dado de usuário → precisarão de RLS (`*rls`). Tabela pública sem RLS é bloqueio: não segue.
7. **Normalização pragmática.** Normalizar até parar de duplicar dado; desnormalizar só com consulta do passo 3 que justifique, dizendo qual.
8. **Revisar com `squads/vegapunk/checklists/atlas-db-predeploy-checklist.md`** (seção Schema).
9. **Fechar:** DDL completo em um bloco, diagrama em texto (`tabela_a 1─N tabela_b`), lista de índices com justificativa, próximo passo: `*migration` para aplicar. "Como desfazer": nada foi aplicado ainda; é só rascunho.

## Regras

- Correção antes de velocidade. Cada coluna com explicação.
- Nunca aplicar nada aqui: desenho é desenho; aplicar é `*migration`.
- Se a modelagem mudar regra de negócio ("cliente pode ter 2 planos?"), é decisão do Fernando — perguntar, não assumir.

## Saída

DDL + diagrama em texto + índices justificados + tabelas marcadas para RLS.

## Exemplo na voz da Atlas

> **Fernando:** `*schema assinaturas de clientes com plano e status`
>
> **Atlas:** Antes de desenhar, três perguntas de uma vez: um cliente pode ter mais de uma assinatura ativa? Os planos mudam de preço (histórico) ou é um valor só? Quem consulta mais: o painel do cliente ou o seu admin? *(respostas)* … Passo 1 de 5 — duas tabelas: `plans` (catálogo, poucas linhas) e `subscriptions` (uma por cliente, FK para `plans` e para `auth.users`). Olha esse trecho:
> ```sql
> create table subscriptions (
>   id uuid primary key default gen_random_uuid(),
>   user_id uuid not null references auth.users(id) on delete restrict,
>   plan_id uuid not null references plans(id) on delete restrict,
>   status text not null check (status in ('trial','active','past_due','canceled')),
>   created_at timestamptz not null default now(),
>   updated_at timestamptz not null default now()
> );
> ```
> Serve para isto: `check` impede status inventado; `on delete restrict` impede apagar um plano que ainda tem gente. Índice em `user_id` porque o painel do cliente filtra por ele. Essa tabela tem dado de usuário → `*rls` antes de ir para produção. Entendeu?
