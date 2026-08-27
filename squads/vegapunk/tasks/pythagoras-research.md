# Task: pythagoras-research

Pesquisa externa com fontes, executada por Pythagoras (`*research {tema}`). Absorvida do FURY `content-researcher`, adaptada: nada de brand-guidelines nem handoff a estrategista; o resultado é um dossiê que Lilith ataca, Shaka julga e Stella usa para decidir.

## Entrada
- `{tema}` — pergunta de mercado, concorrente, tendência, ferramenta ou dado.
- Opcional: `--saas` | `--cliente` | `--geral` (define o filtro de aplicabilidade). Sem flag → perguntar uma vez, ou inferir do contexto e dizer que inferiu.
- Opcional: `--interno` (só vault, sem WebSearch/WebFetch).

## Regra de ouro
Duas colunas que nunca se misturam: **o que o Punk Records guarda** e **o que a web diz hoje**. Cada afirmação carrega origem e data. Sem fonte, não entra — vira lacuna.

## Passos
1. **Vault primeiro.** Rodar `consult-punk-records.md` para o tema. Registrar: quantos itens, quais convergem, quais divergem, confidence de cada um. Se vazio, escrever "não há registro" e seguir.
2. **Definir a pergunta de pesquisa.** Uma frase, respondível. Ex.: "quais ferramentas de X cobram menos de R$ 100/mês para 1 usuário". Se o pedido do Fernando for vago, propor 2–3 perguntas numeradas e pedir que escolha.
3. **Pesquisa externa** (WebSearch/WebFetch), máximo 6 consultas e 8 páginas abertas:
   - Priorizar: documentação oficial, página de preços, changelog, repositório, relatório com metodologia. Depois: artigos técnicos assinados. Por último: threads e vídeos (marcar como `confidence: baixa`).
   - Para cada fonte anotar: título, URL, data de publicação (ou "sem data"), o que ela afirma, em uma linha.
   - Concorrentes: coletar preço, público, diferencial declarado, limitações visíveis. Nunca inferir faturamento ou número de clientes sem fonte.
4. **Cruzar.** Montar a tabela de convergência: afirmação · fontes que sustentam · fontes que contradizem · registro do vault que toca no ponto. Divergência entre vault e web é o achado mais valioso — destacar.
5. **Lacunas.** Listar o que nenhuma fonte cobriu. Para cada lacuna, sugerir o que mandar ao bot ou onde procurar.
6. **Inferência marcada.** Fechar com no máximo 3 deduções, cada uma iniciada por "eu deduzo".
7. **Escrever** usando `templates/pythagoras-research-report.md`. Salvar em `docs/research/YYYY-MM-DD_{slug}.md` do projeto ativo se o Fernando pedir arquivo; caso contrário, responder no chat.
8. **Passar pelo checklist** `checklists/pythagoras-source-discipline.md`.
9. **Encaminhar.** Encerrar com: "Dossiê pronto. Lilith ataca com `*attack`; Shaka julga com `*judge`; se virar feature, Stella abre `*story`." Anotar em `memory/pythagoras.md › Lacunas` o que faltou, se houver.

## Não fazer
- Opinar sobre valor (Shaka) ou apontar furos da ideia (Lilith).
- Escrever copy, estratégia ou plano de marketing.
- Apresentar número sem URL e data ao lado.
- Citar página que não foi aberta.
