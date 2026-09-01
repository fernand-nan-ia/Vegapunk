"""A cascata do grupo (PRD §4.1): quem responde, quem cala, e quanto custa cada decisão."""
from unittest.mock import MagicMock, patch

import pytest

from vegapunk import bot, router
from vegapunk.chat import Chat
from vegapunk.db import Database

GRUPO = -1002
DENTRO, FORA = router.WINDOW_SECONDS - 60, router.WINDOW_SECONDS + 60


@pytest.fixture(autouse=True)
def teto_limpo():
    router._recentes.clear()
    yield
    router._recentes.clear()


def _sem_roteador():
    """Patch que EXPLODE se a camada 3 for alcançada: prova custo zero."""
    return patch("vegapunk.router.route", side_effect=AssertionError("roteador não devia ter sido chamado"))


# ── camada 1: @menção não passa pelo roteador ───────────────────────────
def test_mencao_explicita_funciona_com_o_roteador_quebrado():
    """Caminho de escape determinístico: @menção decide sem gastar nada."""
    with _sem_roteador():
        r = router.decide("preciso de você", explicitos=["shaka"])
    assert r.satellites == ["shaka"] and r.confidence == "alta"


def test_mencao_respeita_o_teto_de_satelites():
    with _sem_roteador():
        r = router.decide("todos!", explicitos=list(router.satellites.IDS))
    assert len(r.satellites) == router.MAX_SATELLITES


def test_mencoes_explicitas_saem_das_entidades_na_ordem():
    users = {"lilith": "vegapunkklilithbot", "shaka": "vegapunkshakabot", "york": "vegapunkkyorkbot"}
    assert bot.mencoes_explicitas("@vegapunkshakabot e @vegapunkklilithbot, o que acham?", users) == ["shaka", "lilith"]
    assert bot.mencoes_explicitas("bom dia", users) == []
    assert bot.mencoes_explicitas("@VEGAPUNKKYORKBOT quanto custou?", users) == ["york"]


# ── camada 2: a peneira, nos dois modos ─────────────────────────────────
def test_com_triagem_desligada_sem_nome_nao_gasta_nada(monkeypatch):
    """Modo original: silêncio é grátis. Preservado atrás de VEGAPUNK_GROUP_TRIAGE=false."""
    monkeypatch.setattr(router.settings, "group_triage", False)
    with _sem_roteador():
        r = router.decide("bom dia", ativo="lilith", idade_do_ativo=FORA)
    assert r.satellites == [] and "custo zero" in r.reason
    with _sem_roteador():
        assert router.decide("bom dia").satellites == []


def test_com_triagem_ligada_sem_nome_o_roteador_escolhe_o_dono(monkeypatch):
    """Pedido do Fernando 2026-08-28: sem nome, quem responde é escolhido pelo ASSUNTO."""
    monkeypatch.setattr(router.settings, "group_triage", True)
    with patch("vegapunk.router.route", return_value=router.Routing(["shaka"], "alta", "LGPD é dele")) as r:
        got = router.decide("o que a LGPD exige de mim?")
    assert got.satellites == ["shaka"]
    assert r.call_args.kwargs["triagem"] is True        # modo triagem, não modo destinatário
    assert r.call_args.kwargs["active"] is None


def test_triagem_ainda_pode_calar(monkeypatch):
    """Recado, 'ok', 'kkk': o roteador continua podendo devolver lista vazia."""
    monkeypatch.setattr(router.settings, "group_triage", True)
    with patch("vegapunk.router.route", return_value=router.Routing([], "alta", "não pede resposta")):
        assert router.decide("kkk").satellites == []


def test_especialidades_saem_do_md_do_satelite_nao_de_copia_no_router():
    """Regra do projeto: o `.md` do agente é a fonte da verdade. Havia um dicionário paralelo aqui,
    e ele JÁ tinha divergido (o York do router falava de preço; o do .md, de healthcheck)."""
    esp = router.especialidades()
    assert set(esp) == set(router.satellites.IDS)
    for i in router.satellites.IDS:
        foco = router.satellites.load(i).data["persona"]["focus"]
        assert esp[i] and esp[i] in foco          # veio do arquivo, não de uma cópia
    prompt = router.system_prompt(triagem=True)
    assert "MODO TRIAGEM" in prompt and len(prompt) < 3000     # continua barato


def test_triagem_corta_em_um_dono(monkeypatch):
    """Produção 2026-08-28: o prompt dizia 'UM só' e vieram 3 respostas de ~55k tokens cada."""
    def _resp(*a, **k):
        m = MagicMock(); m.choices = [MagicMock()]
        m.choices[0].message.content = '{"satellites":["shaka","pythagoras","york"],"confidence":"alta","reason":"tres"}'
        m.usage = MagicMock(prompt_tokens=1, completion_tokens=1)
        return m
    with patch("vegapunk.router._client") as c:
        c.return_value.chat.completions.create.side_effect = _resp
        assert router.route("e a LGPD?", triagem=True).satellites == ["shaka"]        # teto 1
        assert router.route("Shaka e Lilith?").satellites == ["shaka", "pythagoras", "york"]  # teto 3


# ── janela de continuidade de 10 minutos ────────────────────────────────
def test_dentro_da_janela_o_ultimo_continua_respondendo():
    with patch("vegapunk.router.route", return_value=router.Routing(["lilith"], "alta", "continuação")) as r:
        got = router.decide("e isso aí?", ativo="lilith", idade_do_ativo=DENTRO)
    assert got.satellites == ["lilith"]
    assert r.call_args.kwargs["active"] == "lilith"      # o roteador recebe o contexto da janela


def test_fora_da_janela_o_ativo_nao_e_oferecido_ao_roteador():
    """Aos 11 min a mensagem sem nome nem chega ao roteador; com nome, chega sem 'ativo'."""
    with patch("vegapunk.router.route", return_value=router.Routing([], "alta", "x")) as r:
        router.decide("Shaka, e aí?", ativo="lilith", idade_do_ativo=FORA)
    assert r.call_args.kwargs["active"] is None


def test_nome_de_outro_dentro_da_janela_troca_o_interlocutor():
    with patch("vegapunk.router.route", return_value=router.Routing(["shaka"], "alta", "trocou")):
        r = router.decide("Shaka, o que você acha?", ativo="lilith", idade_do_ativo=DENTRO)
    assert r.satellites == ["shaka"]


def test_janela_sai_do_chat_state(tmp_path):
    """`Chat.active_age` é a fonte da janela: mede a última interação real."""
    c = Chat(Database(":memory:"))
    assert c.active_age(GRUPO) == (None, None)
    c.wake(GRUPO, "lilith")
    sat, idade = c.active_age(GRUPO)
    assert sat == "lilith" and idade is not None and idade < 5


# ── camada 3: teto de rajada (achado 8 da Lilith) ───────────────────────
def test_teto_de_chamadas_por_minuto_falha_fechado():
    def _resp(*a, **k):
        m = MagicMock(); m.choices = [MagicMock()]
        m.choices[0].message.content = '{"satellites":["shaka"],"confidence":"alta","reason":"ok"}'
        m.usage = MagicMock(prompt_tokens=1, completion_tokens=1)
        return m
    with patch("vegapunk.router._client") as c:
        c.return_value.chat.completions.create.side_effect = _resp
        for _ in range(router.MAX_ROUTES_PER_MIN):
            assert router.route("Shaka?").satellites == ["shaka"]
        estourou = router.route("Shaka?")                 # a de número 21
    assert estourou.satellites == [] and "teto" in estourou.reason


# ── estrutura: a camada 2 é impossível de pular (achado 7 da Lilith) ────
def test_bot_nao_chama_o_roteador_direto():
    """Enquanto compor as camadas fosse tarefa do chamador, alguém pularia mentions() e pagaria à toa."""
    fonte = open(bot.__file__, encoding="utf-8").read()
    assert "router.decide(" in fonte
    assert "router.route(" not in fonte


# ── consertos do *verify da Lilith na Story 1c ─────────────────────────
def test_teto_da_camada_cara_e_o_que_segura_o_dinheiro():
    """ALTO: 20 roteadores/min autorizavam 60 respostas/min — 1,5 milhão de tokens. O teto tem de ser aqui."""
    router._respostas.clear()
    assert all(router.pode_responder() for _ in range(router.MAX_REPLIES_PER_MIN))
    assert router.pode_responder() is False
    router._respostas.clear()


def test_mencao_funciona_com_o_bot_daquele_satelite_fora_do_ar():
    """MÉDIO-ALTO: em 2026-08-28 a Lilith não respondeu ao get_me; sem isto o grupo ignorava o Fernando."""
    so_o_shaka = {"shaka": "vegapunkshakabot"}
    assert bot.mencoes_explicitas("@vegapunkklilithbot socorro", so_o_shaka) == ["lilith"]
    assert bot.mencoes_explicitas("@vegapunkshakabot e @vegapunkkyorkbot", so_o_shaka) == ["shaka", "york"]
    assert bot.mencoes_explicitas("@alguem_qualquer_bot oi", so_o_shaka) == []


def test_teto_por_hora_calibrado_pela_york():
    """York 2026-08-31: 60/h autorizava US$ 23,76/dia de descontrole contra US$ 0,33 de uso real."""
    router._respostas.clear()
    assert router.MAX_REPLIES_PER_HOUR == 25 and router.MAX_REPLIES_PER_MIN == 6
    agora = __import__("time").monotonic()
    router._respostas.extend([agora - 120] * router.MAX_REPLIES_PER_HOUR)   # cheio na hora, vazio no minuto
    assert router.pode_responder() is False
    router._respostas.clear()


def test_pipeline_tem_teto_de_itens_em_paralelo():
    """ALTO da Lilith 2026-08-31: 30 links colados disparavam 30 pipelines juntos — Whisper e 429."""
    from vegapunk.pipeline import MAX_PARALELO, Pipeline
    from unittest.mock import AsyncMock
    p = Pipeline(Database(":memory:"), AsyncMock())
    assert MAX_PARALELO == 3 and p._vaga._value == MAX_PARALELO
