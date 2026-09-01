---
item_id: "c811cf26-b861-4731-a52e-b5afe965308a"
platform: article
external_id: "5db57f423da9"
canonical_url: "https://resend.com/docs/dashboard/emails/attachments"
channel: "Resend"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["resend", "anexos", "base64", "api", "limites"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend — anexos: arquivo remoto (path) ou local (Base64), CID, download via API e limites (40 MB, sem lote)

🔗 https://resend.com/docs/dashboard/emails/attachments

## Resumo

Anexos no Resend: remoto com path (URL) + filename, ou local com content (Base64) + filename. Imagens podem ser embutidas via CID (dois passos). Anexos de e-mails enviados podem ser vistos/baixados no painel ou pela Attachments API (List/Retrieve devolvem download_url assinada). Limites: e-mail até 40 MB incluindo anexos após Base64; alguns tipos de arquivo não são aceitos; sem anexos no endpoint de lote. Exemplos em Next.js, PHP, Laravel, Python e Ruby.

## Tópicos

- **Formas** — path (URL) ou content (Base64) + filename.
- **Recuperar** — Painel ou Attachments API com download_url assinada.
- **Limites** — 40 MB com Base64; tipos não suportados; sem lote.

## Pontos-chave

- Preferir path (URL) para arquivos grandes — Base64 infla 33%.
- Guardar o ID do e-mail permite recuperar o anexo depois pela API.
- Lista de tipos bloqueados existe — checar antes de mandar .exe/.zip.

## Como aplicar

Enviar laudos/relatórios em PDF do SaaS por URL assinada do storage em vez de Base64.

## 🔧 Atlas diz

Anexo por URL é o caminho leve: o PDF fica no storage e o Resend busca. Base64 só para coisa pequena. 40 MB é teto, não meta. E anexo nunca vai em lote — já disse, repito, porque é o erro mais comum.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

We currently do not support sending attachments when using our batch
endpoint.

### Send attachments from a remote file

Include the`path` parameter to send attachments from a remote file. This parameter accepts a URL to the file you want to attach.
Define the file name that will be attached using the `filename` parameter.
### Send attachments from a local file

Include the`content` parameter to send attachments from a local file. This parameter accepts the Base64 encoded content of the file you want to attach.
Define the file name that will be attached using the `filename` parameter.
### Embed Images using CID

You can optionally embed an image in the HTML body of the email. Both remote and local attachments are supported. All attachment requirements, options, and limitations apply to embedded inline images as well. Embedding images requires two steps:
**1. Add the CID in the email HTML.**Use the prefix

`cid:` to reference the ID in the `src` attribute of an image tag in the HTML body of the email.
**2. Reference the CID in the attachment**The content id is an arbitrary string set by you, and must be less than 128 characters.

### View and Download Attachments

You can view and download attachments from sent emails from the dashboard or programmatically through the Attachments API.
#### From the dashboard

1. Go to Emails.
2. Navigate to any email you sent with an attachment.
3. Click on the attachment to download it locally.

- Image
- Spreadsheet
- Default (for unknown types)

#### From the API

Use List Attachments to fetch all attachments for a sent email, or Retrieve Attachment to fetch a single one. Both endpoints return a signed`download_url` that you can use to download the content.
### Attachment Limitations

- Emails can be no larger than 40MB (including attachments after Base64 encoding).
- Not all file types are supported. See the list of unsupported file types.
- Emails with attachments cannot be sent using our batching endpoint.

### Examples

#### Attachments

### Next.js (TypeScript)

See the full source code.

### Next.js (JavaScript)

See the full source code.

### PHP

See the full source code.

### Laravel

See the full source code.

### Python

See the full source code.

### Ruby

See the full source code.

#### Inline Images (CID)

### Next.js (TypeScript)

See the full source code.

### Next.js (JavaScript)

See the full source code.

### PHP

See the full source code.

### Laravel

See the full source code.

### Python

See the full source code.

### Ruby

See the full source code.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
