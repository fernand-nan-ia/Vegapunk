"""Orquestra um item do início ao fim. Extração e enriquecimento são serializados (locks)."""
import asyncio
import json
import logging
import time

from . import vault
from .db import Database
from .enrich import EnrichmentError, enrich
from .extract import ExtractionError, extract
from .normalize import normalize

log = logging.getLogger("vegapunk.pipeline")

extract_lock = asyncio.Lock()
enrich_lock = asyncio.Lock()
MAX_RETRIES = 6


LEVEL_ICON = {"alta": "🟢", "media": "🟡", "baixa": "🟠", "nenhuma": "⚪"}


def format_summary(e: dict, limit: int = 3900) -> str:
    """Mensagem Telegram (HTML) do resumo enriquecido. Seções opcionais só aparecem se houver conteúdo."""
    a = e["applicability"]
    parts = [f"🧠 <b>{esc(e['title'])}</b>", "", esc(e["summary"])]
    if e.get("topics"):
        parts += ["", "📚 <b>Tópicos</b>"]
        parts += [f"• <b>{esc(t['name'])}</b> — {esc(t['detail'])}" for t in e["topics"]]
    if e.get("tools"):
        parts += ["", "🛠 <b>Ferramentas citadas</b>"]
        parts += [f"• <b>{esc(t['name'])}</b>: {esc(t['role'])}" for t in e["tools"]]
    if e.get("key_points"):
        parts += ["", "✅ <b>Pontos-chave</b>"]
        parts += [f"• {esc(p)}" for p in e["key_points"][:6]]
    if e.get("how_to_apply"):
        parts += ["", f"💡 <b>Como aplicar:</b> {esc(e['how_to_apply'])}"]
    parts += ["",
              f"📌 SaaS {LEVEL_ICON.get(a['saas_pessoal'], '')} {a['saas_pessoal']} · "
              f"Cliente {LEVEL_ICON.get(a['projeto_cliente'], '')} {a['projeto_cliente']} · "
              f"Estudo {LEVEL_ICON.get(a['estudo_geral'], '')} {a['estudo_geral']}",
              f"🎯 Confiança: {e['confidence']}",
              f"🏷 {esc(' '.join('#' + t.replace('-', '_') for t in e['tags']))}"]
    text = "\n".join(parts)
    if len(text) > limit:
        # corta no fim de uma linha para não quebrar tag HTML
        text = text[:limit].rsplit("\n", 1)[0] + "\n…"
    return text


class Pipeline:
    def __init__(self, db: Database, notify):
        """notify(chat_id, text, reply_to=None, item_id=None) -> awaitable. item_id != None => teclado de triagem."""
        self.db = db
        self.notify = notify

    async def run(self, item_id: str):
        try:
            item = self.db.get(item_id)
            if item["status"] == "captured":
                item_id = await self.step_normalize(item_id)
                if item_id is None:
                    return
            item = self.db.get(item_id)
            if item["status"] == "normalized":
                if not await self.step_extract(item_id):
                    return
            item = self.db.get(item_id)
            if item["status"] == "extracted":
                if not await self.step_enrich(item_id):
                    return
            await self.step_persist(item_id)
        except Exception:
            log.exception("pipeline falhou item=%s", item_id)
            item = self.db.get(item_id)
            await self.notify(item["telegram_chat_id"], f"💥 Erro inesperado no item {item_id[:8]}. Veja os logs.")

    # ── etapas ──────────────────────────────────────────────
    async def step_normalize(self, item_id: str) -> str | None:
        item = self.db.get(item_id)
        n = await asyncio.to_thread(normalize, item["raw_url"])
        if n.external_id:
            dup = self.db.find_by_external(n.platform, n.external_id)
            if dup and dup["id"] != item_id:
                self.db.bump_shared(dup["id"])
                self.db.transition_to(item_id, "duplicate", "normalize_job", {"of": dup["id"]},
                                      platform=n.platform, external_id=None, canonical_url=n.canonical_url)
                await self.notify(item["telegram_chat_id"],
                                  f"♻️ Já capturado em {dup['captured_at'][:10]} (x{dup['shared_count'] + 1}). Status: {dup['status']}.",
                                  reply_to=item["telegram_message_id"])
                return None
        self.db.transition_to(item_id, "normalized", "normalize_job", {},
                              platform=n.platform, external_id=n.external_id or item_id[:8],
                              canonical_url=n.canonical_url)
        return item_id

    async def step_extract(self, item_id: str) -> bool:
        item = self.db.get(item_id)
        if item["platform"] == "other":
            return await self._pending(item_id, "ERR-002", "plataforma não suportada")
        t0 = time.time()
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                async with extract_lock:
                    ex = await asyncio.to_thread(extract, item["canonical_url"], item["platform"], item_id)
                self.db.transition_to(item_id, "extracted", "extract_job",
                                      {"content_type": ex.content_type, "chars": len(ex.text), "ms": int((time.time() - t0) * 1000)},
                                      title=ex.title, channel=ex.channel, duration=ex.duration, description=ex.description,
                                      content_type=ex.content_type, raw_content=ex.text, content_lang=ex.lang,
                                      extracted_at=vault_now(), error_code=None, error_detail=None)
                return True
            except ExtractionError as e:
                log.warning("extração item=%s tentativa=%s %s", item_id, attempt, e)
                if not e.retryable or attempt == MAX_RETRIES:
                    return await self._pending(item_id, e.code, e.detail)
                await asyncio.sleep(15 * attempt)
            except Exception as e:
                log.exception("extração crash item=%s", item_id)
                return await self._pending(item_id, "ERR-003", str(e))
        return False

    async def _pending(self, item_id: str, code: str, detail: str) -> bool:
        item = self.db.get(item_id)
        status = "extraction_failed" if code in ("ERR-003", "ERR-004", "ERR-005", "ERR-008") else "pending_manual"
        self.db.transition_to(item_id, status, "extract_job", {"error": code}, error_code=code, error_detail=detail)
        item = self.db.get(item_id)
        path = await asyncio.to_thread(vault.write_item, dict(item))
        self.db.update(item_id, vault_path=str(path))
        await asyncio.to_thread(vault.git_commit, f"kb: pending {item['platform']}/{item['external_id']}")
        msg = ("📥 Salvo como pendente (plataforma não suportada)." if code == "ERR-002"
               else f"📷 Post de imagens (slideshow/carrossel) — não tem áudio nem vídeo para eu transcrever. "
                    f"Link salvo em _pending/. Se quiser guardar, cole o texto das imagens em 'Notas manuais' "
                    f"e mande /reprocess {item_id[:8]}." if code == "ERR-008"
               else f"⚠️ Não consegui extrair o conteúdo ({code}). Link salvo em _pending/. "
                    f"Cole o texto em 'Notas manuais' e mande /reprocess {item_id[:8]}.")
        await self.notify(item["telegram_chat_id"], msg, reply_to=item["telegram_message_id"])
        return False

    async def step_enrich(self, item_id: str) -> bool:
        item = dict(self.db.get(item_id))
        for attempt in (1, 2):
            try:
                async with enrich_lock:
                    result, usage = await asyncio.to_thread(enrich, item, item["raw_content"])
                self.db.transition_to(item_id, "enriched", "enrich_job", usage,
                                      enrichment=result.model_dump_json(), enriched_at=vault_now(),
                                      model_used=usage["model"], error_code=None, error_detail=None)
                return True
            except EnrichmentError as e:
                log.warning("enriquecimento item=%s tentativa=%s %s", item_id, attempt, e)
                if e.code == "ERR-006" and attempt == 1:
                    await asyncio.sleep(15)
                    continue
                self.db.transition_to(item_id, "enrichment_failed", "enrich_job", {"error": e.code},
                                      error_code=e.code, error_detail=e.detail)
                await self.notify(item["telegram_chat_id"],
                                  f"⚠️ Extraí o conteúdo mas o resumo falhou ({e.code}). Mande /reprocess {item_id[:8]} depois.",
                                  reply_to=item["telegram_message_id"])
                return False
        return False

    async def step_persist(self, item_id: str):
        item = dict(self.db.get(item_id))
        path = await asyncio.to_thread(vault.write_item, item)
        self.db.update(item_id, vault_path=str(path))
        await asyncio.to_thread(vault.write_index, [dict(r) for r in self.db.all_with_enrichment()])
        await asyncio.to_thread(vault.git_commit, f"kb: add {item['platform']}/{item['external_id']}")
        text = format_summary(json.loads(item["enrichment"]))
        await self.notify(item["telegram_chat_id"], text, reply_to=item["telegram_message_id"], item_id=item_id)

    # ── triagem ─────────────────────────────────────────────
    async def triage(self, item_id: str, decision: str) -> str:
        item = self.db.get(item_id)
        if item is None:
            return "Item não encontrado"
        if item["status"] != "enriched":
            prev = item["triage_decision"]
            return f"Já triado: {vault.TRIAGE_HUMAN.get(prev, prev or item['status'])}"
        self.db.transition_to(item_id, vault.TRIAGE_LABEL[decision], "user_triage", {},
                              triage_decision=decision, triaged_at=vault_now())
        item = dict(self.db.get(item_id))
        await asyncio.to_thread(vault.write_item, item)
        await asyncio.to_thread(vault.write_index, [dict(r) for r in self.db.all_with_enrichment()])
        await asyncio.to_thread(vault.git_commit, f"kb: triage {decision} {item['platform']}/{item['external_id']}")
        return f"✔ {vault.TRIAGE_HUMAN[decision]}"

    async def reprocess(self, item_id: str) -> str:
        item = self.db.get(item_id)
        if item is None:
            return "Item não encontrado"
        st = item["status"]
        if st in ("extraction_failed", "pending_manual"):
            notes = vault.read_manual_notes(vault.item_path(dict(item))) if item["vault_path"] else ""
            if len(notes) >= 50:  # usuário colou o conteúdo manualmente
                self.db.transition_to(item_id, "extracted", "manual", {"chars": len(notes)},
                                      raw_content=notes, content_type="manual", content_lang="und",
                                      title=item["title"] or item["canonical_url"], extracted_at=vault_now())
            elif st == "extraction_failed":
                self.db.transition_to(item_id, "normalized", "manual", {})
            else:
                return "Item pendente sem notas manuais (≥50 chars) no .md para processar."
        elif st == "enrichment_failed":
            self.db.transition_to(item_id, "extracted", "manual", {})
        else:
            return f"Status {st} não é reprocessável."
        asyncio.create_task(self.run(item_id))
        return "🔁 Reprocessando..."


def vault_now() -> str:
    from .db import now
    return now()


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
