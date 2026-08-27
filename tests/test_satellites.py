import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from vegapunk import satellites
from vegapunk.chat import Chat
from vegapunk.db import Database

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("sat_id", satellites.IDS)
def test_load_all_satellites(sat_id):
    sat = satellites.load(sat_id, ROOT / ".claude/commands/vegapunk/agents")
    assert sat.name and sat.icon and sat.role
    for k in ("mind", "relationships", "conversation", "examples"):
        assert k in sat.data, f"{sat_id} sem {k}"


def test_system_prompt_contains_persona_and_diary():
    sat = satellites.load("lilith", ROOT / ".claude/commands/vegapunk/agents")
    p = satellites.build_system_prompt(sat, diary_text="## Diário\n- 2026-08-26 · teste", index_text="- linha")
    assert "Lilith" in p and "Vegaforce" in p and "2026-08-26 · teste" in p and "ÍNDICE" in p
    assert "procedures" not in p and "commands:" not in p  # operacional fica fora


def test_pick_vault_items(tmp_path):
    (tmp_path / "x").mkdir()
    (tmp_path / "x/a.md").write_text("# Segurança em SaaS\ncorpo", encoding="utf-8")
    (tmp_path / "x/b.md").write_text("# Design\ncorpo", encoding="utf-8")
    (tmp_path / "INDEX.md").write_text(
        "# Índice\n\n- 2026 · yt · [Falhas de Segurança em SaaS](x/a.md) · `seguranca-saas` `rls` · alta · archive\n"
        "- 2026 · tt · [Boas práticas de UI](x/b.md) · `ui-design` · alta · archive\n", encoding="utf-8")
    got = satellites.pick_vault_items("o que eu sei sobre segurança no meu saas?", tmp_path)
    assert [rel for rel, _ in got] == ["x/a.md"]
    assert satellites.pick_vault_items("oi tudo bem", tmp_path) == []


def test_pick_vault_items_searches_body_and_stems(tmp_path):
    (tmp_path / "article").mkdir()
    (tmp_path / "article/h.md").write_text("---\nplatform: article\n---\n# Hot take sobre engenharia\n\n## Resumo\n\n"
                                           "Akita diz que harnesses e loop engineering são modismo.\n", encoding="utf-8")
    (tmp_path / "article/o.md").write_text("---\nplatform: article\n---\n# Outro\n\ncorpo sem relação\n", encoding="utf-8")
    (tmp_path / "INDEX.md").write_text("- 2026 · article · [Hot take sobre engenharia](article/h.md) · `opiniao` · alta · archive\n"
                                       "- 2026 · article · [Outro](article/o.md) · `x` · alta · archive\n", encoding="utf-8")
    got = satellites.pick_vault_items("o que o Akita falou de harness?", tmp_path)
    assert [rel for rel, _ in got] == ["article/h.md"]
    assert got[0][1].startswith("\n# Hot take")  # frontmatter removido


def _resp(text, model="m", tool_calls=None):
    r = MagicMock(); r.choices = [MagicMock()]; r.choices[0].message.content = text
    r.choices[0].message.tool_calls = tool_calls
    r.model = model; r.usage = MagicMock(prompt_tokens=10, completion_tokens=5)
    return r


def _call(name, args, cid="c1"):
    c = MagicMock(); c.id = cid; c.function.name = name; c.function.arguments = json.dumps(args)
    return c


def test_chat_state_history_and_reply():
    db = Database(":memory:")
    chat = Chat(db)
    assert chat.active(1) is None
    with patch("vegapunk.chat._client") as c, patch.object(satellites, "AGENTS_DIR", ROOT / ".claude/commands/vegapunk/agents"), \
         patch("vegapunk.satellites.settings") as st:
        st.vault_dir = ROOT / "punk_records"
        c.return_value.chat.completions.create.return_value = _resp("Três navios afundados.")
        sat, text = chat.reply(1, "oi Lilith")          # ninguém ativo → Stella
        assert sat.id == "stella"
        chat.wake(1, "lilith")
        sat, text = chat.reply(1, "oi de novo")
        assert sat.id == "lilith" and text == "Três navios afundados."
        msgs = c.return_value.chat.completions.create.call_args.kwargs["messages"]
        assert msgs[0]["role"] == "system" and "Lilith" in msgs[0]["content"]
        assert msgs[-1] == {"role": "user", "content": "oi de novo"}
    assert len(chat.history(1, "lilith")) == 2 and len(chat.history(1, "stella")) == 2
    assert chat.cost_rows(1)[0][1:] == (1, 10, 5)
    assert chat.forget(1, "lilith") == 2 and chat.history(1, "lilith") == []
    chat.sleep(1)
    assert chat.active(1) is None


def test_nothing_lost_vs_baseline():
    """Toda seção e todo comando que existiam antes da absorção do FURY continuam existindo."""
    import json
    base = json.loads((ROOT / "tests/satellites_baseline.json").read_text(encoding="utf-8"))
    for sat_id, b in base.items():
        sat = satellites.load(sat_id, ROOT / ".claude/commands/vegapunk/agents")
        missing_sections = [s for s in b["sections"] if s not in sat.data]
        names = [c["name"] for c in sat.data["commands"]]
        missing_cmds = [c for c in b["commands"] if c not in names]
        assert not missing_sections and not missing_cmds, f"{sat_id}: seções {missing_sections} comandos {missing_cmds}"
        assert len(names) == len(set(names)), f"{sat_id}: comandos duplicados"


def test_dependencies_exist_when_absorbed():
    """Tasks/checklists/templates citados em dependencies existem em squads/vegapunk/ (autossuficiente)."""
    base = ROOT / "squads/vegapunk"
    for sat_id in satellites.IDS:
        sat = satellites.load(sat_id, ROOT / ".claude/commands/vegapunk/agents")
        deps = sat.data.get("dependencies") or {}
        for kind, items in deps.items():
            for rel in items or []:
                if kind == "squads":
                    assert (base / rel).is_dir(), f"{sat_id}: squad {rel} ausente"
                else:
                    assert (base / rel).exists() or (base / kind / rel).exists(), f"{sat_id}: {kind}/{rel} ausente"


def test_parse_command_and_canned_replies():
    assert satellites.parse_command("*attack  usar scraping") == ("attack", "usar scraping")
    assert satellites.parse_command("* cost") == ("cost", "")
    assert satellites.parse_command("oi tudo bem") is None
    lilith = satellites.load("lilith")
    assert Chat.unavailable_reply(lilith, "attack") is None                      # roda no Telegram
    assert "/vegapunk:lilith" in Chat.unavailable_reply(lilith, "verify")        # só no Claude Code
    assert "*attack" in Chat.unavailable_reply(lilith, "help") and "Punk-02" in Chat.unavailable_reply(lilith, "help")
    assert "não conheço" in Chat.unavailable_reply(lilith, "xyz")


def test_reply_runs_tool_loop_and_command_procedure(tmp_path):
    db = Database(":memory:")
    chat = Chat(db)
    chat.wake(1, "york")
    with patch("vegapunk.chat._client") as c, patch("vegapunk.satellites.settings") as st, \
         patch("vegapunk.tools.punk_records_status", return_value={"estimated_cost_usd": 0.13}) as status:
        st.vault_dir = tmp_path
        c.return_value.chat.completions.create.side_effect = [
            _resp("", tool_calls=[_call("punk_records_status", {})]),
            _resp("Bocejo. Treze centavos, uma coxinha."),
        ]
        sat, text = chat.reply(1, "*cost")
        assert sat.id == "york" and "coxinha" in text
        status.assert_called_once()
        calls = c.return_value.chat.completions.create.call_args_list
        assert "tools" in calls[0].kwargs                                          # 1ª rodada oferece ferramentas
        msgs = calls[1].kwargs["messages"]
        assert any(m.get("role") == "tool" and "0.13" in m["content"] for m in msgs)  # resultado voltou ao modelo
        assert any("=== COMANDO *cost ===" in m.get("content", "") for m in msgs if m["role"] == "system")
        assert any("=== FERRAMENTAS ===" in m.get("content", "") for m in msgs if m["role"] == "system")
    assert chat.cost_rows(1)[0][1:] == (1, 20, 10)                               # tokens das 2 rodadas somados


def test_reply_unavailable_command_costs_nothing():
    db = Database(":memory:")
    chat = Chat(db)
    chat.wake(1, "atlas")
    with patch("vegapunk.chat._client") as c:
        sat, text = chat.reply(1, "*develop a story")
        c.assert_not_called()
    assert "Claude Code" in text and "*explain" in text and "<b>" not in text and text.startswith("🔧 Atlas · Punk-05")
