# Checklist: atlas-dod (Definition of Done)

Rodada por Atlas no fim de `*develop`, `*build` e `*fix` (`*dod` roda avulsa). Absorvida do `story-dod-checklist` do FURY, sem Story/Epic: aqui o "pronto" é do pedido de uma frase. Cada item é ✅ / ❌ / N/A com uma linha de evidência. ❌ sem justificativa = não está pronto.

## 1. Fez o que foi pedido

- [ ] O escopo em uma frase foi entregue — nem mais, nem menos
- [ ] Nada fora do escopo foi alterado (refatoração "de passagem" ficou como sugestão)
- [ ] Decisões de valor/risco que apareceram foram levadas a Shaka/Lilith, não decididas por Atlas

## 2. Código

- [ ] Segue o estilo do projeto (nomes, estrutura de pastas, linguagem já usada)
- [ ] Sem segredo no código (`grep -rE "sk-|api_key|password" {arquivos}` limpo); segredos em `.env` e `.env` no `.gitignore`
- [ ] Sem `print`/`console.log` de debug esquecido
- [ ] Dependência nova só com aprovação explícita e registrada em `requirements.txt`/`package.json`
- [ ] Erros tratados onde podem acontecer de verdade (rede, arquivo, banco) — sem `except: pass`

## 3. Testes (evidência colada, não descrita)

- [ ] Todos os testes existentes rodaram e passaram (saída na conversa)
- [ ] Existe teste que prova a mudança nova (se não havia, o mínimo foi criado)
- [ ] Lint rodou, se o projeto tem (`ruff`, `eslint`)
- [ ] Nada de "deve funcionar" — só "rodei e deu X"

## 4. Explicação (regra de bancada da Atlas)

- [ ] Cada trecho mostrado veio com "para que serve" nível júnior
- [ ] O Fernando consegue apontar, por arquivo, o que mudou e por quê
- [ ] "Entendeu?" foi perguntado e respondido

## 5. Ambiente e dados

- [ ] Mudanças em `.env`, Docker, infra ou banco foram avisadas ANTES e explicadas
- [ ] Migration, se houve: snapshot + dry-run + rollback existem (`atlas-db-predeploy-checklist.md`)
- [ ] Dado de usuário não foi tocado sem aviso

## 6. Fechamento

- [ ] Lista "arquivo → mudança" completa (inclui arquivos criados e apagados)
- [ ] "Como desfazer" em 1–2 linhas, testável
- [ ] "Pronto para commit:" listado — e nenhum `git add/commit/push` executado
- [ ] `memory/atlas.md` › `## Construído` atualizado (data · o quê · onde · como desfazer)

## Resultado

| Seção | ✅ | ❌ | N/A |
|---|---|---|---|
| 1–6 | | | |

**Veredito:** PRONTO / VOLTA AO PASSO k (motivo em uma linha)
