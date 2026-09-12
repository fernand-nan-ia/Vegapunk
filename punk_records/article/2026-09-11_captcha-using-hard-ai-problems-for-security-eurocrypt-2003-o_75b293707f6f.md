---
item_id: "d1d3ae87-3612-4a22-bbaa-c43f8e81a2f4"
platform: article
external_id: "75b293707f6f"
canonical_url: "https://www.cs.princeton.edu/~chazelle/courses/BIB/captcha-eurocrypt.pdf"
channel: "von Ahn, Blum, Hopper, Langford — CMU / Princeton BIB"
captured_at: 2026-09-11
status: archived
triage: archive
tags: ["captcha", "problemas-dificeis-de-ia", "criptografia", "esteganografia", "teste-de-turing", "anti-bot", "prova-de-seguranca", "eurocrypt-2003"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: nenhuma
  estudo_geral: alta
confidence: alta
theme: seguranca-e-privacidade
content_type: manual
---

# CAPTCHA: Using Hard AI Problems for Security (Eurocrypt 2003) — o paper que formalizou o CAPTCHA

🔗 https://www.cs.princeton.edu/~chazelle/courses/BIB/captcha-eurocrypt.pdf

## Resumo

Paper de Luis von Ahn, Manuel Blum e Nicholas Hopper (CMU) com John Langford (IBM), apresentado no Eurocrypt 2003, que dá a fundação teórica do CAPTCHA: um teste automatizado que a maioria dos humanos passa e que nenhum programa atual passa, de modo que qualquer programa com alta taxa de sucesso sobre o teste pode ser convertido em solução para um problema aberto de Inteligência Artificial. A tese central é tratar problema difícil de IA como premissa de segurança, do mesmo jeito que a criptografia trata fatoração de inteiros de 1024 bits — com a diferença honesta que os autores assumem: não existe prova de que um programa não possa passar num teste que um humano passa, já que o cérebro humano é um programa que passa; o que se faz é uma redução entre passar no teste e superar o estado da arte dos algoritmos. Formalmente o paper define sucesso sobre um teste, teste (α,β)-executável por humanos, problema de IA como a tripla (S, D, f), problema (δ,τ)-resolvido e (δ,τ)-difícil, e finalmente o (α,β,η)-captcha — exigindo que o código do teste seja público. A partir de duas famílias de problemas de IA sobre imagens (P1: reconhecer que uma imagem transformada veio de uma imagem específica de um banco; P2: rotular a imagem transformada), constrói duas famílias de testes: MATCHA, teoricamente limpa mas impraticável, e PIX, prática e já em uso à época no Yahoo! e no Hotmail, com o exemplo do Animal-PIX. Cada construção vem com teorema ligando a dificuldade do problema de IA ao parâmetro de segurança do teste. A segunda metade do paper mostra uma aplicação independente: soluções para P1 e P2 permitem esteganografia robusta baseada em imagens, com sigilo e robustez provados contra um adversário que transforma as imagens em trânsito sem poder degradá-las a ponto de atrapalhar correspondentes legítimos. A conclusão é o argumento ganha-ganha, hoje famoso: ou o CAPTCHA resiste e existe um jeito de separar humano de máquina, ou ele é quebrado e um problema útil de IA foi resolvido. O paper credita explicitamente a Moni Naor o primeiro manuscrito com as intuições de 'teste de Turing automatizado', reconhecendo que faltavam ali proposta concreta e definição formal.

## Tópicos

- **Motivação e aplicações** — Enquete do Slashdot de 1999 (21.156 × 21.032 votos entre bots de MIT e CMU), cadastro em massa em e-mail gratuito, bots de busca, worms e spam, e prevenção de ataque de dicionário conforme Pinkas e Sander.
- **Criptógrafos preguiçosos fazendo IA** — Não há como provar que um programa não passa num teste que um humano passa — o cérebro é esse programa. O método é o da criptografia: supor que o adversário não supera o estado da arte e provar a redução.
- **Definições formais** — Sucesso sobre um teste, teste (α,β)-executável por humanos, problema de IA como tripla (S, D, f), problema (δ,τ)-resolvido e (δ,τ)-difícil, e o (α,β,η)-captcha — com exigência de código público.
- **Problemas de IA como primitiva de segurança** — Dificuldade definida por consenso da comunidade, não por assintótica; não existe parâmetro de segurança como o tamanho da chave — reforça-se repetindo o teste. Em compensação, só é preciso resistir por segundos, não por anos como um dado cifrado.
- **MATCHA** — Teste em que o verificador mostra (i, t(j)) e pergunta se a imagem transformada veio da mesma origem; Lema 1 e Teorema 1 ligam sucesso no teste a uma solução de P1. Acerta 1/2 por chute, então precisa de várias rodadas — limpo na teoria, impraticável na prática.
- **PIX** — Verificador sorteia imagem e transformação, manda t(i) com a lista de rótulos e aceita se o rótulo bate; Teorema 2 liga a segurança à dificuldade de P2. É a família em uso no Yahoo! e no Hotmail, e o Animal-PIX é o exemplo com vinte animais.
- **Esteganografia robusta baseada em imagens** — Solução para P1/P2 constrói um stegosystem com sigilo e robustez provados; implementa o 'canal supraliminal' de Craver, apoiado no fato de que o adversário não pode distorcer as imagens além do que o olho humano tolera.

## Ferramentas citadas

- **Yahoo!**: Usava um CAPTCHA de desenho dos autores para impedir cadastro automatizado de contas — a Figura 1 do paper
- **Hotmail**: Citado como portal onde instanciações de PIX já estavam em uso
- **Animal-PIX**: Instanciação de PIX em captcha.net: foto distorcida de animal comum com vinte alternativas
- **AltaVista**: Primeiro exemplo prático de teste de Turing automatizado, baseado em ler caracteres levemente distorcidos para derrotar OCR de prateleira
- **SpamArrest**: Empresa citada como já comercializando a ideia de só aceitar e-mail se houver humano do outro lado

## Pontos-chave

- A definição exige que o código do CAPTCHA seja público — segurança por obscuridade está fora desde o primeiro parágrafo formal.
- Não existe prova de impossibilidade: o paper assume explicitamente que o adversário não supera o estado da arte da IA, exatamente como a criptografia assume que não se fatora 1024 bits.
- Problema de IA não tem parâmetro de segurança como tamanho de chave; para elevar a barra, repete-se o teste (uma vez, duas, três).
- Em compensação, CAPTCHA só precisa resistir por segundos: um programa que quebre o teste amanhã não compromete o que foi protegido ontem — o oposto de um dado cifrado, que precisa aguentar anos.
- Nem todo problema difícil de IA serve: é preciso haver jeito automático de gerar instância junto com a resposta.
- MATCHA acerta 1/2 no chute, o que a torna inútil em rodada única — a prática ficou com PIX, que é a família dos CAPTCHAs de portal.
- A precedência da ideia é de Moni Naor, em manuscrito não publicado — o paper reconhece as intuições e aponta a ausência de proposta concreta e definição formal.
- O ganha-ganha é a tese de venda do paper: ou o teste segura e separa humano de máquina, ou é quebrado e um problema aberto de IA foi resolvido.
- O mesmo problema de IA que segura o CAPTCHA constrói esteganografia robusta: o adversário não pode destruir a informação escondida sem deformar a imagem a ponto de atrapalhar usuários legítimos.
- Vinte e três anos depois, a premissa de dificuldade da versão visual foi vencida por visão computacional — o que valida a própria previsão do paper, e explica por que a defesa moderna migrou para sinais de comportamento e atestação em vez de leitura de texto distorcido.

## Como aplicar

É estudo de fundamento, não receita de implementação: nenhum dos dois sites de cliente tem formulário para proteger. O que sobrevive para uso prático é o método — declarar em voz alta qual é a premissa de dificuldade de qualquer proteção que se adote e aceitar que ela tem prazo de validade, e a observação de que teste que precisa resistir por segundos pode assumir risco que um dado cifrado nunca poderia.

## 🧠 Stella diz

Alô, alô. Teste, teste — este é o tipo de paper que eu invejo, meu caro: os autores confessam na segunda página que não conseguem provar o que gostariam, porque o cérebro humano também é um programa que passa no teste. E fizeram ciência assim mesmo, declarando a premissa em vez de escondê-la. A profecia deles se cumpriu: a IA alcançou o teste, e o mundo ganhou a leitura automática de texto distorcido. Ganha-ganha, exatamente como estava escrito — só que a conta veio para quem dependia do CAPTCHA.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
