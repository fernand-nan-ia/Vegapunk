# X001 — Extração de Transcript (YouTube)

## Estratégia (ADR-004: transcript, nunca vídeo)

Ferramenta: `yt-dlp` via CLI, chamado do job Ruby com `Open3.capture3`. Motivos: extractor de legendas mais mantido do ecossistema, atualização independente do app (`yt-dlp -U`), e chamada via CLI mantém o runtime único (ADR-001).

## Normalização prévia (entrada deste doc)

Formatos de URL que DEVEM resolver para o mesmo `external_id` (videoId de 11 chars):

| Formato | Exemplo |
|---|---|
| Curto | `https://youtu.be/6DJFl-g83dM?si=...` |
| Padrão | `https://www.youtube.com/watch?v=6DJFl-g83dM&t=42` |
| Shorts | `https://www.youtube.com/shorts/6DJFl-g83dM` |
| Embed | `https://www.youtube.com/embed/6DJFl-g83dM` |

Regra: extrair o videoId via parsing de URL (sem requisição de rede); `canonical_url = https://www.youtube.com/watch?v=<id>`. Query params de tracking (`si`, `feature`, etc.) são descartados.

## Comando de extração

```bash
yt-dlp \
  --skip-download \
  --write-auto-subs --write-subs \
  --sub-langs "pt.*,en.*" \
  --sub-format "vtt" \
  --print "%(title)s\t%(channel)s\t%(duration)s\t%(upload_date)s" \
  -o "/tmp/kb/%(id)s.%(ext)s" \
  "<canonical_url>"
```

- `--write-subs` prioriza legenda humana; `--write-auto-subs` cobre a maioria (legenda automática).
- Preferência de idioma: legenda humana pt > humana en > automática pt > automática en.
- O `--print` captura metadados (título, canal, duração, data) sem segunda requisição.

## Pós-processamento do VTT (obrigatório)

Legendas automáticas em VTT vêm com timestamps, tags e **linhas duplicadas em janela deslizante** (cada linha aparece 2-3x). Pipeline de limpeza:

1. Remover cabeçalho WEBVTT, timestamps e tags (`<c>`, `<00:00:00.000>`).
2. Deduplicar linhas consecutivas idênticas.
3. Colapsar em parágrafo corrido; normalizar espaços.
4. Persistir em `raw_content`; detectar `content_lang` pelo sufixo do arquivo de legenda escolhido.

**REQ-X01:** transcript limpo com menos de 200 caracteres é tratado como ERR-004 (conteúdo insuficiente para enriquecimento útil).

## Mapa de erros => ERR-###

| Sinal no stderr/exit | Classificação | Retry? |
|---|---|---|
| `no subtitles` / nenhum arquivo `.vtt` gerado | ERR-004 | Não (determinístico) |
| `Private video` / `Video unavailable` / `region` | ERR-005 | Não |
| Timeout de rede, 5xx, `Unable to download` | ERR-003 | Sim (Sidekiq padrão) |
| Exit ≠ 0 não classificado | ERR-003 | Sim; logar stderr completo em `error_detail` |

## Higiene operacional

- **REQ-X02:** `yt-dlp` instalado via pip/binário com versão pinada em produção; job de saúde semanal roda `yt-dlp --version` e alerta se houver release nova (extractors quebram quando desatualizados — é a causa nº 1 de falha silenciosa).
- **REQ-X03:** limpar `/tmp/kb/<id>.*` no `ensure` do job, sucesso ou falha.
- **REQ-X04:** máximo 1 extração concorrente por plataforma (fila Sidekiq dedicada `extraction` com concorrência 1) — volume pessoal não justifica paralelismo, e serialização reduz risco de rate-limit.
