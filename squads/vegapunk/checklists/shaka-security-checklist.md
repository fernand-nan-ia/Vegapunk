# Checklist: shaka-security (8 pontos)

Usada por Shaka em `*security-check` e resumida no `gate`. Para cada ponto: evidência (comando ou trecho lido), não afirmação. Explicar pela consequência, não pelo jargão.

| # | Ponto | Como verificar | Consequência se falhar | Severidade típica |
|---|---|---|---|---|
| 1 | **Segredos** — chave OpenRouter, token Telegram, service key Supabase, senha de banco em código, log ou git | `git diff` + `grep -rEn "sk-or-|eyJ|api_key\s*=\s*['\"]" --exclude-dir=.venv .`; `.env` no `.gitignore`; `git log -p --all -S "sk-or-"` se houver suspeita | Qualquer pessoa com o repositório usa sua conta e paga com seus tokens | CRÍTICO |
| 2 | **Injeção** — SQL montado por concatenação, comando shell com entrada do usuário, prompt com entrada não delimitada | `grep -rn "execute(f\|execute(\"\.\*%\|os.system\|subprocess.*shell=True"`; parâmetros ligados (`?`/`%s`) em toda query; entrada do usuário no prompt entre delimitadores e tratada como dado | Usuário apaga ou lê o banco inteiro; ou faz o modelo ignorar as instruções | CRÍTICO |
| 3 | **XSS / saída** — texto do usuário renderizado em HTML sem escape; Markdown/HTML do Telegram reenviado sem sanitizar | Templates com autoescape ligado; `grep -rn "|safe\|innerHTML\|dangerouslySetInnerHTML"` | Um link malicioso rouba sessão de outro usuário do site do cliente | ALTO |
| 4 | **Autenticação e sessão** — senha com hash forte, sessão expira, logout invalida, rate limit no login, reset de senha com token único e curto | Ler o módulo de auth; testar login errado 20× seguidas | Força bruta em senha; sessão roubada vale para sempre | ALTO |
| 5 | **Autorização / IDOR** — toda rota que recebe id verifica se o id pertence ao usuário logado | Para cada rota com `{id}`: onde está o filtro por dono? Teste: usuário A pede recurso de B → 403/404 | Qualquer usuário vê ou altera dado de qualquer outro trocando um número na URL | CRÍTICO |
| 6 | **RLS e banco** — Supabase: RLS habilitado em toda tabela exposta, política por `auth.uid()`, anon key só com o que o público pode ver; SQLite: arquivo fora do diretório servido, permissões restritas | Painel Supabase → Policies; `SELECT ... WHERE rowsecurity = false`; `ls -l data/` | Com a anon key (que está no front) qualquer um lê a tabela inteira | CRÍTICO |
| 7 | **Dependências e superfície** — dependência nova justificada, versão fixada, sem CVE conhecida; portas do Docker só as necessárias; webhook valida assinatura/origem | `pip list --outdated`, `pip-audit` se disponível; `docker compose config` → `ports`; verificar segredo no webhook | Biblioteca comprometida executa código no seu container; webhook forjado cria dados falsos | ALTO |
| 8 | **Logs e dado pessoal** — logs não gravam senha, token, e-mail, telefone ou texto integral do usuário; erros ao usuário não expõem stack trace ou caminho interno | `grep -rn "logger\.\|print(" src/` nos pontos de auth e de entrada; provocar um erro e ler a resposta | Log vira vazamento de dado pessoal (passivo LGPD); stack trace ensina o atacante | ALTO |

## Saída
```
| ponto | status | onde | correção |
Must-fix: 1. ... 
Gate: qualquer CRÍTICO aberto → FAIL automático
```

## Regras
- "Não encontrei" só vale com o comando que foi rodado ao lado.
- Ponto n/a precisa de motivo ("não há Supabase neste projeto").
- Item do vault sobre segurança em SaaS é a referência; citar quando pertinente.
