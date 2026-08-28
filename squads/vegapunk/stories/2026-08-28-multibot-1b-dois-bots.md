# Story 1b: N bots no mesmo processo — Stella lê, os outros só falam (+ porteiro do dinheiro)

**Projeto:** vegapunk     **Status:** rascunho (só vira `pronta` depois que a 1a passar no gate)
**Origem:** `docs/prd/satelites-multibots-grupo-telegram.md` §0 (a) e §7

## Objetivo (1 frase)
Fazer o Vegapunk rodar vários bots do Telegram no mesmo processo — Stella lendo o grupo e os demais apenas publicando com nome e ícone próprios — sem quebrar nada do DM que já funciona **e sem que ninguém além do Fernando consiga gastar a chave dele**.

## Contexto que Atlas precisa (esboço, revisar antes de construir)
- `bot.py::build_app` hoje monta **uma** `Application` com `settings.bot_token` e `__main__.py` chama `app.run_polling(...)`.
- Passa a existir uma Application por token, todas no mesmo loop `asyncio`, mesmo SQLite. **Só a do Stella registra handlers de mensagem**; a da Lilith existe para `bot.send_message`.
- `.env` novo: um token por Satélite no padrão `TELEGRAM_BOT_TOKEN_<ID EM MAIÚSCULAS>` (`_LILITH`, `_SHAKA`, …). O `TELEGRAM_BOT_TOKEN` atual continua sendo o Stella (não renomear agora — renomeação é da Story 2).
- `config.Settings` ganha `bot_tokens: dict[str, str]` montado por varredura de `satellites.IDS` sobre o ambiente — **não** um campo fixo por Satélite. Ausente = aquele bot simplesmente não sobe.
- **Estado real em 2026-08-28**: o Fernando criou o grupo «Vegapunk» e cadastrou **os 7 bots** no BotFather, todos já no grupo. Stella com privacy OFF (`has access to messages`); os outros 6 com privacy ON (`has no access to messages`), conferido na lista de membros. A configuração manual prevista para as Stories 1b **e 2** já está feita — resta só código.
- **Porteiro do dinheiro** (achados 11 e 12 da Lilith em 2026-08-28, `*verify` do roteador). Hoje `bot.py::allowed()` é a única coisa entre um estranho e a chave do OpenRouter, e tem duas brechas:
  1. **Falha aberta**: `return bool(chat) and (not settings.allowed_chat_ids or chat.id in settings.allowed_chat_ids)` — lista **vazia** faz a expressão inteira virar verdadeira e o bot aceitar qualquer chat do Telegram. É a única falha aberta de um sistema em que todo o resto falha fechado. Bots são públicos: qualquer um que descubra o @username abre DM.
  2. **Sem filtro por pessoa**: dentro de um chat autorizado, QUALQUER participante gasta token do Fernando. Num grupo isso deixa de ser hipótese. Some-se a condição do Shaka: mensagem de terceiro gravada no SQLite e enviada ao OpenRouter é dado de terceiro, e a [política padrão de bots do Telegram](../../../punk_records/article/2026-08-28_standard-bot-privacy-policy-a-politica-de-privacidade-padrao_19b30f460b29.md) §7.3 passa a valer.
- ⚠️ **O id do grupo NÃO entra em `TELEGRAM_ALLOWED_CHAT_IDS` nesta story.** Enquanto a cascata (1c) não existir, autorizar o grupo faz o Stella responder a toda mensagem e capturar todo link. A autorização é o último passo da 1c.
- Privacy mode: OFF só no bot do Stella; Lilith fica ON (privacy limita o que o bot *recebe*, não o que *envia*).

## Critérios de aceite (esboço)
- [ ] `/stella`, `/shaka` … no DM continuam idênticos (suíte atual verde)
- [ ] Uma resposta da Lilith (e do Shaka) no grupo aparece com o nome e o ícone dela, não com os do Stella
- [ ] As Applications que não são a leitora não têm nenhum `MessageHandler` registrado (teste sobre os handlers, não manual)
- [ ] **Anti-loop (bloqueante, condição do Shaka):** mensagem com `from_user.is_bot=True` é descartada antes de qualquer processamento, com teste automatizado
- [ ] Token ausente para um Satélite degrada com aviso no log e o serviço sobe com os que têm token (não derruba nada)
- [ ] **Falha fechada no porteiro:** `TELEGRAM_ALLOWED_CHAT_IDS` vazio passa a recusar TODOS os chats (hoje aceita todos), com uma linha de log gritando o motivo. `/id` continua respondendo sem filtro — é o caminho de bootstrap: instalar → `/id` → preencher o `.env`
- [ ] **`TELEGRAM_ALLOWED_USER_IDS` (novo, opcional):** se preenchido, mensagem de quem não está na lista é descartada ANTES de qualquer chamada paga (teste com `from_user.id` de estranho num chat autorizado). Se vazio, o comportamento é o de hoje **e** o arranque loga aviso quando houver chat de grupo (id negativo) autorizado sem filtro de usuário
- [ ] Teste para cada uma das duas brechas: lista de chats vazia → recusa; usuário fora da lista em chat autorizado → recusa, zero chamada ao modelo
- [ ] Grupo criado **privado**, com "histórico persistente" desligado (membro novo não lê o passado) — FAQ do Telegram, seção de grupos; e na lista de membros só o Stella mostra "tem acesso às mensagens"

## Fora de escopo
Roteador ligado (é a 1c), janela de 10 min, histórico compartilhado, e **autorizar o grupo em `TELEGRAM_ALLOWED_CHAT_IDS`** (só na 1c).
Também fora: teto de chamadas por minuto (achado 8 da Lilith, fica na 1c) e resposta a quem for barrado — o barrado é ignorado em silêncio, não recebe aviso.

## Riscos / Shaka
`*risk` 2026-08-28: token novo no `.env` = **aceito** (mesma classe do que já existe; `.gitignore` e varredura do `*release` cobrem). `is_bot` é **condição bloqueante**.
Lilith `*verify` 2026-08-28, achados 11 e 12 (falha aberta e ausência de filtro por pessoa): tratados nos critérios de aceite acima. O `TELEGRAM_ALLOWED_USER_IDS` é também a resposta parcial à condição do Shaka sobre dado de terceiro — com ele, um convidado no grupo é lido pelo Telegram mas nunca chega ao OpenRouter nem ao SQLite de conversa.

## Como desfazer
Remover os `TELEGRAM_BOT_TOKEN_*` extras do `.env`, reverter `build_app`/`__main__` para uma Application e voltar `allowed()` à versão de uma linha. `TELEGRAM_ALLOWED_USER_IDS` vazio já desliga o filtro de pessoa sem tocar em código.
