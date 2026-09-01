# Story 1c: A cascata no grupo — camadas grátis, roteador e janela de 10 minutos

**Projeto:** vegapunk     **Status:** feita (Atlas, 2026-08-28) — 123 testes; falta só o Fernando ligar o grupo no `.env`
**Origem:** `docs/prd/satelites-multibots-grupo-telegram.md` §4.1 e §0 (b, c, d)

## Objetivo (1 frase)
Ligar o roteador da 1a aos sete bots da 1b, de modo que no grupo só responda quem o Fernando chamou — e que ele possa continuar a conversa por 10 minutos sem repetir o nome.

## Contexto que Atlas precisa
- **O que já existe** (não reconstruir): `bot.is_allowed()` é a camada 0 completa (anti-loop, chat, grupo desligado, usuário). `router.mentions()` é a camada 2 e já ignora nome dentro de link. `router.route()` é a camada 3, com teto de 3 Satélites, falha fechada e cliente próprio. `speakers.say_all()` / `bot.responder()` são a camada 4 e já fazem cada Satélite falar pela própria boca no grupo.
- **O que falta é a costura**: uma função que componha as camadas 1–3 numa decisão só, e o caminho do grupo no `on_message`.
- Camada 1 (`@menção`) sai das **entidades** da mensagem do Telegram (`message.entities` do tipo `mention`), cruzadas com `speakers.usernames` (sat_id → @username, preenchido no arranque). Determinística: **não passa pelo roteador**, então funciona com ele quebrado.
- Janela: 10 minutos desde a última interação no grupo. `chat_state` guarda `(chat_id, satellite, updated_at)` e `Chat.wake()` já atualiza `updated_at` a cada resposta — é a base natural, falta só um leitor.
- Responder COMO um Satélite específico: `Chat.reply()` hoje usa sempre o ativo. Precisa aceitar quem responde, sem mudar o comportamento da DM.
- `chat_messages` é chaveado por `(chat_id, satellite)`. Histórico **misto** do grupo é da Story 2 (H4) — aqui cada Satélite lê o próprio.
- **Links no grupo continuam sendo capturados** como na DM: é a função original do bot e o Fernando encaminha link o tempo todo. Captura não passa pela cascata (não é conversa).

## Herdado do `*verify` da Lilith na Story 1a (dívida que vence aqui)
- **Achado 7** — nada obriga a camada 2 a vir antes da 3. Enquanto o acoplamento ficar com o chamador, alguém esquece e paga roteador em toda mensagem. **Correção:** a composição das camadas vira uma função única no `router.py`; o `bot.py` não tem como chamar `route()` pulando `mentions()`.
- **Achado 8** — sem teto de chamadas por minuto. Rajada de mensagens = rajada de chamadas pagas. **Correção:** teto no próprio `route()`, com falha fechada quando estourar.

## Critérios de aceite
- [ ] A composição das camadas é **uma função só**, testada: `@menção` → responde sem roteador; sem nome e fora da janela → ninguém e **zero chamada**; caso contrário → roteador
- [ ] `mentions()` é impossível de pular: não há caminho no `bot.py` que chame `route()` direto (teste sobre a estrutura, não sobre boa vontade)
- [ ] Teto de chamadas por minuto no `route()`, com falha fechada e log quando estourar (teste com o teto estourado)
- [ ] Janela de 10 min: mensagem sem nome aos 5 min responde o último; aos 11 min, ninguém (teste com relógio controlado)
- [ ] Nome explícito de outro Satélite **dentro** da janela troca o interlocutor
- [ ] `@menção` funciona com o roteador quebrado — teste com `route()` levantando exceção
- [ ] Cada Satélite apontado responde pelo **próprio bot** no grupo (reaproveita `bot.responder()`, já provado na 1b)
- [ ] DM inalterada: `/stella`, `/shaka`… e texto solto continuam como hoje (suíte verde + observação em produção)
- [ ] Link colado no grupo continua sendo capturado, e a captura não aciona a cascata
- [ ] **Só então**, e como último passo: `VEGAPUNK_GROUP_ENABLED=true` no `.env`, **com `TELEGRAM_ALLOWED_USER_IDS` preenchido** (condição permanente do Shaka, registrada no gate da 1a)

## Mudança pedida pelo Fernando depois do primeiro uso real (2026-08-28, PRD §0 e)
Sem nome na mensagem, o roteador entra em **modo triagem** e escolhe o dono pelo ASSUNTO — pode ser o próprio Stella. Cada Satélite ganhou uma linha de especialidade no prompt (`router.ESPECIALIDADES`). **Desfaz a propriedade "grupo calado é grátis"**, que a Lilith aprovou e o Shaka carimbou: mensagem sem nome passa a custar ~500 tokens. O silêncio deixou de ser estrutural e virou decisão do modelo (recado, `ok`, `kkk`, frase sem pergunta → lista vazia). Reversível por `VEGAPUNK_GROUP_TRIAGE=false`, com teste dos dois modos.
**Consequência de processo:** o `*verify` da Lilith e o `*gate` do Shaka sobre a 1c foram dados ANTES desta mudança. Refazer os dois antes do release.

## Fora de escopo
Histórico **compartilhado** do grupo (H4 — cada Satélite ler o que os outros disseram) e `/custo` agregado: Story 2. Um Satélite acionar outro sozinho: Won't da v1.

## Riscos / Shaka
`*risk` 2026-08-28, **condição registrada**: com privacy mode OFF na Stella, se outra pessoa entrar no grupo as mensagens dela passam a ser gravadas no SQLite e enviadas ao OpenRouter — dado de terceiro. Enquanto o grupo for só do Fernando, aceito. Antes de convidar alguém, reabrir com o Shaka (provável necessidade de filtro por `user_id`).

**Fontes do próprio Telegram (lidas em 2026-08-28) que reforçam a condição:**
- FAQ *"Os bots são seguros?"*: por padrão o bot só vê mensagens dirigidas a ele; com privacy mode OFF ele vê **todas** — e isso fica **visível na lista de membros do grupo** ("tem acesso às mensagens"). Serve como verificação de aceite: depois do setup, conferir na lista de membros que só o Stella aparece com acesso.
- *Standard Bot Privacy Policy* §6.2: o desenvolvedor "nunca compartilhará dados de usuário com terceiros, **incluindo com seus próprios serviços ou bots adicionais**, salvo autorização explícita do usuário". O histórico compartilhado entre os Satélites (H4, Story 2) é exatamente isso — inócuo enquanto o único usuário é o Fernando, **bloqueante** se entrar mais alguém.
- §7.3: se houver outro usuário, o desenvolvedor deve dar acesso à política e responder a pedidos de cópia/exclusão de dados em até **30 dias**.
- FAQ chats secretos: são específicos do dispositivo e ficam **fora da nuvem** do Telegram — e é a nuvem que a Bot API enxerga. Leitura do Stella: **os Satélites não podem viver num chat secreto**; o grupo é chat na nuvem (criptografia cliente-servidor), então tudo que passa por lá está nos servidores do Telegram. Não é problema para este uso, mas é um fato a não esquecer antes de colar segredo no grupo.

## Como desfazer
`VEGAPUNK_GROUP_ENABLED=false` no `.env` e o grupo volta a ficar mudo, sem tocar em código — a mesma chave que já protege hoje. Reverter código: `git checkout --` nos arquivos da story.
