# PRD — Satélites como bots separados num grupo do Telegram

> Projeto: vegapunk · Autor: Edison (Punk-03) com Fernando · Data: 2026-08-27 · Status: **escopo aprovado** (decisões do Fernando em 2026-08-28)
> Origem: pedido do Fernando em 2026-08-27 (chat com Stella no Telegram, 21:30), registrado em `squads/vegapunk/memory/stella.md`

## 0. Decisões do Fernando (2026-08-28) — fecham as três perguntas que travavam a Story 1

| # | Pergunta | Decisão |
|---|---|---|
| a | Privacy mode OFF nos 7 bots? | **Sim, mas só no bot leitor.** Um único bot (Stella ou porteiro dedicado) fica com privacy OFF e lê o grupo; os outros 6 são **send-only** (privacy ON, sem handler de mensagem) e apenas publicam com nome e ícone próprios. Resultado visual idêntico, uma superfície de leitura em vez de sete. |
| b | York dispara só por `@menção`? | **Não precisa de exceção.** Quem decide "é pra mim?" deixa de ser regex e passa a ser um **roteador** (1 chamada barata ao modelo, sem persona e sem índice), que lê a frase inteira: "fui pra Nova York" devolve lista vazia. |
| c | Mensagem com dois nomes aciona quem? | **O roteador decide pelo contexto.** "Shaka e Lilith, o que acham?" → os dois; "Shaka, o que você acha do que a Lilith falou?" → só o Shaka. Sem regra fixa escrita à mão. |
| d | Mensagem sem nome nenhum logo após um Satélite falar | **Janela de continuidade de 10 minutos**: o último Satélite que falou continua respondendo. Passados 10 min sem interação, silêncio até alguém ser chamado pelo nome ou `@`. |
| e | Mensagem sem nome **fora** da janela (decidido em 2026-08-28, depois do primeiro uso real) | **Modo triagem**: o roteador passa a escolher o dono pelo ASSUNTO (pode ser o próprio Stella), em vez de calar. **Troca consciente**: a propriedade "grupo calado é grátis" — aprovada pela Lilith e carimbada pelo Shaka — dá lugar a ~500 tokens por mensagem. O roteador continua podendo devolver lista vazia para recado, `ok`, `kkk` e frase sem pergunta. Reversível por `VEGAPUNK_GROUP_TRIAGE=false`. |

**Consequência de projeto:** o Must "filtro local (regex, sem LLM)" do §4 vira uma **cascata de 5 camadas** (§4.1) — o regex continua existindo, mas só como corte de ruído grátis; a decisão de quem responde é do roteador.

## 1. Problema
Fernando conversa com os Satélites pelo Telegram, mas hoje são **um bot só vestindo sete personas**: para falar com outro, ele troca de comando (`/shaka`, `/lilith`...) e só um responde por vez. Ele quer algo mais parecido com estar no laboratório de verdade — um grupo onde cada Satélite é um participante visível, com nome e ícone próprios, e ele fala com quem quiser sem trocar de comando.
**Evidência:** pedido direto ("tem a possibilidade de eu criar para cada satélite um bot aqui no telegram? E fazer um grupo com todos?"), confirmado como próximo passo.

## 2. Objetivo
Sair de "1 bot, 7 máscaras" para **7 bots distintos (nome + ícone próprios) numa única conversa em grupo**, sem que Fernando precise digitar comando de troca — mensurável: no grupo, cada Satélite aparece como remetente separado (hoje são 0; alvo 7) e o Fernando aciona um deles só escrevendo o nome ou @mencionando.

## 3. Usuário
- **Quem:** Fernando, no celular, fora do Claude Code
- **Quer conseguir:** perguntar algo no grupo e deixar o Satélite certo responder — ou chamar um específico — sem sair da conversa
- **Hoje faz assim:** `/lilith`, conversa, depois `/stella` para trocar; nunca vê dois Satélites "na mesma sala"

## 4. Escopo (MoSCoW — ≤ 12 itens)
| | Item | Fins de semana |
|---|---|---|
| **Must** | 7 bots no BotFather (um token por Satélite), todos membros do mesmo grupo | 1 |
| **Must** | Cada bot responde quando @mencionado (`@lilith_vegapunk_bot`) OU quando o roteador o aponta a partir do texto livre ("Lilith, ...") | 0,5 |
| **Must** | Trava anti-loop: nenhum bot processa mensagem cujo autor é outro bot (`from_user.is_bot`) | 0,25 |
| **Must** | Cascata de 5 camadas (§4.1) antes de qualquer resposta em personagem: 3 camadas grátis cortam o ruído, o roteador decide quem fala | 0,5 |
| **Must** | Um único bot leitor (privacy OFF) processa o grupo; os outros 6 são send-only, sem handler de mensagem | 0,25 |
| **Must** | Janela de continuidade de 10 min: sem nome na mensagem, responde quem falou por último dentro da janela; fora dela, ninguém | 0,25 |
| **Must** | `TELEGRAM_ALLOWED_CHAT_IDS` continua valendo — grupo só responde ao(s) chat_id autorizado(s) | — (já existe) |
| **Must** | Histórico do grupo é compartilhado entre os 7 (cada um lê o que os outros disseram, não só o que o humano escreveu) | 0,5 |
| **Should** | Atraso curto e aleatório por bot antes de responder (evita rajada simultânea e flood control do Telegram) | 0,25 |
| **Should** | `/custo` funciona em qualquer um dos 7 e soma o grupo inteiro | 0,25 |
| **Could** | Satélite pode citar outro na resposta ("chama a Lilith") sem disparar a Lilith sozinho — só sugere | 0,25 |
| **Won't** (fora, de propósito) | Um Satélite acionar outro automaticamente sem o Fernando pedir (o "conselho ao vivo") — maior risco de loop e custo; vira PRD v2 depois que a v1 rodar estável | — |
| **Won't** | Substituir o bot único de DM — ele continua exatamente como está; o grupo é aditivo | — |

_Total Must: ~3 fins de semana — não cabe em ≤ 2; **dividir em 2 stories** (ver §10)._

### 4.1 A cascata de decisão (do mais barato para o mais caro)

| Camada | O que faz | Custo por mensagem |
|---|---|---|
| 0 | Ignora mensagem de bot (`from_user.is_bot`) e chat fora de `TELEGRAM_ALLOWED_CHAT_IDS` | zero |
| 1 | Tem `@menção` explícita? → aciona aquele Satélite direto, **sem passar pelo roteador** | zero |
| 2 | Não contém nome de Satélite (regex) **e** está fora da janela de 10 min? → ninguém responde | zero |
| 3 | **Roteador**: 1 chamada ao modelo com a mensagem + últimas 3 linhas do grupo, sem persona e sem `INDEX.md`; devolve `{"satelites": [...], "confianca": "alta\|media\|baixa"}` | ~US$ 0,0002 |
| 4 | Cada Satélite apontado responde em personagem (prompt completo, ~6–14k tokens) | ~US$ 0,002–0,005 cada |

Regras do roteador:
- **Falha fechada**: erro, timeout ou JSON inválido → ninguém responde (nunca "na dúvida, todos").
- `confianca: baixa` → tratado como lista vazia.
- Saída com `response_format json_schema strict` + Pydantic, mesmo padrão do `enrich.py`.
- Toda decisão vai para log/tabela própria com a mensagem e a lista devolvida, para auditar falso positivo e falso negativo na primeira semana.

## 5. Histórias de usuário e critérios de aceite
**H1.** Como Fernando, quero @mencionar um Satélite no grupo para que só ele responda, com nome e ícone próprios.
- [ ] Mandar `@lilith_vegapunk_bot ataca isso` no grupo → só o bot da Lilith responde, com o avatar/nome dela
- [ ] Os outros 6 bots não respondem nem geram log de chamada ao modelo

**H2.** Como Fernando, quero escrever o nome de um Satélite em texto livre ("Lilith, o que acha?") e ele responder, mesmo sem @.
- [ ] "Lilith, o que acha?" aciona o bot da Lilith
- [ ] "fui pra Nova York no ano passado" **não** aciona a York (caso-teste de falso positivo)
- [ ] "Shaka e Lilith, o que acham?" aciona os dois
- [ ] "Shaka, o que você acha do que a Lilith falou?" aciona **só** o Shaka
- [ ] Mensagem sem nenhum nome de Satélite, fora da janela de continuidade, não aciona ninguém nem gera chamada ao modelo
- [ ] Roteador com erro/timeout → ninguém responde (falha fechada)

**H2b.** Como Fernando, quero continuar a conversa sem repetir o nome a cada mensagem.
- [ ] Mensagem sem nome até 10 min depois da última fala de um Satélite → responde aquele mesmo Satélite
- [ ] Mesma mensagem 11 min depois → ninguém responde
- [ ] Nome explícito de outro Satélite dentro da janela troca o interlocutor (a janela não prende a conversa)

**H3.** Como Fernando, quero que nenhum bot responda a mensagem de outro bot, para não ter loop nem gasto de token fora de controle.
- [ ] Mensagem enviada por um dos 7 bots nunca aciona outro dos 7 (testável simulando `is_bot=True`)
- [ ] Teste de estresse: Lilith menciona "Shaka" na resposta → Shaka NÃO dispara sozinho

**H4.** Como Fernando, quero que um Satélite veja o que os outros disseram no grupo, para responder com contexto ("concordo com o Shaka").
- [ ] Histórico usado no prompt inclui as últimas N mensagens do grupo (de humano e de qualquer Satélite), não só as do próprio bot
- [ ] Satélite consegue citar corretamente algo que outro disse 2 mensagens antes (teste manual)

**H5.** Como Fernando, quero continuar falando em DM com o bot único de sempre, sem quebrar nada que já funciona.
- [ ] `/stella`, `/shaka` etc. em conversa privada continuam funcionando como hoje
- [ ] Suíte de testes atual (`tests/test_satellites.py`, `test_db.py`) permanece verde

## 6. Telas
Não há tela — é configuração de bots + lógica de trigger. Onde há "interface", é o BotFather:
| Etapa | Mostra | Wireframe |
|---|---|---|
| Setup de cada bot no BotFather | nome, username, ícone (foto do Satélite), privacy mode | N/A — passo a passo manual, documentar no README |

## 7. Restrições técnicas (o que já existe e não muda)
- Stack: Python 3.12, `python-telegram-bot` (polling, sem webhook), Docker Compose local — sem infra nova
- Banco: SQLite (`data/vegapunk.db`); `chat_messages`/`chat_state` hoje são chaveados por `(chat_id, satellite)` — no grupo, `chat_id` é o mesmo para os 7, o que já funciona para separar histórico por Satélite, mas H4 exige também **ler o histórico misto do grupo** (mensagens de todos), não só o do próprio Satélite — mudança de schema/consulta, não de arquitetura
- `.env` ganha 6 variáveis novas (`TELEGRAM_BOT_TOKEN_SHAKA`, `_LILITH`, ...); `TELEGRAM_BOT_TOKEN` original vira `_STELLA` ou continua sendo o bot de DM — decidir nomeação antes de codar
- `bot.py::build_app` hoje assume 1 `Application`; passa a rodar N `Application`s (uma por token) no mesmo processo `asyncio`, todas lendo/escrevendo no mesmo SQLite. **Apenas a Application do bot leitor registra handlers de mensagem**; as outras 6 existem só para enviar (`bot.send_message`) com nome e ícone próprios
- Privacy mode: **OFF apenas no bot leitor** (precisa receber toda mensagem do grupo). Nos outros 6 fica ON — privacy mode limita o que o bot *recebe*, não o que ele *envia*; membro de grupo publica normalmente. Como eles não têm handler, mesmo um update que chegue é descartado (defesa em profundidade contra resposta dupla)
- O roteador (§4.1, camada 3) reaproveita `enrich._client()` e o modelo barato já em uso; prompt próprio, curto, **sem** persona e **sem** `INDEX.md` — é o que o mantém ~30× mais barato que uma resposta em personagem
- Sem custo de infra: 7 processos de long-polling são leves; o custo real é em tokens do OpenRouter (ver §8) e em **configuração manual** (7× BotFather)
- LGPD/dados pessoais: nenhum dado novo de terceiros; grupo restrito por `allowed_chat_ids`, igual hoje

## 8. Métricas
| Métrica | Hoje | Alvo | Como medir |
|---|---|---|---|
| **Principal:** mensagens bot→bot (loop) em produção / 7 dias | N/A (não existe) | 0 | contar linhas `chat_messages` onde o "usuário" é outro Satélite |
| Secundária: custo médio do grupo por dia | N/A | York mede via `/custo` | soma de `chat_messages.input_tokens/output_tokens` do chat do grupo |

## 9. Riscos e perguntas abertas (≤ 5)
| Risco / pergunta | Mitigação | Lilith ataca? |
|---|---|---|
| Loop de menções entre bots (A cita B, B responde citando A...) | Filtro `is_bot` antes de qualquer processamento; nunca reagir a mensagem de outro bot | ✓ |
| Privacy mode mal configurado em algum dos 7 (bot lê tudo e chama LLM à toa) | Só o bot leitor tem handler — os outros 6 descartam qualquer update; camadas 0–2 rodam antes do LLM; checklist de setup no README | ✓ |
| **Roteador é ponto único de falha e ele próprio erra** (LLM): pode calar todos ou acionar quem não foi chamado; texto do grupo pode tentar induzi-lo | Falha fechada (erro → silêncio); `confianca: baixa` = ninguém; schema estrito + Pydantic; log de toda decisão para auditar falso positivo/negativo na 1ª semana; `@menção` sempre funciona **sem** o roteador, então existe caminho determinístico de escape | novo, 2026-08-28 |
| 7 bots respondendo quase juntos = bagunça visual e possível flood control do Telegram | Atraso curto/aleatório por bot (Should, §4); só responder quando chamado, nunca "modo automático" nesta v1 | — |
| **Política padrão de bots do Telegram** (`telegram.org/privacy-tpa`) se aplica por padrão a todo bot de terceiros: §6.2 proíbe compartilhar dado de usuário entre os **próprios bots do desenvolvedor** sem autorização explícita; §7.3 obriga a responder pedido de cópia/exclusão em 30 dias | Enquanto o único usuário do grupo for o Fernando, não há dado de terceiro e a cláusula é inócua. Se alguém entrar: o histórico compartilhado (H4) vira bloqueante e é preciso política própria + filtro por `user_id` | novo, 2026-08-28 |
| Vazamento de um dos 6 tokens novos no `.env`/commit | Mesma disciplina de hoje (.env fora do git); `stella-release` já varre por padrão de token no `git grep` | — |
| ~~Setup manual no BotFather (7×) é tedioso e sujeito a erro humano~~ — **RESOLVIDO em 2026-08-28**: os 7 bots foram criados e adicionados ao grupo «Vegapunk» de uma vez, com privacy OFF só na Stella (conferido na lista de membros: 1 `has access`, 6 `has no access`) | Risco materializou-se em zero. Documentar mesmo assim no README para reprodutibilidade | — |

## 10. Custo e ordem de construção
- **Custo em tokens, medido em produção 2026-08-28:** roteador ~500–670 tokens por decisão. Resposta em personagem: **~25k tokens** sem ferramenta, **~55k** quando o Satélite busca no Punk Records (medido: 55.191 e 54.057). Tetos: 20 decisões/min, **6 respostas/min e 60/h** → pior caso absoluto ≈ **US$ 1,10 por hora** de abuso contínuo. Com o modo triagem ligado, mensagem sem nome deixou de custar zero e passa a custar a decisão.
- **Custo em tempo:** ~3 fins de semana de Atlas (Must) — York: *"coxinha em tokens; o custo real é o seu tempo cadastrando 7 bots no BotFather, não é Mother Flame"*. Acima de 2 fins de semana → **dividir em 2 stories**:
  - **Story 1** (1 fim de semana, testável em 1 dia): provar o conceito com **2 bots** (Stella + Lilith) no mesmo grupo — Stella como bot leitor, Lilith send-only; cascata das 5 camadas com o roteador; trava anti-loop; janela de 10 min. Se isso não vazar custo nem loopar em uma tarde de uso real, segue para a Story 2.
  - **Story 2** (~2 fins de semana): escalar de 2 para os 7 Satélites, histórico compartilhado do grupo (H4), atraso por bot, `/custo` agregado (somando as chamadas do roteador à parte, para York medir o overhead real).
- Ordem: Story 1 primeiro — é o bloco que testa a hipótese mais arriscada (loop/custo) com o menor investimento.

## Fontes do Punk Records
Nenhum item do vault se aplica diretamente (é decisão de arquitetura do próprio Vegapunk, não conteúdo capturado).

---
Chame Lilith: `*attack` os riscos marcados acima (loop entre bots e privacy mode) antes de aprovar o escopo.
Chame Stella: `*story` para escrever a Story 1 — as decisões de §0 destravam.
Chame Atlas: `*build` a Story 1 (2 bots, prova de conceito) depois da story escrita.
