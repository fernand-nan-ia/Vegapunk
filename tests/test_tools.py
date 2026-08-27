import json
from pathlib import Path

from vegapunk import tools
from vegapunk.db import Database


def _vault(tmp_path):
    (tmp_path / "article").mkdir()
    (tmp_path / "article/h.md").write_text("---\nplatform: article\n---\n# Hot take\n\n## Resumo\n\nHarness é modismo.\n\n## Pontos-chave\n\n- a\n", encoding="utf-8")
    (tmp_path / "INDEX.md").write_text("- 2026 · article · [Hot take](article/h.md) · `opiniao` · alta · archive\n", encoding="utf-8")
    return tmp_path


def test_search_and_read(tmp_path):
    v = _vault(tmp_path)
    r = tools.search_punk_records("o que dizem de harness?", vault_dir=v)
    assert r["results"][0]["path"] == "article/h.md" and r["results"][0]["summary"] == "Harness é modismo."
    assert tools.search_punk_records("zzz", vault_dir=v)["note"].startswith("nenhum")
    item = tools.read_item("article/h.md", vault_dir=v)
    assert item["content"].startswith("# Hot take") and not item["truncated"]
    assert "error" in tools.read_item("../../etc/passwd", vault_dir=v)
    assert "error" in tools.read_item("article/nao.md", vault_dir=v)


def test_status_and_diary(tmp_path):
    db = Database(":memory:")
    db.create_item("https://a.com/x", 1, 1)
    st = tools.punk_records_status(db)
    assert st["items_by_status"] == {"captured": 1} and st["estimated_cost_usd"] == 0
    r = tools.write_diary("york", "Fernando  disse que o cliente paga dia 5", memory_dir=tmp_path)
    assert r["written"].endswith("· Fernando disse que o cliente paga dia 5")
    md = (tmp_path / "york.md").read_text()
    assert "## Diário" in md and "paga dia 5" in md
    tools.write_diary("york", "segundo fato", memory_dir=tmp_path)
    assert (tmp_path / "york.md").read_text().count("\n- 20") == 2


def test_run_tool_returns_json_and_handles_unknown():
    db = Database(":memory:")
    assert json.loads(tools.run_tool("punk_records_status", {}, sat_id="york", db=db))["untriaged"] == 0
    assert "error" in json.loads(tools.run_tool("nope", {}, sat_id="york", db=db))
