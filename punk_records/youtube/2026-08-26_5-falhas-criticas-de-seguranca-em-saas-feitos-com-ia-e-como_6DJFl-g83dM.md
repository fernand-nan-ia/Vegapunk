---
item_id: "5ba32402-11ee-4147-8af9-79229d8b03dc"
platform: youtube
external_id: "6DJFl-g83dM"
canonical_url: "https://www.youtube.com/watch?v=6DJFl-g83dM"
channel: "mano deyvin"
captured_at: 2026-08-26
status: applied_saas
triage: apply_saas
tags: ["seguranca-saas", "vibe-coding", "claude-code", "supabase-rls", "idor", "xss", "gitleaks", "owasp-zap"]
applicability:
  saas_pessoal: alta
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
theme: seguranca-e-privacidade
content_type: transcript
---

# 5 Falhas Críticas de Segurança em SaaS Feitos com IA e Como Auditá-los

🔗 https://www.youtube.com/watch?v=6DJFl-g83dM

## Resumo

O vídeo alerta desenvolvedores que utilizam IA (Vibe Coding/Claude Code) sobre cinco vulnerabilidades críticas que costumam passar despercebidas em aplicações geradas automaticamente. Entre as falhas abordadas estão banco de dados com Row Level Security (RLS) desligado por padrão, validação de permissões administrativas delegada exclusivamente ao frontend, e vulnerabilidades de IDOR ao consultar registros sequenciais sem verificar a titularidade do usuário logado. Também destaca o perigo de expor chaves de API no bundle do cliente e a ausência de sanitização de inputs (XSS). Por fim, apresenta ferramentas gratuitas e instruções para usar o próprio Claude Code para auditar e corrigir essas brechas de segurança de forma direcionada.

## Pontos-chave

- Bancos BaaS como Supabase/Firebase frequentemente vêm com RLS desativado por padrão, expondo dados diretamente no frontend.
- Regras de negócio e autorização (como checagem de admin) nunca devem depender do frontend ou LocalStorage, pois são facilmente manipuláveis no navegador.
- Falhas de IDOR ocorrem quando rotas buscam registros por ID sequencial sem validar no backend se o recurso pertence ao usuário autenticado.
- Segredos e chaves de API nunca devem ser hardcoded nem incluídos em bundles de frontend, pois tornam-se públicos após o build.
- Todo input de usuário deve ser tratado como hostil, aplicando validação e sanitização para prevenir injeções de código (XSS).
- Para auditar vulnerabilidades com Claude Code, use prompts específicos listando essas 5 falhas ou integre ferramentas como Gitleaks e OWASP ZAP.

## Como aplicar

Executar uma varredura com o Claude Code no SaaS pessoal e no site do cliente para auditar RLS no banco de dados, sanitização de inputs e verificar se todas as checagens de autorização e chaves de API residem estritamente no backend. Adicionar Gitleaks ao pipeline de versionamento para garantir que segredos não vazem no histórico do Git.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
