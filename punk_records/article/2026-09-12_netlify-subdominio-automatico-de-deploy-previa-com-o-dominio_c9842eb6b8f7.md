---
item_id: "94d2823e-bb98-498e-a611-de66156dafd2"
platform: article
external_id: "c9842eb6b8f7"
canonical_url: "https://docs.netlify.com/manage/domains/configure-domains/configure-an-automatic-subdomain-for-deploys"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: enriched
triage: null
tags: ["netlify", "deploy-preview", "subdominio-de-deploy", "branch-deploy", "aprovacao-de-cliente", "netlify-dns"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: alta
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Netlify — subdomínio automático de deploy: prévia com o domínio do cliente, não com netlify.app

🔗 https://docs.netlify.com/manage/domains/configure-domains/configure-an-automatic-subdomain-for-deploys

## Resumo

Recurso que troca a URL das prévias por um subdomínio próprio: em vez de deploy-preview-42--meusite.netlify.app, o link vira deploy-preview-42.empresa.com, e branch deploys viram staging.empresa.com. Vale para todos os Deploy Previews e/ou todos os branch deploys de uma vez, e passa a ser o padrão na interface, na API, na CLI e nas notificações de deploy. Os usos declarados são confiança ao compartilhar link com quem aprova, compatibilidade com serviços de terceiros que exigem domínio próprio em lista de permissão, e fluxos de autenticação que dependem de domínio fixo. O requisito é que o domínio esteja sob Netlify DNS e disponível para a equipe; subdomínios de um domínio já delegado entram automaticamente. As URLs antigas em netlify.app continuam funcionando em paralelo, e os deploy permalinks, que apontam para um deploy específico por ID, continuam sempre no domínio da Netlify.

## Tópicos

- **O que muda** — Todas as prévias e branch deploys passam a usar subdomínio próprio, inclusive na API, na CLI e nas notificações.
- **Por que importa** — Link de prévia com domínio da empresa passa confiança a quem aprova e funciona com serviços de terceiros que exigem domínio autorizado.
- **Requisito** — O domínio precisa estar sob Netlify DNS; subdomínios de domínio já delegado valem automaticamente.
- **O que não muda** — As URLs netlify.app continuam ativas, e deploy permalinks seguem sempre no domínio da Netlify.

## Ferramentas citadas

- **Netlify**: plataforma de hospedagem e DNS descrita no documento

## Pontos-chave

- Link de prévia com domínio próprio é argumento comercial: o cliente aprova num endereço com o nome dele.
- Exige Netlify DNS; não funciona com DNS externo.
- As URLs antigas continuam funcionando em paralelo, então não quebra nada.
- Deploy permalink nunca muda de domínio, porque aponta para um deploy específico.

## Como aplicar

Casa direto com o fluxo de aprovação: em vez de mandar ao cliente um link deploy-preview-42--jardinscafe.netlify.app, que parece rascunho, mandar preview.jardinscafe.com.br. Muda a percepção do que você entrega sem mudar uma linha de código. Só funciona com o domínio sob Netlify DNS.

## 📚 Pythagoras diz

Aqui está a versão cara da mesma ideia que já te dei de graça: o Deploy Preview aprova a mudança, e este recurso faz o link parecer profissional. Exige Netlify DNS, então é decisão que vem depois de escolher onde mora o domínio do cliente.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

With automatic deploy subdomains, you can set up automatically branded URLs for Deploy Previews or branch deploys — unifying your site’s preview environments, auth flows, third-party services, and other site versions with a shared custom domain.

Automatic deploy subdomains are a type of custom domain that you can set for all Deploy Previews or all branch deploys.

#### Use cases

Section titled “Use cases”
When you set up an automatic deploy subdomain for all of your Deploy Previews or branch deploys, you can:

- Share branded deploy URLs that don’t include the Netlify subdomain. For example, build greater trust with your stakeholders by sharing `deploy-preview-42.company.com` instead of`deploy-preview-42--mysitename.netlify.app` .
- Use third-party services the way you do for your production site, such as auth flow services that rely on a custom domain.
- Ensure deploys are “trusted” and in the “allowed domain list” for any third-party scripts or services that require this.
- Meet internal security requirements while leveraging Netlify’s Deploy Previews and branch deploys to preview and collaborate on changes before they go live.

Once you configure an automatic deploy subdomain, Netlify uses this custom domain for your Deploy Previews and/or branch deploys by default within the Netlify UI, the API, CLI, and deploy notifications.

#### Domain requirements

Section titled “Domain requirements”
The custom domain you set as your automatic deploy subdomain must be managed by Netlify DNS and available to your team.

By default, domains managed by Netlify DNS can be applied to your Deploy Previews or branch deploys.

For example, if you already delegated `company.com` to Netlify DNS, then subdomains of `company.com`, such as `early-access.company.com`, are also delegated to Netlify DNS by default. That means you can use `early-access.company.com` as your automatic deploy subdomain.

If you want to use a custom domain that Netlify DNS does not already manage, add the custom domain to your Netlify team and configure it to be managed by Netlify DNS. Learn more in these domain setup steps.

#### Example deploy URLs

Section titled “Example deploy URLs”
| Site deploys | Netlify subdomain | Automatic deploy subdomain | 
|---|---|---|
| Deploy Preview | `deploy-preview-42--mysitename.netlify.app` | `deploy-preview-42.company-internal-testing.com` | 
| Branch deploy, e.g. `staging` branch | `staging--mysitename.netlify.app` | `staging.company-internal-testing.com` | 
| Atomic deploy permalink | Uses the Netlify subdomain and a deploy ID, such as `1234abcd12acde000111cdef--mysitename.netlify.app` . | N/A | 

When you set an automatic deploy subdomain for all Deploy Previews or all branch deploys, your deploys are still accessible at the Netlify subdomain, such as `deploy-preview-42--mysitename.netlify.app` or `staging--mysitename.netlify.app`.

Your deploy permalinks, which offer unique URLs for successful deploys of your site, will continue to use the Netlify subdomain. Unlike other deploy URLs, deploy permalinks do not update with new Git commits. Instead, Netlify generates new deploy permalinks for each successful deploy of your site.

### Automatic deploy subdomains for Deploy Previews

Section titled “Automatic deploy subdomains for Deploy Previews”
Deploy Previews are automatically enabled for all sites using continuous integration with Netlify. If your site doesn’t have Netlify continuous integration set up, check out these docs.

#### Set an automatic deploy subdomain for Deploy Previews

Section titled “Set an automatic deploy subdomain for Deploy Previews”
To set up an automatic deploy subdomain for your site’s Deploy Previews:

1. 
Go to **Domain management  Automatic deploy subdomains** .
2. 
Select **Edit custom domains** .
3. 
Next to **Deploy Previews** , select**Add custom domain** .
4. 
Under **Domain** , you’ll find domains managed by Netlify DNS. Select your chosen custom domain. Optionally, enter an additional subdomain, such as`early-access` or`qa` .

1. Review the preview of the deploy URL for your Deploy Previews. To confirm,  select **Save** .

Once saved, Netlify updates the domain for all open Deploy Previews. If you applied a custom domain that is not already live as your primary site domain (or does not already have a security certificate), then your new deploy URL may take up to 24 hours to resolve and work with HTTPS.

### Automatic deploy subdomains for branch deploys

Section titled “Automatic deploy subdomains for branch deploys”
Branch deploys are often used for maintaining a separate version of your site for QA, internal testing, or even to manage different versions of site content for different audiences or product versions.

If you are already using branch subdomains, check out our branch subdomain comparison docs to understand the key differences between these subdomains and how they can work together.

If you set up an automatic deploy subdomain for branch deploys on your site, then each branch deploy will generate the same automatic deploy subdomain and include your branch deploy’s unique branch name.

#### Prerequisites

Section titled “Prerequisites”
To set up an automatic deploy subdomain for your site’s branch deploys, you must first enable branch deploys for your site.

1. To enable branch deploys for your site, go to **Project configuration  Build & deploy  Branches and deploy contexts** .
2. Select **Configure** .
3. Next to **Branch deploys** , set up branch deploys for a specific branch or for all non-production branches. To confirm, select**Save** .
4. Once branch deploys are enabled, create a new branch and push a commit to this branch in your connected site repo. Netlify will automatically generate a branch deploy, which you can preview in your site’s deploy list.

#### Set an automatic deploy subdomain for branch deploys

Section titled “Set an automatic deploy subdomain for branch deploys”
To set up an automatic deploy subdomain for your site’s branch deploys:

1. 
Go to **Domain management  Automatic deploy subdomains** .
2. 
Select **Edit custom domains** .
3. 
Next to **Branch deploys** , select**Add custom domain** .
4. 
Under **Domain** , you’ll find domains managed by Netlify DNS. Select your chosen custom domain. Optionally, enter an additional subdomain, such as`early-access` or`qa` .

1. Review the preview of the deploy URL for your branch deploys. To confirm,  select **Save** .

Once saved, Netlify updates the domain for all active branch deploys. If you applied a custom domain that is not already live as your primary site domain (or does not already have a security certificate), then your new deploy URL may take up to 24 hours to resolve and work with HTTPS.

#### Choose a unique URL for your branch deploys

Section titled “Choose a unique URL for your branch deploys”
It is possible to configure automatic subdomains for branch deploys so that a branch subdomain conflicts with another site’s production domain. Since Deploy Previews are appended with the pull/merge request number, their automatic subdomains are unlikely to conflict with other domains.

For example:

- Site A has a primary site domain of `staging.company.com` for the production site.
- Site B has an automated domain of `staging.company.com` for its`staging` branch.

When there is a conflict, domains listed in your **Production domains** settings will take precedence over other internal domains. So in this example, `staging.company.com` will resolve to the content of site A.

To prevent accidental domain duplication, you might choose to add another subdomain level to your branch subdomains that is not used in production, such as `internal` in `staging.internal.company.com`.

If you get a domain conflict, you can rename the branch. For example, you can rename the branch from `staging` to `qa`. Then, the next time you deploy this branch, it would use the `qa.company.com` domain.

#### Limitations for sites with existing branch subdomains

Section titled “Limitations for sites with existing branch subdomains”
Once you add an automatic deploy subdomain for branch deploys, you cannot edit or change existing manual branch subdomains. You also cannot manually add new branch subdomains, but existing branch subdomains will still work.

If you configured branch subdomains before enabling automatic deploy subdomains, both the branch subdomains and automatic deploy subdomains will resolve and be available. If both are set up, the Netlify UI, CLI, API, and deploy notifications will link to the automatic deploy subdomain by default.

To make changes to your branch subdomain, you must remove the automatic deploy subdomain first.

If you want to compare using branch subdomains with automatic deploy subdomains, check out our comparison docs for applying a custom domain to a branch deploy.

### Use a new custom domain for your automatic deploy subdomain

Section titled “Use a new custom domain for your automatic deploy subdomain”
By default, you can choose primary site domains that are also managed by Netlify DNS as your automatic deploy subdomain. You can also add additional subdomains to these domains, such as `early-access` or `qa`.

If you want to use a custom domain that is not listed in the Netlify UI, you must first delegate this domain to Netlify DNS.

To delegate an existing domain you own to Netlify DNS:

1. Go to your project dashboard, on the left, choose **Domain management** .
2. Under **Automatic deploy subdomains** , check**Add custom domain** .
3. Optionally, you can add a subdomain to your custom domain, such as `early-access` ,`internal` , or`docs` .
4. Under **Domain** , choose a custom domain or add a new custom domain with the option**Configure Netlify DNS for a custom domain** .
5. Enter new domain and confirm with **Set up with Netlify DNS** .
6. Point your domain's name servers to Netlify. To use Netlify DNS, go to your domain registrar and change your domain's name servers to the following custom hostnames assigned to your DNS zone.
7. Confirm with **I've done this, proceed** .
8. Select **Save** .

Your changes may need more time to take effect depending on your DNS updates. Some DNS updates can take up to 24 hours to take effect and some changes take even longer.

Once your changes take effect, your Deploy Preview or branch deploy URLs will automatically update to use the new domain and/or subdomain.

### Use the Netlify API to set automatic deploy subdomains

Section titled “Use the Netlify API to set automatic deploy subdomains”
You can set automatic deploy subdomains when you create a site using the Netlify API. In your `createSite` request, use the following query parameters to pass the values to use for the subdomains:

- `deploy_preview_custom_domain`
- `branch_deploy_custom_domain`

Note that when you create or update a site with an automatic deploy subdomain, the build environment variable `DEPLOY_PRIME_URL` will update for all relevant deploys. Learn more about `DEPLOY_PRIME_URL`.

### Custom certificate requirements

Section titled “Custom certificate requirements”
If you use a custom certificate for your site’s domains, that certificate must explicitly include any new subdomains used for automatic deploy subdomains. The standard wildcard syntax, such as `*.company.com`, does not cover this new subdomain.

For example, your custom certificate will not work as expected in this scenario:

- you have `early-access.company.com` as your automatic deploy subdomain, where`early-access` is the optional new subdomain you added in the Netlify UI
- you have a custom certificate with `*.company.com` as your wildcard domain but not`*.early-access.company.com`

In this scenario, you must update your certificate to include the domains `*.company.com, *.early-access.company.com` so that `early-access.company.com` will work as expected.

### Remove an automatic deploy subdomain

Section titled “Remove an automatic deploy subdomain”
To remove an automatic deploy subdomain from your Deploy Previews or branch deploys:

1. Go to **Domain management  Automatic deploy subdomains** .
2. Select **Edit custom domains** .
3. Next to **Branch deploys** or**Deploy Previews** , clear the**Add custom domain** checkbox.
4. To confirm,  select **Save** .

##### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
