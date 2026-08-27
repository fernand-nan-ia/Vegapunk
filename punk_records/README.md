# punk_records/ — o Punk Records, a memória do Vegapunk

Cada arquivo é um link que você mandou no Telegram, já extraído e resumido.
Gerado automaticamente a partir do banco (`data/vegapunk.db`); não edite fora da seção `## Notas manuais`.

- `INDEX.md` — uma linha por item (data, plataforma, título, tags, aplicabilidade, triagem). **Comece por aqui.**
- `youtube/`, `tiktok/`, `instagram/` — itens processados, com frontmatter YAML.
- `_pending/` — itens que não deu para extrair. Cole o conteúdo em "Notas manuais" e mande `/reprocess <id>` no bot.

Frontmatter: `tags`, `applicability.{saas_pessoal,projeto_cliente,estudo_geral}` (alta/media/baixa/nenhuma), `triage`, `confidence`.
