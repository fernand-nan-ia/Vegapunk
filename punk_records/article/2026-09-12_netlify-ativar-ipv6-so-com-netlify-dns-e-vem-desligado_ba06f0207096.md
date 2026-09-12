---
item_id: "845bc892-0f78-4167-92ee-e7be73015642"
platform: article
external_id: "ba06f0207096"
canonical_url: "https://docs.netlify.com/manage/domains/configure-domains/enable-ipv6"
channel: "Netlify Docs"
captured_at: 2026-09-12
status: discarded
triage: discard
tags: ["ipv6", "netlify-dns", "configuracao-de-dominio"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: baixa
  estudo_geral: baixa
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Netlify — ativar IPv6 (só com Netlify DNS, e vem desligado)

🔗 https://docs.netlify.com/manage/domains/configure-domains/enable-ipv6

## Resumo

Documento curto sobre IPv6. O protocolo usa endereços de 128 bits contra os 32 do IPv4, suporta muito mais endereços e está gradualmente substituindo o antigo. Por padrão a Netlify NÃO habilita IPv6 nos sites, e só quem usa Netlify DNS pode ativá-lo, pelo painel: equipe, DNS na barra lateral, selecionar o domínio e Enable IPv6.

## Ferramentas citadas

- **Netlify**: plataforma de hospedagem e DNS descrita no documento

## Pontos-chave

- IPv6 é desligado por padrão em todos os sites.
- Ativar só é possível com Netlify DNS; DNS externo não tem essa opção.
- O caminho é DNS > selecionar o domínio > Enable IPv6.

## Como aplicar

Nada urgente para site de cafeteria. Fica como caixa a marcar no dia em que o domínio estiver sob Netlify DNS e alguém perguntar por IPv6.

## 📚 Pythagoras diz

Uma chave, duas condições: Netlify DNS e um clique. Não muda nada visível para o cliente, e eu registro só para não ficar lacuna.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

For the complete Netlify documentation index, see llms.txt. Markdown versions of any documentation page are available by appending `.md` to its URL.

Enable IPv6 for your site or app to use the newer IP protocol, which has a range of benefits over the older IPv4 protocol.

IPv6 is a newer protocol for how devices communicate over the internet. Among other differences, it uses a 128-bit address instead of the IPv4’s 32-bit address, supports more IP addresses, and is the process of replacing IPv4.

By default, IPv6 is not enabled on all Netlify sites and apps. If you use Netlify DNS, you can enable it explicitly in your Domains dashboard.

To enable IPv6 for your site or app:

1. Go to your Netlify Team dashboard.
  - From your project dashboard, in the top left, choose **Projects** next to your project name.
2. From your project dashboard, in the top left, choose 

1. Select **DNS** from the left sidebar.

1. Select the domain you want to enable IPv6 for and select **Enable IPv6** .

#### Did you find this doc useful?

Your feedback helps us improve our docs.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
