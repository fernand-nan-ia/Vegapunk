---
item_id: "953234cd-cd45-4388-90a4-6e916ee5f891"
platform: article
external_id: "307fcd951e99"
canonical_url: "https://resend.com/docs/dashboard/automations/connections"
channel: "Resend"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["resend", "automations", "api", "infra-como-codigo", "python"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Resend — connections: definindo as ligações entre passos de uma automação via API (exemplos em 6 linguagens)

🔗 https://resend.com/docs/dashboard/automations/connections

## Resumo

Connections são as arestas do grafo de uma Automation quando ela é criada pela API: um array de objetos {from, to} ligando as chaves dos passos. O exemplo cria a automação 'Welcome series' com dois passos — trigger (eventName user.created) e send_email com template — e a conexão start → welcome, em Node, PHP, Python, Ruby, Go e outras linguagens. Status inicial 'disabled'.

## Tópicos

- **Modelo** — steps (key, type, config) + connections [{from,to}].
- **Exemplo** — Welcome series: start (trigger) → welcome (send_email template), status disabled.

## Pontos-chave

- Automação como código: dá para versionar o onboarding no repositório do SaaS.
- Criar como 'disabled' e habilitar depois de revisar.

## Como aplicar

Definir as automações do SaaS em Python no repositório (steps + connections) em vez de clicar no painel — reprodutível e revisável pela Lilith.

## 🔧 Atlas diz

Isso eu gosto: automação como código, no repositório, com diff. O exemplo em Python é o nosso caso. Cria disabled, a Lilith verifica, aí liga.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

### How it works

Connections are the code definitions for the links between steps in the Automation graph and are defined and retrieved using the API. If creating an Automation via the API, define connections as an array of objects.```
import { Resend } from 'resend';
const resend = new Resend('re_xxxxxxxxx');
const { data, error } = await resend.automations.create({
  name: 'Welcome series',
  status: 'disabled',
  steps: [
    {
      key: 'start',
      type: 'trigger',
      config: { eventName: 'user.created' },
    },
    {
      key: 'welcome',
      type: 'send_email',
      config: {
        template: { id: '34a080c9-b17d-4187-ad80-5af20266e535' },
      },
    },
  ],
  connections: [{ from: 'start', to: 'welcome' }],
});
```
```
$resend = Resend::client('re_xxxxxxxxx');
$resend->automations->create([
  'name' => 'Welcome series',
  'status' => 'disabled',
  'steps' => [
    [
      'key' => 'start',
      'type' => 'trigger',
      'config' => ['event_name' => 'user.created'],
    ],
    [
      'key' => 'welcome',
      'type' => 'send_email',
      'config' => [
        'template' => ['id' => '34a080c9-b17d-4187-ad80-5af20266e535'],
      ],
    ],
  ],
  'connections' => [['from' => 'start', 'to' => 'welcome']],
]);
```
```
import resend
resend.api_key = "re_xxxxxxxxx"
params: resend.Automations.CreateParams = {
  "name": "Welcome series",
  "status": "disabled",
  "steps": [
    {
      "key": "start",
      "type": "trigger",
      "config": {"event_name": "user.created"},
    },
    {
      "key": "welcome",
      "type": "send_email",
      "config": {
        "template": {"id": "34a080c9-b17d-4187-ad80-5af20266e535"},
      },
    },
  ],
  "connections": [{"from": "start", "to": "welcome"}],
}
resend.Automations.create(params)
```
```
require "resend"
Resend.api_key = "re_xxxxxxxxx"
params = {
  name: "Welcome series",
  status: "disabled",
  steps: [
    {
      key: "start",
      type: "trigger",
      config: { event_name: "user.created" },
    },
    {
      key: "welcome",
      type: "send_email",
      config: {
        template: { id: "34a080c9-b17d-4187-ad80-5af20266e535" },
      },
    },
  ],
  connections: [{ from: "start", to: "welcome" }],
}
Resend::Automations.create(params)
```
```
package main
import "github.com/resend/resend-go/v3"
func main() {
	client := resend.NewClient("re_xxxxxxxxx")
	params := &resend.CreateAutomationRequest{
		Name:   "Welcome series",
		Status: resend.AutomationStatusDisabled,
		Steps: []resend.AutomationStep{
			{
				Key:  "start",
				Type: resend.AutomationStepTypeTrigger,
				Config: map[string]any{
					"event_name": "user.created",
				},
			},
			{
				Key:  "welcome",
				Type: resend.AutomationStepTypeSendEmail,
				Config: map[string]any{
					"template": map[string]any{
						"id": "34a080c9-b17d-4187-ad80-5af20266e535",
					},
				},
			},
		},
		Connections: []resend.AutomationConnection{
			{From: "start", To: "welcome"},
		},
	}
	client.Automations.Create(params)
}
```
```
use resend_rs::{
  types::{
    AutomationStatus, AutomationTemplate, Connection, CreateAutomationOptions, SendEmailStepConfig,
    Step, TriggerStepConfig,
  },
  Resend, Result,
};
#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");
  let opts = CreateAutomationOptions {
    name: "Welcome series".to_owned(),
    status: AutomationStatus::Disabled,
    steps: vec![
      Step::Trigger {
        key: "start".to_owned(),
        config: TriggerStepConfig {
          event_name: "user.created".to_owned(),
        },
      },
      Step::SendEmail {
        key: "welcome".to_owned(),
        config: SendEmailStepConfig::new(AutomationTemplate::new(
          "34a080c9-b17d-4187-ad80-5af20266e535",
        )),
      },
    ],
    connections: vec![Connection::new("start", "welcome")],
  };
  let _automation = resend.automations.create(opts).await?;
  Ok(())
}
```
```
import com.resend.*;
public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");
        CreateAutomationOptions options = CreateAutomationOptions.builder()
                .name("Welcome series")
                .status(AutomationStatus.DISABLED)
                .steps(
                    AutomationStep.trigger("start")
                        .eventName("user.created")
                        .build(),
                    AutomationStep.sendEmail("welcome")
                        .template("34a080c9-b17d-4187-ad80-5af20266e535")
                        .build()
                )
                .connections(
                    AutomationConnection.builder()
                        .from("start")
                        .to("welcome")
                        .build()
                )
                .build();
        CreateAutomationResponseSuccess data = resend.automations().create(options);
    }
}
```
```
using Resend;
using System.Text.Json;
IResend resend = ResendClient.Create( "re_xxxxxxxxx" );
var startConfig = JsonSerializer.SerializeToElement( new { event_name = "user.created" } );
var welcomeConfig = JsonSerializer.SerializeToElement( new { template = new { id = "34a080c9-b17d-4187-ad80-5af20266e535" } } );
var resp = await resend.AutomationCreateAsync( new AutomationCreateData()
{
    Name = "Welcome series",
    Status = "disabled",
    Steps = new List<AutomationStepData>
    {
        new AutomationStepData { Ref = "start", Type = "trigger", Config = startConfig },
        new AutomationStepData { Ref = "welcome", Type = "send_email", Config = welcomeConfig },
    },
    Connections = new List<AutomationEdge>
    {
        new AutomationEdge { From = "start", To = "welcome" },
    },
} );
```
```
curl -X POST 'https://api.resend.com/automations' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d '{
  "name": "Welcome series",
  "steps": [
    {
      "key": "start",
      "type": "trigger",
      "config": { "event_name": "user.created" }
    },
    {
      "key": "welcome",
      "type": "send_email",
      "config": {
        "template": { "id": "34a080c9-b17d-4187-ad80-5af20266e535" }
      }
    }
  ],
  "connections": [
    { "from": "start", "to": "welcome" }
  ]
}'
```
```
resend automations create --name "Welcome series" --file ./automation.json
```
```
{
  "object": "automation",
  "id": "c9b16d4f-ba6c-4e2e-b044-6bf4404e57fd",
  "name": "Welcome series",
  "status": "disabled",
  "created_at": "2026-10-01 12:00:00.000000+00",
  "updated_at": "2026-10-01 12:00:00.000000+00",
  "steps": [
    {
      "key": "start",
      "type": "trigger",
      "config": { "event_name": "user.created" }
    },
    {
      "key": "welcome",
      "type": "send_email",
      "config": {
        "template": { "id": "34a080c9-b17d-4187-ad80-5af20266e535" }
      }
    }
  ],
  "connections": [
    {
      "from": "start",
      "to": "welcome",
      "type": "default"
    }
  ]
}
```
### Connection properties

Connections define the links between steps in the automation graph.
string

required

This is the 

`key` of the origin step.
string

required

This is the 

`key` of the destination step.
string

The type of connection between the origin and destination steps. Most
automations use the default connection type.Use a non-default 

`type` only when the origin step can branch to multiple
destinations:
- For `wait_for_event` , use`event_received` or`timeout` .
- For `condition` , use`condition_met` or`condition_not_met` .

- `default`
- `condition_met`
- `condition_not_met`
- `timeout`
- `event_received`

Example

```
{
  "from": "start",
  "to": "welcome",
  "type": "default"
}
```

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
