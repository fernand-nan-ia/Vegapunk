from pathlib import Path
import pytest
from vegapunk import extract as ex
from vegapunk.enrich import EnrichmentError

URL = "https://www.tiktok.com/@orbitt.ia/photo/7672502144024595732"
DATA = {"desc": "Cinco sites\n#design", "author": {"nickname": "Orbit"}, "music": {"original": False, "duration": 34},
        "imagePost": {"images": [{"imageURL": {"urlList": ["https://cdn/1.jpg"]}}, {"imageURL": {"urlList": ["https://cdn/2.jpg"]}}]}}


def test_slides_happy_path(monkeypatch, tmp_path):
    calls = {}
    monkeypatch.setattr(ex, "_tiktok_web_data", lambda u, v: calls.setdefault("url", u) and DATA)
    monkeypatch.setattr(ex, "_download_images", lambda urls: [b"a", b"b"])
    monkeypatch.setattr("vegapunk.enrich.read_slides", lambda blobs: "[Slide 1]\nPicular\n[Slide 2]\nGlyphs")
    monkeypatch.setattr(ex, "fetch_audio", lambda *a: pytest.fail("não deve transcrever música de biblioteca"))
    r = ex.extract_tiktok_slides(URL, tmp_path)
    assert calls["url"].endswith("/video/7672502144024595732")
    assert r.content_type == "slides" and r.title == "Cinco sites" and r.channel == "Orbit"
    assert r.text.startswith("[SLIDES: 2]") and "Glyphs" in r.text and "NARRAÇÃO" not in r.text


def test_slides_with_original_audio_narration(monkeypatch, tmp_path):
    monkeypatch.setattr(ex, "_tiktok_web_data", lambda u, v: {**DATA, "music": {"original": True, "duration": 34}})
    monkeypatch.setattr(ex, "_download_images", lambda urls: [b"a", b"b"])
    monkeypatch.setattr("vegapunk.enrich.read_slides", lambda blobs: "[Slide 1]\ntexto")
    monkeypatch.setattr(ex, "fetch_audio", lambda *a: Path("x.m4a"))
    monkeypatch.setattr(ex, "transcribe", lambda p: ("narração falada com mais de cinquenta caracteres de conteúdo real", "pt"))
    r = ex.extract_tiktok_slides(URL, tmp_path)
    assert "[NARRAÇÃO/ÁUDIO]" in r.text and r.lang == "pt"


def test_slides_no_images_is_err008(monkeypatch, tmp_path):
    monkeypatch.setattr(ex, "_tiktok_web_data", lambda u, v: {"imagePost": {"images": []}})
    with pytest.raises(ex.ExtractionError) as e:
        ex.extract_tiktok_slides(URL, tmp_path)
    assert e.value.code == "ERR-008" and not e.value.retryable


def test_slides_web_data_failure_is_retryable(monkeypatch, tmp_path):
    def boom(u, v): raise RuntimeError("403")
    monkeypatch.setattr(ex, "_tiktok_web_data", boom)
    with pytest.raises(ex.ExtractionError) as e:
        ex.extract_tiktok_slides(URL, tmp_path)
    assert e.value.code == "ERR-003" and e.value.retryable


def test_slides_vision_rate_limit_is_retryable(monkeypatch, tmp_path):
    monkeypatch.setattr(ex, "_tiktok_web_data", lambda u, v: DATA)
    monkeypatch.setattr(ex, "_download_images", lambda urls: [b"a", b"b"])
    def boom(blobs): raise EnrichmentError("ERR-006", "rate limit")
    monkeypatch.setattr("vegapunk.enrich.read_slides", boom)
    with pytest.raises(ex.ExtractionError) as e:
        ex.extract_tiktok_slides(URL, tmp_path)
    assert e.value.retryable


def test_extract_routes_photo_urls(monkeypatch, tmp_path):
    monkeypatch.setattr(ex.settings, "tmp_dir", tmp_path)
    monkeypatch.setattr(ex, "extract_tiktok_slides", lambda url, wd: "ROUTED")
    monkeypatch.setattr(ex, "fetch_metadata", lambda u: pytest.fail("não deve usar caminho de vídeo"))
    assert ex.extract(URL, "tiktok", "item1") == "ROUTED"
