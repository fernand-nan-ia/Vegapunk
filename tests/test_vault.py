import json
from vegapunk import vault

ITEM = {
    "id": "11111111-2222-3333-4444-555555555555", "platform": "youtube", "external_id": "6DJFl-g83dM",
    "canonical_url": "https://www.youtube.com/watch?v=6DJFl-g83dM", "channel": "Canal X", "captured_at": "2026-08-25T10:00:00+00:00",
    "status": "enriched", "triage_decision": None, "content_type": "transcript", "vault_path": None, "title": "orig",
    "enrichment": json.dumps({"title": "Qualquer um vira admin: falha de auth", "summary": "Resumo.", "key_points": ["p1", "p2"],
                              "tags": ["rails-security", "auth"], "applicability": {"saas_pessoal": "alta", "projeto_cliente": "media", "estudo_geral": "alta"},
                              "how_to_apply": "Revisar before_action.", "confidence": "alta"}),
}

def test_render_frontmatter_and_sections():
    md = vault.render(ITEM)
    assert md.startswith("---\nitem_id:")
    assert "tags: [\"rails-security\", \"auth\"]" in md
    assert "## Resumo" in md and "- p1" in md and "## Como aplicar" in md and vault.SENTINEL in md

def test_manual_notes_preserved(tmp_path, monkeypatch):
    monkeypatch.setattr(vault.settings, "vault_dir", tmp_path)
    p = vault.write_item(ITEM)
    assert p.name == "2026-08-25_qualquer-um-vira-admin-falha-de-auth_6DJFl-g83dM.md"
    p.write_text(p.read_text() + "\nminha anotação importante\n- item 2\n")
    item2 = {**ITEM, "vault_path": str(p), "triage_decision": "apply_saas", "status": "applied_saas"}
    p2 = vault.write_item(item2)
    txt = p2.read_text()
    assert "minha anotação importante\n- item 2" in txt
    assert "triage: apply_saas" in txt
    assert txt.count(vault.SENTINEL) == 1

def test_index(tmp_path, monkeypatch):
    monkeypatch.setattr(vault.settings, "vault_dir", tmp_path)
    p = vault.write_item(ITEM)
    idx = vault.write_index([{**ITEM, "vault_path": str(p)}])
    assert "rails-security" in idx.read_text() and "alta/media/alta" in idx.read_text()
