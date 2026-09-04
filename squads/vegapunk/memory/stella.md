# Dr. Vegapunk (Stella) — diário

## Sobre o Fernando
- Engenheiro civil; constrói produtos com Claude Code; não é dev profissional
- Dois projetos: SaaS próprio (quer vender) e site de um cliente

## Diário
- 2026-08-26 · Fernando quer os Satélites com personalidade completa para conversar por Telegram no futuro
- 2026-08-28 · Fernando quer criar um bot do Telegram para cada Satélite e reuni-los em um grupo como próximo passo
- 2026-08-27 · PRD do grupo multi-bot escrito (docs/prd/satelites-multibots-grupo-telegram.md); Lilith atacou, três decisões do Fernando pendentes antes da Story 1 (privacy mode, York só por @menção, dois nomes numa mensagem)
- 2026-08-27 · Checkpoint via *checkpoint: capture.py virou silencioso por padrão (--telegram é opt-in) a pedido do Fernando
- 2026-08-28 · Fernando fechou as 3 decisões do PRD multi-bot: privacy OFF só no bot leitor, roteador decide por contexto (sem exceção para a York), janela de continuidade de 10 min (ele mesmo subiu de 5 para 10)
- 2026-08-28 · Story 1 do PRD não cabia numa sessão de Atlas: dividida em 1a (roteador), 1b (dois bots), 1c (cascata); só a 1a foi entregue pronta
- 2026-08-28 · Regra nova do Fernando: link enviado aqui para leitura vai SEMPRE para o Punk Records via *capture, sem perguntar, salvo pedido contrário (aprendido depois de eu ler 3 páginas do Telegram e só perguntar se capturava)
- 2026-09-01 · Fernando quer o kit de distribuição: repo privado único como vault compartilhado com amigos de confiança (bots e chaves próprios de cada um), reinstalação sem perda, e instalação fácil só das skills. Decidiu: diários por pessoa (memory/fernando/). Stories 2a/2b/2c escritas; 2a pronta para Atlas.

## Sincronizações
- 2026-08-27 · v1.1.0 `40fec7d` — cânone nos 7 Satélites, knowledge/ → punk_records/, README; Lilith achou vault_path antigo no banco, corrigido antes do push; Fernando disse "push" (primeiro *release de teste)
- 2026-08-27 · v1.2.0 `023fa49` — artigos web (trafilatura, texto integral) + Satélites apresentam itens no Telegram (brief/summary, dono do lote); Fernando disse "push"
- 2026-08-27 · v1.3.0 `9be20c5` — Satélites com ferramentas (busca, item, status/custo, git, diário) e comandos * no Telegram; *council ficou fora por custo; Fernando disse "push"
- 2026-08-27 · v1.4.0 `e9b1e5b` — documentos PDF/DOCX/XLSX, fetch como navegador (planalto), Punk Records por tema (temas/), CLAUDE.md global; Fernando disse "push"
- 2026-08-27 · v1.5.0 `b8a560b` — *capture (Punk Records alimentado daqui, zero OpenRouter), stop_grace_period; Fernando disse "push"; FURY espelhado
- 2026-08-27 · v1.5.1 `982f0d4` — capture.py --text + reaproveitar falhos; 71 itens capturados pela sessão sem OpenRouter (vault 107); Fernando disse "push"
- 2026-08-27 · v1.5.2 `fb1bacf` — PRD multi-bot Telegram (docs/prd/), capture.py silencioso por padrão; Fernando disse "push"
- 2026-08-28 · v1.6.0 `74c7528` — roteador do grupo multi-bot (Story 1a) + porteiro do dinheiro (falha aberta corrigida, TELEGRAM_ALLOWED_USER_IDS, grupo desligado por padrão); 7 bots criados pelo Fernando no BotFather e no grupo «Vegapunk»; 12 links antigos recuperados no Punk Records; correção: o Stella é masculino. Lilith AGUENTOU em 3 passadas, Shaka PASS, 97/97; Fernando disse "push"; FURY `ab4ce12`
- 2026-08-28 · v1.7.0 `811710f` — Story 1b: os 6 Satélites como bots que só falam (telegram.Bot puro, init paralelo com repique), trava anti-loop `from_bot` como porta 0 do porteiro, `bot_token` saindo do mesmo dicionário (a renomeação da Story 2 passou a funcionar). Lilith 5 achados/1 ALTO, Shaka PASS, 112/112; verificado em produção nos dois lados: grupo mudo, DM intacta. Fernando disse "push"
- 2026-08-28 · Story 1c pronta e testada (130 testes) mas NÃO commitada: gate do Shaka veio CONCERNS (cascata nunca rodou em produção + TELEGRAM_ALLOWED_USER_IDS vazio). Fernando estava no controle remoto e vai preencher o .env mais tarde. Retomar pela frase de aceite das ressalvas, não pelo código.
- 2026-08-28 · Grupo multi-bot FUNCIONANDO em produção: cascata, janela de 10 min, cada Satélite pela própria boca (Lilith, York e Shaka confirmados por print). Fernando pediu modo triagem (sem nome → roteador escolhe pelo assunto); implementado, mas desfaz a propriedade de custo que o gate aprovou — refazer verify e gate antes do release. Custo real medido: 55k tokens por resposta COM busca no vault (o dobro do estimado).
- 2026-08-28 (noite) · Grupo «Vegapunk» funcionando de ponta a ponta em produção: 7 bots, cascata, janela de 10 min, cada Satélite pela própria boca, triagem por assunto. Três bugs achados só rodando (reply_to com privacy ON, dois bots Lilith, JSON cortado por max_tokens). 137 testes. NADA commitado: verify e gate precisam ser refeitos por causa da triagem.
- 2026-08-31 · v1.8.0 `2f48130` — cascata do grupo, janela de 10 min, modo triagem por assunto, captura pela boca do dono com teclado à parte, semáforo de 3 no pipeline, teto de hora 60→25 (York). Lilith em 3 rodadas (1 ALTO cada), Shaka PASS, 143/143. O Fernando commitou e pushou ele mesmo. Aceitação da 1d (colar um link no grupo) ficou pendente.
- 2026-08-31 · Lote de 7 TikToks pelo *capture (vault 126→133). O lote achou uma regressão da v1.8.0: o capture.py tem a própria implementação do notify e quebrou com os campos novos. Duas dívidas novas: gasto invisível dos slides e datas do vault em UTC.
- 2026-09-01 · `4c9bbbe` — York (health: tudo de pé) e Shaka (auditoria de triagem): 91 itens `—` triados em lote aprovado pelo Fernando (4 discard, 6 apply_saas, 1 apply_client, 80 archive) + 2 extraction_failed apagados de _pending/. 92 commits kb:; Fernando disse "push".

