# HANDOFF — Vegapunk (atualizado em 2026-08-28, sessão 5 — v1.7.0 `811710f` + Story 1c **rodando em produção, não commitada**)

## TL;DR — o que existe hoje

Vegapunk é **duas coisas** que compartilham uma fonte da verdade:

1. **Fabriophase (bot Telegram)** — captura links (YouTube/TikTok/Instagram) → extrai → resume via OpenRouter → guarda no SQLite → projeta em `punk_records/` (o Punk Records, versionado) → commit automático. **E agora conversa**: os 7 Satélites respondem no Telegram em personagem (`/stella`, `/shaka`, …).
2. **Labophase (Claude Code)** — os 7 Satélites como skills (`/vegapunk`, `/vegapunk:lilith`, …), cada um com personalidade completa **e** funções absorvidas do FURY (dev, qa, smith, pm, po, mifune…), autossuficientes em `squads/vegapunk/`.

Fonte da verdade de cada Satélite: `.claude/commands/vegapunk/agents/<id>.md`. **Tudo o mais é cópia** gerada por `scripts/sync_agents.sh` (global `~/.claude/commands`, FURY, plugin, `vegapunk.md`).

Estado: container `vegapunk-vegapunk-1` rodando com o código de hoje; **130/130 testes verdes**; GitHub `fernand-nan-ia/Vegapunk` em `811710f` (tag **v1.7.0**); FURY em `ab4ce12`.

⚠️ **A working tree NÃO está limpa, e o que está nela JÁ RODA EM PRODUÇÃO.** A Story 1c + o modo triagem estão no container e funcionando no grupo «Vegapunk» — mas não commitados: o gate do Shaka foi **CONCERNS**, e depois dele o Fernando pediu o modo triagem, que desfez a propriedade de custo em que aquele gate se apoiava. **`*verify` e `*gate` precisam ser refeitos antes do release.** Cerca de 18 arquivos parados (`src/vegapunk/{router,chat,bot,config}.py`, `tests/{test_cascade,test_group_glue,test_router,test_speakers,test_bot_guard}.py`, `.env.example`, PRD, stories, diários). **137/137 testes verdes.**

Sessão 3 já está no GitHub (`fe63b19` / FURY `6ee82c0`). Para as próximas, o padrão é o mesmo — sempre os DOIS repos:

**Repo Vegapunk:**
```bash
git add -A
git commit -m "feat: Satélites com personalidade + funções do FURY (autossuficientes) + conversa no Telegram"
git push
```
Inclui: 7 agentes + `vegapunk.md` + plugin (personalidade e absorção), `src/vegapunk/{chat,satellites}.py`, `bot.py`, `pyproject.toml` (+pyyaml), `tests/{test_satellites.py,satellites_baseline.json}`, `scripts/sync_agents.sh`, `squads/vegapunk/{tasks,checklists,templates,memory,avaliacao-imoveis}/`, este HANDOFF. `.env`, `data/`, `tmp/`, `whisper-cache/` continuam no `.gitignore` (conferido).

**Repo FURY** (`/home/crazu/projetos/FURY`, 3 entradas novas: `.claude/commands/vegapunk.md`, `.claude/commands/vegapunk/`, `squads/vegapunk/`): é o espelho do squad, exigido pela regra global. Commitar lá também:
```bash
git -C /home/crazu/projetos/FURY add -A && git -C /home/crazu/projetos/FURY commit -m "squad vegapunk: 7 Satélites (personalidade + funções absorvidas) e squads/vegapunk autossuficiente" && git -C /home/crazu/projetos/FURY push
```

Depois de commitar, o bot continua fazendo commits `kb:` automáticos — normal.

## Primeira coisa a fazer na próxima sessão

**O grupo multi-bot está a duas linhas de `.env` de funcionar.** Todo o código das Stories 1a, 1b e 1c existe, com 130 testes. O que falta é uma decisão do Fernando e um `.env`.

~~1 e 2 (aceitar ressalvas, editar `.env`)~~ — **FEITOS em 2026-08-28 à noite.** O `.env` está completo (7 tokens, id do grupo, `TELEGRAM_ALLOWED_USER_IDS`, `VEGAPUNK_GROUP_ENABLED=true`), o container foi recriado e **o grupo funciona** (ver Sessão 5e).

1. **Decidir o teto de respostas por hora.** A York recomenda baixar de **60 para 25** (`router.MAX_REPLIES_PER_MIN` fica em 6, que ela aprovou). Motivo: 60/h autoriza US$ 23,76 num dia de descontrole — quatro dias de uso real a cada hora. É uma linha de código.
2. **Refazer `*verify` (Lilith) e `*gate` (Shaka) sobre a Story 1c + triagem.** Os dois foram dados ANTES do modo triagem, que desfez a propriedade de custo em que se apoiavam. Sem isso o Stella não faz release — e há ~18 arquivos rodando em produção sem commit.
3. **Depois: `*release`.** Working tree pronta, 137 testes verdes. Sugestão de versão: **v1.8.0** (cascata do grupo + triagem).
4. **Falta um teste de aceite**: a sétima mensagem do roteiro — esperar 11 minutos e escrever `e aí?` sem nome. Esperado: ninguém responde (janela expirada). Com a triagem ligada, o roteador é consultado e deve devolver lista vazia por ser frase sem pergunta — **este caso mudou de natureza e ainda não foi observado**.
3. Se o site do cliente for vender online: `*capture` o Decreto nº 7.962/2013 (regulamenta e-commerce sob o CDC) — lacuna marcada pelo Shaka no item do Código de Defesa do Consumidor.
4. Investigar os US$ 8,58 gastos na chave do OpenRouter que não batem com o que o bot registra (achado em 2026-08-27 ao rodar `*cost`; ~13 centavos são do bot, o resto é gasto não explicado — checar se a chave está em outro projeto).

## Sessão 4 (2026-08-27) — cânone da wiki incorporado aos 7 Satélites

Cada agente em `.claude/commands/vegapunk/agents/*.md` foi enriquecido (só adição) com o cânone das páginas `onepiece.fandom.com/wiki/Vegapunk[/Satélite]`: aparência real, habilidades, eventos do arco Egghead (traição da York, morte do Shaka, Pythagoras/Atlas/Shaka reconvergindo no corpo do Edison, Lilith fugindo com os Chapéus de Palha, transmissão final do Stella), relações canônicas, falas traduzidas. Seções tocadas: `persona_profile.canon/signature_phrases/vocabulary`, `mind`, `relationships`, `quirks`, `examples` (+2–4 diálogos cada). Duas correções factuais: Lilith (macacão rosa + capacete vermelho, não vestido laranja) e York (olhos água-marinha). 41/41 testes verdes; prompt do Telegram cresceu para ~20–23k chars por Satélite (era ~13k) → custo por mensagem sobe proporcionalmente.

Também incorporados dois vídeos (Uselessinho `Pveu6gs7-LM` e o discurso completo do Vegapunk `_sAI-ganFAw`, transcritos via `extract.extract` no venv): a voz do discurso em Stella ("Alô, alô, teste, teste", "só a verdade confirmada", "dois pecados", "acredito na ciência"), a regra "Satélites sincronizam 1×/dia e não se encontram à toa" (Stella `council` raro), "não rotular bom/mau antes de compreender" (Shaka), lacuna marcada > lacuna preenchida (Pythagoras), Karakuri sem financiamento (York). Container estava parado (exit 127, sem log de erro — provável reinício do Docker/WSL) e foi subido com `docker compose up -d`.

**Pasta renomeada: `knowledge/` → `punk_records/`** (tema; underscore em vez de espaço para não quebrar shell/Docker/links). Trocado em `config.py` (default), `.env`/`.env.example` (`VEGAPUNK_VAULT_DIR=punk_records`), teste, 7 agentes + `vegapunk.md`, plugin, `squads/vegapunk/`, README. Links do INDEX são relativos — não mudam. Container recriado com `--force-recreate`. A cópia global em `~/.claude/commands` ainda diz `knowledge/` até rodar o sync.

**Release v1.1.0 feita pelo Stella (teste do `*release`, 2026-08-27):** Lilith achou que o SQLite guardava `vault_path` absoluto com `/app/knowledge/` (21 linhas) → migrado (backup `data/vegapunk.db.bak-rename-20260827`) + `vault._rel_to_vault` tolerante + teste; 42/42; sync rodado; Vegapunk `40fec7d` tag `v1.1.0` pushado; FURY pushado. Sem pendências.

## Sessão 4b (2026-08-27) — artigos + voz dos Satélites no bot — **v1.2.0 `023fa49` pushado**

- **Artigos**: `normalize.normalize_article` (qualquer http(s) não-vídeo → `article`, id = sha1 da URL sem utm/fbclid/ref/si), `extract.extract_article` (trafilatura, `output_format="markdown"`, `with_metadata=True`), `vault.render` adiciona `## Texto integral` (títulos rebaixados via `_demote_headings`). `other` sobrou só para canal/playlist de YouTube/TikTok/IG. Testados de verdade com 2 artigos do Akita (24k e 19k chars) — itens em `punk_records/article/`, commits `kb:` feitos pelo bot.
- **Voz**: `enrich.Enrichment` ganhou `satellite` (enum) e `satellite_take` (2–3 frases); `VOICE_RULES` no system prompt decide quem apresenta. `pipeline.format_summary` abre com o ícone do Satélite e fecha com o take; `voices.py` tem as falas de captura (sorteio), duplicata, ERR-002/008/extração/enriquecimento/crash. Itens antigos sem `satellite` continuam renderizando (default stella).
- **Ajustes do Fernando (mesma sessão)**: (1) fim do "…" — `bot.notify` envia em `chunks`, teclado na última parte; (2) quem anuncia apresenta — `voices.pick()` no `on_message`, coluna `satellite` (migração em `db._migrate`), `enrich` recebe "SATÉLITE JÁ ESCOLHIDO"; (3) cabeçalho `voices.speaker()` = `ícone Nome · Punk-NN`; (4) chat compacto (`brief`, 3 pontos-chave, sem tópicos/ferramentas) e vault completo (`summary` 4-10 frases). Itens antigos sem `brief` usam `summary`.
- Imagem **rebuildada** (trafilatura) e container rodando. 50/50 testes.
- Release feita pelo Stella após "push" do Fernando (gate PASS, 51/51). Duplicata/falhas agora falam na voz do dono do lote.
- Ideia decorrente: "Notas manuais" e `/reprocess` continuam valendo para artigo com paywall (cai em ERR-004 → `_pending/`).

## Sessão 4c (2026-08-27) — Satélites com ferramentas e comandos no Telegram — **v1.3.0 `9be20c5` pushado**

- `src/vegapunk/tools.py`: 5 ferramentas (busca, leitura de item, status/custo, git log do vault, diário). Só leitura + diário; nada executa código.
- `chat.py`: `parse_command` (`*cmd args`); comando fora de `TELEGRAM_COMMANDS` ou `*help` → resposta pronta (zero tokens); senão o procedimento do `.md` entra como system message e roda o loop de tool-use (3 rodadas conversa / 8 comando). Tokens das rodadas somados em `chat_messages`.
- `satellites.py`: `search_index` (título/tags ×3 + corpo ×1, radical), `TELEGRAM_COMMANDS`, `parse_command`, `command_info`, `procedure`.
- Custo: um comando com 2–3 rodadas ≈ 20–30k tokens de entrada (persona ~7k + índice + itens lidos) ≈ US$ 0,01–0,02. York avisa.
- Testes: 58/58 (`tests/test_tools.py` novo; loop mockado em `test_satellites.py`).
- Ideias decorrentes: cache de prompt (persona é idêntica em toda chamada); `*council` no Telegram (6 chamadas — caro, ficou fora); resumo do histórico.

## Sessão 4d (2026-08-27) — documentos (PDF/DOCX/XLSX) no Telegram e no Claude Code — **v1.4.0 `e9b1e5b`**

- Telegram: `bot.on_document` (filtro `Document.ALL`, registrado ANTES do de texto) baixa para `tmp/documents/<file_unique_id>.<ext>`, cria item `file://…` com Satélite dono; `normalize_document` = sha1 do conteúdo; `extract_document` por extensão; após extração o arquivo temporário é apagado (texto já está no banco). Falha de extração deixa o arquivo em `tmp/documents/` para reprocess manual.
- Vault: frontmatter `canonical_url` = nome do arquivo (o caminho temporário não sobrevive); corpo mostra `📎 nome (enviado pelo Telegram)`; `## Texto integral` também para `document`.
- Claude Code: `.venv` tem pypdf/python-docx/openpyxl — para ler .docx/.xlsx aqui, converter com `extract.extract_document(Path)` e ler o texto; PDF eu leio direto.
- Sem OCR: PDF escaneado → ERR-004 → `_pending/`. Ideia: OCR por visão (`enrich.read_slides` com páginas renderizadas) sob gatilho manual.
- Testes: 66 (`tests/test_document.py`).
- **Armadilha nova**: planalto.gov.br fecha a conexão para User-Agent não-navegador (`fetch_url` do trafilatura falha). `extract.fetch_html` usa cabeçalhos de Chrome primeiro. Item da LGPD (`f831b2bb`) ficou 5 tentativas em ERR-003 e foi retomado pelo `resume_unfinished` após o restart com a correção — funcionou (112k chars).

## Sessão 4e (2026-08-27) — Punk Records por tema — **v1.4.0 `e9b1e5b`**

- Pedido do Fernando: organização visual por assunto (LGPD ≠ IA ≠ jogos) e páginas por tema para outros projetos não lerem todos os .md.
- `src/vegapunk/themes.py`: 11 temas fixos (slug → ícone, nome, descrição, gatilhos). `Enrichment.theme` (enum) + regra no prompt; `theme:` no frontmatter; `vault.write_index` agrupa por tema e chama `themes.write_theme_pages` → `punk_records/temas/<slug>.md` (remove página de tema vazio). `satellites.search_index` ignora `temas/`.
- `scripts/backfill_themes.py`: classifica os itens sem `theme` em UMA chamada (json_object) e regenera todo o vault. Rodado no container em 2026-08-27.
- Pastas por origem não mudaram (o bot gera; mover quebraria `vault_path`).
- Para adicionar tema: editar `THEMES` + `Theme` (Literal em enrich.py) e rodar o backfill.

## Sessão 4f (2026-08-27) — `*capture`: alimentar o Punk Records pelo Claude Code sem OpenRouter — **v1.5.0 `b8a560b`**

- Motivo (Fernando): minimizar custo do OpenRouter — a sessão do Claude Code faz o resumo. `scripts/capture.py extract|enrich|auto|pending`; `stella.md` ganhou `capture` (+ task). `enrich` usa `db.transition_to(..., "enriched", "claude_code", …, model_used="claude-code")` e depois `Pipeline.step_persist` (vault, índice, temas, commit, Telegram). York: `punk_records_status` soma tokens só de `item_events`, então itens claude-code entram como custo zero — correto.
- Sync rodado; FURY commitado e pushado junto. Compose: `stop_grace_period: 30s` (fim dos exit 137 em restart).

## Sessão 4g (2026-08-27) — lote de captura sem OpenRouter — capture.py com `--text` — **v1.5.1 `982f0d4`**

- Lote da noite de 2026-08-27 pelo `*capture` (custo OpenRouter zero, resumos escritos pela sessão): Hostinger 8, Shopify 2, Registro.br 6, Claude Code memória 1, SerpApi 4, Resend 27, Sentry 1, Cloudflare (Workers/Analytics/R2) 11, UptimeRobot 2, reCAPTCHA 2, GitHub 1, Nominatim 2, MapTiler 2, Geoapify 2 = **71 itens**. Páginas só de navegação/vitrine (menus em JS) foram descartadas do banco em vez de poluir o vault (SerpApi 3, Cloudflare 2, Sentry guides, R2 buckets, reCAPTCHA home/samples, docs.github home).
- **Armadilha nova — SPA (registro.br)**: HTML de 4 KB, conteúdo em chunks Vue (`/assets/<Rota>-<hash>.js`) e API com XSRF de sessão (preços não obtidos). Solução usada: baixar os chunks, extrair strings de texto (script ad hoc no scratchpad) e alimentar com `capture.py extract <url> --text arquivo.txt`. Páginas de preço da Hostinger/Shopify também renderizam tabelas por JS: preços registrados só onde o texto trazia; `confidence: media` quando faltou.
- `docker compose exec -T` dentro de `while read` consome o stdin do laço → usar `</dev/null` (ou `for`).
- `_pending/` restante: carrinho da Hostinger (checkout pessoal, sem texto) e um Instagram antigo.

## Sessão 4h (2026-08-27) — planejamento: Satélites como bots separados num grupo do Telegram — **v1.5.2 `fb1bacf`**

- **Origem**: pedido do Fernando pelo Telegram (21:30, "criar para cada satélite um bot e fazer um grupo com todos"), registrado no diário do Stella como próximo passo; retomado aqui no Claude Code a pedido dele.
- **PRD escrito**: `docs/prd/satelites-multibots-grupo-telegram.md` (Edison, status rascunho). Ideia: 7 bots reais no BotFather (um token por Satélite) no mesmo grupo, cada um responde por `@menção` ou pelo nome em texto livre; trava anti-loop (nunca reagir a mensagem de outro bot, `is_bot`); filtro local (regex) decide "é pra mim?" antes de qualquer chamada ao OpenRouter; histórico do grupo compartilhado entre os 7 (para "Shaka, o que acha do que a Lilith falou?" fazer sentido). **Won't da v1**: um Satélite acionar outro sozinho sem o Fernando pedir — fica para v2, é o item de maior risco de custo/loop. Custo estimado (§10 do PRD): ~2,5 fins de semana de Atlas, dividido em Story 1 (1 fim de semana — prova de conceito com 2 bots: Stella + Lilith) e Story 2 (~1,5 — escalar para os 7 + histórico compartilhado).
- **Lilith atacou o PRD** (registrado no diário dela) e achou dois furos reais antes de aprovar escopo:
  1. Responder por nome em texto livre (sem `@`) **exige privacy mode OFF nos 7 bots** — não é detalhe de configuração, é os 7 lendo toda mensagem do grupo; o PRD não deixava isso explícito no §7.
  2. Nome como palavra solta vai casar com falso positivo real (ex.: "fui pra Nova York" aciona o bot da York); e o comportamento com **dois nomes na mesma mensagem** ("Shaka e Lilith, o que acham?") não está definido.
- **Três decisões do Fernando ainda pendentes** (bloqueiam a Story 1 — ver "Primeira coisa a fazer"): (a) aceitar privacy mode OFF nos 7 bots; (b) York disparar só por `@menção`, nunca por nome solto; (c) mensagem com dois nomes aciona os dois ou só o primeiro.
- **Nenhuma story escrita ainda, nenhum código tocado** — o PRD está em `docs/prd/`, sem commit até este checkpoint.
- **Também nesta sessão** (fora do tema multi-bot, mas na mesma conversa): pedido do Fernando para o `*capture` não avisar mais o Telegram por padrão quando o pedido é feito aqui no Claude Code. `scripts/capture.py`: `enrich`/`auto` agora são **silenciosos por padrão**; a flag virou `--telegram` (opt-in), substituindo `--quiet` (opt-out antigo). `stella-capture.md` e `stella.md` atualizados; sync rodado. Preferência gravada em memória de feedback (`capture-silencioso-por-padrao.md`).
- Também capturado nesta sessão: [Resolução CD/ANPD nº 2/2022](punk_records/article/2026-08-28_resolucao-cd-anpd-no-2-2022-regulamento-da-lgpd-para-agentes_ee0ac20cec91.md) (pelo bot, via Telegram) e o [Código de Defesa do Consumidor](punk_records/article/2026-08-28_codigo-de-defesa-do-consumidor-lei-no-8-078-1990-texto-integ_6bb7420aee5e.md) na íntegra (pelo `*capture`, dono Shaka) — lacuna marcada: falta o Decreto 7.962/2013 (e-commerce) se o site do cliente vender online.

## Sessão 5 (2026-08-28) — multi-bot: decisões, roteador e porteiro — **v1.6.0 `74c7528` pushado**

Container estava parado de novo (Docker Desktop sem integração WSL no início da sessão); subido com `docker compose up -d`.

As três perguntas que travavam a Story 1 foram respondidas pelo Fernando, e a resposta dele à segunda mudou o desenho do PRD — está tudo em `docs/prd/satelites-multibots-grupo-telegram.md` §0 e §4.1:

- **(a) Privacy mode OFF: sim, mas só num bot.** Fernando confirmou o OFF; ao desenhar o roteador ficou claro que apenas **um** bot precisa *ler* o grupo. Privacy mode controla o que o bot **recebe**, não o que ele **envia** — logo os outros 6 ficam privacy ON e **send-only** (sem handler de mensagem), publicando com nome e ícone próprios. Sete participantes visíveis, uma superfície de leitura.
- **(b) e (c) resolvidas por contexto, não por regra.** Fernando perguntou se o bot não podia ler o contexto e entender se está sendo chamado. Pode — a questão era onde essa inteligência mora: 7 bots perguntando ao modelo = 7 chamadas por mensagem. A saída é **um roteador central** (os 7 já rodam no mesmo processo): 1 chamada barata, **sem persona e sem `INDEX.md`**, com a mensagem + 3 últimas linhas, devolvendo `{"satelites": [...], "confianca": ...}`. Resolve "fui pra Nova York" (lista vazia) e "Shaka e Lilith" (os dois) sem exceção escrita à mão para a York.
- **(d) Janela de continuidade: 10 minutos** (Fernando ajustou de 5 para 10). Mensagem sem nome dentro da janela → responde quem falou por último; fora dela, silêncio.

**A cascata (§4.1)** substitui o Must antigo "filtro local (regex, sem LLM)": camadas 0–2 grátis (is_bot/chat autorizado → `@menção` direta sem roteador → sem nome e fora da janela = ninguém), camada 3 roteador (~US$ 0,0002), camada 4 resposta em personagem (~US$ 0,002–0,005). O regex sobrevive só como corte de ruído. **Roteador falha fechada** (erro/timeout/`confianca: baixa` → ninguém responde), schema estrito + Pydantic como no `enrich`, e log de toda decisão para auditar falso positivo/negativo na primeira semana; `@menção` é o caminho determinístico de escape que não passa por ele.

Custo do Must subiu de ~2,5 para ~3 fins de semana (Story 2 virou ~2). H2 ganhou casos de aceite concretos (Nova York, dois nomes, dois nomes com um sendo objeto da frase) e nasceu H2b (janela).

Punk Records consultado: **nenhum registro** sobre bots de Telegram, roteamento ou detecção de intenção — decisão tomada só com raciocínio de arquitetura.

## Sessão 5b (2026-08-28) — Story 1a entregue: roteador + porteiro do dinheiro

**Os 7 bots existem.** O Fernando criou todos no BotFather e pôs no grupo «Vegapunk»: Stella com privacy OFF (`has access to messages`), os outros 6 com privacy ON — conferido na lista de membros, que é como o FAQ do Telegram diz que se audita isso. O setup manual previsto para as Stories 1b **e** 2 está feito; falta só código. Os 7 tokens e o id do grupo já estão no `.env`.

**`src/vegapunk/router.py` (novo)** — camadas 2 e 3 da cascata. `mentions()` é grátis, acha nome como palavra inteira, entende apelido ("Dr. Vegapunk" → stella) e **ignora nome dentro de link** (`site.com/atlas-map` não paga roteador). `route()` gasta 1 chamada **sem persona e sem `INDEX.md`** — é isso que a mantém ~30× mais barata que uma resposta em personagem. Falha **sempre fechada**: erro, timeout, JSON inválido, id desconhecido ou `confidence: baixa` → ninguém responde. Teto de **3 Satélites por mensagem** (mesmo sob injeção de prompt: há teste com a frase). Cliente próprio, `timeout=15` com 1 repique — o do `enrich` é 180 s × 3, feito para transcrições, e daria 9 min de silêncio no grupo.

**`bot.is_allowed()` (novo)** — o porteiro do dinheiro, 4 portas. Corrige a **única falha aberta do sistema**: `TELEGRAM_ALLOWED_CHAT_IDS` vazio fazia o bot aceitar QUALQUER chat do Telegram (bots são públicos; qualquer um que descubra o @username abre DM e gasta a chave). Agora recusa. Novos: `TELEGRAM_ALLOWED_USER_IDS` (só quem está na lista dispara chamada paga, mesmo dentro do grupo) e `VEGAPUNK_GROUP_ENABLED` (default **false** — o id do grupo pode ficar no `.env` sem risco). `/id` fica fora do porteiro de propósito: é o bootstrap.

**Ciclo completo rodou pela primeira vez de ponta a ponta**: Edison `prd` → Stella `story` → Atlas `develop` → Lilith `verify` → Shaka `gate` → Stella `release`. A Lilith achou **13 problemas em 3 passadas** (3 ALTOs: sem teto de custo, timeout de 9 min, contexto sem truncar) e só disse AGUENTOU na terceira. Shaka deu PASS com uma condição permanente: **o grupo só deve ser autorizado quando `TELEGRAM_ALLOWED_USER_IDS` estiver preenchido**.

**Punk Records: 112 → 125 itens.** Auditoria dos links que o Fernando mandou: os 3 do Telegram, as 7 páginas da wiki dos Satélites e os 2 vídeos da sessão 4 **nunca tinham sido guardados** — foram lidos por subagentes/scratchpad e o texto morreu junto. Recuperados. Regra nova do Fernando, gravada em memória: **link enviado no Claude Code vai para o Punk Records sem perguntar**, salvo pedido contrário. Dos 38 links de 27/08 conferidos um a um, 35 estavam guardados; os 3 ausentes são páginas SPA do SerpApi que devolvem 334 chars de rodapé idêntico (descarte correto).

**Correção do Fernando: o Stella é masculino.** 22 linhas em 9 arquivos. O `stella.md` sempre esteve certo; o erro estava nos documentos em volta.

**Próximo passo: Story 1b** (`squads/vegapunk/stories/`) — N Applications no mesmo processo, só a do Stella com handlers, trava `is_bot`, e as duas brechas do porteiro já viraram critério de aceite lá.

## Sessão 5c (2026-08-28) — Story 1b: os 7 Satélites como bots no grupo — **v1.7.0 `811710f`**

**`src/vegapunk/speakers.py` (novo).** Decisão de projeto do Atlas: a story previa uma `Application` por token; ele usou **`telegram.Bot` puro** para os seis que só publicam. Uma `Application` existe para RECEBER (Updater, fila, polling); quem só fala não recebe. Ganho: **um laço de polling em vez de sete**, e o critério "os outros não registram handler" virou **estrutural** — num `Bot` não existe `add_handler` (há teste disso).

**Trava anti-loop** — condição bloqueante do Shaka desde a análise de risco: `is_allowed(from_bot=True)` é a **porta 0** do porteiro, antes até da lista de chats. Sete bots num grupo, um respondendo ao outro, era o único caminho para custo verdadeiramente descontrolado.

**`config.bot_tokens`** por varredura do ambiente: `TELEGRAM_BOT_TOKEN` → stella, `TELEGRAM_BOT_TOKEN_<ID>` → `<id>`. Acrescentar um bot é uma linha no `.env`. **E o `bot_token` do `build_app` passou a sair do mesmo dicionário** — antes, `TELEGRAM_BOT_TOKEN_STELLA` derrubava o serviço no arranque **enquanto um comentário no código afirmava ser o caminho da renomeação da Story 2**. O Fernando tinha tentado exatamente isso pela manhã. Foi o ALTO do `*verify`.

**Quem fala.** `bot.responder()`: no grupo cada Satélite sai pelo próprio bot (nome e ícone dele); na DM, pelo bot de sempre — um bot não pode escrever para quem nunca abriu conversa com ele. Resposta longa sai toda pela **mesma boca** (se o primeiro pedaço cai para o leitor, o resto vai com ele); a queda larga o `reply_to_message_id` (se a mensagem original sumiu, ela É a causa); o laço de envio está protegido — resposta já paga não some em silêncio.

**O que a produção ensinou em três restarts.** Primeira subida com tokens reais: 5 de 6 bots vieram e o da Lilith caiu com `TimedOut`. A degradação funcionou ("ele falará pelo bot do stella"), mas expôs duas falhas: init **sequencial** custava ~17 s de polling parado, e **não havia segunda chance** — um piscar de rede aposentava o bot até o restart. Agora `asyncio.gather` + 1 repique: **1,6 s**, e há teste com o caso real. Terceira falha achada pela Lilith: o bot que falha no `get_me` era descartado sem `shutdown`, vazando o pool httpx (duas vezes, uma por tentativa).

**Verificação em produção, os dois lados:**
- `/lilith oi` no **grupo** → `grupo -5120920932 está no .env mas VEGAPUNK_GROUP_ENABLED=false: ignorando`. Silêncio por decisão, custo zero. Primeira prova de que o id do grupo pode ficar no `.env` sem risco.
- `/lilith oi` na **DM** → resposta em personagem, com `reply_to` e ícone (24.788 tokens de entrada — conversa com item do vault anexado). Única regressão possível da story, descartada por observação.

**Setup do Fernando:** os 7 bots criados no BotFather e no grupo «Vegapunk» (`-5120920932`); Stella com privacy OFF, os outros 6 ON; 7 tokens e o id do grupo no `.env`. Usernames: `@vegapunkkyorkbot`, `@vegapunkkedisonbot`, `@vegapunkkatlasbot`, `@vegapunkshakabot`, `@vegapunkkpythagorasbot`, `@vegapunkklilithbot`.

**Próximo passo: Story 1c** — ligar a cascata do §4.1 (camadas 0–2 grátis, roteador, resposta), janela de continuidade de 10 min, e só então `VEGAPUNK_GROUP_ENABLED=true` **com `TELEGRAM_ALLOWED_USER_IDS` preenchido** (condição permanente do Shaka). Herdadas do `*verify` da 1a: obrigar `mentions()` antes de `route()` e teto de chamadas por minuto.

## Sessão 5d (2026-08-28) — Story 1c: a cascata do grupo — **pronta, NÃO commitada (gate CONCERNS)**

**A cascata do PRD §4.1 existe e está testada.** `router.decide()` compõe as camadas 1 a 3 numa função só:

```
camada 1 · @menção explícita  → responde direto, SEM roteador (escape determinístico)
camada 2 · sem nome no texto E fora da janela → ninguém, custo zero
camada 3 · roteador decide (com teto de 20 decisões/min)
camada 4 · cada apontado responde pelo próprio bot (com teto de 6 respostas/min, 60/h)
```

**Por que `decide()` existe como função única:** era o achado 7 da Lilith na Story 1a. Enquanto compor as camadas fosse tarefa de quem chama, alguém pularia `mentions()` e pagaria o roteador em toda mensagem. Agora **não há caminho** até `route()` que não passe pelas duas peneiras grátis — e há um teste que lê o `bot.py` e falha se alguém escrever `router.route(` lá.

**Janela de continuidade de 10 min**: `Chat.active_age()` lê o `updated_at` do `chat_state` (que `wake()` já atualizava). Aos 9 min a conversa segue sem repetir o nome; aos 11, a mensagem sem nome **nem chega ao roteador**. A janela passa a seguir **quem foi chamado primeiro**, não quem falou por último.

**O ALTO do `*verify` da Lilith — o teto guardava a porta errada.** O Atlas tinha posto teto de 20/min no `route()`, que é a camada **barata** (~500 tokens). A camada cara custou **24.788 tokens medidos em produção** numa única resposta: 20 decisões autorizavam 60 respostas ≈ 1,5 milhão de tokens. O teto mudou para `router.pode_responder()`, chamado imediatamente antes de gastar, com dois horizontes (6/min segura a rajada, 60/h segura a tarde). **Pior caso absoluto ≈ US$ 0,50 por hora**; antes esse número não existia.

**Outros quatro achados corrigidos:** (1) `@menção` dependia do `get_me` ter respondido no arranque — e a Lilith **não respondeu** na primeira subida real; agora o padrão `@…<id>…bot` casa mesmo com o bot fora do ar, senão o grupo ignoraria o Fernando em silêncio. (2) O contexto do roteador ia sem dizer quem falou (`"Fernando: ..."` / `"Lilith: ..."` agora). (3) A costura decidir→responder não tinha teste: virou `bot.responder_no_grupo()`, fora do `build_app`, com 5 testes. (4) Estouro de teto avisa uma vez na voz da York, custo zero — grupo que cala sem explicação é pior que grupo caro.

**Gate do Shaka: CONCERNS**, com duas ressalvas numeradas (ver "Primeira coisa a fazer"). Não é FAIL: o código está correto e coberto. É que esta é **a única das três stories cujo comportamento nunca foi observado** — a 1a era inerte, a 1b foi confirmada com um `/lilith oi` na DM, e a cascata não pode rodar enquanto o grupo dorme.

**Estado do `.env` do Fernando hoje:** 7 tokens ✓, id do grupo ✓, `VEGAPUNK_GROUP_ENABLED=false` (grupo mudo), `TELEGRAM_ALLOWED_USER_IDS` **vazio** (a condição do Shaka que falta).

## Mapa do multi-bot — o que existe e onde

| Peça | Arquivo | Story |
|---|---|---|
| Porteiro do dinheiro (5 portas, falha fechada) | `bot.is_allowed()` | 1a + 1b |
| Roteador (mentions grátis + route pago) | `src/vegapunk/router.py` | 1a |
| Cascata completa numa função | `router.decide()` | 1c |
| Tetos de custo | `router.pode_responder()` (cara) e `_dentro_do_teto()` (barata) | 1c |
| Os 6 bots que só falam | `src/vegapunk/speakers.py` | 1b |
| Quem fala por quem | `bot.responder()` / `speakers.say_all()` | 1b |
| Costura do grupo | `bot.responder_no_grupo()` | 1c |
| Janela de 10 min | `chat.active_age()` + `router.WINDOW_SECONDS` | 1c |
| Responder como um Satélite escolhido | `chat.reply(..., as_sat=)` | 1c |

Stories em `squads/vegapunk/stories/`: 1a e 1b **feitas**; 1c **feita, aguardando release**.

## Variáveis novas do `.env` (todas opcionais, todas com default seguro)

| Variável | Default | Para que serve |
|---|---|---|
| `TELEGRAM_BOT_TOKEN_<ID>` | — | um por Satélite (`_SHAKA`, `_LILITH`…). Ausente = aquele bot fala pela boca do Stella |
| `TELEGRAM_ALLOWED_USER_IDS` | vazio | só estes ids disparam chamada paga, mesmo dentro de chat autorizado |
| `VEGAPUNK_GROUP_ENABLED` | `false` | **o grupo só acorda quando isto for `true`** |
| `VEGAPUNK_ROUTER_MODEL` | vazio | modelo do roteador; vazio usa `VEGAPUNK_MODEL` |

## Sessão 5e (2026-08-28, noite) — o grupo multi-bot FUNCIONANDO em produção

**O que o Fernando pediu ontem às 21:30 no Telegram existe e roda.** No grupo «Vegapunk» (`-5120920932`), com os 7 bots dentro:

| Ele escreve | Acontece | Custo |
|---|---|---|
| `bom dia` | ninguém responde | zero (antes da triagem) |
| `Lilith, o que acha disso?` | só a Lilith, **pelo bot dela** (`@vegapunkklilithbot`) | ~US$ 0,017 |
| `e isso aí, funciona?` (< 10 min) | a Lilith de novo, sem repetir o nome — **janela funcionou** | idem |
| `Shaka e Lilith, o que acham?` | os dois, na ordem, dois bots diferentes | 2× |
| `@vegapunkkyorkbot quanto custou?` | só a York, sem passar pelo roteador | 1× |
| `qual é o melhor de vocês para LGPD?` | **triagem** escolheu o Shaka, que disse "Veredito: sou eu" e citou 4 leis do vault | 1× |

Confirmado por print e por log em todos os casos.

### Três bugs que SÓ a produção achou (nenhum teste pegaria)

1. **`Message to be replied not found`** — os seis bots rodam com privacy mode ON, nunca "viram" a mensagem original, e o Telegram recusa a citação. A queda para o leitor mascarava isso em "todo mundo responde como Stella". Correção: só o leitor cita; os outros respondem sem citação, e há uma segunda tentativa **mantendo a identidade** antes de cair para o Stella.
2. **`Chat not found` só da Lilith** — havia **dois bots Lilith**: `@Vegapunklilith_bot` no grupo e `@vegapunkklilithbot` no `.env`. Diagnosticado com `get_chat_member` usando o id que é o prefixo do token. O Fernando trocou pelo certo. **Técnica reaproveitável**: para saber se um bot está mesmo num chat, `leitor.get_chat_member(chat_id, int(token.split(':')[0]))`.
3. **`JSONDecodeError: Unterminated string`** — `max_tokens=200` cortava o JSON do roteador no meio do `reason`. Falhou fechado (correto), mas o silêncio foi por defeito. Correção: `max_tokens=400` + `reason` com `max_length=120` no schema e no prompt.

### Modo triagem (pedido do Fernando, PRD §0 e)

Sem nome na mensagem, o roteador escolhe o dono **pelo assunto** — pode ser o próprio Stella. **Desfaz a propriedade "grupo calado é grátis"** que a Lilith aprovou e o Shaka carimbou: mensagem sem nome passa a custar a decisão (~US$ 0,0004). O silêncio deixou de ser estrutural e virou decisão do modelo (recado, `ok`, `kkk` → lista vazia). Reversível por `VEGAPUNK_GROUP_TRIAGE=false`, com teste dos dois modos.

**Duas correções do `*verify` da Lilith sobre a triagem:**
- **Teto de 1 em triagem** (`MAX_TRIAGE`): o prompt dizia "UM só" e a produção devolveu **três** respostas de ~55k tokens. Instrução sem enforcement é sugestão.
- **`ESPECIALIDADES` deixou de ser fonte paralela**: o roteador agora lê `persona.focus` do `.md` de cada Satélite. A cópia fixa **já tinha divergido** (o York do roteador falava de preço; o do arquivo, de healthcheck). Teste compara os dois e falha se voltarem a discordar.

## Custo: extrato real e projeção (York, 2026-08-28)

Preço em `tools.py`: `PRICE_IN = 0,375/M`, `PRICE_OUT = 1,875/M` (gemini-3.7-flash).

```
conversas       1.005.100 in +  15.272 out = US$ 0,406
enriquecimento    225.164 in +  69.569 out = US$ 0,215
TOTAL do bot desde que existe               US$ 0,620   (R$ 3,22)
só o grupo, 11 respostas no dia             US$ 0,176
```

| Unidade | Custo |
|---|---|
| 1 decisão do roteador (~650 tokens) | **US$ 0,0004** |
| 1 resposta em personagem (~42k tokens, média medida no grupo) | **US$ 0,0165** |
| 1 resposta COM busca no Punk Records | ~55k tokens (pior caso) |

**O roteador é 40× mais barato que a resposta** — é isso que justifica a cascata inteira.

**Projeção mensal:** leve (5 respostas/dia) **US$ 2,60** · médio (15/dia) **US$ 7,80** · pesado (40/dia) **US$ 20,79**. Estimativa da York para o Fernando: **US$ 3 a 6/mês**.

**Três riscos de custo, na ordem em que importam:**
1. **O `INDEX.md` vai em TODA resposta** — hoje 43.066 chars ≈ **10,7k tokens, um quarto do custo de cada resposta**, com 126 itens. É a única despesa que cresce sozinha: com 500 itens no vault, cada resposta custa o triplo sem ninguém conversar mais. Solução futura: índice resumido ou busca em vez de despejo.
2. **Teto de 60 respostas/hora não segura nada**: US$ 0,99/h, ou US$ 23,76 num dia de descontrole — quatro dias de uso real a cada hora. **York recomenda 25/h** (US$ 0,41/h). O de 6/min ela aprovou: é o dobro do pico observado (3/min) e não deve ser mexido.
3. **A DM não tem teto nenhum** — e mais da metade do gasto de hoje saiu por lá (514k de 976k tokens). Não é urgente (é o Fernando sozinho, sem bot respondendo a bot), mas o cofre está trancado e a janela aberta.

## Os 7 Satélites — mapa completo

| Satélite | Faceta | Funções originais (vault) | Absorvido do FURY | Comandos absorvidos |
|---|---|---|---|---|
| 🧠 Stella (`/vegapunk`) | soma / roteador | `ask`, `wake`, `council`, `sync` | fury-master, hamann, checkpoint, devops, sm | `route`, `story`, `release`, `checkpoint`, `premises` |
| 🪖 Shaka | juiz, risco, triagem | `judge`, `risk`, `audit-triage`, `versus` | qa, seraph, compliance do content-reviewer | `review`, `gate` (PASS/CONCERNS/FAIL/WAIVED), `test-design`, `compliance`, `security-check` |
| 🏴‍☠️ Lilith | red team, hype | `attack`, `hype-check`, `premortem`, `versus` | smith | `verify`, `break`, `evidence` |
| 💡 Edison | ideias → protótipo | `ideas`, `apply`, `combine`, `weekend` | analyst, pm, ux-design-expert | `brainstorm`, `discovery`, `prd`, `wireframe` |
| 📚 Pythagoras | arquivista do vault | `recall`, `dossier`, `compare`, `gaps`, `tags` | content-researcher, architect, po | `research`, `architecture`, `backlog`, `decision` (ADR) |
| 🔧 Atlas | implementa | `build`, `plan`, `explain`, `fix` | dev, data-engineer + **master do squad `avaliacao-imoveis`** | `develop`, `undo`, `run-tests`, `dod`, `critique`, `schema`, `rls`, `migration`, `avaliar` |
| 🍩 York | custo, saúde, retorno | `health`, `cost`, `stuck`, `worth-it` | mifune, budget/ROI do traffic-manager | `pricing`, `offer`, `roi`, `budget`, `launch` |

**Regras de relação codificadas nas procedures** (não mudar sem revisar as tasks):
- Só **Stella** faz `git push`, e só após `gate` do Shaka com PASS (ou CONCERNS/WAIVED aceito) **e** com Fernando escrevendo literalmente "push" na sessão. Todos os outros: nunca `git add/commit/push`.
- Lilith `verify` antes do `gate` em risco alto. Atlas para e chama Shaka quando o pedido exige decisão de valor/risco. Edison pergunta a York "coxinha ou jantar?" antes de propor algo caro. York dá `roi` antes de Atlas gastar Mother Flame.
- Ciclo padrão: **Edison `prd` → Stella `story` → Atlas `develop` → Lilith `verify` → Shaka `gate` → Stella `release`**.
- Fora do laboratório (marketing, copy, brand, tráfego, storytelling): Stella `route` aponta o squad do FURY instalado em `~/.claude/commands/<squad>/agents/`.

## Anatomia de um agente `.md` (ordem das seções no YAML)

`activation-instructions` (prosa; inclui CONVERSATION MODE, PERSONAL MEMORY, ABSORBED CAPABILITIES, SOURCE DISCIPLINE, VAULT IS READ-ONLY) → `agent` → `persona_profile` (canon, tom, greeting_anchor, signature_phrases) → `persona` → `vault` → `user_context` → seção própria (`judgement_rubric` Shaka / `attack_patterns` Lilith / `ideation_rules` Edison / `build_rules` Atlas / `ops` York / `routing` Stella) → **`mind`, `relationships`, `conversation`, `quirks`, `examples`, `memory`** (personalidade, sessão 3) → **`absorbed_from`, `absorbed_principles`, `dependencies`** (absorção, sessão 3) → `commands` (originais, depois `# ── absorvidos do FURY ──`, depois `exit`) → `procedures` (originais + absorvidas no fim).

- **Parser**: `activation-instructions` NÃO é YAML válido (prosa com `:`); o bot e os testes parseiam a partir de `\nagent:`. Ao editar, manter strings com `:`/`→` entre aspas — `tests/test_satellites.py::test_load_all_satellites` quebra se o YAML quebrar.
- **Editar um agente** = editar a fonte, rodar `PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_satellites.py`, rodar `scripts/sync_agents.sh`. Nunca editar as cópias (global/FURY/plugin) diretamente.
- **Nada se perde**: `tests/satellites_baseline.json` guarda seções e comandos anteriores à absorção; `test_nothing_lost_vs_baseline` falha se algum sumir. Se adicionar comandos novos de propósito, regenerar o baseline (script inline no histórico da sessão 3; ou simplesmente editar o JSON).
- **Dependências existem**: `test_dependencies_exist_when_absorbed` confere que cada task/checklist/template/squad citado em `dependencies` existe em `squads/vegapunk/`.

## `squads/vegapunk/` — autossuficiente (não depende do FURY)

```
squads/vegapunk/
  memory/<id>.md            diário de cada Satélite (relacionamento; NÃO é vault). Lido na ativação e pelo bot.
  tasks/<id>-*.md           procedimentos passo a passo das funções absorvidas (63 arquivos no total com os abaixo)
  checklists/<id>-*.md      DoD, gate, segurança, compliance, vereditos da Lilith, dinheiro da York…
  templates/<id>-*.md       PRD (Edison), research/architecture/backlog/ADR (Pythagoras), pricing/ROI (York)
  avaliacao-imoveis/        squad de laudos NBR 14653 copiado do FURY (agents em commands/agents/, tasks, checklists, workflows, squad.yaml). Atlas = master via *avaliar.
  squad.yaml, README.md, tasks/ (originais do squad)
```
As tasks foram **escritas do zero** (condensadas dos agentes FURY, que só tinham procedimentos inline — as tasks que eles referenciam não existem como arquivos no FURY). Adaptadas ao contexto: Fernando engenheiro civil, SaaS pessoal para vender, site de cliente, Claude Code + Docker + OpenRouter + SQLite/Supabase. Sem Epics/ADE/WIS.

**Limitação conhecida**: a diretiva `ABSORBED CAPABILITIES` usa caminho absoluto `/home/crazu/projetos/vegapunk/squads/vegapunk/`. Funciona de qualquer projeto nesta máquina; o plugin instalado em outra máquina precisa desse diretório (ou trocar por caminho relativo ao plugin — o plugin já recebe `squads/vegapunk/` pelo sync? **NÃO**: o sync copia agentes para `plugin/.../skills/<id>/SKILL.md`; as tasks não vão para o plugin ainda. Tarefa pendente se o plugin for usado fora daqui).

## Satélites no Telegram

- `src/vegapunk/satellites.py`: `load(id)` lê o `.md` da fonte (YAML de `agent:` em diante); `build_system_prompt` = seções `PROMPT_SECTIONS` (agent, persona_profile, persona, mind, relationships, conversation, quirks, examples, absorbed_from, absorbed_principles) + diário + `INDEX.md`; `pick_vault_items` anexa até 3 itens do vault por palavras-chave do título/tags (sem tool calls).
- `src/vegapunk/chat.py`: tabelas `chat_state` (Satélite ativo por chat) e `chat_messages` (histórico; 12 últimas ao modelo; tokens por resposta). `Chat.reply()` é síncrono, chamado via `asyncio.to_thread`.
- `bot.py`: `/stella` (= `/vegapunk`), `/shaka`, `/lilith`, `/edison`, `/pythagoras`, `/atlas`, `/york` `[mensagem]`; texto sem link → Satélite ativo (Stella se ninguém); `/quem`, `/dormir`, `/esquecer` (apaga histórico do ativo), `/conta` (tokens por Satélite). **Links continuam sendo capturados normalmente.**
- Custo medido: ~6k tokens de entrada por mensagem sem item anexado, ~14k com (≈ US$ 0,002–0,005 no gemini-3.7-flash). Cresce com o INDEX.
- Limites: **sem ferramentas** no Telegram (não executa comandos absorvidos, não escreve no diário — só lê; diz que "isso se faz no Claude Code"); histórico cortado, não resumido; `/stella` responde "acordou. Pode falar." sem saudação em personagem (melhoria fácil: uma chamada extra ao modelo no wake).
- Validado em produção 2026-08-26 22:19–22:25 (prints): Stella, Shaka e Lilith responderam em personagem e apontaram `/nome` corretamente; 4 links encaminhados foram capturados no meio da conversa.

## Como operar

| Ação | Comando |
|---|---|
| Logs | `docker compose logs --tail 50 -f` (container em UTC: 22:19 local = 01:19 no log) |
| Mudou `.env` | `docker compose up -d --force-recreate` (restart NÃO relê o .env) |
| Mudou código em `src/` ou um agente `.md` | `docker compose restart` (montado por volume, sem rebuild) |
| Mudou `pyproject.toml` / deps | `docker compose build && docker compose up -d` (pyyaml já está na imagem via huggingface_hub; foi só declarado) |
| Testes | `PYTHONPATH=src .venv/bin/python -m pytest -q` (41) |
| Editou agente | `scripts/sync_agents.sh` (global + FURY + plugin + `vegapunk.md` + `squads/vegapunk/` → FURY) |
| Ver banco | `sqlite3 data/vegapunk.db "select id,status,platform,title from knowledge_items"` · conversas: `select satellite,count(*) from chat_messages group by 1` |
| Conversa por Satélite no chat | `/conta` no Telegram |

## Decisões fechadas (não reabrir)
- Python único + polling + SQLite + Docker local. Sem Rails/Sidekiq/webhook/VPS.
- Sem API da Anthropic direta (custo). OpenRouter via SDK `openai`, `response_format json_schema strict` + Pydantic com 1 retry (enrich); chat livre com `temperature=0.8`.
- Vault `punk_records/` é projeção do SQLite; só `## Notas manuais` é editável à mão.
- **Uma personalidade, dois lugares**: Telegram lê o mesmo `.md` do Claude Code. Nunca criar system prompt separado no bot.
- **Absorção é aditiva**: nunca remover comandos/seções originais dos Satélites ao adicionar funções.
- **Autossuficiência**: `squads/vegapunk/` não aponta para o FURY; o FURY recebe cópia (sync), não o contrário.
- York NÃO é devops/scrum (foi cogitado e descartado em 2026-08-27): Ganância = dinheiro (pricing/oferta/ROI). Push e cadência são do Stella.

## Armadilhas conhecidas
- **`.env`: NUNCA comentário na mesma linha do valor** (Docker `env_file` não trata `#`; foi a causa do 403 do TikTok). Se aparecer `# cookies.txt (Netscape)...` na raiz, é esse bug.
- TikTok "Unable to extract universal data for rehydration" é intermitente (~40%) → 6 tentativas com espera crescente.
- YouTube legendas: só manuais (pt/en/es) ou auto ORIGINAL (`*-orig`); nunca `pt` de auto-caption (429 → 33 min de Whisper).
- Whisper: `language_detection_segments=4`; áudio com <3 s de fala após VAD é pulado.
- Item `extraction_failed`/`pending_manual` → `punk_records/_pending/`; colar texto em "Notas manuais" e `/reprocess <id>`.
- `yt-dlp` desatualizado é a causa nº 1 de falha: `docker compose build --no-cache`.
- YAML dos agentes: `vocabulary: [..., "aguenta?"]` e `routing: - {need: "...", satellite: x}` precisam ficar assim (com aspas / flow mapping) — foram os dois pontos que quebravam o parser.
- Texto sem link no Telegram agora **custa tokens** (vai ao modelo). Mensagem acidental = uma coxinha.

## Mapa do código
`src/vegapunk/`: `bot.py` (handlers: links → pipeline; texto → chat; comandos de Satélite) → `pipeline.py` (normalize→extract→enrich→persist, retries, triagem, reprocess) → `normalize.py`, `extract.py` (yt-dlp + VTT + faster-whisper + slides TikTok), `enrich.py` (OpenRouter; schema; `read_slides`; `_client()` reutilizado pelo chat), `vault.py` (md + INDEX + git), `db.py` (SQLite + `transition_to`), `config.py` (env), **`satellites.py`** (persona → prompt, vault picker), **`chat.py`** (estado/histórico/reply).
`tests/`: 41 testes; `test_satellites.py` cobre load dos 7, prompt, vault picker, chat state/history/reply (mock), nada-se-perde, dependências existem.

## Dívida conhecida do multi-bot (escrita, não esquecida)
- **Story 2** (não escrita): histórico **compartilhado** do grupo (H4 — cada Satélite ler o que os outros disseram), `/custo` agregado, atraso aleatório por bot, renomear `TELEGRAM_BOT_TOKEN` → `_STELLA` (o código já aceita os dois desde a v1.7.0).
- **Won't da v1**: um Satélite acionar outro sozinho, sem o Fernando pedir. Maior risco de loop e custo.
- Indicador "digitando…" sai como Stella mesmo quando quem vai responder é outro (BAIXO, `*verify` da 1c).
- `enrich` continua com `timeout=180, max_retries=2` — correto para transcrição de uma hora, mas o raciocínio que corrigiu o roteador se aplica a ele um dia (ressalva do gate da 1a).

## Ideias para depois (não iniciadas)
- **Ler imagens no Telegram (Story 1e, pedida em 2026-08-31, adiada pelo Fernando)**. Hoje print **não é lido**: os handlers são `filters.Document.ALL` e `filters.TEXT | filters.CAPTION`; não há `filters.PHOTO`. Print sem legenda cai no vazio; com legenda, só a legenda é lida — **parece que funcionou e não funcionou**, que é o pior caso. `DOC_EXTS` também não aceita imagem. **A peça já existe**: `enrich.read_slides()` manda imagens ao modelo multimodal (usada nos carrosséis do TikTok) e o `gemini-3.7-flash` enxerga imagem nativamente. Falta ligar ao Telegram. Três decisões antes de codar: (a) print é **contexto de conversa** ou **item do vault**? (b) só **transcrever texto** (como o read_slides faz hoje) ou também **descrever** a imagem — são prompts diferentes; (c) teto de imagens por mensagem, porque imagem custa vários milhares de tokens. Palpite do uso real do Fernando (engenheiro civil): print de planilha, laudo e tela de sistema, para o Satélite ler o conteúdo e comentar → caminho "ler + transcrever".
- **Telegram com ferramentas**: deixar os Satélites executarem comandos absorvidos leves pelo chat (ler item do vault por nome, `*roi` da York, `*evidence` da Lilith) via tool-use no OpenRouter; e **escrever no diário** (`## Diário`) quando o Fernando conta algo. Hoje só leem.
- Saudação em personagem no `/nome` (uma chamada ao modelo no wake).
- Resumo do histórico quando passar de N mensagens (hoje corta em 12).
- Plugin autossuficiente: copiar `squads/vegapunk/{tasks,checklists,templates}` para dentro do plugin e trocar o caminho absoluto da diretiva.
- Mover `examples` de cada agente para arquivo à parte se os `.md` ficarem grandes demais para manter a voz.
- **Visão (Opção A, decidido 2026-08-26)**: `ffmpeg` 1 frame/10 s → `enrich.read_slides()`; gatilho manual `/ver <link>`; ~US$ 0,02 por 10 min.
- Parser do enrich mais tolerante (extrair `{...}` do texto).
- TikTok slideshow já suportado (`extract_tiktok_slides`, API privada do yt-dlp — se quebrar, log mostra `tiktok web data:`). Instagram carrossel/Reels: exigem cookies (`VEGAPUNK_COOKIES_FILE`), não testados.
- Healthcheck diário no Telegram (York já tem o comando no Claude Code; falta agendar no bot).
- Push automático do vault (`VEGAPUNK_GIT_PUSH=true` + `~/.ssh` no compose).
- ~~Bloco "Base de conhecimento" no CLAUDE.md do SaaS e do site do cliente~~ — FEITO 2026-08-27: bloco em `docs/punk-records-claude-md.md` e adicionado ao **global** `~/.claude/CLAUDE.md` (vale para todo projeto da máquina). O SaaS e o site do cliente ficam em outros diretórios.
- MCP de consulta ao vault.
- **Integrar o Punk Records com Notion ou Obsidian** (pedido do Fernando em 2026-08-27, a estudar). Obsidian: o vault já é Markdown com frontmatter — basta abrir `punk_records/` como vault; avaliar wikilinks, Dataview sobre `tags`/`applicability`, e não quebrar `## Notas manuais`. Notion: exige sync via API (páginas por item, propriedades = frontmatter); há um doc antigo em `.docs/pacote_telegram_knowledge_bot_v1/06_persistencia_obsidian/`.
