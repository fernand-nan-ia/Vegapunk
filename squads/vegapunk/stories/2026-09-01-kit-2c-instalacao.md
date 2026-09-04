# Story: Kit 2c — Instalação para amigos e reinstalação (README + install_skills)
**Projeto:** vegapunk   **Status:** rascunho (aguarda 2a e 2b)
**Origem:** pedido do Fernando em 2026-09-01

## Objetivo (1 frase)
Qualquer amigo de confiança (ou o próprio Fernando numa máquina nova) sai do zero até o primeiro link capturado — ou até só as skills funcionando no Claude Code — seguindo um README, sem precisar do Fernando ao lado.

## Contexto que Atlas precisa
- Repo privado no GitHub com colaboradores; cada instalação roda bot próprio (tokens e chave OpenRouter próprios) e commita `kb:` no MESMO repo. Rotina de sincronização: `git pull --rebase` → `scripts/import_vault.py` (2a) → usar → `git push`.
- Dois perfis de instalação: **completa** (Docker + bot Telegram + skills) e **só skills** (Claude Code lendo o vault, sem bot).
- Armadilha central das skills: os 7 agentes usam caminhos absolutos (`/home/crazu/projetos/vegapunk/...`). O `install_skills.sh` copia para `~/.claude/commands/` reescrevendo os caminhos para onde o clone está — e gravando o dono do diário (2b).
- `.env.example` existe (1.971 bytes); revisar cobrindo TODAS as variáveis do HANDOFF (7 tokens, `TELEGRAM_ALLOWED_USER_IDS`, `TELEGRAM_ALLOWED_CHAT_IDS`, `VEGAPUNK_GROUP_ENABLED`, `VEGAPUNK_GROUP_TRIAGE`, `VEGAPUNK_MODEL`, `VEGAPUNK_ROUTER_MODEL`, `VEGAPUNK_OWNER`), cada uma com 1 linha de comentário.
- Armadilhas conhecidas que o README deve citar: Docker Desktop não sobe sozinho após reboot (`docker compose up -d`); grupo só liga com `TELEGRAM_ALLOWED_USER_IDS` preenchido (condição permanente do Shaka); privacy OFF só no bot leitor.

## Critérios de aceite (rascunho)
- [ ] `INSTALL.md` (ou seção do README): pré-requisitos, BotFather (1 leitor + 6 opcionais), OpenRouter, `.env`, `docker compose up -d`, primeiro link, rotina pull→import→push
- [ ] Perfil "só skills": clone + `scripts/install_skills.sh` → `/vegapunk` funciona no Claude Code em qualquer pasta, com caminhos corretos
- [ ] `.env.example` completo, só placeholders (grep de padrões de chave = 0)
- [ ] Aviso explícito no INSTALL.md: colaborador vê tudo (vault, diários, HANDOFF) — condição 3 do Shaka
- [ ] Teste de fumaça documentado: como conferir que a instalação deu certo em 3 comandos

## Fora de escopo
Repo separado para o motor; automação de convite de colaborador; CI.

## Riscos / Shaka
Herda o veredito de 2026-09-01 (condições 2 e 3). Refinar no `*risk` quando promovida.

## Testes esperados
A definir na promoção (mínimo: install_skills.sh idempotente + reescrita de caminho testada).

## Como desfazer
Apagar INSTALL.md e `scripts/install_skills.sh`; skills instaladas se removem apagando `~/.claude/commands/vegapunk*`.

## Handoff → Atlas: promover a "pronta" depois da 2a e 2b
