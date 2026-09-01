"""A costura do grupo: decidir → responder como o Satélite certo → firmar a janela."""
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from vegapunk import bot, router
from vegapunk.chat import Chat
from vegapunk.db import Database

GRUPO = -1002


@pytest.fixture(autouse=True)
def orcamento_limpo():
    router._respostas.clear(); router._recentes.clear()
    yield
    router._respostas.clear(); router._recentes.clear()


def _speakers():
    s = MagicMock()
    s.usernames = {"lilith": "vegapunkklilithbot", "shaka": "vegapunkshakabot"}
    s.say_all = AsyncMock()
    s.fallback.send_message = AsyncMock()
    return s


def _chat():
    c = Chat(Database(":memory:"))
    c.reply = MagicMock(side_effect=lambda cid, txt, sat=None: (MagicMock(id=sat, icon="x"), f"resposta de {sat}"))
    return c


def test_grupo_chama_reply_com_o_satelite_decidido_e_fala_pela_boca_dele():
    chat, sp = _chat(), _speakers()
    with patch("vegapunk.router.route", return_value=router.Routing(["shaka"], "alta", "ok")):
        quem = asyncio.run(bot.responder_no_grupo(chat, sp, GRUPO, "Shaka, e aí?", 7))
    assert quem == ["shaka"]
    assert chat.reply.call_args.args[2] == "shaka"        # respondeu COMO shaka, não como o ativo
    assert sp.say_all.await_args.args[0] == "shaka"       # e falou pela boca dele
    assert chat.active(GRUPO) == "shaka"                  # janela firmada


def test_roteador_calado_nao_gera_resposta_nem_custo_de_personagem():
    """Com triagem ligada o roteador é consultado, mas lista vazia continua significando silêncio."""
    chat, sp = _chat(), _speakers()
    with patch("vegapunk.router.route", return_value=router.Routing([], "alta", "não pede resposta")):
        quem = asyncio.run(bot.responder_no_grupo(chat, sp, GRUPO, "kkk", 7))
    assert quem == [] and chat.reply.call_count == 0     # a camada CARA não foi tocada
    sp.say_all.assert_not_awaited()


def test_teto_estourado_avisa_uma_vez_e_para():
    chat, sp = _chat(), _speakers()
    for _ in range(router.MAX_REPLIES_PER_MIN):
        router.pode_responder()
    with patch("vegapunk.router.route", return_value=router.Routing(["shaka", "lilith"], "alta", "dois")):
        quem = asyncio.run(bot.responder_no_grupo(chat, sp, GRUPO, "Shaka e Lilith?", 7))
    assert quem == [] and chat.reply.call_count == 0
    sp.fallback.send_message.assert_awaited_once()        # você fica sabendo por que o grupo calou


def test_janela_segue_quem_foi_chamado_primeiro():
    chat, sp = _chat(), _speakers()
    with patch("vegapunk.router.route", return_value=router.Routing(["shaka", "lilith"], "alta", "dois")):
        quem = asyncio.run(bot.responder_no_grupo(chat, sp, GRUPO, "Shaka e Lilith?", 7))
    assert quem == ["shaka", "lilith"]
    assert chat.active(GRUPO) == "shaka"                  # não o último que falou


def test_contexto_do_roteador_diz_quem_falou():
    chat, sp = _chat(), _speakers()
    chat.wake(GRUPO, "lilith")
    chat._save(GRUPO, "lilith", "user", "ataca isso")
    chat._save(GRUPO, "lilith", "assistant", "já ataquei")
    with patch("vegapunk.router.route", return_value=router.Routing(["lilith"], "alta", "x")) as r:
        asyncio.run(bot.responder_no_grupo(chat, sp, GRUPO, "e isso aí?", 7))
    recentes = r.call_args.kwargs["recent"]
    assert recentes == ["Fernando: ataca isso", "Lilith: já ataquei"]


# ── Story 1d: a captura fala pela boca do dono, o teclado sai pelo leitor ──
def test_no_grupo_o_resumo_sai_pelo_dono_e_o_teclado_pelo_leitor():
    """O clique de um botão volta para o bot que ENVIOU: teclado da Lilith seria botão morto."""
    sp = _speakers()
    sp.bot_for = MagicMock(side_effect=lambda sat, cid: MagicMock() if cid < 0 else sp.fallback)
    asyncio.run(bot.notificar(sp, GRUPO, "resumo do item", reply_to=5, item_id="abc123", sat="lilith",
                              titulo="Amostrando — avaliação completa"))
    assert sp.say_all.await_args.args[0] == "lilith"          # o dono resumiu
    kw = sp.fallback.send_message.await_args.kwargs
    assert kw["reply_markup"] is not None                     # e o leitor mandou os botões
    # com vários itens chegando fora de ordem, botões idênticos viram loteria: o título identifica
    assert "Amostrando" in sp.fallback.send_message.await_args.args[1]


def test_na_dm_nada_muda_uma_mensagem_so_com_teclado():
    sp = _speakers()
    sp.bot_for = MagicMock(return_value=sp.fallback)
    asyncio.run(bot.notificar(sp, 111, "resumo", reply_to=5, item_id="abc123", sat="lilith"))
    sp.say_all.assert_not_awaited()
    kw = sp.fallback.send_message.await_args.kwargs
    assert kw["reply_markup"] is not None and kw["reply_to_message_id"] == 5


def test_sem_item_id_nao_manda_teclado_nenhum():
    sp = _speakers()
    sp.bot_for = MagicMock(side_effect=lambda sat, cid: MagicMock())
    asyncio.run(bot.notificar(sp, GRUPO, "capturei o link", sat="atlas"))
    assert sp.say_all.await_args.args[0] == "atlas"
    sp.fallback.send_message.assert_not_awaited()


def test_titulo_longo_e_cortado_e_item_sem_titulo_tem_texto_neutro():
    assert "este item" in bot.triagem_linha(None)
    assert len(bot.triagem_linha("x" * 200)) < 120



def test_capture_py_aceita_o_contrato_atual_do_notify():
    """Regressão da v1.8.0: `notify` ganhou `sat`/`titulo` e o notificador do `scripts/capture.py`
    quebrou — ele é a SEGUNDA implementação do mesmo callback e nenhum teste cobria o script.
    Aqui basta ler a assinatura: importar o script puxa dependências que o teste não precisa."""
    import re
    from pathlib import Path
    fonte = (Path(__file__).parents[1] / "scripts/capture.py").read_text(encoding="utf-8")
    assinaturas = re.findall(r"async def (?:silent|notify)\(([^)]*)\)", fonte)
    assert assinaturas, "o notificador do capture.py sumiu"
    for a in assinaturas:
        assert "**kw" in a, f"assinatura sem **kw quebra no próximo campo novo: {a}"
