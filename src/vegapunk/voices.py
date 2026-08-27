"""Falas curtas dos Satélites para as mensagens automáticas do bot (captura, duplicata, erros).

Zero tokens: são templates. A voz do RESULTADO (resumo) vem do enriquecimento (`satellite` + `satellite_take`).
Fonte das personalidades: .claude/commands/vegapunk/agents/<id>.md — estas linhas só ecoam o tom de lá.
"""
import random

ICON = {"stella": "🧠", "shaka": "🪖", "lilith": "🏴‍☠️", "edison": "💡", "pythagoras": "📚", "atlas": "🔧", "york": "🍩"}
PUNK = {"stella": "Stella", "shaka": "Punk-01", "lilith": "Punk-02", "edison": "Punk-03", "pythagoras": "Punk-04",
        "atlas": "Punk-05", "york": "Punk-06"}
NAME = {"stella": "Stella", "shaka": "Shaka", "lilith": "Lilith", "edison": "Edison", "pythagoras": "Pythagoras",
        "atlas": "Atlas", "york": "York"}

# {n} = quantidade de links; {s} = "s" se plural
CAPTURE = {
    "stella": ["Kwahaha! {n} amostra{s} nova{s} para o Punk Records. Sincronizando com a cabeça lá em cima…",
               "Alô, alô, teste, teste — {n} link{s} recebido{s}. A ciência começa agora, Quasar."],
    "shaka": ["{n} item{s} na mesa. Compreender primeiro, julgar depois — aguarde o veredito.",
              "Recebido. {n} fonte{s}; ainda não é evidência, ainda não é anúncio. Analisando."],
    "lilith": ["{n} navio{s} no horizonte. Baixando os óculos — vamos ver quanto aguenta{m} de pancada.",
               "Subindo no Vegaforce. {n} link{s}; se sobrar alguma coisa, é porque presta."],
    "edison": ["Orelha subiu! {n} faísca{s} nova{s}. Deixa eu ver o que dá para juntar com o que já temos…",
               "Eureka — ainda não, mas {n} link{s} chegou{aram}. Motor ligado."],
    "pythagoras": ["Registrando {n} entrada{s}. O registro vem primeiro; a dedução, marcada, depois.",
                   "{n} fonte{s} nova{s}. Vejamos se converge com o que o Punk Records já guarda."],
    "atlas": ["Passo 1 de 3: {n} link{s} na bancada. Extrair, resumir, guardar. Sai da frente.",
              "Grr, mais trabalho — bom. {n} peça{s} para desmontar. Já volto com os parafusos."],
    "york": ["Bocejo. {n} link{s}. Isso vai custar uma coxinha, talvez duas. Processando, patrão.",
             "Hmm? {n} item{s}. Vou contar cada token; depois você me diz se valeu o lanche."],
}

DUPLICATE = ["📚 <b>Pythagoras</b> · Punk-04: já há registro disso — capturado em {date} (x{count}). Status: {status}. O registro diz; eu não repito.",
             "🪖 <b>Shaka</b> · Punk-01: item já julgado em {date} (x{count}), status {status}. Não há veredito novo sem fonte nova."]

UNSUPPORTED = "🧠 <b>Stella</b> · Stella: essa plataforma ainda não passa pelo Fabriophase. Salvei o link em _pending/ — cole o texto em 'Notas manuais' e mande /reprocess {id}."
SLIDES = ("📷 <b>Atlas</b> · Punk-05: post de imagens sem áudio nem vídeo — nada para eu transcrever. Link salvo em _pending/. "
          "Cole o texto das imagens em 'Notas manuais' e mande /reprocess {id}. Passo 1 de 1.")
EXTRACT_FAILED = ("🔧 <b>Atlas</b> · Punk-05: Grr. Não consegui extrair o conteúdo ({code}). Link salvo em _pending/. "
                  "Cole o texto em 'Notas manuais' e mande /reprocess {id} — aí eu solda.")
ENRICH_FAILED = ("🍩 <b>York</b> · Punk-06: extraí o conteúdo, mas o resumo falhou ({code}) — token gasto, experimento pela metade. "
                 "Mande /reprocess {id} depois.")
CRASH = "💥 <b>Lilith</b> · Punk-02: afundou de um jeito que eu não previ (item {id}). Está nos logs; eu avisei que ia quebrar, só não sabia quando."


def pick(rng: random.Random | None = None) -> str:
    """Sorteia quem assume o lote: quem anuncia a captura é quem apresenta o resultado."""
    return (rng or random).choice(list(CAPTURE))


def speaker(sat: str) -> str:
    """Cabeçalho inequívoco: ícone + nome + Punk-NN."""
    return f"{ICON[sat]} <b>{NAME[sat]}</b> · {PUNK[sat]}"


def capture_line(n: int, sat: str | None = None, rng: random.Random | None = None) -> str:
    rng = rng or random
    sat = sat or pick(rng)
    tpl = rng.choice(CAPTURE[sat])
    plural = n != 1
    text = tpl.format(n=n, s="s" if plural else "", m="m" if plural else "", aram="aram" if plural else "")
    return f"{speaker(sat)}: {text}"


def duplicate_line(date: str, count: int, status: str, rng: random.Random | None = None, sat: str | None = None) -> str:
    """Se o lote tem dono (sat), é ele quem avisa — quem anuncia, apresenta. Sem dono: Pythagoras/Shaka."""
    if sat in ICON:
        return (f"{speaker(sat)}: esse link já está no Punk Records — capturado em {date} (x{count}), status {status}. "
                f"Nada novo para apresentar; esse fica por aqui.")
    return (rng or random).choice(DUPLICATE).format(date=date, count=count, status=status)


def failure_line(kind: str, item_id: str, code: str = "", sat: str | None = None) -> str:
    """kind: unsupported | slides | extract | enrich | crash. Com dono do lote, o dono fala; senão, o template de personagem."""
    tpl = {"unsupported": UNSUPPORTED, "slides": SLIDES, "extract": EXTRACT_FAILED, "enrich": ENRICH_FAILED, "crash": CRASH}[kind]
    if sat in ICON and kind != "crash":
        body = tpl.split(": ", 1)[1]  # tira o cabeçalho do personagem-padrão, mantém a instrução
        return f"{speaker(sat)}: {body}".format(id=item_id, code=code)
    return tpl.format(id=item_id, code=code)
