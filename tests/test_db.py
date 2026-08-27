import pytest
from vegapunk.db import Database, InvalidTransitionError

def make():
    return Database(":memory:")

def test_happy_path_and_events():
    db = make()
    i = db.create_item("https://youtu.be/x", 1, 1)
    db.transition_to(i, "normalized", "normalize_job", platform="youtube", external_id="x", canonical_url="u")
    db.transition_to(i, "extracted", "extract_job", raw_content="abc")
    db.transition_to(i, "enriched", "enrich_job", {"input_tokens": 1}, enrichment="{}")
    db.transition_to(i, "applied_saas", "user_triage", triage_decision="apply_saas")
    ev = db.conn.execute("SELECT to_status, actor FROM item_events WHERE item_id=? ORDER BY id", (i,)).fetchall()
    assert [tuple(e) for e in ev] == [("captured", "webhook"), ("normalized", "normalize_job"), ("extracted", "extract_job"),
                                      ("enriched", "enrich_job"), ("applied_saas", "user_triage")]

def test_invalid_transition():
    db = make()
    i = db.create_item("u", 1, 1)
    with pytest.raises(InvalidTransitionError):
        db.transition_to(i, "enriched", "x")

def test_status_update_blocked():
    db = make()
    i = db.create_item("u", 1, 1)
    with pytest.raises(ValueError):
        db.update(i, status="enriched")

def test_dedup_lookup():
    db = make()
    a = db.create_item("u", 1, 1)
    db.transition_to(a, "normalized", "n", platform="youtube", external_id="abc", canonical_url="c")
    assert db.find_by_external("youtube", "abc")["id"] == a
    db.bump_shared(a)
    assert db.get(a)["shared_count"] == 2


def test_satellite_column_migrated_and_stored(tmp_path):
    from vegapunk.db import Database
    db = Database(tmp_path / "x.db")
    i = db.create_item("https://a.com/x", 1, 1, satellite="york")
    assert db.get(i)["satellite"] == "york"
    assert db.get(db.create_item("https://a.com/y", 1, 2))["satellite"] is None
