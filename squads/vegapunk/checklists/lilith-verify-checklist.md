# Checklist: lilith-verify-checklist

Usada em `tasks/lilith-verify-delivery.md`. Uma pergunta por dimensão é o mínimo; cada "não" ou "não sei" vira finding com Onde · Por quê · Como corrigir · Severidade. Adaptada ao contexto: Claude Code, Docker local, OpenRouter, SQLite, bot Telegram, site de cliente, SaaS pessoal.

## 1. Correção
- [ ] Faz o que a promessa diz, no caminho feliz? (rodei ou li — qual?)
- [ ] Os nomes batem com o comportamento (função `salvar` que também apaga = mentira no código)?
- [ ] Números, datas, fuso, encoding: certos?

## 2. Completude (o que FALTA)
- [ ] Tratamento de erro em toda chamada externa (TikTok, YouTube, OpenRouter, Telegram)?
- [ ] Validação na borda (o que chega do usuário / do scraper)?
- [ ] Caso vazio, caso duplicado, primeira execução com banco vazio?
- [ ] Migração para dados que JÁ existem em `data/vegapunk.db`?
- [ ] Como desfazer (rollback) se der errado?

## 3. Segurança
- [ ] Segredo (token Telegram, chave OpenRouter) fora do repositório e fora do `docker compose` versionado?
- [ ] Entrada do usuário chega a SQL/shell/prompt sem sanitizar?
- [ ] Site do cliente: formulário sem rate limit, sem validação de servidor, dado pessoal sem necessidade (LGPD)?
- [ ] SaaS: o usuário A consegue ver dado do usuário B?

## 4. Robustez
- [ ] Rede cai no meio: o que acontece com o registro pela metade?
- [ ] Container reinicia: retoma ou duplica?
- [ ] Retry tem limite? Backoff? Ou vira martelada na API até o 429?

## 5. Dados (SQLite)
- [ ] Chave única onde precisa (item duplicado do mesmo vídeo)?
- [ ] Transação envolve as escritas que precisam ser atômicas?
- [ ] Escrita concorrente (bot + skill lendo) — `database is locked` tratado?
- [ ] Backup: existe? Testado restaurar?

## 6. Custo
- [ ] Quantas chamadas de LLM por item? Qual modelo? Dá para estimar em reais/mês?
- [ ] Loop ou retry que pode multiplicar o custo sem teto?
- [ ] York já viu? Se não, chamar.

## 7. Dependências
- [ ] Depende de API privada ou scraping (vai quebrar; quando)?
- [ ] Fornecedor único sem plano B?
- [ ] Versões fixadas (`yt-dlp`, libs) ou "latest" que muda numa terça?

## 8. Testes
- [ ] Existe teste para o caminho feliz? Para o caminho de erro?
- [ ] Os testes rodam (`pytest` passou agora, não semana passada)?
- [ ] "Funciona na minha máquina" — rodou no container?

## 9. Docs / explicação
- [ ] O Fernando consegue explicar o que isso faz sem abrir o código? Se não, falta um parágrafo em nível dev júnior.
- [ ] Como rodar, como reverter, o que olhar quando quebrar (log, tabela)?

## 10. Quem usa
- [ ] Mensagem de erro que uma pessoa entende, não stack trace?
- [ ] Site do cliente: celular, lento, acessível (contraste, teclado)?
- [ ] O que acontece se clicar duas vezes / mandar duas vezes?

## Antes de fechar
- [ ] Contei findings: 10+? Se menos, olhei de novo uma vez e disse quantos sobraram.
- [ ] Cada finding tem Onde · Por quê · Como corrigir · Severidade.
- [ ] Citei item do vault se houver relação.
- [ ] Terminei com "Odeio admitir, mas…" + o que sobreviveu + UMA condição.
