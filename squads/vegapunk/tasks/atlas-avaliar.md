# Task: atlas-avaliar

Executada por Atlas (`*avaliar`) como MASTER do squad `avaliacao-imoveis`. Atlas não avalia imóvel: ela orquestra o ciclo, chama cada especialista por nome, guarda os artefatos entre fases e faz o portão entre uma e outra. O papel de decisão final é de Roland (avaliador-chief). Referências: `squads/vegapunk/avaliacao-imoveis/squad.yaml`, `README.md`, `workflows/wf-property-evaluation.yaml`.

## Squad (6 agentes, em `squads/vegapunk/avaliacao-imoveis/commands/agents/`)

| Agente | Nome | Tier | Papel |
|---|---|---|---|
| `avaliador-chief` | Roland | 0 | Triagem, mediação, aprovação final (exclusiva) |
| `inspetor-tecnico` | Sentinel | 1 | Vistoria IBAPE, patologias, análise de imagens |
| `pesquisador-mercado` | Trainman | 1 | Amostra de mercado saneada e rastreável |
| `engenheiro-dados` | Dozer | 2 | Regressão, pressupostos, campo de arbítrio, ponte SisDea/CalcImov |
| `redator-laudos` | Rama-Kandra | 2 | Laudo NBR 14.653, enquadramento de grau |
| `revisor-adversarial` | Agent Johnson | 3 | Simula banco, juízo e comprador — portão obrigatório |

## Entrada

| Campo | Obrigatório | Descrição |
|---|---|---|
| imóvel | sim | Tipo, endereço, características |
| fim | sim | `bancário` · `judicial` · `particular` |
| imagens | não | Fotos (acionam a visão do Sentinel) |
| prazo | não | Restrição de prazo |
| fase | não | Rodar só uma fase (`vistoria`, `pesquisa`, `tratamento`, `laudo`, `compliance`, `adversarial`, `decisao`) |

## Ciclo (8 fases, sequencial, `wf-property-evaluation`)

| # | Fase | Agente | Task (em `avaliacao-imoveis/tasks/`) | Cria | Portão (gate) |
|---|---|---|---|---|---|
| 1 | Triagem | Roland | `diagnose.md` | `triagem` | fim + grau-alvo + método definidos |
| 2 | Vistoria | Sentinel | `conduct-inspection.md` (+ `analyze-pathology-images.md` se há fotos) | `laudo_inspecao` | 9 etapas IBAPE; patologias classificadas; limitações declaradas |
| 3 | Pesquisa | Trainman | `conduct-market-research.md` | `amostra_saneada` | amostra dimensionada ao grau; oferta×transação; origens rastreáveis |
| 4 | Tratamento | Dozer | `build-sample-dataset.md` | `modelo_tratado` | pressupostos testados; significância vs. grau; campo de arbítrio |
| 5 | Laudo | Rama-Kandra | `draft-laudo.md` | `laudo` | estrutura NBR completa; zero afirmação órfã; ressalvas |
| 6 | Compliance | Rama-Kandra | `validate-norms.md` | `enquadramento` | grau sustentado pela tabela; lacunas reportadas |
| 7 | Adversarial | Agent Johnson | `adversarial-laudo-review.md` | `veredito` | 3 adversários; fragilidades com vetor + reparo |
| 8 | Decisão | Roland | `review.md` → `approve-laudo` | `laudo_aprovado` | 8 critérios; veredito considerado |

Fases 2 e 3 dependem só da 1 e podem rodar em paralelo. A 4 depende das duas.

## Procedimento da Atlas

1. **Passo 0 — abrir o caso.** Confirmar `imóvel` + `fim`. Sem `fim`, Roland veta e Atlas nem chama. Criar pasta de trabalho `avaliacoes/{slug-do-imovel}/` e um `caso.md` com os inputs. Nível júnior: "cada fase deixa um arquivo aqui; a próxima lê o anterior — é a memória do ciclo".
2. **Para cada fase k de 8:** anunciar "Fase k de 8 — {agente} ({nome})", carregar o agente em `commands/agents/{id}.md`, executar a task da tabela com os artefatos anteriores como entrada, salvar a saída em `avaliacoes/{slug}/{k}_{cria}.md`.
3. **Portão.** Conferir o gate da tabela contra a saída. Passou → próxima. Reprovou → repetir a fase com o motivo (máx. 2 vezes); na 3ª, parar e reportar ao Fernando ("Grr.").
4. **Devolução do adversarial (fase 7).** `veredito = devolver` → voltar à fase dona da fragilidade (vetor + reparo indicados) e reexecutar dali em diante. Roland não aprova laudo que não passou aqui.
5. **Checklists nos portões:** fase 2 → `checklists/inspection-quality.md`; fase 6 → `checklists/norms-compliance.md`; fase 7 → `checklists/bank-defensibility.md`; fase 8 → `checklists/laudo-dod.md`.
6. **Erros previstos** (do workflow): amostra insuficiente → parecer técnico em vez de laudo (NBR 14.653-2 §9.1.2); grau abaixo do alvo → reforçar amostra/modelo ou rebaixar grau com transparência; divergência entre especialistas → Roland media pelo fim e grau-alvo.
7. **Fechar:** tabela fase → artefato → status; laudo aprovado (ou devolvido com motivos); tokens gastos por fase se York estiver por perto; "Como desfazer": apagar `avaliacoes/{slug}/` — nada mais foi tocado. Registrar em `memory/atlas.md` › `## Construído`.

## Regras

- Atlas orquestra; não escreve laudo, não homogeneíza, não aprova. Cada fase é do seu agente, pela task dele.
- A decisão final (fase 8) é indelegável de Roland. Atlas só entrega.
- Se o Fernando pedir "só o valor, sem ciclo": responder que sem fases 3, 4 e 7 é chute, não avaliação — e chamar Shaka se ele insistir.
- Fotos e endereço real do cliente: não sair da pasta do caso; nunca ir para o vault.

## Saída

Pasta `avaliacoes/{slug}/` com 8 artefatos + resumo do ciclo + laudo aprovado/devolvido.
