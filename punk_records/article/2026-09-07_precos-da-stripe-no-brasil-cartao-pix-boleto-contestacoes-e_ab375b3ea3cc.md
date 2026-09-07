---
item_id: "f5784ba1-69bf-4f97-91e5-fe13ded231cb"
platform: article
external_id: "ab375b3ea3cc"
canonical_url: "https://stripe.com/br/pricing"
channel: "Stripe"
captured_at: 2026-09-07
status: enriched
triage: null
tags: ["stripe", "taxas-de-transacao", "chargeback", "stripe-billing", "stripe-connect", "pix", "boleto", "pagamento-internacional"]
applicability:
  saas_pessoal: alta
  projeto_cliente: baixa
  estudo_geral: alta
confidence: media
theme: negocios-e-financas
content_type: article
---

# Preços da Stripe no Brasil: cartão, Pix, boleto, contestações e produtos adicionais

🔗 https://stripe.com/br/pricing

## Resumo

Página oficial de preços da Stripe para o Brasil, com modelo de pagamento conforme o uso, sem tarifa mensal, sem taxa de configuração e sem tarifas ocultas. O preço base de Payments é 3,99% + R$ 0,39 por transação realizada com cartões nacionais; transações com cartões internacionais custam 2% adicionais sobre o valor já convertido para a moeda local. Entre as formas de pagamento locais, o boleto bancário custa R$ 3,45 por boleto pago e o Pix 1,19% por Pix pago (disponibilidade sob convite). Contestações (chargebacks) custam R$ 55,00 por contestação recebida e R$ 55,00 por contestação respondida manualmente, valor devolvido quando a disputa é vencida; o Smart Disputes, que monta a defesa com IA, cobra 30% do valor contestado apenas nas contestações ganhas. Ferramentas de prevenção via Verifi (Visa) e Ethoca (Mastercard) estão incluídas no Payments, assim como 3D Secure, Authorization Boost e o Radar Lite de prevenção a fraude; o Radar avulso é cobrado por transação rastreada. Nos produtos de receita, o Billing custa 0,7% do volume faturado, o Invoicing 0,4% por fatura paga (com teto por fatura), o Revenue Recognition um percentual do volume e o Connect cobra 0,25% de tarifa de entrada para plataformas que aplicam preços próprios sobre os pagamentos. Em dados e automação: Sigma a partir de R$ 50 por mês de infraestrutura mais cerca de R$ 0,10 por cobrança, Data Pipeline por transação, e Workflows com 10.000 etapas mensais mais valor por etapa adicional. Para grandes volumes ou modelos atípicos, a Stripe oferece pacote sob medida com precificação IC+, descontos por volume e por combinação de produtos e tarifas específicas por país.

## Tópicos

- **Cartão nacional e internacional** — 3,99% + R$ 0,39 por transação realizada com cartões nacionais; cartões internacionais têm 2% adicionais sobre o valor da transação após conversão para a moeda local.
- **Formas de pagamento locais** — Boleto bancário a R$ 3,45 por boleto pago e Pix a 1,19% por Pix pago, este último com acesso por convite.
- **Contestações e disputas** — R$ 55,00 por contestação recebida e R$ 55,00 por contestação respondida manualmente (devolvidos se vencer); Smart Disputes cobra 30% do valor contestado só nas disputas ganhas.
- **Prevenção a fraude incluída** — 3D Secure, Authorization Boost, Radar Lite e as ferramentas de prevenção da Verifi (Visa) e Ethoca (Mastercard) estão incluídas no plano Payments; o Radar avulso é cobrado por transação rastreada.
- **Produtos de receita recorrente** — Billing a 0,7% do volume faturado, Invoicing a 0,4% por fatura paga com teto por fatura, Revenue Recognition sobre percentual do volume e Payment Links cobrados como Payments.
- **Plataformas e marketplaces (Connect)** — 0,25% de tarifa de entrada para plataformas que aplicam seus próprios preços sobre os pagamentos e monetizam cada transação; a Stripe define e cobra as tarifas dos usuários finais.
- **Dados, automação e pacotes personalizados** — Sigma a partir de R$ 50/mês mais ~R$ 0,10 por cobrança, Data Pipeline por transação, Workflows com 10.000 etapas/mês; grandes volumes negociam IC+, descontos por volume e tarifas por país.

## Ferramentas citadas

- **Stripe Payments**: Processamento de cartão e formas locais, base do preço de 3,99% + R$ 0,39
- **Stripe Billing**: Gestão de assinaturas e cobrança recorrente, a 0,7% do volume
- **Stripe Invoicing**: Faturamento avulso, a 0,4% por fatura paga com teto
- **Stripe Connect**: Pagamentos integrados para plataformas e marketplaces, com 0,25% de tarifa de entrada
- **Stripe Radar**: Prevenção a fraude com IA; Radar Lite incluso no Payments, versão avulsa por transação rastreada
- **Smart Disputes**: Defesa de contestação montada por IA, cobrando 30% do valor contestado só quando a disputa é ganha
- **Stripe Sigma**: Ambiente SQL sobre os dados da Stripe, a partir de R$ 50/mês mais tarifa por cobrança
- **Stripe Atlas**: Abertura de empresa nos EUA com EIN, emissão de ações e opção fiscal 83(b), por tarifa única

## Pontos-chave

- Cartão nacional na Stripe Brasil custa 3,99% + R$ 0,39 — bem acima das ~2,99% + R$ 0,49 de players nacionais como o Asaas; o preço se paga em quem vende para fora, não em quem vende só no Brasil.
- Cartão internacional acrescenta 2% sobre o valor já convertido, então uma venda internacional sai perto de 6% + fixo.
- Pix custa 1,19% (percentual, não valor fixo) e é liberado por convite — o oposto do modelo nacional de R$ 1,99 fixos, o que inverte a conta conforme o ticket.
- Boleto sai por R$ 3,45 por boleto pago, quase o dobro do boleto de plataformas nacionais.
- Chargeback custa R$ 55 ao receber e mais R$ 55 se você responder manualmente; o valor da resposta volta se você ganhar, o da contestação recebida não.
- Smart Disputes só cobra quando você ganha (30% do valor contestado) — alinhado ao seu resultado, mas caro em disputa de valor alto.
- Radar Lite, 3D Secure e Authorization Boost já vêm no Payments: não há antifraude contratado à parte no plano padrão.
- Assinaturas custam 0,7% do volume no Billing EM CIMA da taxa de processamento — cobrança recorrente na Stripe é preço de processamento + preço de Billing.
- Marketplace via Connect tem 0,25% de tarifa de entrada quando a plataforma define os próprios preços e monetiza as transações.
- Sem mensalidade, sem setup e sem mínimo mensal no preço padrão; volume grande ou modelo atípico negocia IC+, descontos por volume e tarifas por país.

## Como aplicar

Serve de comparação direta para decidir onde cobrar o SaaS: em venda só no Brasil, Stripe (3,99% + R$ 0,39, mais 0,7% de Billing na assinatura) sai claramente mais caro que Asaas ou Mercado Pago; a Stripe só compensa se houver cliente pagando de fora, cobrança em múltiplas moedas ou necessidade do ferramental de assinatura pronto. Para o site de cliente brasileiro, não há motivo de custo para usá-la.

## 🍩 York diz

Fernando, faz a conta comigo: 3,99% + R$ 0,39 no cartão, mais 0,7% de Billing se for assinatura — quase 5% do seu faturamento indo embora antes de qualquer rosquinha. Contra ~3% no Asaas, isso é caro para vender no Brasil. A Stripe só vale o preço quando o cliente paga em dólar ou você precisa do maquinário de assinatura pronto; para venda nacional, é conveniência cobrada em porcentagem. Nota: os valores vieram da página renderizada, porque o extrator engoliu os números — confira na página antes de assinar qualquer coisa.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Acesse uma plataforma de pagamentos completa com preços simples e pagamento conforme o uso. Sem tarifas mensais, ocultas ou de configuração.

        
        
          
        
      por transação realizada para cartões nacionais

Crie um pacote individualizado. Disponível para empresas com um grande volume de pagamentos ou modelos de negócios únicos.

        
        
          
        
      Precificação IC+

      
    
      
        Descontos por volume

      
    
      
        Descontos ao adquirir vários produtos

      
    
      
        Tarifas específicas por país

        Pagamentos online e presenciais, cobrança recorrente, pagamentos integrados e muito mais.

Otimize a taxa de conversão, aceite formas de pagamento locais e aumente as taxas de aceitação.

Uma plataforma de pagamentos online projetada para o crescimento.

- 
  
    
  
  
    Aumente a aquisição de clientes com mais de 100 formas de pagamento.
- 
  
    
  
  
    Melhore a conversão com o Link, o checkout acelerado da Stripe.
- 
  
    
  
  
    Obtenha proteção contra fraudes com tecnologia de IA para pagamentos com cartão usando o Radar Lite.
- 
  
    
  
  
    Economize tempo de engenharia com UIs pré-integradas. 

Aceite cartões de crédito e débito, cartões pré-pagos e carteiras digitais amplamente utilizados para pagamentos online.

  
    
      
      
  +
  
  
  
  
    2%
  
  
  
  
para transações com cartões internacionais, a Stripe cobra do usuário uma tarifa correspondente ao percentual aplicado acima sobre o valor da transação (após conversão para a moeda local).


  
  
  
Ofereça débitos bancários, transferências bancárias e outras formas de pagamento com relevância local.

Boleto bancário

por boleto pago

Veja outras formas de pagamento
Permita que seus clientes paguem diretamente pela conta bancária ou carteira eletrônica usando PIX.

por PIX pago

Saiba mais
Responda a contestações de pagamentos com cartão, também conhecidas como estornos.

por cada contestação que você recebe.

Em casos raros, tarifas da bandeira de cartão também se aplicam.

por cada contestação que você responde manualmente.

Você recebe essa tarifa de volta em contestações ganhas. Você não recebe essa tarifa de volta em contestações perdidas.

Saiba mais
Responda a contestações com os comprovantes que a IA da Stripe prepara para você. Você também pode adicionar seus próprios comprovantes.

do valor contestado por cada contestação ganha.

Não há tarifa do Smart Disputes para contestações perdidas. A tarifa de contestação recebida ainda é válida.

Saiba mais
Ajude a reduzir as taxas de contestação com ferramentas de prevenção de contestações viabilizadas pela Verifi da Visa e Ethoca da Mastercard.

        Incluído no Payments 

    
    
  Links no-code para vender online sem um site.

- 
  
    
  
  
    Aceite pagamentos em minutos gerando links no-code. 
- 
  
    
  
  
    Venda produtos, ofereça assinaturas e muito mais.
- 
  
    
  
  
    Crie em grande escala usando nossa API para automatizar campanhas de marketing e operações de vendas.

Aceite pagamentos realizados com um link de pagamento.

com Payments

Use seu próprio domínio e hospede sua página de pagamentos ou portal de clientes na Stripe.

por mês

Saiba mais
Gere automaticamente uma fatura após uma compra avulsa.

sobre o total da transação

teto por fatura

Saiba mais
Formulário de pagamento pré-configurado e otimizado para conversão.

- 
  
    
  
  
    Economize tempo de engenharia e comece a usar rapidamente.
- 
  
    
  
  
    Reduza inconvenientes com recursos desenvolvidos para melhorar a conversão. 
- 
  
    
  
  
    Personalize com seu branding.

Aceite pagamentos realizados no Stripe Checkout.

Aprimore sua plataforma integrando serviços financeiros: configure contas financeiras, emita cartões e ofereça financiamentos.

Pagamentos integrados para plataformas e marketplaces.

- 
  
    
  
  
    Acelere os lançamentos usando soluções hospedadas na Stripe ou componentes pré-integrados.
- 
  
    
  
  
    Economize tempo usando ferramentas da Stripe para onboarding, risco, informes fiscais e muito mais.
- 
  
    
  
  
    Aumente a receita com a monetização de pagamentos.

A Stripe define e cobra tarifas dos seus usuários para que você não precise fazer isso. Saiba mais sobre como se qualificar para uma participação em receita da Stripe.

  
    
      
      
  
  
  
  
  
    0,25%
  
  
  
  
de tarifa de entrada para plataformas que aplicam seus próprios preços sobre pagamentos para gerar receita em cada transação


  
  
  
    Veja detalhes dos preços 
  
Otimize processos essenciais de negócios com ferramentas modulares de cobrança, impostos, relatórios de receita e análises de dados que operam de forma integrada.

Software de gestão de assinaturas para modelos de receita recorrente² e faturamento avulso.

- 
  
    
  
  
    Agilize a resposta às demandas dos usuários com modelos de preços flexíveis.
- 
  
    
  
  
    Aumente a receita e reduza a perda de clientes com o Smart Retries e as automações de fluxo de trabalho de recuperação.
- 
  
    
  
  
    Economize tempo de engenharia com ferramentas no-code ou APIs modulares.

Comece a fazer cobrança por assinaturas recorrentes e conforme o uso.

do volume no Billing

Veja detalhes dos preços
Medição, precificação e análises em tempo real para cobrança por uso.

- 
  
    
  
  
    Lance rapidamente com qualquer modelo de precificação baseado em uso ou híbrido.
- 
  
    
  
  
    Ajuste a precificação sem sobrecarga de engenharia.
- 
  
    
  
  
    Obtenha visibilidade em tempo real do uso e da receita.

        Escolha um plano
      

    
    Para equipes que estão lançando produtos com faturamento por uso. Pague conforme sua empresa cresce.

por 1.000 eventos de ingestão

do volume de faturamento

Saiba mais
Para empresas que estão expandindo a receita ou transformando a precificação. Preços personalizados para suas necessidades.

Exportação de dados disponível apenas em planos personalizados:

  
    
      
      
  
  
  
  
    US$ 0,03
  
  
  
  
  

          
          
        
          
          por 1.000 exportações de dados padrão

  
    
      
      
  
  
  
  
    US$ 0,05
  
  
  
  
  

  
  
  
    Entrar em contato com a Metronome 
  
por 1.000 exportações de dados premium

Software de faturamento global.

- 
  
    
  
  
    Crie, personalize e envie uma fatura em minutos, sem necessidade de código.
- 
  
    
  
  
    Economize tempo com fluxos automatizados de contas a receber e faturamento. 
- 
  
    
  
  
    Configure faturas para qualquer caso de uso.

Recursos de faturamento para você começar a usar em pouco tempo.

por fatura paga

Veja detalhes dos preços
Um ambiente SQL interativo para analisar seus dados da Stripe e criar relatórios personalizados.

- 
  
    
  
  
    Obtenha insights mais rápidos e abrangentes usando SQL ou prompts de linguagem natural com IA. 
- 
  
    
  
  
    Tome decisões confiantes e baseadas em dados com relatórios totalmente personalizáveis.
- 
  
    
  
  
    Mantenha as equipes em sincronia e economize tempo com relatórios programados.

Comece a explorar os dados da sua empresa.

por mês, tarifa de infraestrutura

  
    
      + uma tarifa por cobrança, a partir de 
      
  +
  
  
  
    R$ 0,10
  
  
  
  
  
  

  
  
  
    Veja detalhes dos preços 
  
Envie dados e relatórios da Stripe diretamente para seu armazém de dados ou armazenamento em nuvem.

- 
  
    
  
  
    Configure seu pipeline em minutos e automatize a entrega de dados - não é necessário nenhum código.
- 
  
    
  
  
    Acelere seu fechamento financeiro e obtenha insights empresariais mais completos.
- 
  
    
  
  
    Descarregue a manutenção contínua com um pipeline incorporado a Stripe.

Centralize seus dados da Stripe com outros dados da empresa.

por transação

Veja detalhes dos preços
Relatórios de receita automatizados para otimizar o regime de competência.

- 
  
    
  
  
    Feche os livros contábeis de forma rápida e precisa com relatórios contábeis automatizados e Dashboards. 
- 
  
    
  
  
    Revise as finanças com facilidade e audite em tempo real.
- 
  
    
  
  
    Mantenha a conformidade com ASC 606 e IFRS 15.

Simplifique o regime de competência.

do volume

Veja detalhes dos preços
Proteção contra fraudes e abusos baseada em IA.

- 
  
    
  
  
    Reduza a fraude em todas as formas de pagamento com a IA viabilizada pela rede da Stripe.
- 
  
    
  
  
    Sinalize e evite que contas suspeitas entrem na sua plataforma.
- 
  
    
  
  
    Fique à frente das fraudes emergentes e interrompa abusos em todo o ciclo de vida do cliente.
- 
  
    
  
  
    Comece já sem precisar de integração ou acesse a inteligência do Radar via API.

Pague pelo que usar. Sem taxas recorrentes. Ideal para volumes baixos ou imprevisíveis.

por transação rastreada

Software para abrir rapidamente sua startup.

- 
  
    
  
  
    Registre a documentação de abertura em minutos.
- 
  
    
  
  
    Utilize documentos confiáveis de escritórios de advocacia, advogados tributários e investidores de venture capital.
- 
  
    
  
  
    Receba mais de US$ 50 mil em descontos e benefícios. 

Abra sua empresa, obtenha seu EIN, emita ações e declare sua opção fiscal 83(b).

tarifa única de configuração (inclui tarifas governamentais e do primeiro ano do agente registrado)

Veja detalhes dos preços
Automatize tarefas e crie fluxos personalizados, sem escrever código.

- 
  
    
  
  
    Automatize processos de negócios com mais de 600 gatilhos de eventos.
- 
  
    
  
  
    Elimine código boilerplate com um criador de fluxos visual.
- 
  
    
  
  
    Amplie as funcionalidades da Stripe conectando aplicativos de terceiros.
- 
  
    
  
  
    Monitore e depure com logs e versionamento integrados.

Sem compromisso, sem taxas recorrentes. Comece a desenvolver fluxos de trabalho hoje mesmo.

10.000 etapas por mês

por etapa adicional

Saiba mais
- Pagamentos globais
- Gestão dos valores
- Automação de receitas e finanças
- Mais

Crie soluções personalizadas para facilitar a expansão para novos mercados, otimizar o desempenho dos pagamentos, automatizar os fluxos de trabalho de receita e finanças, monetizar os serviços financeiros e muito mais.

Projete uma solução para suas necessidades em conjunto com a nossa equipe de vendas:

- Payments
- Radar
- Connect
- Invoicing
- Billing
- e muito mais

Preços IC+, taxas fixas com desconto, assinaturas e taxas de juros especiais para plataformas.

Descontos com base em níveis de volume, comprometimentos e utilização de produtos.

Preços agregados opcionais para todos os mercados, facilitando a sua expansão global.

Dashboards, ferramentas e APIs que oferecem uma visão transparente dos seus custos.

O estudo Total Economic Impact da Forrester sugere um retorno sobre o investimento de mais de 3 vezes nas empresas que implantaram a Stripe.

    
    
    
    Leia a história 
    
      # Saiba por que a BMW escolheu a Stripe para gerenciar o e-commerce e os pagamentos

    
  

    
  
    
    
    
    Leia a história 
    
      # Veja como a Amazon simplificou os pagamentos internacionais com a Stripe

    
  

    
  
    
    
    
    Leia a história 
    
      # Veja como a Maersk aplicou novas tecnologias para facilitar a logística global

    
  

    
  
    
    
    
    Leia a história 
    
      # Veja como a Twilio aumentou em 10% as taxas de autorização com a Stripe

    
  

          Acesse uma plataforma completa de pagamentos com modelo de preços simples baseado em uso ou fale conosco para criarmos um pacote personalizado, específico para sua empresa.

Descubra como milhões de empresas, de startups a grandes corporações, usam a Stripe para iniciar e expandir seus negócios.

Comece a criar sua integração e aceite seu primeiro pagamento em minutos. As bibliotecas da Stripe estão disponíveis em todas as linguagens, de Rubi a Go.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
