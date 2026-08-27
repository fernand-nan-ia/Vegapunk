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
    n = normalize("https://akitaonrails.com/2026/07/30/novo-llm-benchmark-refiz-todos-os-testes/?utm_source=tg&ref=x#topo")
    assert n.platform == "article" and len(n.external_id) == 12
    assert n.canonical_url == "https://akitaonrails.com/2026/07/30/novo-llm-benchmark-refiz-todos-os-testes"
    # mesma página com/sem rastreadores => mesmo id (duplicata detectada)
    assert normalize("https://akitaonrails.com/2026/07/30/novo-llm-benchmark-refiz-todos-os-testes").external_id == n.external_id

def test_other_only_for_unparseable_video_urls():
    assert normalize("https://www.youtube.com/@canal").platform == "other"

def test_extract_urls_dedup():
    assert extract_urls("veja https://a.com/x, e https://a.com/x e https://b.com.") == ["https://a.com/x", "https://b.com"]
