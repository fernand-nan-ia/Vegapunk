# Task: consult-punk-records

Consulta ao vault com fontes. Executada por Pythagoras (`*recall`) ou pelo Stella quando a pergunta é simples.

1. Ler `punk_records/INDEX.md` inteiro. Vazio → "não há registro" + o que mandar ao bot.
2. Selecionar candidatos por tags, título e aplicabilidade vs. pergunta e projeto (SaaS → `saas_pessoal`; cliente → `projeto_cliente`). `discard` peso baixo; `_pending/` ignorado salvo pedido.
3. Ler até 8 `.md` (priorizar `confidence: alta`, triagem `apply_*`). `## Notas manuais` > resumo automático.
4. Responder com cada item citado como `[título](caminho)`. Separar "o registro diz" de "eu deduzo". `confidence: baixa` sinalizado.
5. Se a pergunta pede aplicação → encaminhar a Edison (`*apply`) ou Atlas (`*build`).
