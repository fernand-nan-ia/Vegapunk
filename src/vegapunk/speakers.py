"""Os outros Satélites como bots que só FALAM: sem polling, sem handler, só `send_message`.

Decisão de projeto (Atlas, 2026-08-28) — a Story 1b previa uma `Application` por token. Uma
`Application` existe para RECEBER: traz Updater, fila de updates e laço de polling. Os seis que
apenas publicam não recebem nada, então usam `telegram.Bot` puro. Duas consequências boas:

  1. um laço de polling (o do Stella) em vez de sete;
  2. o critério "os outros não registram handler" vira **estrutural** — num `Bot` não existe
     onde registrar. Deixa de ser uma regra que alguém precisa lembrar de respeitar.

Quem lê o grupo continua sendo só o Stella (privacy mode OFF nele, ON nos outros seis).
"""
import asyncio
import logging

from telegram import Bot
from telegram.constants import ParseMode

from . import satellites
from .config import settings

log = logging.getLogger("vegapunk.speakers")

READER = satellites.DEFAULT   # stella: o único que recebe updates


def tokens() -> dict[str, str]:
    """Tokens do `.env` que correspondem a um Satélite real, sem o leitor (que já tem Application)."""
    desconhecidos = [k for k in settings.bot_tokens if k not in satellites.IDS]
    if desconhecidos:
        log.warning("TELEGRAM_BOT_TOKEN_* com nome que não é Satélite (ignorados): %s", desconhecidos)
    return {k: v for k, v in settings.bot_tokens.items() if k in satellites.IDS and k != READER}


class Speakers:
    """Registro dos bots que publicam. `fallback` é o bot do leitor: usado na DM e quando falta token."""

    def __init__(self, fallback: Bot):
        self.fallback = fallback
        self.bots: dict[str, Bot] = {}
        self.usernames: dict[str, str] = {}

    async def _subir(self, sat_id: str, token: str, tentativa: int) -> None:
        bot = Bot(token)
        try:
            await bot.initialize()
            me = await bot.get_me()
        except Exception as e:                        # token errado, revogado, ou rede piscando
            log.warning("bot de %s não subiu na tentativa %s (%s: %s)",
                        sat_id, tentativa, type(e).__name__, str(e)[:120])
            try:
                await bot.shutdown()                  # `initialize` pode ter passado e aberto o pool httpx
            except Exception:
                pass
            return
        self.bots[sat_id] = bot
        self.usernames[sat_id] = me.username or ""
        log.info("bot de %s pronto: @%s", sat_id, me.username)

    async def initialize(self) -> dict[str, str]:
        """Sobe um `Bot` por token e confirma a identidade de cada um no Telegram (`get_me`).

        Em PARALELO: são 6 chamadas de rede e o polling do leitor não começa antes disto terminar —
        sequencial custava ~17 s de bot fora do ar a cada restart.

        Com UMA segunda chance: o `TimedOut` do Telegram é intermitente conhecido neste projeto, e sem
        repique um piscar de rede aposentaria aquele Satélite até o próximo restart.

        Token ausente, inválido ou que falhou duas vezes não derruba nada: aquele Satélite fala pela
        boca do leitor.
        """
        pendentes = tokens()
        for tentativa in (1, 2):
            if not pendentes:
                break
            await asyncio.gather(*(self._subir(s, tk, tentativa) for s, tk in pendentes.items()))
            pendentes = {s: tk for s, tk in pendentes.items() if s not in self.bots}
            if pendentes and tentativa == 1:
                log.info("segunda chance para: %s", sorted(pendentes))
        faltando = [i for i in satellites.IDS if i != READER and i not in self.bots]
        if faltando:
            log.warning("Satélites sem bot próprio (falam pelo %s): %s", READER, faltando)
        return dict(self.usernames)

    async def shutdown(self):
        for sat_id, bot in self.bots.items():
            try:
                await bot.shutdown()
            except Exception:
                log.warning("falha ao desligar o bot de %s", sat_id)

    def bot_for(self, sat_id: str, chat_id: int) -> Bot:
        """Em GRUPO cada Satélite fala pelo próprio bot (nome e ícone dele na conversa).

        Na DM, sempre o leitor: um bot não pode escrever para alguém que nunca abriu conversa com ele.
        """
        if chat_id < 0 and sat_id in self.bots:
            return self.bots[sat_id]
        return self.fallback

    async def _enviar(self, bot: Bot, sat_id: str, chat_id: int, text: str, **kw) -> Bot:
        """Envia e devolve o bot que REALMENTE falou (pode ter caído para o leitor)."""
        try:
            await bot.send_message(chat_id, text, **kw)
            return bot
        except Exception:
            if bot is self.fallback:
                raise
            log.exception("bot de %s falhou ao enviar; caindo para o %s", sat_id, READER)
            # sem `reply_to_message_id`: se a mensagem original sumiu, ela é a causa da falha e
            # repetir o mesmo kwarg faria o leitor falhar igual — a resposta já foi paga, não pode sumir
            kw.pop("reply_to_message_id", None)
            await self.fallback.send_message(chat_id, text, **kw)
            return self.fallback

    async def say(self, sat_id: str, chat_id: int, text: str, **kw):
        """Uma mensagem, como o Satélite dono. Falha do bot dele cai para o leitor."""
        kw.setdefault("parse_mode", ParseMode.HTML)
        await self._enviar(self.bot_for(sat_id, chat_id), sat_id, chat_id, text, **kw)

    async def say_all(self, sat_id: str, chat_id: int, parts: list[str], reply_to: int | None = None, **kw):
        """Uma resposta inteira pela MESMA boca.

        Decidir por pedaço deixaria uma fala longa metade com a cara de um Satélite e metade com a
        de outro — se o primeiro pedaço caiu para o leitor, o resto vai com ele também.
        """
        kw.setdefault("parse_mode", ParseMode.HTML)
        bot = self.bot_for(sat_id, chat_id)
        for i, part in enumerate(parts):
            bot = await self._enviar(bot, sat_id, chat_id, part,
                                     reply_to_message_id=reply_to if i == 0 else None, **kw)
