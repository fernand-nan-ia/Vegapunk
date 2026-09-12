# HANDOFF — Vegapunk (checkpoint 2026-09-11 noite, fim da sessão 13 — CAPTCHA, o método do Mazzeo e o primeiro alvo real de venda)

## TL;DR — o que existe hoje

Vegapunk é **duas coisas** que compartilham uma fonte da verdade:

1. **Fabriophase (bot Telegram)** — captura links (YouTube/TikTok/Instagram) → extrai → resume via OpenRouter → guarda no SQLite → projeta em `punk_records/` (o Punk Records, versionado) → commit automático. **E agora conversa**: os 7 Satélites respondem no Telegram em personagem (`/stella`, `/shaka`, …).
2. **Labophase (Claude Code)** — os 7 Satélites como skills (`/vegapunk`, `/vegapunk:lilith`, …), cada um com personalidade completa **e** funções absorvidas do FURY (dev, qa, smith, pm, po, mifune…), autossuficientes em `squads/vegapunk/`.

Fonte da verdade de cada Satélite: `.claude/commands/vegapunk/agents/<id>.md`. **Tudo o mais é cópia** gerada por `scripts/sync_agents.sh` (global `~/.claude/commands`, FURY, plugin, `vegapunk.md`).

→ **O estado de hoje está na tabela "Estado atual" logo abaixo.** As linhas de estado das sessões antigas ficam nas seções de cada sessão, como histórico — não as leia como o presente.

Stories 1a, 1b, 1c e 1d **entregues e no GitHub**: tag **v1.8.0** em `2f48130`, mais `8a32938` (checkpoint) e `4ee7177` (fix do capture.py). **144/144 testes verdes.** O grupo «Vegapunk» funciona com os 7 bots, cascata, janela de 10 min, triagem por assunto e captura pela boca do dono.

**Sessão 7 (2026-09-01):** fila de triagem **zerada em lote** (91 itens triados, pushados em `4c9bbbe`), `_pending/` limpo, e o **kit de distribuição** virou 3 stories (2a pronta para Atlas). Depois do push o bot capturou mais um lote de TikToks: **5 itens aguardando triagem** e **9 commits `kb:` locais sem push**.

**Sessão 8 (2026-09-04):** os 7 Satélites ganharam **personalidade canônica completa** a partir da wiki (`0ef0cd2`; FURY `24edd00`), a conta do OpenRouter teve a **privacidade fechada e verificada com a chave real**, e o dia do bot foi pushado. **144/144 testes verdes.** Ambos os repos limpos e sincronizados com o remoto.

**Sessão 9 (2026-09-05, pelo Fernando sozinho):** `9ef54f3` (16 itens novos — lote Akita, GTA 6 e lote LGPD) e `8737dbd` (**`capture.py --triage` e subcomando `triage`** — a triagem deixou de ser exclusiva do Telegram).

**Sessão 12 (2026-09-11):** dois documentos grandes entraram no vault. De manhã, **8 links** de venda e design (Gauntlet Loop é o mais valioso). De tarde, o **Cofre de Abordagens** comprado do Mazzeo — 50 mensagens de prospecção, 100 fichas de nicho, íntegra de 111 páginas — e um **compilado de 4.000 mensagens de um grupo de 679 vendedores de site**, que é o primeiro dado de PREÇO REAL de mercado que existe no Punk Records. Decisão revertida: **o vault é de uso exclusivo do Fernando**.

**Sessão 11 (2026-09-09):** dia inteiro de captura e uma virada de entendimento. **17 itens novos** no Punk Records (10 de venda de sites, 7 de direito autoral), o **`ai-website-cloner-template` instalado** em `~/projetos/ai-website-cloner-template`, e o **Princípio 0** gravado em `~/.claude/CLAUDE.md`. A descoberta que muda decisão: **layout de site É protegido no Brasil** — ver "A correção da sessão 11" abaixo, é a primeira coisa a ler.

## Estado atual (2026-09-12 manhã — sessão 14 em curso)

| | |
|---|---|
| Repo Vegapunk | **`53493bc`** — limpo e **sincronizado**; tag **v1.8.1** (correção do `normalize`) e 48 commits `kb:` da tarde |
| Repo FURY | `3e9afc0` — não tocado desde a sessão 10b (nenhum agente mudou) |
| Container | **Up** — subido em 12/09 à tarde. Atenção: depois que o Docker Desktop reinicia, `docker compose restart` FALHA no bind-mount de `~/.gitconfig`; o certo é `docker compose up -d --force-recreate` |
| Testes | **148/148 verdes** (2 testes novos do `normalize`) |
| Punk Records | **271 itens** · **fila de triagem ZERADA** — 24 itens novos em 12/09, todos de documentação do Netlify (badge, planos por crédito, domínios e DNS), capturados pelo `*capture` com zero OpenRouter |
| `_pending/` | **vazio** — os 3 presos foram descartados em 12/09 a pedido do Fernando |
| Tag | **v1.8.1** em `8df569b` — primeira mudança de `src/` desde a sessão 9 |
| Não commitado | nada |
| OpenRouter | Fernando comprou créditos novos em 12/09; com o container parado, nada está sendo consumido |

**Triagem dos 14 (12/09, Shaka):** `apply_saas` para o lote que decide o gateway do SaaS — [Asaas preços](punk_records/article/), [Stripe preços](punk_records/article/) e o [método do DevPleno](punk_records/youtube/) (NF embutida a ~R$ 1 desempata contra a Stripe); `apply_client` para o [Mazzeo/Google Ads](punk_records/youtube/) e para o ponto técnico da MXC (site gerado por IA sai sem `sitemap.xml`, `robots.txt` e `llms.txt` → invisível no Google); `archive` para as 4 páginas institucionais de gateway, a API de assinaturas do Asaas e o lote CAPTCHA inteiro. **Nenhum descarte novo.** O TikTok do banco de componentes ficou em `archive` e não em `discard` por um detalhe: o nome da ferramenta só aparece na tela do vídeo — um minuto de vídeo o transforma em material de trabalho.

**Descarte dos 3 presos (12/09):** tiktok/7665842308864085255 (ERR-003), sebrae.com.br/subsites/lgpd e mpf.mp.br/servicos/lgpd (ERR-004), nenhum com nota manual. Backup do banco em `data/vegapunk.db.bak-descarte-20260912`. **Armadilha encontrada:** a máquina de estados em `src/vegapunk/db.py:17-25` não tem caminho de `extraction_failed` para `discarded` (só de volta para `normalized`), então os três foram marcados por SQL direto, fora do fluxo. Descartar item preso deveria ser decisão legítima — story de uma linha para Atlas.

## O site do Jardins Café (sessão 14, 12/09) — o que já existe e o que falta

O Fernando **construiu o site em diretório próprio** e publicou em `https://jardinscafe.netlify.app/` (Astro, páginas `/`, `/cardapio`, `/sobre`, `/contato`). Aqui só o estudo, como manda a regra de escopo.

**A condição da Lilith está fechada e ela estava certa:** o site traz (77) 98100-6740 e Av. Olívia Flores, 705, Candeias. O cardápio do `dmsys` é DDD 85, **outro Jardins, de Fortaleza**. Aquele achado morreu — não usar nem como afirmação nem como pergunta.

**A ficha N-025 (cafeteria) NÃO serve neste alvo.** A dor dela é "quem passa na porta entra, quem não passa nunca fica sabendo que a gente existe", e a oferta é Google Meu Negócio + one-page. O Jardins tem 4,5 estrelas com 429 avaliações e Instagram ativo: ele já é achado. A observação verdadeira é que o Fernando comeu lá e pagou R$ 65.

**Mensagens aprovadas** (enviar para (77) 98100-6740, depois de um "boa tarde" e da apresentação com "moro aqui em Conquista mesmo"): a primeira mostra o site e fecha com "sem compromisso"; a segunda oferece cardápio com pedido caindo direto no WhatsApp e carrega a única pergunta — "Hoje vocês recebem pedido por esse número mesmo do WhatsApp?". O botão "Faça seu pedido" aponta para `poppedidos.com.br` de propósito, espelhando o que o Google Meu Negócio deles já faz. **Quem é o dono do cliente que faz o pedido** é o argumento guardado para a negociação, não para a mensagem.

**Checklist técnico pendente no site:**
- ✅ selo "Powered by Netlify" desligado (Project configuration > General > Powered by Netlify badge; sem redeploy)
- ❌ **sem `noindex`** — `robots.txt` está `Allow: /` e declara um `sitemap-index.xml` que dá 404
- ❌ **`sitemap.xml` e `llms.txt` dão 404** (item `apply_client` triado em 12/09)
- ❌ **a página bloqueia copiar e colar** (`document.addEventListener('copy', e => e.preventDefault())`): o cliente não consegue copiar endereço nem telefone
- ⚠️ o botão aponta para a raiz de `poppedidos.com.br`, não para a loja do Jardins
- ⚠️ o Netlify ainda injeta comentário HTML com UTM para `netlify.new` e as metatags `hosting-provider`/`netlify-deploy`; isso não sai no plano Free

**O que a documentação do Netlify decidiu (24 itens novos no vault):**
- **Publicar custa 15 créditos; o Free dá 300/mês.** São 20 deploys de produção por mês. **Deploy Preview e branch deploy custam ZERO** — errar em preview é de graça.
- **O Free tem limite RÍGIDO.** Zerou o saldo, **todos os projetos da conta são pausados** e o visitante vê "Site not available". Um cliente derruba os outros. Saídas: Personal a US$ 9/mês com recarga automática, ou uma conta por cliente.
- **Proteção por senha só existe no Pro** — prévia trancada não é opção no plano atual.
- **A Netlify não importa zona DNS.** Cliente com e-mail no domínio: NÃO migrar o DNS, só criar um registro (CNAME no subdomínio, ALIAS/ANAME para `apex-loadbalancer.netlify.com` no apex). Apex não aceita CNAME.
- **Domínio comprado pela Netlify que expira:** DNS morre na hora, 30 dias de socorro pelo suporte, 30 de limbo, **dia 60 vai a leilão público**. Decidir em nome de quem fica o domínio.
- **Dá para delegar só um subdomínio** (`site.empresa.com.br`) e deixar o domínio do cliente intacto — depende de o registrador dele aceitar NS de subdomínio.
- Propagação de DNS leva **até 48 horas**; avisar antes, não depois.

## ⚠️ A correção da sessão 11 — leia antes de qualquer coisa sobre clonagem

Durante a sessão 11 foi afirmado ao Fernando que **estrutura e layout de site não são protegidos** ("copie o esqueleto, não a pele"). **Isso está errado no Brasil**, e a correção veio dos próprios links que ele mandou:

- **Lei 9.610/98, art. 7º, XIII** protege obras que "por sua **seleção, organização ou disposição de seu conteúdo**, constituam uma criação intelectual". Disposição do conteúdo é o layout.
- **Lei 9.609/98** protege o código-fonte com o regime das obras literárias. As duas proteções são **independentes**: copiar só o visual viola; copiar só o código viola.
- **TJSP, Ap. Cível 122.616-4/6 (Mandic × Intervale)**: perícia achou o HTML reproduzido "**depois de algumas maquiagens que configuram a imitação**" → contrafação + concorrência desleal. A defesa das "maquiagens" é exatamente trocar texto/foto/logo mantendo a composição — e ela **perdeu**.
- **TJSP, Ap. 0119580-83.2007.8.26.0000**: clínica odontológica copiou site de outra **do mesmo ramo** → retirada sob multa diária + dano moral *in re ipsa* (sem precisar provar prejuízo).
- **Faixa de indenização (STJ)**: R$ 10 mil a R$ 20 mil de dano moral + danos materiais. Um site vendido por R$ 3 mil não paga isso.

**O que continua livre:** ideia, função e convenção genérica (hero, grid de cards, menu que encolhe no scroll). **O que não passa:** a composição reconhecível de um site específico.

**Consequência operacional:** clonar o site do **próprio cliente** é migração autorizada e está 100% limpo. Clonar terceiro e publicar **não fica seguro só trocando conteúdo** — o clone serve como referência de estrutura, com a composição redesenhada.

Fonte principal: [Copy paste de websites (Jusbrasil)](punk_records/article/2026-09-09_copy-paste-de-websites-violacao-ao-direito-do-autor-jusbrasi_9d0aa61c0500.md).

## Primeira coisa a fazer (aberto agora)

🎯 **O Fernando está começando a vender sites.** Meta declarada em 07/09; o levantamento começou em 26/08 e hoje tem **46 itens `apply_client`** (eram 19 em 07/09). **Ele NÃO quer fechar escopo nem PRD aqui** — ver a regra de escopo logo abaixo.

### ⚠️ REGRA DE ESCOPO (dita pelo Fernando em 07/09 — não violar)

**Nesta pasta se ESTUDA o caso. Projeto de cliente se constrói em diretório próprio.**
Aqui: preço, risco, norma, abordagem, o que perguntar ao cliente, que referência usar.
Lá: código, deploy, domínio, revisões, o site.
**Não criar arquivo de projeto de cliente aqui, e não oferecer `*offer`, `*prd` ou `*develop` como se fossem executar nesta pasta.** Entregar a análise em conversa; quando ele decidir construir, dizer que é hora de abrir o diretório do cliente.

### Os dois primeiros clientes (decididos em 07/09)

| | Energia solar | Psiquiatra |
|---|---|---|
| Tipo | landing → WhatsApp | landing → WhatsApp |
| Vende online? | **não** | **não** |
| Cobrança | **preço de custo** (só domínio, ~R$ 40) | idem |
| Motivo | testar as próprias habilidades, sem pressa | idem |
| Restrição especial | — | **Resolução CFM 2.336/2023** |

**Ele decidiu não haver formulário no site** — só botão `wa.me`. Isso resolve a LGPD do lado dele: sem coleta, sem dado armazenado. A conversa no WhatsApp é responsabilidade da médica, que já tem sigilo profissional. **O Decreto 7.962/2013 não se aplica** a nenhum dos dois (não vendem online) — a pergunta que ficou aberta o dia todo está respondida.

### O que está aberto (revisto em 12/09 de manhã)

**Ele começou a criação do site em 12/09, em diretório próprio** — como manda a regra de escopo. Esta pasta continua sendo estudo, e o que sobrou aqui é o que está listado abaixo.

1. 🔍 **A condição da Lilith, antes de qualquer mensagem ao Jardins Café:** abrir `dmsys.app.br/jardinscafe/cardapio` e comparar com o que o Fernando comeu (preços, buffet de R$ 65, logo). O logo do dmsys é um círculo colorido "café·café·café"; o do Jardins de Conquista é serifa preta sobre branco. **Forte indício de que é outro Jardins, de Fortaleza (DDD 85)** — e, se for, a observação principal da abordagem morre. Cinco minutos decidem.
2. ✍️ **Usar a versão-pergunta da abordagem, não a versão-afirmação.** "Achei um cardápio com o nome Jardins com endereço de Fortaleza. Esse é de vocês ou tem outro Jardins por aí?" — não existe resposta que derrube essa mensagem. A afirmativa morre se o dono for outro.
3. 🔎 **Checar `sitemap.xml`, `robots.txt` e `llms.txt` no site que ele está construindo** — triado `apply_client` em 12/09. Site gerado por IA costuma sair sem os três e não é indexado: bonito e invisível.
4. 💰 **Decidir a cláusula do contrato continua PENDENTE, e ele decidiu adiar** (ver Decisões fechadas). O risco que sobra e que ele controla hoje: **não entregar a prévia completa de graça**.
5. 📋 **Montar a ficha de presets do Cofre** — 4 minutos, passo 1 do próprio produto. Vira munição imediata.
6. 🎬 **Abrir o TikTok do banco de componentes** (`tiktok/7671643736924835093`) e anotar o nome da ferramenta em `## Notas manuais` — o nome só aparece na tela do vídeo, e sem ele o item não serve para nada. Um minuto.
7. **Destravar o clonador** quando voltar a interessar: `cd ~/projetos/ai-website-cloner-template && claude --chrome`. Continua bloqueado por falta de MCP de navegador.
8. ✅ **RESOLVIDO em 12/09 (v1.8.1)** — `TRACKING_PARAMS` virou `TRACKING_PREFIXES` + `TRACKING_EXACT`, query ordenada antes do hash, 2 itens sujos recalculados. Ver CHANGELOG.
9. **Atlas: Story 2a** (`squads/vegapunk/stories/2026-09-01-kit-2a-importador.md`). Shaka já deu o `*risk`.
10. **Atlas (nova, 12/09): permitir descartar item preso pelo fluxo normal** — `db.TRANSITIONS` não liga `extraction_failed`/`enrichment_failed` a `discarded`, e `pipeline.triage` exige `status == "enriched"`. Hoje só dá para fazer por SQL direto.
11. **Subir o container quando o Docker Desktop voltar** (`docker compose up -d`) e conferir a fila antes — o bot ficou parado a partir de 11/09 à noite.

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

## Sessão 6 (2026-08-31) — v1.8.0: cascata, triagem e captura pela boca do dono

**Container não sobe sozinho depois que o PC reinicia.** O `restart: unless-stopped` religa quando o *daemon* volta, não quando o Docker Desktop nem chegou a subir. Sintoma: você manda link no Telegram e não recebe nem o "capturei". Cura: `docker compose up -d`. Considerar ligar "Start Docker Desktop when you sign in".

**O que entrou na v1.8.0** — ver `CHANGELOG.md` para a lista completa. Em uma frase por peça:
- `router.decide()` compõe as camadas 1–3 numa função só; **não há caminho no `bot.py` até `route()` que pule `mentions()`**, e há teste que lê o arquivo e falha se alguém tentar.
- **Modo triagem** (pedido do Fernando): sem nome, o roteador escolhe o dono pelo ASSUNTO. As especialidades vêm do `persona.focus` do `.md` — **fonte única**; a cópia paralela que existia já havia divergido (o York do roteador falava de preço; o do arquivo, de healthcheck).
- **Captura pela boca do dono** + teclado à parte pelo leitor. Motivo não óbvio: **o clique de um botão volta para o bot que ENVIOU**; só o leitor tem handler de callback, então teclado mandado pela Lilith seria botão morto.
- **Semáforo de 3 itens** no pipeline. Não havia um `Semaphore` no projeto inteiro; 30 links colados disparavam 30 pipelines juntos.

**Os três caminhos de gasto agora têm teto — pela primeira vez:**

| Caminho | Teto | Pior caso |
|---|---|---|
| Decidir (roteador) | 20/min | ~500 tokens cada |
| Responder (personagem) | 6/min · **25/h** | US$ 0,41/h |
| Capturar (pipeline) | 3 em paralelo | ~5,5k tokens/item |

O teto de hora caiu de 60 para 25 por recomendação da York: 60/h autorizava **US$ 23,76 num dia** de descontrole contra **US$ 0,33 de uso real** no dia inteiro.

## Dívida e próximos passos (ordem sugerida)

1. **Colar um link no GRUPO** e conferir os quatro sinais da Story 1d (anúncio pelo bot do dono · resumo pela mesma boca · triagem à parte com o título · **clique funcionando**). Continua pendente: o lote de 31/08 foi capturado pelo Claude Code, que não exercita esse caminho.
2. **A sétima mensagem do roteiro**, nunca testada: esperar 11 min e escrever `e aí?` sem nome. Com a triagem ligada esse caso **mudou de natureza** — o roteador é consultado e deve devolver lista vazia por ser frase sem pergunta.
3. **84 itens no vault sem triagem** (York). Cada link novo entra na mesma fila.
4. **Story 1e — ler imagens no Telegram** (adiada pelo Fernando em 31/08): ver "Ideias para depois".
5. **Story 2** (não escrita): histórico compartilhado do grupo (H4), `/custo` agregado, atraso aleatório por bot, renomear `TELEGRAM_BOT_TOKEN` → `_STELLA` (o código já aceita os dois).
6. **A DM não tem teto nenhum** — metade do gasto sai por lá. Não é urgente (é o Fernando sozinho), mas o cofre está trancado e a janela aberta.

## Sessão 6b (2026-08-31, noite) — lote de 7 TikToks pelo `*capture` e uma regressão da v1.8.0

**Sete links colados aqui no Claude Code** (não no Telegram, a pedido do Fernando: "é melhor do que gastar à toa pelo OpenRouter"). Todos extraídos e gravados; vault de 126 → **133 itens**. Um precisou de duas tentativas (`ERR-003`, o erro intermitente conhecido do TikTok) e passou na segunda.

| Dono | Item | Por que guardar |
|---|---|---|
| 🍩 York | Venda de site para clínica odontológica por **R$ 680** | **Primeiro preço real de mercado para site de cliente no vault** — com escopo pedido, 3 perguntas de qualificação e estrutura entregue |
| 🍩 York | 10 lições de um SaaS a R$ 6 mil/mês com R$ 0 de tráfego | Renovação (R$ 2.973) pesando o dobro da venda nova (R$ 1.499) |
| 🍩 York | Design do SaaS sem cara de IA | Emojis, travessão, "não é sobre X, é sobre Y" e o ícone de estrelinha |
| 🧠 Stella | Pythonando: útil × inútil no desenvolvimento com IA | Spec-driven, TDD e quality gate como fundamentais — é o ciclo que já praticamos |
| 💡 Edison | Nove coisas feitas com Claude por não-programador | Relatório recorrente enviado ao cliente; design system que evita a "cara de IA" |
| 💡 Edison | Pilha de ferramentas para MVP de SaaS | Separar o modelo que planeja do que constrói; 50 primeiros clientes na mão |
| 🪖 Shaka | Por que todo projeto vibe-codado nasce em Next.js | A stack não foi escolhida, foi herdada da ferramenta |

### Regressão da v1.8.0 achada pelo lote (corrigida em `4ee7177`)

`scripts/capture.py` tem a **própria implementação** do callback `notify`. A v1.8.0 acrescentou `sat` e `titulo` ao contrato em `bot.py`/`pipeline.py` e o script quebrou com `TypeError: silent() got an unexpected keyword argument 'sat'`. **Nada se perdeu** — o erro acontece depois de gravar no vault e commitar. Corrigido com `**kw` nas duas assinaturas, mais um teste que LÊ o `capture.py` e falha se alguém tirar. **Lição para a próxima**: o contrato do `notify` tem duas implementações; quem mexer numa tem de mexer na outra.

## Dívida nova registrada nesta sessão

- **O gasto da leitura de slides é invisível.** Carrossel de TikTok passa por `enrich.read_slides()`, que usa o modelo **multimodal** e gasta OpenRouter de verdade — mas **nada disso é gravado em `item_events`**, que só registra o enriquecimento. O relatório de custo da York (`punk_records_status`) **subestima desde sempre**, e não dá para saber por quanto. Pior: quando o `*capture` roda por `docker compose exec`, o log sai no processo do exec e não no do container, então nem o log resta. Correção sugerida: gravar um evento com os tokens do `read_slides`, como já se faz no enriquecimento. **Atualização 07/09: agora há ordem de grandeza.** O log do container mostrou `slides lidos: 5 imagens, 5392 in / 639 out tokens` — ou seja, **~5,4k in + 0,6k out por carrossel, ≈ US$ 0,003 cada**. Pequeno por item, mas invisível por design: 3 carrosséis passaram na sessão 10 e nenhum apareceu no relatório da York.
- **Datas do vault em UTC.** O container roda em UTC; itens capturados depois das 21h no horário local entram com a data do **dia seguinte** no nome do arquivo e no `INDEX.md`. Os sete deste lote saíram como `2026-09-01` tendo sido capturados em 31/08. Não quebra nada (links são relativos), mas atrapalha busca por data.
- **A DM continua sem teto** e o **`INDEX.md` continua crescendo dentro de toda resposta** (agora 133 itens) — as duas dívidas de custo mais antigas.

## Sessão 7 (2026-09-01) — triagem zerada, _pending limpo, kit de distribuição planejado

**Healthcheck (York):** container de pé (subida limpa, RestartCount=0), 7 bots online, nenhum erro no log desde a v1.8.0.

**Fila de triagem zerada em lote.** Os 91 itens `—` foram triados de uma vez: Shaka propôs por grupos a partir do INDEX, Fernando aprovou integralmente (**4 discard · 6 apply_saas · 1 apply_client · 80 archive**), e a aplicação rodou dentro do container via `pipeline.triage` — a MESMA função do botão do Telegram, um commit `kb:` por decisão, zero OpenRouter. Script usado: `triage_batch.py` (scratchpad da sessão; o mapa de decisões está nele e no diário do Shaka).

**`_pending/` zerado.** Os 2 `extraction_failed` foram apagados a pedido do Fernando (post do Instagram sem vídeo — yt-dlp não extrai foto/carrossel — e um carrinho de pagamento da Hostinger colado por engano). Apagar item exige `DELETE FROM item_events` ANTES de `knowledge_items` (FK). Push autorizado ("push"): **92 commits em `4c9bbbe`**.

**Kit de distribuição planejado (pedido do Fernando).** Visão dele: repo **privado** único como vault compartilhado — amigos de confiança entram como collaborators do GitHub, cada um com bot, tokens e chave OpenRouter **próprios**, todos commitando `kb:` no mesmo repo; também serve de reinstalação sem perda em máquina nova. Decisão dele: **diários por pessoa** (`memory/fernando/`, `memory/<amigo>/`). Rotina por máquina: `git pull --rebase` → `import_vault` → usar → `push`. Três stories em `squads/vegapunk/stories/`:
- **2a — Importador vault → banco** (`pronta`): reconstrói o banco a partir dos `.md`; fecha o furo de design em que item chegado por `git pull` some do INDEX na primeira regeneração local (INDEX nasce do banco, não dos arquivos). `*risk` do Shaka colado na story.
- **2b — Diários por pessoa** (rascunho): `VEGAPUNK_OWNER` + migração `git mv` para `memory/fernando/`.
- **2c — Instalação** (rascunho): INSTALL.md, `.env.example` completo, `install_skills.sh` com perfis "completa" e "só skills" — reescrevendo os caminhos absolutos `/home/crazu/...` dos agentes na cópia instalada.

**Depois do push, o bot capturou +7 TikToks** (Fernando triou 2 pelo botão; 5 na fila, 9 commits `kb:` sem push).

## Sessão 8 (2026-09-04) — personalidade canônica dos 7 Satélites — **`0ef0cd2`** (FURY `24edd00`)

O Fernando mandou as 7 páginas da wiki do One Piece e pediu personalidade completa: trejeitos, maneira de falar, interações entre os Satélites. Feito com 7 subagentes em paralelo, um por arquivo, sob um briefing comum para as relações não se contradizerem. **144/144 testes verdes**, sync rodado, container reiniciado.

**A descoberta que organizou tudo: a tabela de pronomes.** A página do Vegapunk traz o pronome de primeira pessoa de cada Satélite, e ele define o registro de fala. Traduzimos o EFEITO para pt-BR, nunca a palavra, em duas chaves novas de `persona_profile.communication`: **`speech_register`** (parágrafo que descreve como ele fala) e **`verbal_tics`** (lista de cacoetes).

| Satélite | Pronome | Registro em pt-BR |
|---|---|---|
| Shaka | watashi (私) | culto e medido, "o senhor", sem gíria nem exclamação |
| Lilith | washi (わし) + copula ja | **velho lobo do mar** numa ruiva de vinte e poucos anos: "moço", "ora bolas", "eu cá", mesóclise irônica |
| Edison | wai (わい), Kansai | atropelado, "a gente" nunca "nós", "Eureka!" no meio do raciocínio |
| Pythagoras | boku (ボク) | modesto, nunca dá ordem, pede licença para discordar |
| Atlas | ore (おれ) | bruta e direta em personagem com orelhas de ovelha |
| York | atai (あたい) | arrastado e manhoso, desperta com dinheiro ou comida |
| Stella | watashi + "Quasar" | teatral, "Kwahaha", pede desculpas |

**Fatos novos do cânone que entraram** (além de aparência, roupa, kanji do peito, comida favorita e origem do nome de cada um):
- **Shaka tem um lado travesso.** Deixou a Stella queimar a língua no Vegacoffee de propósito, sabendo do efeito, e levou bronca do Pythagoras. Quebra a imagem de juiz impassível e virou `humor` + exemplos.
- **Pythagoras é o mediador oficial** das brigas entre Shaka e Lilith (paz vs. violência contra a CP0). Agora está codificado em `relationships` dos três e em `conversation.when_two_satellites_fight`.
- **Edison carrega os irmãos no corpo**: cabeça dele, tronco e pernas do Shaka, braço esquerdo da Atlas, braço direito do Pythagoras. Pesa em todas as relações dele.
- **Edison e Pythagoras cedem as refeições à York** — a função original dela era comer, dormir e ir ao banheiro PELOS outros. Explica a preguiça e o ressentimento.
- **Todos destruíram as peças de reposição da York.** Ela sabe e faz piada amarga com isso.

**Números por Satélite** (canon / trejeitos / exemplos): atlas 27/22/16 · edison 32/22/16 · lilith 35/21/16 · pythagoras 29/22/15 · shaka 34/22/16 · stella 33/22/16 · york 32/22/16. Crescimento aditivo: 606 inserções contra 89 linhas reescritas em versão ampliada nos agentes.

### Armadilhas desta sessão

- ⚠️ **A dosagem da voz nunca foi observada em produção.** Todo o risco novo está aí. Cada `speech_register` traz a regra explícita "se o arcaísmo começar a comer a clareza, corta o arcaísmo, nunca a clareza", mas quem decide se pegou é o Fernando lendo no Telegram. **Se soar excessivo, o ajuste é nessa chave, não no código.**
- ⚠️ **A York precisa continuar confiável.** No cânone ela é a traidora que matou os irmãos; aqui ela cuida do dinheiro do Fernando. O briefing exigiu que a traição entrasse só como PASSADO — matéria de humor amargo e de argumento profissional (é por isso que ela insiste em 10-15% de imprevisto no orçamento) — nunca como comportamento atual. `when_asked_about_betrayal` proíbe usar isso como ameaça. **Se um dia ela mentir sobre número ou ameaçar, é regressão de personagem, não charme.**
- **`yaml.safe_load` do bloco ```yaml inteiro falha em TODOS os agentes, e SEMPRE falhou.** A causa é `activation-instructions`, que é prosa com `:` (a linha do `confidence: baixa`). O loader de produção (`satellites._yaml_block`) corta tudo antes de `\nagent:` justamente por isso. Ao validar um agente, use o loader do projeto, não `safe_load` do bloco cru — os 7 subagentes desta sessão tropeçaram nisso e todos chegaram à mesma conclusão.
- **O fandom bloqueia o WebFetch com HTTP 402.** As páginas foram baixadas com trafilatura de dentro do container, que tem rede: `docker compose exec -T vegapunk python -c "import trafilatura; ..."`. As 7 estão em `tmp/wiki/*.txt` (não versionado) se precisar reconsultar.
- **O sync copia `squads/` inteiro para o FURY.** Nesta sessão as 3 stories do kit foram commitadas no FURY ANTES de existirem no Vegapunk, porque o rsync não pergunta se a fonte rastreia o arquivo. Ficou uma inversão por alguns minutos: o espelho tinha o que a fonte não tinha. **Commite a fonte primeiro.**

## Sessão 8b (2026-09-04) — privacidade do OpenRouter fechada e verificada

O Fernando mandou a página de configurações de privacidade da conta. Ela é autenticada (o WebFetch só vê a tela de login), então a doc pública equivalente foi arquivada no Punk Records pelo Shaka: `punk_records/article/2026-09-04_openrouter-politica-de-treino-retencao-de-logs-e-roteamento_a7e3e9a3d6ba.md`. **As `## Notas manuais` desse item guardam o estado da conta antes e depois, e a verificação — leia lá antes de mexer.**

**O que mudou na conta:** o toggle `Allow free endpoints that train on request data` estava LIGADO e foi desligado; `Zero Data Retention · Non-frontier` foi ligado. Os demais toggles de treino já estavam fechados. Roteamento regional exige plano Business.

**Por que isso importava:** o bot roda em `google/gemini-3.7-flash`, que é pago, então nada passava por endpoint gratuito hoje. O risco era o experimento futuro — o item do catálogo de modelos de 03/09 sugere testar um `:free` multimodal, e naquele dia as transcrições virariam material de treino sem aviso.

**Verificação feita com a chave real, não por suposição** (o ZDR Non-frontier podia ter deixado o modelo do bot sem endpoint):
- `/api/v1/models/user` → 347 modelos elegíveis, `google/gemini-3.7-flash` entre eles.
- Chamada real de inferência → HTTP 200, provedor Google, resposta correta.
- 4 modelos `:free` seguem elegíveis: desligar o toggle exclui os que TREINAM, não todos os gratuitos.

**Captura do dia:** 8 itens do TikTok pelo bot (7 triados, 1 preso em `_pending/`) mais o artigo do OpenRouter. Tudo pushado.

## Sessão 9 (2026-09-05) — capture.py aprendeu a triar — **`8737dbd`**

Feita pelo Fernando sozinho, registrada só no diário do Stella até agora. Dois pushes:
- `9ef54f3` — **16 itens novos** (164 → 180). Lote Akita (benchmarks de LLM, ai-memory, ai-jail, mangá) + GTA 6 + um lote LGPD de 10 links que rendeu só 2 úteis: 2 duplicatas recusadas pelo próprio script, 4 descartes por redundância (a 13.853 é lei de diferença; o compilado é 2ª cópia; o MPF confessa copiar o Serpro; o do DF é para órgão público) e 2 páginas sem texto no HTML (Sebrae, índice do MPF).
- `8737dbd` — **`capture.py --triage`** no `enrich` e **subcomando `triage <id> <decisão>`**. Ambos chamam `pipeline.triage`, a MESMA função dos botões do Telegram — sem lógica duplicada. A triagem deixou de ser exclusiva do Telegram, e foi isso que tornou possível o lote da sessão 10.

## Sessão 10 (2026-09-07) — 13 capturas e a fila zerada — **`0783fec`**

**27 commits pushados**, vault **170 → 182 itens**, fila de triagem **14 → 0**. Nenhuma linha de `src/` mudou, então **sem tag**.

**O dia formou um tema sozinho, em duas metades.** Os 13 itens não foram escolhidos por assunto, mas convergiram:

*Como se VENDE um site para negócio local* — e agora há **quatro preços observados** no Punk Records, que é a primeira faixa de mercado real do vault:

| Valor | Caso | Prova |
|---|---|---|
| R$ 250 | lavagem automotiva | **fechado no print** |
| R$ 450 | hortifruti | proposto, terminou em "vou pensar" |
| R$ 680 | clínica odontológica (31/08) | relatado |
| R$ 1.250 | hamburgueria | **Pix recebido no print** |

Dois padrões repetem nos que fecharam: o preço **nunca** aparece antes do aceite da proposta, e a proposta é uma **lista de entregáveis nomeados**, não descrição genérica de site.

*Como se CONSTRÓI um sem cara de IA* — três itens com processo de verdade:
- **AI slop** ([item](punk_records/youtube/2026-09-07_fugir-do-ai-slop-no-claude-code-referencias-skills-de-design_HtbZQaDjUvM.md)): o problema não é feiura, é uniformidade — quando tudo tem a mesma cara, o cliente acha que qualquer um entrega igual e o preço cai. Processo: biblioteca de referências que case com o TIPO de cliente (Awwwards filtrado, Dribbble, Pinterest) → skills de design (**Impeccable e Taste conflitam se ativadas juntas; nomear uma no prompt**) → iterar em 3 versões antes de refinar. Truque: baixar o código-fonte do site de referência e anexar ao brief.
- **Cérebro do projeto** ([item](punk_records/youtube/2026-09-07_cerebro-do-projeto-no-claude-code-claude-md-spec-e-memoria-i_KstiVYfjf58.md)): confirmação externa da nossa própria arquitetura — regras (`CLAUDE.md`), spec e memória em arquivos separados **porque cada um muda num ritmo diferente**. Traz a regra que NÃO temos (item 1 da lista acima) e dois padrões operacionais: um `imagens.md` que devolve prompts com proporção em vez de pedir foto a foto, e devolver o print do PageSpeed ao agente para ele corrigir desempenho.
- **Claude Design** ([item](punk_records/youtube/2026-09-07_claude-design-brief-em-vez-de-prompt-corrido-exportar-html-e_7TSnITL-LfY.md)): o campo espera **brief em 5 campos** (tipo de página, público-alvo, objetivo, estilo, seções obrigatórias), não texto corrido. Os 5 campos viram o questionário da reunião com o cliente; exportar em PDF aprova o layout antes de gastar com domínio.

**Custo do lote: quase zero.** Os resumos foram escritos pela sessão do Claude Code (`*capture`), não pelo OpenRouter. Únicos gastos: 3 carrosséis de TikTok que passam por `enrich.read_slides()` (~5,4k tokens de entrada cada, ≈ US$ 0,01 no total). Os 6 vídeos do YouTube vieram com **legenda pronta** — Whisper não rodou.

### A triagem em lote pelo Shaka (14 vereditos)

3 `apply_saas` · 3 `apply_client` · 7 `archive` · 1 `discard`. Aplicados por `capture.py triage`, um commit `kb:` cada, zero OpenRouter.

**O Shaka recusou duas marcações que pareciam óbvias, e a razão vale como regra:**
1. **Loja virtual da Hostinger → `archive`**, não `apply_client`. A lista de requisitos é boa, mas a aplicação depende de uma decisão não tomada (o cliente vende online?). Marcar `apply_*` com aplicação condicional é inflar a fila com aplicação vaga — o defeito que o `*audit-triage` existe para caçar.
2. **Escada de preço (R$ 200→500→1.000→2.000) → `archive`.** Uma escada afirmada por um afiliado não manda em quatro preços observados.

**Todos os 13 itens de hoje são conteúdo de afiliado ou funil de curso** (Hostinger, HostGator, cursos de Claude Code). Isso está marcado no campo `tools` e nos `key_points` de cada um — o resumo separa o que é processo do que é anúncio. O único `discard` foi o método que manda **baixar foto do Instagram do prospecto** para peça comercial: fonte superada por itens melhores, com risco de uso de imagem de terceiro embutido.

## Sessão 10b (2026-09-07, noite) — preço do serviço, regra de escopo e a norma do CFM

**O Fernando declarou que vai vender sites**, e ao reler o vault ficou claro que o levantamento começou em **26/08**, não hoje: são 19 itens `apply_client` sobre venda, prospecção, estrutura de página e design. Ele estava fazendo pesquisa de mercado sem declarar a intenção.

### A precificação da York (`*pricing`)

**O benchmark brasileiro derruba os preços dos vídeos.** Cinco fontes ([BluePaper](https://bluepaper.io/blog/quanto-custa-landing-page), [BQHost](https://bqhost.com.br/lp/quanto-custa-uma-landing-page/), [Safira](https://safiradesign.com.br/blog/quanto-custa-uma-landing-page-2026/), [Vibe](https://govibe.digital/quanto-custa-criacao-de-site-para-empresa-em-2026/), [BigData University](https://bigdatauniversity.com.br/quanto-cobrar-por-uma-landing-page-2026/)) põem landing para pequena empresa entre **R$ 1.500 e R$ 5.000**. Os preços do TikTok (R$ 250 a R$ 1.250) estão **abaixo do piso de mercado**.

**A conta que importa, e que nenhum vídeo mostra:** ~4h de produção + **~5h de prospecção** = **~9h por cliente FECHADO**. A prospecção custa mais que a produção. A R$ 250, a hora do Fernando vale R$ 28.

**Princípio de preço que explica os dados do vault:** cobrar pelo **ticket do cliente do cliente**, não pelo número de seções. Hortifruti (ticket R$ 80) hesitou em R$ 450; clínica odontológica (ticket R$ 500-3.000) fechou R$ 680 em cinco minutos.

| Degrau | Preço | Observação |
|---|---|---|
| Entrada | **grátis** | a prévia pronta ANTES do preço — presente em todos os casos que fecharam |
| Núcleo | R$ 1.500 | piso do mercado brasileiro |
| Premium | R$ 2.800 | com agendamento, SEO local, Google Meu Negócio |
| Recorrência | R$ 200/mês | **o Fernando adiou**, mas fica "a combinar" escrito na proposta |

**Decisão dele, registrada:** os **três primeiros a preço de custo** (só o domínio, ~R$ 40), porque são projetos-treino. A York aceitou e propôs o enquadramento de **preço de portfólio com contrapartida** (autorização de uso + depoimento + indicação), que ancora o R$ 1.500 sem parecer desconto.

**Custo real por site: R$ 40** — hospedagem é zero (Vercel/Netlify/Cloudflare Pages) e o **botão de WhatsApp é um link `wa.me`, sem API e sem custo**. A API oficial só serve para automação, que não está no escopo.

**Domínio: sempre no CNPJ do cliente.** Um `.com.br` exige CPF/CNPJ brasileiro — registrar no próprio nome torna o Fernando dono legal do domínio do cliente, com risco de parecer refém e de o site morrer se ele esquecer de renovar. Cobrar a configuração, nunca a posse.

### A norma que ninguém tinha visto: publicidade médica

O Punk Records **não tinha nada** sobre isso antes desta sessão. Sete fontes capturadas, das quais duas primárias.

**Resolução CFM nº 2.336/2023**, vigente desde **11/03/2024** (substituiu a 1.974/2011). Site de médico é "rede própria" e está integralmente sujeito a ela. **Três regras quebram uma landing gerada por IA:**

1. **Identificação obrigatória na PÁGINA PRINCIPAL** (art. 4º e 6º): nome + a palavra **MÉDICO/MÉDICA** + número do CRM + RQE da especialidade. E o **Manual da Codame** acrescenta uma exigência de DESIGN: **sem diferença de fonte, tamanho e cor** entre essas informações. Nome em display grande com CRM cinza miúdo no rodapé descumpre — e é o padrão que todo gerador produz.
2. **Vedado garantir, prometer ou INSINUAR bons resultados** (art. 11, XII). "Insinuar" alcança headline persuasiva comum. Também é vedado causar medo ou insegurança, o que derruba copy de dor. E vale para **símbolo, ícone, selo e slogan**, não só texto.
3. **Máximo de DUAS especialidades**, cada uma com seu RQE, e só as reconhecidas na Resolução CFM 2.330/2023 (o CRM-PR cita Medicina Estética como exemplo do que NÃO é especialidade).

**O que a norma nova PERMITE** e a antiga proibia: divulgar preço da consulta e formas de pagamento, campanhas promocionais, fotos do consultório e da equipe, imagem de paciente com finalidade educativa. Muito conteúdo na internet ainda ensina pela norma revogada.

**O risco é do médico, não do fornecedor** — quem responde ao CRM é ela. Mas o prejuízo volta: página reprovada custa a cliente, o depoimento e a indicação.

### Armadilha técnica nova

**O `capture.py` não extrai PDF pela URL.** O `extract_article` usa trafilatura, que devolve ERR-004 em PDF. O caminho que funcionou, e que deve virar rotina para norma e documento oficial:

```python
# dentro do container
urllib.request.urlopen(req)  # baixar o PDF (User-Agent de navegador)
from vegapunk.extract import extract_document
extract_document(Path("arquivo.pdf"))  # pypdf converte
# depois: capture.py extract <url> --text arquivo.txt --title "..." --sat shaka
```
Funcionou com 46k e 146k chars. **Atenção**: a URL já existe no banco como `extraction_failed`, e o `extract` recusa duplicata — é preciso apagar o item (`item_events` ANTES de `knowledge_items`, por causa da FK) e remover o `.md` órfão de `_pending/`.

**Listas gigantes também não passam pelo trafilatura**: `awesome-mcp-servers` (1,5 MB de README) e `awesome-claude-code` devolveram só navegação do GitHub. Solução usada: baixar o README cru, condensar para o **mapa estrutural** (seções + contagem) e alimentar por `--text`. Guardar 3.793 links que mudam toda semana incharia o vault sem ganho.

## Sessão 11 (2026-09-09) — direito autoral, Princípio 0 e o clonador de sites — **`67d380d` pushado**

Dia inteiro pelo Claude Code, sem tocar em `src/`. Nenhuma tag nova, nenhum agente alterado (FURY não precisou de sync).

### O que entrou no Punk Records: 17 itens

**Bloco 1 — venda de sites (10 itens, todos `apply_client` salvo indicado):**

| item | o que carrega |
|---|---|
| [Quatro formas de faturar com IA](punk_records/youtube/2026-09-09_quatro-formas-de-faturar-com-ia-sites-dashboards-automacao-d_Qoe61lzBQSk.md) | faixa de mercado R$ 1.000–5.000 por site contra ~R$ 150/mês de custo; +R$ 10k sites, +R$ 8k dashboards, +R$ 6k automação |
| [Parar de vender site](punk_records/youtube/2026-09-09_parar-de-vender-site-perguntar-a-dor-e-nao-dar-nome-a-soluca_bQeOZczf5q0.md) | **não dar nome à solução** — nomear a categoria (site, CRM, N8N) transfere a conversa de qualidade para preço. Escada real: LP R$ 500 → IA de atendimento R$ 2–2,5k → painel R$ 6k = +R$ 10k no mesmo cliente |
| [Como vender o primeiro site](punk_records/tiktok/2026-09-09_como-vender-o-primeiro-site-prospeccao-no-google-maps-nicho_7683264480263884050.md) | Google Maps, fugir de advogado/dentista, 50% adiantado, desconto **somado a benefício** |
| [Parar de mostrar portfólio](punk_records/tiktok/2026-09-09_parar-de-mostrar-portfolio-e-mandar-o-site-pronto-no-primeir_7683569617746496788.md) | filtrar por cidade e nicho **negócios que ainda não têm site** — a origem de lead que faltava |
| [Sete repositórios open source](punk_records/tiktok/2026-09-09_sete-repositorios-open-source-para-implantar-e-cobrar-como-s_7681261206534917394.md) | modelo Red Hat; licenças conferidas; **changedetection.io** e **PaddleOCR** são os dois vendáveis a negócio local |
| [Erros de SEO](punk_records/tiktok/2026-09-09_lista-de-erros-que-impedem-um-site-de-ser-encontrado-no-goog_7683300020581453074.md) | Google Meu Negócio abandonado e sem avaliações — atinge a VDC, cujo endereço no Google está errado |
| [Clientes internacionais](punk_records/tiktok/2026-09-09_vender-sites-feitos-com-ia-para-clientes-internacionais-vend_7682823642698337557.md) | vitrine de infoproduto; só a tática de demo se aproveita |
| [AI Website Cloner Template](punk_records/article/2026-09-09_ai-website-cloner-template-clonar-qualquer-site-em-next-js-p_2a59fbf9b429.md) | o repo que foi instalado — ver seção própria abaixo |
| [5 testes de segurança sem código](punk_records/tiktok/2026-09-09_5-testes-de-seguranca-em-app-feito-com-ia-sem-escrever-codig_7682949171111922964.md) | **`apply_saas`** — checklist de 10 min: número na URL, 20 senhas erradas, `sk-` no F12, preço no inspetor, link de arquivo sem login |
| [ECC — 68 agentes](punk_records/tiktok/2026-09-09_ecc-pacote-que-instala-68-agentes-e-286-skills-no-assistente_7683346049486015762.md) | **`archive`** — as 254k estrelas alegadas não conferem com a realidade; guardado como registro de um padrão que vai voltar |

**Bloco 2 — direito autoral (7 itens, mandados por ele às 21h):** ver a seção "A correção da sessão 11" no topo. Os quatro que valem:
[Jusbrasil](punk_records/article/2026-09-09_copy-paste-de-websites-violacao-ao-direito-do-autor-jusbrasi_9d0aa61c0500.md) (jurisprudência), [Guia do Senado](punk_records/article/2026-09-09_guia-de-direitos-autorais-do-senado-federal_61e4247615f8.md) (fonte oficial, imagem e banco de imagens), [Avctoris](punk_records/article/2026-09-09_direito-autoral-para-designers-protecao-automatica-registro_b9493ae2aecf.md) (cessão × licença no contrato), [VILAGE](punk_records/article/2026-09-09_direito-autoral-de-logotipo-criado-no-canva-quando-da-e-quan_74120014d534.md) (INPI não checa biblioteca do Canva — registro nasce anulável).
Arquivados: [TermsFeed](punk_records/article/2026-09-09_website-copyright-law-protecao-de-sites-nos-eua-reino-unido_35e0191756a9.md) (lei estrangeira) e [Estadão/TecMundo](punk_records/article/2026-09-09_direito-autoral-para-designers-protecao-automatica-prova-de_c0a312e9a6ae.md) (publieditorial duplicado; guardado pela faixa do STJ). O link do Reddit foi **descartado** — Reddit serve JS e bloqueia extração.

### A convergência que vale mais que qualquer item isolado

**Quatro conteúdos independentes, capturados no mesmo dia, chegaram à mesma conclusão sem se conhecerem: construa a demo ANTES de conversar.** O vídeo do A Vizinhança, o TikTok do Code Nog, o guia "gringa" e o carrossel dos 7 repositórios. Isso deixou de ser dica de criador e virou convergência — o mais perto de evidência que este tipo de material chega. **E o Fernando já executa sem saber:** a landing da VDC existe antes de qualquer contrato.

### O clonador instalado — `~/projetos/ai-website-cloner-template`

`JCodesMore/ai-website-cloner-template`, MIT, 34.114 estrelas e 4.973 forks conferidos na API do GitHub em 09/09. Criado em 13/03/2026, último release v0.4.0 em 10/08, **13 contribuidores, 2 issues e 2 PRs abertos** — projeto viral com manutenção de uma pessoa só.

| | |
|---|---|
| Estado | `npm install` feito, **build verde**, `npm audit` = **0 vulnerabilidades** |
| Correção aplicada | Next.js **16.3.0 → 16.3.4** (patch). O 16.3.0 tinha RCE crítico não autenticado (servidor Windows e API de otimização de imagem com AVIF) |
| **Bloqueio** | **não roda sem MCP de navegador** (Chrome MCP, Playwright MCP…). Nenhum está configurado — só `agentmemory` |
| Saída | projeto **Next.js 16 + React 19 + Tailwind v4 + shadcn**, não HTML estático |
| Git | clonado direto (o README pede "Use this template"); `origin` ainda aponta para o repo original. `git remote remove origin` resolve se incomodar |

**Como funciona:** cinco fases — reconhecimento (prints em 3 tamanhos, tokens de design, varredura de interação) → fundação (CSS global, download de todos os ativos) → specs por componente com `getComputedStyle()` exato → construção paralela por agentes em **worktrees do git** → montagem com diff visual. A regra interna: se o builder precisar adivinhar uma cor, a extração falhou.

**Três coisas a lembrar:**
- **`SECURITY.md` avisa que projetos criados do template NÃO recebem correções.** O mantenedor do clone é o Fernando.
- **O patrocinador está dentro das instruções do agente** (linha 257 do `SKILL.md`): fallback opcional de geração de imagem pela **Atlas Cloud**, exige `ATLASCLOUD_API_KEY` que ele não tem, vedado para logo/marca. Na prática não dispara. Registrado por transparência.
- **Custo de token alto** — dispara vários agentes em paralelo, um por seção.

### Princípio 0 gravado — ética por AVISO, não por bloqueio

Gravado em **`~/.claude/CLAUDE.md`**, como primeira seção do arquivo, e na memória do projeto (`principio-0-etica-avisar-nao-bloquear.md`).

**Decisão do Fernando, textual:** *"NUNCA EVITE, mas se acontecer de clonar objetos que atacam o princípio 0, avisar SEMPRE. Eu falo para não evitar, para não correr o risco de mexer no funcionamento da skill de clonagem."*

Logo: a skill roda inteira, na fidelidade dela. O agente **reporta depois** o que veio protegido — textos/copy, fotos e ilustrações, logo e nome, composição visual distintiva — antes de publicar. A troca é decisão dele.

⚠️ **Não escrever a regra dentro de `ai-website-cloner-template/`** (nem `SKILL.md`, nem `AGENTS.md`, nem `CLAUDE.md`). Qualquer texto ali é lido pelo agente durante a clonagem e pode alterar o comportamento — foi exatamente o que ele pediu para evitar.

### Armadilhas novas descobertas nesta sessão

- **Reddit não extrai.** Serve página em JavaScript; `.json`, `old.reddit` e strip de HTML falharam todos. Caminho: colar o texto e usar `--text`.
- **`capture.py triage` recusa item com `status=extraction_failed`** ("Já triado"). Para descartar, é preciso escrever direto no banco: `update knowledge_items set triage_decision='discard', status='discarded' where id=...` e apagar o `.md` de `_pending/`.
- **O schema do enrichment tem `topics` com máximo de 7.** Passar 8 dá erro Pydantic `too_long` sem dizer qual campo. `key_points` ≤ 10, `tags` ≤ 8, `tools` ≤ 10.
- **A tabela `knowledge_items` não tem coluna `triage`** — o nome é `triage_decision`.

### Estado do laboratório de design (pasta vizinha, não é deste repo)

`~/projetos/testes-skills-design/` avançou em 09/09 **fora desta sessão** (ele trabalhou em paralelo): rodada 5 da Taste com a identidade visual da VDC (teal `#008096` + amber `#ffa300`, detector 6→5) e uma **versão Impeccable v2 "Placa de Obra" com 0 achados**. A skill Impeccable foi **desinstalada**, mas o detector foi salvo em `lab-taste/ferramentas/detector`. ⚠️ **A skill global `ui-ux-pro-max` continua desligada** em `~/.claude/skills-off/` — restaurar quando os testes acabarem.

Com o clonador, a VDC passará a ter **três versões** pela mesma régua: Taste v5 (5), Impeccable v2 (0), clone (?).

## Sessão 12 (2026-09-11, manhã/tarde) — lote de 8 links de venda e design — **`d58b88b` pushado**

Nenhuma linha de `src/` tocada.

### O que entrou: 8 itens (5 apply_client, 3 archive)

| item | o que carrega |
|---|---|
| [Gauntlet Loop](punk_records/youtube/2026-09-10_gauntlet-loop-construtor-tres-criticos-independentes-para-de_jvfllKWDqRk.md) | **o mais valioso do lote** — construtor + 3 críticos independentes (briefing, sistema, visual). Skill gratuita. Custo medido: US$ 3,19 num HTML, US$ 7,54 num site |
| [Claude Design em 5 níveis](punk_records/youtube/2026-09-10_claude-design-em-5-niveis-do-prompt-solto-ao-design-system-r_BKt3WKwAk8U.md) | o nível 3 (design system exportável) é o que o Fernando ainda não tem |
| [IA de atendimento no WhatsApp](punk_records/youtube/2026-09-10_como-criar-e-vender-agentes-de-ia-no-whatsapp-com-n8n-e-clau_jjMnQDAc5Mo.md) | R$ 2.500–7.000/instalação, custo R$ 250/mês **no CNPJ do cliente**, skill Genesis grátis. ⚠️ Notas manuais têm o alerta CFM+LGPD para a psiquiatra |
| [Script de cold call](punk_records/tiktok/2026-09-10_script-de-cold-calling-para-venda-de-sites-no-mercado-intern_7683167461994220808.md) | o roteiro da ligação em 7 passos, destrinchado nas Notas manuais |
| [Checklist pós-lançamento](punk_records/tiktok/2026-09-10_checklist-basico-de-pos-lancamento-de-landing-page-open-grap_7678514322129063186.md) | Open Graph, metadados, Search Console |
| 3 itens "vender pra gringa" | **archive** — vitrine de infoproduto; aplicação depende de decisão não tomada |

### O que mudou no entendimento

**O Gauntlet Loop fecha o buraco apontado na análise do "prompt mestre"** (feita na sessão 11, a pedido do Fernando): um agente constrói, três críticos independentes avaliam — um checa fidelidade ao pedido, outro cor/fonte/identidade, o terceiro compara com a referência. O modelo deixa de julgar o próprio trabalho. É a automação das cinco rodadas manuais da landing da VDC, e dá para medir contra a régua que já existe (`lab-taste/ferramentas/detector`).

⚠️ O vídeo do Gauntlet Loop **usa o site da Apple como referência** e defende textualmente copiar o que já funciona — exatamente o que a jurisprudência da sessão 11 condena. Usar a técnica, trocar o alvo.

**Falta o design system da VDC.** A identidade (teal `#008096`, amber `#ffa300`) está em prosa neste HANDOFF, não num arquivo exportável. O nível 3 do Claude Design resolve em ~5 min e vira insumo do crítico de sistema do loop.

**Confirmação independente da paleta:** na sessão 11, o Playwright mediu o header do vdcsolar.com em `rgb(0,128,150)` = `#008096` — exatamente o teal que o Fernando havia extraído do logo por medição de pixel. Duas medições, caminhos diferentes, mesmo valor.

### Pendências abertas desta sessão

- O clonador (`~/projetos/ai-website-cloner-template`) segue **pronto e não usado**. Playwright verificado funcionando no vdcsolar.com (título, stack WordPress+Elementor, hero com PNG tingido). Falta rodar `/clone-website`.
- O Fernando disse que ia clonar **outro site**, não a VDC — alvo ainda não informado. Quando informar: se não for site de cliente dele, aplicar o Princípio 0 (avisar antes e depois o que veio protegido).

### Tarde: o Cofre de Abordagens e o dado de campo do mercado

Entraram **dois documentos** que mudam o patamar do que o vault tem sobre venda de sites.

**1. [Cofre de Abordagens (MazyOS)](punk_records/document/2026-09-11_cofre-de-abordagens-mazyos-50-mensagens-de-prospeccao-100-fi_16284fb93b86.md)** — produto pago, comprado pelo Fernando. Guardado **com texto integral** (210 mil caracteres, 111 páginas). Conferido peça por peça: 55 códigos de mensagem (WA 13/13, FU 8/8, GK 5/5, DM 9/9, EM 6/6, OBJ 9/9, AU 5/5) e **100/100 fichas de nicho**, mais 157 blocos "COPIE DAQUI", combos por setor, Top 10, regra de ouro, limites anti-ban e Plano de 14 Dias.

⚠️ **O PDF trunca em 150 mil caracteres na extração.** Os 39.509 caracteres finais (parte dos setores 9/10, tabela de Combos e Plano de 14 Dias) foram recuperados do texto bruto e **colados na íntegra dentro de `## Notas manuais`**, com aviso. Por isso "Plano de 14 Dias" aparece duas vezes no arquivo — não é duplicata por erro.

**2. [Grupo Code Makers](punk_records/document/2026-09-11_grupo-code-makers-whatsapp-679-membros-precos-praticados-lim_739f9436c388.md)** — destilação de ~4.000 mensagens de um grupo de WhatsApp com 679 vendedores de site, janela de 08 a 11/09. **É o primeiro dado de preço praticado que o vault tem**, e é auto-relato de quem vendeu, não opinião de criador de conteúdo.

O que ficou registrado: vendas fechadas de R$ 120 a **R$ 1.890** (energia solar, presencial, primeira abordagem), consenso de **R$ 500–800** para landing simples, e o dado mais consistente de todos — **teto de 30 a 50 disparos/dia no WhatsApp**, com o gatilho do ban sendo a *mensagem repetida*, não o volume. Funil médio: 30 mensagens → 1 a 2 vendas.

⚠️ **O anexo chegou só no contexto, não em disco.** Foi gravada a destilação em 8 blocos, não o chat bruto. Se o Fernando quiser o dump literal um dia, precisa reenviar o arquivo.

**A descoberta que vale mais que o preço:** o grupo apontou, sem saber com quem falava, que **marmoraria, vidraçaria e serralheria** são o melhor nicho — *"um trabalho deles paga um site bom"*. O Fernando é **engenheiro civil**: fala a linguagem técnica desses clientes. É a única vantagem dele que nenhum dos 679 consegue copiar, e não depende de preço.

### Material entregue ao grupo (não commitado)

Ele pediu um resumo para devolver à comunidade. Gerados em **`tmp/compartilhar/`**: `code-makers-resumo.md` (11 KB) e `.txt` (12 KB), mesmo conteúdo em 9 seções. **Escritos sem citar nome, sem print e sem julgar ninguém** — pedido explícito dele, em maiúsculas. Os avisos de segurança (extensões maliciosas, LGPD, referência × cópia) foram enquadrados como proteção do próprio vendedor, nunca como sermão.

Está em `tmp/` de propósito: é entregável pontual, não faz parte do repo.

### Decisão fechada nesta sessão

**O vault é de uso exclusivo do Fernando** (reverte a decisão de 01/09 de compartilhar com amigos). Consequências registradas em "Decisões fechadas": (a) produto pago pode ser guardado com texto integral, porque não há redistribuição; (b) a **Story 2a NÃO foi suspensa** — perdeu a razão "amigos commitando", mantém "reinstalar em outra máquina" (agora crítica: o vault virou o único backup) e o bug do INDEX; (c) **Stories 2b e 2c precisam ser relidas** sob essa ótica antes de entrarem na fila — nasceram do mesmo pedido de 01/09 e não foram abertas.

### Armadilha nova

**`git push` com produto pago dentro é barrado pelo classificador do Claude Code.** Aconteceu duas vezes (motivo `[Out-of-Place Publication]`), porque o commit levava ~200 KB do texto integral de um produto comprado para um remoto GitHub. **A saída é o Fernando rodar o `git push` ele mesmo** — é a regra do projeto de qualquer forma. Não insistir, não tentar contornar: passar o comando e explicar.

## Sessão 13 (2026-09-11, noite) — CAPTCHA, o método do Mazzeo e o primeiro alvo real de venda — **`266d567` pushado**

Sessão de captura e de estratégia de venda. **Nenhuma linha de `src/` tocada**; dois pushes de conteúdo (`36b72e1` e `266d567`), 144/144 verdes antes de cada um.

### O que entrou: 6 itens (241 → 247)

**Lote 1 — CAPTCHA (4 links, 3 itens).** [Moni Naor](punk_records/article/2026-09-11_moni-naor-o-criptografo-que-teve-a-ideia-do-captcha-antes-do_6ff294c5147c.md), [captcha.net](punk_records/article/2026-09-11_captcha-net-o-site-oficial-do-captcha-aplicacoes-diretrizes_57f98e6b71e3.md) e o [paper do Eurocrypt 2003](punk_records/article/2026-09-11_captcha-using-hard-ai-problems-for-security-eurocrypt-2003-o_75b293707f6f.md). O quarto link era o mesmo paper em PDF local e **não virou item duplicado**.

**Lote 2 — venda de sites (3 links, 3 itens).** O pesado é o [vídeo do Vagner Mazzeo](punk_records/youtube/2026-09-11_vagner-mazzeo-google-ads-de-cliente-real-montado-do-zero-com_KUf-vS_gSZo.md) — o mesmo autor do Cofre — montando o Google Ads de um cliente real de climatização com Claude Code, pacote **site + Ads por R$ 5.000**. Mais dois TikToks: [MXC sobre sitemap/robots/llms.txt](punk_records/tiktok/2026-09-11_tiktok-mxc-digital-site-bonito-feito-so-com-ia-sem-sitemap-r_7679994027420208391.md) e [banco de elementos visuais com copiar-para-IA](punk_records/tiktok/2026-09-11_tiktok-banco-gratuito-de-elementos-visuais-prontos-com-botao_7671643736924835093.md) (lacuna marcada: **o vídeo não diz o nome da ferramenta**, só mostra na tela).

### O achado do vídeo do Mazzeo (vale para o nicho de construção civil)

A IA gerou 52 sementes de palavra-chave; a validação com dado real (DataForSEO, **US$ 0,18 a consulta inteira**) derrubou quase todas — **inclusive a de maior volume**. "Instalação de ar-condicionado" tem 3.600 buscas/mês e traz residencial de 12.000 BTU procurando serviço de R$ 500, para uma empresa que faz obra com ART. "Retrofit" e "alto padrão": **zero busca**. O mercado digita **termo técnico**, não nome de segmento. Sobraram PMOC, VRF/VRV e dutado (~900 buscas/mês, CPC R$ 5). Outras peças do método: pasta por cliente com o contexto da empresa em arquivo, **uma landing page por anúncio gerada por subagentes** (ele chama de "o ouro"), CSV → Google Ads Editor, e conversão no GTM **antes** de ativar.

### A virada de nicho: do diploma para a rua

A recomendação inicial (vidraçaria, serralheria, climatização, laudos — onde a formação de engenheiro é argumento) **foi revista pelo próprio Fernando**: ele mora em **Vitória da Conquista (BA)**, onde há muita cafeteria, lanchonete e açaiteria, e quer começar por quem consegue **observar**. Isso não contraria o Cofre — **aplica a regra dele**: *"comece pelo nicho que você consegue observar hoje; observação real vale mais que nicho perfeito."* Duas das três escolhas dele estão no **Top 10 do próprio Cofre** (hamburgueria nº 2, confeitaria nº 3), e as fichas são N-021, N-024 (açaíteria) e N-025 (cafeteria), todas **acesso 3/3**, ticket R$ 500–1.500.

Tensão registrada entre as fontes: o Grupo Code Makers marca "comércio de comida" como nicho que **trava**. O motivo importa — travam porque chegam vendendo **site**, e o dono já tem Instagram e iFood. Vendendo **canal próprio sem comissão** (hamburgueria) ou **cliente que volta no dia frio** (açaiteria), a dor existe. Regra do setor: **abordar fora do pico, 15h–17h é a janela de ouro**; objeção típica **OBJ-02 "tá caro"**.

### O primeiro alvo real: Jardins Café (Vitória da Conquista)

Fernando foi ao local, **pagou R$ 65 no buffet livre** e trouxe prints. O que os prints provam: **não têm site próprio** (o botão "Site" do Google aponta para o Pop Pedidos, plataforma de terceiro), o **Google não tem o telefone deles**, e o negócio é forte — **32,6 mil seguidores, 621 posts, 429 avaliações com 4,5★**, pico sexta às 18h.

**A Lilith atacou a abordagem (a pedido dele, com fim educativo) e derrubou os dois achados principais:**

1. **O cardápio "com telefone de Fortaleza" provavelmente não é deles.** Logo diferente (círculo "café·café·café" contra a serifa do Jardins), rua de Fortaleza, DDD 85, cardápio de pizzas e massas. É **outro Jardins Café**, e o Google embaralhou. Se ele afirmar que o cardápio é deles e não for, a abordagem morre no primeiro balão.
2. **Os "quatro endereços divergentes" são provavelmente dois.** O print de satélite mostra o Jardins **na esquina de Av. Oscar Silva com Av. Olívia Flores** — prédio de esquina tem duas faces. Sobra divergência de um número (704 × 705), que é erro de agregador, não dor de dono.

Outros modos de falha listados: a dor da ficha N-025 não se aplica a quem tem 32 mil seguidores locais; as artes profissionais do feed indicam **agência ou social media já contratado** (OBJ-03); o Pop Pedidos pode ser contrato pago e ativo; e prévia completa entregue de graça, sem nada adiantado e sem contrato, é desenho que fica com o cliente.

**O que sobreviveu ao ataque:** ele é cliente pagante e foi lá (credencial que nenhum dos 679 do grupo tem); eles realmente não têm site próprio (fato verificável); e a **versão-pergunta** da abordagem — *"esse cardápio é de vocês ou tem outro Jardins por aí?"* — não tem resposta que a derrube.

**A lição transferível, que é o que ele pediu levar:** toda observação de abordagem tem um **dono presumido**. Antes de enviar, perguntar *"e se este achado não for dele?"*. Se a mensagem morre com essa resposta, reescrever como pergunta. **Achado forte com dono errado é pior que achado fraco** — o fraco não desmente ninguém.

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

`activation-instructions` (prosa; inclui CONVERSATION MODE, PERSONAL MEMORY, ABSORBED CAPABILITIES, SOURCE DISCIPLINE, VAULT IS READ-ONLY) → `agent` → `persona_profile` (canon, tom, greeting_anchor, signature_phrases, **`speech_register` e `verbal_tics`** — sessão 8) → `persona` → `vault` → `user_context` → seção própria (`judgement_rubric` Shaka / `attack_patterns` Lilith / `ideation_rules` Edison / `build_rules` Atlas / `ops` York / `routing` Stella) → **`mind`, `relationships`, `conversation`, `quirks`, `examples`, `memory`** (personalidade, sessão 3) → **`absorbed_from`, `absorbed_principles`, `dependencies`** (absorção, sessão 3) → `commands` (originais, depois `# ── absorvidos do FURY ──`, depois `exit`) → `procedures` (originais + absorvidas no fim).

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
| Testes | `PYTHONPATH=src .venv/bin/python -m pytest -q` (144) |
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
- **Repo original privado = vault único compartilhado** (decidido 2026-09-01): amigos entram como collaborators, cada um com bot/tokens/chave próprios, todos commitam `kb:` no mesmo repo. Sem repo-modelo separado; o kit é o próprio repo + importador + INSTALL.
- **Esta pasta é para ESTUDAR; projeto de cliente é em diretório próprio** (decidido 2026-09-07). Aqui: preço, risco, norma, abordagem. Lá: código, deploy, domínio, o site. Não criar arquivo de projeto de cliente aqui nem oferecer `*offer`/`*prd`/`*develop` como se fossem executar nesta pasta.
- **Domínio sempre no CNPJ do cliente** (decidido 2026-09-07): `.com.br` exige CPF/CNPJ, e registrar no próprio nome torna o fornecedor dono legal do domínio alheio. Cobrar a configuração, nunca a posse.
- **Botão `wa.me` em vez de formulário** (decidido 2026-09-07, nos dois primeiros clientes): sem coleta no site, a LGPD do fornecedor deixa de existir. A conversa no WhatsApp é do cliente, que já tem dever próprio de sigilo.
- **Diários por pessoa** (decidido 2026-09-01): `squads/vegapunk/memory/<dono>/` — versionados (backup), sem mistura entre usuários (Story 2b).
- **`apply_*` exige ação concreta e incondicional** (Shaka, 2026-09-07): item cuja aplicação depende de uma decisão ainda não tomada vai para `archive`, não para `apply_client`. Aplicação condicional é aplicação vaga, e é ela que faz a fila de `apply_*` perder o sentido. O item volta a ser candidato no dia em que a decisão for tomada.
- **Link mandado no Claude Code é capturado pelo `*capture`, não pelo bot** (praticado desde 27/08, consolidado em 07/09): o resumo sai da sessão, custo de OpenRouter é zero, e o único gasto residual são os carrosséis de TikTok que passam pelo `read_slides()`. O bot do Telegram continua sendo o caminho para captura em movimento.
- **Princípio 0 — ética por AVISO, nunca por bloqueio** (decidido 2026-09-09, gravado em `~/.claude/CLAUDE.md`): em clonagem de site, a ferramenta roda **inteira**, na fidelidade dela; o agente **avisa depois** o que veio protegido (textos, fotos, logo/nome, composição distintiva) antes de publicar. **Nunca escrever a regra dentro do repositório da ferramenta** — instrução ali é lida durante a execução e pode quebrar o comportamento. Palavras dele: "NUNCA EVITE, mas se acontecer (…) avisar SEMPRE".
- **Layout de site É protegido no Brasil** (corrigido 2026-09-09, com jurisprudência): Lei 9.610/98 art. 7º XIII protege "seleção, organização ou disposição do conteúdo"; TJSP já condenou cópia de HTML "depois de algumas maquiagens". Clonar o site do **próprio cliente** é migração autorizada e está limpo; clonar terceiro e publicar não fica seguro só trocando conteúdo.
- **Vault é de uso exclusivo do Fernando** (decidido 2026-09-11, REVERTE a decisão de 01/09): ele desistiu de compartilhar o Punk Records com amigos. O repositório segue privado e sem collaborators. **Consequências:** (a) produto pago pode ser guardado com texto integral, porque não há redistribuição — foi o caso do Cofre de Abordagens; (b) a **Story 2a NÃO é suspensa** — ela perdeu só a razão "amigos", e mantém as outras duas: reinstalar em outra máquina sem perder o catálogo (agora mais importante, porque o vault virou o único backup) e fechar o bug de design em que item vindo por `git pull` some na regeneração do INDEX; (c) as Stories 2b e 2c devem ser relidas sob essa ótica antes de entrarem na fila.

- **Sem contrato por ora; Pix e acerto por mensagem** (decidido 2026-09-11): o Fernando avaliou a cláusula licença × cessão e decidiu **adiar**, por considerar complicação excessiva no início. A pendência continua real (vender sem cláusula cede os direitos do layout e impede reaproveitar o mesmo modelo) e **não tem conserto retroativo** — mas a decisão é dele, foi tomada com a informação na mão, e não se reabre sem pedido. O risco que resta sob controle dele: **não entregar a prévia completa de graça**.
- **Nicho inicial: alimentação local em Vitória da Conquista** (decidido 2026-09-11, revendo a sugestão de construção civil): cafeteria, lanchonete e açaiteria, porque ele consegue **observar** o negócio pessoalmente — e observação real é a matéria-prima da abordagem. Construção civil (vidraçaria, serralheria, marcenaria, laudos) fica como **segunda onda**, quando o diploma virar argumento de venda. Venda para fora da cidade vem depois, com os casos na mão.

## Armadilhas conhecidas
- **PDF antigo gerado por `dvips` não tem texto extraível** (descoberto 2026-09-11 com o paper do CAPTCHA de 2003): fontes Type3 com codificação própria e sem mapa Unicode — o extrator do bot devolve ERR-004 e o `pdftotext` devolve lixo (`/BV/BT/C8`). **Saída que funcionou:** procurar outra cópia do mesmo documento em outro servidor (a da CMU extraiu limpo), converter com `pdftotext` e alimentar com `capture.py extract <url-original> --text arquivo.txt`, **mantendo a URL que o Fernando mandou** como fonte. O item `extraction_failed` é reaproveitado automaticamente e o arquivo de `_pending/` some sozinho.
- **Campo do `Topic` no JSON de enriquecimento é `detail`, não `description`** (errado duas vezes em 11/09): o Pydantic rejeita com `topics.N.detail Field required`. O contrato impresso em `tmp/capture/<id>.md` mostra o schema completo — conferir ali antes de escrever.
- **Observação de abordagem tem dono presumido** (Lilith, 2026-09-11): antes de mandar qualquer achado a um prospect, perguntar "e se isto não for dele?". Perfil, cardápio ou anúncio com o mesmo nome pode ser de outro estabelecimento em outra cidade. Achado forte com dono errado desmente a mensagem no primeiro balão; a saída é reescrever a afirmação como pergunta.
- **`.env`: NUNCA comentário na mesma linha do valor** (Docker `env_file` não trata `#`; foi a causa do 403 do TikTok). Se aparecer `# cookies.txt (Netscape)...` na raiz, é esse bug.
- TikTok "Unable to extract universal data for rehydration" é intermitente (~40%) → 6 tentativas com espera crescente.
- YouTube legendas: só manuais (pt/en/es) ou auto ORIGINAL (`*-orig`); nunca `pt` de auto-caption (429 → 33 min de Whisper).
- Whisper: `language_detection_segments=4`; áudio com <3 s de fala após VAD é pulado.
- Item `extraction_failed`/`pending_manual` → `punk_records/_pending/`; colar texto em "Notas manuais" e `/reprocess <id>`.
- `yt-dlp` desatualizado é a causa nº 1 de falha: `docker compose build --no-cache`.
- YAML dos agentes: `vocabulary: [..., "aguenta?"]` e `routing: - {need: "...", satellite: x}` precisam ficar assim (com aspas / flow mapping) — foram os dois pontos que quebravam o parser.
- Texto sem link no Telegram agora **custa tokens** (vai ao modelo). Mensagem acidental = uma coxinha.
- Apagar item do banco: `item_events` referencia `knowledge_items` (FK) — deletar os eventos ANTES do item, senão `IntegrityError`.
- `pipeline.triage` só aceita item em status `enriched`: `extraction_failed` não tem caminho de descarte pelo bot — a saída é colar conteúdo em Notas manuais + `/reprocess`, ou delete manual (com a FK acima).
- INDEX.md e `temas/` são regenerados INTEIROS a partir do banco a cada triagem/captura: item que existir só como arquivo (ex.: vindo de `git pull` de outra instalação) some do índice — é o furo que a Story 2a (importador) fecha.
- **Reddit não extrai** (09/09): serve página em JavaScript; `.json`, `old.reddit` e strip de HTML falham todos. Caminho: colar o texto e usar `--text`.
- **Descartar item `extraction_failed`**: `capture.py triage` responde "Já triado" e não faz nada. Escrever no banco: `update knowledge_items set triage_decision='discard', status='discarded', triaged_at=datetime('now') where id=...`, depois apagar o `.md` de `_pending/`. A coluna chama-se `triage_decision`, **não** `triage`.
- **Limites do schema do enrichment**: `topics` ≤ **7**, `key_points` ≤ 10, `tags` ≤ 8, `tools` ≤ 10. Estourar dá erro Pydantic `too_long` **sem dizer qual campo** — conferir o `topics` primeiro.
- **Fila pendente + `docker compose up` = o bot enriquece tudo sozinho E AVISA NO TELEGRAM** (11/09): ao subir o container com itens em `extracted`, a pipeline drena a fila via OpenRouter, os resumos saem do Gemini em vez do Claude Code, **e cada item dispara mensagem dos Satélites no Telegram** — gasta crédito e enche o celular do Fernando à toa. (O silêncio padrão vale para o `*capture` feito daqui; a pipeline do bot tem comportamento próprio.) — e aí `capture.py enrich` recusa ("só itens 'extracted' recebem enriquecimento manual"). Antes de subir o container, rodar `capture.py pending`; se houver fila, enriquecer local primeiro (**o enrich NÃO precisa do container**, só o extract precisa). Recuperação sem refazer: escrever o cruzamento em `## Notas manuais`, que é editável à mão e sobrevive à regeneração.
- **Docker Desktop fechado no Windows derruba o container com exit 127** e o `docker` some do WSL ("could not be found in this WSL 2 distro"). Não é bug do projeto: abrir o Docker Desktop e `docker compose up -d`.
- ✅ RESOLVIDO em 12/09 (v1.8.1) — **`normalize.TRACKING_PARAMS` não cobria os parâmetros novos do Google Ads** (`normalize.py:103` limpa `utm_`, `fbclid`, `gclid`, `igsh`, `si`, `ref`, `mc_cid`, `mc_eid`). **`gad_source`, `gad_campaignid` e `gbraid` sobrevivem** — e como o id do item é o sha1 da URL limpa, a MESMA página vinda de dois anúncios diferentes entra como dois itens. Visto em 07/09 no artigo da Hostinger (`a19b8d1384f3`), que ficou com os três na `canonical_url`.
- **Container morre com `Exited (127)` sem uma linha de log quando o Docker Desktop sobe.** O `restart: unless-stopped` religa cedo demais, antes do ambiente estar pronto. Terceira ocorrência (sessões 4, 6 e 10). Sintoma: link mandado no Telegram não recebe nem o "capturei". Cura: `docker compose up -d` na mão. **Não é o exit 137**, que era o `stop_grace_period` e já foi resolvido.
- **`Enrichment.topics` aceita no máximo 7 itens** (e `tools` 10, `key_points` 10, `tags` 8). Escrever o JSON do `*capture` com 8 tópicos falha no Pydantic DEPOIS da extração — nada se perde, mas custa uma rodada. Conferir antes de rodar `enrich`.
- **PDF pela URL cai em ERR-004**: o `extract_article` usa trafilatura, que não lê PDF. Baixar + `extract.extract_document` (pypdf) + `--text` é o caminho; ver sessão 10b. Se a URL já falhou antes, apagar o item (eventos ANTES do item, FK) e o `.md` de `_pending/`.
- **README gigante do GitHub devolve só navegação**: listas tipo `awesome-*` (1,5 MB) não passam pelo trafilatura. Baixar o raw, condensar para mapa estrutural e usar `--text`. Não guardar listas de link inteiras: envelhecem em dias e incham o vault.
- **A extensão de captura de tela e o `--text` continuam sendo a saída para página em JavaScript**, mas repare: o `*capture` de artigo agora acerta a maioria dos sites de conteúdo (trafilatura + cabeçalhos de Chrome). Os que ainda falham são SPA de vitrine, não artigo.

## Mapa do código
`src/vegapunk/`: `bot.py` (handlers: links → pipeline; texto → chat; comandos de Satélite) → `pipeline.py` (normalize→extract→enrich→persist, retries, triagem, reprocess) → `normalize.py`, `extract.py` (yt-dlp + VTT + faster-whisper + slides TikTok), `enrich.py` (OpenRouter; schema; `read_slides`; `_client()` reutilizado pelo chat), `vault.py` (md + INDEX + git), `db.py` (SQLite + `transition_to`), `config.py` (env), **`satellites.py`** (persona → prompt, vault picker), **`chat.py`** (estado/histórico/reply).
`tests/`: 144 testes; `test_satellites.py` cobre load dos 7, prompt, vault picker, chat state/history/reply (mock), nada-se-perde, dependências existem.

**`scripts/capture.py` — o caminho do Claude Code (sem OpenRouter):**
```
extract <url|arquivo> [--sat id] [--text arq.txt]   → tmp/capture/<id>.md (metadados + TEXTO + contrato JSON)
   (a sessão lê esse .md e escreve tmp/capture/<id>.json)
enrich <id> [--telegram] [--triage <decisão>]       → valida com o MESMO Pydantic do bot, grava, índice, temas, commit kb:
triage <id> archive|apply_saas|apply_client|discard → mesma função dos botões (pipeline.triage)
pending                                              → itens extraídos à espera do passo 2
```
Rodar dentro do container (`docker compose exec -T vegapunk python scripts/capture.py …`), que é onde estão yt-dlp, ffmpeg e Whisper. **Silencioso por padrão**; `--telegram` é opt-in. O `id` aceita prefixo. **Duas implementações do contrato `notify`** (aqui e no `bot.py`): quem mexer numa tem de mexer na outra — há teste que lê o arquivo e falha se o `**kw` sumir.

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
- **Comparar gateways de pagamento para receber pelo serviço** (10 itens capturados em 07/09, sem triagem: Asaas, Stripe, Mercado Pago, checkout transparente). York já ofereceu; para R$ 900 pagos uma vez, a resposta provável é Pix direto, sem gateway nenhum.
- MCP de consulta ao vault.
- **Regra de contradição de spec no `CLAUDE.md`** (aprendida em 07/09, item `apply_saas`): *pedido novo que contradiz uma decisão registrada → o agente PARA e avisa antes de alterar*. Uma frase. Protege as "Decisões fechadas" deste arquivo de serem desfeitas por engano numa sessão distraída. É o item 1 da lista de abertura.
- **`imagens.md` como padrão de geração de imagem** (07/09): em vez de pedir foto a foto, um arquivo lê as referências e devolve TODOS os prompts em inglês já com a proporção de cada imagem. Aplicável ao site do cliente. Companheiro: `follow the ref` junto das fotos originais quando o produto sai inconsistente.
- **Devolver o print do PageSpeed ao agente** para ele corrigir desempenho, acessibilidade e SEO — o relatório é a especificação do conserto. Vale como passo final de entrega do site do cliente, junto com o `securityheaders.com` (item `apply_client` de 07/09).
- **Biblioteca de referências por tipo de cliente** (anti-AI-slop): uma pasta com 3 referências que casem com o SEGMENTO, não com o gosto geral. Advocacia e agência criativa não pedem a mesma linguagem. Barato de montar, e é o passo que o item de 07/09 aponta como o mais importante dos três.
- **Integrar o Punk Records com Notion ou Obsidian** (pedido do Fernando em 2026-08-27, a estudar). Obsidian: o vault já é Markdown com frontmatter — basta abrir `punk_records/` como vault; avaliar wikilinks, Dataview sobre `tags`/`applicability`, e não quebrar `## Notas manuais`. Notion: exige sync via API (páginas por item, propriedades = frontmatter); há um doc antigo em `.docs/pacote_telegram_knowledge_bot_v1/06_persistencia_obsidian/`.
