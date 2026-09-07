---
item_id: "299d3fa5-c7fb-4263-957e-1fbb49ba8ca6"
platform: tiktok
external_id: "7680992910879264021"
canonical_url: "https://www.tiktok.com/@liviasimoes.ia/video/7680992910879264021"
channel: "liviasimoes.ia"
captured_at: 2026-09-07
status: applied_client
triage: apply_client
tags: ["security-headers", "csp", "hardening-web", "vibe-coding", "checklist-de-lancamento", "auditoria-externa"]
applicability:
  saas_pessoal: alta
  projeto_cliente: alta
  estudo_geral: media
confidence: alta
theme: seguranca-e-privacidade
content_type: whisper
---

# Checagem de cabeçalhos de segurança em site feito com IA (securityheaders.com)

🔗 https://www.tiktok.com/@liviasimoes.ia/video/7680992910879264021

## Resumo

Site recém-codado com IA costuma nascer sem cabeçalhos HTTP de segurança, e a autora trata isso como um item de checklist que se resolve em dois minutos. O procedimento é entrar em securityheaders.com, digitar a URL do projeto e receber uma nota de A a F. A expectativa dela é que a maioria dos sites vibe-codados não tire A na primeira medição. A correção proposta é tirar um print dos erros apontados pelo relatório, colar no chat com o agente de IA e deixar ele aplicar os cabeçalhos. O critério de aceite declarado é fechar em A ou A+, e não menos. É um teste externo, gratuito e objetivo sobre um site já publicado, que não exige acesso ao código para rodar.

## Ferramentas citadas

- **securityheaders.com**: scanner externo que audita cabeçalhos HTTP de segurança e devolve nota de A a F

## Pontos-chave

- Site gerado por IA normalmente sai sem cabeçalhos de segurança configurados
- A auditoria é externa e não precisa de acesso ao código: basta a URL pública
- Critério de aceite proposto: nota A ou A+, nada abaixo disso
- O conserto é delegável ao próprio agente, colando o relatório de erros no chat

## Como aplicar

Rodar securityheaders.com contra o site do cliente e contra o SaaS antes de qualquer entrega, e tratar a nota como gate de publicação. O relatório vira issue direto: Content-Security-Policy, HSTS, X-Frame-Options e Referrer-Policy são os que costumam faltar em app publicado por Vercel/Cloudflare sem configuração explícita.

## 📚 Pythagoras diz

O registro diz pouco, mas o pouco que diz é verificável: uma URL, uma nota, um critério de corte. Eu deduzo que o valor aqui não está na ferramenta e sim no hábito — medir o que foi publicado, não o que foi escrito. Anoto uma lacuna, com licença: a nota A não descreve a qualidade da política, apenas a presença do cabeçalho.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
