---
item_id: "11df3b44-eab1-4560-ae27-89d8ee133eb1"
platform: youtube
external_id: "jjMnQDAc5Mo"
canonical_url: "https://www.youtube.com/watch?v=jjMnQDAc5Mo"
channel: "A Vizinhança"
captured_at: 2026-09-10
status: applied_client
triage: apply_client
tags: ["n8n", "whatsapp-api", "manychat", "openai", "agentes-ia", "vps-hosting", "ia-atendimento", "redis"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: alta
  estudo_geral: media
confidence: alta
theme: ia-e-agentes
content_type: transcript
---

# Como criar e vender agentes de IA no WhatsApp com n8n e Claude

🔗 https://www.youtube.com/watch?v=jjMnQDAc5Mo

## Resumo

O vídeo ensina a estruturar e comercializar um agente de atendimento automatizado via WhatsApp para empresas utilizando n8n, ManyChat e a API da OpenAI. O autor defende um modelo de negócio em que cobra entre R$ 2.500 e R$ 7.000 pela instalação, repassando os custos operacionais de cerca de R$ 280 mensais diretamente ao cartão do cliente. A arquitetura técnica combina uma VPS Hostinger pré-configurada com n8n, uma instância Redis para latência/estado, ManyChat Pro conectado à Meta Cloud API e automação de fluxos orquestrada pelo Claude via VS Code com uma skill dedicada. A solução suporta mensagens de texto, transcrição de áudio e análise multimodal de imagens para responder dúvidas e enviar links de pagamento. Por fim, é apresentada uma abordagem de vendas focada na perda de conversões após o horário comercial para justificar o investimento perante donos de pequenas empresas.

## Tópicos

- **Modelo comercial e precificação** — Proposta de cobrar R$ 2.500 a R$ 7.000 por setup e transferir custos de VPS, ManyChat e tokens de IA (aprox. R$ 280/mês) para o cliente.
- **Infraestrutura e setup n8n com Redis** — Instalação do n8n em VPS Hostinger com container Redis auxiliar no mesmo Docker compose para gestão de fila e latência.
- **Integração Meta API via ManyChat Pro** — Configuração da BM do Facebook, verificação do CNPJ/número e criação dos fluxos de webhook, handoff humano e resposta personalizada no ManyChat.
- **Geração do fluxo com Claude Skill** — Uso de uma skill personalizada no Claude Code/VS Code para criar automaticamente os nós e a lógica do workflow dentro do n8n via API.
- **Script de prospecção e vendas** — Argumentação baseada em perguntar quem atende clientes após as 18h para evidenciar vendas perdidas durante a noite e madrugada.

## Ferramentas citadas

- **n8n**: Orquestrador de fluxos de automação e integração com a IA auto-hospedado na VPS
- **ManyChat Pro**: Interface de conexão oficial com WhatsApp Business API e controle de webhooks
- **OpenAI API**: Motor de inteligência artificial para processamento de texto, transcrição de áudio e visão computacional
- **Hostinger VPS**: Hospedagem em nuvem que executa a stack Docker com n8n e Redis
- **Redis**: Banco em memória para controle de concorrência, latência e estado nas chamadas da API
- **Claude**: Assistente utilizado no VS Code com skill customizada para gerar o workflow do n8n via API

## Pontos-chave

- O custo recorrente de infraestrutura (ManyChat Pro + VPS + créditos OpenAI) gira em torno de R$ 280/mês por cliente.
- A integração com a API oficial do WhatsApp exige verificação de empresa (BM) no Facebook com CNPJ, levando de 1 a 3 dias úteis.
- Uso de Redis no mesmo Docker Compose da VPS é necessário para contornar gargalos de latência no fluxo do n8n.
- O fluxo utiliza tags de 'transferido_humano' (handoff) no ManyChat para pausar a IA quando um atendente assume a conversa.
- A skill no Claude automatiza a criação do workflow dentro do n8n através de chamadas à API interna da ferramenta.

## Como aplicar

Pode ser adaptado como um serviço adicional de automação de WhatsApp para o projeto do cliente, reaproveitando a arquitetura de webhook do ManyChat com n8n para captura de leads e suporte básico.

## 🏴‍☠️ Lilith diz

Ah, claro, o clássico 'ganhe 6 mil por mês dormindo' embalado num cupom de afiliado da Hostinger! A arquitetura n8n + ManyChat + Redis até funciona, Fernando, mas o que ele não te conta é a dor de cabeça de suporte quando a BM da Meta bloquear o número do cliente na primeira campanha de spam. Se for montar isso pra alguém, cobre a implantação à vista e fuja da gestão do número antes que sobre pra você.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->

### Cruzamento com os projetos do Fernando (Claude Code, 11/09)

**Números declarados no vídeo:** cobrança de **R$ 2.500 a R$ 7.000** por instalação; custo recorrente de **R$ 250–280/mês** (VPS ~R$ 45 + ManyChat Pro R$ 150 + créditos), **no nome do cliente, não no do fornecedor**. Setup ~7 dias, quase todo consumido pela verificação da Business Manager do Facebook com CNPJ do cliente.

**Onde encaixa:** é o segundo degrau da escada de serviços que o vault já registra do mesmo canal — landing barata para entrar, automação depois. Deixar o custo recorrente no CNPJ do cliente é a mesma decisão já fechada para o domínio e para o Google Meu Negócio.

⚠️ **NÃO aplicar na psiquiatra sem passar pelo Shaka.** Atendimento automatizado em contexto médico esbarra na Resolução CFM 2.336/2023 e em **dado sensível de saúde** sob a LGPD. A decisão de não ter formulário no site foi tomada justamente para não coletar nada — um robô conversando sobre sintoma desfaz isso inteiro. Para a VDC (energia solar) não há esse impedimento; a pergunta a fazer ao cliente é se há volume de WhatsApp fora do horário comercial.

⚠️ **Conflito de interesse:** o vídeo é patrocinado pela Hostinger, com cupom do canal. A recomendação de VPS tem incentivo comercial — a pilha funciona em qualquer VPS.

**Skill Genesis** é gratuita e está na descrição do vídeo, sem cadastro. Revogar a chave de API do N8N depois de cada uso (o próprio autor alerta: ela dá acesso total ao fluxo).
