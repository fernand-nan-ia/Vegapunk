import json

from vegapunk import themes, vault

E = {"title": "T", "summary": "Primeira frase. Segunda frase.", "key_points": ["a"], "tags": ["x"], "confidence": "alta",
     "applicability": {"saas_pessoal": "alta", "projeto_cliente": "media", "estudo_geral": "baixa"}, "how_to_apply": ""}


def _item(i, **e):
    return {"id": str(i), "platform": "article", "external_id": f"id{i}", "canonical_url": f"https://a.com/{i}", "channel": "",
            "captured_at": f"2026-08-{10+i:02d}T10:00:00+00:00", "status": "enriched", "triage_decision": None, "content_type": "article",
            "vault_path": None, "title": "T", "raw_content": "x", "enrichment": json.dumps({**E, **e})}


def test_guess_theme_from_tags_and_title():
    assert themes.guess_theme({"title": "Lei Geral de Proteção de Dados", "tags": ["lgpd", "privacidade"]}) == "seguranca-e-privacidade"
    assert themes.guess_theme({"title": "Checklist de vistoria de obra", "tags": ["construcao-civil"]}) == "engenharia-civil"
    assert themes.guess_theme({"title": "Top 10 jogos de PlayStation", "tags": ["videogame"]}) == "jogos-e-entretenimento"
    assert themes.guess_theme({"title": "tutorial de tricô", "tags": ["croche"]}) == "outros"
    assert themes.theme_of({"theme": "design-e-ux", "title": "lgpd", "tags": ["lgpd"]}) == "design-e-ux"   # modelo vence a reserva
    assert themes.theme_of({"theme": "inexistente", "title": "lgpd", "tags": ["lgpd"]}) == "seguranca-e-privacidade"


def test_index_grouped_by_theme_and_theme_pages(tmp_path, monkeypatch):
    monkeypatch.setattr(vault.settings, "vault_dir", tmp_path)
    items = [_item(1, title="LGPD", tags=["lgpd"], theme="seguranca-e-privacidade"),
             _item(2, title="Claude Code", tags=["claude-code"], theme="ia-e-agentes"),
             _item(3, title="Mais IA", tags=["llm"], theme="ia-e-agentes")]
    for it in items:
        it["vault_path"] = str(vault.write_item(it))
        assert "theme: " in (tmp_path / it["vault_path"]).read_text() if not it["vault_path"].startswith("/") else True
    idx = vault.write_index(items).read_text()
    assert "## Mapa de temas" in idx and "🤖 IA e agentes — 2 item(ns) → [temas/ia-e-agentes.md]" in idx
    assert idx.index("## 🤖 IA e agentes") < idx.index("## 🔐 Segurança e privacidade")   # ordem de THEMES
    assert "[Mais IA](article/" in idx and "[LGPD](article/" in idx
    page = (tmp_path / "temas/ia-e-agentes.md").read_text()
    assert page.startswith("# 🤖 IA e agentes") and "## [Claude Code](../article/" in page and "Primeira frase." in page
    assert (tmp_path / "temas/seguranca-e-privacidade.md").exists() and not (tmp_path / "temas/outros.md").exists()
    # tema que esvaziou some da pasta
    vault.write_index(items[:1])
    assert not (tmp_path / "temas/ia-e-agentes.md").exists()


def test_search_index_ignores_theme_map(tmp_path):
    from vegapunk import satellites
    (tmp_path / "temas").mkdir(); (tmp_path / "article").mkdir()
    (tmp_path / "temas/ia-e-agentes.md").write_text("# IA\n\nclaude code tudo", encoding="utf-8")
    (tmp_path / "article/a.md").write_text("# Claude Code\n\ncorpo", encoding="utf-8")
    (tmp_path / "INDEX.md").write_text("- 🤖 IA — 1 → [temas/ia-e-agentes.md](temas/ia-e-agentes.md)\n"
                                       "- 2026 · article · [Claude Code](article/a.md) · `claude-code` · alta · archive\n", encoding="utf-8")
    assert [rel for _, _, rel, _ in satellites.search_index("claude code", tmp_path)] == ["article/a.md"]
