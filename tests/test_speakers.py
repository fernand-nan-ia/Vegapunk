"""Os Satélites que só falam: um Bot por token, nenhum handler, e o leitor como rede de segurança."""
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from vegapunk import satellites, speakers
from vegapunk.config import settings

GRUPO, DM = -1002, 111


def corre(coro):
    """Roda uma corrotina num teste síncrono — evita a dependência do pytest-asyncio."""
    return asyncio.run(coro)


def _bot(username="x_bot"):
    b = MagicMock()
    b.initialize = AsyncMock()
    b.shutdown = AsyncMock()
    b.get_me = AsyncMock(return_value=MagicMock(username=username))
    b.send_message = AsyncMock()
    return b


@pytest.fixture
def tokens_dos_sete(monkeypatch):
    monkeypatch.setattr(settings, "bot_tokens", {i: f"tok-{i}" for i in satellites.IDS})


def test_tokens_ignora_o_leitor_e_nomes_desconhecidos(monkeypatch):
    monkeypatch.setattr(settings, "bot_tokens", {"stella": "a", "lilith": "b", "kizaru": "c"})
    assert speakers.tokens() == {"lilith": "b"}          # stella tem Application; kizaru não é Satélite


def test_initialize_sobe_um_bot_por_satelite(tokens_dos_sete):
    with patch("vegapunk.speakers.Bot", side_effect=lambda tok: _bot(f"{tok}_bot")):
        s = speakers.Speakers(fallback=_bot("stella_bot"))
        nomes = corre(s.initialize())
    assert set(nomes) == set(satellites.IDS) - {"stella"}   # seis; o leitor não entra
    assert nomes["lilith"] == "tok-lilith_bot"


def test_token_ruim_nao_derruba_o_servico(monkeypatch):
    """Critério: token ausente ou inválido degrada com aviso; o Satélite fala pela boca do leitor."""
    monkeypatch.setattr(settings, "bot_tokens", {"lilith": "boa", "shaka": "ruim"})
    def cria(tok):
        b = _bot()
        if tok == "ruim":
            b.get_me = AsyncMock(side_effect=RuntimeError("401 Unauthorized"))
        return b
    with patch("vegapunk.speakers.Bot", side_effect=cria):
        s = speakers.Speakers(fallback=_bot())
        nomes = corre(s.initialize())
    assert list(nomes) == ["lilith"] and "shaka" not in s.bots


def test_no_grupo_fala_o_satelite_na_dm_fala_o_leitor(tokens_dos_sete):
    leitor = _bot("stella_bot")
    with patch("vegapunk.speakers.Bot", side_effect=lambda tok: _bot()):
        s = speakers.Speakers(fallback=leitor)
        corre(s.initialize())
    assert s.bot_for("lilith", GRUPO) is s.bots["lilith"]   # grupo: nome e ícone dela
    assert s.bot_for("lilith", DM) is leitor                # DM: um bot não escreve para quem não o abriu
    assert s.bot_for("stella", GRUPO) is leitor             # o leitor fala por si mesmo


def test_satelite_sem_token_cai_para_o_leitor(monkeypatch):
    monkeypatch.setattr(settings, "bot_tokens", {})
    s = speakers.Speakers(fallback=_bot())
    corre(s.initialize())
    assert s.bot_for("york", GRUPO) is s.fallback


def test_falha_de_envio_cai_para_o_leitor_sem_perder_a_resposta(tokens_dos_sete):
    leitor = _bot("stella_bot")
    ruim = _bot()
    ruim.send_message = AsyncMock(side_effect=RuntimeError("chat not found"))
    with patch("vegapunk.speakers.Bot", side_effect=lambda tok: ruim):
        s = speakers.Speakers(fallback=leitor)
        corre(s.initialize())
        corre(s.say("lilith", GRUPO, "aguenta?"))
    ruim.send_message.assert_awaited_once()
    leitor.send_message.assert_awaited_once()   # a resposta chegou de qualquer jeito


def test_bots_que_so_falam_nao_tem_onde_registrar_handler():
    """Estrutural: `Bot` não tem `add_handler` — o critério deixa de depender de alguém lembrar."""
    from telegram import Bot
    assert not hasattr(Bot, "add_handler")


def test_falha_intermitente_ganha_segunda_chance(monkeypatch):
    """Produção 2026-08-28: o bot da Lilith caiu com TimedOut e ficou fora até o restart seguinte."""
    monkeypatch.setattr(settings, "bot_tokens", {"lilith": "tok"})
    tentativas = {"n": 0}

    def cria(tok):
        b = _bot("lilith_bot")
        tentativas["n"] += 1
        if tentativas["n"] == 1:
            b.get_me = AsyncMock(side_effect=TimeoutError("Timed out"))
        return b

    with patch("vegapunk.speakers.Bot", side_effect=cria):
        s = speakers.Speakers(fallback=_bot())
        nomes = corre(s.initialize())
    assert tentativas["n"] == 2 and nomes["lilith"] == "lilith_bot"


def test_desiste_depois_de_duas_tentativas(monkeypatch):
    monkeypatch.setattr(settings, "bot_tokens", {"lilith": "tok"})
    def cria(tok):
        b = _bot()
        b.get_me = AsyncMock(side_effect=TimeoutError("Timed out"))
        return b
    with patch("vegapunk.speakers.Bot", side_effect=cria) as m:
        s = speakers.Speakers(fallback=_bot())
        assert corre(s.initialize()) == {}
    assert m.call_count == 2 and s.bot_for("lilith", GRUPO) is s.fallback


# ── consertos do *verify da Lilith na Story 1b ──────────────────────────
def test_bot_que_falha_no_get_me_e_desligado(monkeypatch):
    """MÉDIO: `initialize` já abriu o pool httpx; descartar sem shutdown vaza conexão."""
    monkeypatch.setattr(settings, "bot_tokens", {"lilith": "tok"})
    ruim = _bot()
    ruim.get_me = AsyncMock(side_effect=TimeoutError("Timed out"))
    with patch("vegapunk.speakers.Bot", return_value=ruim):
        s = speakers.Speakers(fallback=_bot())
        corre(s.initialize())
    assert ruim.shutdown.await_count == 2        # uma por tentativa


def test_resposta_longa_sai_toda_pela_mesma_boca(tokens_dos_sete):
    """MÉDIO: decidir por pedaço deixaria metade da fala com a cara de outro Satélite."""
    leitor = _bot("stella_bot")
    lilith = _bot("lilith_bot")
    lilith.send_message = AsyncMock(side_effect=[RuntimeError("boom"), None, None])
    with patch("vegapunk.speakers.Bot", return_value=lilith):
        s = speakers.Speakers(fallback=leitor)
        corre(s.initialize())
        corre(s.say_all("lilith", GRUPO, ["um", "dois", "tres"], reply_to=9))
    assert lilith.send_message.await_count == 1          # falhou no 1º e não voltou a ser usada
    assert leitor.send_message.await_count == 3          # os três pedaços saíram pela mesma boca


def test_queda_para_o_leitor_larga_o_reply_to(tokens_dos_sete):
    """MÉDIO: se a mensagem original sumiu, ela É a causa — repetir o kwarg faria o leitor falhar igual."""
    leitor = _bot("stella_bot")
    lilith = _bot()
    lilith.send_message = AsyncMock(side_effect=RuntimeError("message to be replied not found"))
    with patch("vegapunk.speakers.Bot", return_value=lilith):
        s = speakers.Speakers(fallback=leitor)
        corre(s.initialize())
        corre(s.say_all("lilith", GRUPO, ["oi"], reply_to=9))
    assert leitor.send_message.await_args.kwargs.get("reply_to_message_id") is None
