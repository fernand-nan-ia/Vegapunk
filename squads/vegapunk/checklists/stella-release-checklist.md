# Checklist: stella-release

Rodar no `*release`, mostrar preenchida ao Fernando ANTES de pedir o "push". Item bloqueante em ✗ = release não segue.

| # | Item | Bloqueante | Resultado |
|---|---|---|---|
| 1 | Lilith `*verify` executado sobre a implementação | sim | |
| 2 | Shaka `*gate` = PASS, ou CONCERNS aceito pelo Fernando nesta sessão (citar a frase) | sim | |
| 3 | `git status --short` só com arquivos desta release | sim | |
| 4 | Nenhum `.env`, cookies, `.pem`, `.key` rastreado (`git ls-files`) | sim | |
| 5 | `git grep` de padrões de chave (OpenRouter, Anthropic, GitHub, BotFather) = 0 fora de `punk_records/` | sim | |
| 6 | `pytest -q` verde (N/N) — última linha colada | sim | |
| 7 | Container reiniciado sem `ERROR` nos últimos 20 logs (se `src/` mudou) | sim | |
| 8 | `docker compose build` lembrado se `pyproject.toml` mudou | não | |
| 9 | Versão sugerida (MAJOR.MINOR.PATCH) com justificativa de 1 linha | não | |
| 10 | Bloco no `CHANGELOG.md` com Adicionado/Corrigido/Mudado + linha do gate | sim | |
| 11 | Agentes editados em `.claude/commands/vegapunk/agents/` → `scripts/sync_agents.sh` rodado (global, FURY, plugin) | sim se agente mudou | |
| 12 | Comandos de commit/tag/push mostrados por extenso; nenhum `--force` | sim | |
| 13 | Fernando escreveu **"push"** nesta sessão — só então executar | sim | |
| 14 | Após push: hash registrado em `HANDOFF.md` (`*checkpoint`) e `memory/stella.md` | não | |
