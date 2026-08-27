---
item_id: "df37af58-03d9-4b8c-abca-f9bed0627f72"
platform: tiktok
external_id: "7652116731359431954"
canonical_url: "https://www.tiktok.com/@gabmirandamkt/video/7652116731359431954"
channel: "gabmirandamkt"
captured_at: 2026-08-27
status: applied_saas
triage: apply_saas
tags: ["vibe-coding", "supabase-rls", "edge-functions", "env-leaks", "security-audit", "app-security", "claude-code"]
applicability:
  saas_pessoal: alta
  projeto_cliente: alta
  estudo_geral: media
confidence: media
theme: seguranca-e-privacidade
content_type: whisper
---

# Top 3 erros de segurança comuns no vibe coding

🔗 https://www.tiktok.com/@gabmirandamkt/video/7652116731359431954

## Resumo

O vídeo alerta sobre as três falhas de segurança mais recorrentes cometidas por quem desenvolve com ferramentas de IA. Entre os problemas críticos estão o esquecimento de políticas de segurança em bancos como Supabase, a exposição de rotas e Edge Functions sem autenticação, e o commit de arquivos .env com chaves secretas no GitHub. A ideia central é auditar e proteger essas camadas antes de colocar aplicações em produção.

## Tópicos

- **Falta de políticas de segurança no banco de dados (RLS)** — Deixar o Row Level Security (RLS) desativado no Supabase ou PostgreSQL permite que qualquer usuário acesse ou modifique tabelas diretamente via API pública.
- **Ausência de autenticação em rotas e Edge Functions** — Expor endpoints de backend e funções sem validação de sessão ou login permite abusos e execuções indevidas das funcionalidades do sistema.
- **Commit de arquivos .env com credenciais** — Subir o arquivo .env contendo chaves privadas para o GitHub expõe credenciais críticas a vazamentos e acessos não autorizados.

## Ferramentas citadas

- **Supabase**: Banco de dados/BaaS citado pelo risco de exposição via API quando políticas de segurança estão desativadas.
- **PostgreSQL**: Banco de dados relacional mencionado quanto à necessidade de configuração de controle de acesso.
- **Lovable**: Plataforma de vibe coding citada como exemplo de ferramenta que cria arquivos .env automaticamente ao linkar com GitHub.
- **GitHub**: Plataforma de repositórios citada pelo risco de vazamento de segredos em commits públicos ou comprometidos.
- **Claude Code**: Ferramenta de CLI citada como agente para auditar e detectar automaticamente essas três vulnerabilidades na base de código.

## Pontos-chave

- A API padrão do Supabase permite leitura e escrita irrestrita se as políticas de RLS não forem explicitamente ativadas.
- Edge Functions e rotas de API precisam de middlewares de autenticação para evitar uso não autorizado de recursos.
- Ferramentas de geração de código criam arquivos .env automaticamente, exigindo validação manual do .gitignore antes de enviar ao repositório remoto.

## Como aplicar

Solicitar ao Claude Code uma varredura nas regras de RLS do Supabase, auditar a proteção de rotas/Edge Functions e checar se nenhum segredo do .env está presente no histórico do Git tanto no SaaS quanto no projeto do cliente.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
