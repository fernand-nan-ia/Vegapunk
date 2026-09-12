---
item_id: "309a16dd-3e70-4126-a7f5-4827398385a8"
platform: article
external_id: "16dbdfda644f"
canonical_url: "https://docs.netlify.com/manage/domains/set-up-netlify-dns"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: enriched
triage: null
tags: ["netlify-dns", "delegacao-de-dominio", "name-servers", "migracao-de-dns", "registrador"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: alta
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Netlify — ativar o Netlify DNS: pelo site já configurado ou delegando name servers

🔗 https://docs.netlify.com/manage/domains/set-up-netlify-dns

## Resumo

Procedimento para ligar o Netlify DNS em domínio novo ou já existente. Para domínio já atribuído ao site, o caminho é o painel do site, domain management, Options ao lado do domínio e Set up Netlify DNS. Para domínio registrado em outro provedor, o processo é delegação: copiar antes os registros DNS existentes do provedor atual e depois trocar, no registrador, os name servers autoritativos pelos da Netlify — passo cujo procedimento varia por registrador, com a documentação citando GoDaddy, Google Domains, AWS, Name.com e Hover. Os benefícios citados repetem os do documento de comparação: subdomínios autônomos, branch deploys e certificado wildcard, além de garantir o CDN também no apex.

## Tópicos

- **Domínio já no site** — Domain management, Options ao lado do domínio, Set up Netlify DNS e seguir os avisos.
- **Domínio registrado fora** — Copiar os registros DNS atuais, depois trocar os name servers no registrador pelos da Netlify.

## Ferramentas citadas

- **Netlify**: plataforma de hospedagem e DNS descrita no documento

## Pontos-chave

- Copiar os registros existentes ANTES de trocar os name servers é o passo que evita perder e-mail e serviços.
- A troca de name servers é feita no registrador, não na Netlify.
- O procedimento varia por registrador; a doc cita GoDaddy, Google Domains, AWS, Name.com e Hover.

## Como aplicar

Se for delegar o domínio de um cliente, copie a zona inteira ANTES — print, exportação, o que der — porque a Netlify não importa nada e o que você esquecer simplesmente para de existir. Em cliente com e-mail no domínio, isso é a diferença entre uma migração limpa e um telefonema no sábado.

## 📚 Pythagoras diz

O registro diz para copiar os registros existentes antes de trocar os name servers, e essa frase é a única que importa aqui. Quem troca primeiro e copia depois descobre o que esqueceu pelo cliente reclamando que o e-mail parou.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

Set up Netlify DNS for your new or existing domain.

Netlify DNS offers you advanced subdomain automation and deployment features, such as:

- standalone subdomains, such as `docs.company.com` without delegating`company.com`
- branch deploys, such as deploying the `staging` branch of your site/app
- a wildcard SSL certification for all your deploys

Netlify DNS also ensures that your site uses our CDN for the apex domain as well as subdomains like www. Learn more in Why Netlify DNS.

### Enable Netlify DNS

Section titled “Enable Netlify DNS”
There are several pathways to enabling Netlify DNS.

#### For a domain already added to your site

Section titled “For a domain already added to your site”
If you already assigned a production domain to your site, to set up Netlify DNS:

1. 
Go to your site’s dashboard, then select **domain management** from the left sidebar.
2. 
Next to your domain, select **Options** , then**Set up Netlify DNS** .
3. 
Follow the prompts to finish setting up Netlify DNS.

#### For a domain you already registered

Section titled “For a domain you already registered”
If your domain is registered with another provider, you can still take advantage of Netlify’s managed DNS service by delegating your domain to Netlify.

##### Delegate to Netlify

Section titled “Delegate to Netlify”
Assuming you have copied existing DNS records from your current provider, the final step to making your DNS records live is to update your domain registrar with the name servers that will be authoritative for your domain.

The process for changing your domain’s name servers varies from registrar to registrar. Check your domain registrar’s documentation for updating name servers. For your convenience, we’ve gathered links to instructions for popular registrars GoDaddy, Google Domains, AWS, Name.com, and Hover.

To delegate your domain to Netlify:

1. Go to your Netlify Team dashboard.
  - From your project dashboard, in the top left, choose **Projects** next to your project name.
2. From your project dashboard, in the top left, choose 

1. Select **DNS** from the left sidebar.

1. Select your domain.
2. Make note of the four name servers listed in the **Name servers** panel.
3. Log in to the account you have with your domain registrar and find their instructions for updating name servers.
4. Replace the name servers with the name servers for your Netlify DNS zone. If your registrar requires name server IP addresses, visit our Forums for a verified Support Guide on finding the IP addresses for Netlify’s name servers.

It may take up to a day for the changes to propagate to the public internet.

#### For a new domain you need to buy and register

Section titled “For a new domain you need to buy and register”
Check out our instructions to register and buy a domain from Netlify.

##### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
