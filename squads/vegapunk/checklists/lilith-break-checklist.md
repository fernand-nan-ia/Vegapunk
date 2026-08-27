# Checklist: lilith-break-checklist

Usada em `tasks/lilith-break-feature.md` e `tasks/lilith-evidence.md`. Para cada passo do caminho feliz, passar por cada família. Marcar: **trata** · **ignora em silêncio** · **quebra com erro claro** · **quebra sem erro** (o pior; sempre CRÍTICO ou ALTO).

## Entrada hostil
- [ ] Vazia / nula / só espaços
- [ ] Enorme (texto de 50 páginas, vídeo de 3h, lista com 10 mil itens)
- [ ] Duplicada (mesma URL, mesmo ID, mesma mensagem reenviada pelo Telegram)
- [ ] Encoding: emoji, acento, RTL, caractere de controle
- [ ] Injeção: `'; DROP`, `$(rm)`, "ignore as instruções anteriores" dentro do conteúdo capturado
- [ ] Tipo errado: string onde esperava número, URL sem esquema, data impossível

## Tempo e concorrência
- [ ] Terceiro demora 60s: há timeout? O que acontece depois dele?
- [ ] Duas mensagens no mesmo segundo
- [ ] Reprocessar item que já está em processamento
- [ ] Relógio: fuso, virada de dia, horário de verão

## Estado
- [ ] Banco vazio (primeira execução)
- [ ] Registro já existe com status diferente
- [ ] Migração/escrita interrompida pela metade (kill no meio)
- [ ] Arquivo esperado sumiu (`_pending/`, cache do Whisper)
- [ ] Disco cheio / permissão negada no volume do Docker
- [ ] Container reiniciou entre passo 2 e passo 3

## Terceiro (TikTok, YouTube, OpenRouter, Telegram)
- [ ] Mudou o HTML/JSON de resposta
- [ ] 429 (cota) — retry com limite? Ou loop infinito caro?
- [ ] 401/403 (chave expirou, IP bloqueado)
- [ ] Resposta vazia com status 200
- [ ] Modelo do OpenRouter retornou JSON inválido / truncado
- [ ] `yt-dlp` desatualizado (causa nº 1 histórica)

## Custo
- [ ] Rodar 100× por engano custa quanto (tokens, minutos de Whisper)?
- [ ] Há teto (max retries, max itens por rodada)?

## Humano
- [ ] Fernando manda comando errado / meio comando
- [ ] Cliente do site clica duas vezes, volta com o botão do navegador, recarrega no meio do envio
- [ ] Usuário do SaaS faz o que nenhum usuário "normal" faria — porque um vai fazer

## O que deveria existir e não existe
- [ ] Teste automatizado para o caso que quebrou
- [ ] Log com contexto (ID do item, passo, erro) — legível às 2h da manhã
- [ ] Validação na borda, não no meio
- [ ] Mensagem de erro para humano
- [ ] Documento de "o que fazer quando quebrar"
