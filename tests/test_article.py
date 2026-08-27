import json
import random

import pytest

from vegapunk import vault, voices
from vegapunk.extract import ExtractionError, extract_article
from vegapunk.pipeline import format_summary

HTML = """<html><head><title>Novo LLM benchmark</title><meta name="author" content="Fabio Akita">
<meta property="og:site_name" content="AkitaOnRails"></head><body><nav>menu</nav>
<article><h1>Novo LLM benchmark: refiz todos os testes</h1>
<p>{p}</p><h2>Metodologia</h2><p>{p}</p><ul><li>item um</li><li>item dois</li></ul></article>
<footer>rodapé</footer></body></html>""".format(p="Texto do parágrafo com conteúdo suficiente para a extração funcionar bem. " * 6)


def test_extract_article_markdown_and_meta():
    ex = extract_article("https://akitaonrails.com/2026/07/30/x", html=HTML)
    assert ex.content_type == "article" and ex.duration is None
    assert "Metodologia" in ex.text and "item um" in ex.text and "rodapé" not in ex.text
    assert "Akita" in ex.channel and ex.title.startswith("Novo LLM benchmark")


def test_extract_article_too_short_is_not_retryable():
    with pytest.raises(ExtractionError) as e:
        extract_article("https://x.com/y", html="<html><body><p>oi</p></body></html>")
    assert e.value.code == "ERR-004" and not e.value.retryable


ENRICH = {"title": "T", "summary": "S.", "key_points": ["a"], "tags": ["llm-benchmark"],
          "applicability": {"saas_pessoal": "alta", "projeto_cliente": "media", "estudo_geral": "alta"},
          "how_to_apply": "x", "confidence": "alta", "satellite": "pythagoras",
          "satellite_take": "O registro diz: benchmark refeito. Eu deduzo que vale ler inteiro."}
ITEM = {"id": "1", "platform": "article", "external_id": "abc123def456", "canonical_url": "https://akitaonrails.com/x",
        "channel": "Fabio Akita · AkitaOnRails", "captured_at": "2026-08-27T10:00:00+00:00", "status": "enriched",
        "triage_decision": None, "content_type": "article", "vault_path": None, "title": "T",
        "raw_content": "# Título\n\nParágrafo integral do artigo.", "enrichment": json.dumps(ENRICH)}


def test_vault_keeps_full_article_text_and_satellite_take(tmp_path, monkeypatch):
    monkeypatch.setattr(vault.settings, "vault_dir", tmp_path)
    p = vault.write_item(ITEM)
    md = p.read_text()
    assert p.parent.name == "article"
    assert "## Texto integral" in md and "Parágrafo integral do artigo." in md
    assert "\n## Título" not in md and "\n### Título" in md  # títulos do artigo rebaixados
    assert "## 📚 Pythagoras diz" in md and "benchmark refeito" in md
    assert md.index("## Texto integral") < md.index(vault.SENTINEL)  # notas manuais continuam por último


def test_format_summary_in_satellite_voice_and_backward_compat():
    text = format_summary(ENRICH)
    assert text.startswith("📚 <b>Pythagoras</b> · Punk-04 apresenta:") and "<b>Pythagoras:</b>" in text
    assert "…" not in text and "Punk Records" in text
    old = {k: v for k, v in ENRICH.items() if k not in ("satellite", "satellite_take")}
    assert format_summary(old).startswith("🧠 <b>Stella</b> · Stella apresenta:")
    # Satélite fixado na captura vence o que o modelo escolheu
    assert format_summary(ENRICH, sat="lilith").startswith("🏴‍☠️ <b>Lilith</b> · Punk-02")


def test_brief_is_used_in_chat_and_summary_in_vault(tmp_path, monkeypatch):
    e = {**ENRICH, "brief": "Curto para o chat.", "summary": "Longo e completo para o arquivo. " * 3}
    assert "Curto para o chat." in format_summary(e) and "Longo e completo" not in format_summary(e)
    monkeypatch.setattr(vault.settings, "vault_dir", tmp_path)
    md = vault.write_item({**ITEM, "enrichment": json.dumps(e)}).read_text()
    assert "Longo e completo" in md


def test_capture_line_plural_and_html():
    rng = random.Random(1)
    one = voices.capture_line(1, sat="lilith", rng=rng)
    many = voices.capture_line(3, sat="lilith", rng=rng)
    assert one.startswith("🏴‍☠️ <b>Lilith</b> · Punk-02:") and "1 navio " in one and "3 navios" in many
    for sat in voices.CAPTURE:
        for n in (1, 2):
            assert "{" not in voices.capture_line(n, sat=sat)


def test_batch_owner_speaks_on_duplicate_and_failure():
    d = voices.duplicate_line("2026-08-27", 2, "archived", sat="york")
    assert d.startswith("🍩 <b>York</b> · Punk-06:") and "Nada novo" in d
    assert voices.duplicate_line("2026-08-27", 2, "archived", rng=random.Random(0)).split(":")[0] in ("📚 <b>Pythagoras</b> · Punk-04", "🪖 <b>Shaka</b> · Punk-01")
    f = voices.failure_line("extract", "abc12345", "ERR-003", sat="york")
    assert f.startswith("🍩 <b>York</b> · Punk-06:") and "/reprocess abc12345" in f and "ERR-003" in f
    assert voices.failure_line("extract", "abc12345", "ERR-003").startswith("🔧 <b>Atlas</b>")
