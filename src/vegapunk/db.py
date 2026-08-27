"""SQLite: tabela knowledge_items + item_events e máquina de estados."""
import json
import sqlite3
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

STATUSES = {
    "captured", "normalized", "duplicate",
    "extracted", "extraction_failed", "pending_manual",
    "enriched", "enrichment_failed",
    "archived", "applied_saas", "applied_client", "discarded",
}
TERMINAL_TRIAGE = {"archived", "applied_saas", "applied_client", "discarded"}

TRANSITIONS: dict[str, set[str]] = {
    "captured": {"normalized", "duplicate"},
    "normalized": {"extracted", "extraction_failed", "pending_manual"},
    "extracted": {"enriched", "enrichment_failed"},
    "enriched": TERMINAL_TRIAGE,
    "extraction_failed": {"normalized"},
    "enrichment_failed": {"extracted"},
    "pending_manual": {"extracted", "normalized"},
}

SCHEMA = """
CREATE TABLE IF NOT EXISTS knowledge_items (
  id TEXT PRIMARY KEY,
  raw_url TEXT NOT NULL,
  telegram_chat_id INTEGER NOT NULL,
  telegram_message_id INTEGER NOT NULL,
  captured_at TEXT NOT NULL,
  platform TEXT, external_id TEXT, canonical_url TEXT,
  shared_count INTEGER NOT NULL DEFAULT 1,
  last_shared_at TEXT NOT NULL,
  title TEXT, channel TEXT, duration INTEGER, description TEXT,
  content_type TEXT, raw_content TEXT, content_lang TEXT, extracted_at TEXT,
  enrichment TEXT, enriched_at TEXT, model_used TEXT,
  triage_decision TEXT, triaged_at TEXT,
  status TEXT NOT NULL DEFAULT 'captured',
  error_code TEXT, error_detail TEXT,
  vault_path TEXT,
  created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_items_platform_external
  ON knowledge_items (platform, external_id) WHERE external_id IS NOT NULL AND status <> 'duplicate';
CREATE INDEX IF NOT EXISTS idx_items_status ON knowledge_items (status);
CREATE TABLE IF NOT EXISTS item_events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  item_id TEXT NOT NULL REFERENCES knowledge_items(id),
  from_status TEXT, to_status TEXT NOT NULL, actor TEXT NOT NULL,
  metadata TEXT, created_at TEXT NOT NULL
);
"""


class InvalidTransitionError(Exception):
    pass


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class Database:
    def __init__(self, path: Path | str):
        self.path = Path(path)
        if str(path) != ":memory:":
            self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(path), check_same_thread=False, isolation_level=None)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA journal_mode=WAL")
        self.conn.execute("PRAGMA foreign_keys=ON")
        self.conn.executescript(SCHEMA)
        self._migrate()

    def _migrate(self):
        """Colunas adicionadas depois do schema inicial (ADD COLUMN é idempotente via checagem)."""
        cols = {r[1] for r in self.conn.execute("PRAGMA table_info(knowledge_items)")}
        if "satellite" not in cols:
            self.conn.execute("ALTER TABLE knowledge_items ADD COLUMN satellite TEXT")

    @contextmanager
    def tx(self):
        self.conn.execute("BEGIN")
        try:
            yield
            self.conn.execute("COMMIT")
        except Exception:
            self.conn.execute("ROLLBACK")
            raise

    # ── CRUD ──────────────────────────────────────────────
    def create_item(self, raw_url: str, chat_id: int, message_id: int, satellite: str | None = None) -> str:
        item_id, ts = str(uuid.uuid4()), now()
        with self.tx():
            self.conn.execute(
                "INSERT INTO knowledge_items (id, raw_url, telegram_chat_id, telegram_message_id, captured_at,"
                " last_shared_at, created_at, updated_at, satellite) VALUES (?,?,?,?,?,?,?,?,?)",
                (item_id, raw_url, chat_id, message_id, ts, ts, ts, ts, satellite),
            )
            self._event(item_id, None, "captured", "webhook", {"raw_url": raw_url})
        return item_id

    def get(self, item_id: str) -> sqlite3.Row | None:
        return self.conn.execute("SELECT * FROM knowledge_items WHERE id=?", (item_id,)).fetchone()

    def find_by_external(self, platform: str, external_id: str) -> sqlite3.Row | None:
        return self.conn.execute(
            "SELECT * FROM knowledge_items WHERE platform=? AND external_id=? AND status<>'duplicate'",
            (platform, external_id),
        ).fetchone()

    def update(self, item_id: str, **fields):
        if "status" in fields:
            raise ValueError("use transition_to() para mudar status")
        if not fields:
            return
        fields["updated_at"] = now()
        cols = ", ".join(f"{k}=?" for k in fields)
        self.conn.execute(f"UPDATE knowledge_items SET {cols} WHERE id=?", (*fields.values(), item_id))

    def bump_shared(self, item_id: str):
        self.conn.execute(
            "UPDATE knowledge_items SET shared_count=shared_count+1, last_shared_at=?, updated_at=? WHERE id=?",
            (now(), now(), item_id),
        )

    def transition_to(self, item_id: str, new_status: str, actor: str, metadata: dict | None = None, **fields):
        item = self.get(item_id)
        if item is None:
            raise KeyError(item_id)
        cur = item["status"]
        if new_status not in TRANSITIONS.get(cur, set()):
            raise InvalidTransitionError(f"{cur} -> {new_status} (item {item_id})")
        with self.tx():
            fields["updated_at"] = now()
            cols = ", ".join(f"{k}=?" for k in fields)
            self.conn.execute(
                f"UPDATE knowledge_items SET status=?, {cols} WHERE id=?", (new_status, *fields.values(), item_id)
            )
            self._event(item_id, cur, new_status, actor, metadata)

    def _event(self, item_id, from_status, to_status, actor, metadata):
        self.conn.execute(
            "INSERT INTO item_events (item_id, from_status, to_status, actor, metadata, created_at) VALUES (?,?,?,?,?,?)",
            (item_id, from_status, to_status, actor, json.dumps(metadata or {}, ensure_ascii=False), now()),
        )

    # ── Consultas operacionais ─────────────────────────────
    def stats(self) -> list[tuple[str, int]]:
        rows = self.conn.execute("SELECT status, COUNT(*) c FROM knowledge_items GROUP BY status ORDER BY c DESC")
        return [(r["status"], r["c"]) for r in rows]

    def by_status(self, *statuses: str) -> list[sqlite3.Row]:
        q = ",".join("?" * len(statuses))
        return self.conn.execute(
            f"SELECT * FROM knowledge_items WHERE status IN ({q}) ORDER BY captured_at DESC", statuses
        ).fetchall()

    def all_with_enrichment(self) -> list[sqlite3.Row]:
        return self.conn.execute(
            "SELECT * FROM knowledge_items WHERE enrichment IS NOT NULL ORDER BY captured_at DESC"
        ).fetchall()
