# Task: stella-checkpoint

Executada por Stella (`*checkpoint`). Absorvida de `checkpoint` (FURY). Leve: sem análise de código, só coleta de estado. Único arquivo editado: `HANDOFF.md` (e, se pedido, `memory/stella.md`).

## Fontes (ler antes de escrever)
1. `/home/crazu/projetos/vegapunk/HANDOFF.md` — estado anterior (para diff).
2. `git -C /home/crazu/projetos/vegapunk log --oneline -15` — o que entrou.
3. `git -C /home/crazu/projetos/vegapunk status --short` — o que está solto.
4. `PYTHONPATH=src .venv/bin/python -m pytest -q 2>&1 | tail -3` — contagem de testes (só se rodar em < 2 min; senão usar a última contagem conhecida e marcar "não rodado").
5. `docker compose ps` — container vivo?
6. Contexto da conversa atual: o que foi feito, decidido e deixado pendente nesta sessão.

## Padrão do HANDOFF.md (manter EXATAMENTE as seções existentes; só atualizar/anexar)
```
# HANDOFF — Vegapunk (atualizado em YYYY-MM-DD, sessão N)
## Estado atual: <uma linha>
  parágrafo da sessão N + bullets (container, modelo, commit, testes)
## Primeira coisa a fazer amanhã      (lista numerada, curta, executável)
## Satélites … / seções temáticas     (anexar subseção "(sessão N, data)" se houve mudança)
## Como operar                        (tabela; só mexer se surgiu comando novo)
## Decisões fechadas (não reabrir)    (anexar decisão nova com data; nunca apagar)
## Armadilhas conhecidas              (anexar armadilha nova em negrito no início do bullet)
## Mapa do código                     (atualizar se arquivo novo em src/)
## Ideias para depois (não iniciadas) (mover para "Estado" o que foi iniciado; anexar ideias novas)
```

## Passos
1. Ler as fontes. Montar diff mental: o que mudou desde o HANDOFF anterior.
2. Atualizar o cabeçalho (data, sessão N+1) e "Estado atual".
3. Reescrever "Primeira coisa a fazer amanhã" a partir dos pendentes reais desta sessão (3–5 itens, verbo no início).
4. Anexar decisões, armadilhas e ideias novas nas seções certas. Não remover histórico; compactar só se o Fernando pedir.
5. Se houve `git push` autorizado nesta sessão, registrar o hash em "Estado atual".
6. Mostrar ao Fernando um resumo em ≤ 6 linhas do que foi atualizado (seções tocadas + próximos passos).
7. Opcional (se houve fato pessoal explícito ou sincronização de Satélite): 1–3 linhas em `squads/vegapunk/memory/stella.md`, seções `## Diário` / `## Sincronizações`.

## Gatilhos recomendados
- Fim de sessão (sempre). Início de sessão em modo verificação: ler HANDOFF + `git log -5` e dizer se está em dia, sem editar.
- Após story concluída, após `*release`, após decisão fechada no `*council`.

## Regras
- Nunca escrever o que não aconteceu; "não testado" é informação válida.
- Nunca commit/push — o Fernando sincroniza.
- Voz de Stella só na moldura (abertura e fechamento); o HANDOFF é prosa técnica seca.

## Modo `verify` (início de sessão, sem editar)
1. Ler HANDOFF.md, `git log --oneline -5`, `git status --short`.
2. Responder em 3 linhas: "HANDOFF está em dia até <commit>; há N commits depois dele não registrados; tree limpa/suja". Se desatualizado, oferecer `*checkpoint`.

## Exemplo de resumo entregue ao Fernando
> Registrado no HANDOFF (sessão 4, 2026-08-27):
> - Estado atual: Stella absorveu route/story/release/checkpoint/premises; testes 16/16; container Up.
> - Primeira coisa amanhã: 1) rodar `scripts/sync_agents.sh`; 2) testar `*release` num commit pequeno; 3) Reel do Instagram.
> - Decisão nova: release só com gate do Shaka. Armadilha nova: nenhuma.
> - Não testado: `*route` com squad ausente.
> A cabeça pesa, mas o registro não falha. Amanhã ele lembra por mim.

## O que NUNCA vai para o HANDOFF
- Conteúdo do vault (fica em `knowledge/`), segredos ou valores do `.env`, opiniões dos Satélites (ficam nos diários), lista de comandos.
