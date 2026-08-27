# Task: edison-wireframe

Executada por Edison (`*wireframe {tela}`). Wireframe de baixa fidelidade em TEXTO (ASCII/markdown) + notas de interação + mini design system — absorvido do `ux-design-expert` do FURY (ux-create-wireframe + tokens + a11y), sem Paper/21st.dev/Tailwind-pipeline. O que sai daqui é o desenho que Atlas transforma em HTML/JSX.

## Entrada
- `tela`: nome ("login", "dashboard do cliente", "página de contato").
- Contexto `{saas|cliente}` e dispositivo principal (perguntar: "celular primeiro ou PC?"; site de cliente costuma ser celular).
- Ler itens de UI/UX/design no `knowledge/INDEX.md` (tags `ui`, `ux`, `design`, `landing`); citar os usados. Se o projeto já tem um `design-system.md` ou tokens, ler e respeitar — não inventar paleta nova.

## Passos

1. **Objetivo da tela em 1 frase**: "o usuário entra aqui para {ação} e sai com {resultado}". Uma tela, uma ação principal. Se tiver duas, são duas telas.

2. **Conteúdo antes de layout.** Listar tudo que precisa estar na tela, em ordem de importância (1 = o que o usuário vê primeiro). Máximo 10 itens. O que não entrou na lista não entra no desenho.

3. **Wireframe ASCII** (celular primeiro se for o caso; depois variação PC se mudar muito). Convenções:
   ```
   ┌──────────────────────┐
   │ [logo]        [menu] │   ← cabeçalho
   │ # Título             │
   │ texto de apoio...    │
   │ [ campo: e-mail    ] │
   │ (  Botão primário  ) │   ← ação principal, só UM por tela
   │ link secundário      │
   └──────────────────────┘
   ```
   `[ ]` campo/elemento · `( )` botão · `#` título · `…` texto · `▣` imagem · `☐` checkbox. Cada bloco numerado à margem, ligando à lista do passo 2.

4. **Notas de interação** (por número do bloco): o que acontece ao clicar · estados (vazio, carregando, erro, sucesso) · validação de campo · o que muda no celular. Curto: uma linha por estado.

5. **Mini design system (átomos)** — só o que a tela usa, como tabela de tokens que Atlas copia direto:

   | Token | Valor | Uso |
   |---|---|---|
   | `--radius` | 8px | todos os cantos (raio inconsistente mata confiança — item do vault) |
   | `--space` | 4 / 8 / 16 / 24 / 32 px | escala única de espaçamento |
   | `--color-primary` | … | botão primário, links |
   | `--color-text` / `--color-bg` | … | contraste ≥ 4.5:1 |
   | fonte | 1 família, 3 tamanhos (14/16/24) | corpo / label / título |
   | botão | primário · secundário · desabilitado | nunca um 4º estilo |

   Se já existe design system no projeto: "usa o que existe", listar só o que falta.

6. **Checklist rápido de acessibilidade** (marcar ✓/✗): contraste texto/fundo ≥ 4.5:1 · todo campo tem label visível · botão tem texto (não só ícone) · área de toque ≥ 44px no celular · ordem de leitura faz sentido sem CSS · foco visível no teclado. ✗ tem que ter uma linha de correção.

7. **Rodar `checklists/edison-wireframe.md`.**

8. **Entregar.** Salvar em `docs/wireframes/{slug}.md` no projeto alvo (perguntar caminho se não souber). Terminar com: "Chame Atlas: *build {tela} a partir de docs/wireframes/{slug}.md". Se a tela nasceu de um PRD, linkar o PRD.

## Regras
- Baixa fidelidade de propósito: sem cor exata, sem ícone bonito, sem copy final. Copy real é do Fernando ou do cliente.
- Explicar o que é token/átomo/contraste na primeira vez, meia linha — Fernando é engenheiro civil (planta baixa é wireframe; ele já sabe o que é, só chama de outro nome).
- Uma ação primária por tela. Sempre.
- Não desenhar mais de 3 telas por chamada; se pediram um fluxo, desenhar a principal e listar as demais como "próximas".
