---
item_id: "08e7e411-a886-444a-9d9d-77d7cf21e197"
platform: youtube
external_id: "6lKMViPJh6A"
canonical_url: "https://www.youtube.com/watch?v=6lKMViPJh6A"
channel: "DevPleno"
captured_at: 2026-09-08
status: applied_saas
triage: apply_saas
tags: ["asaas", "meio-de-pagamento-saas", "nota-fiscal-automatica", "cobranca-recorrente", "cobranca-por-uso", "webhook", "multitenant", "integracao-minima"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: alta
confidence: alta
theme: negocios-e-financas
content_type: transcript
---

# Asaas como meio de pagamento para SaaS: os 4 estágios de integração, nota fiscal automática e custo real por cobrança

🔗 https://www.youtube.com/watch?v=6lKMViPJh6A

## Resumo

Túlio (DevPleno) mostra como usa o Asaas como meio de pagamento em três dos seus SaaS que vendem para o Brasil, sem ser afiliado da plataforma. A tese central é que a integração deve acompanhar o estágio do negócio, não antecipá-lo. No estágio 1 (1 a 5 clientes) ele não integra nada e recebe como der — até Pix de pessoa física serve —, porque o objetivo ali é descobrir se alguém paga pela solução, e programar checkout antes disso é trabalho jogado fora se o projeto morrer. No estágio 2 (5 a 10 clientes) ele cria a assinatura manualmente no painel do Asaas e faz a integração mínima: guarda o ID do cliente Asaas no tenant e usa um único GET em /payments?customer= para listar as cobranças dentro de uma tela de Billing no próprio SaaS, além de mostrar um alerta quando há mensalidade em aberto — sem webhook, sem bloqueio automático, porque ele prefere conversar com o inadimplente antes de cortar. No estágio 3, quando o modelo virou cobrança por uso (mínimo + consumo), a assinatura deixou de servir e ele passou a disparar cobrança avulsa via POST, com um cron no Upstash rodando todo dia 5 e calculando o valor na própria plataforma; o cadastro do cliente no Asaas continua manual, feito no onboarding. A segunda integração ouve o webhook de pagamento confirmado e emite a nota fiscal de serviço por API (criar + agendar emissão), e o link invoice_url devolvido pelo Asaas é o que ele manda ao cliente para ver boleto, QR Code do Pix, status e a nota. O argumento decisivo pelo Asaas é a nota fiscal embutida: no Stripe seria preciso contratar eNotas ou Tecnospeed à parte, com taxa de adesão e pacote antecipado, enquanto no Asaas a nota sai por cerca de R$ 1 avulsa e o custo total fica em torno de R$ 3 a R$ 4 por cobrança. Ele fecha lembrando que Asaas só serve para cobrança no Brasil — para fora, Stripe — e que a arquitetura pode ser híbrida, roteando pelo país do tenant (BR → Asaas, US → Stripe, null → padrão).

## Tópicos

- **Estágio 1: 1 a 5 clientes** — Nenhuma integração e nenhum gateway: receba como der, até Pix de pessoa física. O objetivo é validar que alguém paga, e o modelo e o preço ainda vão mudar.
- **Estágio 2: 5 a 10 clientes** — Assinatura criada manualmente no painel do Asaas e integração mínima: guardar o ID do cliente Asaas no tenant e usar um GET em /payments?customer= para exibir uma tela de Billing e alertar sobre cobrança em aberto.
- **Estágio 3: cobrança por uso** — Quando o modelo virou mínimo + consumo, a assinatura deixou de servir; um cron no Upstash roda todo dia 5, calcula o uso na própria plataforma e dispara cobrança avulsa por POST na API do Asaas.
- **Webhook e nota fiscal automática** — Ouvir só o evento de pagamento confirmado e, ao recebê-lo, criar e agendar a emissão da nota fiscal por API; em assinaturas manuais dá para ligar a NF automática e dispensar o webhook.
- **Custo real e comparação** — Cerca de R$ 3 a R$ 4 por cobrança somando transação e nota (~R$ 1 por NF); no Stripe seria preciso contratar eNotas ou Tecnospeed, que cobram adesão e pacote antecipado (ex.: 60 notas/mês a R$ 1.227 por ano).
- **Baixa automática das cobranças** — A vantagem sobre receber Pix direto na conta é a conciliação: o Asaas identifica que aquele cliente pagou aquele mês e dá baixa sozinho, o que Pix na conta pessoal não faz.
- **Brasil x exterior e arquitetura híbrida** — Asaas só atende cobrança no Brasil; para fora, Stripe ou outro. Ele guarda a sigla do país no tenant e roteia: BR usa Asaas, US usa Stripe, null cai na plataforma padrão.

## Ferramentas citadas

- **Asaas**: Conta digital e meio de pagamento usado nos SaaS do autor para Pix, boleto, cartão, assinatura e nota fiscal
- **Stripe**: Alternativa citada para clientes fora do Brasil; não emite nota fiscal brasileira
- **eNotas / Tecnospeed**: Plataformas de emissão de nota fiscal que seriam necessárias à parte se não houvesse NF no gateway
- **Upstash (QStash)**: Serviço usado para rodar o cron que dispara as cobranças todo dia 5
- **Axios**: Cliente HTTP usado na integração; a API do Asaas é simples o bastante para dispensar SDK
- **Conta Azul**: Ferramenta usada na versão 1 de um dos SaaS, sendo migrada para o Asaas

## Pontos-chave

- Não integre gateway com 1 a 5 clientes: receba por Pix pessoal e gaste o tempo descobrindo se alguém paga — preço e modelo de cobrança ainda vão mudar, e integração feita cedo vira retrabalho.
- A integração de estágio 2 são DUAS coisas: guardar o ID do cliente Asaas no tenant e fazer um GET em /payments?customer= — isso já entrega tela de Billing, status de pagamento e alerta de inadimplência, sem webhook.
- Assinatura e cobrança parcelada são coisas diferentes: parcelada gera todas as parcelas na criação e cobra o valor cheio no cartão de uma vez; assinatura é template que gera uma cobrança nova a cada ciclo.
- Modelo de cobrança por uso não cabe em assinatura: exige calcular o valor na sua plataforma e disparar cobrança avulsa por POST, aqui com um cron mensal no Upstash.
- Só um webhook importa no começo: pagamento confirmado. Ao recebê-lo, criar e agendar a nota fiscal por API — duas requisições.
- O invoice_url devolvido pela API é o link único que mostra ao cliente boleto, QR Code do Pix, status e nota fiscal: elimina construir essa tela.
- A nota fiscal embutida é o motivo real de escolher Asaas sobre Stripe para B2B no Brasil: no Stripe a NF é ferramenta contratada à parte, com adesão e pacote pago antecipadamente.
- Custo declarado na prática: algo entre R$ 3 e R$ 4 por cobrança somando taxa de transação e nota fiscal (~R$ 1 por NF, paga por uso, sem antecipar pacote).
- Não bloqueie o inadimplente por padrão: em assinatura de software que não queima recurso caro, converse antes — o autor só mostra alerta no painel e liga para o cliente.
- Coletar CNPJ, endereço completo, CEP e e-mail no cadastro para poder emitir NF piora o onboarding: por isso ele cadastra o cliente no Asaas manualmente durante o onboard, e só automatizaria com 30-50 clientes.

## Como aplicar

É o roteiro pronto para cobrar no SaaS sem virar projeto: começar recebendo Pix na mão, e só quando houver cliente recorrente guardar o customer_id do Asaas no tenant e listar cobranças com um GET — o resto (cron de cobrança avulsa, webhook de pagamento confirmado, NF por API) entra quando o modelo de preço estabilizar. Para vender sites como serviço, a mesma conta cobra o cliente e emite a nota automaticamente, resolvendo a parte chata do faturamento por ~R$ 1 por NF.

## 🧠 Stella diz

Kwahaha! Fernando, este aqui é ouro puro disfarçado de vídeo de canal pequeno: um engenheiro mostrando a ordem em que as coisas devem ser construídas, e não a arquitetura completa que ninguém precisa no primeiro dia. A frase que eu quero que você tatue é a dele — é melhor arrumar a casa com cliente pagando do que ter a casa arrumada e ninguém dentro. Ah, e perdão pelo entusiasmo, mas a nota fiscal automática por um real resolve sozinha o problema que sempre trava o brasileiro que vende software.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
