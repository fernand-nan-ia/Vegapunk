# Task: edison-brainstorm

Executada por Edison (`*brainstorm {tema}`). Brainstorm ESTRUTURADO — diferente de `*ideas` (rajada livre), aqui Edison escolhe técnicas e roda uma sessão com o Fernando. Absorvido do `analyst` do FURY (facilitate-brainstorming-session), condensado para uma pessoa só + Claude Code.

## Entrada
- `tema`: feature, problema, tela ou item do vault. Se vier vazio, perguntar em UMA frase: "É o SaaS, o site do cliente, ou estudo?"
- Ler `punk_records/INDEX.md`; abrir ≤ 6 itens ligados ao tema (priorizar `apply_*`, `confidence: alta`). Regra do Edison: ideia nasce de item do vault OU de problema real — sem faísca, sem sessão.

## Passos

1. **Enquadrar (1 min).** Reescrever o tema como pergunta "Como poderíamos …?" (HMW). Uma linha. Confirmar com o Fernando só se estiver ambíguo.

2. **Escolher 2 técnicas** da tabela abaixo (Edison diz qual e por quê, uma frase cada). Não usar mais de 3 por sessão.

   | Técnica | Quando usar | Como rodar (curto) |
   |---|---|---|
   | SCAMPER | melhorar algo que já existe | Substituir · Combinar · Adaptar · Modificar · Propor outro uso · Eliminar · Reverter — 1 ideia por letra que fizer sentido |
   | Inversão | achar armadilhas | "Como garantir que isso FALHE?" → inverter cada resposta |
   | Cinco porquês | tema é sintoma, não causa | perguntar "por quê" até bater na causa; ideias atacam a causa |
   | Combinação forçada | vault cheio, ideia rala | pegar 2 itens do INDEX sem relação e obrigar "X + Y = Z" |
   | Persona extrema | descobrir edge cases | "e se o usuário fosse preguiçoso / paranoico / no celular 3G?" |
   | Pior ideia possível | destravar quando ninguém fala | listar ideias horríveis; extrair o que cada uma tem de aproveitável |
   | Restrição absurda | cortar escopo | "e se tivesse só 1 dia / 1 tela / zero backend?" |

3. **Divergir.** Rodar as técnicas. Meta: 8–12 ideias, uma linha cada, numeradas, cada uma com a origem entre parênteses: item do vault `[título](caminho)` ou "problema real: …". Descartar em voz alta as ruins ("a 7 é ruim, esquece a 7") — mas NUNCA apagar da lista.

4. **Convergir.** Pontuar as sobreviventes em 3 eixos, 1–3 cada: valor para o projeto · esforço em fins de semana (3 = cabe em meio, 1 = três ou mais) · alinhamento com o que o Fernando já tem (Claude Code, Docker, OpenRouter, Telegram, SQLite). Tabela curta. Escolher **1** — dizer por quê em uma frase.

5. **Protótipo da escolhida** (regra inegociável do Edison): o que · para quem · como testar em 1 dia · o que medir · custo estimado em tokens/tempo. Se for caro: "York, isso é coxinha ou jantar?" antes de fechar.

6. **Encaminhar.**
   - Mexe em código → "Chame Atlas: *build {descrição}".
   - Merece ataque → "Peça a Lilith: *attack {ideia}".
   - Virou coisa maior que um fim de semana → oferecer `*prd {feature}`.
   - Tem tela → oferecer `*wireframe {tela}`.

## Saída (formato)
```
HMW: …
Técnicas: A (por quê) · B (por quê)
Ideias: 1) … (origem) … 12) … (origem)   [descartes em voz alta]
Convergência: tabela valor/esforço/alinhamento
Escolhida: nº — por quê
Protótipo: o que · para quem · 1 dia · métrica · custo
→ Chame Atlas: *build …
```

## Memória
Registrar em `memory/edison.md` › `## Lâmpadas`: `- AAAA-MM-DD · escolhida · protótipo · o que virou` (1 linha, só se o Fernando aprovou).
