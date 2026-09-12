---
item_id: "76004883-d482-4d03-92e1-acbce911453e"
platform: article
external_id: "db0f157d9556"
canonical_url: "https://docs.netlify.com/manage/domains/configure-domains/bring-a-domain-to-netlify"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: applied_client
triage: apply_client
tags: ["netlify", "dominio-existente", "propagacao-de-dns", "registro-a", "dig", "verificacao-de-dns"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: alta
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Netlify — trazer domínio já registrado: adicionar ao site, apontar o DNS, esperar até 48h

🔗 https://docs.netlify.com/manage/domains/configure-domains/bring-a-domain-to-netlify

## Resumo

Passo a passo para usar na Netlify um domínio registrado em outro lugar. Primeiro, adicionar o domínio ao site em Domain management > Add domain > Add a domain you already own, digitar, verificar e confirmar; ele vira o domínio primário por padrão. Depois, configurar o DNS no provedor atual: o painel da Netlify mostra, em Pending DNS verification ao lado do domínio, as instruções específicas daquele caso, incluindo o valor exato a usar — o exemplo da documentação é copiar 75.2.60.5 para um registro A. Por fim, a verificação: as mudanças podem levar até 48 horas para propagar, e dá para conferir com o comando dig no terminal ou por um site como digwebinterface.com.

## Tópicos

- **Passo 1 — adicionar ao site** — Domain management > Add domain > Add a domain you already own, verificar e confirmar; vira primário por padrão.
- **Passo 2 — apontar o DNS** — A tela Pending DNS verification mostra o registro e o valor exatos para aquele domínio, como o IP 75.2.60.5 num registro A.
- **Passo 3 — verificar** — Até 48 horas de propagação; conferir com dig no terminal ou por um serviço como digwebinterface.com.

## Ferramentas citadas

- **dig**: comando de terminal para conferir a propagação do DNS
- **digwebinterface.com**: alternativa web ao dig para checar propagação

## Pontos-chave

- As instruções exatas de DNS aparecem em Pending DNS verification, personalizadas para o domínio.
- A propagação pode levar até 48 horas: prometer ao cliente que fica pronto na hora é promessa que você não controla.
- dig é a forma de saber se já propagou, em vez de ficar recarregando o navegador.
- O domínio adicionado vira primário automaticamente.

## Como aplicar

Este é o caminho quando o cliente já tem domínio e você NÃO quer mexer no DNS dele: adiciona o domínio ao projeto, cria um registro só, e o e-mail dele continua intocado. Avise das 48 horas antes, não depois — é a reclamação número um de quem entrega site com domínio.

## 📚 Pythagoras diz

Deduzo que este é o caminho que você mais vai usar com cliente que já existe: um registro, e o e-mail dele segue vivo. E diga as 48 horas ANTES; o cliente que não foi avisado acha que você quebrou o site dele.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

Bring an existing domain you’ve already registered to Netlify DNS and set it as a custom domain for your production site.

### Step 1: Add custom domain to your Netlify site

Section titled “Step 1: Add custom domain to your Netlify site”
1. 
Go to your Site Overview dashboard in Netlify and in the left sidebar, select **Domain management** .
2. 
Select **Add domain** , then**Add a domain you already own** .
3. 
Enter your domain and select **Verify** . Next, confirm with**Add domain** .

The custom domain you added will be the primary domain for your production site by default.

### Step 2: Update your DNS configuration

Section titled “Step 2: Update your DNS configuration”
The next steps will vary depending on your DNS provider, domain, and the DNS records you need but here is a general overview.

1. 
Go to the DNS provider settings for your custom domain.
2. 
Based on the custom domain you entered, you typically need to add a new DNS record for your domain.

1. 
Select or enter the DNS record type you need, add your custom domain or subdomain.
2. 
In Netlify, go to your domain dashboard for your site and select **Pending DNS verification** next to your custom domain. You’ll find more details there you can use to set up your custom domain. These details are customized for your domain.

For example, you may find this instruction:

You can copy the value `75.2.60.5` to add to an A record in your DNS provider for blueberry.com.

For more detailed help, check out Configure external DNS.

### Step 3: (Optional) Verify your setup

Section titled “Step 3: (Optional) Verify your setup”
After updating your DNS settings, you may need to wait up to 48 hours for your changes to take full effect.

In the meantime, you can re-review your setup and then verify your DNS propagation is working with the `dig` command in your terminal.

For example:

Or you can try a Dig lookup site like https://www.digwebinterface.com/.

##### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
