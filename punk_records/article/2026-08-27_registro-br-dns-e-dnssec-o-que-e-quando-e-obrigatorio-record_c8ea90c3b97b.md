---
item_id: "98c2737f-c5c9-4531-98dd-6c8feff587be"
platform: article
external_id: "c8ea90c3b97b"
canonical_url: "https://registro.br/tecnologia/dnssec"
channel: "Registro.br (NIC.br)"
captured_at: 2026-08-27
status: archived
triage: archive
tags: ["registro-br", "dnssec", "dns", "seguranca-de-dominio", "records-ds", "bind"]
applicability:
  saas_pessoal: media
  projeto_cliente: media
  estudo_geral: alta
confidence: alta
theme: seguranca-e-privacidade
content_type: manual
---

# Registro.br — DNS e DNSSEC: o que é, quando é obrigatório, records e erros comuns

🔗 https://registro.br/tecnologia/dnssec

## Resumo

FAQ técnica do Registro.br sobre DNSSEC, a extensão de segurança do DNS que assina as respostas com criptografia assimétrica para impedir respostas falsas (envenenamento de cache, sequestro de transações). Qualquer domínio sob .br pode usar; é obrigatório apenas em b.br, bet.br, def.br, jus.br, leg.br, mp.br e tc.br, e é ativado automaticamente (sem opção de desligar) nos domínios que usam os servidores DNS do próprio Registro.br. Records introduzidos: DNSKEY (chave pública), RRSIG (assinatura de um RRset, com validade inicial e final), DS (delegação, informado ao Registro.br) e NSEC. Chaves não expiram, assinaturas sim — por isso servidores recursivos precisam de relógio sincronizado (NTP). Erros diagnosticados pelo sistema: NOSIG (zona não assinada pelas chaves do DS), EXPSIG (assinatura expirada — reassinar), NOKEY (DS não corresponde a chave da zona — usar a ferramenta DScheck), SIGERROR (assinatura inválida), TIMEOUT e PLAIN DNS ERROR (falha de consulta, muitas vezes firewall que não remonta fragmentos UDP/EDNS0; alternativa: edns-udp-size no BIND). Softwares com suporte: BIND 9.7+ e NSD 3.2.6+. Não é obrigatório assinar subdomínios delegados. Referências: RFCs 3833, 4033–4035, 4398, 4641, 5155 e tutoriais do Registro.br.

## Tópicos

- **Por que e quem** — Evita respostas DNS falsas; qualquer .br pode usar; obrigatório em 7 categorias; automático e irreversível no DNS do Registro.br.
- **Records e chaves** — DNSKEY, RRSIG (com validade), DS (informado ao registro), NSEC; chaves não expiram; NTP obrigatório no recursivo.
- **Erros e diagnóstico** — NOSIG, EXPSIG, NOKEY, SIGERROR, TIMEOUT, PLAIN DNS ERROR; ferramenta DScheck; firewall e EDNS0/UDP > 512 bytes.
- **Software e referências** — BIND 9.7+, NSD 3.2.6+; RFCs 3833/4033-4035/4398/4641/5155; tutoriais do Registro.br.

## Ferramentas citadas

- **DScheck**: valida o record DS do domínio
- **BIND / NSD**: servidores DNS com suporte a DNSSEC
- **NTP.br**: sincronização de relógio exigida pelo DNSSEC

## Pontos-chave

- Usando o DNS do Registro.br, DNSSEC já vem ligado — zero configuração e não dá para desligar.
- Com DNS próprio ou de hospedagem, DNSSEC é opcional e exige informar o DS ao Registro.br e reassinar a zona periodicamente.
- Assinatura expirada (EXPSIG) derruba o domínio para quem valida — automatizar a reassinatura.
- Firewall que bloqueia fragmentos UDP quebra DNSSEC (EDNS0); ajustar ou reduzir edns-udp-size.
- Não é preciso assinar subdomínios delegados.

## Como aplicar

Para o cliente e para o SaaS: se o DNS ficar no Registro.br, DNSSEC é automático; se o DNS for da Hostinger/Cloudflare, só ativar se o provedor cuidar da reassinatura — DNSSEC mal mantido derruba o site.

## 📚 Pythagoras diz

Registro técnico completo, e ele converge com o que já guardamos sobre segurança: a proteção só vale se for mantida. Deduzo — marcando — que para você a escolha é binária: DNS no Registro.br (DNSSEC automático, esquece) ou DNS no provedor (só ligue se ele reassinar sozinho). Chave não expira; assinatura expira; site cai. Isso é aritmética, não opinião.

## Notas manuais

<!-- PRESERVADO EM REGENERAÇÃO: tudo abaixo desta linha é mantido. Anote livremente. -->
