---
item_id: "d394e9c1-e30e-47f4-b008-0ab9f38df823"
platform: article
external_id: "4dc8456d476a"
canonical_url: "https://docs.netlify.com/manage/domains/configure-domains/dns-records"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: enriched
triage: null
tags: ["dns-records", "mx", "txt", "spf", "caa", "netlify-dns", "email-no-dominio"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Netlify DNS — tipos de registro suportados e como adicionar (inclusive MX de e-mail)

🔗 https://docs.netlify.com/manage/domains/configure-domains/dns-records

## Resumo

Referência dos registros DNS aceitos pelo Netlify DNS. Para domínios gerenciados pela Netlify, registros NETLIFY apontando para os servidores dela são criados automaticamente ao atribuir domínio ou subdomínio a um site. Além desses, o usuário pode adicionar os seus para apontar a outros serviços, como provedor de e-mail. Os tipos suportados são A (IPv4), AAAA (IPv6), CAA (quais autoridades podem emitir certificado), CNAME (nome alternativo), MX (servidores de e-mail), NS (delegação de zona), SPF (obsoleto, usar TXT), SRV (localizador de serviço, usado por VoIP e mensageria) e TXT (texto de até 255 caracteres, usado para verificação e segurança). O caminho é o painel da equipe, DNS na barra lateral, selecionar a zona, Add new record e salvar; mudanças podem levar algumas horas para propagar. Há uma condição comercial declarada: é possível hospedar registros de outros serviços, como e-mail ou API de backend, desde que pelo menos um site naquele domínio esteja hospedado na Netlify.

## Tópicos

- **Registros automáticos** — Registros NETLIFY apontando para os servidores da plataforma são criados sozinhos ao atribuir domínio a um site.
- **Tipos suportados** — A, AAAA, CAA, CNAME, MX, NS, SPF (obsoleto, usar TXT), SRV e TXT de até 255 caracteres.
- **Condição para hospedar outros serviços** — É permitido manter registros de e-mail ou API, desde que pelo menos um site daquele domínio esteja hospedado na Netlify.

## Ferramentas citadas

- **Netlify**: plataforma de hospedagem e DNS descrita no documento

## Pontos-chave

- MX é suportado: o e-mail do cliente pode continuar funcionando com DNS na Netlify.
- SPF como tipo de registro está obsoleto; o correto hoje é TXT.
- TXT tem limite de 255 caracteres.
- CAA controla qual autoridade certificadora pode emitir certificado para o domínio.
- Hospedar registros de terceiros exige ter ao menos um site do domínio na Netlify.
- Mudanças de registro podem levar horas para propagar.

## Como aplicar

É a lista de conferência quando você migrar o DNS de um cliente que tem e-mail: MX, TXT de verificação e SPF precisam ser recriados um a um, porque a Netlify não importa zona. Esquecer um MX derruba o e-mail da empresa, e o cliente vai associar isso ao seu site novo.

## 📚 Pythagoras diz

A lista importa menos que a ausência: não há importação, então cada MX e cada TXT do cliente é recriado à mão por você. Faça a lista antes de mexer, e confira item por item depois.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

DNS records are rules that tell domain name servers how to handle traffic to your domains and subdomains.

For domains managed by Netlify, we will automatically create “NETLIFY” records that point to our servers when you assign a domain or subdomain for your site. To learn more, visit our Forums for a verified support guide on this type of DNS record.

You can also add your own DNS records to point to other services, such as an email provider. Visit our Forums for a verified Support Guide on how to receive emails on your domain.

### Supported record types

Section titled “Supported record types”
Netlify DNS supports the following types of records:

- **A** : Address record, which is used to map host names to their IPv4 address.
- **AAAA** : IPv6 Address record, which is used to map host names to their IPv6 address.
- **CAA** : Certificate Authority (CA) Authorization, which is used to specify which CAs are allowed to create certificates for a domain.
- **CNAME** : Canonical name record, which is used to specify alias names.
- **MX** : Mail exchange record, which is used in routing requests to mail servers.
- **NS** : Name server record, which delegates a DNS zone to an authoritative server.
- **SPF** : Sender Policy Framework record, a deprecated record type formerly used in e-mail validation systems (use a TXT record instead).
- **SRV** : Service locator record, which is used by some voice over IP, instant messaging protocols, and other applications.
- **TXT** : Text record, up to 255 characters. Can contain arbitrary text and can also be used to define machine-readable data, such as security or abuse prevention information.

### Add a new record

Section titled “Add a new record”
To add a new DNS record:

1. Go to your Netlify Team dashboard.
  - From your project dashboard, in the top left, choose **Projects** next to your project name.
2. From your project dashboard, in the top left, choose 

1. Select **DNS** from the left sidebar.

1. Select the domain (or DNS zone) you want to add a new DNS record for.
2. At the bottom of the **DNS records** section, select**Add new record** .
3. Choose the type of record to create from the menu and fill in the remaining options. The fields you need to fill out will depend on the type of record you select.
4. Select **Save** to create the record and make the changes live.

Remember, it may take up to a few hours for record changes to propagate.

Note that you can host records for other services, such as your mail provider or your backend API, with us as long as you host at least one website with us that uses the domain.

### Edit a record

Section titled “Edit a record”
To make DNS changes, you need to first add a new record with the new value and then delete the old record. DNS allows multiple entries for the same name and type, so you can avoid downtime by making changes this way.

### Delete a record

Section titled “Delete a record”
To delete a DNS record:

1. Go to your Netlify Team dashboard.
  - From your project dashboard, in the top left, choose **Projects** next to your project name.
2. From your project dashboard, in the top left, choose 

1. Select **DNS** from the left sidebar.

1. Select the domain (or DNS zone) you want to delete a DNS record for.
2. In the **DNS records** section, find the record you want to delete.
3. Select the record to expand the details and then select the delete option.
4. Review the warning message and select **Delete** to confirm.

Remember, it may take up to a few hours for record changes to propagate.

### API endpoints

Section titled “API endpoints”
You can use the API to get DNS records, create DNS records, and more.

##### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
