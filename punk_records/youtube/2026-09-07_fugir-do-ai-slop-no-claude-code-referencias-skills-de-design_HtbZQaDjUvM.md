---
item_id: "26feee03-588c-4197-a221-980f3eba270c"
platform: youtube
external_id: "HtbZQaDjUvM"
canonical_url: "https://www.youtube.com/watch?v=HtbZQaDjUvM"
channel: "Felipe Borges - Fala IA!"
captured_at: 2026-09-07
status: applied_saas
triage: apply_saas
tags: ["ai-slop", "design-com-ia", "agent-skills", "mcp", "iteracao-de-design", "biblioteca-de-referencias", "claude-code"]
applicability:
  saas_pessoal: alta
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
theme: design-e-ux
content_type: transcript
---

# Fugir do AI slop no Claude Code: referências, skills de design e iteração em três versões

🔗 https://www.youtube.com/watch?v=HtbZQaDjUvM

## Resumo

O vídeo ataca o AI slop — o padrão visual que denuncia que um site saiu de um ou dois prompts — e argumenta que o problema não é feiura e sim uniformidade: quando tudo tem a mesma cara, o cliente conclui que qualquer um faz o mesmo trabalho, e o preço cai junto. O processo proposto tem três etapas. A primeira é montar uma biblioteca de referências que combine com o projeto, buscando em Awwwards (com filtro por categoria, como agências de design), Dribbble, Pinterest e perfis de designers no X; a regra é que a referência precise fazer sentido para o tipo de cliente, porque escritório de advocacia e agência criativa não pedem os mesmos elementos. A segunda é instalar skills e MCP: ele usa as skills Impeccable — que afirma monitorar 64 padrões conhecidos de AI slop — e Taste Skills v2, com o alerta de que as duas não devem ser ativadas juntas porque entram em conflito, sendo preciso nomear explicitamente qual usar; e o MCP do Higgsfield para gerar imagens e vídeos, com o ChatGPT citado como alternativa mais barata. A terceira é a sequência de construção por iteração: pedir três versões diferentes, uma por referência, comparar, escolher a preferida, gerar mais três a partir dela e então refinar. Ele acrescenta um truque concreto: abrir o código-fonte do site de referência, baixá-lo e passá-lo como arquivo ao Claude Code junto do brief. O acabamento vem de componentes prontos do 21st.dev, copiados como código ou como prompt. A conclusão dele é comercial, não estética: fugir do slop é o que sustenta o preço do trabalho. O vídeo é também funil para o curso do autor, citado várias vezes.

## Tópicos

- **O que é AI slop** — Não é feiura, é uniformidade: mesma paleta, mesma fonte, mesmo layout. O custo é comercial — o cliente passa a achar que qualquer um entrega igual.
- **Biblioteca de referências** — Awwwards com filtro por categoria, Dribbble, Pinterest e designers no X; a referência tem de combinar com o tipo de cliente, não ser só bonita.
- **Skills de design** — Impeccable (afirma monitorar 64 padrões de slop) e Taste Skills v2; NÃO ativar as duas ao mesmo tempo, porque conflitam — é preciso nomear qual usar no prompt.
- **MCP de imagens** — Higgsfield para gerar imagens e vídeos de fundo; ChatGPT citado como alternativa mais barata para as imagens.
- **Código-fonte como referência** — Abrir o fonte do site de referência, baixar o arquivo e anexá-lo à conversa junto do brief, para o agente ver estrutura real e não só a aparência.
- **Iteração em três versões** — Gerar três versões, uma por referência, escolher a melhor, gerar mais três a partir dela e refinar; pode ser em agentes separados para não misturar contexto.
- **Acabamento com componentes** — 21st.dev fornece efeitos prontos (cursor, meteoros) copiáveis como código ou como prompt para o agente incorporar.

## Ferramentas citadas

- **Claude Code**: agente que constrói o site a partir do brief, das referências e das skills instaladas (dito Cloud Code na transcrição)
- **Awwwards**: banco de referências filtrável por categoria de site, com link para o site real
- **Dribbble**: fonte de referências visuais de interface
- **Pinterest**: busca de referências por termo, imagens copiáveis para o agente
- **Impeccable**: skill de design com subskills; declara monitorar 64 padrões de AI slop para evitá-los
- **Taste Skills**: skill alternativa de design, versão 2 experimental; conflita com a Impeccable se ativada junto
- **Higgsfield**: MCP para gerar imagens e vídeos usados no site
- **21st.dev**: biblioteca de componentes e efeitos prontos, copiáveis como código ou prompt

## Pontos-chave

- O custo do AI slop é comercial: uniformidade faz o cliente achar que qualquer um entrega igual, e derruba o preço
- Referência precisa casar com o tipo de cliente — advocacia e agência criativa pedem linguagens diferentes
- Duas skills de design ativas ao mesmo tempo conflitam: nomear explicitamente qual usar no prompt
- Passar o código-fonte baixado do site de referência dá ao agente a estrutura real, não só a aparência
- Iterar em três versões e depois refinar a escolhida é o núcleo do processo, não o prompt único
- Agentes ou conversas separados por versão evitam misturar contexto entre as alternativas
- Componentes prontos do 21st.dev economizam prompt e entregam efeito que seria caro descrever
- O autor recomenda a Impeccable citando 48 estrelas no GitHub logo após dizer que estrelas medem recomendação — a Taste tem 72 mil

## Como aplicar

É o processo mais aplicável do lote: vale para a interface do SaaS e para o site do cliente, e não depende de comprar nada. Montar uma pasta de referências por tipo de cliente, pedir três versões antes de escolher, e nomear uma única skill de design por projeto são mudanças que cabem no fluxo que já usamos aqui no Claude Code.

## 🏴‍☠️ Lilith diz

Moço, este aqui é dos bons, e não é elogio que eu dê com frequência — o processo de três referências, três versões e só então acabamento é osso duro e serve. Mas eu cá reparo em duas coisas: o sujeito diz que estrela no GitHub mede recomendação e em seguida recomenda a skill de quarenta e oito contra a de setenta e dois mil, e o vídeo inteiro desemboca num curso dele. Fique com o método, que é de graça, e teste as duas skills o senhor mesmo antes de acreditar em qualquer uma delas.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
