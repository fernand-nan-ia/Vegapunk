# Changelog

## v1.4.0 — 2026-08-27
### Adicionado
- **Documentos pelo Telegram**: PDF, DOCX, XLSX/XLSM, TXT/MD/CSV (≤ 20 MB) → `platform: document`, texto integral no vault (`punk_records/document/`), duplicata por hash do conteúdo, links na legenda também capturados. `extract_document` (pypdf + `pdftotext` de reserva, python-docx com títulos/tabelas, openpyxl por aba com teto de 300 linhas).
- Dockerfile: `poppler-utils`. `pyproject`: pypdf, python-docx, openpyxl (exige `docker compose build`).
- **Temas**: cada item ganha `theme` (escolhido pelo modelo; `themes.guess_theme` de reserva). `INDEX.md` com mapa de temas e itens agrupados por tema; `punk_records/temas/<tema>.md` — uma página por assunto para outros projetos lerem. `scripts/backfill_themes.py` classifica o acervo existente numa chamada.
### Corrigido
- Páginas que derrubam clientes 'de robô' (planalto.gov.br): `extract.fetch_html` baixa com cabeçalhos de navegador, trafilatura como reserva. Teto de artigos/documentos subiu para 150k chars (`settings.max_document_chars`) — uma lei inteira cabe.

### Gate: Shaka PASS (ressalva: restart com item em retentativa perde a task em voo; resume_unfinished retoma) · Verify: Lilith ✓ (docs, planalto e temas testados em produção) · Testes: 70/70
## v1.3.0 — 2026-08-27
### Adicionado
- Satélites com **ferramentas no Telegram** (`tools.py`, tool-use via OpenRouter): `search_punk_records`, `read_item`, `punk_records_status` (saúde + custo em US$), `recent_changes` (git log do vault), `write_diary`. Loop de até 3 rodadas em conversa e 8 em comando.
- **Comandos `*` no Telegram**: whitelist por Satélite (`satellites.TELEGRAM_COMMANDS`) dos comandos que são raciocínio sobre o vault; o procedimento do `.md` vai ao prompt. `*help` e comandos que exigem código respondem sem token ("se faz no Claude Code").
- Busca do vault por corpo dos itens com radical de palavra (`satellites.search_index`); prompt manda consultar antes de responder.
- `CLAUDE.md` do projeto: consultar o Punk Records antes de responder; Satélite ativo por nome.
### Gate: Shaka PASS · Verify: Lilith ✓ (loop, comandos e respostas prontas testados em produção) · Testes: 58/58

## v1.2.0 — 2026-08-27
### Adicionado
- Artigos/páginas web como fonte (`platform: article`): extração com trafilatura (título, autor, data, Markdown), texto integral guardado no vault em `## Texto integral`, pasta `punk_records/article/`. Duplicata por hash da URL sem rastreadores (utm, fbclid…).
- Resultado no Telegram na voz de um Satélite: enriquecimento devolve `satellite` + `satellite_take`; seção `## <ícone> <Nome> diz` no `.md`.
- `voices.py`: mensagens de captura, duplicata e erros em personagem (templates, sem custo). Cabeçalho inequívoco `ícone Nome · Punk-NN`.
- Quem anuncia a captura é quem apresenta: Satélite sorteado no `on_message`, gravado na coluna `knowledge_items.satellite` (migração automática) e imposto ao modelo no enriquecimento.
- `brief` no enriquecimento: 2-3 frases para o Telegram; `summary` (4-10 frases), tópicos e ferramentas ficam só no Punk Records.
- Mensagens longas vão em partes (fim do corte com "…"); teclado de triagem na última parte.
- Duplicata e falhas de extração/resumo são anunciadas pelo Satélite dono do lote (`voices.duplicate_line`/`failure_line` com `sat`); duplicata diz explicitamente "nada novo para apresentar".
### Mudado
- Prompt de enriquecimento: regras para artigos (resumo mais completo) e guia de vozes; `content_type: article`.
- `pyproject.toml`: +trafilatura (exige `docker compose build`).
### Gate: Shaka PASS · Verify: Lilith ✓ (migração e schema testados em produção) · Testes: 51/51

## v1.1.0 — 2026-08-27
### Adicionado
- Os 7 Satélites ganharam cânone completo do arco de Egghead (One Piece Wiki + vídeos da comunidade): aparência, habilidades, eventos, relações, falas e diálogos — de forma aditiva, sem remover comandos ou seções.
- README completo: capacidades, instalação, uso no Telegram e no Claude Code, perfil e personalidade de cada Satélite, Punk Records, `.env`, operação.
- `CHANGELOG.md`.
### Mudado
- Pasta do vault renomeada: `knowledge/` → `punk_records/` (config, `.env.example`, agentes, plugin, squads, docs). Caminhos no SQLite migrados (backup em `data/vegapunk.db.bak-rename-20260827`).
### Corrigido
- `vault.write_index` tolera `vault_path` gravado com a pasta antiga (não derruba o INDEX após renomeação); teste de regressão.
- Lilith: aparência corrigida (macacão rosa + capacete de aviadora); York: olhos água-marinha.
### Gate: Shaka PASS (finding da Lilith sobre caminhos no banco corrigido e testado) · Verify: Lilith ✓ · Testes: 42/42
