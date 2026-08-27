---
item_id: "4cc5a980-bcca-4224-b6a2-53e4dbbf97db"
platform: article
external_id: "db9f7210abeb"
canonical_url: "https://registro.br/dominio/regras"
channel: "Registro.br (NIC.br)"
captured_at: 2026-08-27
status: enriched
triage: null
tags: ["registro-br", "dominio-br", "regras-de-registro", "dns", "saci-adm", "categorias-de-dominio"]
applicability:
  saas_pessoal: media
  projeto_cliente: alta
  estudo_geral: media
confidence: alta
theme: desenvolvimento-e-ferramentas
content_type: manual
---

# Registro.br — regras para registro de domínios .br (quem pode, DNS, categorias com documentação, tickets)

🔗 https://registro.br/dominio/regras

## Resumo

FAQ 'Registro de novos domínios' do Registro.br, que responde às regras práticas do .br. Pode registrar qualquer pessoa física (CPF) ou jurídica (CNPJ) estabelecida no Brasil com contato nacional; estrangeiros precisam de procurador no país. Ninguém reserva domínio — só o Comitê Gestor. Não é preciso provedor: são necessários dois servidores DNS configurados, que podem ser os do próprio Registro.br (exceto para gov.br, leg.br, jus.br, mp.br, edu.br, def.br, b.br, emp.br, tc.br e bet.br); sem DNS próprio e sem pendência, o domínio sai em até 5 minutos; com DNS próprio com erro, há 2 semanas para corrigir. Domínio 'reservado pelo CG' não está disponível; domínio registrado mas sem site não pode ser tomado. Pode-se registrar qualquer nome disponível, não só razão social ou marca — mas registro de má-fé em outra categoria pode ser suspenso ou transferido via SACI-Adm. Categorias com documentação (am.br, coop.br, edu.br, fm.br, g12.br, org.br) enviam comprovantes a doc@registro.br; outras exigem autorização de órgão (b.br, def.br, jus.br, leg.br, mil.br, mp.br, tc.br, bet.br, leilao.br); edu.br só para ensino superior com nome não genérico. Acentos e cedilha são permitidos se a versão sem acento for do mesmo titular ou estiver livre — recomenda-se registrar as duas. radio.br só para pessoa jurídica; ong.br para CPF ou CNPJ. A fila de tickets roda a cada 5 minutos; pendências são comunicadas por e-mail e o ticket expira se não resolvidas.

## Tópicos

- **Quem pode registrar** — CPF ou CNPJ com contato no Brasil; estrangeiro via procurador; nenhuma reserva de nome.
- **DNS e prazos** — Dois servidores DNS (Registro.br oferece, salvo categorias institucionais); 5 minutos sem pendência; 2 semanas para corrigir DNS próprio.
- **Nome e categorias** — Qualquer nome disponível; má-fé em outra categoria → SACI-Adm; documentação por e-mail para am/coop/edu/fm/g12/org; autorização para b/def/jus/leg/mil/mp/tc/bet/leilao.
- **Acentos e casos especiais** — Acento/cedilha se a versão ASCII for do mesmo titular ou livre; radio.br só PJ; ong.br PF ou PJ; gov.br só federal.
- **Tickets** — Fila a cada 5 minutos; pendências por e-mail; ticket cancelado se não resolver no prazo.

## Ferramentas citadas

- **SACI-Adm**: sistema administrativo de conflitos para nomes de domínio .br
- **whois do Registro.br**: consultar responsáveis por domínios e subdomínios estaduais gov.br

## Pontos-chave

- Não precisa de hospedagem para registrar: os servidores DNS do Registro.br bastam e o domínio sai em ~5 minutos.
- Pode registrar qualquer nome disponível — não precisa ser a razão social — mas má-fé pode custar o domínio no SACI-Adm.
- Registrar a versão com e sem acento evita que outro pegue a variante.
- Categorias institucionais e regulamentadas exigem documento ou autorização; o .com.br comum não.
- DNS próprio com erro tem 2 semanas para ser corrigido, senão o ticket cai.

## Como aplicar

Para o cliente: registrar o .com.br no CNPJ dele, usar DNS do Registro.br até a hospedagem existir e depois apontar; registrar também a versão sem acento se o nome tiver. Para o SaaS: mesmo caminho, e checar SACI-Adm se o nome coincidir com marca alheia.

## 📚 Pythagoras diz

Aqui o registro é completo e diz o que importa: o .br não depende de provedor, sai em cinco minutos e aceita qualquer nome disponível. Eu deduzo — marcando — que a única armadilha para o seu cliente é o acento: registre 'joão' e 'joao', ou alguém registra o outro. E anote o SACI-Adm: é onde uma marca briga por um nome.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
