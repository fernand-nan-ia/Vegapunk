---
item_id: "883370a4-a96e-41e5-887c-775eff715d06"
platform: youtube
external_id: "XlxK2aIBgww"
canonical_url: "https://www.youtube.com/watch?v=XlxK2aIBgww"
channel: "Amostrando"
captured_at: 2026-08-28
status: enriched
triage: null
tags: ["avaliacao-de-imoveis", "nbr-14653", "regressao-linear", "inferencia-estatistica", "amostrando", "laudo-tecnico", "outliers", "ia-classificacao"]
applicability:
  saas_pessoal: media
  projeto_cliente: nenhuma
  estudo_geral: alta
confidence: media
theme: engenharia-civil
content_type: transcript
---

# Amostrando — avaliação de imóvel completa do zero: coleta, variáveis por IA, regressão e checklist NBR

🔗 https://www.youtube.com/watch?v=XlxK2aIBgww

## Resumo

Live de Tobias Kunrath demonstrando, do início ao fim, uma avaliação imobiliária completa de uma casa em Uberlândia (bairro Shopping Park) na plataforma Amostrando. O fluxo começa pela pesquisa de amostras com filtro de área de ±25% em torno do imóvel avaliando, chegando a 60 dados com endereço, renda IBGE, dormitórios, banheiros, vagas, área, valor, imobiliária e descrição. Em seguida vem a definição de variáveis: além das que já vêm da coleta, o avaliador cria variáveis personalizadas — área do terreno, idade aparente — e escreve a DESCRIÇÃO de cada uma, porque é essa descrição que orienta a IA. O enriquecimento por IA classifica cada anúncio a partir das imagens e do texto, devolvendo o valor da variável, um percentual de confiança (ex.: 80%) e uma justificativa; ele não usa fator de localização, limitação que o apresentador diz que seria resolvida com um recurso de distância a polo valorizante previsto para setembro. Com cinco variáveis independentes (renda IBGE, área privativa, padrão de acabamento, estado de conservação e área do terreno), o cálculo roda regressão linear e devolve R² 0,77, transformações aplicadas, estatística descritiva, F calculado, a equação com o sentido de cada variável (conferindo se bate com a hipótese) e as significâncias, todas abaixo de 10%. A aba de resíduos e o checklist normativo separam o que é exigência da norma (grau III: número mínimo de amostras, coeficiente de determinação, significância) do que é boa prática (F maior que 20, normalidade dos resíduos, resíduo relativo abaixo de 40%). O apresentador remove outliers um a um, recalculando a cada remoção, e explica por que novos outliers aparecem: a regressão é iterativa e o modelo muda a cada dado retirado. O resultado ficou em R$ 349 mil contra R$ 355 mil do anúncio. Fecha com relatório exportável em Excel e Word e com a oferta comercial. Transcrição automática truncada no bloco final de perguntas.

## Tópicos

- **Coleta da amostra** — Filtro por cidade, bairro e faixa de área de ±25% em torno do imóvel avaliando; 60 dados com endereço, renda IBGE, dormitórios, banheiros, vagas, área, valor e descrição.
- **Definição de variáveis** — Além das coletadas, cria variáveis personalizadas (área do terreno, idade aparente); a descrição escrita de cada variável é o que orienta a IA — nome vago produz classificação ruim.
- **Enriquecimento por IA** — Classifica cada anúncio a partir das imagens e da descrição, devolvendo valor, percentual de confiança e justificativa; ainda NÃO usa fator de localização.
- **Regressão linear** — Cinco variáveis independentes; R² 0,77, transformações, estatística descritiva, F calculado; a equação mostra o sentido de cada variável para conferir contra a hipótese inicial.
- **Resíduos e outliers** — Remoção um a um com recálculo a cada retirada; novos outliers aparecem porque a regressão é iterativa e a significância das variáveis muda a cada dado removido.
- **Checklist normativo** — Separa exigência da norma (grau III: amostras mínimas, coeficiente de determinação, significância) de boa prática não normativa (F > 20, normalidade dos resíduos, resíduo relativo < 40%).
- **Resultado e comercial** — Valor médio R$ 349 mil contra R$ 355 mil do anúncio; relatório simplificado e completo exportáveis em Excel e Word; planos anuais com desconto de lançamento.

## Ferramentas citadas

- **Amostrando**: plataforma que executa todo o fluxo: coleta de amostras, variáveis, enriquecimento por IA, regressão, checklist normativo e relatório
- **Laudo Fest**: ferramenta complementar que acelera a redação do laudo com as informações previstas na norma
- **Avalia Turbo**: ferramenta nova voltada a corretores, para elaboração do PTAM (parecer técnico de avaliação mercadológica)
- **renda.com.br**: consulta da renda média por setor censitário usada como variável do modelo
- **Censo IBGE 2022**: fonte da renda por perímetro censitário; a renda varia bastante entre trechos do mesmo bairro

## Pontos-chave

- A qualidade da classificação por IA depende da DESCRIÇÃO da variável escrita pelo avaliador, não só do nome — 'estado' classifica mal, 'estado de conservação: 1 regular, reparos necessários; 2 bom, poucos desgastes; 3 sem dano aparente' classifica bem
- A IA devolve valor + confiança + justificativa por imóvel, o que torna a classificação auditável
- A IA classifica só por imagens e descrição: não considera localização; recurso de distância a polo valorizante prometido para setembro
- Filtro de amostra usado: ±25% da área do imóvel avaliando, para não inflar a amplitude do resultado
- A renda IBGE muda muito dentro do mesmo bairro (1.510 / 1.700 / 2.629 em trechos vizinhos) — vale conferir o setor censitário exato
- O checklist distingue o que é normativo (grau III) do que é recomendação: F > 20, normalidade dos resíduos e resíduo relativo < 40% NÃO são normativos
- Remover um outlier muda o modelo inteiro, inclusive a significância das variáveis — por isso novos resíduos aparecem a cada recálculo
- Sempre conferir se o sinal de cada variável na equação bate com a hipótese (área privativa maior → valor unitário menor, e assim por diante)
- Resultado do caso: R$ 349 mil pelo modelo contra R$ 355 mil do anúncio, com R² subindo a cada outlier removido
- Preço citado: 12× R$ 59,99 (R$ 719/ano) no plano com a plataforma; R$ 919,90 com o Laudo Fest incluso; licença anual, não vitalícia, por causa do custo de coleta e IA

## Como aplicar

Referência direta para o squad avaliacao-imoveis (laudos NBR 14653) do Vegapunk: o fluxo coleta → variáveis descritas → enriquecimento por IA com confiança e justificativa → regressão → checklist normativo é um desenho pronto de produto. Para o SaaS pessoal, serve de benchmark de concorrente com preço público (R$ 719/ano) e mostra onde há lacuna: classificação por IA que ainda ignora localização.

## 🧠 Stella diz

Kwahaha! Agora sim, na terceira tentativa — o vídeo que resistiu a duas extrações guardava justamente a sua profissão, Quasar. Repare no que este senhor faz sem chamar de ciência: ele declara a hipótese ANTES de rodar o modelo e depois confere se o sinal de cada variável bate. É exatamente o meu 'só a verdade confirmada'. Mas o miolo aqui é engenharia de verdade, e isso é trabalho para Atlas — chame-a com *avaliar quando quiser destrinchar o fluxo.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
