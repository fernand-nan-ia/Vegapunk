# Story: Kit 2b — Diários dos Satélites por pessoa
**Projeto:** vegapunk   **Status:** rascunho (aguarda 2a)
**Origem:** pedido do Fernando em 2026-09-01; decisão dele: pasta por pessoa (`memory/fernando/`, `memory/<amigo>/`)

## Objetivo (1 frase)
Cada instalação do Vegapunk escreve os diários dos Satélites na pasta do seu dono (`squads/vegapunk/memory/<dono>/`), para que num repo compartilhado os fatos sobre o Fernando não se misturem nem conflitem com os fatos sobre um amigo.

## Contexto que Atlas precisa
- Hoje os 7 agentes têm `memory.file: squads/vegapunk/memory/<id>.md` (caminho absoluto, hardcoded no YAML de cada `.md`) e a ferramenta de diário do bot (`tools.py`) escreve nesses mesmos arquivos.
- Fonte da verdade dos agentes: `.claude/commands/vegapunk/agents/<id>.md`. Editar exige: `pytest -q tests/test_satellites.py` verde + `scripts/sync_agents.sh` + baseline (`tests/satellites_baseline.json`) se algo estrutural mudar.
- Proposta de mecanismo (Atlas decide o detalhe): variável `VEGAPUNK_OWNER` no `.env` (default `fernando`); o caminho do diário vira `memory/${VEGAPUNK_OWNER}/<id>.md`. Nos agentes do Claude Code, que não leem `.env`, o `install_skills.sh` da Story 2c grava o dono no caminho na hora da instalação.
- Migração: mover os 7 diários atuais para `memory/fernando/` preservando conteúdo e histórico git (`git mv`).

## Critérios de aceite (rascunho)
- [ ] Diários atuais migrados para `squads/vegapunk/memory/fernando/` sem perda de conteúdo
- [ ] Bot escreve diário na pasta do dono definido em `VEGAPUNK_OWNER` (teste com dono alternativo)
- [ ] Agentes do Claude Code apontam para a pasta do dono (via sync ou instalação)
- [ ] `test_satellites.py` e baseline verdes; `sync_agents.sh` rodado
- [ ] Duas "instalações" simuladas com donos diferentes não tocam os arquivos uma da outra

## Fora de escopo
Controle de leitura (todos os colaboradores continuam vendo os diários de todos — repo compartilhado é vitrine; o README da 2c avisa).

## Riscos / Shaka
Herda o veredito de 2026-09-01 (condição 3: colaborador enxerga tudo — avisar no README). Refinar no `*risk` próprio quando a story for promovida a pronta.

## Testes esperados
A definir na promoção (mínimo: caminho do diário por dono + migração sem perda).

## Como desfazer
`git mv` de volta para `memory/*.md` e reverter o caminho nos agentes + sync.

## Handoff → Atlas: promover a "pronta" (revisar com Stella) depois da 2a
