# Task: stella-story

Executada por Stella (`*story`). Absorvida de `sm` (Scrum Master). Stella prepara; Atlas constrói. Stella NUNCA implementa nem toca em código nesta task.

## Entrada
Um pedido do Fernando ("quero que o bot faça X", um item do vault com `## Como aplicar`, uma ideia de Edison) e o projeto-alvo: **Vegapunk** (este repo), **SaaS pessoal** ou **site do cliente**.

## Saída
`squads/vegapunk/stories/YYYY-MM-DD-<slug>.md` (criar pasta se não existir). Uma story = uma sessão de Atlas (≤ 2 h). Se não cabe, dividir em 2–3 stories numeradas e entregar só a primeira como "pronta".

## Template da story
```
# Story: <título curto>
**Projeto:** vegapunk | saas | cliente     **Status:** pronta | em andamento | revisão | feita
**Origem:** [título](caminho no vault) ou "pedido do Fernando em YYYY-MM-DD"

## Objetivo (1 frase, valor para o Fernando)
## Contexto que Atlas precisa (≤ 8 linhas: arquivos envolvidos, decisões fechadas do HANDOFF que se aplicam, armadilhas conhecidas)
## Critérios de aceite (checkboxes verificáveis, 3–6)
- [ ] ...
## Fora de escopo (o que NÃO fazer — evita o Atlas sair construindo)
## Riscos / Shaka (dado de usuário? segredo? custo em tokens? → o que Shaka já disse ou precisa dizer)
## Testes esperados (nome do arquivo/teste ou "manual: passos")
## Como desfazer (1–2 linhas)
## Handoff → Atlas: `*develop <este arquivo>` (ou `*build` se develop não existir)
```

## Passos
1. Entender o pedido em uma frase; se vago, fazer no máximo 2 perguntas.
2. Ler as fontes: item do vault (se houver), `HANDOFF.md` (decisões fechadas + armadilhas), mapa do código do projeto-alvo (`CLAUDE.md` ou `src/`).
3. Se envolver dado de usuário, `.env`, permissões ou dinheiro: acordar Shaka (`*risk`) ANTES de escrever a story e colar o veredito na seção Riscos.
4. Escrever a story pelo template. Critérios de aceite têm que ser testáveis por alguém que não escreveu o código.
5. Rodar `checklists/stella-story-checklist.md`. Só marcar `Status: pronta` com tudo ✓.
6. Entregar: caminho da story + uma frase para o Fernando ("Atlas, quando você quiser: `*develop …`"). Ciclo esperado: Atlas `develop` → Lilith `verify` → Shaka `gate` → Stella `release`.

## Regras
- Linguagem para dev júnior: sem jargão sem explicação; código só se for a interface que Atlas deve respeitar.
- Sem Epics, sprints, story points ou ADE — é um homem só com uma cabeça grande.
- Não editar stories que Atlas já marcou "em andamento"; criar uma nova.

## Quem entra em cada fase (para Stella saber quem acordar)
| Fase | Satélite | Comando | Stella faz |
|---|---|---|---|
| origem | Pythagoras / Edison | `*recall` / `*apply` | pega o item ou a ideia |
| risco | Shaka | `*risk` | cola o veredito na story |
| construção | Atlas | `*develop <story>` | entrega e sai da frente |
| ataque | Lilith | `*verify` | agenda depois de Atlas dizer "feito" |
| carimbo | Shaka | `*gate` | espera PASS / WAIVED / CONCERNS aceito |
| release | Stella | `*release` | prepara; Fernando dá o "push" |

## Exemplo mínimo (SaaS pessoal)
```
# Story: Auditoria de segredos antes do deploy
**Projeto:** saas   **Status:** pronta
**Origem:** [5 Falhas Críticas de Segurança em SaaS Feitos com IA](youtube/2026-08-26_5-falhas-criticas-de-seguranca-em-saas-feitos-com-ia-e-como_6DJFl-g83dM.md)
## Objetivo
Impedir que uma chave de API suba para o GitHub do SaaS sem ninguém perceber.
## Contexto que Atlas precisa
Repo do SaaS usa Supabase; já houve vazamento de token no Vegapunk (histórico reescrito). Sem CI hoje.
## Critérios de aceite
- [ ] `scripts/audit.sh` retorna código ≠ 0 se encontrar padrão de chave fora de `.env`
- [ ] Teste que planta uma chave falsa e confirma que o script falha
- [ ] README do SaaS explica em 3 linhas quando rodar
## Fora de escopo
Não configurar GitHub Actions; não tocar em RLS (story separada).
## Riscos / Shaka
Shaka `*risk` 2026-08-26: baixo; ressalva — não gravar a chave falsa do teste em arquivo rastreado.
## Testes esperados
`tests/test_audit.sh` (bash) ou manual: rodar com `.env` limpo → 0; com chave em `x.py` → 1.
## Como desfazer
Apagar `scripts/audit.sh` e o teste; nada mais é tocado.
## Handoff → Atlas: `*develop squads/vegapunk/stories/2026-08-26-audit-segredos.md`
```
