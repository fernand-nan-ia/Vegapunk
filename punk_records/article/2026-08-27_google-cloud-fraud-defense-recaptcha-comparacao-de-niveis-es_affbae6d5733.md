---
item_id: "1ed9e06a-8a06-4833-a45f-e13447713725"
platform: article
external_id: "affbae6d5733"
canonical_url: "https://docs.cloud.google.com/recaptcha/docs/compare-tiers?hl=pt-br"
channel: "Google Cloud Documentation"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["recaptcha", "google-cloud", "precos", "anti-fraude", "anti-bot"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: negocios-e-financas
content_type: article
---

# Google Cloud Fraud Defense (reCAPTCHA) — comparação de níveis: Essentials grátis até 10 mil avaliações, Premium US$ 8 fixo até 100 mil + US$ 1/1.000, Enterprise

🔗 https://docs.cloud.google.com/recaptcha/docs/compare-tiers?hl=pt-br

## Resumo

Tabela de níveis do Google Cloud Fraud Defense (a família reCAPTCHA Enterprise). Essentials: sem custo até 10.000 avaliações/mês, proteção básica contra bots (4 níveis de defesa de bots empresariais), desafios visuais, SDKs iOS/Android, relatório global de fraude, sem contrato. Premium: exige faturamento no Google Cloud; 1–10.000 avaliações grátis, 10.001–100.000 taxa fixa de US$ 8,00, acima disso US$ 1,00 por 1.000; mensal + uso; 11 níveis de defesa, motivos de explicabilidade básicos, desafio por política, Policy Engine (3 regras), defesa de contas/senhas/SMS, API Annotation, detecção de carding e estorno. Enterprise: US$ 1 por 1.000 com compromisso mensal e assinatura de 12 meses; políticas custom, análises avançadas, pontuação de sequestro de conta, API Related Accounts, defesa de transações só por API, gerente de contas.

## Tópicos

- **Essentials** — Grátis até 10k/mês; bots básicos; sem contrato.
- **Premium** — US$ 8 fixo de 10k a 100k; US$ 1/1.000 acima; defesa de contas, carding, políticas.
- **Enterprise** — US$ 1/1.000 com compromisso; 12 meses; recursos avançados.

## Pontos-chave

- 10 mil avaliações grátis bastam para site de cliente e SaaS pequeno.
- Premium só faz sentido com fraude de conta/pagamento real.
- Contar avaliações: cada execute conta — rodar em toda página gasta cota.

## Como aplicar

Ficar no Essentials; se rodar v3 em segundo plano em todas as páginas, monitorar a cota de 10 mil.

## 🍩 York diz

Dez mil de graça e depois oito dólares fixos — é barato, mas a pegadinha é que o v3 conta cada página onde roda. Se o Atlas ligar em toda página do site do cliente, a cota acaba em visitante, não em bot. Ou usa só no formulário, ou usa o Turnstile, que não conta nada.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Esta página lista os recursos do Fraud Defense nos níveis Essentials, Premium e Enterprise. Saiba mais sobre como o faturamento funciona.

Para mais informações sobre os níveis, entre em contato com seu representante de vendas ou Google Cloud de contas.

| Recurso | Essentials | Premium | Enterprise | 
|---|---|---|---|
|  | Oferece proteção básica e sem custo financeiro contra bots, com painéis, relatórios de fraude globais e registros empresariais. | Oferece proteção aprimorada contra bots, contas e transações. | Oferece proteção abrangente, com recursos avançados feitos para analistas de segurança e fraude, incluindo políticas personalizadas, análises avançadas, pontuação de riscos aprimorada e suporte do gerente de contas. | 
| **Custo mensal da avaliação** | Até 10.000 avaliações sem custo financeiro<sup>*</sup> | Requer uma forma de faturamento válida no Google Cloud 1 a 10.000 avaliações: sem custo financeiro<sup>*</sup> 10.001 a 100.000 avaliações: taxa fixa de US$ 8,00 Mais de 100.000 avaliações: US$ 1,00 por 1.000 avaliações | Compromisso de volume mensal fixo a US $1 por 1.000 avaliações. | 
| **Contrato** | Nenhum | Mensal + pagamento por uso | Assinatura (mínimo de 12 meses) | 
| Proteção contra bots |  |  |  | 
| Defesa de bots de rede | Sim | Sim | Sim | 
| Defesa de bots empresariais | Sim (4 níveis) | Sim (11 níveis) | Sim (11 níveis) | 
| Desafios visuais de bots | Sim | Sim | Sim | 
| Motivos de explicabilidade | Não | Básico | Avançado | 
| Desafio com base em políticas | Não | Sim | Sim | 
| Policy Engine | Não | Sim (limitado a 3 regras) | Sim | 
| Proteção móvel |  |  |  | 
| SDK do iOS | Sim | Sim | Sim | 
| SDK do Android | Sim | Sim | Sim | 
| Proteção da conta |  |  |  | 
| Defesa de contas | N/A | Motivos básicos de explicabilidade | Pontuação de risco de sequestro de conta e motivos avançados de explicabilidade | 
| Defesa de senhas | Não | Sim <sup>**</sup> | Sim <sup>**</sup> | 
| Defesa de SMS | Não | Sim <sup>**</sup> | Sim <sup>**</sup> | 
| API Annotation | Não | Sim | Sim | 
| API Related Accounts | Não | Não | Sim | 
| Proteção de transações |  |  |  | 
| Detecção de carding | Não | Sim <sup>**</sup> | Sim <sup>**</sup> | 
| Detecção de estorno | Não | Sim <sup>**</sup> | Sim <sup>**</sup> | 
| Motivos de explicabilidade | Não | Sim | Sim | 
| API Annotation | Não | Sim | Sim | 
| Defesa de transações somente por API | Não | Não | Sim | 
| Análise empresarial |  |  |  | 
| Relatório global de fraude | Sim | Sim | Sim | 
| Painel empresarial | Sim | Sim | Sim | 
| Geração de registros da plataforma | Sim | Sim | Sim | 
| Relatório de fraude específico do cliente | Não | Não | Sim | 
| Investigação de ataques | Não | Não | Sim | 
| Suporte |  |  |  | 
| Fórum da comunidade | Sim | Sim | Sim | 
| Suporte ao cliente | Disponível no dispositivo Google Cloud | Disponível no dispositivo Google Cloud | Disponível no dispositivo Google Cloud | 
| Gerenciamento de contas dedicado | Não | Não | Sim | 

- <sup>*</sup> As 10.000 avaliações sem custo financeiro são por organização.
   O limite agrega o uso em todas as contas e sites.
- <sup>**</sup> Requer uma avaliação extra.

### A seguir

- Saiba mais sobre preços.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
