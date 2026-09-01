---
item_id: "3bbe2d4a-1aed-48f0-b3f4-49961da32640"
platform: article
external_id: "461904727fd2"
canonical_url: "https://telegram.org/faq"
channel: "Telegram"
captured_at: 2026-08-28
status: archived
triage: archive
tags: ["telegram", "telegram-bot", "privacy-mode", "grupos-telegram", "chats-secretos", "gdpr", "miniapps", "bot-api"]
applicability:
  saas_pessoal: media
  projeto_cliente: baixa
  estudo_geral: alta
confidence: alta
theme: seguranca-e-privacidade
content_type: article
---

# Telegram FAQ — grupos, chats secretos, bots, privacy mode, GDPR e miniapps

🔗 https://telegram.org/faq

## Resumo

O FAQ oficial do Telegram cobre o funcionamento da plataforma de ponta a ponta. Grupos comportam até 200.000 membros, podem ser públicos ou privados, têm administradores com privilégios granulares e um interruptor de histórico persistente que decide se membros novos leem as mensagens antigas. A arquitetura de dados tem duas camadas: chats na nuvem (privados e grupos) usam criptografia cliente-servidor e ficam nos servidores do Telegram, acessíveis de qualquer dispositivo; chats secretos usam criptografia de ponta a ponta, são específicos do dispositivo, ficam fora da nuvem, não permitem encaminhamento e suportam autodestruição — e por isso bots e grupos não existem dentro deles. Sobre bots: são programas de terceiros feitos sobre a Bot API; veem nome público, username e foto do usuário, nunca o telefone (a menos que o usuário entregue); em grupos operam em dois modos — por padrão o privacy mode faz o bot ver só mensagens dirigidas a ele, e quando o desenvolvedor o desativa o bot vê tudo, o que fica visível na lista de membros como 'tem acesso às mensagens'. O FAQ recomenda não adicionar bots não confiáveis a grupos com informação sensível e tratá-los como estranhos (nunca dar senhas ou códigos). Sobre GDPR: o Telegram afirma não usar dados para anúncios nem vendê-los, e oferece o bot @EURegulation para pedir cópia dos dados. Miniapps são aplicativos completos rodando dentro do Telegram sobre a plataforma de bots, com loja própria, pagamentos e assinaturas via Telegram Stars e programas de afiliados. A API é aberta (Bot API para bots; API principal para clientes) e todos os apps de usuário são open source com builds verificáveis.

## Tópicos

- **Grupos** — Até 200.000 membros, públicos ou privados; admins com privilégios granulares; histórico persistente configurável (membro novo lê ou não o passado); mensagens fixadas.
- **Chats na nuvem vs. chats secretos** — Nuvem: criptografia cliente-servidor, multi-dispositivo, armazenado nos servidores. Secretos: ponta a ponta, específicos do dispositivo, sem encaminhamento, com autodestruição; perdidos ao sair da conta.
- **Bots e privacy mode** — Por padrão o bot em grupo só vê mensagens dirigidas a ele ('não tem acesso às mensagens' na lista de membros); com privacy mode desativado vê tudo e a lista exibe 'tem acesso às mensagens'.
- **Segurança dos bots** — Bots veem nome público, username e foto; nunca o telefone. Tratar como estranhos (sem senhas ou códigos); para parar um, bloquear como usuário humano ou usar comando de silêncio do dev.
- **GDPR e privacidade** — Telegram diz não usar dados para segmentar anúncios nem vendê-los; bot @EURegulation fornece cópia dos dados; infraestrutura distribuída exige múltiplas ordens judiciais de jurisdições diferentes; '0 bytes' de mensagens entregues a terceiros até hoje.
- **Miniapps** — Aplicativos completos dentro do Telegram, sobre a plataforma de bots: interface própria, loja de miniapps, tela cheia, pagamentos e assinaturas via Telegram Stars, programas de afiliados.
- **API aberta** — Bot API para construir bots e aceitar pagamentos; API principal aberta para clientes alternativos; apps de usuário 100% open source com builds verificáveis iOS/Android.

## Ferramentas citadas

- **BotFather**: citado indiretamente como caminho oficial de criação de bots via Bot API
- **Telegram Bot API**: plataforma para criar bots, integrar serviços e aceitar pagamentos
- **@EURegulation**: bot oficial para pedir cópia dos dados pessoais e tratar assuntos GDPR
- **Telegram Stars**: moeda interna para venda de itens digitais e assinaturas em miniapps

## Pontos-chave

- Privacy mode de um bot é AUDITÁVEL a olho nu: a lista de membros do grupo mostra 'tem acesso às mensagens' quando está OFF — serve de verificação de setup no grupo dos Satélites
- Bots nunca veem o número de telefone do usuário, só nome público, username e foto
- Chats secretos ficam fora da nuvem e são específicos do dispositivo — bots e grupos não funcionam neles; todo grupo é chat na nuvem (servidores do Telegram)
- Histórico persistente de grupo é configurável: desligado, membro novo não lê o passado
- Grupos privados: o Telegram declara não processar solicitações de terceiros sobre eles (só conteúdo público é moderado)
- FAQ recomenda explicitamente não adicionar bots não 100% confiáveis a grupos com informação sensível
- Sair da conta apaga todos os chats secretos do dispositivo; mudar de número mantém tudo
- Miniapps monetizam via Telegram Stars (itens digitais, assinaturas, afiliados) — canal de distribuição/receita dentro da plataforma
- Chamadas em grupo até 200 participantes; grupos até 200.000 membros; canais com público ilimitado
- Telegram afirma ter entregue 0 bytes de mensagens de usuários a governos/terceiros até hoje

## Como aplicar

No multi-bot dos Satélites: usar a lista de membros como verificação de aceite (só a Stella com 'tem acesso às mensagens'), criar o grupo privado com histórico persistente desligado, e lembrar que o grupo vive na nuvem do Telegram — nada de colar segredos lá. Miniapps + Telegram Stars ficam anotados como possível canal de monetização se o SaaS ganhar presença no Telegram.

## 📚 Pythagoras diz

O registro diz — e agora fica dito aqui também: privacy mode é visível na lista de membros, chats secretos não abrigam bots, e histórico persistente se desliga. Eu deduzo que as três coisas viram critérios de aceite do grupo dos Satélites, e duas já viraram. A lacuna que marco: o FAQ aponta uma 'Bots FAQ' para desenvolvedores que não capturamos — se a Story 1b tropeçar em detalhe de API, é lá que está.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Este FAQ fornece respostas para perguntas básicas sobre o Telegram.

Confira nossa FAQ avançada para informações mais técnicas.


O Telegram está sempre evoluindo e adicionando novos recursos. Portanto, este documento pode conter informações desatualizadas. Esperamos terminar de atualizar as perguntas frequentes, manuais de bots e outros documentos dentro de alguns meses.


O Telegram é um aplicativo de mensagens com foco em velocidade e segurança, é super-rápido, simples e gratuito. Você pode usar o Telegram em todos os seus dispositivos **ao mesmo tempo** — suas mensagens são sincronizadas perfeitamente em qualquer quantidade de seus telefones, tablets ou computadores. O Telegram tem mais de **1 bilhão** de usuários ativos mensais e é um dos **5 aplicativos mais baixados** do mundo.

Com o Telegram, você pode enviar mensagens, fotos, vídeos e **arquivos** de qualquer tipo (doc, zip, mp3, etc), além de criar grupos de até  **200.000** pessoas ou canais para transmitir para públicos **ilimitados**. Você pode escrever para seus contatos da agenda e encontrar pessoas pelos **nomes de usuário** delas. Como resultado, o Telegram é como SMS e e-mail combinados – e pode cuidar de todas as suas necessidades de mensagens pessoais ou comerciais. Além disso, oferecemos suporte a **chamadas de voz** e **videochamadas** criptografadas de ponta a ponta, **chamadas em grupo** para até 200 participantes, e **chats de voz** em grupos que os membros podem entrar quando quiserem.

Siga nosso **Canal de Dicas** para saber mais sobre os recursos do Telegram.


O Telegram é para todos que querem mensagens rápidas, confiáveis e chamadas. Usuários de negócios e pequenas equipes podem gostar dos grandes grupos, nomes de usuário, aplicativos para desktop e opções poderosas para compartilhamento de arquivos.

Como os grupos do Telegram podem ter até 200.000 membros, temos compatibilidade com respostas, menções e hashtags que ajudam a manter a ordem e manter a comunicação em grandes comunidades eficiente. Você pode nomear administradores com ferramentas avançadas para ajudar essas comunidades a prosperar em paz. Qualquer pessoa pode entrar em grupos públicos e são plataformas poderosas para discussões e coleta de feedback.

Se você gosta mais de imagens, o Telegram tem pesquisa de GIFs animados, um editor de fotos muito avançado, e uma plataforma aberta de stickers (encontre alguns stickers legais aqui, ou aqui. Além disso, não há necessidade de se preocupar com o espaço em disco no seu dispositivo. Com o suporte à nuvem do Telegram e as opções de gerenciamento de cache, o Telegram pode ocupar quase **zero** de espaço no seu telefone.

Aqueles que procuram privacidade adicional podem verificar nossas configurações avançadas e a revolucionária política de privacidade. E se você quiser sigilo, experimente nossos Chats Secretos específicos por dispositivo, com mensagens, fotos e vídeos autodestrutivos — e bloqueie seu aplicativo com uma senha de bloqueio.

Estamos sempre evoluindo — confira nossa Breve História do Telegram e siga-nos no Twitter e no Telegram para ficar por dentro das novidades.


Ao contrário do WhatsApp, o Telegram é um mensageiro baseado em nuvem com sincronização contínua. Como resultado, você pode acessar suas mensagens de vários dispositivos ao mesmo tempo, incluindo tablets e computadores, e compartilhar um número ilimitado de fotos, vídeos e arquivos (doc, zip, mp3, etc.) de até **2 GB** *cada*.

O Telegram precisa de menos de **100 MB** no seu dispositivo – você pode manter **todas as suas mídias** na nuvem sem precisar apagar nada – basta limpar o cache para liberar espaço.

Graças à nossa infraestrutura de múltiplos data centers e criptografia, o Telegram é mais rápido e muito mais seguro. Além disso, conversas privadas no Telegram são gratuitas e continuarão gratuitas — sem anúncios, sem taxas de assinatura, para sempre.

A API e o código do Telegram são abertos, e os desenvolvedores são bem-vindos para criar seus próprios aplicativos do Telegram. Também temos a Bot API, uma plataforma para desenvolvedores que permite a qualquer pessoa construir facilmente ferramentas especializadas para o Telegram, integrar quaisquer serviços e até mesmo aceitar pagamentos de usuários de todo o mundo.

E essa é apenas a ponta do iceberg.

O Telegram para iOS foi lançado em 14 de agosto de 2013. A versão alfa do Telegram para Android foi lançada oficialmente em 20 de outubro de 2013. Mais e mais clientes para o Telegram aparecem, construídos por desenvolvedores independentes usando a plataforma aberta do Telegram.

Você pode usar o Telegram em celulares, tablets e até mesmo em computadores. Temos aplicativos para iOS (13.0 e superior), Android (5.0 e superior), um aplicativo nativo para macOS e um aplicativo universal para desktop (disponível aqui) para Windows, macOS e Linux. O Telegram Web também pode ajudar você a fazer o que precisar rapidamente em qualquer lugar.

Você pode fazer login no Telegram a partir de quantos dispositivos desejar — tudo **ao mesmo tempo**. Basta usar o número do seu celular para fazer login em todos os lugares, e suas conversas na nuvem serão sincronizadas instantaneamente.


Nossa API é aberta para desenvolvedores, caso você queira criar seus próprios aplicativos para outras plataformas.

O Telegram é apoiado por Pavel Durov e seu irmão Nikolai. Pavel apoia financeiramente e ideologicamente o Telegram, enquanto a contribuição de Nikolai é tecnológica. Para tornar o Telegram possível, Nikolai desenvolveu um protocolo de dados personalizado e exclusivo, que é aberto, seguro e otimizado para o trabalho com vários data centers. Como resultado, o Telegram combina segurança, confiabilidade e velocidade em qualquer rede.

Veja também: artigos sobre o Telegram.


A equipe de desenvolvimento do Telegram está sediada em Dubai.

A maioria dos desenvolvedores por trás do Telegram vem originalmente de São Petersburgo, a cidade famosa por seu número sem precedentes de engenheiros altamente qualificados. A equipe do Telegram teve que deixar a Rússia devido às regulamentações locais de TI e tentou vários locais como sua base, incluindo Berlim, Londres e Singapura. No momento, estamos felizes em Dubai, mas estamos prontos para nos mudar novamente se as regulamentações locais mudarem.

Não. Veja este post para detalhes.

Acreditamos em mensagens rápidas e seguras que também são 100% gratuitas.

Nosso fundador e CEO Pavel Durov, que financiou o Telegram durante a maior parte de sua história, planejou uma **estratégia para tornar o Telegram sustentável** neste post.

Seguindo esse plano, o Telegram implementou formas sustentáveis de monetização que priorizam seus usuários:

- Em 2021, o Telegram lançou as Mensagens Patrocinadas – anúncios minimalistas e que respeitam a privacidade que podem aparecer em determinados canais públicos.
- Em 2022, o Telegram lançou uma assinatura Premium que os usuários podem adquirir para oferecer suporte ao aplicativo e desbloquear recursos adicionais exclusivos.

Esses fluxos de receita nos ajudam a pagar os custos de infraestrutura e os salários dos desenvolvedores; no entanto, obter lucros nunca será o objetivo final do Telegram.

Saiba mais sobre assinaturas na FAQ do Telegram Premium.


No Telegram, acreditamos que os dois componentes mais importantes da privacidade na Internet devem ser:

1. Proteger suas conversas privadas de terceiros bisbilhoteiros, como funcionários, empregadores, etc.
2. Proteger seus dados pessoais de terceiros, como profissionais de marketing, anunciantes, etc.

O objetivo do Telegram é criar um mensageiro verdadeiramente livre, com uma política de privacidade revolucionária.

A Regulação Geral de Proteção de Dados (GDPR) entrou em vigor na Europa em 25 de maio de 2018. Como o direito à privacidade foi o motivo pelo qual fizemos o Telegram, não tínhamos muito o que mudar. Não usamos seus dados para a segmentação de anúncios, não os vendemos para outras pessoas e não fazemos parte de nenhuma ~~máfia~~ “família de empresas”.

O Telegram mantém apenas as informações necessárias para funcionar como um serviço em nuvem rico em recursos — por exemplo, seus chats na nuvem para que você possa acessá-los de qualquer dispositivo sem usar backups de terceiros, ou seus contatos para poder facilitar o envio de mensagens para seus amigos e familiares no Telegram. Por favor, consulte nossa Política de Privacidade para mais informações.

Você pode usar o **@EURegulation** para:

- Solicitar uma cópia de todos os seus dados que o Telegram armazena.
- Entrar em contato conosco sobre privacidade de dados.

Todos os aplicativos do Telegram possuem botões de **'Denunciar'** que permitem que você sinalize conteúdo ilegal para nossos moderadores — com apenas alguns toques.

No Telegram para Android, toque na mensagem e selecione *Denunciar* no menu. No iOS, pressione e segure a mensagem. No Telegram Desktop, Web ou Telegram para macOS, clique com o botão direito na mensagem e selecione *Denunciar*. Em seguida, escolha o motivo apropriado.

Você também pode usar nosso e-mail automatizado de remoção abuse@telegram.org. Se for enviar um pedido de remoção por e-mail, certifique-se de incluir **links** (como `t.me/...` ou `@...`) para o conteúdo no Telegram que você acha que precisa de atenção dos nossos moderadores.

Usuários da União Europeia podem consultar as Orientações para Usuários na Lei de Serviços Digitais da UE para as opções de denúncia relevantes.

Nota: Se um golpista estiver fingindo ser você, entre em contato com @NoToScam.


O Regulamento (UE) 2021/784 do Parlamento Europeu e do Conselho de 29 de abril de 2021 sobre o tratamento da disseminação de conteúdo terrorista online (Terrorist Content Online Regulation, ou TCO) permite que as autoridades dos países da UE enviem pedidos de remoção de conteúdo terrorista, se for descoberto na plataforma pública do Telegram. Também designamos um terceiro, o Representante Europeu de Serviços Digitais (EDSR, na sigla em inglês), para nos dar assistência com as comunicações relacionadas ao TCO.

Os usuários cujas publicações foram removidas em conexão com o Regulamento TCO podem solicitar detalhes sobre o motivo pelo qual suas publicações foram consideradas terroristas e como contestar a remoção:

- escrevendo para EDSR na Avenue Huart Hamoir 71, 1030 Bruxelas, Bélgica, ou
- entrando em contato com o bot @EURegulation no Telegram e usando o comando `/tco_ask` .

As solicitações podem ser feitas em inglês e francês.

**Grupos e chats privados** no Telegram são privados entre seus participantes. Não processamos nenhuma solicitação relacionada a eles. No entanto, o Telegram também oferece suporte a **pacotes de stickers**, **bots**, **canais** e **grupos** que são *disponíveis publicamente*.

Se você vir um bot, canal, pacote de stickers ou outro conteúdo que faça parte da plataforma pública do Telegram e que esteja infringindo seus direitos autorais, envie uma reclamação para dmca@telegram.org. Observe que tais solicitações devem ser enviadas apenas pelo proprietário dos direitos autorais ou por um agente autorizado a agir em nome do proprietário.

Nossa missão é fornecer um meio de comunicação seguro que funcione em qualquer lugar do planeta. Para fazer isso nos lugares onde é mais necessário (e continuar distribuindo o Telegram pela App Store e Google Play), temos que processar solicitações legítimas para remover conteúdo **público** ilegal (por exemplo, pacotes de stickers, bots, grupos e canais) dentro do aplicativo. Por exemplo, podemos remover pacotes de stickers que violam direitos de propriedade intelectual ou bots pornográficos.

Conteúdo público no Telegram, como pacotes de stickers enviados por usuários, canais e bots por desenvolvedores terceirizados não fazem parte da interface principal do Telegram. Sempre que recebemos uma denúncia sobre conteúdo público potencialmente ilegal, realizamos as verificações legais necessárias e o removemos quando considerado apropriado.

Observe que isso **não** se aplica a restrições locais à liberdade de expressão. Por exemplo, se criticar o governo for ilegal em algum país, o Telegram não fará parte dessa censura com motivação política. Isso vai contra os princípios dos nossos fundadores. Embora bloqueemos bots e canais terroristas (por exemplo, relacionados ao ISIS), não bloquearemos ninguém que expresse pacificamente opiniões alternativas.

Se você acredita que seu bot, canal ou pacote de sticker foi banido sem razões óbvias, envie-nos uma mensagem em abuse@telegram.org.

Chats secretos usam criptografia de ponta a ponta, graças à qual não temos dados para revelar ou compartilhar.

Para proteger os dados que não são cobertos pela criptografia de ponta a ponta, o Telegram usa uma infraestrutura distribuída. Os dados do chat na nuvem são armazenados em vários datacenters ao redor do mundo que são controlados por diferentes entidades legais espalhadas por diferentes jurisdições. As chaves de descriptografia relevantes são divididas em partes e nunca são mantidas no mesmo lugar que os dados que protegem. Como resultado, várias ordens judiciais de diferentes jurisdições são necessárias para nos forçar a revelar quaisquer dados.

Graças a essa estrutura, podemos garantir que nenhum governo ou bloco de países com ideias semelhantes possa invadir a privacidade e a liberdade de expressão das pessoas. O Telegram pode ser forçado a revelar dados somente se um problema for grave e universal o suficiente para passar pelo escrutínio de vários sistemas legais diferentes ao redor do mundo.

Até hoje, divulgamos 0 bytes de mensagens de usuários para terceiros, incluindo governos.

Para obter mais informações sobre como seus dados são protegidos, consulte a Política de Privacidade do Telegram e este post do CEO do Telegram.


Você pode escrever para as pessoas que estão nos contatos do seu telefone e usam o Telegram. Outra maneira de entrar em contato com as pessoas é digitar o nome de usuário do Telegram delas no campo de busca — você não precisa saber o número de telefone delas para isso.

As pessoas podem entrar em contato com você no Telegram se **souberem seu número de telefone** ou se você **iniciar uma conversa com elas primeiro**.

Se não souberem seu número de telefone, podem encontrar você nos seguintes casos:

- Quando ambos forem membros do **mesmo grupo** .
- Se você definir um **nome de usuário público** . Outros podem usar a**Busca Global** para encontrar você pelo nome de usuário.

O Telegram permite que serviços de terceiros enviem códigos de verificação para os usuários deles pelo Telegram. Esses códigos aparecem apenas no **chat verificado *'Códigos de Verificação'*** e permitem que você toque para copiar instantaneamente o código.

Serviços que não especificam um nome ou foto de perfil para seus códigos aparecerão com o nome e foto padrão de *'Códigos de Verificação'*.


Se você receber um código no chat *'Códigos de Verificação'*, provavelmente foi porque solicitou um login em um serviço de terceiros, como um **site externo, aplicativo ou marketplace**. Também é possível que outra pessoa tenha inserido seu número de telefone por engano ao tentar fazer login em outro serviço. **De qualquer forma, sua conta do Telegram está completamente segura** — se você não solicitou um código, basta tocar nele e selecionar *'Denunciar'*, sem necessidade de qualquer outra ação.

Os serviços de terceiros determinam como seus códigos de verificação serão enviados – o Telegram não consegue controlar isso nem informar as preferências de envio de um serviço. Diferente de códigos SMS que frequentemente falham ou podem ser interceptados, os códigos enviados via Telegram são **entregues instantaneamente** e **criptografados de forma segura** – tornando-os mais confiáveis e seguros para usuários e serviços.

A conversa *'Códigos de Verificação'* é usado apenas para códigos de **serviços de terceiros**. Os códigos de login da sua conta do Telegram são enviados para o **chat de notificações de serviço verificado** chamado *'Telegram'* na sua lista de conversas e **nunca devem ser compartilhados** com outras pessoas, incluindo outros serviços ou aplicativos.

Se você deseja economizar e aumentar a eficiência ao enviar códigos de verificação para seu aplicativo ou serviço via Telegram, confira o Telegram Gateway.


Seus contatos que têm o Telegram são mostrados no topo da lista de Contatos. Eles também possuem fotos.

*iOS:* Os convites básicos são mensagens SMS simples. O envio de SMS é cobrado de acordo com o seu plano na sua operadora (a menos que seja enviado via iMessage). Naturalmente, você tem outras opções para trazer seus amigos para cá. Envie um link de download através de qualquer outro serviço de mensagens: email, Facebook, WhatsApp, um telegrama real — a escolha é sua. O link: **https://telegram.org/dl/**

*Android:* Abra o menu do aplicativo (deslize para a direita na lista de chats) > Convidar Amigos. Em seguida, escolha o aplicativo através do qual você gostaria de enviar os convites.

Você pode informar a seus amigos um link t.me com o seu nome de usuário para que eles possam encontrá-lo facilmente no Telegram, mesmo que eles não tenham o seu número de telefone.


*Um traço* — mensagem entregue à nuvem do Telegram e seu amigo foi notificado, se ele permitir notificações.*Dois traços* — mensagem lida (seu amigo abriu o Telegram e abriu a conversa com a mensagem).

Não temos um status de “mensagem entregue ao dispositivo” porque o Telegram pode ser usado em quantos dispositivos você desejar ao mesmo tempo. Como saber qual dispositivo em particular seria esse?

Você pode escolher quem vê essas informações nas configurações de Privacidade e Segurança do Telegram.

Lembre-se de que você não verá o horário do Visto por Último de pessoas com quem você não compartilha o seu. Você verá, no entanto, um Visto por Último aproximado. Isso mantém os stalkers afastados, mas torna possível entender se uma pessoa é alcançável pelo Telegram. Existem quatro valores aproximados possíveis:

- **Visto recentemente** - abrange qualquer período entre 1 segundo e 2-3 dias
- **Visto na última semana** — entre 2, 3 e sete dias
- **Visto no último mês** — entre 6, 7 dias e um mês
- **Visto há muito tempo** — mais de um mês (isso também é sempre exibido para usuários bloqueados)

As regras do visto por último também se aplicam ao seu status online. As pessoas só podem ver você online se você estiver compartilhando seu status visto por último com elas.

Existem algumas exceções porque às vezes é óbvio que você está online. Independentemente das configurações de Visto por Último, as pessoas verão você online por um breve período (~30 segundos) se você fizer o seguinte:

- Enviar uma mensagem em um chat privado ou em um grupo em que ambos são membros.
- Ler uma mensagem que eles te enviaram em um chat privado.
- Transmitir um status “digitando…” para o chat privado com eles ou em um grupo no qual ambos são membros.

Se você não está compartilhando seu Visto por Último com alguém e não fizer nenhuma das ações acima, eles nunca verão você online. Outra maneira de conseguir isso é bloquear essa pessoa.

Sim. Você sempre pode apagar qualquer mensagem que **enviou** ou **recebeu** para *ambos os lados* em *qualquer* conversa individual (em grupos, ainda são apenas as suas próprias mensagens). Você também pode limpar o histórico inteiro do chat para ambas as partes. No Telegram, mensagens apagadas não deixam rastros no chat.

Junto com as configurações de privacidade para mensagens encaminhadas, isso torna a troca de mensagens no Telegram parecida com uma conversa cara a cara (sem gravador). Como resultado, os usuários não precisam mais se preocupar com o acúmulo de dados em seus chats ao longo dos anos. Ambas as partes de uma conversa têm controle total sobre o que pertence, ou não, à sua identidade online.

Sim. Você pode fazer Chamadas de Voz e Chamadas de Vídeo criptografadas de ponta a ponta, e pode transformar qualquer chamada em uma Chamada em Grupo com até **200 participantes** — também protegida por criptografia de ponta a ponta, que você pode verificar a qualquer momento.

Os participantes podem enviar comentários e reações diretamente dentro da chamada, sem interromper o áudio.

Se você quiser um chat de áudio contínuo que os membros de um grupo possam entrar quando quiserem, você também pode iniciar um Chat de Voz em qualquer grupo — útil como um escritório virtual ou um bate-papo informal.

Digite **uma palavra** no seu campo de digitação para receber sugestões de emoji relevantes. Você também pode digitar “:” seguido de qualquer palavra-chave para abrir a **busca de emojis** – como *:coracao*.

Você pode sugerir palavras-chave que faltam para emojis no seu idioma usando esta interface.

Os grupos do Telegram podem ter até **200.000 membros** cada e são ferramentas de comunicação extremamente poderosas. Aqui estão alguns recursos importantes que os destacam no mundo das mensagens:

**Histórico unificado**

Edite suas mensagens após enviar, apague-as para que elas desapareçam para todos.

**Disponibilidade entre plataformas**

Acesse suas mensagens a qualquer momento, de qualquer um de seus celulares, tablets ou computadores.

**Busca instantânea**

Encontre a mensagem que você está procurando, mesmo entre milhões. Filtre por autor para encontrar mais facilmente.

**Respostas, menções e hashtags**

Mantenha facilmente uma conversa e tenha uma comunicação eficiente, não importando o tamanho do grupo.

**Notificações importantes**

Silencie o grupo para receber notificações apenas quando as pessoas mencionarem você ou responderem às suas mensagens.

**Mensagens fixadas**

Você pode fixar qualquer mensagem para ser exibida na parte superior da tela do chat. Todos os membros receberão uma notificação — mesmo que tenham silenciado as mensagens comuns do seu grupo.

**Ferramentas de moderação**

Adicione administradores que podem apagar mensagens em massa, controlar a entrada de usuários e fixar mensagens importantes. Defina os privilégios de administrador com precisão granular.

**Ferramentas antispam**

Em grupos grandes, ative o Antispam Agressivo para usar o conjunto completo de ferramentas antispam do Telegram no seu chat.

**Permissões do grupo**

Defina permissões padrão para impedir que os membros publiquem tipos específicos de conteúdo. Ou até mesmo restringir os membros de enviarem mensagens completamente — e permitir que os administradores conversem entre si enquanto todos os outros assistem.

**Compartilhamento de arquivos**

Envie e receba arquivos de qualquer tipo, com até 2 GB de tamanho cada (ou 4 GB com o Premium), e acesse-os instantaneamente em seus outros dispositivos.

**Tópicos**

Divida as discussões do grupo em tópicos — cada um com seu próprio histórico de chat, mídia compartilhada e configurações de notificação, como fóruns clássicos.

**Grupos públicos**

Receba um link curto para o seu grupo e torne-o público, como o t.me/publictestgroup. Dessa forma, qualquer pessoa pode visualizar todo o histórico de chat do grupo e participar para postar mensagens.

**Impulsos de grupo**

Os membros podem impulsionar um grupo com a assinatura Premium para desbloquear recursos para todos — como postar stories, pacotes de emoji personalizados, voz para texto e aparência de grupo personalizada.

**Customização via bots**

Crie ferramentas personalizadas para qualquer necessidade específica usando nossa Bot API e Bots Inline.

**Saindo de um grupo de forma organizada**

Se você é o dono e quer sair do grupo, escolha um novo dono enquanto faz isso, para que o grupo continue funcionando.

**Grupos** do Telegram são ideais para compartilhar coisas com amigos e familiares ou para colaboração em pequenas equipes. Mas os grupos também podem crescer muito e ter suporte a comunidades de até **200.000 membros**. Você pode tornar qualquer grupo **público**, alternar o **histórico persistente** para controlar se novos membros têm acesso às mensagens anteriores e nomear **administradores** com privilégios granulares. Você também pode fixar mensagens importantes no topo da tela para que todos os membros possam vê-las, incluindo aqueles que acabaram de entrar.

**Canais** são uma ferramenta para transmitir mensagens para grandes públicos. Na verdade, um canal pode ter um número ilimitado de inscritos. Quando você publica em um canal, a mensagem é assinada com o nome e a foto do canal e não com o seu. Cada mensagem em um canal tem um **contador de visualizações** que é atualizado quando a mensagem é visualizada, incluindo as cópias encaminhadas da mensagem.

*iOS:* Inicie uma nova mensagem (toque no ícone no canto superior direito em Chats) > “Novo Grupo”.*Android:* Toque no ícone de lápis circular na lista de chats > “Novo Grupo”.*Telegram Desktop:* Clique no botão de menu no canto superior esquerdo > “Novo Grupo”.

Você pode adicionar administradores para te ajudar a gerenciar o seu grupo e pode definir as permissões deles com precisão granular.

*iOS*: Vá para Info do Grupo (abra o grupo e toque na foto no canto superior direito) > Editar > Administradores.*Android*: Vá para Info do Grupo (abra o grupo e toque no nome do grupo no cabeçalho) > toque no ícone de lápis (no canto superior direito) > Administradores.*Telegram Desktop*: Abra o grupo e clique em ‘…’ no canto superior direito > Gerenciar grupo > Administradores.

Você pode adicionar seus contatos ou usar a busca por nome de usuário.

É fácil migrar grupos existentes para o Telegram enviando para as pessoas um **link de convite**. Para criar um link de convite, vá para *Info do Grupo > Adicionar Membros > Convidar via link*.

Qualquer pessoa que tenha o Telegram instalado poderá participar do seu grupo seguindo este link. Se você optar por revogar o link, ele deixará de funcionar imediatamente.

Sim. Donos de canais podem ativar as Mensagens Diretas para que os assinantes possam enviar mensagens privadas a eles — sem que o dono do canal precise compartilhar sua conta pessoal.

Os assinantes também podem sugerir publicações para o canal — inclusive sugestões pagas. O dono pode revisá-las, editá-las, agendá-las ou rejeitá-las. Isso dá aos canais uma forma clara de obter conteúdo colaborativo ou trabalhar com marcas.

Você pode configurar um nome de usuário **público** no Telegram. A partir daí, é possível que outros usuários encontrem você por esse nome de usuário. Você aparecerá na busca de contatos na seção “Busca global”. Observe que as pessoas que encontrarem você poderão enviar mensagens para você, mesmo que não saibam seu número de telefone. Se você não está confortável com isso, desaconselhamos configurar um nome de usuário no Telegram.

Você pode configurar um nome de usuário em Configurações e usar a caixa de busca global na lista de chats para buscar por chats, mensagens e nomes de usuários.

Nomes de Usuário Colecionáveis funcionam exatamente como os nomes de usuário básicos, eles aparecem nos resultados da Busca Global e têm seus próprios links que podem ser usados fora do Telegram: usuario.t.me e t.me/usuario.

Eles podem ser comprados e vendidos por meio de plataformas de terceiros, como Fragment, oferecendo uma maneira **simples** e **segura** de adquirir e trocar domínios valiosos do Telegram. A aquisição de um nome de usuário colecionável fornece propriedade permanente, verificada pelo blockchain TON. Os proprietários de nomes de usuário colecionáveis podem livremente **atribuí-los** a chats, **vendê-los** ou **guardá-los** para uso posterior.

Um único usuário, grupo ou canal pode ter vários nomes de usuário colecionáveis apontando para ele ao mesmo tempo. Cada um tem seu próprio link `t.me/nomedeusuario` e endereço `nomedeusuario.t.me`.

Depois de configurar um nome de usuário, você pode fornecer às pessoas um link como este: t.me/NomesDeUsuario. Abrir esse link no telefone abrirá automaticamente o aplicativo do Telegram e abrirá um chat com você. Você pode compartilhar links de nome de usuário com amigos, escrevê-los em cartões de visita ou colocá-los em seu site.

Dessa forma, as pessoas podem entrar em contato com você pelo Telegram sem saber o seu número de telefone.

Se não quiser criar um nome de usuário público e não se importar em compartilhar seu número, você também pode criar um link t.me com seu número de telefone em **formato internacional** – por exemplo, **t.me/+123456789**. Esse tipo de link pode abrir rapidamente um chat com você em qualquer aplicativo, mas só funcionará se suas configurações de privacidade permitirem que outras pessoas encontrem você pelo seu número de telefone.

Você pode usar a-z, 0-9 e sublinhados (letras, números e underline). Os nomes de usuário não diferenciam maiúsculas de minúsculas, mas o Telegram armazenará suas preferências de capitalização (por exemplo, Telegram e TeleGram são o mesmo usuário).

Você não precisa necessariamente configurar um. Lembre-se de que os nomes de usuários do Telegram são públicos e que a escolha de um nome de usuário no Telegram possibilita que as pessoas encontrem você na busca global e enviem mensagens, mesmo que não tenham seu número de telefone. Se você não está confortável com isso, desaconselhamos configurar um nome de usuário.

Não. Nenhum dos dois verá o número de telefone do outro (a menos que isso seja permitido pelas suas configurações de privacidade). Isso é semelhante ao que acontece quando você envia uma mensagem para uma pessoa que você conheceu em um grupo do Telegram.

Vá para Configurações e salve um nome de usuário vazio. Isso removerá seu nome de usuário; as pessoas não poderão mais encontrá-lo por meio da busca. Isso não afetará as conversas existentes.

Existem dois tipos de nome de usuário no Telegram, nomes de usuário básicos e nomes de usuário colecionáveis.

**Nomes de Usuário Básicos**

Os nomes de usuário **básicos** do Telegram são distribuídos por ordem de chegada.

Entendemos que certos nomes de usuário são parte da identidade online de alguns de nós. Se o nome de usuário desejado já estiver em uso e **não estiver registrado como colecionável**, podemos te ajudar a adquiri-lo para sua conta ou canal, desde que você tenha o mesmo nome de usuário em pelo menos dois destes serviços: Facebook, Twitter, Instagram.

Devido ao fato de que uma conta pode registrar vários nomes de usuário de bots e canais, reservamos o direito de recuperar nomes de usuário atribuídos a bots e canais não utilizados, bem como a nomes de usuário ocupados sem necessidade.

Para solicitar um nome de usuário, entre em contato com o @Username_bot.

**Nomes de Usuário Colecionáveis**

Se você deseja um nome de usuário colecionável, mas ele já está em uso, verifique se ele está disponível para venda. Não podemos atribuir nomes de usuário colecionáveis, eles só podem ser gerenciados por seus **respectivos proprietários**.

Se um golpista estiver se passando por você, entre em contato com @NoToScam.

Se você é um usuário avançado, talvez pode achar nosso FAQ for the Technically Inclined útil também.


O Telegram é mais seguro do que os mensageiros de mercado de massa, como o WhatsApp e o Line. Nós nos baseamos no protocolo MTProto (veja a descrição e a FAQ avançada), construído sobre algoritmos testados ao longo do tempo para tornar a segurança compatível com a alta velocidade de entrega e confiabilidade em conexões instáveis. Estamos continuamente trabalhando com a comunidade para melhorar a segurança de nosso protocolo e clientes.

Não se preocupe. Os chats secretos especiais do Telegram usam criptografia de ponta a ponta, não deixam rastros em nossos servidores, oferecem suporte a mensagens autodestrutivas e não permitem o encaminhamento. Além disso, os chats secretos não fazem parte da nuvem do Telegram e só podem ser acessados nos dispositivos em que foram iniciados.

Oferecemos suporte a duas camadas de criptografia segura. A criptografia cliente-servidor é usada em Chats na Nuvem (chats privados e em grupo), os Chats Secretos usam uma camada adicional de criptografia cliente-cliente. Todos os dados, independentemente do tipo, são criptografados da mesma maneira — seja texto, mídia ou arquivos.

Nossa criptografia é baseada em criptografia AES simétrica de 256 bits, criptografia RSA de 2048 bits e troca de chaves segura Diffie-Hellman. Você pode encontrar mais informações no FAQ Avançado.

Veja também: Vocês processam solicitações de dados?


O Telegram é aberto, qualquer um pode verificar nosso código-fonte, protocolo e a API, ver como tudo funciona e tomar uma decisão bem informada. O Telegram tem compatibilidade com builds verificáveis, que permitem que especialistas verifiquem de forma independente que o nosso código publicado no GitHub é **o mesmo exato código** usado para construir os apps que você baixa da App Store ou da Google Play.

Encorajamos especialistas em segurança a auditar o nosso sistema e ficamos gratos por qualquer feedback em security@telegram.org.

Além disso, o foco principal do Telegram não é gerar lucro, por isso os interesses comerciais nunca interferirão em nossa missão.

Quando falamos de chats secretos, você não precisa — apenas garanta que a chave visualizada em seu chat secreto é igual a de seu amigo nas configurações do chat secreto. Mais sobre isto abaixo.

Consulte esta página para obter os detalhes mais recentes sobre o Programa de Recompensa por Bugs do Telegram.


Qualquer um que afirme que as mensagens do Telegram podem ser decifradas é bem-vindo para provar a sua afirmação em nossa competição e ganhar US$ 300.000. Você pode verificar a descrição da competição para saber mais.

Quaisquer comentários sobre a segurança do Telegram são bem-vindos em security@telegram.org. Todos os envios que resultarem em uma mudança de código ou configuração são elegíveis a recompensas que variam de **US$ 100** a **US$ 100.000** ou mais, de acordo com a gravidade do problema. Por favor note que não podemos oferecer recompensas para problemas que são divulgados ao público antes de serem corrigidos.

O Telegram pode ajudar quando se trata de transferência de dados e comunicação segura. Isso significa que todos os dados (incluindo mídia e arquivos) que você envia e recebe via Telegram não podem ser decifrados quando interceptados pelo seu provedor de serviços de Internet, proprietários de roteadores Wi-Fi conectados a você ou outros terceiros.

Mas lembre-se de que não podemos protegê-lo de sua própria mãe se ela pegar seu telefone desbloqueado sem uma senha. Ou do seu departamento de TI, se eles acessarem seu computador no trabalho. Ou de qualquer outra pessoa que tenha acesso físico ou root aos seus telefones ou computadores que estejam executando o Telegram.

Se você tiver motivos para se preocupar com sua segurança pessoal, recomendamos usar somente Chats Secretos em aplicativos oficiais ou pelo menos de código-fonte aberto verificável para informações confidenciais, de preferência com um timer de autodestruição. Também recomendamos ativar a verificação em duas etapas e configurar uma senha forte para bloquear seu aplicativo. Você encontrará as duas opções em *Configurações > Privacidade e segurança*.

Fazer login com um código SMS é um padrão de indústria dos mensageiros, mas se você estiver procurando mais segurança ou tiver motivos para duvidar de sua operadora de celular ou do governo, recomendamos proteger seus chats na nuvem com uma senha adicional.

Você pode fazer isso em *Configurações > Privacidade e Segurança > Verificação em Duas Etapas*. Uma vez habilitada, você precisará do código SMS e também da sua senha para entrar. Você também pode definir um email para recuperação, que ajudará você obter acesso novamente caso esqueça sua senha. Se você fizer isso, lembre-se de que é importante que o email de recuperação também seja protegido com uma senha forte e Verificação em Duas Etapas, quando possível.

Veja isso, em Inglês, para dicas sobre como criar uma senha forte que seja fácil de lembrar.

Você também pode configurar uma Chave de Acesso para fazer login sem um código SMS, usando o PIN, a impressão digital ou o reconhecimento facial do seu dispositivo.

Usar um dispositivo com root ou jailbreak torna mais fácil para um atacante em potencial obter controle administrativo total sobre seu dispositivo — acesso root.

Um usuário com acesso root pode facilmente contornar os recursos de segurança embutidos no sistema operacional, ler memória de processos ou acessar áreas restritas, como o armazenamento interno. Uma vez que um atacante tem acesso root, quaisquer esforços para combater as ameaças se tornam inúteis. Nenhum aplicativo pode ser chamado de seguro sob estas circunstâncias, não importa quão forte é sua criptografia.

Cocoon é uma plataforma de IA segura, de código aberto e descentralizada que permite que aplicativos com foco em privacidade, como o Telegram, utilizem os modelos de IA mais recentes.

O Telegram desenvolveu a Cocoon e a utiliza para alimentar seus recursos de IA com segurança, sem depender de terceiros, garantindo que seus dados permaneçam **protegidos** e **inacessíveis**.

**Não**. Os recursos de IA do Telegram — incluindo tradução, tons personalizados, resumos por IA de publicações longas de canais e artigos de Instant View, e busca de figurinhas com IA — funcionam na Cocoon e **nunca enviam dados** para terceiros.

Quando você usa um recurso de IA fornecido pelo Telegram, o processamento ocorre em um ambiente altamente seguro, isolado e criptografado – seus dados permanecem inacessíveis.

Se você usar IA por meio de um bot ou miniapp de terceiros, você está usando um **serviço de terceiros**, não o Telegram. Consulte a política de privacidade desse bot para mais detalhes.


Os recursos de IA do Telegram, como tradução e tons personalizados, são alimentados pela Cocoon. A Cocoon é uma plataforma de IA segura, de código aberto e descentralizada que permite que aplicativos com foco em privacidade, como o Telegram, utilizem os modelos de IA mais recentes.

Ao usar um recurso de IA fornecido pelo Telegram, o processamento ocorre em um ambiente altamente seguro, isolado e criptografado – seus dados permanecem inacessíveis.

Observe que, se você acessar a IA por meio de um bot ou miniapp de terceiros, estará interagindo com um serviço de terceiros, não com o Telegram. Nesse caso, consulte a política de privacidade do bot em questão para obter mais informações sobre como os dados são tratados.


Os chats secretos são destinados a pessoas que querem mais sigilo do que a pessoa comum. Todas as mensagens em chats secretos usam criptografia de ponta a ponta. Isso significa que apenas você e o destinatário podem ler essas mensagens — ninguém mais pode decifrá-las, incluindo nós aqui no Telegram (mais sobre isso aqui). Além disso, as mensagens não podem ser encaminhadas de chats secretos. E quando você apagar as mensagens do seu lado da conversa, o aplicativo do outro lado do chat secreto será solicitado a apagá-las também.

Você pode configurar suas mensagens, fotos, vídeos e arquivos para autodestruição em um determinado período depois que elas foram lidos ou abertos pelo destinatário. A mensagem desaparecerá do seu dispositivo e do de seu amigo.

Todas os chats secretos no Telegram são específicos do dispositivo e não fazem parte da nuvem do Telegram. Isso significa que você só pode acessar mensagens em um chat secreto a partir do dispositivo de origem. Eles são seguros desde que o dispositivo esteja seguro em seu bolso.

*iOS*: abra o perfil do usuário e toque nos três pontinhos ‘…’, depois em ‘Iniciar Chat Secreto’.*Android*: deslize para a direita para abrir o menu e então em “Iniciar Chat Secreto”.

Lembre-se de que os chats secretos do Telegram são específicos do dispositivo. Se você iniciar um chat secreto com um amigo em um de seus dispositivos, este chat estará disponível somente no dispositivo em que foi iniciado. Se você sair do Telegram, perderá todos os seus chats secretos naquele dispositivo. Você pode criar vários chats secretos com o mesmo contato se desejar.

O Timer de Autodestruição está disponível para **todas as mensagens** em Chats Secretos e para **mídias** em chats privados na nuvem.

Para definir o timer, basta tocar no ícone de relógio (na caixa de texto no iOS, ou na barra superior no Android) e configurar o limite de tempo desejado. O relógio começa a contar no momento em que a mensagem é exibida na tela do destinatário (recebe dois ticks verdes). Assim que o tempo acabar, a mensagem desaparece de **ambos** os dispositivos. Tentaremos enviar uma notificação se uma captura de tela for realizada.

Por favor, note que o timer em Chats Secretos só se aplica a mensagens que foram enviadas **após** o temporizador ser definido – ele não tem efeito nas mensagens anteriores.

Infelizmente, não há uma maneira à prova de balas de detectar capturas de tela em determinados sistemas (mais notavelmente, alguns dispositivos Android e Windows Phone). Faremos todos os esforços para alertá-lo sobre capturas de tela feitas em seus chats secretos, mas ainda será possível contornar essas notificações e fazer capturas de tela silenciosamente. Aconselhamos compartilhar informações confidenciais apenas com pessoas em quem você confia. Afinal, ninguém pode impedir uma pessoa de tirar uma foto da tela com um dispositivo diferente ou uma câmera fotográfica tradicional.

Quando um chat secreto é criado, os dispositivos participantes trocam chaves de criptografia usando a chamada troca de chaves Diffie-Hellman. Depois que a conexão segura de ponta a ponta for estabelecida, geramos uma imagem que visualiza a chave de criptografia do seu chat. Você pode então comparar esta imagem com a que seu amigo tem — se as duas imagens são as mesmas, você pode ter certeza de que o chat secreto é seguro, e um ataque man-in-the-middle não poderá acontecer.

Versões mais recentes dos aplicativos do Telegram mostrarão uma imagem maior junto com uma representação textual da chave (essa não é a chave em si, é claro!) quando ambos os participantes estiverem usando um aplicativo atualizado.

Sempre compare as visualizações usando um canal que é conhecido por ser seguro — é mais seguro se você fizer isso pessoalmente, em uma reunião offline com seu parceiro de conversa.

Todas as mensagens do Telegram são sempre criptografadas com segurança. Mensagens em Chats Secretos usam criptografia **cliente-cliente**, enquanto os chats na nuvem usam criptografia **cliente-servidor/servidor-cliente** e são armazenadas criptografadamente na Nuvem do Telegram (mais aqui). Isso permite que suas mensagens na nuvem sejam tanto seguras quanto imediatamente acessíveis a partir de qualquer um de seus dispositivos — mesmo se você perder completamente o dispositivo.

O problema de restaurar o acesso ao seu histórico de chats em um dispositivo recém-conectado (por exemplo, quando você perde seu telefone) não tem uma solução elegante no paradigma de criptografia de ponta a ponta. Ao mesmo tempo, backups confiáveis são um recurso essencial para qualquer mensageiro de mercado de massa. Para resolver este problema, alguns aplicativos (como Whatsapp e Viber) permitem backups decriptáveis que colocam em risco a privacidade de seus usuários — mesmo que eles não habilitem os backups por conta própria. Outros aplicativos ignoram completamente a necessidade de backups e deixam seus usuários vulneráveis à perda de dados.

Optamos por uma terceira abordagem, oferecendo dois tipos distintos de chats. O Telegram desativa os backups padrão do sistema e fornece a todos os usuários uma solução integrada de backup com foco em segurança na forma de Chats na Nuvem. Enquanto isso, a entidade separada dos Chats Secretos oferece a você controle total sobre os dados que não deseja armazenar.

Isso permite que o Telegram seja amplamente adotado em círculos sociais grandes, não apenas por ativistas e dissidentes, de modo que o simples fato de usar o Telegram não marque os usuários como alvos de vigilância reforçada em certos países. Estamos convencidos de que a separação de conversas em chats na nuvem e secretos representa a solução mais segura atualmente possível para um aplicativo de mensagens altamente popular.

Veja também, em Inglês: Porquê o Telegram não tem criptografia de ponta a ponta por padrão.


No Telegram, você pode enviar mensagens em chats privados e em grupos sem tornar seu número de telefone visível. Por padrão, seu número é visível apenas para as pessoas que você adicionou como contatos na sua agenda telefônica. Você pode modificar isso ainda mais em *Configurações > Privacidade e Segurança > Número de Telefone*.

Observe que as pessoas sempre irão ver seu número se já souberem e tiverem **salvo** na agenda deles.


Cada número de telefone é uma conta **separada** no Telegram. Você tem várias opções se estiver usando vários números de telefone:

- Se você **não vai mais usar o número antigo** (por exemplo, você se mudou para um novo país ou alterou seu número para sempre), simplesmente vá para Configurações e altere o número conectado à sua conta do Telegram para o novo número.**Importante:** verifique se você tem acesso ao seu número de telefone conectado. Caso contrário, você corre o risco de perder o acesso à sua conta.
- Se você vai usar o novo número por **tempo limitado** (por exemplo, em uma viagem ou férias), não há necessidade de fazer nada.
- Se você quiser continuar usando **ambos os números** (por exemplo, você tem um telefone comercial e um telefone pessoal), escolha um como o número do seu Telegram. Você*pode* criar outra conta do Telegram no segundo número também, por exemplo, se quiser separar assuntos pessoais do trabalho. É possível entrar no app do Telegram com várias contas diferentes ao mesmo tempo.

A maioria dos usuários não precisa sair da conta do Telegram:

- Você pode usar o Telegram em vários dispositivos **ao mesmo tempo** . Basta usar o mesmo número de telefone para fazer login em todos os dispositivos.
- Você pode ir em *Configurações > Dados e Armazenamento > Uso de Armazenamento > Limpar Cache* para**liberar espaço** no seu dispositivo sem sair de sua conta do Telegram.
- Se você usa o Telegram com **vários números de telefone** , poderá alternar entre contas sem sair da conta.
- Se você usa o Telegram em um **dispositivo compartilhado** , poderá definir uma senha de bloqueio em*Configurações > Privacidade e Segurança* para garantir que somente você tenha acesso à sua conta.

Se você quiser sair por algum motivo, veja como você pode fazer isso:

*iOS*: Vá para *Configurações > Editar > Sair*.*Android* e *Telegram Desktop*: Vá para *Configurações > … (no canto superior direito) > Sair*.

Se você sair da conta, manterá todas as suas mensagens na nuvem. No entanto, **perderá** todos os seus **Chats Secretos** e **todas as mensagens** dentro desses chats secretos.

Observe que sair da conta **não** aciona a exclusão remota de suas mensagens de chats secretos no dispositivo de seu parceiro. Para fazer isso, escolha *“Limpar histórico”* no chat primeiro.


Você pode alterar seu número no Telegram e manter **tudo**, incluindo todos os seus contatos, mensagens e mídias na nuvem do Telegram, bem como todos os seus chats secretos em todos os dispositivos.

Para alterar seu número, vá para Configurações e toque no seu número de telefone (logo acima do nome de usuário) e, em seguida, em *“Alterar número”*. Se você já tiver uma conta do Telegram diferente no número de destino, precisará apagar essa conta primeiro.

Se você quiser apagar sua conta, faça isso na página de desativação. A exclusão da sua conta remove permanentemente todas as suas **mensagens** e **contatos**. Todos os grupos e canais que você criou ficarão órfãos sem um criador, mas os administradores mantêm os direitos deles.

Esta ação deve ser confirmada através da sua conta do Telegram e não pode ser desfeita.

Recomendamos usar um navegador desktop para esse processo.

Observe que você receberá o **código** via **Telegram**, e não por SMS.


Como foi mencionado acima, todos os seus dados serão apagados do nosso sistema: todas as mensagens, grupos e contatos associados à sua conta serão apagados. Dito isso, seus contatos ainda poderão conversar nos grupos que você criou e eles ainda terão a cópia *deles* das mensagens que você enviou. Portanto, se você quiser enviar mensagens que podem desaparecer sem deixar rastros, experimente usar nosso timer de autodestruição.

O término de uma conta do Telegram é irreversível. Se você se inscrever novamente, aparecerá como um novo usuário e não receberá seu histórico, contatos ou grupos de volta. As pessoas que tiverem seu número de telefone nos contatos delas serão notificadas. O novo usuário será exibido como uma conversa separada na lista de mensagens deles e o histórico de conversas com esse novo usuário estará vazio.

O Telegram não é uma organização comercial e valorizamos muito nosso espaço em disco. Se você parar de usar o Telegram e não fizer login por pelo menos 18 meses, sua conta será apagada juntamente com todas as mensagens, mídias, contatos e todos os outros dados armazenados na nuvem do Telegram. Você pode alterar o período exato após o qual sua conta inativa será autodestruída nas Configurações.

Você pode apagar a maioria dos seus dados sem apagar sua conta do Telegram.

Para apagar mensagens individuais ou conversas inteiras para ambas as partes a qualquer momento, basta tocar em uma mensagem (ou pressionar e segurar para selecionar várias conversas) e tocar no ícone de apagar, depois marcar a opção de apagar para ambas as partes.

Muitas configurações relevantes estão disponíveis em *Configurações > Privacidade e Segurança* (no iOS, há mais uma etapa > Configurações de Dados), por exemplo:

- Para apagar seus Contatos Sincronizados, escolha *Apagar Contatos Sincronizados* .
- Para apagar seus Rascunhos na Nuvem, escolha *Apagar Todos os Rascunhos na Nuvem* (no Android, esta opção está em Configurações > Dados e Armazenamento).
- Para apagar os metadados de sugestões sobre contatos e bots com os quais você se comunica com frequência, desative *Sugerir Contatos Frequentes* .

Para outros dados:

- Para apagar suas fotos de perfil, abra seu perfil > toque na sua foto de perfil > > Apagar.
- Para apagar as stories que você postou, vá para **Minhas Stories** , pressione e segure para selecionar e toque no ícone de apagar no canto superior direito.
- Para apagar seu histórico de chamadas, vá para Chamadas > / > Apagar Todas as Chamadas.

Primeiro de tudo, sentimos muito pelo seu celular. Infelizmente, o número de telefone é a única maneira de identificarmos um usuário do Telegram no momento. Não coletamos informações adicionais sobre você, portanto, quem tiver o número tem a conta. Isso significa que não podemos ajudá-lo, a menos que você tenha acesso ao número de telefone ou ao próprio aplicativo do Telegram conectado à sua conta em qualquer um dos seus dispositivos.

1. Vá para *Configurações do Telegram > Privacidade e Segurança* e ative a Verificação em Duas Etapas. Dessa forma, o número de telefone, por si só, não será suficiente para fazer login na sua conta.
2. Vá para *Configurações > Dispositivos (ou Privacidade e Segurança > Sessões Ativas)* e encerre sua sessão do Telegram no dispositivo antigo. Quem tiver seu telefone não poderá fazer login novamente, pois não sabe sua senha.
3. Entre em contato com o seu fornecedor de serviços telefônicos, para que eles bloqueiem o seu chip SIM antigo e emitam um novo com o seu número.
4. Se você decidir mudar para um novo número de telefone, não se esqueça de ir em Configurações, tocar no seu número de telefone e alterar o número do seu Telegram para o novo.

1. Em primeiro lugar, você precisa entrar em contato com o seu provedor de telefone para que eles bloqueiem o seu antigo chip SIM e emita um novo com o seu número.
2. Espere até receber o seu novo chip SIM com o número antigo, faça o login no Telegram, depois vá para *Configurações > Dispositivos (ou Privacidade e Segurança > Sessões Ativas)* e encerre sua sessão do Telegram no dispositivo antigo.

Ladrões comuns geralmente jogam fora o chip SIM imediatamente (o telefone é mais difícil de localizar assim), então formatam os dispositivos e vendem, assim não há muito risco para os dados em caso de pequenos furtos regulares. Mas se você tiver motivos para se preocupar com os dados no dispositivo e não conseguir sair por outro dispositivo, é melhor que você formate o dispositivo remotamente. Você pode ler mais sobre isso aqui: Apple iOS, Android. Infelizmente, isso requer que você tenha se preparado com antecedência para esse caso.

Você pode apagar sua conta do Telegram se você estiver logado em pelo menos um dos seus outros dispositivos (móvel ou desktop). Observe que as contas inativas do Telegram se autodestroem automaticamente após um período de tempo - 18 meses sendo a configuração padrão.

Os perfis do Telegram exibem um selo com uma classificação numérica baseada no volume total de transações bem-sucedidas que o usuário realizou com as Estrelas do Telegram.

Sua classificação de perfil destaca seu nível no Telegram e ajuda os donos de canais a verem que você é confiável para Sugerir Posts e outros tipos de solicitações.

Comprar presentes, enviar Mensagens Pagas e financiar Posts Sugeridos com Estrelas aumenta sua classificação. No entanto, se você solicitar reembolso de compras de Estrelas ou converter presentes em Estrelas, sua classificação diminuirá.

Se você já está com a sessão iniciada no Telegram em um dispositivo, você pode **criar uma chave de acesso** que permite que você entre na sua conta do Telegram da mesma forma que você **desbloqueia o seu dispositivo**. Com uma chave de acesso, você pode fazer login no seu dispositivo simplesmente inserindo um **código PIN** ou **dados biométricos**, como o seu Face ID ou a leitura da sua impressão digital.

As chaves de acesso são um **método de login adicional** que pode ser usado **em vez de SMS** para entrar instantaneamente na sua conta – mesmo se você estiver viajando ou não tiver serviço de SMS. As chaves de acesso também são **mais seguras** do que os códigos SMS, ajudando a **proteger os usuários** contra o acesso não autorizado à conta.

Suas chaves de acesso podem ser gerenciadas em *Configurações > Privacidade e Segurança > Chaves de Acesso* em qualquer app — que **mostra informações detalhadas** para cada uma das suas chaves de acesso, como a **data de criação** e quando foram **usadas pela última vez** para fazer login.


Se você tiver um gerenciador de senhas como as Chaves do iCloud, o Gerenciador de senhas do Google ou outro serviço de terceiros, poderá usá-lo para **fazer backup da sua chave de acesso** caso troque de dispositivo ou perca o acesso a ele.

Com uma chave de acesso, você ainda pode **solicitar um código SMS** para fazer login – portanto, certifique-se sempre de que sua conta usa um número de telefone atualizado que seja **controlado por você**. Para ainda mais segurança, você pode adicionar uma senha adicional à sua conta, que será exigida **toda vez** que você fizer login.


Se a sua conta foi restringida devido a denúncias de outros usuários, sua conta está **congelada**. Enquanto estiver congelada, você ainda pode ler suas conversas, mas não pode enviar mensagens nem publicar conteúdo.

Você pode recorrer da restrição diretamente pelo aplicativo. Os moderadores do Telegram vão analisar o seu caso. Se a restrição tiver sido um engano, sua conta será descongelada.

Se você é um desenvolvedor, pode gostar mais da nossa Bots FAQ.


Os bots são pequenos programas que são executados dentro do Telegram. Eles são feitos por desenvolvedores de terceiros usando a API de Bots do Telegram.

Bots modernos podem fazer muito mais do que responder mensagens. Eles podem abrir **miniapps** completos com sua própria interface, executar assistentes de IA com múltiplas conversas em tópicos e streaming de respostas – e muito mais.

Criar bots no Telegram é superfácil, mas você precisará de pelo menos algumas habilidades em programação de computadores. Se você está decidido e quer criar um bot, nossa **Introdução para desenvolvedores** é um bom lugar para começar.

Infelizmente, não há maneiras inovadoras de criar um bot funcional se você não for um desenvolvedor. Mas temos certeza de que você encontrará em breve muitos bots criados por outras pessoas para experimentar.

Se você não quiser que um bot envie mensagens para você, sinta-se à vontade para bloqueá-lo — da mesma forma que bloquearia um usuário humano. Alguns clientes do Telegram têm um botão *“Parar Bot”* no perfil do bot.

Dito isso, a maioria dos desenvolvedores de bots oferece comandos que silenciam o bot, verifique o comando */help* no bot em busca de pistas.

Sim. Bots não são diferentes dos usuários humanos que você encontra em grupos, por exemplo. Eles podem ver seu nome público, nome de usuário e fotos de perfil, e eles podem ver as mensagens que você envia para eles, é isso. Eles **não** veem seu número de telefone (a menos que você decida dar a eles você mesmo).

Naturalmente, qualquer bot deve ser tratado como um estranho — não lhes dê suas senhas, códigos de Telegram ou números de contas bancárias, mesmo que eles perguntem com educação. Além disso, tenha cuidado ao abrir arquivos enviados por bots, da mesma forma que você lidaria com seres humanos comuns. Exemplo: Se um bot nos enviasse um arquivo chamado *clique-aqui-e-me-abra.exe*, provavelmente não o abriríamos.

Os bots podem trabalhar em dois modos quando você os adiciona aos grupos. Por padrão, os bots só veem mensagens destinadas a eles. Nesse caso, você verá que o bot “não tem acesso às mensagens” na lista de membros do grupo perto do nome do bot.

Alguns bots precisam de mais informações para trabalhar, portanto, os desenvolvedores podem desativar o modo de privacidade. Nesse caso, o bot verá todas as mensagens enviadas para o grupo e você verá “tem acesso às mensagens” na lista de membros perto do bot.

Saiba mais sobre o modo de privacidade para bots (em Inglês) »

Se o seu grupo contém informações muito confidenciais, talvez seja melhor evitar adicionar bots nos quais você não confia 100%.

Não. Embora tenhamos alguns bots oficiais para propósitos específicos, (como @gif ou @Stickers), nós geralmente não criamos bots. Os bots são feitos por desenvolvedores de terceiros usando a API e plataforma de Bots do Telegram (Telegram Bot API and platform).

Miniapps são aplicativos completos que rodam dentro do Telegram, criados por desenvolvedores terceirizados sobre a plataforma de Bots. Eles podem ter a aparência e o funcionamento de aplicativos normais, com sua própria interface, pagamentos, assinaturas e muito mais.

Você pode encontrar miniapps na **Loja de Miniapps**, na aba *Apps* da Busca, abri-los em modo de tela cheia e até adicionar um atalho à tela inicial do seu celular.

Os miniapps podem vender itens digitais e assinaturas usando Estrelas do Telegram. Alguns miniapps oferecem **programas de afiliados** — quando você os compartilha com amigos, pode ganhar Estrelas.

Todos os apps de usuário do Telegram são completamente de código-aberto. Oferecemos builds verificáveis tanto para o iOS quanto para o Android – essa tecnologia permite verificar de forma independente que os aplicativos que você baixa das lojas de apps foram construídos usando **o mesmo exato código** que publicamos.

Diferentemente, publicar o código do servidor não dá garantias de segurança nem para Chats Secretos nem para Chats da Nuvem. Isso porque – ao contrário do código dos apps de usuário – não há uma forma de verificar que o **mesmo código** está sendo executado nos servidores.

Sobre Chats Secretos, você não precisa do código do servidor para verificar a integridade deles – a lógica da criptografia de ponta a ponta é que ela precisa ser sólida independentemente da forma como o servidor funciona.

Em um post no canal dele, o Pavel Durov explicou por quê o Telegram não publicou o código do servidor, mesmo se fosse uma jogada de publicidade.


A criptografia e a API usadas no servidor do Telegram são completamente documentadas e abertas para revisão por especialistas em segurança. Damos as boas-vindas para qualquer comentário em *security@telegram.org*.

Nossa arquitetura ainda não suporta federação. O Telegram é um serviço de nuvem unificado, portanto, criar *forks* em que dois usuários podem acabar em duas nuvens diferentes do Telegram é inaceitável. Permitir que você execute o seu próprio servidor do Telegram, mantendo a velocidade e a segurança, é uma tarefa superdifícil. No momento, estamos indecisos se o Telegram deveria ou não seguir nessa direção.

Sim. Desenvolvedores de todas as plataformas são bem-vindos para usar nosso protocolo, API e até código-fonte. Dê uma olhada na seção "Getting started" da documentação.

Não se esqueça da nossa Bot API que permite criar coisas legais em nossa plataforma.


Sim, dá uma olhada aqui.

A Apple criou rótulos de privacidade para informar os usuários sobre quais dados os apps podem coletar, mas as informações lá são vagas e podem ser enganosas. Você pode ver uma explicação detalhada dos rótulos sobre o Telegram aqui.

Um é o nosso aplicativo nativo para macOS, o outro é o Telegram Lite, a versão macOS do nosso cliente multiplataforma. Ambos os aplicativos são oficiais. Ambos começaram como aplicativos não-oficiais por dois desenvolvedores diferentes e variam em design e funcionalidade.

O Telegram para macOS tem compatibilidade com muitos recursos específicos da plataforma, como a Touch Bar do MacBook Pro, navegação por gestos, integração com o menu Compartilhar do Mac e muito mais. Ele tem todos os recursos da versão iOS do aplicativo, incluindo chats secretos.

O Telegram Lite é um aplicativo extremamente rápido, otimizado para tarefas relacionadas ao trabalho e para lidar com grandes comunidades. Ele oferece uma interface de três colunas, perfeita para multitarefas e acesso rápido às mídias, aos arquivos e links compartilhados em seus chats. Esse aplicativo também pode ser usado para exportar os seus dados e chats do Telegram.

O Telegram está oficialmente disponível em muitos idiomas na maioria das plataformas — e estamos sempre adicionando mais.

Se você não gostar de como um elemento específico da interface do Telegram é traduzido no seu idioma ou se quiser nos ajudar a manter a tradução, confira nossa plataforma de tradução. Todos podem sugerir traduções e votar nas melhores, tornando a localização do Telegram um esforço de todos.

Se você quiser ir além das sugestões de frases individuais e quiser nos ajudar a manter a tradução oficial para seu idioma continuamente, entre em contato com @TelegramAuditions. Inclua uma hashtag com o nome em Inglês do seu idioma (por exemplo, #Portuguese ou #Albanian) e alguns links para frases nessa plataforma com suas **sugestões de tradução** ou **comentários**. Certifique-se de ler o **Guia de Estilo** com cuidado antes de se inscrever.

Sim, estamos sempre procurando voluntários para nos ajudar com o suporte ao usuário. Se você estiver interessado em responder perguntas sobre o Telegram a usuários do Brasil, entre em contato com nossa conta de entrevistas.

Antes de se inscrever, confira a Telegram Support Initiative.

**Telegram Passport** é um método de autorização unificado para serviços que exigem identificação pessoal. Com o Telegram Passport, você pode enviar seus documentos uma vez e, em seguida, compartilhar instantaneamente seus dados com serviços que exijam identificação no mundo real (finanças, ICOs, etc).

Seus documentos de identidade e dados pessoais serão armazenados na nuvem do Telegram usando **Criptografia de Ponta a Ponta**. Para o Telegram, esses dados são apenas coisas aleatórias sem utilidade, e não temos acesso às informações que você armazena no seu Telegram Passport. Quando você compartilha dados, eles vão diretamente para o destinatário.

Você pode encontrar mais informações sobre o Telegram Passport em nosso blog.


Se você é um desenvolvedor ou proprietário de um serviço que requer uma identidade real, por favor, dê uma olhada **neste manual**. Você também pode experimentar solicitar dados do Telegram Passport usando esta página.

Por favor, verifique se você está digitando o número do seu celular no formato internacional.

Exemplo: `+(código do país)(cidade ou código da operadora)(seu número).`

Se você está tendo problemas de registro ou login, entre em contato usando este formulário.

Por motivos de segurança, códigos de login ditados via chamada telefônica só estão disponíveis para contas que têm a verificação em duas etapas ativada (Configurações > Privacidade e Segurança > Verificação em Duas Etapas).

Por favor, note também que contas no Telegram só podem ser conectadas a um número de celular. No momento, não temos compatibilidade com números fixos.

Se você usou recentemente um de nossos aplicativos em **outro dispositivo** (também pode ser um aplicativo diferente no mesmo dispositivo), o código de login pode ser enviado **via Telegram** em vez de SMS.

Para receber esse código, basta abrir o Telegram e verificar em qualquer um dos seus dispositivos conectados. Você vai encontrá-lo no chat com o nome de Telegram, um perfil verificado com um check azul:

**ATENÇÃO!** Por favor, note que receber os códigos de acesso via Telegram não deve ser considerado uma alternativa ao uso de um **número de telefone atualizado**. Em caso de troca de números, certifique-se sempre de que o Telegram está conectado a um número de telefone que **você controle**. Caso contrário, você corre o risco de perder o acesso à sua conta para sempre.

*Android:*

1. Vá para as *Configurações do Telegram > Notificações e Sons* , e certifique-se que as notificações estão**ATIVADAS** e a prioridade está configurada como**“Alta”** ou superior.
2. Verifique se o contato ou grupo está *silenciado* .
3. Certifique-se de que o Google Play Services está instalado em seu celular.
4. Verifique a **prioridade das notificações** para o Telegram nas**configurações do Android** . Essa configuração pode ser chamada de*Prioridade* ,*Importância* ,*Estilo de notificação* ou*Comportamento* , dependendo do seu dispositivo.
5. Se o seu telefone usar algum **software de economia de bateria** , verifique se o Telegram está na lista de permissões desse aplicativo.

NOTA: Os dispositivos da **Huawei** e **Xiaomi** possuem serviços gerenciadores de tarefa que interferem no serviço de notificação do Telegram. Para que nossas notificações funcionem, você precisa adicionar o Telegram aos aplicativos permitidos nas configurações de segurança desses dispositivos. Huawei: *App Gerenciador do Telefone > Apps protegidos > Adicione o Telegram à lista*. Xiaomi: *Serviços > Segurança > Permissões > Início Automático, encontre o Telegram e ative a inicialização automática*.


*iOS:*

1. Vá para as *Configurações do Telegram > Notificações e Sons* , e certifique-se que as notificações estão**ATIVADAS** .
2. Certifique-se que as notificações estão **ATIVADAS** nos Ajustes do sistema.
3. Verifique se o contato ou grupo está *silenciado* .
4. Encerre o Telegram (vá para a tela inicial, toque duas vezes no botão home, encerre o Telegram (arraste-o para cima), vá para os ajustes do sistema, defina o estilo de alerta do Telegram para NENHUM, reinicie o Telegram, vá para os ajustes do sistema e defina o estilo de alerta de volta para banners.

Se você sabe que seus amigos têm o Telegram, mas você não pode vê-los — ou eles aparecem com números em vez de nomes.

1. Verifique se você está usando a versão mais recente do aplicativo.
2. Reinicie o aplicativo (encerrando-o da lista de multitarefas e iniciando novamente).
3. Altere temporariamente o nome do contato nos contatos do telefone (adicione alguns símbolos e altere novamente).
4. Se não ajudar, tente fazer o login novamente. Lembre-se de que sair da conta elimina todos os seus chats secretos.

1. Encerre o aplicativo forçadamente (toque duas vezes no botão home e deslize o dedo para cima no Telegram), depois inicie o aplicativo e verifique se ajudou.
2. Se isso não ajudar, altere temporariamente o nome do contato nos contatos do telefone (adicione alguns símbolos e altere novamente).
3. Se isso não funcionar, faça um novo login: *Configurações > Editar > Sair* . Lembre-se de que sair da conta elimina todos os seus chats secretos. Em seguida, faça o login novamente.

Para apagar um contato, abra o chat com a pessoa e toque na foto de perfil, no canto superior direito, e então no menu “…” no canto superior direito e selecione a opção “Apagar”.

Se você deseja apagar os contatos completamente, tenha certeza de que você o apagou da sua agenda de contatos. O Telegram continua sincronizando e adicionará o contato de volta se você não o apagou de lá.

Chats Secretos são estabelecidos entre os dois dispositivos em que foram criados. Isso significa que todas essas mensagens não estão disponíveis na nuvem e não podem ser acessadas em outros dispositivos.

Além disso, os Chats Secretos também estão vinculados à sua sessão de login atual no dispositivo. Se você sair do Telegram e entrar novamente, perderá todos os seus chats secretos.

Quando os usuários relatam mensagens indesejadas de uma conta do Telegram, aplicamos um limite: as contas denunciadas só podem enviar mensagens para pessoas que têm o número delas salvo como um contato.

Isso significa que, se você contatar aleatoriamente pessoas que não conhece e enviar mensagens irritantes, poderá perder a capacidade de fazer isso no futuro.

Se você acredita que esse limite foi aplicado à sua conta incorretamente, visite esta página.

Alguns usuários cobram uma pequena taxa — paga em Estrelas do Telegram — por mensagens de pessoas que não estão em seus contatos. Isso é chamado de Mensagem por Estrelas, e ajuda as pessoas a reduzir o spam na caixa de entrada delas.

Você verá quantas Estrelas são necessárias antes de enviar a mensagem. Se o destinatário responder, ele pode optar por reembolsar a taxa.

Se você não quiser pagar, pode esperar que a outra pessoa te envie uma mensagem primeiro, ou pedir para que ela te adicione aos contatos.

Se o horário no Telegram está diferente do de seu celular após uma mudança de fuso horário, você pode fazer a sincronização do relógio da seguinte maneira:

1. Desative a obtenção automática de hora e do fuso horário nas configurações do sistema.
2. Mude para o seu fuso horário. *Por exemplo: GMT-2 (Horário de Verão de Brasília) ou GMT-3 (Horário de Brasília ou São Paulo)* .
3. Ative a obtenção automática de hora e do fuso horário nas configurações do sistema, e reinicie seu dispositivo se necessário.

Nota: Em alguns casos pode ser necessário ajustar o horário manualmente. E dependendo de onde você está, o fuso horário poderá ser diferente. Veja esta lista para os fuso horários brasileiros.


O Telegram pode usar o **microfone** em segundo plano se você minimizar o app enquanto estiver fazendo uma chamada, gravando um vídeo ou gravando mensagens de voz/vídeo.

Os monitores de permissão da Samsung e da Xiaomi podem, de forma confusa, sinalizar e notificar que o Telegram solicitou acesso à **câmera** em segundo plano. Isso acontece quando o aplicativo solicita informações sobre a câmera – ele não está usando a câmera. Infelizmente, para os monitores de permissão da Samsung e da Xiaomi, pode parecer a mesma coisa.

As informações da câmera são solicitadas pelo aplicativo quando você toca no botão de anexo ou começa a gravar um vídeo ou uma mensagem de vídeo. Se você fizer isso e fechar rapidamente o aplicativo, a solicitação já iniciada poderá tentar ser executada de forma assíncrona quando o aplicativo já estiver em segundo plano ou ser enviada quando o sistema ativar o aplicativo para mostrar uma notificação sobre uma nova mensagem. De qualquer forma, essas solicitações são apenas para informações da câmera, o aplicativo nunca usa a câmera de fato em segundo plano.

Qualquer pessoa pode verificar o código-fonte aberto do Telegram e confirmar que o aplicativo não está fazendo nada escondido. Também oferecemos builds reproduzíveis que podem te ajudar a provar que a versão que você baixou da App Store ou da Google Play foi criada a partir do mesmo código-fonte que publicamos.

Se você tiver outras dúvidas, entre em contato com o Suporte do Telegram (no Telegram, vá para *Configurações > Faça uma pergunta*). Note que o suporte é feito por voluntários.

Temos o @TelegramBR no Telegram, o canal oficial de informações em Português. Lá você receberá informações sobre novas versões e também dicas. Inscreva-se!

Se você não consegue fazer login na sua conta, use este formulário.

Para **solicitações de imprensa**, por favor contate @PressBot no Telegram.


Sim. Segue a gente! **@telegram_br**

Para quem fala Inglês: @telegram

Nossa conta no Twitter em Espanhol: @telegram_es

Em Italiano: @telegram_it

Em Coreano: @Telegram_kr

Em Alemão: @de_telegram

Quem fala Árabe pode achar a @telegram_arabic mais interessante.

Temos uma conta especial que pode ajudar você com problemas de login, o **@smstelegram** no Twitter. Esta conta é oficial. Não tenha medo de enviar lá por DM (Mensagem Privada) o número que você usa para o Telegram. Precisamos dessa informação para investigar os problemas.

Tenha cuidado, não temos outras contas de suporte em nenhuma plataforma de mídia social.

Se alguém no Facebook está dizendo que eles são nós, saiba que eles **não** são.

Para assuntos relacionados ao representante legal nos termos do ECA Digital, por favor contate br4.telegram@br4business.com.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
