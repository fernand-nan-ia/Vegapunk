# Story 1a: Roteador — decidir quem responde no grupo (sem tocar no bot)

**Projeto:** vegapunk     **Status:** pronta
**Origem:** `docs/prd/satelites-multibots-grupo-telegram.md` §0 e §4.1 (decisões do Fernando em 2026-08-28)

## Objetivo (1 frase, valor para o Fernando)
Ter uma função que lê uma mensagem do grupo e responde "quem dos Satélites está sendo chamado?" — acertando "Shaka e Lilith, o que acham?" (os dois) e "fui pra Nova York" (ninguém) — para que os bots só gastem Mother Flame quando o Fernando realmente chamou.

## Contexto que Atlas precisa
- Arquivo novo: `src/vegapunk/router.py`. **Nada mais em `src/` é tocado nesta story** — o bot só passa a usar o roteador na Story 1c.
- Reaproveitar `enrich._client()` (cliente OpenRouter já configurado) e o padrão `response_format={"type":"json_schema","strict":True,...}` + Pydantic com 1 retry, exatamente como `enrich.py:183-188`. Erros de rede/API viram as mesmas exceções (`EnrichmentError`, códigos ERR-006/007).
- Ids válidos: `satellites.IDS` = `("stella","shaka","lilith","edison","pythagoras","atlas","york")`. Nomes de exibição em `voices.NAME`.
- Modelo: `settings.model` por padrão, com override por env `VEGAPUNK_ROUTER_MODEL` (novo campo em `config.Settings`, default `""` = usa `settings.model`).
- Decisão fechada do HANDOFF que se aplica: OpenRouter via SDK `openai`, sem API da Anthropic direta. O prompt do roteador **não** carrega persona nem `INDEX.md` — é isso que o mantém ~30× mais barato que uma resposta em personagem.
- Armadilha do `.env`: nunca comentário na mesma linha do valor (`VEGAPUNK_ROUTER_MODEL=x  # comentário` quebra o Docker).

## Interface que Atlas deve respeitar
```python
# src/vegapunk/router.py
@dataclass
class Routing:
    satellites: list[str]   # ids em satellites.IDS; ordem = ordem de resposta; [] = ninguém
    confidence: str         # "alta" | "media" | "baixa"
    reason: str             # 1 frase curta, só para o log

def mentions(text: str) -> list[str]:
    """Camada 2, GRÁTIS: nomes de Satélite presentes no texto (palavra inteira, sem acento, case-insensitive).
    Não decide nada — só diz se vale a pena pagar o roteador."""

def route(text: str, recent: list[str] | None = None, active: str | None = None) -> Routing:
    """Camada 3, PAGA: 1 chamada ao modelo com o texto + até 3 linhas recentes do grupo.
    `active` = Satélite que falou por último (contexto da janela de continuidade).
    Falha fechada: qualquer exceção, JSON inválido ou id desconhecido -> Routing([], "baixa", "erro: ...")."""
```

## Critérios de aceite
- [ ] `mentions("fui pra Nova York")` devolve `["york"]` (o regex acha mesmo) e `mentions("bom dia")` devolve `[]` — deixando claro que quem descarta o falso positivo é o `route`, não o regex
- [ ] `route` devolve `[]` para "fui pra Nova York no ano passado" e `["lilith"]` para "Lilith, o que acha disso?" (teste com resposta do modelo mockada, no estilo de `tests/test_satellites.py`)
- [ ] `route` devolve `["shaka","lilith"]` para "Shaka e Lilith, o que acham?" e `["shaka"]` para "Shaka, o que você acha do que a Lilith falou?"
- [ ] **Falha fechada:** cliente que levanta exceção, JSON inválido, ou id fora de `satellites.IDS` → `Routing([], "baixa", ...)`; nunca lista cheia, nunca exceção vazando para quem chamou
- [ ] `confidence == "baixa"` sempre sai com `satellites == []` (normalizado dentro do `route`, não no chamador)
- [ ] Toda chamada de `route` emite uma linha de log com: texto truncado em 80 chars, lista devolvida, confiança, e tokens de entrada/saída (auditoria da 1ª semana, condição do Shaka)
- [ ] `PYTHONPATH=src .venv/bin/python -m pytest -q` continua verde (70 + os novos)

## Fora de escopo
- Não mexer em `bot.py`, `chat.py`, `db.py` nem no `.env` de produção — é a Story 1c.
- Não criar bot novo no BotFather, não rodar 2 Applications, não tocar em privacy mode.
- Não implementar a janela de 10 min (é 1c); aqui `active` só é repassado ao prompt como contexto.
- Não persistir as decisões do roteador em tabela — log basta nesta story.

## Riscos / Shaka
Shaka `*risk` 2026-08-28 (veredito completo na sessão): risco **médio-baixo, condicional**. Desta story em diante valem duas condições dele:
- **Custo:** toda decisão do roteador logada com tokens gastos — sem log, não passa no `*gate`. (Coberto pelo 6º critério.)
- Condições de `.env`/privacy mode/`is_bot` pertencem às stories 1b e 1c; aqui nada roda em produção.

## Testes esperados
`tests/test_router.py` — mock do cliente OpenRouter com `patch("vegapunk.router._client")`, no molde de `tests/test_satellites.py:69`. Uma tabela de casos: "Nova York" → `[]`; um nome → 1; dois nomes → 2; nome como objeto da frase → 1; erro do cliente → `[]`.

## Como desfazer
Apagar `src/vegapunk/router.py`, `tests/test_router.py` e o campo `router_model` de `config.py`. Nada mais foi tocado.

## Handoff → Atlas: `*develop squads/vegapunk/stories/2026-08-28-multibot-1a-roteador.md`
