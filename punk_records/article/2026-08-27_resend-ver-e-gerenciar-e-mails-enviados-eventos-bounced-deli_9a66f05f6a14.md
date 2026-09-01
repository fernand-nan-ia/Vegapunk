---
item_id: "0c804c12-bed4-4301-af4a-95fcd9362184"
platform: article
external_id: "9a66f05f6a14"
canonical_url: "https://resend.com/docs/dashboard/emails/manage-emails"
channel: "Resend"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["resend", "eventos-de-email", "bounce", "suppression-list", "painel"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend — ver e gerenciar e-mails enviados: eventos (bounced, delivered, complained…), link público e logs

🔗 https://resend.com/docs/dashboard/emails/manage-emails

## Resumo

Após o primeiro envio, os e-mails aparecem no painel com preview, texto puro e HTML, e podem ser geridos por MCP, API e CLI (listar, enviar, atualizar, cancelar agendados). Eventos possíveis: bounced (servidor do destinatário rejeitou), canceled (agendado cancelado), clicked, complained (marcado como spam), delivered, delivery_delayed (problema temporário, ex.: caixa cheia), failed, opened (impreciso), queued (lote/broadcast), scheduled, sent, suppressed (destinatário na lista de supressão). É possível gerar link público de um e-mail válido por 48 h (também via Share Email API) e ver os logs de API associados.

## Tópicos

- **Painel** — Preview, texto e HTML; gestão por API/CLI/MCP.
- **Eventos** — bounced, canceled, clicked, complained, delivered, delivery_delayed, failed, opened, queued, scheduled, sent, suppressed.
- **Compartilhar e depurar** — Link público 48 h; logs associados.

## Pontos-chave

- suppressed = o Resend nem tenta: destinatário deu bounce/complaint antes.
- delivery_delayed não é falha — o Resend retenta.
- Link público de 48 h resolve 'me mostra o e-mail que o cliente recebeu' sem print.

## Como aplicar

Mapear os eventos do Resend para o status do usuário no SaaS (bounced/complained → bloquear envio; suppressed → avisar admin).

## 🔧 Atlas diz

Doze estados e cada um manda um sinal: bounced e complained são 'para de mandar'; delivery_delayed é 'espera'; suppressed é 'o Resend já parou por você'. Isso vira uma tabelinha no SaaS — três parafusos.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### Manage your sent emails

After you’ve sent or scheduled your first email, your emails appear in the
**Emails**Dashboard page. You can view email details, share a public version, view email logs, and more. You can also manage your scheduled and sent emails using Resend’s code tools including the MCP server, API endpoints and CLI commands for tasks such as listing, sending, updating, and canceling emails.

### View email details

See all the metadata associated with a sent or scheduled email, including the sender address, recipient address, subject, and more from the
**Emails**Dashboard page. Select any email to view its details. Each email contains a

**Preview**,

**Plain Text**, and

**HTML**version to visualize the content of your sent email in its various formats.

### Understand email events

Here are all the events that can be associated with an email:
- `bounced` - The recipient’s mail server rejected the email. (Learn more about bounced emails)
- `canceled` - The scheduled email was canceled (by user).
- `clicked` - The recipient clicked on a link in the email.
- `complained` - The email was successfully delivered to the recipient’s mail server, but the recipient marked it as spam.
- `delivered` - Resend successfully delivered the email to the recipient’s mail server.
- `delivery_delayed` - The email couldn’t be delivered to the recipient’s mail server because a temporary issue occurred. Delivery delays can occur, for example, when the recipient’s inbox is full, or when the receiving email server experiences a transient issue.
- `failed` - The email failed to be sent.
- `opened` - The recipient opened the email. (Open rates are not always accurate)
- `queued` - The email created from Broadcasts or Batches is queued for delivery.
- `scheduled` - The email is scheduled for delivery.
- `sent` - The email was sent successfully.
- `suppressed` - The email was not sent because the recipient is on the suppression list. (Learn more about the suppression list)

### Share email link

You can share a public link of a sent email, which is valid for 48 hours. Anyone with the link can view the email. To share a link, click on the
**dropdown menu**, and select

**Share email**. Copy the URL and share it with your team members. Anyone with the link can view the email without authenticating for 48 hours. You can also create share links programmatically using the Share Email API.

### See associated logs

Check all the logs associated with an email to help you troubleshoot any issues with the request itself. To view the logs, click on the dropdown menu, and select “View log”. This will take you to logs, where you can see all the logs associated with the email.
### Export your data

Admins can download your data in CSV format for the following resources:
- Emails
- Broadcasts
- Contacts
- Segments
- Domains
- Logs
- API keys

Currently, exports are limited to admin users of your team.

All exports your team creates are listed in the
Exports page under 

**Settings**>**Team**>**Exports**. Select any export to view its details page. All members of your team can view your exports, but only admins can download the data.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
