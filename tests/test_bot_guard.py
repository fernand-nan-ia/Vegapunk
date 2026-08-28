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
