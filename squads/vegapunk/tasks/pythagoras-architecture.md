# Task: pythagoras-architecture

Documentação de arquitetura de um projeto existente, executada por Pythagoras (`*architecture {projeto}`). Absorvida do FURY `architect`, invertida: aqui não se desenha o sistema antes de existir — registra-se o que Atlas construiu, a partir do código real. Formato preferido de saída: a "planta de arquitetura" que o Fernando aprovou (artifact HTML com 3 SVGs), gerada sob demanda, nunca mantida no repositório.

## Entrada
- `{projeto}` — caminho ou nome (`vegapunk`, `saas`, `cliente`). Sem argumento → listar os projetos conhecidos em `memory/pythagoras.md › Sobre o Fernando` e perguntar.
- Opcional: `--md` (saída em Markdown em vez de artifact HTML); `--foco {módulo}` (só uma parte).

## Regra de ouro
Nada na planta que não exista no código. Cada módulo, seta, estado e número vem de um arquivo, comando ou consulta que foi aberto ou executado. O que não foi verificado aparece como "não verificado", não como fato.

## Passos
1. **Levantamento.** Ler `README`, `CLAUDE.md`, `HANDOFF.md`, `docker-compose`, `pyproject`/`package.json`, `.env.example` e a árvore de diretórios (2 níveis). Listar: linguagem, framework, banco, serviços externos, entrada e saída do sistema.
2. **Módulos.** Para cada diretório/arquivo relevante: o que faz (uma linha), de quem depende, quem depende dele. Externos (APIs, bots, bancos gerenciados) ficam tracejados.
3. **Percurso de um item.** Escolher a unidade central (uma mensagem, um pedido, um cadastro) e seguir o caminho: entrada → processamento → armazenamento → saída, com caminhos alternativos e, quando houver, custo ou tempo por etapa (tokens, segundos, chamadas).
4. **Máquina de estados.** Se houver campo de status/etapa, mapear estados, transições, falhas (âmbar) e finais (teal). Se não houver, dizer "não há máquina de estados explícita" e não inventar uma.
5. **Números reais.** Consultar banco, índice ou logs para contagens atuais (itens, tabelas, linhas, usuários). Marcar a data da leitura.
6. **Decisões.** Tabela decisão · por quê · o que não fazer, extraída de commits, comentários, `## Notas manuais` e ADRs existentes em `docs/decisions/`. Decisão sem registro de motivo entra como "motivo: não há registro".
7. **Onde pode mudar.** Pontos de extensão e pontos frágeis, com o arquivo de cada um. Aqui cabe até 3 inferências marcadas "eu deduzo".
8. **Produzir.** Usar `templates/pythagoras-architecture.md` como esqueleto. Padrão: artifact HTML com 3 SVGs (mapa de módulos com setas rotuladas; percurso do item; máquina de estados), seguidos de cartões por arquivo, números, tabela de decisões e "onde pode mudar". Metáfora de engenharia civil (planta, cômodos, portas) é bem-vinda — uma por documento.
9. **Explicar** para o Fernando em registro dev júnior: ao citar uma linha de código, mostrar e dizer para que serve.
10. **Encaminhar.** Mudança estrutural sugerida → Atlas (`*build`). Risco encontrado → Lilith. Registrar em `memory/pythagoras.md › Diário` que a planta foi gerada e para qual projeto.

## Não fazer
- Propor stack nova ou reescrever módulo (Atlas decide, Shaka julga).
- Desenhar componente que "deveria existir".
- Manter o HTML no repositório: é foto do momento, gerada sob demanda.
