---
item_id: "af95aed0-506c-4920-be40-375cb4dbb709"
platform: article
external_id: "9ae37bed516d"
canonical_url: "https://mazyos.com.br/duvidasfrequentes"
channel: "mazyos.com.br"
captured_at: 2026-09-14
status: applied_client
triage: apply_client
tags: ["mazyos", "claude-code", "venda-de-sites", "galerias-de-referencia", "hospedagem-de-site", "recorrencia-de-site", "kaptar", "whatsapp-api-oficial"]
applicability:
  saas_pessoal: media
  projeto_cliente: alta
  estudo_geral: media
confidence: alta
theme: marketing-e-vendas
content_type: article
---

# FAQ do MazyOS: instalação, planos do Claude, hospedagem, galerias de referência, venda de sites e integrações

🔗 https://mazyos.com.br/duvidasfrequentes

## Resumo

Página de perguntas frequentes da comunidade MazyOS, um sistema de skills para Claude Code voltado a quem vende site e conteúdo, organizada em nove blocos: instalação, primeiros passos, planos e custo, modelos e tokens, sites e hospedagem, conteúdo, imagem e vídeo, clientes e vendas, integrações. O erro de instalação mais comum é a pasta aninhada (uma pasta MazyOS dentro da pasta principal), que faz o Claude não enxergar as skills; a pasta do produto deve ser a raiz, renomeada com o nome do negócio, e a entrevista /instalar vem antes de qualquer entrega. Em custo, a recomendação é plano Pro até o primeiro cliente pago, Sonnet no dia a dia e Opus só em raciocínio pesado, chat novo por assunto e documentos grandes como arquivo .md com caminho em vez de texto colado; a mensagem credit balance too low indica que o terminal está na API e não na assinatura (/login na conta pessoal). Para hospedagem, Vercel ou Netlify de graça com domínio na Hostinger apontando o DNS; VPS só quando há algo rodando 24h (n8n, Evolution API, bot). O bloco de design é o mais denso: mais de vinte galerias de referência por tipo (gerais, landing page, escuro/minimalista, ecommerce, detalhes de interface), styles.refero.design entregando o design system de mais de 2.000 sites em DESIGN.md, GSAP agora 100% grátis com ScrollTrigger e SplitText, anime.js, three.js, 21st.dev, shadcn/ui blocks e uiverse.io; a tese é que cara de IA é falta de referência, não de gosto. Em vendas: primeiros clientes baratos ou de graça para comprar caso, recorrência de 2% a 5% do projeto por mês com escopo escrito, 50/50 na entrada e na entrega, nota fiscal sempre, prospecção por WhatsApp, Google Maps via Kaptar, e-mail em volume ou ligação oferecendo site de demonstração, sempre apontando um problema real. Em integrações, automação sobre WhatsApp pessoal é caminho para ban; usar API oficial (360 Dialog por volta de R$ 50/mês, UazAPI, Evolution API) com n8n.

## Tópicos

- **Instalação e pasta aninhada** — VS Code, Node e Git antes; entrevista /instalar antes de qualquer entrega; a pasta do MazyOS é a raiz, com o nome do negócio. Pasta MazyOS dentro da principal é o erro que esconde as skills.
- **Planos e economia de tokens** — Pro até o primeiro cliente pago, Max depois. Chat novo por assunto, Sonnet no dia a dia, Opus só no pesado, documento grande como .md com caminho. 'credit balance too low' = terminal na API; /login na conta pessoal.
- **Hospedagem e domínio** — Vercel ou Netlify de graça para começar; domínio na Hostinger com DNS apontado; VPS só para serviço 24h (n8n, Evolution API, bot). .com.br para empresa brasileira. HTML ou Next.js direto; WordPress só se o cliente já vive nele.
- **Cara de IA e galerias de referência** — Falta de referência, não de gosto: link de site parecido, animação no scroll pedida, fonte/cor/espaçamento definidos. Galerias: recent.design, siteinspire, land-book, onepagelove, dark.design, tinyblocks (ecommerce), designspells, styles.refero.design (DESIGN.md).
- **Animação e componentes** — Galerias motionsites.ai, movin.design e gsap.com/showcase. Bibliotecas: GSAP 100% grátis com plugins, anime.js, three.js, 21st.dev. Componentes: shadcn/ui blocks para painéis, uiverse.io (4 mil elementos, uso comercial livre) para detalhes de landing.
- **Clientes, preço e prospecção** — Primeiros clientes baratos ou grátis para comprar caso. Recorrência de 2% a 5% do projeto por mês, com escopo escrito. 50/50 e nota fiscal sempre. Canais: WhatsApp um a um, Google Maps via Kaptar, e-mail em volume, ligação com site demo. LGPD se coleta dado.
- **Integrações e WhatsApp** — Meta Ads e Google Ads via MCP; Google Meu Negócio com Routines respondendo comentários às 7h. WhatsApp só pela API oficial (360 Dialog ~R$ 50/mês, UazAPI, Evolution API) com n8n; automação no número pessoal leva a ban.

## Ferramentas citadas

- **MazyOS**: sistema de skills e pastas de contexto para Claude Code, produto da comunidade que a FAQ documenta
- **Claude Code**: agente principal onde o MazyOS roda; /instalar, /novo-projeto, /model, /login, Routines
- **Antigravity**: alternativa gratuita ao Claude Code para começar sem pagar plano
- **Vercel**: hospedagem recomendada para iniciantes; um repositório por projeto
- **Netlify**: hospedagem gratuita e simples; onde o mazyos.com.br roda
- **Hostinger**: compra de domínio, hospedagem compartilhada e VPS num painel só
- **GSAP**: biblioteca de animação, agora 100% grátis com ScrollTrigger, SplitText e DrawSVG
- **styles.refero.design**: entrega o design system de mais de 2.000 sites em DESIGN.md para colar no Claude Code (beta)
- **Kaptar**: prospecção por nicho e região no Google Maps, liberado no módulo 3 do curso
- **360 Dialog**: API oficial do WhatsApp por volta de R$ 50/mês, alternativa a UazAPI e Evolution API

## Pontos-chave

- A pasta do MazyOS não fica dentro de nada: ela é a raiz, renomeada com o nome do negócio; pasta aninhada é a causa de 'as skills não aparecem'
- Entrevista /instalar antes de qualquer entrega; skill sem contexto entrega material genérico
- Plano Pro até o primeiro cliente pago; o cliente paga o upgrade para Max, não o contrário
- Economia de tokens: chat novo por assunto, Sonnet no dia a dia, Opus só no pesado, .md com caminho em vez de texto colado
- Padrão de hospedagem: domínio na Hostinger, site na Vercel ou Netlify de graça, DNS apontado; VPS só para serviço 24h
- Cara de IA é falta de referência: link de site parecido, animação no scroll pedida explicitamente, fonte/cor/espaçamento definidos
- GSAP virou 100% grátis com todos os plugins; ScrollTrigger não é mais pago
- Recorrência de mercado: 2% a 5% do valor do projeto por mês, sempre com escopo escrito
- Pagamento 50/50 (entrada e entrega); nota fiscal independente do tamanho
- Automação em WhatsApp pessoal é o caminho mais curto para o ban; usar API oficial com n8n

## Como aplicar

Para o site do cliente: usar a lista de galerias (onepagelove e tinyblocks por setor) e o styles.refero.design como insumo de DESIGN.md antes de gerar, pedir GSAP para o scroll, e adotar o padrão domínio na Hostinger + site na Netlify já estudado no vault. Na venda: recorrência de 2% a 5% ao mês com escopo escrito e 50/50 como base da proposta; prospecção no Google Maps com o Kaptar, que já alimenta a skill apurar-leads do FURY.

## 📚 Pythagoras diz

O registro é uma FAQ de comunidade, senhor: opinião de um instrutor organizada por pergunta, sem fonte externa, mas com números concretos que o vault ainda não tinha, como a recorrência de 2% a 5% ao mês e o 50/50. Eu deduzo que as duas partes que mais lhe servem são a lista de galerias, que responde à sua pergunta sobre cara de IA com referência em vez de gosto, e o aviso sobre automação em WhatsApp pessoal, que confirma o item da Dito que o Shaka triou ontem. Anoto uma lacuna: a página não diz o preço do próprio MazyOS nem o que o Kaptar custa fora do curso.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Perguntas frequentes

As dúvidas que mais aparecem nos grupos, respondidas de uma vez. Se a tua não estiver aqui, pergunta pro Claude antes do grupo: na maioria das vezes ele resolve mais rápido.

#### Instalação

Meio minuto de vídeo resolve o que trava a maioria na primeira hora. Assiste antes de rodar qualquer coisa.

**O passo a passo, na ordem:**

1. Prepara o terreno primeiro: VS Code instalado, mais Node.js e Git. Sem isso a instalação para no meio.
2. Instala o Claude Code (ou a IA que você preferir, o MazyOS não depende só dele). Se ainda não quer pagar plano, dá pra começar com o Antigravity de graça.
3. Baixa o MazyOS do GitHub e coloca a pasta onde você vai realmente trabalhar, não em Downloads.
4. Abre a pasta no VS Code (Arquivo, Abrir Pasta) e abre o Claude dentro dela.
5. **Faz a entrevista antes de qualquer outra coisa.** Roda`/instalar` e responde com honestidade. É ela que ensina o sistema quem é a tua empresa, como você escreve e onde está o teu gargalo. Nada de site, carrossel ou proposta antes disso.
6. **No fim da entrevista ele te manda renomear a pasta pro nome do teu negócio e deixar ela como a pasta principal. Não ignora esse passo.** É exatamente aqui que a maioria dos alunos para, e é por isso que depois as skills não aparecem.
7. Confere se deu certo: digita `/` e a lista de skills tem que aparecer.

**O erro que mais acontece:**deixar uma pasta chamada

`MazyOS` dentro da pasta principal. Aninhada assim, o Claude não enxerga as skills e você fica achando que o produto veio quebrado. A pasta do MazyOS não fica dentro de nada: ela É a pasta principal, com o nome do teu negócio, e é ela que você abre no VS Code.
A segunda opção de "sim", a que não pergunta de novo. Ela reduz o número de confirmações no meio do caminho.

E pode autorizar: instalar Python, Git e afins faz parte do processo normal. Não é o sistema fazendo nada estranho no teu computador.

Não. Você instala uma vez só.

Pra projeto novo existe a skill `/novo-projeto`. Você só fala que tem um projeto novo, assim e assado, e ela já cria a pasta dele e roda uma entrevista curta daquele projeto: cliente, objetivo, o que vai ser entregue.

O projeto novo herda sozinho o que você já respondeu na entrevista principal (teu negócio, tom de voz, marca). O que é específico dele fica no `CLAUDE.md` da pasta do projeto. Por isso o contexto de um cliente não vaza pro outro sem você precisar reinstalar nada.

Na esmagadora maioria das vezes é pasta aninhada: sobrou uma pasta `MazyOS` dentro da tua pasta principal. O Claude abre a pasta de fora, as skills estão uma camada abaixo, e ele não enxerga.

Confere nessa ordem:

1. A pasta que está aberta no VS Code é a própria pasta do MazyOS (já com o nome do teu negócio), ou tem uma `MazyOS` pendurada dentro dela? Se tiver, você abriu a pasta errada. Abre direto a de dentro, ou sobe o conteúdo dela um nível.
2. Existe uma pasta `.claude` na raiz do que você abriu? Se não existir, é sinal de que você está no lugar errado ou o download veio incompleto.
3. Fecha e abre o VS Code.

Se digitar `/` e a lista continuar vazia, tem uma aula específica sobre isso no módulo IMPORTANTE da área de membros.

Tem, e é o problema mais comum de todos. Com a pasta aninhada assim, nada funciona direito: sem skill, sem contexto, e a sensação de que o produto veio quebrado.

A regra é simples: **a pasta do MazyOS não fica dentro de nada.** Ela é a pasta principal, com o nome do teu negócio, e é ela que você abre no VS Code.

**Errado:** `Meu-Negocio/MazyOS-main/` com as skills lá dentro, e você abrindo `Meu-Negocio`.

**Certo:** `Meu-Negocio/` com `.claude`, `_contexto` e o resto direto na raiz.

Pra consertar, tira o conteúdo da pasta de dentro, joga um nível acima, apaga a pasta vazia e abre de novo no VS Code. Na dúvida, manda um print da tua estrutura de pastas pro Claude e pede pra ele te dizer o que mover.

Versão nova é de graça pra quem já comprou. Você nunca paga de novo.

O que vem do repositório são as skills e a estrutura. O que é teu (o `_contexto/` preenchido na entrevista, as pastas de cliente e as skills que você mesmo criou) continua sendo teu: não sobrescreve esses arquivos ao atualizar.

Antes de mexer, salva teu trabalho no Git. Assim, se algo se perder, é um comando pra voltar.

Pergunta direto pro Claude: *"Como instalo o Git e adiciono ao PATH no Windows?"* (ou Mac). Ele te dá o passo a passo pro teu sistema e ainda confere se deu certo.

Esse tipo de erro é o melhor treino que existe pra você parar de depender do grupo pra coisa técnica.

Não é problema. Essa pasta guarda só personalização visual, cor de ícone, esse tipo de coisa. O projeto roda igual sem ela.

Se mesmo assim quiser deixar idêntico ao da aula, manda um print pro Claude e pede pra ele criar.

Pede pro próprio Claude adicionar a configuração de idioma no `settings.json` dentro da pasta `.claude`, depois reinicia o VS Code.

Atalho que funciona sempre: escreve com ele em português. Ele acompanha o idioma da conversa.

Três saídas, da mais simples pra mais robusta:

- Ditado nativo do Windows (tecla Windows + H), que respeita o idioma do sistema.
- Whisper instalado localmente.
- Transcrever no ChatGPT e colar o texto.

#### Primeiros passos

Na ordem: instalação do MazyOS primeiro, criação de site depois. São as duas aulas que destravam todo o resto.

Depois disso, entra no `#conteudo-denso` do Discord e escolhe um projeto real pra fazer. Assistir aula sem construir nada não gera cliente.

Não. Tem aluno que nunca tinha aberto um terminal na vida e hoje entrega site pra cliente.

O que você precisa é saber explicar o que quer. Quem escreve o código é o Claude. A parte difícil nunca foi a técnica, é a clareza no pedido.

Uma tarefa que você já ensinou uma vez e não precisa explicar de novo. Em vez de escrever um prompt gigante toda vez que quer um carrossel, você digita `/carrossel` e ele já sabe o formato, o tom e a tua marca.

É por isso que a entrevista importa tanto: as skills leem o contexto que você preencheu ali. Skill sem contexto entrega material genérico.

Pra ver o que você tem, digita `/` e a lista aparece.

Dá. O MazyOS não é só Claude Code: você instala nele ou na IA que preferir. Quem não quer pagar plano no começo costuma entrar pelo Antigravity, de graça.

Eu uso no Claude porque, pra marketing, ele é a melhor de longe. Mas o sistema é teu, e a estrutura de pastas e contexto funciona do mesmo jeito.

Salva teu trabalho no Git desde o primeiro dia. Com isso, qualquer coisa que ele mexer e você não gostar volta atrás com um comando. Pede pro Claude configurar e subir pro GitHub, ele faz isso sozinho.

É também o que te protege de perder o computador, ou de trabalhar em duas máquinas.

Tem um conteúdo no módulo EXTRAS da área de membros com o link de autenticação do bot. Você entra por ele, confirma a compra e o cargo cai automático.

Se autenticar e o cargo não aparecer, avisa no Discord com o email que você usou na compra.

Começando, fica no modo automático padrão. Ele pede confirmação nas ações que mexem em arquivo, e é isso que te protege enquanto você ainda não sabe o que é normal.

O bypass faz sentido depois, em tarefa repetitiva que você já conhece o resultado. Mesmo aí, abre só a pasta do projeto pro Claude, nunca o computador inteiro.

O Design é uma versão simplificada do Code, com criação visual, mais parecida com wireframe. Por baixo, os dois fazem a mesma coisa.

O jeito que rende: rascunha no Design pra definir o esqueleto, refina no Code.

Mesma empresa: pede pro chat atual "pausar o assunto e resumir onde paramos" antes de sair. Você retoma depois sem perder quase nada.

Empresas diferentes: janelas separadas do VS Code, pastas separadas, cores diferentes por janela. Contexto misturado entre clientes é o jeito mais rápido de entregar a coisa errada pra pessoa errada.

#### Planos e custo

Pro. Ele aguenta tranquilo a fase de aprender e pegar os primeiros clientes.

O Max entra depois do primeiro cliente pago, quando o limite do Pro começar a te atrapalhar de verdade. Deixa o cliente pagar o upgrade, não o contrário.

Dá. O MazyOS não depende só do Claude Code: tem aluno que começa no Antigravity de graça e pega os primeiros clientes assim.

Conta pirata não vale a pena. Some no meio do trabalho e leva teu projeto junto.

Quando puder pagar, encara como ferramenta de trabalho. Um cliente pequeno já cobre o ano.

O que mais economiza, na prática:

- Chat novo pra assunto novo. Chat gigante recarrega tudo a cada mensagem.
- Sonnet no dia a dia, Opus só no que exige raciocínio pesado.
- Documento grande vira arquivo `.md` na pasta, e você passa o caminho em vez de colar o texto inteiro.
- Pedido claro de primeira. Cada ida e volta pra corrigir mal-entendido custa igual.

Nas configurações do Claude, seção Usage. O horário exato do reset aparece ali.

Digita `/login` no terminal e escolhe a conta pessoal, não a opção de API.

A mensagem "credit balance too low" é o sintoma clássico: ele está puxando da API, não da tua assinatura.

#### Modelos e tokens

Digita `/model` no chat do Claude dentro do VS Code e escolhe pelo teclado.

Sonnet dá conta do dia a dia. Opus vale quando a tarefa exige raciocínio mais pesado, arquitetura, decisão complexa. Ele consome mais.

Na ordem: abre um chat novo, troca pra um modelo de janela maior, salva o documento grande como `.md` e passa só o caminho do arquivo.

Se o volume é realmente grande e recorrente, aí o caminho é montar um RAG. Mas raramente é o teu caso.

#### Sites e hospedagem

- **Vercel:** a mais indicada pra quem está começando. O Claude integra bem.
- **Netlify:** gratuito e simples. É onde o mazyos.com.br roda.
- **Hostinger:** domínio, hospedagem e VPS. É onde eu compro meus domínios. A VPS às vezes fica lenta no Brasil.
- **Hetzner:** alternativa de VPS.

Começa em Vercel ou Netlify. VPS só quando o projeto pedir.

Hostinger. É onde eu compro meus domínios, e resolve os três casos num painel só.

- **Domínio:** o que você vai comprar em quase todo projeto de cliente.`.com.br` pra empresa brasileira,`.com` quando o negócio for mais amplo.
- **Hospedagem compartilhada:** só se o cliente já vive em WordPress e mexer nisso sairia caro.
- **VPS:** quando o projeto precisa de algo rodando 24h, n8n, Evolution API, bot de WhatsApp, painel próprio. Aí não tem jeito, site estático não dá conta.

Comprar domínio lá não te obriga a hospedar lá. O padrão que eu uso: domínio na Hostinger, site na Vercel ou Netlify de graça, e você só aponta o DNS. Pede pro Claude que ele te guia registro por registro.

Pode. Cada um vira um projeto independente, com URL própria.

Na Vercel, cada projeto precisa do seu próprio repositório no GitHub.

HTML ou Next.js direto com o Claude. Sai mais rápido, você tem controle total e o resultado fica melhor.

WordPress só quando o cliente já tem um ecossistema em cima dele e mexer sairia caro.

Cara de IA quase sempre é falta de referência. Se você não dá direção, ele entrega o padrão genérico.

- Manda imagem de referência de um site que você acha bonito.
- Pede transições e animação no scroll explicitamente.
- Rascunha no Design, refina no Code.
- Define fonte, cor e espaçamento em vez de deixar ele escolher.

Referências que a comunidade usa: typeui.sh/design-skills, impeccable.style/slop, awesomeclaude.ai.

Movimento é o que mais separa site vivo de site morto. Tem uma pergunta só sobre isso logo abaixo, com as galerias e as bibliotecas de animação.

Essa é a resposta pra "site com cara de IA". Você não precisa ter gosto, precisa ter referência. Abre a galeria, acha um site parecido com o que o cliente pediu, manda o link pro Claude e fala o que você quer daquele.

**As gerais, o melhor da web:**

- godly.website: a mais famosa. Hoje ela abre como recent.design, é rebrand, o acervo é o mesmo.
- siteinspire.com: acervo antigo e bem filtrado, dá pra buscar por estilo e por tipo de negócio.
- land-book.com: enorme, boa pra procurar pelo setor do cliente.
- httpster.net: mais autoral, menos padrãozinho de startup.
- curated.design: seleção enxuta (hoje dentro do Craftwork).
- admiretheweb.com
- **Pinterest:** vale pra clima e paleta, não pra copiar layout. Busca em inglês ("dark landing page", "minimal portfolio") que o resultado muda de nível.

**Landing page, que é o que você mais vai vender:**

- landing.love
- lapa.ninja
- onepagelove.com: só site de uma página, que é o formato da maioria dos teus primeiros clientes.
- landing.gallery
- saaslandingpage.com e saaspo.com: os dois só de SaaS, bons pra estrutura de página que vende.

**Escuro e minimalista, o estilo que combina com o MazyOS:**

- dark.design e darkmodedesign.com: fundo preto feito direito.
- minimal.gallery e siiimple.com: quando menos elemento é o ponto.

**Loja e ecommerce:**

- tinyblocks.cc: só loja online, e o filtro é o ouro aqui. Dá pra buscar por setor (moda, beleza, móveis) e pela plataforma que a loja usa (Shopify, WooCommerce, Squarespace). Quando o cliente é ecommerce, começa por essa.

**Feitos numa ferramenta só:**

- webflow.com/made-in-webflow e framer.com/awards: você não precisa usar Webflow nem Framer pra roubar a ideia. O Claude reproduz.

**Detalhe de interface:**

- designspells.com: coleção daqueles detalhinhos que fazem o site parecer caro. É o que separa entrega de R$ 500 de entrega de R$ 5.000.

**E uma que é diferente de todas as outras:**

- styles.refero.design: em vez de te mostrar o print do site, ela te entrega o **design system** dele já pronto pra IA ler: cor, tipografia, espaçamento e componentes, num arquivo DESIGN.md que você cola direto no Claude Code. São mais de 2.000 sistemas tirados de sites de produto de verdade. É o atalho pra parar de descrever o que você quer e simplesmente entregar a receita pronta. Está em beta.

Separa duas coisas, porque elas resolvem problemas diferentes: **galeria** é onde você acha a ideia, **biblioteca** é o que faz o movimento acontecer.

**Pra se inspirar:**

- motionsites.ai: galeria de landing pages animadas prontas, por categoria (SaaS, ecommerce, portfólio). Tem parte grátis e parte paga.
- movin.design: galeria curada de motion design, de graça. Boa pra achar o efeito antes de saber o nome dele.
- gsap.com/showcase: sites reais feitos com GSAP. Tem uma vantagem que as outras galerias não têm: como você já sabe que o efeito foi feito com a mesma biblioteca que o Claude vai usar, o que você vê ali é reproduzível de verdade.

**Pra fazer acontecer:**

- gsap.com: a biblioteca de animação usada por profissional há mais de 15 anos. **Virou 100% grátis** , com todos os plugins juntos (ScrollTrigger, SplitText, DrawSVG). Se você ouviu que o ScrollTrigger era pago, isso acabou. É a primeira que eu pediria pro Claude usar.
- animejs.com: leve (24KB no total) e modular, você importa só o que usa. Grátis. Boa quando o GSAP é canhão pra matar mosquito.
- threejs.org: 3D no navegador. É o que entra quando o cliente quer o produto girando na tela.
- 21st.dev: componentes de React e Tailwind prontos pra copiar, feitos à mão, com bastante coisa de movimento (marquee, shader, scroll). Atalho pra quando você não quer construir o efeito do zero.

Aqui é diferente de galeria de referência. Galeria te dá a ideia, componente te dá o código pronto pra colar. Duas fontes resolvem quase tudo:

- ui.shadcn.com/blocks: blocos inteiros de interface, prontos e de graça. Menu lateral (o famoso sidebar), dashboard, tela de login, calendário, gráfico. É React com Tailwind, então serve pros projetos em Next.js. Você instala o bloco com um comando (`npx shadcn add sidebar-01` ) e ele cai no projeto funcionando.
- uiverse.io: mais de 4 mil elementos soltos feitos pela comunidade, em CSS puro ou Tailwind. Botão, checkbox, card, loader, toggle, aquele efeito de hover que você não sabia nomear. Copia o HTML e o CSS e cola. Não precisa de React nem de framework nenhum, funciona no site HTML mais simples, e é livre pra uso comercial.

Na prática: shadcn quando o projeto é um painel ou aplicação com várias telas. Uiverse quando é um detalhe específico da landing page que você quer que fique caro.

A referência é liquidglassdesign.com: mais de 110 exemplos de site e interface com o efeito de vidro, e cada um vem com o prompt de estilo pra recriar. É galeria, não biblioteca: você tira de lá a direção visual, não o código.

Tecnicamente é menos complicado do que parece. O que faz o vidro acontecer é `backdrop-filter: blur()` com fundo semitransparente e uma borda clara em cima. Só que ele só aparece se tiver alguma coisa atrás pra desfocar: imagem, gradiente, conteúdo passando no scroll. Em cima de fundo chapado o efeito some.

Baixa o modelo 3D, instala o Blender, conecta o Blender MCP no Claude Code e pede a animação guiada por scroll usando Three.js.

Se for só ícone animado, Lottie resolve com uma fração do peso.

Pede explicitamente: *"revisa o layout responsivo no desktop e no mobile"*. Ele não faz isso sozinho se você não pedir.

Depois do deploy, dá alguns segundos e atualiza a página. Boa parte do "não mudou nada" é cache ou deploy ainda processando.

Pede pro Claude criar. Se quiser o visual igual ao da aula, é uma extensão de ícone de pasta no VS Code.

#### Conteúdo

Dá, com as Routines do Claude. Elas rodam na nuvem, no horário que você definir, com o computador desligado.

É um dos serviços mais fáceis de transformar em recorrência com cliente.

Pouco. Um carrossel de 6 a 8 slides sai rápido.

Se estiver demorando muito, geralmente é chat carregado demais ou modelo pesado sem necessidade. Chat novo costuma resolver.

O MazyOS já gera os PNG prontos, você não precisa converter nada na mão.

Se pegar um HTML solto de outro lugar, dá pra converter em site pronto de conversão ou pedir pro Claude implementar.

Sobe tuas skills num repositório no teu GitHub e referencia nos projetos.

Vale manter um fork organizado: quando sair skill nova do MazyOS, você atualiza sem perder o que criou.

Pergunta pro Claude: *"Como eu converto um emoji em SVG?"*

#### Imagem e vídeo

- **ChatGPT Plus ou Pro:** melhor fotorrealismo.
- **Nano Banana:** mais barato.
- **Higgsfield:** junta várias IAs num lugar só.
- **Gemini:** bom pra remover fundo.

Pra tirar fundo também servem remove.bg, Canva e Adobe Express.

1. Gera uma imagem e ajusta até ficar exatamente como você quer.
2. Devolve essa imagem pro ChatGPT e pede o prompt que descreve o estilo dela.
3. Usa esse prompt como base pras próximas.

ChatGPT Plus e Gemini pras primeiras versões, refinamento no Canva.

Mas o que decide não é a ferramenta, é a clareza do briefing. Briefing vago gera logo genérico em qualquer uma delas.

NotebookLM, gratuito e com transcrição muito boa.

Vantagem extra: dá pra conversar com a reunião ali dentro e extrair só o que importa antes de levar pro Claude.

#### Clientes e vendas

Nos primeiros, cobra pouco ou faz de graça. Você não está vendendo site ainda, está comprando caso e relacionamento.

Ticket alto (R$ 10 mil ou mais) vem quando você consegue mostrar impacto em faturamento, não quando você fica bom de design.

A prática de mercado fica entre 2% e 5% do valor do projeto por mês. Projeto de R$ 25 mil, algo perto de 5% ao mês.

Deixa o escopo escrito. Recorrência sem escopo definido vira suporte infinito de graça.

50/50: metade na entrada, metade na entrega. É o mais comum e protege os dois lados.

Tem cliente que paga 100% adiantado no PIX. Quando oferecerem, aceita.

Cliente pequeno costuma fechar no boca a boca mesmo. Cliente grande, contrato simples resolve e evita dor de cabeça.

Nota fiscal, independente do tamanho.

- **WhatsApp:** direto e personalizado, um a um.
- **Google Maps:** segmenta por nicho e região. É pra isso que serve o Kaptar, liberado de graça pra você no módulo 3.
- **Email em volume:** na casa de mil por dia.
- **Ligação:** oferece um site de demonstração de graça.

O que amarra tudo: chegar apontando um problema real que a empresa tem, não oferecendo "serviço de IA".

Se o site coleta dado de gente, sim. E é mais simples de resolver do que parece.

A comunidade recomenda este vídeo, que explica a lei e os ajustes mais comuns: youtu.be/3no84kEEH3U.

#### Integrações

Dá, pelo MCP oficial da Meta ou por MCPs de terceiros. Google Ads também.

Só que a integração não substitui saber de tráfego. Ela executa mais rápido o que você já sabe decidir. Campanha ruim automatizada continua ruim, só queima verba mais rápido.

Dá, conectando o Google Meu Negócio. Funciona com Cowork.

O pedido é literalmente esse: *"todo dia às 7h, confere os comentários novos e responde"*.

Opções que a comunidade usa: 360 Dialog (por volta de R$ 50 por mês), Evolution API, UazAPI ou a automação de WhatsApp da Hostinger.

A API oficial dá mil conversas gratuitas por mês, e cobra por mensagem depois disso. Junta com n8n pra orquestrar o fluxo.

Existe o risco, sim. Automação em cima do WhatsApp pessoal é o caminho mais curto pro ban.

Faz pela API oficial (360 Dialog, UazAPI). Perder o número que os teus clientes usam sai muito mais caro que a mensalidade.

Nenhuma dúvida encontrada.

Tenta outra palavra, ou pergunta direto pro Claude: ele costuma resolver mais rápido.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
