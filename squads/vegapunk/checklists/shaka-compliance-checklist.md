# Checklist: shaka-compliance

Usada por Shaka em `*compliance`. Vale para SaaS pessoal (Fernando = controlador) e site de cliente (cliente = controlador; Fernando = quem entrega). Para cada item: ok / falta / parcial / n/a com motivo. Coluna "bloqueia gate" já decidida abaixo.

## A. Mapa de coleta (pré-requisito — sem ele, parar)
- [ ] Tabela `dado · onde é coletado · para quê · onde fica · quem mais recebe` preenchida
- [ ] Integrações que recebem dado listadas (Supabase, OpenRouter, WhatsApp, e-mail, pagamento, analytics)
- [ ] Logs do backend verificados quanto a IP, e-mail, telefone, texto do usuário

## B. LGPD
| Item | Bloqueia gate |
|---|---|
| [ ] Base legal identificada para cada dado do mapa | sim |
| [ ] Política de privacidade existe e está linkada no rodapé e junto de todo formulário | sim, se há coleta |
| [ ] A política diz: o que coleta, finalidade, prazo de retenção, com quem compartilha, direitos do titular (acesso, correção, exclusão, portabilidade) e como exercê-los | sim |
| [ ] E-mail ou canal de contato do controlador/encarregado na política | sim |
| [ ] Dado sensível (saúde, biometria, religião, orientação) ou de menor: consentimento específico e destacado | sim |
| [ ] Há como apagar o usuário e seus dados a pedido (rotina ou procedimento manual documentado) | não (CONCERNS) |
| [ ] Termos de uso existem quando há conta/pagamento | não (CONCERNS) |

## C. Cookies e rastreamento
| Item | Bloqueia gate |
|---|---|
| [ ] Inventário: quais cookies/scripts, essenciais ou não | — |
| [ ] Só cookies essenciais (sessão, CSRF): aviso simples basta; registrar que é esse o caso | não |
| [ ] Cookies/scripts não-essenciais (analytics, pixel): banner com "recusar" tão visível quanto "aceitar" | sim |
| [ ] Scripts não-essenciais não carregam antes do consentimento (verificar no DevTools → Network com banner aberto) | sim |
| [ ] Consentimento registrado (data, versão da política) e revogável | não (CONCERNS) |

## D. Claims e texto
| Item | Bloqueia gate |
|---|---|
| [ ] Toda promessa com número, prazo ou resultado tem prova ou disclaimer visível | não (CONCERNS) |
| [ ] Nenhum "garantido" sem garantia contratual escrita | sim |
| [ ] Depoimentos com autorização; sem depoimento inventado | sim |
| [ ] Sem comparação com concorrente nomeado sem base verificável | não (CONCERNS) |
| [ ] Preço exibido é o preço cobrado (impostos, recorrência, cancelamento claros) | sim, se há venda |
| [ ] Classificação em voz alta: cada claim é evidência, opinião ou anúncio | — |

## E. Acessibilidade mínima
| Item | Bloqueia gate |
|---|---|
| [ ] Contraste texto/fundo suficiente (verificar com DevTools → Accessibility) | não (CONCERNS) |
| [ ] Imagens com informação têm `alt`; decorativas têm `alt=""` | não |
| [ ] Foco visível ao navegar por Tab; ordem de foco faz sentido | não |
| [ ] Todo campo de formulário com `label`; erro de validação em texto, não só em cor | não (CONCERNS) |
| [ ] Botões e links com texto ou `aria-label`; sem "clique aqui" | não |
| [ ] Vídeo principal com legenda; áudio não dispara sozinho | não |

## Decisão
- Qualquer "sim" aberto em B, C ou D → `gate` FAIL até corrigir; condição mínima para lançar é a lista desses itens.
- Só "não (CONCERNS)" abertos → CONCERNS, nomeados no registro.
- Shaka aponta lacunas e consequências; parecer jurídico é de advogado. Dizer uma vez.
