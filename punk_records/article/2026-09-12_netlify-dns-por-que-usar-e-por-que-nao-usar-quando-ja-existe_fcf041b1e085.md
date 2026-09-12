---
item_id: "3aab8203-8c3d-4f4d-a793-0d8bd1492400"
platform: article
external_id: "fcf041b1e085"
canonical_url: "https://docs.netlify.com/manage/domains/why-netlify-dns"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: enriched
triage: null
tags: ["netlify-dns", "ssl-wildcard", "branch-deploy", "subdominio-autonomo", "dns-externo", "migracao-de-dns"]
applicability:
  saas_pessoal: media
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Netlify DNS — por que usar, e por que NÃO usar quando já existem muitos registros

🔗 https://docs.netlify.com/manage/domains/why-netlify-dns

## Resumo

Documento que compara DNS da Netlify com DNS externo. A favor do Netlify DNS: certificado SSL wildcard cobrindo automaticamente todos os subdomínios, inclusive um por branch do repositório; branch deploys servindo como ambiente de homologação permanente; subdomínios autônomos, permitindo delegar só docs.empresa.com sem trazer empresa.com; e subdomínios personalizados para URLs de prévia, trocando deploy-preview-42--meusite.netlify.app por deploy-preview-42.empresa.com, o que importa quando serviços de terceiros exigem domínio próprio em lista de permissão. Também garante que o CDN da Netlify sirva o domínio apex, e não só o www. Contra: a Netlify NÃO aceita transferência de zona DNS de entrada, então quem já tem muitos registros configurados terá de recriar tudo à mão, e nesse caso o próprio documento recomenda ficar no provedor externo.

## Tópicos

- **SSL wildcard automático** — Um certificado cobre todos os subdomínios, inclusive um por branch, provisionado com um clique.
- **Subdomínios autônomos** — Dá para delegar docs.empresa.com à Netlify mantendo empresa.com em outro provedor.
- **Prévia com domínio próprio** — Deploy Previews e branch deploys passam a usar subdomínio da empresa, o que resolve listas de permissão de serviços de terceiros e fluxos de autenticação.
- **O limite que decide contra** — Não existe importação de zona DNS: muitos registros existentes significam recriar tudo manualmente, e o documento recomenda o provedor externo nesse caso.

## Ferramentas citadas

- **Netlify**: plataforma de hospedagem e DNS descrita no documento

## Pontos-chave

- SSL wildcard automático é o maior ganho prático do Netlify DNS.
- Netlify DNS garante o CDN também no domínio apex, não só no www.
- Dá para delegar apenas um subdomínio, sem mover o domínio inteiro.
- Não há transferência de zona DNS de entrada: tudo é recriado à mão.
- A própria documentação recomenda DNS externo para quem já tem muitos registros.
- Prévia com domínio próprio importa quando serviços externos exigem domínio autorizado.

## Como aplicar

Para site novo de cliente, Netlify DNS é o caminho curto: SSL wildcard sozinho e nada para configurar. Para cliente que JÁ tem domínio com e-mail funcionando, pare e leia de novo: sem importação de zona, todo registro MX, TXT e SPF do e-mail dele teria que ser recriado à mão, e um erro ali derruba o e-mail da empresa. Nesse caso, DNS externo e só um registro apontando para a Netlify.

## 📚 Pythagoras diz

A linha que eu destaco é a que joga contra o próprio produto: não existe importação de zona. Se o café já usa o domínio para e-mail, migrar o DNS significa recriar MX e SPF na unha, e errar ali tira o e-mail do cliente do ar. Nesses casos, deduzo que o certo é não mexer no DNS dele.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

Netlify DNS offers advanced subdomain automation and deployment features and ensures that your site uses our CDN for the apex domain as well as subdomains like www.

### Netlify DNS domain support

Section titled “Netlify DNS domain support”
You can delegate many different types of domains to Netlify DNS, including apex domains or subdomains, which include stand-alone subdomains.

For example, you can delegate a subdomain to Netlify DNS without the need to bring your apex domain to Netlify DNS. So you can delegate just `docs.company.com` to Netlify without bringing over `company.com` too. Learn more about stand-alone subdomain support.

### Netlify DNS key benefits

Section titled “Netlify DNS key benefits”
Besides the convenience of managing your domains along with your site and app hosting, Netlify DNS offers the following benefits:

- 
**Wildcard SSL certificate:** If your repo has multiple branches all serving different content, you can have a subdomain for every single branch in your repo, and a wildcard SSL certificate will cover them all. This will happen automatically, with one click.
- 
**Branch deploys:** Netlify DNS allows you to set up branch deploys for each branch in your repo, which can serve as an ongoing staging environment for each branch or alternative version of your site.
- 
**Standalone subdomains:** Netlify DNS allows you to have standalone subdomains for each branch in your repo so you can delegate`docs.company.com` to Netlify DNS and keep`company.com` delegated to another DNS provider.
- 
**Custom subdomains for preview URLs (also called Automatic deploy subdomains):** Netlify DNS allows you to customize subdomains for all Deploy Previews and/or for all branch deploys so you can unify your site's URLs across all branches and share`deploy-preview-42.company.com` instead of`deploy-preview-42--mysitename.netlify.app` . This ensures deploys can be "trusted" and in the "allowed domain list" for any third-party scripts or services that require this. This also allows you to use third-party services the way you do for your production site, such as auth flow services that rely on a custom domain.

### External DNS key benefits

Section titled “External DNS key benefits”
Netlify does not allow inbound DNS zone transfers. If you have a lot of existing DNS records, it's simplest and safest to use an external DNS provider.

### Further learning

Section titled “Further learning”
##### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
