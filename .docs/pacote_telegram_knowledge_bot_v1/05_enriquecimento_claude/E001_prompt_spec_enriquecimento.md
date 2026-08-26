# E001 — Enriquecimento via Claude API: Prompt Spec e Contrato

## Chamada

- Endpoint: `POST /v1/messages` (Anthropic API).
- Modelo: `claude-sonnet-4-6` (custo/qualidade adequado para sumarização; registrar em `model_used`).
- `max_tokens`: 2000. Temperatura padrão.
- Input: metadados do item (título, canal, duração, plataforma) + `raw_content` truncado em ~50k caracteres (transcripts de vídeos longos excedem o necessário para resumo; truncar com aviso no prompt).

## System prompt (template)

```
Você é um analista de conhecimento técnico. Recebe transcripts de vídeos
sobre desenvolvimento de software, IA e tecnologia, e produz um resumo
estruturado em JSON.

Contexto do usuário final: engenheiro de workflows de IA que mantém
(a) um SaaS pessoal em Rails e (b) um site de cliente, ambos desenvolvidos
via Claude Code. A matriz "applicability" avalia relevância prática do
conteúdo para cada frente.

REGRAS DE OUTPUT:
1. Responda APENAS com um objeto JSON válido. Sem markdown, sem backticks,
   sem texto antes ou depois.
2. O objeto DEVE validar contra o schema fornecido. Não adicione campos.
3. summary em pt-BR, 3 a 6 frases, fiel ao conteúdo — não extrapole.
4. key_points: afirmações acionáveis ou fatos centrais, não títulos vagos.
5. tags: kebab-case, minúsculas, específicas (ex.: "rails-security",
   "prompt-injection"), nunca genéricas como "tecnologia".
6. confidence reflete a qualidade do transcript de entrada: transcript
   truncado, com muito ruído de auto-legenda ou incoerente => "baixa".
7. Se o transcript for insuficiente para um resumo honesto, ainda assim
   retorne o JSON, com confidence "baixa" e summary descrevendo o que foi
   possível apurar.
```

## User message (template)

```
SCHEMA:
<json schema completo do README>

ITEM:
item_id: <uuid>
platform: <platform>
titulo_original: <title>
canal: <channel>
duracao_segundos: <duration>

TRANSCRIPT:
<raw_content truncado>
```

## Validação (ADR-005 — bloqueante)

1. Parse do JSON. Se houver fences ```` ```json ````, remover antes do parse (defensivo).
2. Validar contra o schema com a gem `json_schemer`.
3. **Falha na 1ª tentativa:** reenviar com mensagem adicional: `"Seu output anterior falhou na validação: <erros>. Corrija e reenvie apenas o JSON."`
4. **Falha na 2ª tentativa:** `transition_to!('enrichment_failed')` com ERR-007; output bruto salvo em `error_detail` para diagnóstico.
5. Sucesso: gravar em `enrichment` (JSONB), registrar `model_used` e `enriched_at`.

## Regras de custo e segurança

- **REQ-E01:** logar tokens de input/output de cada chamada (vêm no response `usage`) num campo do `item_events.metadata` — base para auditoria de custo.
- **REQ-E02:** o transcript é conteúdo de terceiros não confiável. O system prompt acima já restringe o formato de saída; adicionalmente, o pipeline NUNCA executa nada vindo do enriquecimento — é dado, não instrução. Nenhum campo do JSON é interpolado em comandos ou queries sem sanitização.
- **REQ-E03:** rate limit defensivo: fila Sidekiq `enrichment` com concorrência 1 e `sleep` desnecessário — o volume pessoal (unidades/dia) está ordens de magnitude abaixo dos limites da API. Não implementar throttling complexo (over-engineering).
