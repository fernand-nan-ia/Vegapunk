---
item_id: "4e74e2fb-1412-47f5-b015-5e052cdc5517"
platform: article
external_id: "936685d222df"
canonical_url: "https://resend.com/docs/dashboard/emails/custom-headers"
channel: "Resend"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["resend", "headers", "gmail", "list-unsubscribe", "email-transacional"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend — cabeçalhos customizados: X-Entity-Ref-ID (evitar agrupamento no Gmail) e List-Unsubscribe

🔗 https://resend.com/docs/dashboard/emails/custom-headers

## Resumo

Cabeçalhos customizados no envio: o parâmetro headers aceita pares chave/valor. Dois usos documentados: X-Entity-Ref-ID com valor único por e-mail para impedir que o Gmail agrupe mensagens numa mesma thread, e List-Unsubscribe para oferecer descadastro em um clique. Exemplos em Node, PHP, Python, Ruby, Go, Rust, Java e outros.

## Tópicos

- **X-Entity-Ref-ID** — Valor único por mensagem; Gmail não agrupa.
- **List-Unsubscribe** — Descadastro em um clique; exigido em marketing.

## Pontos-chave

- Notificações repetidas (mesmo assunto) precisam de X-Entity-Ref-ID para não sumirem numa thread.
- List-Unsubscribe é boa prática e requisito de grandes provedores para volume.

## Como aplicar

Alertas do SaaS com assunto igual: X-Entity-Ref-ID = id do evento; newsletter: List-Unsubscribe.

## 🔧 Atlas diz

Um parafuso que salva suporte: alerta com o mesmo assunto some dentro da thread do Gmail e o usuário jura que não recebeu. X-Entity-Ref-ID único e pronto. Exemplo Python na doc.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

- Prevent threading on Gmail with the **`X-Entity-Ref-ID`** header (Example)
- Include a shortcut for users to unsubscribe with the **`List-Unsubscribe`** header

```
import { Resend } from 'resend';
const resend = new Resend('re_xxxxxxxxx');
await resend.emails.send({
  from: 'Acme <onboarding@resend.dev>',
  to: ['delivered@resend.dev'],
  subject: 'hello world',
  html: '<p>it works!</p>',
  headers: {
    'X-Entity-Ref-ID': 'xxx_xxxx',
  },
});
```
```
$resend = Resend::client('re_xxxxxxxxx');
$resend->emails->send([
  'from' => 'Acme <onboarding@resend.dev>',
  'to' => ['delivered@resend.dev'],
  'subject' => 'hello world',
  'html' => '<p>it works!</p>',
  'headers' => [
    'X-Entity-Ref-ID' => 'xxx_xxxx',
  ]
]);
```
```
import resend
resend.api_key = "re_xxxxxxxxx"
params: resend.Emails.SendParams = {
  "from": "onboarding@resend.dev",
  "to": ["delivered@resend.dev"],
  "subject": "hi",
  "html": "<p>it works!</p>",
  "headers": {
    "X-Entity-Ref-ID": "xxx_xxxx"
  }
}
email = resend.Emails.send(params)
print(email)
```
```
require "resend"
Resend.api_key = "re_xxxxxxxxx"
params = {
  "from": "Acme <onboarding@resend.dev>",
  "to": ["delivered@resend.dev"],
  "subject": "hello world",
  "html": "<p>it works!</p>",
  "headers": {
    "X-Entity-Ref-ID": "123"
  },
}
sent = Resend::Emails.send(params)
puts sent
```
```
import (
	"fmt"
	"github.com/resend/resend-go/v3"
)
func main() {
  ctx := context.TODO()
  client := resend.NewClient("re_xxxxxxxxx")
  params := &resend.SendEmailRequest{
      From:        "Acme <onboarding@resend.dev>",
      To:          []string{"delivered@resend.dev"},
      Subject:     "hello world",
      Html:        "<p>it works!</p>",
      Headers:     map[string]string{
        "X-Entity-Ref-ID": "xxx_xxxx",
      }
  }
  sent, err := client.Emails.SendWithContext(ctx, params)
  if err != nil {
    panic(err)
  }
  fmt.Println(sent.Id)
}
```
```
use resend_rs::types::{Attachment, CreateEmailBaseOptions, Tag};
use resend_rs::{Resend, Result};
#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");
  let from = "Acme <onboarding@resend.dev>";
  let to = ["delivered@resend.dev"];
  let subject = "hello world";
  let email = CreateEmailBaseOptions::new(from, to, subject)
    .with_html("<p>it works!</p>")
    .with_header("X-Entity-Ref-ID", "xxx_xxxx");
  let _email = resend.emails.send(email).await?;
  Ok(())
}
```
```
import com.resend.*;
public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");
        CreateEmailOptions params = CreateEmailOptions.builder()
                .from("Acme <onboarding@resend.dev>")
                .to("delivered@resend.dev")
                .subject("hello world")
                .html("<p>it works!</p>")
                .headers(Map.of(
                    "X-Entity-Ref-ID", "xxx_xxxx"
                ))
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
    Subject = "hello world",
    HtmlBody = "<p>it works!</p>",
    Headers = new Dictionary<string, string>()
    {
        { "X-Entity-Ref-ID", "xxx_xxxx" },
    },
};
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
  "subject": "hello world",
  "html": "<p>it works!</p>",
  "headers": {
    "X-Entity-Ref-ID": "xxx_xxxx"
  }
}'
```
```
resend emails send \
  --from "Acme <onboarding@resend.dev>" \
  --to delivered@resend.dev \
  --subject "hello world" \
  --html "<p>it works!</p>" \
  --headers "X-Entity-Ref-ID=xxx_xxxx"
```

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
