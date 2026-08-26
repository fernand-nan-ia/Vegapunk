from vegapunk.extract import clean_vtt

VTT = """WEBVTT
Kind: captions
Language: pt

00:00:00.000 --> 00:00:02.000 align:start position:0%
olá<00:00:01.000><c> pessoal</c>

00:00:02.000 --> 00:00:04.000
olá pessoal
hoje vamos falar

00:00:04.000 --> 00:00:06.000
hoje vamos falar
de rails
"""

def test_clean_vtt_removes_timestamps_tags_and_dupes():
    assert clean_vtt(VTT) == "olá pessoal hoje vamos falar de rails"


def test_classify_image_posts_not_retryable():
    from vegapunk.extract import _classify
    e = _classify("ERROR: Unsupported URL: https://www.tiktok.com/@x/photo/123")
    assert e.code == "ERR-008" and not e.retryable
    e = _classify("ERROR: [Instagram] abc: No video formats found!")
    assert e.code == "ERR-008" and not e.retryable
    assert _classify("ERROR: [TikTok] 1: Unable to download webpage: HTTP Error 403").retryable
