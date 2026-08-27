---
item_id: "b0719519-d2d2-4464-93f5-bc1dc1dabf7d"
platform: article
external_id: "119ad20aa1ad"
canonical_url: "https://resend.com/docs/dashboard/emails/embed-inline-images"
channel: "Resend"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["resend", "cid", "imagens-inline", "anexos", "html-email", "python"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend — imagens embutidas (CID) em e-mails: HTML com cid: e anexo com content_id (exemplos em várias linguagens)

🔗 https://resend.com/docs/dashboard/emails/embed-inline-images

## Resumo

Como embutir imagens inline no corpo do e-mail via CID: no HTML, <img src="cid:logo-image">; no anexo, informar content_id (string arbitrária, menos de 128 caracteres). Funciona com anexos remotos (path = URL) e locais (content em Base64), com as mesmas regras e limites dos anexos; não funciona no endpoint de lote. Exemplos completos em Node, PHP, Python, Ruby, Go e outros para imagem remota e local.

## Tópicos

- **Passos** — cid: no src; content_id no attachment.
- **Fontes** — Remota (path) ou local (content Base64).
- **Limites** — Mesmos dos anexos; sem lote.

## Pontos-chave

- Logo no e-mail sem depender de imagem externa bloqueada pelo cliente de e-mail.
- Aumenta o tamanho do e-mail — respeitar 40 MB.
- Sem CID em batch.

## Como aplicar

Logo do SaaS nos e-mails transacionais via CID (exemplo Python pronto), fora dos lotes.

## 🔧 Atlas diz

Dois parafusos: cid: no HTML e content_id no anexo. O exemplo em Python está na doc, copia e cola. Só lembra que imagem embutida pesa e não vai em lote.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

We currently do not support sending attachments (including inline images)
when using our batch endpoint.

1

Add the CID in the email HTML.

Use the prefix 

`cid:` to reference the ID in the `src` attribute of an image tag in the HTML body of the email.```
  <img src="cid:logo-image">
```
2

Reference the CID in the attachment.

Include the content id parameter in the attachment object (see below for example implementations). The ID is an arbitrary string set by you, and must be less than 128 characters.

### Implementation details

Both remote and local attachments are supported. All attachment requirements, options, and limitations apply to inline images as well. As with all our features, inline images are available across all our SDKs.
#### Remote image example

```
import { Resend } from 'resend';
const resend = new Resend('re_xxxxxxxxx');
await resend.emails.send({
  from: 'Acme <onboarding@resend.dev>',
  to: ['delivered@resend.dev'],
  subject: 'Thank you for contacting us',
  html: '<p>Here is our <img src="cid:logo-image"/> inline logo</p>',
  attachments: [
    {
      path: 'https://resend.com/static/sample/logo.png',
      filename: 'logo.png',
      contentId: 'logo-image',
    },
  ],
});
```
```
$resend = Resend::client('re_xxxxxxxxx');
$resend->emails->send([
  'from' => 'Acme <onboarding@resend.dev>',
  'to' => ['delivered@resend.dev'],
  'subject' => 'Thank you for contacting us',
  'html' => '<p>Here is our <img src="cid:logo-image"/> inline logo</p>',
  'attachments' => [
    [
      'path' => 'https://resend.com/static/sample/logo.png',
      'filename' => 'logo.png',
      'content_id' => 'logo-image',
    ]
  ]
]);
```
```
import resend
resend.api_key = "re_xxxxxxxxx"
attachment: resend.RemoteAttachment = {
  "path": "https://resend.com/static/sample/logo.png",
  "filename": "logo.png",
  "content_id": "logo-image",
}
params: resend.Emails.SendParams = {
  "from": "Acme <onboarding@resend.dev>",
  "to": ["delivered@resend.dev"],
  "subject": "Thank you for contacting us",
  "html": "<p>Here is our <img src=\"cid:logo-image\"/> inline logo</p>",
  "attachments": [attachment],
}
resend.Emails.send(params)
```
```
require "resend"
Resend.api_key = "re_xxxxxxxxx"
params = {
  "from": "Acme <onboarding@resend.dev>",
  "to": ["delivered@resend.dev"],
  "subject": "Thank you for contacting us",
  "html": "<p>Here is our <img src=\"cid:logo-image\"/> inline logo</p>",
  "attachments": [
    {
      "path": "https://resend.com/static/sample/logo.png",
      "filename": 'logo.png',
      "content_id": "logo-image",
    }
  ]
}
Resend::Emails.send(params)
```
```
import (
	"fmt"
	"github.com/resend/resend-go/v3"
)
func main() {
  ctx := context.TODO()
  client := resend.NewClient("re_xxxxxxxxx")
  attachment := &resend.Attachment{
    Path:  "https://resend.com/static/sample/logo.png",
    Filename: "logo.png",
    ContentId: "logo-image",
  }
  params := &resend.SendEmailRequest{
      From:        "Acme <onboarding@resend.dev>",
      To:          []string{"delivered@resend.dev"},
      Subject:     "Thank you for contacting us",
      Html:        "<p>Here is our <img src=\"cid:logo-image\"/> inline logo</p>",
      Attachments: []*resend.Attachment{attachment},
  }
  sent, err := client.Emails.SendWithContext(ctx, params)
  if err != nil {
    panic(err)
  }
  fmt.Println(sent.Id)
}
```
```
use resend_rs::types::{CreateAttachment, CreateEmailBaseOptions};
use resend_rs::{Resend, Result};
#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");
  let from = "Acme <onboarding@resend.dev>";
  let to = ["delivered@resend.dev"];
  let subject = "Thank you for contacting us";
  let path = "https://resend.com/static/sample/logo.png";
  let filename = "logo.png";
  let content_id = "logo-image";
  let email = CreateEmailBaseOptions::new(from, to, subject)
    .with_html("<p>Here is our <img src=\"cid:logo-image\"/> inline logo</p>")
    .with_attachment(
      CreateAttachment::from_path(path)
        .with_filename(filename)
        .with_content_id(content_id),
    );
  let _email = resend.emails.send(email).await?;
  Ok(())
}
```
```
import com.resend.*;
public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");
        Attachment att = Attachment.builder()
                .path("https://resend.com/static/sample/logo.png")
                .fileName("logo.png")
                .ContentId("logo-image")
                .build();
        CreateEmailOptions params = CreateEmailOptions.builder()
                .from("Acme <onboarding@resend.dev>")
                .to("delivered@resend.dev")
                .subject("Thank you for contacting us")
                .html("<p>Here is our <img src=\"cid:logo-image\"/> inline logo</p>")
                .attachments(att)
                .build();
        CreateEmailResponse data = resend.emails().send(params);
    }
}
```
```
using Resend;
using System.Collections.Generic;
IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI
var message = new EmailMessage()
{
    From = "Acme <onboarding@resend.dev>",
    To = "delivered@resend.dev",
    Subject = "Thank you for contacting us",
    HtmlBody = "<p>Here is our <img src=\"cid:logo-image\"/> inline logo</p>",
};
message.Attachments = new List<EmailAttachment>();
message.Attachments.Add( new EmailAttachment() {
  Filename = "logo.png",
  Path = "https://resend.com/static/sample/logo.png",
  ContentId = "logo-image",
} );
var resp = await resend.EmailSendAsync( message );
Console.WriteLine( "Email Id={0}", resp.Content );
```
```
curl -X POST 'https://api.resend.com/emails' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d $'{
  "from": "Acme <onboarding@resend.dev>",
  "to": ["delivered@resend.dev"],
  "subject": "Thank you for contacting us",
  "html": "<p>Here is our <img src=\"cid:logo-image\"/> inline logo</p>",
  "attachments": [
    {
      "path": "https://resend.com/static/sample/logo.png",
      "filename": "logo.png",
      "content_id": "logo-image"
    }
  ]
}'
```
#### Local image example

```
import { Resend } from 'resend';
import fs from 'fs';
const resend = new Resend('re_xxxxxxxxx');
const filepath = `${__dirname}/static/logo.png`;
const attachment = fs.readFileSync(filepath).toString('base64');
await resend.emails.send({
  from: 'Acme <onboarding@resend.dev>',
  to: ['delivered@resend.dev'],
  subject: 'Thank you for contacting us',
  html: '<p>Here is our <img src="cid:logo-image"/> inline logo</p>',
  attachments: [
    {
      content: attachment,
      filename: 'logo.png',
      contentId: 'logo-image',
    },
  ],
});
```
```
$resend = Resend::client('re_xxxxxxxxx');
$resend->emails->send([
  'from' => 'Acme <onboarding@resend.dev>',
  'to' => ['delivered@resend.dev'],
  'subject' => 'Thank you for contacting us',
  'html' => '<p>Here is our <img src="cid:logo-image"/> inline logo</p>',
  'attachments' => [
    [
      'filename' => 'logo.png',
      'content' => $invoiceBuffer,
      'content_id' => 'logo-image',
    ]
  ]
]);
```
```
import os
import resend
resend.api_key = "re_xxxxxxxxx"
f: bytes = open(
  os.path.join(os.path.dirname(__file__), "../static/logo.png"), "rb"
).read()
attachment: resend.Attachment = {"content": list(f), "filename": "logo.png", "content_id": "logo-image"}
params: resend.Emails.SendParams = {
  "from": "Acme <onboarding@resend.dev>",
  "to": ["delivered@resend.dev"],
  "subject": "Thank you for contacting us",
  "html": "<p>Here is our <img src=\"cid:logo-image\"/> inline logo</p>",
  "attachments": [attachment],
}
resend.Emails.send(params)
```
```
require "resend"
Resend.api_key = "re_xxxxxxxxx"
file = IO.read("logo.png")
params = {
  "from": "Acme <onboarding@resend.dev>",
  "to": ["delivered@resend.dev"],
  "subject": "Thank you for contacting us",
  "html": "<p>Here is our <img src=\"cid:logo-image\"/> inline logo</p>",
  "attachments": [
    {
      "content": file.bytes,
      "filename": 'logo.png',
      "content_id": "logo-image",
    }
  ]
}
Resend::Emails.send(params)
```
```
import (
	"fmt"
	"os"
	"github.com/resend/resend-go/v3"
)
func main() {
  ctx := context.TODO()
  client := resend.NewClient("re_xxxxxxxxx")
  pwd, _ := os.Getwd()
  f, err := os.ReadFile(pwd + "/static/logo.png")
  if err != nil {
    panic(err)
  }
  attachment := &resend.Attachment{
    Content:  f,
    Filename: "logo.png",
    ContentId: "logo-image",
  }
  params := &resend.SendEmailRequest{
      From:        "Acme <onboarding@resend.dev>",
      To:          []string{"delivered@resend.dev"},
      Subject:     "Thank you for contacting us",
      Html:        "<p>Here is our <img src=\"cid:logo-image\"/> inline logo</p>",
      Attachments: []*resend.Attachment{attachment},
  }
  sent, err := client.Emails.SendWithContext(ctx, params)
  if err != nil {
    panic(err)
  }
  fmt.Println(sent.Id)
}
```
```
use std::fs::File;
use std::io::Read;
use resend_rs::types::{CreateAttachment, CreateEmailBaseOptions};
use resend_rs::{Resend, Result};
#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");
  let from = "Acme <onboarding@resend.dev>";
  let to = ["delivered@resend.dev"];
  let subject = "Thank you for contacting us";
  let filename = "logo.png";
  let content_id = "logo-image";
  let mut f = File::open(filename).unwrap();
  let mut invoice = Vec::new();
  f.read_to_end(&mut invoice).unwrap();
  let email = CreateEmailBaseOptions::new(from, to, subject)
    .with_html("<p>Here is our <img src=\"cid:logo-image\"/> inline logo</p>")
    .with_attachment(
      CreateAttachment::from_content(invoice)
        .with_filename(filename)
        .with_content_id(content_id),
    );
  let _email = resend.emails.send(email).await?;
  Ok(())
}
```
```
import com.resend.*;
public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");
        Attachment att = Attachment.builder()
                .fileName("logo.png")
                .content("invoiceBuffer")
                .contentId("logo-image")
                .build();
        CreateEmailOptions params = CreateEmailOptions.builder()
                .from("Acme <onboarding@resend.dev>")
                .to("delivered@resend.dev")
                .subject("Thank you for contacting us")
                .html("<p>Here is our <img src=\"cid:logo-image\"/> inline logo</p>")
                .attachments(att)
                .build();
        CreateEmailOptions params = CreateEmailOptions.builder()
    }
}
```
```
using Resend;
using System.Collections.Generic;
using System.IO;
IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI
var message = new EmailMessage()
{
    From = "Acme <onboarding@resend.dev>",
    To = "delivered@resend.dev",
    Subject = "Thank you for contacting us",
    HtmlBody = "<p>Here is our <img src=\"cid:logo-image\"/> inline logo</p>",
};
message.Attachments = new List<EmailAttachment>();
message.Attachments.Add( new EmailAttachment() {
  Filename = "logo.png",
  Content = await File.ReadAllBytesAsync( "logo.png" ),
  ContentId = "logo-image",
} );
var resp = await resend.EmailSendAsync( message );
Console.WriteLine( "Email Id={0}", resp.Content );
```
```
curl -X POST 'https://api.resend.com/emails' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d $'{
  "from": "Acme <onboarding@resend.dev>",
  "to": ["delivered@resend.dev"],
  "subject": "Thank you for contacting us",
  "html": "<p>Here is our <img src=\"cid:logo-image\"/> inline logo</p>",
  "attachments": [
    {
      "content": "UmVzZW5kIGF0dGFjaG1lbnQgZXhhbXBsZS4gTmljZSBqb2Igc2VuZGluZyB0aGUgZW1haWwh%",
      "filename": "invoice.txt",
      "content_id": "logo-image"
    }
  ]
}'
```
### Other considerations

Before adding inline images, consider the following.
- As these images are sent as attachments, you need to encode your image as Base64 when sending the raw content via the API. There is no need to do this when passing the path of a remote image (the API handles this for you).
- Inline images increase the size of the email.
- Inline images may be rejected by some clients (especially webmail).
- As with all attachments, add a `content_type` (e.g.`image/png` ) or`filename` (e.g.`logo.png` ) parameter to the attachment object. This helps email clients render the attachment correctly.

All attachments (including inline images) do not currently display in the
emails dashboard when previewing email HTML.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
