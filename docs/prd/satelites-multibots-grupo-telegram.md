# PRD — Satélites como bots separados num grupo do Telegram

> Projeto: vegapunk · Autor: Edison (Punk-03) com Fernando · Data: 2026-08-27 · Status: rascunho
> Origem: pedido do Fernando em 2026-08-27 (chat com Stella no Telegram, 21:30), registrado em `squads/vegapunk/memory/stella.md`

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
| **Must** | Cada bot responde quando @mencionado (`@lilith_vegapunk_bot`) OU quando o próprio nome aparece em texto livre ("Lilith, ...") | 0,5 |
| **Must** | Trava anti-loop: nenhum bot processa mensagem cujo autor é outro bot (`from_user.is_bot`) | 0,25 |
| **Must** | Filtro local (regex, sem LLM) decide se a mensagem é "para mim" antes de qualquer chamada ao OpenRouter | 0,25 |
| **Must** | `TELEGRAM_ALLOWED_CHAT_IDS` continua valendo — grupo só responde ao(s) chat_id autorizado(s) | — (já existe) |
| **Must** | Histórico do grupo é compartilhado entre os 7 (cada um lê o que os outros disseram, não só o que o humano escreveu) | 0,5 |
| **Should** | Atraso curto e aleatório por bot antes de responder (evita rajada simultânea e flood control do Telegram) | 0,25 |
| **Should** | `/custo` funciona em qualquer um dos 7 e soma o grupo inteiro | 0,25 |
| **Could** | Satélite pode citar outro na resposta ("chama a Lilith") sem disparar a Lilith sozinho — só sugere | 0,25 |
| **Won't** (fora, de propósito) | Um Satélite acionar outro automaticamente sem o Fernando pedir (o "conselho ao vivo") — maior risco de loop e custo; vira PRD v2 depois que a v1 rodar estável | — |
| **Won't** | Substituir o bot único de DM — ele continua exatamente como está; o grupo é aditivo | — |

_Total Must: ~2,5 fins de semana — não cabe em ≤ 2; **dividir em 2 stories** (ver §10)._

## 5. Histórias de usuário e critérios de aceite
**H1.** Como Fernando, quero @mencionar um Satélite no grupo para que só ele responda, com nome e ícone próprios.
- [ ] Mandar `@lilith_vegapunk_bot ataca isso` no grupo → só o bot da Lilith responde, com o avatar/nome dela
- [ ] Os outros 6 bots não respondem nem geram log de chamada ao modelo

**H2.** Como Fernando, quero escrever o nome de um Satélite em texto livre ("Lilith, o que acha?") e ele responder, mesmo sem @.
- [ ] Mensagem contendo "lilith" (case-insensitive, como palavra) aciona o bot da Lilith
- [ ] Mensagem sem nenhum nome de Satélite não aciona ninguém

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
- `bot.py::build_app` hoje assume 1 `Application`; passa a rodar N `Application`s (uma por token) no mesmo processo `asyncio`, todas lendo/escrevendo no mesmo SQLite
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
| Privacy mode mal configurado em algum dos 7 (bot lê tudo e chama LLM à toa) | Filtro local (regex) roda antes do LLM, independente do privacy mode; checklist de setup no README | ✓ |
| 7 bots respondendo quase juntos = bagunça visual e possível flood control do Telegram | Atraso curto/aleatório por bot (Should, §4); só responder quando chamado, nunca "modo automático" nesta v1 | — |
| Vazamento de um dos 6 tokens novos no `.env`/commit | Mesma disciplina de hoje (.env fora do git); `stella-release` já varre por padrão de token no `git grep` | — |
| Setup manual no BotFather (7×) é tedioso e sujeito a erro humano (esquecer de desligar privacy mode) | Documentar passo a passo no README/HANDOFF; testar 2 bots primeiro (ver §10) antes de fazer os 7 | — |

## 10. Custo e ordem de construção
- **Custo:** ~2,5 fins de semana de Atlas (Must) — York: *"coxinha em tokens; o custo real é o seu tempo cadastrando 7 bots no BotFather, não é Mother Flame"*. Acima de 2 fins de semana → **dividir em 2 stories**:
  - **Story 1** (1 fim de semana, testável em 1 dia): provar o conceito com **2 bots** (Stella + Lilith) no mesmo grupo — trigger por nome/@menção, trava anti-loop, filtro local antes do LLM. Se isso não vazar custo nem loopar em uma tarde de uso real, segue para a Story 2.
  - **Story 2** (~1,5 fim de semana): escalar de 2 para os 7 Satélites, histórico compartilhado do grupo (H4), atraso por bot, `/custo` agregado.
- Ordem: Story 1 primeiro — é o bloco que testa a hipótese mais arriscada (loop/custo) com o menor investimento.

## Fontes do Punk Records
Nenhum item do vault se aplica diretamente (é decisão de arquitetura do próprio Vegapunk, não conteúdo capturado).

---
Chame Lilith: `*attack` os riscos marcados acima (loop entre bots e privacy mode) antes de aprovar o escopo.
Chame Atlas: `*build` a Story 1 (2 bots, prova de conceito) depois que o Fernando aprovar este PRD.
