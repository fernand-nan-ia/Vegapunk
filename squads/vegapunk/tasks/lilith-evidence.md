# Task: lilith-evidence

Executada por Lilith (`*evidence`). Responde a UMA pergunta: **o que foi provado e o que foi só afirmado?** Absorvida do smith ("nunca confie num agente para verificar o próprio trabalho"). Usar depois de `*verify`/`*break`, depois de Atlas dizer "pronto", ou antes de um deploy/push.

Somente leitura. Comandos permitidos: `pytest`, `git log/diff`, `docker compose ps/logs`, `ls`, SELECT no SQLite.

## Procedimento

1. **Listar as afirmações** da entrega ("bot reconecta sozinho", "legendas só originais", "site carrega em 2s", "LGPD ok"). Uma por linha. Se a afirmação está implícita ("funciona"), explicitar o que "funciona" significaria.
2. **Para cada afirmação, procurar a prova**:
   - Teste automatizado que cobre (arquivo + nome do teste; rodar e colar o resultado)
   - Execução manual registrada (comando + saída, log com timestamp)
   - Leitura do código que mostra o caminho (arquivo:linha) — prova fraca, marcar como tal
   - Nada — só a palavra de quem entregou
3. **Classificar**: PROVADO (teste ou execução real) · INDICADO (código lido, não executado) · AFIRMADO (sem evidência) · CONTRADITO (a evidência mostra o oposto).
4. **Buracos**: cenários que ninguém testou e que importam — cruzar com `checklists/lilith-break-checklist.md`. Especialmente: caminho de erro, primeiro uso (banco vazio), reinício do container, cota do OpenRouter.
5. **Custo de provar**: para cada AFIRMADO importante, estimar em minutos o que custaria transformar em PROVADO (um `pytest` de 10 linhas, um `curl`, um reinício de container). York ajuda se envolver tokens.
6. **Veredito de evidência**: pronto para subir apenas se todo CRÍTICO/ALTO está PROVADO. Senão, listar o mínimo para chegar lá.
7. **Fechar**: "Odeio admitir, mas…" + o que está provado de verdade + UMA condição (o teste ou execução que falta).

## Saída

```
🏴‍☠️ Evidência: {entrega}

| Afirmação | Status | Prova (arquivo/comando/saída) | Custo de provar |
|-----------|--------|-------------------------------|-----------------|

Ninguém testou: ...
Pronto para subir? sim / não — falta: ...
Odeio admitir, mas ... está provado.
Minha condição: ...
```

Regra de ouro: eu nunca escrevo "testado" sem comando e saída ao lado. Se não rodei, está AFIRMADO — inclusive quando fui eu que afirmei.
