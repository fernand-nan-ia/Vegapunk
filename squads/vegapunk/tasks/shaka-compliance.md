# Task: shaka-compliance

Checagem legal e de acessibilidade de site ou feature. Executada por Shaka (`*compliance`). Usa `checklists/shaka-compliance-checklist.md`.

## Princípio

LGPD, cookies e acessibilidade não são feature; são pré-condição. Este é o único procedimento em que a condição pode ser "não lançar": coleta de dado pessoal sem base legal é passivo, não pendência. Vale para o SaaS pessoal (Fernando é o controlador) e para o site do cliente (o cliente é o controlador; Fernando é quem entrega o site e será cobrado pela ausência).

## Passos

1. **Mapear a coleta.** Sem este mapa não há julgamento. Tabela `dado · onde é coletado · para quê · onde fica · quem mais recebe`:
   - formulários (contato, cadastro, login), analytics, pixel de anúncio, cookies, logs com IP/e-mail, integrações (WhatsApp, e-mail transacional, pagamento, OpenRouter — texto do usuário sai para terceiro).
   - Ler o código quando houver: `grep -ri "cookie\|analytics\|gtag\|pixel\|fbq" src/ templates/`; verificar o que o backend loga.
2. **LGPD.** Para cada linha do mapa: base legal (consentimento, execução de contrato, legítimo interesse, obrigação legal). Política de privacidade: existe, está linkada no rodapé e no formulário, diz o que coleta, para quê, por quanto tempo, com quem compartilha, como o titular acessa/corrige/apaga, e-mail de contato do controlador. Dado de menor ou sensível (saúde, biometria, religião) → tratar como risco alto e sinalizar.
3. **Cookies.** Só existem cookies não-essenciais? Se sim: banner com recusa real (botão "recusar" tão visível quanto "aceitar"), scripts não-essenciais bloqueados até o consentimento, registro do consentimento (data, versão). Site só com cookie de sessão: aviso simples basta; dizer isso.
4. **Claims.** Toda promessa do texto com número, prazo ou resultado ("economize 40%", "em 24h", "garantido"): há prova ou disclaimer? "Garantido" sem garantia contratual escrita é claim indevida. Comparação com concorrente nomeado é risco; depoimento sem autorização é risco. Classificar em voz alta: evidência, opinião, anúncio.
5. **Acessibilidade mínima.** Contraste texto/fundo, `alt` em imagem com informação, foco visível ao navegar por Tab, todo campo com `label`, botões e links com texto (não só ícone), informação não transmitida só por cor, vídeo com legenda quando for conteúdo principal.
6. **Consolidar.** Para cada item: status (ok / falta / parcial) · consequência se ignorar, em linguagem de consequência (multa, pedido de remoção, cliente exposto, usuário excluído) · correção em uma frase · bloqueia gate? (sim para: coleta sem base legal, sem política de privacidade com coleta de dado, cookie de terceiro sem consentimento, claim "garantido" sem garantia; não para o resto).
7. **Citar o vault** quando houver item pertinente (ex.: requisitos legais essenciais para sites). Não inventar item.

## Saída

```
Veredito: {1 linha}
| item | status | consequência se ignorar | correção | bloqueia gate |
Condições mínimas para lançar: 1. ... 2. ...
Fonte no vault: [título](caminho) — se existir
Lilith diria "ninguém fiscaliza". Eu digo: o passivo existe antes da fiscalização.
```

## Regras

- Não redigir a política de privacidade; apontar o que ela precisa conter. Redação é Edison/Atlas com revisão jurídica humana se o cliente exigir.
- Não afirmar conformidade jurídica plena: Shaka aponta riscos e lacunas; parecer é advogado. Dizer isso uma vez, sem se esconder atrás.
- Máximo 20 linhas para um site simples.
