---
item_id: "153948eb-92d0-4002-8eaf-8735777a3331"
platform: article
external_id: "6ff294c5147c"
canonical_url: "https://en.wikipedia.org/wiki/Moni_Naor"
channel: "Authority control databases · Wikimedia Foundation, Inc."
captured_at: 2026-09-11
status: archived
triage: archive
tags: ["criptografia", "captcha", "moni-naor", "manuel-blum", "criptografia-visual", "traitor-tracing", "broadcast-encryption", "historia-da-computacao"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: baixa
  estudo_geral: media
confidence: alta
theme: seguranca-e-privacidade
content_type: article
---

# Moni Naor — o criptógrafo que teve a ideia do CAPTCHA antes do CAPTCHA existir

🔗 https://en.wikipedia.org/wiki/Moni_Naor

## Resumo

Verbete da Wikipédia sobre Moni Naor, cientista da computação israelense, professor do Weizmann Institute of Science, doutor por Berkeley em 1989 sob orientação de Manuel Blum. Trabalha nos fundamentos da criptografia e é creditado por iniciar a pesquisa em sistemas de chave pública seguros contra ataque de texto cifrado escolhido, por criar a criptografia não-maleável (com Dwork e Dolev) e a criptografia visual (com Adi Shamir). Para o assunto CAPTCHA, o ponto central é este: foi Naor quem propôs métodos para verificar que o usuário de um sistema é humano, o que levou à noção de CAPTCHA — o manuscrito não publicado dele é a referência [10] do paper de 2003 da CMU, que o descreve como contendo as noções cruciais mas sem proposta concreta nem definição formal. Também foi o primeiro, com Amos Fiat, a estudar formalmente broadcast encryption (1994), e contribuiu para traitor tracing, que rastreia a origem do arquivo vazado em vez de tentar impedir a cópia. A lista de prêmios é longa: IACR Fellow (2008), Prêmio Gödel (2014), Paris Kanellakis da ACM (2016, com Fiat), STOC Test-of-Time de 30 anos (2022, pelo paper de criptografia não-maleável de 1991), RSA Award for Excellence in Mathematics (2022, com Cynthia Dwork) e Prêmio Rothschild em Ciência da Computação (2024). Entre os orientandos de doutorado estão Yehuda Lindell, Omer Reingold e Kobbi Nissim. O verbete é biográfico e curto — serve como âncora de autoria e linhagem intelectual, não como material técnico.

## Tópicos

- **Linhagem acadêmica** — Doutorado em Berkeley (1989) sob Manuel Blum, o mesmo Blum que coassina o paper do CAPTCHA na CMU em 2003; orientou Lindell, Reingold e Nissim.
- **Contribuições em criptografia** — Segurança contra ataque de texto cifrado escolhido, criptografia não-maleável, criptografia visual com Adi Shamir e espaços amostrais de pequeno viés.
- **Origem do CAPTCHA** — Sugeriu métodos para verificar que usuários de um sistema são humanos, o que originou a noção de CAPTCHA; a fonte citada é a reportagem 'Who Made that CAPTCHA' do New York Times.
- **Broadcast encryption e traitor tracing** — Primeiro estudo formal de broadcast encryption prático (com Fiat, 1994) e desenvolvimento do traitor tracing, que rastreia a fonte do vazamento em vez de bloquear a cópia.
- **Prêmios** — Gödel (2014), Kanellakis (2016), STOC Test-of-Time (2022), RSA Award (2022) e Rothschild (2024).

## Pontos-chave

- A ideia de um teste automático para separar humano de computador é anterior ao CAPTCHA e vem de um manuscrito não publicado de Moni Naor — o paper da CMU de 2003 o cita como referência [10] e reconhece a precedência.
- Manuel Blum orientou o doutorado de Naor em Berkeley e é coautor do paper que batizou o CAPTCHA em 2000 — a mesma escola intelectual nas duas pontas.
- Naor criou, com Adi Shamir, a criptografia visual: decodificação feita pelo olho humano sobrepondo transparências, sem computador.
- Traitor tracing inverte a lógica da proteção de conteúdo: em vez de impedir a cópia, identifica quem vazou — modelo que vale considerar para material digital vendido.
- O verbete é biográfico e não traz definição formal nem construção de CAPTCHA; para isso a fonte é o paper do Eurocrypt 2003.

## Como aplicar

Serve como fundo histórico, não como receita: se um dia um formulário do SaaS precisar de proteção anti-bot, a decisão continua sendo usar implementação testada (reCAPTCHA/Turnstile) em vez de inventar teste próprio. O que vale guardar daqui é o conceito de traitor tracing, caso material digital seja vendido e a preocupação passe a ser vazamento em vez de bloqueio.

## 💡 Edison diz

Eureka! Olha a linhagem, Fernando: o orientador é Manuel Blum, e o orientando de Blum é quem assina o paper que batizou o CAPTCHA. A ideia boa quase nunca nasce sozinha — ela nasce numa conversa de corredor e leva dez anos para virar botão de site. A orelha subiu no traitor tracing: rastrear quem vazou em vez de tentar trancar a porta é uma inversão que cabe em produto digital, guarde essa.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Moni Naor

| Moni Naor |  | 
|---|---|
| מוני נאור |  | 
| Born | 1961 (age 64–65) | 
| Citizenship | Israeli | 
| Education | Technion University of California, Berkeley | 
| Awards | Gödel Prize (2014) Paris Kanellakis Award (2016) | 
| **Scientific career** |  | 
| Fields | Computer Science, Cryptography | 
| Workplaces | Weizmann Institute of Science | 
|  | Manuel Blum | 
| Doctoral students | Yehuda Lindell Omer Reingold Kobbi Nissim | 

**Moni Naor** (Hebrew: מוני נאור) is an Israeli computer scientist, currently a professor at the Weizmann Institute of Science. Naor received his Ph.D. in 1989 at the University of California, Berkeley. His advisor was Manuel Blum.

He works in various fields of computer science, mainly the foundations of cryptography. He is notable for initiating research on public key systems secure against chosen ciphertext attack and creating non-malleable cryptography, visual cryptography (with Adi Shamir), and suggesting various methods for verifying that users of a computer system are human (leading to the notion of CAPTCHA).<sup>[1]</sup> His research on Small-bias sample space, give a general framework for combining small k-wise independent spaces with small -biased spaces to obtain -almost k-wise independent spaces of small size.<sup>[2]</sup> In 1994 he was the first, with Amos Fiat, to formally study the problem of practical broadcast encryption.<sup>[3]</sup> Along with Benny Chor, Amos Fiat, and Benny Pinkas, he made a contribution to the development of Traitor tracing, a copyright infringement detection system which works by tracing the source of leaked files rather than by direct copy protection.<sup>[4]</sup>

#### Bibliography

[edit]
- Cynthia Dwork, Jeff Lotspiech and Moni Naor, *Digital Signets: Self-Enforcing Protection of Digital Information.*
- Dalit Naor, Moni Naor and Jeff Lotspiech, *Revocation and Tracing Schemes for Stateless Receivers.*
- David Chaum, Amos Fiat and Moni Naor, *Untraceable Electronic Cash,* 1990*.<sup>[5]</sup>*
- Amos Fiat and Moni Naor, *Implicit O(1) Probe Search,* SIAM J. Computing 22: 1-10 (1993).
- Amos Fiat and Moni Naor, *Broadcast Encryption,* 1994*.<sup>[6]</sup>*
- Moni Naor and Benny Pinkas, *Threshold Traitor Tracing* , Crypto 98.
- Moni Naor and Benny Pinkas, *Efficient Trace and Revoke Schemes* , FC'2000.
- Benny Chor, Amos Fiat, Moni Naor and Benny Pinkas, *Tracing Traitors* , IEEE Transactions on Information Theory, Vol. 46(3), pp. 893–910, 2000.<sup>[7]</sup>

#### Honors and awards

[edit]
- 2008: Named an IACR fellow<sup>[8]</sup>
- 2014: The Gödel Prize (with co-authors)<sup>[9]</sup>
- 2016: The Paris Kanellakis Theory and Practice Award of the Association for Computing Machinery<sup>[10]</sup> (with Amos Fiat)
- 2022: The 30-year Test-of-Time STOC Award for his 1991 STOC paper “Non-Malleable Cryptography” (with Cynthia Dwork and Danny Dolev)<sup>[11]</sup>
- 2022: RSA Award for Excellence in Mathematics (with Cynthia Dwork)<sup>[12]</sup>
- 2024: Rothschild Prize in Computer Science for 2024<sup>[13]</sup>

#### References

[edit]
1. ↑ "Who Made that CAPTCHA". *New York Times* . Retrieved January 17, 2014.
2. ↑ Joseph Naor; Moni Naor (1990). "Small-bias Probability Spaces: efficient constructions and Applications". *Proceedings of the 22nd Annual ACM Symposium on Theory of Computing, STOC 1990* (abstract): 213–223.
3. ↑ Amos Fiat; Moni Naor (1994). "Broadcast Encryption". *Advances in Cryptology — CRYPTO' 93* . Lecture Notes in Computer Science. Vol. 773. pp. 480–491. doi:10.1007/3-540-48329-2_40. ISBN 978-3-540-57766-9.
4. ↑ Naor, Moni; Benny Chor; Amos Fiat; Benny Pinkas (May 2000). "Tracing Traitors". *IEEE Transactions on Information Theory* .**46** (3): 893–910. doi:10.1109/18.841169. S2CID 11699689.
5. ↑ Chaum, David; Fiat, Amos; Naor, Moni (1990). "Untraceable Electronic Cash". In Goldwasser, Shafi (ed.). *Advances in Cryptology — CRYPTO' 88* . Lecture Notes in Computer Science. Vol. 403. Springer New York. pp. 319–327. doi:10.1007/0-387-34799-2_25. ISBN 9780387971964.
6. ↑ Amos Fiat; Moni Naor (1994). "Broadcast Encryption". *Advances in Cryptology — CRYPTO' 93* . Lecture Notes in Computer Science. Vol. 773. pp. 480–491. doi:10.1007/3-540-48329-2_40. ISBN 978-3-540-57766-9.
7. ↑ Naor, Moni; Benny Chor; Amos Fiat; Benny Pinkas (May 2000). "Tracing Traitors". *IEEE Transactions on Information Theory* .**46** (3): 893–910. Bibcode:2000ITIT...46..893C. doi:10.1109/18.841169. S2CID 11699689.
8. ↑ "Moni Naor, 2008 IACR Fellow". *iacr.org* . Retrieved 2023-08-27.
9. ↑ "EATCS and ACM SIGACT present the Gödel Prize 2014 for designing innovative algorithms". *EATCS* .
10. ↑ "ACM Paris Kanellakis Award". ACM. Retrieved 6 June 2017.
11. ↑ "The 2022 STOC Test of Time Awards".
12. ↑ "RSA Conference Award for Excellence in Mathematics". *www.iacr.org* . Retrieved 2023-08-27.
13. ↑ The Rothschild Prize

#### Sources

[edit]

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
