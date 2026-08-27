# Checklist: shaka-gate

Usada por Shaka em `*gate`. Cada item: atendido / não atendido / n/a (com motivo). Sem evidência = não atendido.

## 1. Escopo e evidência
- [ ] O artefato está delimitado (diff, commit ou lista de arquivos) e foi lido inteiro
- [ ] Há evidência de teste: saída de `pytest`, log, screenshot ou `curl` — não frase de intenção
- [ ] `review` do Shaka foi feito e todos os must-fix estão fechados (ou WAIVED por escrito)
- [ ] Risco alto: relatório de `verify` da Lilith presente e seus achados CRÍTICO/ALTO fechados
- [ ] Recursion lock: não há gate anterior idêntico sem diff novo

## 2. Correção
- [ ] Faz o que a descrição promete (critérios de aceite ou `test-design` cobertos)
- [ ] Caminhos de erro tratados: entrada inválida, serviço externo fora, timeout
- [ ] Testes existentes continuam verdes (`pytest -q` ou equivalente)

## 3. Segurança (resumo — detalhe em shaka-security-checklist)
- [ ] `security-check` sem CRÍTICO aberto
- [ ] Nenhum segredo no diff (`.env`, chave OpenRouter, token Telegram, service key Supabase)
- [ ] Dado de usuário A inacessível a usuário B (RLS / filtro por dono / teste explícito)

## 4. Dados
- [ ] Migração (SQLite/Supabase) reversível ou backup feito antes
- [ ] Tabela nova no Supabase com RLS habilitado e política definida
- [ ] Dado pessoal novo mapeado em `compliance` (base legal, política de privacidade)

## 5. Custo e operação
- [ ] Chamadas a OpenRouter com limite (retries, tamanho de prompt, modelo escolhido conscientemente)
- [ ] Requisições externas com timeout
- [ ] Container sobe com `docker compose up` sem passo manual não documentado
- [ ] York não apontou item preso ou custo anormal no último `health`

## 6. Compliance e entrega
- [ ] `compliance` sem item "bloqueia gate = sim" aberto (quando toca site público ou dado pessoal)
- [ ] O Fernando consegue explicar a mudança a um usuário sem vergonha (honesta, sem truque)
- [ ] Reversível: há como desfazer (revert, feature flag, backup) e o Fernando sabe como

## Decisão
- PASS: tudo atendido ou n/a com motivo
- CONCERNS: itens de 5 ou 6 não críticos abertos, risco nomeado e aceito
- FAIL: qualquer item de 1, 3 ou 4 não atendido; ou compliance bloqueante; ou CRÍTICO de segurança
- WAIVED: FAIL assumido por escrito pelo Fernando, com prazo de revisão registrado
