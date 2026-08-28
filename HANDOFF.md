# HANDOFF — Vegapunk (atualizado em 2026-08-28, sessão 5)

## TL;DR — o que existe hoje

Vegapunk é **duas coisas** que compartilham uma fonte da verdade:

1. **Fabriophase (bot Telegram)** — captura links (YouTube/TikTok/Instagram) → extrai → resume via OpenRouter → guarda no SQLite → projeta em `punk_records/` (o Punk Records, versionado) → commit automático. **E agora conversa**: os 7 Satélites respondem no Telegram em personagem (`/stella`, `/shaka`, …).
2. **Labophase (Claude Code)** — os 7 Satélites como skills (`/vegapunk`, `/vegapunk:lilith`, …), cada um com personalidade completa **e** funções absorvidas do FURY (dev, qa, smith, pm, po, mifune…), autossuficientes em `squads/vegapunk/`.

Fonte da verdade de cada Satélite: `.claude/commands/vegapunk/agents/<id>.md`. **Tudo o mais é cópia** gerada por `scripts/sync_agents.sh` (global `~/.claude/commands`, FURY, plugin, `vegapunk.md`).

Estado: container `vegapunk-vegapunk-1` rodando com o código de hoje; **70/70 testes verdes**; GitHub `fernand-nan-ia/Vegapunk` em `fb1bacf` (v1.5.2, sessão 4h); working tree limpa.

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

1. ~~Decidir as 3 perguntas em aberto do PRD multi-bot~~ — **FEITO em 2026-08-28** (Sessão 5); decisões em `docs/prd/satelites-multibots-grupo-telegram.md` §0.
2. Pedir ao Stella `*story` (Story 1 do PRD — prova de conceito com 2 bots, Stella + Lilith) e cadastrar os 2 bots no BotFather: **Stella = bot leitor, privacy mode OFF**; **Lilith = send-only, privacy ON**.
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

## Sessão 5 (2026-08-28) — decisões do multi-bot fechadas: cascata de camadas + roteador — **PRD atualizado, sem código**

Container estava parado de novo (Docker Desktop sem integração WSL no início da sessão); subido com `docker compose up -d`.

As três perguntas que travavam a Story 1 foram respondidas pelo Fernando, e a resposta dele à segunda mudou o desenho do PRD — está tudo em `docs/prd/satelites-multibots-grupo-telegram.md` §0 e §4.1:

- **(a) Privacy mode OFF: sim, mas só num bot.** Fernando confirmou o OFF; ao desenhar o roteador ficou claro que apenas **um** bot precisa *ler* o grupo. Privacy mode controla o que o bot **recebe**, não o que ele **envia** — logo os outros 6 ficam privacy ON e **send-only** (sem handler de mensagem), publicando com nome e ícone próprios. Sete participantes visíveis, uma superfície de leitura.
- **(b) e (c) resolvidas por contexto, não por regra.** Fernando perguntou se o bot não podia ler o contexto e entender se está sendo chamado. Pode — a questão era onde essa inteligência mora: 7 bots perguntando ao modelo = 7 chamadas por mensagem. A saída é **um roteador central** (os 7 já rodam no mesmo processo): 1 chamada barata, **sem persona e sem `INDEX.md`**, com a mensagem + 3 últimas linhas, devolvendo `{"satelites": [...], "confianca": ...}`. Resolve "fui pra Nova York" (lista vazia) e "Shaka e Lilith" (os dois) sem exceção escrita à mão para a York.
- **(d) Janela de continuidade: 10 minutos** (Fernando ajustou de 5 para 10). Mensagem sem nome dentro da janela → responde quem falou por último; fora dela, silêncio.

**A cascata (§4.1)** substitui o Must antigo "filtro local (regex, sem LLM)": camadas 0–2 grátis (is_bot/chat autorizado → `@menção` direta sem roteador → sem nome e fora da janela = ninguém), camada 3 roteador (~US$ 0,0002), camada 4 resposta em personagem (~US$ 0,002–0,005). O regex sobrevive só como corte de ruído. **Roteador falha fechada** (erro/timeout/`confianca: baixa` → ninguém responde), schema estrito + Pydantic como no `enrich`, e log de toda decisão para auditar falso positivo/negativo na primeira semana; `@menção` é o caminho determinístico de escape que não passa por ele.

Custo do Must subiu de ~2,5 para ~3 fins de semana (Story 2 virou ~2). H2 ganhou casos de aceite concretos (Nova York, dois nomes, dois nomes com um sendo objeto da frase) e nasceu H2b (janela).

Punk Records consultado: **nenhum registro** sobre bots de Telegram, roteamento ou detecção de intenção — decisão tomada só com raciocínio de arquitetura.

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

## Ideias para depois (não iniciadas)
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
