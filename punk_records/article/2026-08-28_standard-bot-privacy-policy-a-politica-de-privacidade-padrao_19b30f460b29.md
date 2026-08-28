---
item_id: "fdbbe7bc-64bb-4639-8653-e5a9e040c91b"
platform: article
external_id: "19b30f460b29"
canonical_url: "https://telegram.org/privacy-tpa"
channel: "Telegram"
captured_at: 2026-08-28
status: enriched
triage: null
tags: ["telegram-bot", "privacidade", "politica-de-privacidade", "compliance", "dados-pessoais", "termos-de-uso"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: alta
confidence: alta
theme: seguranca-e-privacidade
content_type: article
---

# Standard Bot Privacy Policy — a política de privacidade padrão dos bots do Telegram

🔗 https://telegram.org/privacy-tpa

## Resumo

O Telegram publica uma política de privacidade padrão que se aplica automaticamente a todo bot e miniapp de terceiros na plataforma, a menos que o desenvolvedor publique uma política própria — o que o Telegram recomenda fazer. O documento define o desenvolvedor como responsável pelo serviço (identificável, por exemplo, pelo comando /developer_info) e regula só a relação entre desenvolvedor e usuário, sem substituir a Política de Privacidade do próprio Telegram. O bot só deve coletar e processar dados necessários ao seu funcionamento (§5.1), não pode monetizar dados fora do escopo do serviço (§5.2) e — cláusula central — o §6.2 proíbe compartilhar dados de usuário com terceiros, incluindo com os próprios serviços ou bots adicionais do mesmo desenvolvedor, salvo autorização explícita do usuário ou ordem judicial. O usuário tem direito a pedir cópia de todos os seus dados, exigir exclusão, restringir processamento e revogar consentimento (§7.3), e o desenvolvedor deve responder em no máximo 30 dias. O Telegram se reserva o direito de apagar dados, o chat inteiro ou o próprio bot em caso de abuso da plataforma (§7.1). Usar o bot constitui aceite da política, dos Bot Terms e dos Mini App Terms.

## Tópicos

- **Aplicação por padrão** — A política vale automaticamente para todo bot/miniapp sem política própria (§2.1); o desenvolvedor continua responsável por adequá-la ao seu caso e às leis locais (§2.6).
- **Coleta mínima e legítimo interesse** — O bot só coleta o necessário para suas funções (§5.1), sob a base legal de legítimo interesse; proibido monetizar dados fora do escopo do serviço (§5.2).
- **Não compartilhamento entre bots do mesmo dono** — §6.2: dados de usuário nunca vão a terceiros, incluindo outros serviços ou bots do próprio desenvolvedor, salvo autorização explícita do usuário ou exigência legal.
- **Direitos do usuário** — §7.3: cópia de todos os dados, exclusão, restrição/objeção ao processamento e revogação de consentimento; resposta obrigatória em até 30 dias.
- **Poderes do Telegram** — §7.1: em caso de abuso, o Telegram pode apagar mensagens, o armazenamento em nuvem do miniapp, o chat inteiro ou o próprio bot.

## Pontos-chave

- A política se aplica POR PADRÃO a todo bot de terceiros — quem opera um bot já está vinculado a ela mesmo sem nunca tê-la lido
- §6.2: compartilhar dados de usuário entre bots do MESMO desenvolvedor exige autorização explícita do usuário — relevante direto para o grupo multi-bot dos Satélites com histórico compartilhado
- §7.3: pedidos de cópia ou exclusão de dados devem ser respondidos em até 30 dias
- §5.1: coleta mínima — só dados necessários às funções declaradas do bot
- §5.2: proibido monetizar ou usar dados do usuário fora do escopo do serviço sem consentimento claro
- O bot recebe dados adicionais quando o usuário envia mensagens, arquivos ou compartilha contato/telefone (§4.2)
- Telegram pode deletar dados, o chat ou o próprio bot em resposta a abuso da plataforma (§7.1)
- Telegram recomenda que cada desenvolvedor publique política própria em vez de depender da padrão
- A política não substitui a Telegram Privacy Policy nem os Bot/Mini App Terms — soma-se a eles

## Como aplicar

No grupo multi-bot dos Satélites: enquanto o Fernando for o único usuário, o §6.2 é inócuo; se outra pessoa entrar no grupo, o histórico compartilhado entre bots exige autorização explícita dela e resposta a pedidos de dados em 30 dias. Se o SaaS um dia tiver bot de Telegram, publicar política própria em vez de depender da padrão.

## 🪖 Shaka diz

Isto é contrato, não opinião — e o senhor já está vinculado a ele desde o primeiro /start do Vegapunk. A cláusula 6.2 diz exatamente o que eu disse sobre o grupo dos Satélites: dados entre bots do mesmo dono só com autorização explícita. Enquanto o único usuário for o senhor, está tudo em ordem; no dia em que outra pessoa entrar naquele grupo, releia este item antes, não depois.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

The following serves as a standard Privacy Policy for bots and mini apps on the Telegram platform.

By design, this policy is written to be generally applicable to a wide range of services. While this document serves as a functional agreement between developers and users, Telegram still encourages all developers to create their own, separate privacy policies to better describe the ways in which their service receives, processes and stores data from its users.

1.1. Telegram – Telegram Messenger Inc (also “we”).

1.2. Platform – The Telegram Bot Platform.

1.3. Developer – The person or legal entity who operates and maintains Third-Party Service, as further defined in 3.1.

1.4. Third-Party Service – The bot or mini app of Developer, made available to users on Platform.

1.5. User – The person accessing Third-Party Service via their account on Platform (also “you”).

1.6. Policy – This document, governing the relationship between Third-Party Service and User.

2.1. Policy is a standard document which applies to all third-party bots and mini apps on Platform by default, unless or until their respective developer has published a separate privacy policy.

2.2. Policy governs solely the relationship between Developer and User. It cannot and does not regulate the relationship between Telegram and its users, nor does it supersede the Telegram Privacy Policy.

2.3 Developer follows all privacy guidelines set forth by platforms that distribute Telegram apps, including Apple's App Review Guidelines and Google's Developer Policies.

2.4. Policy regulates the collection, storage, distribution, usage and protection of information of Users who access Third-Party Service.

2.5. Your continued access to and use of Third-Party Service shall constitute your acceptance of Policy, the Telegram Bot Terms and the Telegram Mini App Terms.

2.6. Note that this default Policy is meant to aid Developer in providing a functional privacy policy to their Users, with the understanding that the Policy is written to be generally applicable to a wide range of services. Accordingly, if Developer opts to use the Policy, it is solely their responsibility to ensure that the Policy fits the Developer’s use case and complies with all local laws.

2.7. If you do not accept all the aforementioned terms, you should immediately cease your use of Third-Party Service.

3.1. Third-Party Service is an independent third-party application that is neither maintained, endorsed, nor affiliated with Telegram. Developer is the person or entity defined as such, for example within the Terms of Service of Third-Party Service, its interfaces or in its response to the `/developer_info` command.

3.2. You understand and agree that, without limiting section 8, this Policy may be amended at any time, and it is your responsibility to review and agree to all changes.

3.3. You acknowledge that you have read, understood and agreed to the Telegram Bot Terms and the Telegram Mini App Terms, as well as any other terms made available to you by Developer.

3.4. You acknowledge and warrant that you possess all the necessary rights and permissions to use Third-Party Service in compliance with applicable local laws and legal obligations, including without limitation age restrictions and third-party store terms.

3.5. Developer operates under the understanding that all information you provide is submitted in good-faith, and is not obligated to check or verify your statements for errors or inaccuracies. It is your responsibility to ensure that all information you provide is accurate and up-to-date.

3.6. You may decide to make some information available in the public domain, either directly on Platform, elsewhere on the internet, or via Third-Party Service. The information you choose to make public may be accessed by other users of Third-Party Service via Platform or on the internet, in which case it will not be covered or protected by Policy.

4.1. The ways in which Platform natively allows Third-Party Service to access certain limited information from and about User are described in the Telegram Privacy Policy and Mini App Terms.

4.2. Without limiting section 4.1., Third-Party Service has the ability to receive additional data from you if you send it messages, upload files to it, or choose to share personal information such as your contact or phone number.

4.3. If Third-Party Service is a mini app, it may also receive additional data as detailed in sections 4.1. and 4.2. of the Mini App Terms. In this case, Third-Party Service may also acquire additional information as a result of your interactions with it.

4.4. Third-Party Service may collect anonymous data that is not linked to you in any way, such as anonymized diagnostics or usage statistics.

5.1. Third-Party Service only requests, collects, processes and stores data that is necessary for its designated features to function properly. Third-Party Service processes your personal data on the legal ground that such processing is necessary to further its legitimate interests, including (i) providing services to its users; (ii) detecting and addressing security issues in respect of its provision of services; unless those interests are overridden by your interest or fundamental rights and freedoms that require protections of personal data.

5.2. Developer does not monetize or otherwise utilize user data for applications outside the scope of Third-Party Service, unless otherwise clearly stated by Developer and explicitly agreed to by User.

5.3. Without limiting section 6.2., private user information will not be transferred or made accessible to any third party, except as stipulated by Policy and agreed to by User.

5.4. In any event, Developer will only collect or otherwise aggregate user data in compliance with applicable laws, third-party store terms, and for no other purposes than those clearly stated in Policy and necessary to furnish and enhance the functionality of Third-Party Service.

6.1. Developer employs robust security measures to protect the integrity and confidentiality of all data it processes. User information is handled, transferred and stored in compliance with applicable laws, including all necessary precautions to prevent unauthorized access, modification, deletion, or distribution.

6.2. Developer will never share user data with third parties, including with Developer’s own additional services or bots (if any, as the case may be) unless explicitly authorized by User or required by law, such as in response to a lawful court order.

7.1. Telegram may:

(a) delete data sent from User to Third-Party Service from its servers in response to abuse of Platform by either User or Developer. This deletion may include sent messages, mini app cloud storage, the entire chat with Third-Party Service, or Third-Party Service itself as the case may be;

7.2. Developer may:

(a) seek verification of the identity of the User submitting data requests if they suspect unauthorized access to or misuse of personal information;

(b) impose reasonable limits on the number of data requests User can submit within a given timeframe, in order to prevent abuse of the request system. In any event, these limits cannot undermine User’s rights under applicable law;

7.3. Developer shall:

(a) comply with the stipulations set forth in Policy, or those outlined in any additional or substitute Policy they choose to enact, provided that neither can supersede the Telegram Terms of Service, and, by extension, the Telegram Bot Developer Terms;

(b) provide an easily accessible avenue for User to consult Policy, and for them to exercise all rights Policy entitles them to under applicable law;

(c) promptly process and respond to lawful requests from users within the timeframes allowed by applicable law, and, in any event, no later than 30 days from the date the request was submitted.

7.3. User may:

(a) submit a request to Developer for a copy of all personal data Third-Party Service collected and stored in connection with them;

(b) submit a request to Developer for the timely deletion of all personal data Third-Party Service collected and stored in connection with them, with the exception of essential data that Developer may preserve if and as permitted by applicable law. Examples of essential data vary by jurisdiction and may include but are not limited to data required for performing legal obligations, defense of legal claims, public interest or transactional history for the purpose of fulfilling tax obligations;

(c) amend, restrict, or object to the processing of their data, or exercise the option to revoke any previously given consent at any time and for any reason, including withdrawing from Policy entirely and discontinuing their use of Third-Party Service;

(d) lodge a complaint with national data protection authorities having jurisdiction if they believe their rights are not being upheld by Developer.

7.4. User shall:

(a) provide accurate and up-to-date information when submitting data requests to Developer, and cooperate with any reasonable measures necessary for Developer to fulfill these requests;

(b) adhere to the terms set forth in Policy and any additional policy enacted by Developer or Telegram.

While we do not anticipate frequent changes, we will review and may update this Privacy Policy from time to time. Any changes to this Privacy Policy will become effective when we post the revised Privacy Policy on this page https://telegram.org/privacy-tpa. Please check our website frequently to see any updates or changes to this Privacy Policy, a summary of which we will set out below.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
