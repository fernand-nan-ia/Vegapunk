from vegapunk.normalize import extract_urls, normalize

def test_youtube_formats_same_id():
    urls = ["https://youtu.be/6DJFl-g83dM?si=abc", "https://www.youtube.com/watch?v=6DJFl-g83dM&t=42",
            "https://www.youtube.com/shorts/6DJFl-g83dM", "https://www.youtube.com/embed/6DJFl-g83dM"]
    for u in urls:
        n = normalize(u)
        assert (n.platform, n.external_id, n.canonical_url) == ("youtube", "6DJFl-g83dM", "https://www.youtube.com/watch?v=6DJFl-g83dM")

def test_tiktok_short_resolves():
    n = normalize("https://vm.tiktok.com/ZMabc123/", resolver=lambda u: "https://www.tiktok.com/@user/video/7300000000000000000?x=1")
    assert (n.platform, n.external_id) == ("tiktok", "7300000000000000000")
    assert "?" not in n.canonical_url

def test_instagram_reel():
    n = normalize("https://www.instagram.com/reel/C9abcDEF12/?igsh=xyz")
    assert (n.platform, n.external_id, n.canonical_url) == ("instagram", "C9abcDEF12", "https://www.instagram.com/reel/C9abcDEF12/")

def test_article_any_web_page():
    n = normalize("https://akitaonrails.com/2026/07/30/novo-llm-benchmark-refiz-todos-os-testes/?utm_source=tg&fbclid=x#topo")
    assert n.platform == "article" and len(n.external_id) == 12
    assert n.canonical_url == "https://akitaonrails.com/2026/07/30/novo-llm-benchmark-refiz-todos-os-testes"
    # mesma página com/sem rastreadores => mesmo id (duplicata detectada)
    assert normalize("https://akitaonrails.com/2026/07/30/novo-llm-benchmark-refiz-todos-os-testes").external_id == n.external_id

def test_other_only_for_unparseable_video_urls():
    assert normalize("https://www.youtube.com/@canal").platform == "other"

def test_extract_urls_dedup():
    assert extract_urls("veja https://a.com/x, e https://a.com/x e https://b.com.") == ["https://a.com/x", "https://b.com"]

def test_same_page_from_two_ads_is_one_item():
    """Bug de 07/09: gad_source/gad_campaignid/gbraid sobreviviam ao sha1 e a mesma página
    vinda de dois anúncios entrava como dois itens no vault."""
    base = "https://www.hostinger.com/br/tutoriais/como-vender-um-site"
    anuncio1 = base + "?gad_source=1&gad_campaignid=20417074995&gbraid=0AAAAADMy"
    anuncio2 = base + "?gad_source=5&gad_campaignid=99999999999&wbraid=XYZ&msclkid=abc&ttclid=def"
    ids = {normalize(u).external_id for u in (base, anuncio1, anuncio2)}
    assert len(ids) == 1
    assert normalize(anuncio1).canonical_url == base


def test_tracking_match_is_exact_not_prefix():
    """"si" não pode engolir "site" nem "ref" engolir "refresh": isso fundiria páginas DIFERENTES
    no mesmo id, que é pior que duplicata."""
    a = normalize("https://exemplo.com/doc?site=br&refresh=1")
    b = normalize("https://exemplo.com/doc?site=pt&refresh=1")
    assert a.external_id != b.external_id
    assert "site=br" in a.canonical_url and "refresh=1" in a.canonical_url
    # e o rastreador de nome exato continua caindo fora
    assert normalize("https://exemplo.com/doc?site=br&refresh=1&si=xyz&fbclid=tg").external_id == a.external_id


def test_ad_platform_ids_are_content_not_tracking():
    """Lilith, verify de 12/09: campaignid/adid dentro de plataforma de anúncio é CONTEÚDO.
    Derrubá-los fundiria duas campanhas diferentes num item só — pior que duplicata."""
    a = normalize("https://ads.google.com/campanha?campaignid=20417074995")
    b = normalize("https://ads.google.com/campanha?campaignid=99999999999")
    assert a.external_id != b.external_id
    # e o ?ref= do GitHub é o branch, não rastreador
    assert normalize("https://github.com/u/r/blob/x.py?ref=main").external_id != \
           normalize("https://github.com/u/r/blob/x.py?ref=dev").external_id


def test_param_order_does_not_create_two_items():
    assert normalize("https://x.com/a?b=2&a=1").external_id == normalize("https://x.com/a?a=1&b=2").external_id
