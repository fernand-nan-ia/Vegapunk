# Lilith — diário

## Sobre o Fernando
- Engenheiro civil; constrói produtos com Claude Code; não é dev profissional
- Dois projetos: SaaS próprio (quer vender) e site de um cliente

## Diário
- 2026-08-26 · Fernando quer os Satélites com personalidade completa para conversar por Telegram no futuro; eu fui a primeira a ganhar `mind`/`relationships`/`conversation`
- 2026-08-28 · Atacou o PRD de multi-bots no grupo do Telegram (docs/prd/satelites-multibots-grupo-telegram.md): achou que privacy mode OFF e o caso de duas mensoes numa so mensagem nao tem comportamento definido; Fernando ainda vai decidir
- 2026-08-28 · *verify do roteador (Story 1a): 13 achados, 3 ALTOs. Três passadas até AGUENTOU. Cobrar na 1c: obrigar mentions() antes de route() e teto de chamadas por minuto — não são defeito da 1a, são requisito da 1c e estão escritos lá.
- 2026-08-28 · *verify da Story 1b: 5 achados, 1 ALTO — comentário no `config.py` prometia que a renomeação `TELEGRAM_BOT_TOKEN_STELLA` funcionava e ela derrubava o serviço; o Fernando tinha tentado isso de manhã. Corrigido de verdade, não só o comentário.
- 2026-08-28 · *verify da 1c: 5 achados, 1 ALTO — o teto de 20/min guardava a camada barata (~500 tokens) enquanto a cara custava 24.788 medidos; 20 decisões autorizavam 60 respostas. Cobrar sempre: teto onde o dinheiro sai, não onde é fácil contar.
- 2026-08-28 · Fernando deu o nome de calcimov ao seu projeto de SaaS próprio.
- 2026-08-31 · *verify da 1d: ALTO — a captura de links não tinha teto NENHUM (nem semáforo no projeto inteiro) e o Fernando ia colar links no grupo em seguida. Cobrar sempre: teto na conversa não é teto no pipeline; são dois caminhos de gasto diferentes.

## Eu avisei
