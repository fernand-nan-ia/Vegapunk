---
item_id: "6a00df4a-eef3-4c7a-8608-a0fb6c8f6663"
platform: article
external_id: "8ff27fbb138d"
canonical_url: "https://developers.cloudflare.com/workers/ci-cd"
channel: "Cloudflare Docs"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["cloudflare", "workers", "ci-cd", "deploy", "github"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: article
---

# Cloudflare Workers — CI/CD: Workers Builds (GitHub/GitLab) ou provedores externos; por que automatizar o deploy

🔗 https://developers.cloudflare.com/workers/ci-cd

## Resumo

CI/CD para Workers: usar o sistema integrado Workers Builds (conecta GitHub ou GitLab e faz deploy a cada push numa branch, com setup mínimo) ou um provedor externo (necessário para GitHub/GitLab self-hosted ou outros provedores). Motivos: elimina wrangler deploy manual, builds consistentes no mesmo SCM, ambiente uniforme, gestão simples das credenciais de produção. A página aponta para o llms.txt do Workers como índice completo da documentação.

## Tópicos

- **Opções** — Workers Builds integrado ou CI externo.
- **Por quê** — Sem deploy manual, builds consistentes, credenciais centralizadas.
- **Docs** — llms.txt do Workers para agentes.

## Pontos-chave

- Workers Builds é o caminho curto para GitHub.
- Credencial de produção sai da máquina do dev.

## Como aplicar

Ligar Workers Builds na branch main do SaaS; a Stella continua sendo quem faz push.

## 🔧 Atlas diz

Push na main → deploy. Isso casa com a nossa regra: a Stella dá o push, a Cloudflare faz o deploy, ninguém roda wrangler deploy da própria máquina com chave de produção.

## Texto integral

<!-- extraído da fonte; artigos e documentos são guardados por inteiro (títulos rebaixados um nível) -->

Documentation Index Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt Use this file to discover all available pages before exploring further.

You can set up continuous integration and continuous deployment (CI/CD) for your Workers by using either the integrated build system, Workers Builds, or using external providers to optimize your development workflow.

Why use CI/CD?

Using a CI/CD pipeline to deploy your Workers is a best practice because it:

Automates the build and deployment process, removing the need for manual wrangler deploy commands.

Ensures consistent builds and deployments across your team by using the same source control management (SCM) system.

Reduces variability and errors by deploying in a uniform environment.

Simplifies managing access to production credentials.

Which CI/CD should I use?

Choose Workers Builds if you want a fully integrated solution within Cloudflare's ecosystem that requires minimal setup and configuration for GitHub or GitLab users.

You have a self-hosted instance of GitHub or GitLabs, which is currently not supported in Workers Builds' Git integration

You are using a Git provider that is not GitHub or GitLab

Workers Builds

Workers Builds is Cloudflare's native CI/CD system that allows you to integrate with GitHub or GitLab to automatically deploy changes with each new push to a selected branch (e.g. main).

Ready to streamline your Workers deployments? Get started with Workers Builds.

External CI/CD

You can also choose to set up your CI/CD pipeline with an external provider.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
