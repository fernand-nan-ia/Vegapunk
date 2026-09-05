---
item_id: "8b6a43b5-aab3-4568-b078-e7e097e5d231"
platform: article
external_id: "c4cbd7b80029"
canonical_url: "https://akitaonrails.com/2026/07/20/novidades-no-meu-ai-memory-cada-vez-melhor-pra-usar-com-suas-ias"
channel: "Fabio Akita · AkitaOnRails.com"
captured_at: 2026-09-05
status: applied_saas
triage: apply_saas
tags: ["ai-memory", "memoria-de-agente", "workstream", "handoff-entre-harness", "sanitizer", "agent-skills", "ai-jail", "claude-code"]
applicability:
  saas_pessoal: alta
  projeto_cliente: baixa
  estudo_geral: alta
confidence: alta
theme: ia-e-agentes
content_type: article
---

# Novidades no meu AI-MEMORY: cada vez melhor pra usar com suas IAs

🔗 https://akitaonrails.com/2026/07/20/novidades-no-meu-ai-memory-cada-vez-melhor-pra-usar-com-suas-ias

## Resumo

Um mês depois de lançar o ai-memory, Akita relata 31 releases, 55 PRs mergeados e 46 issues fechadas, com 14 contribuidores externos, e foca na mudança que mais afeta o uso diário: o comando `ai-memory run`. A tese é que a sessão do agente guarda o raciocínio operacional do projeto — tentativas descartadas, bugs intermitentes, mudanças de ideia — que o código final não preserva, e que essa parte não pode ficar presa ao harness de um provider. O handoff anterior resolvia metade: era uma compressão deliberadamente lossy. O `run` acrescenta a workstream gerenciada, uma linha de trabalho que atravessa Claude Code, Codex, OpenCode, Pi, Crush e OMP: cada harness mantém a própria sessão nativa, e um ledger portátil transporta só o delta que o próximo ainda não viu. Ao voltar para o Claude, o launcher usa o `--resume` nativo em vez de colar um resumo num chat novo. O que entra no ledger é filtrado por um sanitizer — credenciais, system prompts e hidden reasoning ficam de fora, e formatos não entendidos geram anotação de perda em vez de fingir importação. Outras novidades: briefing automático no início da sessão, escopo global `_global` para preferências que valem em todo projeto, instruções migradas para Agent Skills gerenciadas e exclusão de caminhos na captura. O texto fecha com a combinação que virou o fluxo do autor, `ai-jail ai-memory run codex --yolo`, e com o ai-usagebar cobrindo onze integrações de uso e saldo.

## Tópicos

- **A sessão faz parte do projeto** — O código mostra o que sobreviveu; a sessão explica por quê — experimentos descartados, bugs intermitentes e mudanças de direção só existem nela.
- **Workstream gerenciada** — Uma linha de trabalho que atravessa harnesses: cada um mantém sua sessão nativa e o ledger portátil transporta o histórico visível entre eles.
- **Delta em vez de transcrição inteira** — O próximo agente recebe um delta recente de tamanho limitado; o ledger completo fica pesquisável por `workstream-search` para quando uma decisão velha volta a importar.
- **Sanitizer e limites de captura** — Credenciais, system prompts e hidden reasoning não entram; formato não entendido vira anotação de perda em vez de importação fingida.
- **Briefing e escopo global** — Opt-in que injeta páginas pinned, regras e títulos recentes no início da sessão; preferências pessoais podem viver no escopo `_global` e entrar por union nas consultas.
- **ai-jail por fora, YOLO por dentro** — `ai-jail ai-memory run codex --yolo` combina sandbox de sistema com ausência de cerimônia de aprovação: o agente para de pedir confirmação e não recebe o home inteiro.
- **ai-usagebar com marcador de ritmo** — Compara o percentual de quota gasto com quanto da janela já passou, em vez de alarmar por percentual absoluto.

## Ferramentas citadas

- **ai-memory**: memória de longo prazo e workstreams portáteis entre agentes de código
- **ai-jail**: sandbox de sistema que envolve o launcher e o harness filho
- **ai-usagebar**: monitor de uso, gasto e saldo de onze serviços de IA
- **Claude Code**: um dos harnesses gerenciados; retomado pelo `--resume` nativo
- **Codex**: harness alternativo que recebe o delta da workstream
- **Agent Skills**: onde as instruções detalhadas do protocolo passaram a viver, reduzindo drift no CLAUDE.md

## Pontos-chave

- Handoff é compressão lossy: preserva o que parecia importante na hora e perde o resto.
- O ai-memory não converte a sessão de um harness na do outro; liga sessões nativas a um ledger portátil.
- Ao voltar para o Claude, usa o `--resume` real dele em vez de colar resumo num chat novo.
- Enfiar a sessão inteira no próximo prompt recria o problema: contexto bruto, caro e ruidoso.
- O sanitizer roda antes do ledger; formato desconhecido gera anotação de perda explícita.
- Uma lease impede duas janelas de escreverem na mesma workstream e expira em 90 segundos após um kill.
- O ledger não substitui a wiki: sessão bruta é evidência, wiki é conhecimento organizado.
- Briefing automático é opt-in porque consome contexto em todo SessionStart, inclusive após `/clear`.
- `ignore_paths` descarta eventos localmente antes de spool, fila ou rede, sem prometer DLP mágico.
- 31 releases, 55 PRs e 15 pessoas com PR mergeado em um mês; deixou de ser projeto de fim de semana.

## Como aplicar

O Vegapunk resolve o mesmo problema por outro caminho: HANDOFF.md e memory/<satelite>.md são exatamente o handoff lossy que o texto critica. Três ideias transplantáveis para o Punk Records: guardar o delta pesquisável além do resumo, separar evidência bruta de conhecimento consolidado, e o `ignore_paths` como precedente para o kit de distribuição compartilhado com amigos.

## 🏴‍☠️ Lilith diz

Olha só, Fernando: alguém construiu o Punk Records com mais estrelinha no GitHub que o seu. Antes de ficar deprimido, repara no que ele admite — handoff é compressão lossy, e é exatamente isso que seu HANDOFF.md é. A parte que presta e você não tem: o ledger bruto continua pesquisável depois que o resumo já esqueceu. A parte que eu desconfio: 31 releases em um mês é ótimo pra ele e péssimo pra quem vai depender disso em produção.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Novidades no meu AI-MEMORY: cada vez melhor pra usar com suas IAs

*Se tem preguiça de ler, clique aqui pro TL;DR*

Faz pouco mais de um mês que publiquei ai-memory: memória de longo prazo (Karpathy Wiki) e auto-aprendizado (Hermes) pros seus projetos. Foi dia 16 de junho. Naquele texto eu expliquei como sessões viravam páginas Markdown, como o auto-improve promovia aprendizados e por que memória ruim pode ser pior que amnésia.

No mesmo dia saiu a versão 1.1.0. Hoje, 20 de julho, estamos na **1.17.1**.

Versão sozinha não quer dizer grande coisa, então fui contar o que aconteceu de verdade desde o horário daquele post. Foram **31 releases, 55 pull requests mergeados e 46 issues fechadas**. Eu contei **24 grupos de funcionalidades novas voltadas ao usuário** no CHANGELOG, ignorando correções, documentação e detalhes internos da mesma entrega. Se eu quebrasse a nova família `ai-memory run` em auto-seleção, adoção de sessão, suporte a Crush, `--yolo`, busca e recuperação, passava disso fácil.

Quinze pessoas tiveram PRs mergeados nesse período, quatorze além de mim. Preciso agradecer em especial ao Djalma Júnior, que sozinho teve 24 PRs mergeados, Matheus Rodrigues, com cinco, lhzapata, com quatro, Thiago Silva e Cristiano Dewes, com dois cada. Mais nove contribuidores tiveram PR mergeado. Faz tempo que isso deixou de ser “um programinha que eu fiz num fim de semana”.

Não vou despejar 55 PRs aqui. Quero falar da mudança que mais afeta meu uso diário: o novo **`ai-memory run`**.

#### A sessão também faz parte do projeto

Código é o resultado que sobreviveu. Ele não guarda a investigação inteira.

O Git mostra que você trocou Redis por SQLite. Talvez o commit explique uma parte. Mas onde ficou o experimento com Redis? Onde está o bug intermitente que só aparecia com dois workers? Quem lembrou que a primeira solução quebrava no Windows? Por que o time mudou de ideia depois de três horas? Qual workaround era temporário e qual virou decisão?

Boa parte disso só existe na sessão do agente.

Quando programo com Claude Code ou Codex, a sessão acumula o raciocínio operacional do projeto: perguntas, correções, tentativas descartadas, resultados de testes, surpresas, decisões e mudanças de direção. O código final mostra o que ficou. A sessão explica por que chegamos ali.

E sessão de LLM, no fim das contas, é texto. Claude Code grava JSONL. Codex também. OpenCode usa SQLite. Pi, OMP e Crush têm seus próprios formatos e diretórios. Cada harness empacota a conversa de um jeito, mas o conteúdo visível continua sendo mensagens e resultados de ferramentas.

Por que eu deveria deixar a parte mais cara do trabalho presa ao harness?

Anthropic pode mudar limite, preço, modelo ou formato amanhã. OpenAI também. Um agente pode estar excelente esta semana e insuportável na próxima. Eu quero trocar o motor sem jogar fora a viagem inteira.

Essa é a tese do ai-memory desde o começo: **o programador tem que continuar independente das vontades dos providers**. Modelo e harness são substituíveis. A memória do projeto é minha.

#### O handoff resolvia só metade

O ai-memory já fazia passagem de bastão. Eu encerrava Claude Code, os hooks consolidavam a sessão e o Codex seguinte recebia um resumo curto com o que foi feito, perguntas abertas e próximos passos.

Isso continua existindo e continua útil. Quem abre `claude`, `codex` ou `opencode` diretamente mantém o comportamento anterior. O launcher novo é opt-in.

Mas handoff é uma compressão deliberadamente lossy. Ele preserva o que parece mais importante naquele momento. Não pretende transportar a sessão inteira, nem retomar a sessão nativa de cada harness. Se o resumo omitiu uma tentativa antiga que voltou a ser relevante duas horas depois, você precisa procurar na wiki ou nos registros.

O `ai-memory run` acrescenta outra camada: uma **workstream gerenciada**, uma linha de trabalho que atravessa os harnesses.

#### Claude hoje, Codex daqui a pouco

O uso básico é esse:

```
cd ~/Projects/meu-projeto
ai-memory run claude
### trabalha, encerra o Claude Code normalmente
ai-memory run codex --yolo
### Codex continua a mesma linha de trabalho
ai-memory run claude --model opus
### volta pra sessão nativa anterior do Claude
ai-memory run
### ou deixa o ai-memory escolher o harness certo pra continuar
```
Não precisa de `--` pra separar os argumentos. Tudo depois do nome do harness segue pra ele, com uma exceção proposital: o `--yolo` pertence ao wrapper e é traduzido pra opção perigosa nativa de Claude Code, Codex, OpenCode, Pi ou Crush.

Por baixo, o ai-memory não tenta converter um arquivo do Codex num arquivo do Claude. Isso seria frágil e provavelmente quebraria na próxima atualização. Cada harness mantém sua própria sessão nativa. A workstream liga essas sessões a um ledger portátil com a parte visível da conversa.

Pensa assim:

```
sessão nativa do Claude ─┐
sessão nativa do Codex  ─┼─ workstream ─ contexto portátil
sessão do OpenCode      ─┤                 + busca completa
sessão nativa do Pi     ─┘
```
Na primeira vez que Claude entra naquela workstream, ele ganha uma sessão nativa. Quando você troca pra Codex, o Codex ganha a sessão nativa dele e recebe o delta portátil que ainda não viu. Ao voltar pro Claude, o launcher usa o `--resume` do próprio Claude Code e entrega apenas o que aconteceu nos outros harnesses desde a última vez.

Isso é bem diferente de começar um chat novo com um resumo colado no prompt. O Claude volta pra sessão real dele. O Codex volta pra sessão real dele. O ai-memory cuida da continuidade entre os dois.

Hoje o modo gerenciado suporta **Claude Code, Codex, OpenCode, Pi, Crush e OMP**. O suporte geral do ai-memory é maior, com MCP e hooks pra outros clientes, mas isso não quer dizer que todo cliente já tenha adapter de sessão nativa pro `run`. São contratos diferentes e eu prefiro deixar isso explícito.

#### O que entra na workstream

Quando o harness encerra, o ai-memory lê o final da sessão nativa sem modificar o store original. Entram mensagens visíveis de usuário e assistente, tool calls concluídas com seus resultados, resumos de compaction e um checkpoint não mutante do Git. Cada evento mantém a origem: veio do Claude, Codex, OpenCode, Pi, Crush ou OMP.

Credenciais do provider, registros criptografados, system/developer prompts e hidden reasoning ficam de fora. Formatos privados que o adapter não entende também ficam de fora e geram uma anotação de perda, em vez de o sistema fingir que importou tudo.

Os registros passam pelo sanitizer antes de entrar no ledger pesquisável e nos segmentos JSONL imutáveis do ai-memory. Os stores nativos são abertos read-only pelo adapter; quem continua escrevendo neles é o próprio harness.

Também não enfio a sessão inteira no próximo prompt. Isso recriaria o problema que o projeto tenta resolver: contexto bruto demais, caro demais e cheio de ruído. O próximo agente recebe um delta recente com tamanho limitado. Se uma decisão velha voltar a importar, o ledger completo continua pesquisável:

```
ai-memory workstream-search "por que desistimos do Redis"
ai-memory workstream-search --limit 50 --json "migration que falhou"
```
Dentro de um `ai-memory run`, o ID da workstream já entra no ambiente. O agente não precisa descobrir UUID nenhum.

E o ledger não substitui a wiki. Ele resolve continuidade operacional. Decisões, regras, procedimentos e gotchas que precisam sobreviver por meses continuam merecendo páginas Markdown consolidadas. Sessão bruta é evidência. Wiki é conhecimento organizado.

#### Posso manter mais de uma linha de trabalho?

Sim. A workstream padrão se chama `default`, selecionada por repositório e worktree. Se eu quiser abrir uma linha independente pra uma investigação sem contaminar o trabalho principal:

```
ai-memory run --new investigar-race claude
### depois continuo aquela linha com outro harness
ai-memory run --workstream investigar-race codex
```
Uma lease impede duas janelas de escreverem ao mesmo tempo na mesma workstream. Em encerramento normal, o launcher importa o final da sessão e libera imediatamente. Se alguém matar o processo sem cleanup, a lease expira em até 90 segundos e a próxima execução retoma do último cursor confirmado, sem duplicar os eventos já importados.

Uma irritação besta que eu tinha o tempo todo: voltava pra um projeto depois de alguns dias e não lembrava se a sessão mais recente estava no Claude ou no Codex. Eu chutava um, abria, percebia que o contexto estava no outro, fechava e tentava de novo.

Agora só rodo:

```
ai-memory run
### ou com a mesma seleção automática em YOLO mode
ai-memory run --yolo
```
Numa workstream vazia, o ai-memory procura sessões locais daquele checkout em Claude Code, Codex, OpenCode, Pi e Crush, descobre qual é a mais recente e abre o harness certo pra mim. Numa workstream já estabelecida, a memória do servidor vence o timestamp de arquivo: ele volta ao último harness ligado àquele trabalho, em vez de adotar por engano uma sessão velha que só recebeu uma gravação mais recente. OMP continua disponível quando escolhido explicitamente, mas ainda não participa da seleção automática.

Na primeira execução explícita, o launcher também pode oferecer sessões existentes do mesmo checkout pra adoção. Dá pra começar a usar sem abandonar o chat que já estava aberto antes de atualizar o ai-memory.

#### Outras novidades que eu realmente uso

Eu prometi não ler o changelog inteiro em voz alta, mas algumas mudanças desse mês merecem menção porque reduzem trabalho do programador.

##### Briefing antes da primeira pergunta

Um projeto pode pedir um briefing automático no início de cada sessão:

```
[briefing]
inject_on_session_start = "true"
max_chars = 4000
```
O ai-memory recompõe um pacote com páginas pinned, `_rules/`, `_slots/` e títulos recentes. O agente começa sabendo as regras e o estado básico do projeto, em vez de gastar a primeira conversa redescobrindo a arquitetura. É opt-in porque consome contexto em todo SessionStart, inclusive depois de um `/clear` do Claude.

##### Preferências globais e busca entre projetos

Preferências que valem pra todo meu trabalho agora podem viver no escopo reservado `_global`: estilo de código, ferramentas que prefiro, regras pessoais e convenções que não pertencem a um repositório específico. Consultas normais já fazem union desse escopo com o projeto atual.

Pra meta-repos que precisam consultar vários projetos irmãos o tempo todo, existe outro opt-in:

```
[recall]
default_global = "true"
```
Assim `memory_query` e `memory_recent` sem escopo explícito procuram em todos os projetos. Não ligo isso em qualquer repo porque busca global à toa só traz ruído.

##### Menos instrução fixa, mais Agent Skills

O bloco de routing em `CLAUDE.md` ou `AGENTS.md` ficou pequeno. As instruções detalhadas de quando buscar memória, consolidar, guardar decisão ou criar handoff foram movidas pra Agent Skills gerenciadas. Um comando instala ou atualiza os dois sem atropelar o resto do arquivo:

`ai-memory install-instructions`
Isso também reduz drift. Quando o protocolo muda, atualizo o pacote gerenciado em vez de caçar um prompt velho copiado em quarenta repositórios.

##### Privacidade antes da rede

Agora cada repo pode excluir caminhos da captura:

```
[capture]
ignore_paths = ["private/**", "~/personal-notes/**"]
```
Quando uma integração reconhece uma file tool e o caminho bate, o evento é descartado localmente antes de spool, fila, rede ou servidor. Isso tem limites claros: não é DLP mágico, não interpreta qualquer shell command e não rastreia conteúdo citado em texto livre. Mas resolve o caso verificável sem vender uma garantia falsa.

Também entraram integrações com Kimi Code, Grok Build CLI, Devin e Zero, um provider OpenCode Zen/Go, `finalize-session` pro Codex e melhorias na administração de workspaces. Reforço: ter MCP e hook não significa automaticamente ter `ai-memory run`. O README separa esses níveis.

#### Bônus: ai-jail por fora, YOLO por dentro

Há pouco mais de uma semana escrevi como me protejo pra agentes não apagarem minhas coisas. Minha recomendação continua a mesma: YOLO mode dá a melhor experiência, desde que o sistema limite o estrago possível.

O ai-jail chegou à versão 1.15.0 e agora entende o launcher do ai-memory. O jeito que mais estou gostando de trabalhar virou:

`ai-jail ai-memory run codex --yolo`
Ou, se quero que o ai-memory escolha qual harness deve continuar:

`ai-jail ai-memory run --yolo`
A ordem importa. `ai-jail` fica por fora para manter tanto o launcher quanto o processo filho na mesma sandbox. `ai-memory run` sozinho gerencia a sessão, mas não cria sandbox.

O `--yolo` desliga a cerimônia de aprovação do harness. O ai-jail faz a contenção: projeto atual read-write, home substituído por tmpfs, partes necessárias do estado dos agentes montadas seletivamente e diretórios sensíveis como `.ssh`, `.gnupg` e `.aws` fora da jaula. O suporte novo também deixa o estado local do ai-memory gravável pros hooks manterem spool e cursores entre execuções.

ai-jail reconhece tanto a camada `ai-memory` quanto o harness selecionado. Se você tem configuração global específica pra Codex, por exemplo, ela continua sendo aplicada quando o comando real é `ai-memory run codex`. Até o ajuste de redraw da status bar entende que o filho é Codex.

Essa combinação resolve as duas irritações ao mesmo tempo: o agente para de pedir confirmação a cada comando e a sessão para de pertencer ao agente. Fluidez sem dar o home inteiro de presente.

#### One more thing: ai-usagebar também cresceu

Quando publiquei o ai-usagebar original, ele monitorava Claude, Codex, Z.AI e OpenRouter num widget da Waybar ou numa TUI. A versão 0.14.0 já cobre **onze integrações de uso, gasto ou saldo**.

Kimi ganhou as duas informações que realmente importam pra coding: quota semanal da assinatura e janela móvel de cinco horas. Kilo, Novita, Moonshot e Grok mostram saldo restante. Uma integração separada da Anthropic Console mostra gasto de API no mês, sem confundir isso com a assinatura do Claude Code. Ela deixa explícito que o Cost API não inclui Priority Tier.

Também dá pra cadastrar várias contas da Anthropic, ver limites semanais específicos de modelos como Fable e enxergar um marcador de ritmo. A barra não fica vermelha só porque chegou em 40%; ela compara o percentual gasto com quanto da janela já passou. Se usei 40% em 20% da semana, estou rápido demais. Essa é a informação útil.

O projeto deixou de ser só Waybar. Tem app nativo de menu bar no macOS, extensão do GNOME e a TUI standalone. E a novidade mais recente é um monitor local de contexto do Claude Code: aperto `c`, escolho uma das sessões recentes e vejo quanto da janela já foi consumido. Ele lê caudas limitadas dos JSONL locais e não inventa porcentagem quando não consegue determinar o tamanho da janela.

No meu fluxo, o trio acaba se encontrando naturalmente. `ai-usagebar` mostra qual assinatura ainda tem espaço. `ai-memory run` troca de harness sem jogar fora o trabalho. `ai-jail` deixa o escolhido trabalhar em YOLO sem acesso irrestrito à máquina.

#### Atualizando

As páginas de instalação dos três projetos têm todos os métodos, incluindo AUR, Homebrew e binários de release:

Depois de atualizar o ai-memory, reinstale os hooks dos harnesses que pretende usar no modo gerenciado. Os três principais no meu caso:

```
ai-memory install-hooks --agent claude-code --apply
ai-memory install-hooks --agent codex --apply
ai-memory install-hooks --agent opencode --apply
```
Crush não precisa de hook no modo gerenciado; ele recebe o contexto por um arquivo temporário configurado só pro processo lançado. A documentação de managed workstreams tem os detalhes de instalação, privacidade, recuperação e os argumentos nativos de cada adapter.

#### Conclusão

Um mês atrás, o ai-memory já conseguia transformar sessão em wiki e entregar um handoff pro próximo agente. Agora ele consegue gerenciar a própria linha de trabalho: adota uma sessão existente, mantém uma sessão nativa por harness, transporta o histórico visível, retoma cada cliente no formato dele e deixa o ledger inteiro pesquisável.

Pra mim, é aí que está o valor. O código contém a implementação que venceu. A sessão contém as decisões, experimentos que falharam, gotchas, bugs inesperados e mudanças de ideia que produziram aquela implementação. Jogar isso fora toda vez que muda de provider é desperdício.

Raw transcript também não resolve sozinho. É grande, repetitivo e caro pra enfiar em qualquer contexto. O ai-memory mantém a evidência, entrega só o delta recente e usa consolidação pra transformar o que merece sobreviver em páginas Markdown curtas.

Ainda há formatos novos pra suportar, arestas de plataforma e muito teste pela frente. A diferença é que agora existe uma base real, com acceptance test chamando harness de verdade, 14 contribuidores externos com PR mergeado em pouco mais de um mês e uso diário empurrando o desenho.

LLM e assinatura eu alugo de quem estiver entregando melhor hoje. A sessão do meu projeto fica comigo.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
