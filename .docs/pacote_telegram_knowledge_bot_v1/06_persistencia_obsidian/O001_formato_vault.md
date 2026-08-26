# O001 — Vault Obsidian: Formato, Nomenclatura e Git

## Localização e estrutura

```
<vault>/knowledge-inbox/
├── youtube/
│   └── 2026-08-13_qualquer-um-vira-admin_6DJFl-g83dM.md
├── tiktok/        (Fase 2)
├── instagram/     (Fase 3)
└── _pending/      (itens pending_manual — stub com link e metadados mínimos)
```

Nomenclatura: `<data-captura>_<slug-do-titulo-max-60-chars>_<external_id>.md`. O `external_id` no nome garante unicidade e permite localizar o registro no Postgres a partir do arquivo.

## Template do arquivo

```markdown
---
item_id: "<uuid>"
platform: youtube
external_id: "<videoId>"
canonical_url: "<url>"
channel: "<canal>"
captured_at: 2026-08-13
status: enriched
triage: null            # archive | apply_saas | apply_client | discard
tags: [rails-security, vibecoding]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: alta
confidence: alta
---

# <Título>

## Resumo

<summary do enriquecimento>

## Pontos-chave

- <key_point 1>
- <key_point 2>

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha até o fim do arquivo
     é mantido pelo vault:rebuild. Anote aqui livremente. -->
```

## Regras

- **REQ-O01 (ADR-003):** o arquivo é projeção do Postgres. A rake task `vault:rebuild` regenera todo o vault a partir do banco. Na regeneração, a seção `## Notas manuais` (do comentário-sentinela até EOF) do arquivo existente é lida e reinjetada no novo arquivo.
- **REQ-O02:** frontmatter YAML espelha campos do banco 1:1 — é o que permite queries via Dataview no Obsidian e parsing trivial pelo Claude Code.
- **REQ-O03:** triagem do usuário atualiza banco E frontmatter (`triage:` + `status:`) no mesmo job.
- **REQ-O04:** commit git automático por item: mensagem `kb: add|update <platform>/<external_id>`. Push é batch (job a cada hora ou manual) — commit local nunca falha por rede; push com retry (ERR-008).
- **REQ-O05:** transcript bruto NÃO vai para o vault (polui busca e infla o repo). Vive só em `raw_content` no Postgres.

## Consumo pelo Claude Code (Fase 1)

O vault versionado é a interface. Padrões de uso:

1. **Contexto direto:** referenciar arquivos relevantes no prompt do agente (`@knowledge-inbox/youtube/...`).
2. **Descoberta:** `grep -rl "tag-desejada" knowledge-inbox/` ou busca por frontmatter — instrução que pode ser embutida no CLAUDE.md do projeto.
3. Sugestão de bloco para o CLAUDE.md dos dois projetos:

```markdown
## Base de conhecimento
Antes de implementar features relacionadas a segurança, IA ou padrões novos,
consultar knowledge-inbox/ (grep por tags no frontmatter). Itens com
applicability.saas_pessoal: alta são leitura obrigatória para este projeto.
```
