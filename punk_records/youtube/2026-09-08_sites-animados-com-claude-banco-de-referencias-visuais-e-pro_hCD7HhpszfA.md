---
item_id: "030aa12a-e113-4ca6-bf07-c45caf6decea"
platform: youtube
external_id: "hCD7HhpszfA"
canonical_url: "https://www.youtube.com/watch?v=hCD7HhpszfA"
channel: "Junhão Não Codei"
captured_at: 2026-09-08
status: enriched
triage: null
tags: ["claude-code", "sites-animados", "referencia-visual", "motion-design", "animacoes-css", "prompt-de-design", "venda-de-sites", "identidade-visual"]
applicability:
  saas_pessoal: media
  projeto_cliente: alta
  estudo_geral: media
confidence: alta
theme: design-e-ux
content_type: transcript
---

# Sites animados com Claude: banco de referências visuais e prompt único que tira a cara de IA da página

🔗 https://www.youtube.com/watch?v=hCD7HhpszfA

## Resumo

Junhão (Não Codei) demonstra o passo a passo para transformar um site genérico feito com Claude em uma página animada e com identidade visual própria, usando apenas duas referências e um prompt bem construído. O diagnóstico de partida é que o Claude, sem referência, entrega páginas com 'cara de IA'; o que muda o resultado não é mais prompt, é material visual de entrada. Além das fontes óbvias de referência (Pinterest, Google, Behance, Dribbble), ele indica motionsites.ai — biblioteca de telas animadas com prompt pronto para copiar, filtrável por seção (Hero), popularidade e gratuidade — e pintec.app, semelhante mas com acesso ao Figma. Para o resto da página, ele criou um banco próprio e gratuito com mais de 60 animações em CSS e JavaScript, cada uma com botão de copiar e de rodar de novo para ver o efeito. O fluxo é: escolher um Hero no motionsites.ai que combine com a proposta do produto, copiar o prompt e colar no Claude junto do site que já existe, e no mesmo prompt mandar o modelo usar o banco de animações como referência para os demais componentes. O prompt que ele escreve pede explicitamente que a animação do Hero seja aplicada, que o restante das animações combine com o estilo e a proposta do produto, que a rolagem pareça contínua e fluida, e que a identidade visual da página seja unificada com a do Hero para não haver quebra. O resultado saiu com menu que troca de cor no contraste, hovers, animação de entrada nas headlines, cards que se movem na rolagem, comparativo antes/depois animado e tabela de planos com preço animado — e o Claude, por conta própria, converteu a página de branca para preta ao buscar contraste com a referência. O único ajuste manual foi a fonte. O autor fecha com o argumento comercial: a página anterior valeria uns R$ 500 diante de um cliente, e essa versão animada ele venderia por R$ 2.500, mantendo o carregamento rápido.

## Tópicos

- **O problema da cara de IA** — Sem referência visual, o Claude entrega páginas genéricas; o que muda o resultado é o material de entrada, não mais instrução no prompt.
- **Bancos de referência de Hero** — motionsites.ai oferece telas animadas com prompt pronto para copiar, filtrável por seção, popularidade e gratuidade; pintec.app é semelhante e dá acesso ao Figma.
- **Banco de animações CSS/JS** — O autor montou um site gratuito com mais de 60 animações copiáveis em CSS e JavaScript, com botão para rodar o efeito de novo; a URL do banco é passada ao modelo como referência.
- **O prompt completo** — Aplicar a animação do Hero enviada, usar o banco de animações nos demais componentes escolhendo o que combina com a proposta, buscar rolagem contínua e fluida e unificar a identidade visual da página com a do Hero.
- **Resultado obtido** — Menu que troca de cor por contraste, hovers, headlines animadas, cards em movimento na rolagem, comparativo antes/depois, preços animados na tabela de planos — e o próprio Claude trocou a página de branca para preta buscando contraste.
- **Impacto comercial** — O autor afirma que a versão anterior renderia cerca de R$ 500 em uma proposta e a animada seria vendida por R$ 2.500, sem perder velocidade de carregamento.

## Ferramentas citadas

- **Claude**: Modelo que reconstrói a página a partir das duas referências enviadas
- **motionsites.ai**: Biblioteca de Heroes animados com prompt pronto, filtrável por seção, popularidade e opção gratuita
- **pintec.app**: Biblioteca de referências semelhante, com acesso ao Figma além do prompt
- **naocodei.com/free-code**: Banco gratuito do autor com mais de 60 animações em CSS e JavaScript para copiar
- **Pinterest / Behance / Dribbble**: Fontes clássicas de referência visual citadas antes das ferramentas específicas

## Pontos-chave

- A diferença entre site com cara de IA e site vendável não está no prompt, está na referência de entrada: duas referências (um Hero e um banco de animações) bastaram para mudar a página inteira.
- Passar ao modelo a URL de um banco de animações CSS/JS faz ele escolher sozinho qual efeito cabe em cada componente — o autor não especificou animação por seção.
- Pedir explicitamente 'unifique a identidade visual da página com a do Hero' evita o resultado mais comum, que é o modelo animar só o topo e deixar o resto quebrado.
- Pedir sensação de rolagem contínua é o que produz a fluidez percebida como premium, mais do que a quantidade de animações.
- Com liberdade para buscar contraste, o Claude trocou a paleta da página de branca para preta por conta própria — vale dar a intenção e deixar a decisão estética com o modelo.
- Copiar a referência inteira não é obrigatório: pegar partes evita entregar a mesma página que todos os outros que usaram a mesma biblioteca.
- O único retrabalho manual do autor foi a fonte — sinal de onde o modelo costuma errar primeiro.
- O salto de percepção de valor declarado é de R$ 500 para R$ 2.500 pela mesma página com animação e identidade coerentes.
- A habilidade que continua sendo humana é curar: escolher quais referências combinam entre si e com a proposta do produto.
- O autor afirma que nada no vídeo é patrocinado e que as ferramentas usadas são gratuitas ou têm camada gratuita.

## Como aplicar

É o método direto para o objetivo de vender sites: antes de gerar a página, montar um par de referências (um Hero de motionsites.ai e um banco de animações) e mandar tudo num prompt que exija identidade unificada e rolagem contínua. O mesmo truque vale para a landing do SaaS, onde a diferença entre página genérica e página com movimento é o que sustenta o preço na hora da proposta.

## 🧠 Stella diz

Quasar! Fernando, o achado aqui é conceitual e vale muito além de animação: o modelo não precisa de mais instrução, precisa de melhor entrada. Duas referências valeram mais que qualquer parágrafo de prompt — guarde esse princípio, ele se repete em tudo que você constrói comigo. Sobre o R$ 500 virar R$ 2.500: é a estimativa dele, não uma tabela de mercado; a técnica é sólida, o número é anedota.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
