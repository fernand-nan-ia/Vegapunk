# Checklist: edison-prd

Edison roda antes de entregar um PRD (`*prd`). Item ✗ → corrigir ou justificar em uma linha. Ideia grande demais é a que falha em 4 ou mais.

## Problema e objetivo
- [ ] Problema em uma frase com {quem}/{o quê}/{por quê}
- [ ] Objetivo tem número (de A para B) ou público mensurável
- [ ] Evidência citada: item do vault `[título](caminho)`, dado real ou fala do Fernando/cliente — nada "porque é padrão"

## Escopo
- [ ] MoSCoW preenchido; **Won't** não está vazio
- [ ] ≤ 12 itens no total
- [ ] Conjunto **Must** cabe em ≤ 2 fins de semana (senão: cortar ou dividir em 2 PRDs)
- [ ] Brownfield: cita o que JÁ existe no código e não propõe de novo

## Histórias e aceite
- [ ] 3–6 histórias no formato "Como / quero / para"
- [ ] Cada história com 2–4 critérios de aceite verificáveis (Atlas consegue dizer "pronto" ou "não")
- [ ] Nenhum critério usa "rápido", "bonito", "intuitivo" sem número ou exemplo

## Telas, técnica, métricas
- [ ] Telas listadas com 1 linha cada; as que precisam desenho apontam para `*wireframe`
- [ ] Restrições técnicas refletem o que o Fernando já tem (Claude Code, Docker local, OpenRouter, SQLite, Telegram, host do cliente)
- [ ] LGPD/dados pessoais considerados se a feature toca usuário (item do vault citado se existir)
- [ ] 1 métrica principal com "como medir"

## Risco e custo
- [ ] ≤ 5 riscos, cada um com mitigação; os que Lilith deve atacar estão marcados
- [ ] Custo em fins de semana por bloco Must; se > 2, resposta da York registrada ("coxinha ou jantar?")
- [ ] Ordem de construção começa com algo testável em 1 dia

## Forma
- [ ] 80–150 linhas
- [ ] Termos técnicos explicados na primeira vez (nível dev júnior)
- [ ] Site de cliente: seção "O que o cliente aprova" existe
- [ ] Termina com "Chame Atlas: *build {primeiro bloco Must}"
- [ ] Salvo em `docs/prd/` do projeto alvo, nunca em `knowledge/`
