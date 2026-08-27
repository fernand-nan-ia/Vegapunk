from vegapunk.pipeline import format_summary

E = {"title": "T <b>", "summary": "S & s.", "topics": [{"name": "RLS", "detail": "desligado por padrão"}],
     "tools": [{"name": "Supabase", "role": "banco"}], "key_points": ["p1"], "tags": ["a-b"],
     "applicability": {"saas_pessoal": "alta", "projeto_cliente": "media", "estudo_geral": "nenhuma"},
     "how_to_apply": "faça x", "confidence": "alta"}


def test_escaping_and_compact_chat_format():
    t = format_summary(E)
    assert "T &lt;b&gt;" in t and "S &amp; s." in t and "💡" in t and "#a_b" in t
    # tópicos e ferramentas ficam no Punk Records, não no chat
    assert "RLS" not in t and "Supabase" not in t and "Punk Records" in t


def test_optional_sections_hidden():
    t = format_summary({**E, "how_to_apply": ""})
    assert "💡" not in t


def test_never_truncates_only_top3_points():
    e = {**E, "key_points": ["x" * 100] * 10, "summary": "y" * 3000}
    t = format_summary(e)
    assert "…" not in t and t.count("• ") == 3 and "y" * 3000 in t
