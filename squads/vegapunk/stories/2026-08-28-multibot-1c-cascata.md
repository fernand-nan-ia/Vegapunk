# Story 1c: A cascata no grupo — camadas grátis, roteador e janela de 10 minutos

**Projeto:** vegapunk     **Status:** rascunho (depende de 1a e 1b)
**Origem:** `docs/prd/satelites-multibots-grupo-telegram.md` §4.1 e §0 (b, c, d)

## Objetivo (1 frase)
Ligar o roteador da 1a aos dois bots da 1b, de modo que no grupo só responda quem o Fernando chamou — e que ele possa continuar a conversa por 10 minutos sem repetir o nome.

## Contexto que Atlas precisa (esboço, revisar antes de construir)
- Cascata do §4.1: (0) `is_bot` + `allowed_chat_ids` → (1) `@menção` responde direto **sem** roteador → (2) sem nome e fora da janela = ninguém, custo zero → (3) `router.route` → (4) `chat.reply` de cada apontado.
- Janela: 10 minutos desde a última fala de um Satélite no grupo. `chat_state` já guarda `(chat_id, satellite, updated_at)` — `updated_at` é a base natural.
- `chat_messages` é chaveado por `(chat_id, satellite)`; no grupo o `chat_id` é o mesmo para os dois. Histórico misto do grupo é da Story 2 (H4) — aqui basta a leitura por Satélite.

## Critérios de aceite (esboço)
- [ ] Todos os casos da H2 do PRD passam de ponta a ponta no grupo real (Nova York, um nome, dois nomes, nome como objeto da frase)
- [ ] Mensagem sem nome 5 min depois da Lilith falar → Lilith responde; 11 min depois → ninguém responde
- [ ] Nome explícito de outro Satélite dentro da janela troca o interlocutor
- [ ] `@menção` funciona mesmo com o roteador quebrado (caminho determinístico de escape)
- [ ] Mensagem que morre na camada 2 não gera **nenhuma** chamada ao OpenRouter (verificável no log)
- [ ] Uma tarde de uso real sem loop bot↔bot e com o custo do roteador medido pela York

## Fora de escopo
Os outros 5 bots, histórico compartilhado do grupo, atraso aleatório por bot, `/custo` agregado — tudo Story 2.

## Riscos / Shaka
`*risk` 2026-08-28, **condição registrada**: com privacy mode OFF na Stella, se outra pessoa entrar no grupo as mensagens dela passam a ser gravadas no SQLite e enviadas ao OpenRouter — dado de terceiro. Enquanto o grupo for só do Fernando, aceito. Antes de convidar alguém, reabrir com o Shaka (provável necessidade de filtro por `user_id`).

**Fontes do próprio Telegram (lidas em 2026-08-28) que reforçam a condição:**
- FAQ *"Os bots são seguros?"*: por padrão o bot só vê mensagens dirigidas a ele; com privacy mode OFF ele vê **todas** — e isso fica **visível na lista de membros do grupo** ("tem acesso às mensagens"). Serve como verificação de aceite: depois do setup, conferir na lista de membros que só o Stella aparece com acesso.
- *Standard Bot Privacy Policy* §6.2: o desenvolvedor "nunca compartilhará dados de usuário com terceiros, **incluindo com seus próprios serviços ou bots adicionais**, salvo autorização explícita do usuário". O histórico compartilhado entre os Satélites (H4, Story 2) é exatamente isso — inócuo enquanto o único usuário é o Fernando, **bloqueante** se entrar mais alguém.
- §7.3: se houver outro usuário, o desenvolvedor deve dar acesso à política e responder a pedidos de cópia/exclusão de dados em até **30 dias**.
- FAQ chats secretos: são específicos do dispositivo e ficam **fora da nuvem** do Telegram — e é a nuvem que a Bot API enxerga. Leitura do Stella: **os Satélites não podem viver num chat secreto**; o grupo é chat na nuvem (criptografia cliente-servidor), então tudo que passa por lá está nos servidores do Telegram. Não é problema para este uso, mas é um fato a não esquecer antes de colar segredo no grupo.

## Como desfazer
Desligar a cascata por env (`VEGAPUNK_GROUP_ROUTER=false`) e o grupo volta a não responder; DM intacto.
