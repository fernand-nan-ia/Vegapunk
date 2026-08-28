"""Porteiro do dinheiro (bot.is_allowed): nada chega ao OpenRouter sem passar por aqui."""
import pytest

from vegapunk import bot
from vegapunk.config import settings

DM, GRUPO, EU, ESTRANHO = 111, -1002, 999, 42


@pytest.fixture
def limpo(monkeypatch):
    monkeypatch.setattr(settings, "allowed_chat_ids", {DM, GRUPO})
    monkeypatch.setattr(settings, "allowed_user_ids", set())
    monkeypatch.setattr(settings, "group_enabled", False)
    return settings


def test_lista_de_chats_vazia_recusa_tudo(limpo, monkeypatch):
    """A antiga falha ABERTA: lista vazia fazia o bot aceitar qualquer chat do Telegram."""
    monkeypatch.setattr(settings, "allowed_chat_ids", set())
    assert bot.is_allowed(DM, EU) is False
    assert bot.is_allowed(GRUPO, EU) is False


def test_chat_fora_da_lista_recusa(limpo):
    assert bot.is_allowed(777, EU) is False


def test_dm_autorizada_passa(limpo):
    assert bot.is_allowed(DM, EU) is True


def test_grupo_no_env_mas_desligado_nao_passa(limpo):
    """O id do grupo pode ficar no .env sem risco enquanto a cascata não existir."""
    assert bot.is_allowed(GRUPO, EU) is False


def test_grupo_ligado_de_proposito_passa(limpo, monkeypatch):
    monkeypatch.setattr(settings, "group_enabled", True)
    assert bot.is_allowed(GRUPO, EU) is True


def test_estranho_em_chat_autorizado_nao_gasta(limpo, monkeypatch):
    """Sem isto, qualquer participante do grupo gasta a chave do Fernando."""
    monkeypatch.setattr(settings, "group_enabled", True)
    monkeypatch.setattr(settings, "allowed_user_ids", {EU})
    assert bot.is_allowed(GRUPO, EU) is True
    assert bot.is_allowed(GRUPO, ESTRANHO) is False
    assert bot.is_allowed(GRUPO, None) is False


def test_sem_filtro_de_usuario_mantem_comportamento_antigo(limpo):
    assert bot.is_allowed(DM, ESTRANHO) is True


# ── trava anti-loop (condição bloqueante do Shaka, Story 1b) ────────────
def test_mensagem_de_bot_e_descartada_antes_de_tudo(limpo, monkeypatch):
    """No grupo há 7 bots: um respondendo ao outro seria conversa infinita paga por token."""
    monkeypatch.setattr(settings, "group_enabled", True)
    assert bot.is_allowed(GRUPO, EU, from_bot=True) is False
    assert bot.is_allowed(DM, EU, from_bot=True) is False


def test_anti_loop_vem_antes_ate_da_lista_de_chats(monkeypatch):
    """Porta 0: nem um chat perfeitamente autorizado salva uma mensagem vinda de bot."""
    monkeypatch.setattr(settings, "allowed_chat_ids", {DM})
    monkeypatch.setattr(settings, "allowed_user_ids", {EU})
    monkeypatch.setattr(settings, "group_enabled", True)
    assert bot.is_allowed(DM, EU) is True
    assert bot.is_allowed(DM, EU, from_bot=True) is False


def test_a_resposta_sai_pela_boca_do_satelite_que_respondeu():
    """Critério principal da Story 1b, que não tinha prova: no grupo, quem fala é o bot da Lilith."""
    import asyncio
    from unittest.mock import AsyncMock, MagicMock
    from vegapunk.speakers import Speakers

    leitor, lilith = MagicMock(), MagicMock()
    leitor.send_message = AsyncMock(); lilith.send_message = AsyncMock()
    s = Speakers(fallback=leitor)
    s.bots["lilith"] = lilith
    sat = MagicMock(id="lilith", icon="🏴‍☠️")

    asyncio.run(bot.responder(s, sat, "aguenta?", GRUPO, reply_to=7))
    lilith.send_message.assert_awaited_once()
    leitor.send_message.assert_not_awaited()
    assert "🏴‍☠️ aguenta?" in lilith.send_message.await_args.args

    asyncio.run(bot.responder(s, sat, "na DM", DM))       # na DM, o bot de sempre
    leitor.send_message.assert_awaited_once()
