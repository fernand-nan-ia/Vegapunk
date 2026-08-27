"""URL → (platform, external_id, canonical_url). Sem rede, exceto resolução de shortlinks."""
import hashlib
import re
import urllib.request
from dataclasses import dataclass
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

YT_ID = r"([A-Za-z0-9_-]{11})"
YT_PATTERNS = [
    re.compile(r"youtu\.be/" + YT_ID),
    re.compile(r"youtube\.com/(?:shorts|embed|live|v)/" + YT_ID),
]
TT_VIDEO = re.compile(r"tiktok\.com/@[^/]+/(?:video|photo)/(\d+)")
TT_SHORT = re.compile(r"(?:vm|vt)\.tiktok\.com/([A-Za-z0-9]+)|tiktok\.com/t/([A-Za-z0-9]+)")
IG_PATTERN = re.compile(r"instagram\.com/(?:[^/]+/)?(?:reel|reels|p|tv)/([A-Za-z0-9_-]+)")

URL_RE = re.compile(r"https?://[^\s<>\"')\]]+")


@dataclass(frozen=True)
class Normalized:
    platform: str          # youtube | tiktok | instagram | article | document | other
    external_id: str | None
    canonical_url: str


def extract_urls(text: str) -> list[str]:
    seen, out = set(), []
    for u in URL_RE.findall(text or ""):
        u = u.rstrip(".,;")
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def resolve_redirect(url: str, timeout: float = 10) -> str:
    """Segue redirects de shortlinks (vm.tiktok.com etc.). Falha => devolve a própria URL."""
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.geturl()
    except Exception:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.geturl()
        except Exception:
            return url


def normalize_document(url: str) -> Normalized:
    """file:///caminho/arquivo.pdf → ('document', sha1 do conteúdo, mesma URL). Arquivo idêntico = duplicata."""
    from pathlib import Path
    path = Path(url.removeprefix("file://"))
    h = hashlib.sha1()
    try:
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
    except OSError:
        return Normalized("document", None, url)
    return Normalized("document", h.hexdigest()[:12], url)


def normalize(url: str, resolver=resolve_redirect) -> Normalized:
    if url.startswith("file://"):
        return normalize_document(url)
    host = (urlparse(url).hostname or "").lower()

    if "youtu" in host:
        parsed = urlparse(url)
        vid = parse_qs(parsed.query).get("v", [None])[0]
        if not vid:
            for p in YT_PATTERNS:
                m = p.search(url)
                if m:
                    vid = m.group(1)
                    break
        if vid and re.fullmatch(YT_ID, vid):
            return Normalized("youtube", vid, f"https://www.youtube.com/watch?v={vid}")
        return Normalized("other", None, url)   # canal/playlist: não é vídeo nem artigo

    if "tiktok" in host:
        if TT_SHORT.search(url):
            url = resolver(url)
        m = TT_VIDEO.search(url)
        if m:
            return Normalized("tiktok", m.group(1), url.split("?")[0])
        return Normalized("other", None, url)

    if "instagram" in host:
        m = IG_PATTERN.search(url)
        if m:
            code = m.group(1)
            kind = "reel" if "/reel" in url else "p"
            return Normalized("instagram", code, f"https://www.instagram.com/{kind}/{code}/")
        return Normalized("other", None, url)

    return normalize_article(url)


TRACKING_PARAMS = ("utm_", "fbclid", "gclid", "igsh", "si", "ref", "mc_cid", "mc_eid")


def normalize_article(url: str) -> Normalized:
    """Qualquer página http(s) que não é vídeo: artigo/post. id = hash da URL sem rastreadores."""
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        return Normalized("other", None, url)
    query = [(k, v) for k, v in parse_qs(parsed.query, keep_blank_values=True).items()
             if not k.lower().startswith(TRACKING_PARAMS)]
    clean = urlunparse((parsed.scheme, parsed.hostname.lower() + (f":{parsed.port}" if parsed.port else ""),
                        parsed.path.rstrip("/") or "/", "", urlencode(query, doseq=True), ""))
    return Normalized("article", hashlib.sha1(clean.encode()).hexdigest()[:12], clean)
