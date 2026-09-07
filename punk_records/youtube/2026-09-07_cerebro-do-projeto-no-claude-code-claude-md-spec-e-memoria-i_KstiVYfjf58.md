---
item_id: "69be4afe-3fb7-4663-8cb5-fad2a7814847"
platform: youtube
external_id: "KstiVYfjf58"
canonical_url: "https://www.youtube.com/watch?v=KstiVYfjf58"
channel: "LABS"
captured_at: 2026-09-07
status: enriched
triage: null
tags: ["claude-code", "claude-md", "spec-driven", "memoria-de-projeto", "geracao-de-imagens", "deploy-estatico", "pagespeed"]
applicability:
  saas_pessoal: alta
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
theme: ia-e-agentes
content_type: transcript
---

# Cérebro do projeto no Claude Code: CLAUDE.md, spec e memória, imagens por .md e deploy

🔗 https://www.youtube.com/watch?v=KstiVYfjf58

## Resumo

O vídeo é um passo a passo completo de criação de uma landing page de produto físico com o Claude Code desktop, e o miolo dele é a estrutura de arquivos que o autor chama de cérebro do projeto. O ponto de partida é que o agente não lembra de sessões anteriores: o chat some, os arquivos ficam, então o que importa precisa sair da conversa e virar arquivo dentro da pasta. Ele separa em três tipos de .md com ritmos de mudança diferentes — regras, que quase não mudam e ficam no CLAUDE.md lido a cada abertura; spec, que descreve o que construir, incluindo paleta, tipografia e tom em specs/design.md, e muda a cada ajuste; e memória, atualizada pelo próprio agente conforme decisões são tomadas. Misturar os três num arquivo só é o que faz qualquer mudança pequena virar bagunça. Uma regra que ele coloca no CLAUDE.md merece registro: se um pedido novo contradiz uma spec, o agente deve parar e avisar antes de executar. As referências vêm antes do pedido — no máximo três, para não misturar estilo — capturadas em print de página inteira e salvas numa pasta que o agente lê. A geração de imagens também vira arquivo: um imagens.md analisa as fotos do produto e o site de referência e devolve os prompts em inglês com proporção de cada imagem, para colar no gerador; quando o produto sai diferente, a instrução follow the ref junto das fotos originais corrige. Na construção ele usa o modelo mais forte para planejar antes de executar, edita apontando e rabiscando na tela, e puxa componentes prontos do 21st.dev — com o cuidado de mandar recriar em HTML e CSS, porque os componentes vêm em React e trocar de stack quebraria o deploy. O site sai compactado, sobe em public_html e é medido no PageSpeed, com o relatório voltando em print para o agente corrigir.

## Tópicos

- **Por que virar arquivo** — O agente não lembra de sessões anteriores; o chat some e os arquivos permanecem, então decisão importante precisa sair da conversa e virar .md na pasta do projeto.
- **Os três tipos de arquivo** — Regras (CLAUDE.md, quase imutável, lido a cada abertura), spec (o que construir, incluindo paleta, tipografia e tom) e memória (atualizada pelo agente conforme decide). Separados porque mudam em ritmos diferentes.
- **Regra de contradição** — No CLAUDE.md: se um pedido novo contradiz uma spec já registrada, parar e avisar antes de alterar.
- **Referências antes do pedido** — No máximo três, capturadas em print de página inteira e salvas em pasta própria; mostrar o resultado desejado funciona melhor que descrever o caminho.
- **Imagens geradas por arquivo** — Um imagens.md lê as fotos do produto e o site de referência e devolve os prompts em inglês com a proporção de cada imagem; follow the ref corrige quando o produto sai diferente.
- **Publicação e medição** — Compactar o site, subir em public_html com o cache limpo, medir no PageSpeed e devolver o print do relatório ao agente para corrigir desempenho.
- **Construção: planejar, editar e reaproveitar** — Usar o modelo mais capaz para o plano antes de executar; editar apontando ou rabiscando na tela; componentes do 21st.dev entram por prompt, mas precisam ser recriados na stack do projeto.

## Ferramentas citadas

- **Claude Code**: agente que lê a pasta do projeto, constrói o site e roda comandos; usado na versão desktop (dito Cloud Code na transcrição)
- **GoFullPage**: extensão que captura print da página inteira do site de referência
- **ChatGPT**: gerador das imagens a partir dos prompts produzidos pelo imagens.md
- **21st.dev**: biblioteca de componentes prontos; os trechos vêm em React e precisam ser recriados na stack do projeto
- **WhisperFlow**: ditado por voz para escrever prompts falando
- **PageSpeed / web.dev**: medição de desempenho, acessibilidade e SEO do site publicado
- **Hostinger**: hospedagem onde o zip é enviado para public_html; recomendada por afiliado com cupom

## Pontos-chave

- Separar regras, spec e memória em arquivos distintos porque cada um muda num ritmo diferente
- CLAUDE.md é lido a cada abertura do projeto e aponta quais outros arquivos carregar
- Regra explícita de segurança de escopo: pedido que contradiz spec para o agente e pede confirmação
- Máximo de três referências — misturar estilos demais confunde o resultado
- A pasta do projeto é o ambiente de contexto do agente, não apenas onde o site fica salvo
- Gerar os prompts de imagem por arquivo, com proporção definida, em vez de pedir imagem a imagem
- follow the ref junto das fotos originais corrige produto que sai inconsistente
- Componentes do 21st.dev vêm em React: mandar recriar em HTML e CSS para não trocar a stack e quebrar o deploy
- Planejar com o modelo mais forte e executar com um mais barato quando a tarefa já está dirigida
- O autor admite no fim que o site de R$ 10.000 do título exige várias páginas — o que ele construiu é uma landing

## Como aplicar

A separação regras/spec/memória é exatamente a arquitetura que já usamos aqui (CLAUDE.md, HANDOFF.md e os diários em squads/vegapunk/memory), o que serve de confirmação externa — e a regra de parar quando um pedido contradiz a spec é uma linha que vale acrescentar. Para o site do cliente, o imagens.md com proporções e o cuidado de recriar componentes na stack do projeto são os dois ganhos operacionais imediatos.

## 💡 Edison diz

Eureka! Olha só, a orelha subiu aqui: o sujeito chegou sozinho na mesma divisão que a gente usa — regra num arquivo, spec noutro, memória num terceiro, e cada um mudando no seu ritmo. Três ideias que a gente pode pegar já: (1) a regra de parar quando o pedido briga com a spec, que a gente não tem escrita em lugar nenhum; (2) o imagens.md que devolve prompt com proporção em vez de a gente pedir foto por foto; (3) mandar o relatório de desempenho de volta como print para o agente consertar. Barato, barato — coxinha, não jantar.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
