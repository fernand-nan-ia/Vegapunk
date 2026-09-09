---
item_id: "3c3bdcb7-63bd-4017-82e3-4937920afd4c"
platform: tiktok
external_id: "7682949171111922964"
canonical_url: "https://www.tiktok.com/@isnaldo.dev/photo/7682949171111922964"
channel: "Isnaldo.dev"
captured_at: 2026-09-09
status: enriched
triage: null
tags: ["seguranca-de-aplicacao", "idor", "rate-limiting", "chave-exposta", "validacao-no-servidor", "bucket-privado", "vibe-coding", "checklist-pre-lancamento"]
applicability:
  saas_pessoal: alta
  projeto_cliente: media
  estudo_geral: alta
confidence: alta
theme: seguranca-e-privacidade
content_type: slides
---

# 5 testes de segurança em app feito com IA, sem escrever código

🔗 https://www.tiktok.com/@isnaldo.dev/photo/7682949171111922964

## Resumo

O carrossel propõe cinco testes que qualquer pessoa faz em dez minutos com o navegador aberto, para descobrir falhas comuns em aplicações geradas por IA. O primeiro é trocar o número na URL de um recurso que é seu (pedido, perfil, fatura) e ver se aparece o dado de outra pessoa — o conserto é buscar todo dado junto com o dono, com `where('user_id', auth()->id())` ou RLS ligado em toda tabela no Supabase. O segundo é errar a senha vinte vezes seguidas: se a vigésima resposta é igual à primeira, um robô faz dezenas de milhares de tentativas por minuto, e a correção é limite por IP e por conta no login. O terceiro é abrir o F12 e procurar por 'sk-', 'secret' e 'key', porque tudo que está no front é público — chave exposta se troca hoje, e a chamada à OpenAI passa a sair do servidor. O quarto é editar preço e quantidade pelo inspetor e tentar comprar: se o pedido é criado por um centavo ou com quantidade negativa, o app só valida na tela, e a regra é o cliente mandar o ID do produto enquanto o preço vem do banco. O quinto é copiar o link de um arquivo enviado e abrir em aba anônima; se abrir, todo arquivo de todo cliente está público, e a correção é bucket privado com link assinado. O autor diz que os dois que mais reprovam nas auditorias dele são o número na URL e o preço pelo F12, que 3 de 5 é a média que ele encontra, e alerta que passar nos cinco não significa seguro — faltam backup, deploy, dependências e LGPD. O post termina como isca comercial para o serviço de auditoria dele.

## Tópicos

- **IDOR pela URL** — Trocar o número do recurso na URL e ver dado alheio; corrigir buscando sempre com o dono na consulta ou com RLS.
- **Sem rate limit no login** — Vinte senhas erradas sem bloqueio nem atraso permitem força bruta; limitar por IP e por conta.
- **Segredo no front-end** — Chave de OpenAI ou Stripe visível no bundle; segredo só no servidor e rotação imediata da chave exposta.
- **Preço confiado ao cliente** — Editar preço e quantidade pelo inspetor e o pedido ser aceito; o servidor revalida e o preço vem do banco.
- **Arquivo público por link** — Link de upload abre em aba anônima; bucket privado mais link assinado com validade.
- **O que os 5 testes não cobrem** — Passar nos cinco não é 'seguro': ficam de fora backup, deploy, dependências e LGPD.

## Ferramentas citadas

- **Supabase**: citado pelo RLS por tabela como correção do teste 1 e por link assinado no teste 5
- **Laravel**: exemplo de rate limit com `throttle:5,1` na rota
- **express-rate-limit**: equivalente em Node para limitar tentativas de login
- **DevTools do navegador (F12)**: ferramenta única exigida pelos testes 3 e 4
- **Amazon S3 / DigitalOcean Spaces**: citados como armazenamento com bucket privado e link assinado

## Pontos-chave

- Os cinco testes exigem só o app aberto e o navegador — nenhum código.
- Teste 1: trocar o número na URL; se aparecer dado de outro usuário, reprovou.
- Teste 2: 20 senhas erradas sem bloqueio nem atraso = força bruta liberada.
- Teste 3: procurar 'sk-', 'secret' e 'key' nas Sources do F12; tudo no front é público.
- Teste 4: editar preço e quantidade no inspetor; o servidor nunca deve receber preço do navegador.
- Teste 5: link de arquivo que abre em aba anônima significa bucket público.
- Segundo o autor, 3 de 5 é a média nas auditorias dele; os campeões de reprovação são a URL e o preço.
- Passar nos cinco não cobre backup, deploy, dependências nem LGPD.
- O post é isca para o serviço pago de auditoria do autor.

## Como aplicar

Vira checklist de dez minutos antes de publicar qualquer coisa gerada com Claude Code. Nos dois primeiros clientes de Fernando (landing sem formulário, só botão wa.me) só os testes 3 e 5 se aplicam de fato — não há login, pedido nem upload. Para o SaaS pessoal, os cinco valem inteiros e o teste 1 (dado buscado junto com o dono / RLS) é o mais caro de descobrir tarde.

## 🪖 Shaka diz

Isso é checklist, não anúncio — apesar de terminar em anúncio. Os cinco testes são verificáveis, o fix de cada um é específico e o autor delimita o próprio escopo ao dizer que passar nos cinco não é ser seguro. Guarde e rode antes de publicar; na landing sem formulário só dois se aplicam, mas no dia em que houver login ou upload, os cinco passam a ser obrigatórios.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
