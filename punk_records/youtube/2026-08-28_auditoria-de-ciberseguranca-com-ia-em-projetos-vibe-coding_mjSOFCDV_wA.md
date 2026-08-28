---
item_id: "d3a4c68f-67b2-416c-bf1d-bb2eaaf14eb2"
platform: youtube
external_id: "mjSOFCDV_wA"
canonical_url: "https://www.youtube.com/watch?v=mjSOFCDV_wA"
channel: "mano deyvin"
captured_at: 2026-08-28
status: archived
triage: archive
tags: ["vibe-coding", "auditoria-seguranca", "claude", "idor", "supabase-rls", "appsec", "hardening"]
applicability:
  saas_pessoal: alta
  projeto_cliente: alta
  estudo_geral: alta
confidence: alta
theme: seguranca-e-privacidade
content_type: transcript
---

# Auditoria de Cibersegurança com IA em Projetos Vibe Coding

🔗 https://www.youtube.com/watch?v=mjSOFCDV_wA

## Resumo

O autor demonstra a execução de um prompt abrangente de auditoria de segurança via Claude em quatro projetos brasileiros de código aberto desenvolvidos com vibe coding. As análises revelaram vulnerabilidades graves e recorrentes, como validação de autorização puramente no cliente, falhas de IDOR, chaves de API expostas no bundle frontend, geração de OTP sem aleatoriedade criptográfica (Math.random) e brechas de RLS no Supabase. O vídeo enfatiza boas práticas de segurança defensiva e ética hacker, clonando e testando as aplicações apenas localmente para evitar violações de produção. Ao final, o relatório em PDF gerado pelo modelo é utilizado para abrir issues estruturadas no GitHub, reportando as falhas diretamente aos mantenedores de forma responsável.

## Tópicos

- **Ética e regras de auditoria em código aberto** — Reforça que a análise deve ocorrer em ambiente local e com licenças abertas, reportando problemas de endurecimento via issue pública e falhas críticas via canal privado.
- **Falhas em aplicações locais e móveis (Curió)** — Identificou ausência de defesa em profundidade, segredos expostos no cofre do servidor e risco de servir snapshots de dados na rede local sem autenticação forte.
- **Autorização decorativa e IDOR (Invest Pro VT)** — Detectou endpoints que confiam cegamente em parâmetros do corpo da requisição, CORS com wildcard em subdomínios da Vercel e ausência de verificação de propriedade por ID de objeto.
- **Vazamento de credenciais no bundle (WhatsApp Login)** — Verificação de OTP realizada no navegador com Math.random, credenciais da Meta e Evolution API embutidas no build do React e ausência de rate limiting.
- **Vulnerabilidades em arquitetura multi-tenant (Open BSBI)** — Políticas de Row Level Security (RLS) aplicadas por linha e não por coluna, permitindo leitura de segredos de terceiros e webhooks com privilégios excessivos.

## Ferramentas citadas

- **Claude**: LLM e CLI utilizada para executar o prompt de auditoria de código nos quatro terminais
- **Supabase**: Banco de dados backend citado na análise de falhas de Row Level Security (RLS)
- **GitHub Issues**: Plataforma utilizada para submeter os relatórios e reportar vulnerabilidades aos mantenedores

## Pontos-chave

- Aplicações desenvolvidas com vibe coding frequentemente sofrem de autorização decorativa, onde a interface simula proteção mas o backend não valida permissões reais.
- O uso de Math.random para tokens OTP e a inclusão de variáveis de ambiente secretas no bundle do frontend continuam sendo armadilhas comuns.
- No Supabase, o RLS protege linhas inteiras, mas tabelas com colunas sensíveis expostas exigem restrições adicionais ou views para evitar vazamento entre membros.
- Prompts estruturados de auditoria são eficazes para mapear caminhos de exploração e gerar documentação pronta para correção.

## Como aplicar

Execute uma bateria de prompts de auditoria focada em OWASP Top 10 e permissões de dados no SaaS pessoal e no site do cliente antes de qualquer deploy em produção. Verifique especificamente se tokens de terceiros não estão caindo no bundle do frontend e se todas as chamadas por ID validam o ID do usuário da sessão.

## 🧠 Stella diz

Kwahaha! Quasar! A inteligência artificial acelera o desenvolvimento a passos galácticos, Fernando, mas o 'vibe coding' sem inspeção rigorosa gera castelos de cartas prontos para desmoronar! Este experimento prova que confiar autorização ao navegador ou deixar tokens no bundle é um convite ao desastre. Devemos passar imediatamente um scanner desses em nossas próprias criações antes que o mundo exterior as examine!

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
