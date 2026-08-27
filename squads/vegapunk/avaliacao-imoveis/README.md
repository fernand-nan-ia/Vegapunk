# Avaliação de Imóveis

6 especialistas em avaliação imobiliária (NBR 14.653) — liderança técnica, pesquisa de mercado, inspeção com visão, redação de laudos, revisão adversarial e engenharia de dados.

## Quick Start

```
@avaliacao-imoveis:avaliador-chief   # Ativa o orquestrador (Roland)
*diagnose                            # Triagem do caso de avaliação
*workflow wf-property-evaluation     # Roda o ciclo completo de avaliação
*review                              # Submete um laudo para revisão de qualidade
```

## Agentes (6)

- **avaliador-chief** (Roland) — Orquestrador do ciclo de avaliação
- **inspetor-tecnico** (Sentinel) — Vistoria e patologias, com análise de imagem
- **pesquisador-mercado** (Trainman) — Pesquisa de mercado, amostragem, homogeneização
- **engenheiro-dados** (Dozer) — Planilha amostral, tratamento de dados, ponte SisDea/CalcImov
- **redator-laudos** (Rama-Kandra) — Redação do laudo e compliance normativo
- **revisor-adversarial** (Agent Johnson) — Revisão adversarial anti-rejeição bancária

## Fluxo

```
Vistoria (Sentinel) → Pesquisa de mercado (Trainman) → Tratamento de dados (Dozer)
→ Laudo (Rama-Kandra) → Revisão adversarial (Agent Johnson) → Entrega (Roland)
```

## Componentes

- **6 agentes**, **10 tasks**, **1 workflow**, **4 checklists**, **3 bases de referência**

## Domínio

- `engenharia-civil` — squad inaugural; 1ª missão: assistir a recriação do projeto **CalcImov** (bridge → software-dev)

## Requisitos

- FURY >= 5.3.5
