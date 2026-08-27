# Checklist: edison-wireframe

Edison roda antes de entregar um wireframe (`*wireframe`). Item ✗ → corrigir ou justificar.

## Propósito
- [ ] Objetivo da tela em 1 frase (entra para {ação}, sai com {resultado})
- [ ] Exatamente UMA ação primária (um botão `( )` principal)
- [ ] Lista de conteúdo ≤ 10 itens, em ordem de importância, e o desenho só tem o que está na lista

## Desenho
- [ ] Versão celular existe (se o público usa celular — site de cliente quase sempre)
- [ ] Blocos numerados, ligados à lista de conteúdo
- [ ] Convenções respeitadas: `[ ]` campo · `( )` botão · `#` título · `▣` imagem
- [ ] Baixa fidelidade: sem cor final, sem copy final, sem ícone decorativo

## Interação
- [ ] Cada bloco interativo tem: o que acontece ao clicar + estados (vazio / carregando / erro / sucesso)
- [ ] Campos com validação descrita (obrigatório? formato? mensagem de erro?)
- [ ] Diferenças celular × PC anotadas quando existem

## Mini design system
- [ ] Tabela de tokens presente e só com o que a tela usa
- [ ] Raio de borda ÚNICO (`--radius`) e escala de espaçamento única
- [ ] ≤ 3 estilos de botão (primário / secundário / desabilitado)
- [ ] 1 família de fonte, ≤ 3 tamanhos
- [ ] Se o projeto já tem design system: reutilizado, não reinventado

## Acessibilidade (mínimo)
- [ ] Contraste texto/fundo ≥ 4.5:1
- [ ] Todo campo com label visível (placeholder não é label)
- [ ] Botões com texto, não só ícone
- [ ] Área de toque ≥ 44px no celular
- [ ] Ordem de leitura faz sentido sem CSS; foco visível no teclado

## Entrega
- [ ] Itens do vault usados citados `[título](caminho)`
- [ ] Salvo em `docs/wireframes/{slug}.md` do projeto alvo; linka o PRD se houver
- [ ] Termina com "Chame Atlas: *build {tela} a partir de …"
