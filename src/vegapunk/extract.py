"""Extração de texto: legendas (yt-dlp) ou áudio → Whisper. Nunca guarda vídeo."""
import json
import logging
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from .config import settings

log = logging.getLogger("vegapunk.extract")


class ExtractionError(Exception):
    def __init__(self, code: str, detail: str, retryable: bool = False):
        super().__init__(f"{code}: {detail}")
        self.code, self.detail, self.retryable = code, detail[:2000], retryable


@dataclass
class Extracted:
    title: str
    channel: str
    duration: int | None
    description: str
    content_type: str   # transcript | caption | whisper
    text: str
    lang: str | None


# ── VTT ───────────────────────────────────────────────────────
_TS = re.compile(r"^\d{2}:\d{2}:\d{2}[.,]\d{3} --> .*$")
_TAGS = re.compile(r"<[^>]+>")


def clean_vtt(raw: str) -> str:
    lines, last = [], None
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")) or _TS.match(line) or line.isdigit():
            continue
        line = _TAGS.sub("", line).replace("&nbsp;", " ").strip()
        if not line or line == last:
            continue
        lines.append(line)
        last = line
    return re.sub(r"\s+", " ", " ".join(lines)).strip()


# ── yt-dlp ────────────────────────────────────────────────────
def _ytdlp(*args: str, timeout: int = 600) -> subprocess.CompletedProcess:
    cmd = ["yt-dlp", "--no-playlist", "--no-warnings", "--extractor-retries", "5", "--retry-sleep", "extractor:5"]
    if settings.cookies_file:
        cmd += ["--cookies", settings.cookies_file]
    cmd += list(args)
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def _classify(stderr: str) -> ExtractionError:
    s = stderr.lower()
    if "unsupported url" in s and "/photo/" in s or "no video formats found" in s:
        return ExtractionError("ERR-008", "post de imagens (slideshow/carrossel): sem áudio ou vídeo para transcrever", retryable=False)
    if any(k in s for k in ("private video", "video unavailable", "not available in your country", "removed", "login required", "requested content is not available")):
        return ExtractionError("ERR-005", stderr, retryable=False)
    return ExtractionError("ERR-003", stderr, retryable=True)


def fetch_metadata(url: str) -> dict:
    r = _ytdlp("-j", "--ignore-no-formats-error", url, timeout=120)
    if r.returncode != 0:
        raise _classify(r.stderr)
    try:
        return json.loads(r.stdout.splitlines()[0])
    except (json.JSONDecodeError, IndexError) as e:
        raise ExtractionError("ERR-003", f"json inválido do yt-dlp: {e}", retryable=True)


def _pick_sub_file(workdir: Path) -> tuple[Path, str] | None:
    """Prioridade: humana pt > humana en > auto pt > auto en (yt-dlp nomeia iguais; usamos ordem de idioma)."""
    files = sorted(workdir.glob("*.vtt"))
    for pref in ("pt", "en"):
        for f in files:
            lang = f.suffixes[-2].lstrip(".") if len(f.suffixes) >= 2 else ""
            if lang.startswith(pref):
                return f, lang.split("-")[0]
    return (files[0], "und") if files else None


def fetch_subtitles(url: str, workdir: Path) -> tuple[str, str] | None:
    r = _ytdlp(
        "--skip-download", "--write-subs", "--write-auto-subs",
        "--sub-langs", "pt,pt-BR,pt-PT,en,en-US,en-GB", "--sub-format", "vtt", "--sleep-subtitles", "1",
        "-o", str(workdir / "%(id)s.%(ext)s"), url,
    )
    picked = _pick_sub_file(workdir)
    if r.returncode != 0 and not picked:
        err = _classify(r.stderr)
        if not err.retryable:
            raise err
        log.warning("legenda indisponível, caindo para áudio: %s", r.stderr.strip()[-200:])
        return None
    if not picked:
        return None
    path, lang = picked
    return clean_vtt(path.read_text(encoding="utf-8", errors="ignore")), lang


def fetch_audio(url: str, workdir: Path) -> Path:
    r = _ytdlp("-f", "bestaudio/best", "-o", str(workdir / "audio.%(ext)s"), url)
    if r.returncode != 0:
        raise _classify(r.stderr)
    files = list(workdir.glob("audio.*"))
    if not files:
        raise ExtractionError("ERR-003", "yt-dlp não gerou arquivo de áudio", retryable=True)
    return files[0]


# ── Whisper ───────────────────────────────────────────────────
_whisper = None


def transcribe(audio: Path) -> tuple[str, str]:
    global _whisper
    from faster_whisper import WhisperModel  # import tardio: pesado

    if _whisper is None:
        log.info("carregando whisper model=%s", settings.whisper_model)
        _whisper = WhisperModel(settings.whisper_model, device="cpu", compute_type="int8")
    segments, info = _whisper.transcribe(str(audio), vad_filter=True)
    text = " ".join(s.text.strip() for s in segments)
    return re.sub(r"\s+", " ", text).strip(), info.language


# ── Orquestração ──────────────────────────────────────────────
def extract(url: str, platform: str, item_id: str) -> Extracted:
    workdir = settings.tmp_dir / item_id
    workdir.mkdir(parents=True, exist_ok=True)
    try:
        meta = fetch_metadata(url)
        title = meta.get("title") or meta.get("fulltitle") or url
        channel = meta.get("channel") or meta.get("uploader") or ""
        duration = int(meta["duration"]) if meta.get("duration") else None
        description = (meta.get("description") or "").strip()

        text, lang, ctype = "", None, ""
        has_subs = bool(meta.get("subtitles") or meta.get("automatic_captions"))
        if platform == "youtube" and has_subs:
            got = fetch_subtitles(url, workdir)
            if got:
                text, lang, ctype = got[0], got[1], "transcript"
        if len(text) < 200:
            audio = fetch_audio(url, workdir)
            text, lang = transcribe(audio)
            ctype = "whisper"
        if len(text) < 50 and description:
            text, ctype, lang = description, "caption", lang or "und"
        if len(text) < 50:
            raise ExtractionError("ERR-004", "conteúdo insuficiente (sem legenda, áudio ou descrição útil)")
        return Extracted(title, channel, duration, description[:3000], ctype, text[: settings.max_transcript_chars], lang)
    finally:
        shutil.rmtree(workdir, ignore_errors=True)
