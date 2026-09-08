---
item_id: "68a73752-4433-4123-99f6-66d90a12d65a"
platform: youtube
external_id: "m-ahYNfK_UU"
canonical_url: "https://www.youtube.com/watch?v=m-ahYNfK_UU"
channel: "Asaas"
captured_at: 2026-09-08
status: enriched
triage: null
tags: ["asaas", "api-de-assinaturas", "cobranca-recorrente", "tokenizacao-de-cartao", "nota-fiscal-automatica", "webhook", "reajuste-de-preco", "integracao-de-pagamento"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: transcript
---

# Assinaturas na API do Asaas: template de cobrança, tokenização de cartão e emissão automática de NF

🔗 https://www.youtube.com/watch?v=m-ahYNfK_UU

## Resumo

Vídeo oficial do time de desenvolvedores do Asaas explicando o recurso de assinaturas da API, indicado quando as cobranças são criadas de forma recorrente — mensalidade de software, aluguel, clubes. As periodicidades disponíveis são semanal, quinzenal, mensal, trimestral, semestral e anual. A distinção que estrutura o vídeo é entre assinatura e cobrança parcelada: na parcelada todas as parcelas são geradas no ato e, no cartão, o valor total é cobrado de uma só vez; a assinatura funciona como um template a partir do qual o Asaas gera uma cobrança nova a cada ciclo, como um streaming. Assinatura funciona com qualquer forma de pagamento — boleto, cartão ou Pix — e o vencimento da primeira cobrança é o que for definido em nextDueDate; na criação também se configuram descontos, juros, multa, descrição, ciclo, data de encerramento e número máximo de pagamentos. Para assinatura no cartão basta enviar os dados do cartão ou o token; se nextDueDate não for hoje, o Asaas valida o cartão e retorna 200 ou 400 — mas o vídeo alerta que validar não garante pagamento futuro, porque o cartão pode expirar, ser cancelado, bloqueado ou ficar sem saldo até a data da cobrança. Em Pix e boleto o valor e o vencimento são livremente editáveis; em cartão, alterar valor ou vencimento exige ter a tokenização habilitada na conta, o que passa por análise de risco do gerente de contas e pode ser negado. Como o Asaas gera as cobranças 40 dias antes do próximo vencimento, ao reajustar uma assinatura é preciso enviar updatePendingPayments como true, senão as cobranças já criadas e ainda não enviadas mantêm o valor antigo. Para trocar o cartão de uma assinatura, o procedimento é listar as cobranças da assinatura, pegar a primeira pendente e pagá-la com o novo cartão — o que cobra na hora e passa a valer para as próximas, algo que o vídeo recomenda deixar claro ao cliente. Por fim, há um endpoint de configuração de emissão automática de nota fiscal por assinatura, com escolha do momento (confirmação do pagamento, vencimento ou dias antes) e da restrição a cobranças efetivamente recebidas.

## Tópicos

- **Quando usar assinatura** — Cobranças recorrentes como mensalidade de software ou aluguel, nas periodicidades semanal, quinzenal, mensal, trimestral, semestral e anual.
- **Assinatura x cobrança parcelada** — Parcelada gera todas as parcelas na criação e, no cartão, cobra o total de uma vez; assinatura é um template que gera uma cobrança nova a cada ciclo, como um streaming.
- **Parâmetros de criação** — nextDueDate define o vencimento da primeira cobrança; também se configuram descontos, juros, multa, ciclo, descrição, data de encerramento e número máximo de pagamentos.
- **Assinatura no cartão de crédito** — Envia-se o cartão ou o token; se nextDueDate não for hoje o Asaas valida e retorna 200 ou 400, mas a validação não garante que a cobrança futura será paga (cartão pode expirar, ser cancelado, bloqueado ou ficar sem saldo).
- **Alterações e tokenização** — Em Pix e boleto valor e vencimento são livremente editáveis; em cartão é obrigatório ter a tokenização habilitada, o que depende do gerente de contas e passa por análise de risco, podendo ser negada.
- **Reajuste e updatePendingPayments** — As cobranças são geradas 40 dias antes do vencimento; para que um novo valor atinja as cobranças já criadas e ainda não enviadas é obrigatório enviar updatePendingPayments como true.
- **Troca de cartão e NF automática** — Trocar cartão = listar cobranças da assinatura, pegar a primeira pendente e pagá-la com o novo cartão, o que cobra na hora; há endpoint para configurar emissão automática de nota fiscal por assinatura.

## Ferramentas citadas

- **API de assinaturas do Asaas**: Recurso que cria cobranças recorrentes a partir de um template, objeto do vídeo
- **Tokenização de cartão do Asaas**: Pré-requisito para alterar valor ou vencimento em assinaturas no cartão; habilitação sujeita a análise de risco
- **Endpoint de configuração de NF**: Configura emissão automática de nota fiscal para as cobranças de uma assinatura

## Pontos-chave

- Validação de cartão na criação da assinatura retorna 200, mas não é promessa de pagamento: até a data da cobrança o cartão pode expirar, ser cancelado, bloqueado ou ficar sem saldo — trate falha de cobrança recorrente como cenário esperado, não como exceção.
- Alterar valor ou vencimento de assinatura no cartão exige tokenização habilitada, e a habilitação passa por análise de risco do Asaas, podendo ser negada: é uma dependência externa que precisa ser resolvida antes de prometer reajuste ao cliente.
- O Asaas gera as cobranças 40 dias antes do vencimento; num reajuste, sem updatePendingPayments=true as cobranças já criadas saem com o valor antigo.
- Assinatura não é parcelamento: parcelamento gera tudo na hora e cobra o total no cartão de uma vez; assinatura gera uma cobrança por ciclo.
- Assinatura funciona em boleto, Pix e cartão — em boleto o Asaas notifica o cliente a cada ciclo com o boleto do mês.
- Trocar o cartão de uma assinatura cobra imediatamente: o fluxo é listar as cobranças, pegar a primeira pendente e pagá-la com o novo cartão; avise o cliente antes de executar isso.
- Descontos, juros, multa, data de encerramento e número máximo de pagamentos são definidos na própria criação da assinatura, não em cada cobrança.
- Emissão de nota fiscal pode ser configurada por assinatura, com escolha do gatilho (confirmação do pagamento, vencimento, dias antes) e restrição a cobranças recebidas.

## Como aplicar

É a documentação em vídeo do caminho que o SaaS vai usar para mensalidade: criar a assinatura com nextDueDate e ciclo, ligar a emissão automática de NF ali mesmo e tratar falha de cobrança como fluxo normal. Antes de prometer reajuste ou mudança de plano em cartão, verificar se a tokenização foi aprovada na conta — e lembrar do updatePendingPayments em todo aumento de preço.

## 🪖 Shaka diz

Isto é documentação, não anúncio: o autor expõe as próprias limitações, o que aumenta a confiabilidade do material. Registre dois riscos operacionais. Primeiro, retorno 200 na validação do cartão não é garantia de recebimento futuro; quem tratar isso como certeza terá inadimplência silenciosa. Segundo, a tokenização — condição para alterar valores em cartão — depende de aprovação de terceiro e pode ser negada; não prometa reajuste automático a cliente antes de ter essa permissão em mãos.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
