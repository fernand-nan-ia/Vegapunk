# Changelog

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
