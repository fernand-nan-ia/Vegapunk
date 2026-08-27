# Planta: {projeto}

- **Lido em:** YYYY-MM-DD · **Commit:** {hash curto} · **Autor:** Pythagoras, Punk-04
- **Formato preferido:** artifact HTML com 3 SVGs (gerado sob demanda; este Markdown é o esqueleto do conteúdo)

## Resumo em cinco linhas
- Linguagem / framework:
- Banco e armazenamento:
- Serviços externos:
- Entrada do sistema:
- Saída do sistema:

## Figura 1 — Mapa de módulos
{SVG: cada módulo é um cômodo; setas rotuladas com o que passa por elas; externos tracejados}
| Módulo | Arquivo(s) | Faz | Depende de | Usado por |
|---|---|---|---|---|

## Figura 2 — Percurso de um item
{SVG: entrada → etapas → armazenamento → saída; caminhos alternativos; custo/tempo por etapa quando conhecido}
| Etapa | Arquivo · função | Custo / tempo | Fonte do número |
|---|---|---|---|

## Figura 3 — Máquina de estados
{SVG: estados, transições, falhas em âmbar, finais em teal — ou "não há máquina de estados explícita"}
| Estado | Entra por | Sai por | Falha possível |
|---|---|---|---|

## Cartões por arquivo
### {arquivo}
- **Para que serve:** 
- **Linha que importa:** `{trecho}` — {o que faz, uma frase}
- **Como desfazer / trocar:** 

## Números reais (lidos em YYYY-MM-DD)
| Medida | Valor | Como foi lido |
|---|---|---|

## Decisões
| Decisão | Por quê | O que não fazer | Fonte (ADR, commit, nota) |
|---|---|---|---|
| | motivo: não há registro | | |

## Onde pode mudar
- **Pontos de extensão:** {arquivo · o que dá para plugar}
- **Pontos frágeis:** {arquivo · por que}
- **Eu deduzo:** {até 3}

## Encaminhamento
Mudança estrutural → Atlas `*build`. Risco → Lilith. Decisão nova → `*decision`.
