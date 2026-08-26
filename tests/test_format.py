from vegapunk.pipeline import format_summary

E = {"title": "T <b>", "summary": "S & s.", "topics": [{"name": "RLS", "detail": "desligado por padrão"}],
     "tools": [{"name": "Supabase", "role": "banco"}], "key_points": ["p1"], "tags": ["a-b"],
     "applicability": {"saas_pessoal": "alta", "projeto_cliente": "media", "estudo_geral": "nenhuma"},
     "how_to_apply": "faça x", "confidence": "alta"}


def test_sections_and_escaping():
    t = format_summary(E)
    assert "T &lt;b&gt;" in t and "S &amp; s." in t
    assert "📚" in t and "RLS" in t and "🛠" in t and "Supabase" in t and "💡" in t and "#a_b" in t


def test_optional_sections_hidden():
    e = {**E, "topics": [], "tools": [], "how_to_apply": ""}
    t = format_summary(e)
    assert "📚" not in t and "🛠" not in t and "💡" not in t


def test_truncation_keeps_html_safe():
    e = {**E, "key_points": ["x" * 100] * 10, "summary": "y" * 3000}
    t = format_summary(e, limit=1000)
    assert len(t) <= 1002 and t.endswith("…")
