import json, pytest
from pydantic import ValidationError
from vegapunk.enrich import parse_output, _schema

GOOD = {"title": "T", "summary": "S.", "key_points": ["a"], "tags": ["rails-security"],
        "applicability": {"saas_pessoal": "alta", "projeto_cliente": "media", "estudo_geral": "baixa"},
        "how_to_apply": "x", "confidence": "alta"}

def test_parse_plain_and_fenced():
    assert parse_output(json.dumps(GOOD)).title == "T"
    assert parse_output("```json\n" + json.dumps(GOOD) + "\n```").tags == ["rails-security"]

def test_parse_rejects_missing_field():
    bad = {k: v for k, v in GOOD.items() if k != "tags"}
    with pytest.raises(ValidationError):
        parse_output(json.dumps(bad))

def test_schema_is_strict():
    s = _schema()
    assert s["additionalProperties"] is False
    assert s["$defs"]["Applicability"]["additionalProperties"] is False


def test_schema_requires_all_fields_for_strict_mode():
    s = _schema()
    assert set(s["required"]) == set(s["properties"])
    assert set(s["$defs"]["Topic"]["required"]) == {"name", "detail"}


def test_parse_defaults_topics_and_tools():
    e = parse_output(json.dumps(GOOD))
    assert e.topics == [] and e.tools == []
