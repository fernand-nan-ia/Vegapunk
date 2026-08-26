---
item_id: "cd01058f-338f-4651-b962-7a16a0c297c7"
platform: tiktok
external_id: "7661231446069103880"
canonical_url: "https://www.tiktok.com/@gus_.ai/video/7661231446069103880"
channel: "Gus AI"
captured_at: 2026-08-26
status: enriched
triage: null
tags: ["job-automation", "claude", "cli-tools", "resume-parser", "interview-prep", "web-scraping"]
applicability:
  saas_pessoal: baixa
  projeto_cliente: nenhuma
  estudo_geral: media
confidence: alta
content_type: whisper
---

# Automação de busca de emprego e preparação com Claude e AI Job Search

🔗 https://www.tiktok.com/@gus_.ai/video/7661231446069103880

## Resumo

O vídeo demonstra como utilizar o repositório AI Job Search em conjunto com o Claude para automatizar o processo de recolocação profissional. A ferramenta processa dados exportados do LinkedIn, realiza scraping de vagas, analisa compatibilidade de perfil e cria materiais personalizados de aplicação. Além disso, o sistema inclui um módulo de simulação para preparação de entrevistas técnicas.

## Tópicos

- **Setup e estruturação do currículo** — Instalação do repositório AI Job Search e importação do perfil exportado do LinkedIn para que a IA estruture a base de dados profissional.
- **Scraping e pontuação de vagas** — Uso do comando /scrape para buscar dezenas de vagas em plataformas e categorizá-las por compatibilidade (alta, média ou baixa).
- **Aplicação customizada** — Execução do comando /apply para cruzar os requisitos da vaga com o perfil e redigir materiais contextualizados à visão da empresa.
- **Simulação de entrevista técnica** — Uso do comando /interview para simular perguntas da vaga e mapear lacunas técnicas que o candidato precisa estudar.

## Ferramentas citadas

- **AI Job Search**: Repositório/CLI para automação de busca de empregos, triagem de vagas e preparação para entrevistas
- **Claude**: Assistente de IA executando o pipeline de parsing de currículo, análise de vagas e simulação de entrevista
- **LinkedIn**: Plataforma de onde o perfil profissional é exportado para servir de base documental

## Pontos-chave

- A ferramenta utiliza comandos CLI com slash commands (/scrape, /apply, /interview) para orquestrar o fluxo de recolocação.
- A análise de aplicação busca dados contextuais da empresa para evitar cartas de apresentação genéricas.
- O avaliador de compatibilidade aponta com precisão o que está ausente no perfil do candidato sem alucinar ou mentir qualificações.
- O módulo de entrevista técnica orienta pontos de estudo com base nas discrepâncias entre o currículo e os requisitos da vaga.

## Como aplicar

A estrutura de slash commands e o pipeline de matching entre documentos (perfil vs. requisitos) podem ser estudados como arquitetura de agentes ou features de triagem dentro do SaaS.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
