"""Fallback chain orchestration: DOI → publisher → OA → repository → mirror → metadata."""

from __future__ import annotations

import hashlib
import json
import os
import re
import threading
import time
from pathlib import Path
from typing import Any, Optional

from automation.acquisition.fulltext.doi import (
    extract_doi,
    resolve_crossref,
    resolve_doi_org,
)
from automation.acquisition.fulltext.downloader import (
    convert_to_readable,
    download_url,
    persist_representation,
)
from automation.acquisition.fulltext.open_access import collect_oa_candidates, discover_openalex
from automation.acquisition.fulltext.quality import score_content, usable_text_from_raw
from automation.acquisition.fulltext.ranking import (
    is_metadata_like,
    pick_best,
    representation_rank,
)
from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root

# Optional enable switch (default ON)
def fulltext_enabled() -> bool:
    raw = os.environ.get("IDA_FULLTEXT_ENABLED", "1").strip().lower()
    return raw not in {"0", "false", "no", "off"}


class FullTextSession:
    """Collects acquisition statistics for one production session."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self.started_at = utc_now_iso()
        self.attempts = 0
        self.enriched = 0
        self.skipped_already_rich = 0
        self.failed = 0
        self.metadata_only = 0
        self.full_html = 0
        self.pdf = 0
        self.xml = 0
        self.docx = 0
        self.open_access = 0
        self.publisher = 0
        self.repository = 0
        self.mirror = 0
        self.blocked = 0
        self.redirect = 0
        self.doi_available = 0
        self.doi_resolved = 0
        self.doi_fulltext = 0
        self.content_sizes: list[int] = []
        self.richness_scores: list[float] = []
        self.records: list[dict[str, Any]] = []

    def snapshot(self) -> dict[str, Any]:
        with self._lock:
            n = max(1, self.attempts)
            return {
                "started_at": self.started_at,
                "finished_at": utc_now_iso(),
                "attempts": self.attempts,
                "enriched": self.enriched,
                "skipped_already_rich": self.skipped_already_rich,
                "failed": self.failed,
                "metadata_only": self.metadata_only,
                "full_html": self.full_html,
                "pdf": self.pdf,
                "xml": self.xml,
                "docx": self.docx,
                "open_access": self.open_access,
                "publisher": self.publisher,
                "repository": self.repository,
                "mirror": self.mirror,
                "blocked": self.blocked,
                "redirect": self.redirect,
                "doi_available": self.doi_available,
                "doi_resolved": self.doi_resolved,
                "doi_fulltext": self.doi_fulltext,
                "metadata_pct": round(100.0 * self.metadata_only / n, 2),
                "fulltext_pct": round(
                    100.0 * (self.full_html + self.pdf + self.xml + self.docx) / n, 2
                ),
                "pdf_pct": round(100.0 * self.pdf / n, 2),
                "html_pct": round(100.0 * self.full_html / n, 2),
                "doi_resolution_rate": round(
                    100.0 * self.doi_resolved / max(1, self.doi_available), 2
                ),
                "doi_fulltext_rate": round(
                    100.0 * self.doi_fulltext / max(1, self.doi_available), 2
                ),
                "avg_content_size": round(
                    sum(self.content_sizes) / len(self.content_sizes), 1
                )
                if self.content_sizes
                else 0,
                "avg_richness": round(
                    sum(self.richness_scores) / len(self.richness_scores), 2
                )
                if self.richness_scores
                else 0,
                "records": list(self.records)[:200],
            }

    def _bump_rep(self, rep: str, source: str) -> None:
        if rep == "pdf":
            self.pdf += 1
        elif rep in {"html_fulltext"}:
            self.full_html += 1
        elif rep == "xml":
            self.xml += 1
        elif rep == "docx":
            self.docx += 1
        elif is_metadata_like(rep):
            self.metadata_only += 1
        src = (source or "").lower()
        if "unpaywall" in src or "pmc" in src or "arxiv" in src or "core" in src or "zenodo" in src or "semantic" in src or "openalex" in src:
            self.open_access += 1
        elif "publisher" in src or "crossref" in src or "landing" in src:
            self.publisher += 1
        elif "repo" in src or "hal" in src or "zenodo" in src:
            self.repository += 1
        elif "mirror" in src:
            self.mirror += 1


_SESSION = FullTextSession()


def get_session() -> FullTextSession:
    return _SESSION


def reset_session() -> FullTextSession:
    global _SESSION
    _SESSION = FullTextSession()
    return _SESSION


def _current_richness(doc: dict[str, Any]) -> dict[str, Any]:
    """Score currently attached payload (before enrichment)."""
    meta = doc.get("metadata") or {}
    text = str(meta.get("text_excerpt") or meta.get("snippet") or "")
    path = doc.get("local_path") or meta.get("content_path") or ""
    raw = b""
    if path and Path(str(path)).exists() and Path(str(path)).is_file():
        p = Path(str(path))
        if p.suffix.lower() not in {".json"} or p.stat().st_size < 500_000:
            try:
                # avoid reading queue json as content if it looks like document ref
                if p.suffix.lower() == ".json":
                    head = p.read_text(encoding="utf-8", errors="replace")[:200]
                    if '"document_id"' in head and '"connector_id"' in head:
                        raw = b""
                    else:
                        raw = p.read_bytes()
                else:
                    raw = p.read_bytes()[:5_000_000]
            except Exception:  # noqa: BLE001
                raw = b""
    if not text and raw:
        text = usable_text_from_raw(raw, str(doc.get("content_type") or ""), "")
    ct = str(doc.get("content_type") or "")
    rep = "metadata_json" if "json" in ct.lower() or (raw[:1] in (b"{", b"[")) else (
        "html_fulltext" if "html" in ct.lower() else "txt"
    )
    if raw[:4] == b"%PDF":
        rep = "pdf"
    q = score_content(raw=raw, text=text, content_type=ct, representation=rep)
    return q


def _needs_enrichment(quality: dict[str, Any]) -> bool:
    rep = str(quality.get("representation") or "")
    chars = int(quality.get("usable_chars") or 0)
    if representation_rank(rep) >= representation_rank("html_fulltext") and chars >= 1500:
        return False
    if rep == "pdf" and chars >= 800:
        return False
    if is_metadata_like(rep, usable_chars=chars):
        return True
    if chars < 800:
        return True
    return False


def resolve_fulltext_for_document(
    doc: dict[str, Any],
    *,
    session: FullTextSession | None = None,
    repo_root: Path | None = None,
    max_candidates: int = 5,
) -> dict[str, Any]:
    """Run fallback chain; return enrichment result (does not mutate unless apply)."""
    if not fulltext_enabled():
        return {"ok": False, "skipped": True, "reason": "disabled"}

    sess = session or _SESSION
    root = repo_root or find_repo_root()
    t0 = time.perf_counter()

    url = str(doc.get("original_url") or doc.get("url") or "")
    title = str(doc.get("title") or "")
    meta = dict(doc.get("metadata") or {})
    connector_id = str(doc.get("connector_id") or "FULLTEXT")
    document_id = str(doc.get("document_id") or f"DOC-{hashlib.sha256(url.encode()).hexdigest()[:12].upper()}")

    baseline = _current_richness(doc)
    if not _needs_enrichment(baseline):
        with sess._lock:
            sess.attempts += 1
            sess.skipped_already_rich += 1
            sess.content_sizes.append(int(baseline.get("usable_chars") or 0))
            sess.richness_scores.append(float(baseline.get("representation_score") or 0))
        return {
            "ok": True,
            "skipped": True,
            "reason": "already_rich",
            "baseline": baseline,
            "representation": baseline.get("representation"),
        }

    # DOI extraction from URL, title, metadata, text
    doi = extract_doi(
        url,
        meta.get("doi"),
        meta.get("DOI"),
        title,
        meta.get("text_excerpt"),
        meta.get("snippet"),
    )
    # OpenAlex work id
    openalex_id = None
    if "openalex.org/" in url:
        openalex_id = url.rstrip("/").split("/")[-1]
        if not openalex_id.startswith("W"):
            openalex_id = None

    chain_log: list[dict[str, Any]] = []
    candidates: list[dict[str, Any]] = []
    crossref: dict[str, Any] = {}
    landing = None

    if doi:
        with sess._lock:
            sess.doi_available += 1
        chain_log.append({"step": "doi_detected", "doi": doi})
        try:
            crossref = resolve_crossref(doi)
            chain_log.append(
                {
                    "step": "crossref",
                    "ok": crossref.get("ok"),
                    "landing": crossref.get("landing_page"),
                    "links": len(crossref.get("links") or []),
                }
            )
            if crossref.get("ok"):
                with sess._lock:
                    sess.doi_resolved += 1
                landing = crossref.get("landing_page")
                title = title or str(crossref.get("title") or "")
        except Exception as exc:  # noqa: BLE001
            chain_log.append({"step": "crossref", "ok": False, "error": str(exc)[:120]})
        if not landing:
            try:
                dorg = resolve_doi_org(doi)
                landing = dorg.get("landing_page")
                chain_log.append({"step": "doi.org", "ok": dorg.get("ok"), "landing": landing})
                if dorg.get("ok"):
                    with sess._lock:
                        sess.doi_resolved += 1
            except Exception as exc:  # noqa: BLE001
                chain_log.append({"step": "doi.org", "ok": False, "error": str(exc)[:120]})
    elif openalex_id:
        try:
            oa = discover_openalex(openalex_id=openalex_id)
            if oa.get("doi"):
                doi = oa["doi"]
                with sess._lock:
                    sess.doi_available += 1
            chain_log.append({"step": "openalex_id", "ok": oa.get("ok"), "candidates": len(oa.get("candidates") or [])})
        except Exception as exc:  # noqa: BLE001
            chain_log.append({"step": "openalex_id", "ok": False, "error": str(exc)[:120]})

    # Discover candidates via OA + publisher
    try:
        found = collect_oa_candidates(
            doi=doi,
            title=title,
            openalex_id=openalex_id,
            crossref_links=list(crossref.get("links") or []) if crossref else None,
            landing_page=landing or (url if url.startswith("http") and "api.crossref.org" not in url else None),
        )
        chain_log.append({"step": "discover", "candidates": len(found)})
    except Exception as exc:  # noqa: BLE001
        found = []
        chain_log.append({"step": "discover", "ok": False, "error": str(exc)[:120]})

    # Always consider original URL if not pure API metadata endpoint
    if url.startswith("http") and "api.crossref.org" not in url:
        if not any(c.get("url") == url for c in found):
            found.append(
                {
                    "url": url,
                    "representation_hint": "html_fulltext",
                    "source": "original_url",
                    "oa": False,
                }
            )

    # Download top candidates
    downloaded: list[dict[str, Any]] = []
    for cand in found[:max_candidates]:
        u = str(cand.get("url") or "")
        try:
            dl = download_url(u)
        except Exception as exc:  # noqa: BLE001
            dl = {"ok": False, "error": str(exc)[:120], "url": u, "failure_kind": "failed"}
        if not dl.get("ok"):
            fk = dl.get("failure_kind") or "failed"
            with sess._lock:
                if fk == "blocked":
                    sess.blocked += 1
                elif fk == "redirect":
                    sess.redirect += 1
            chain_log.append(
                {"step": "download", "url": u[:100], "ok": False, "error": dl.get("error")}
            )
            continue
        # PDF text conversion for ranking usable_chars
        rep = str(dl.get("representation") or cand.get("representation_hint") or "unknown")
        readable = str(dl.get("readable_text") or "")
        page_count = None
        if rep == "pdf":
            conv = convert_to_readable(dl["raw"], "pdf")
            if conv.get("text"):
                readable = str(conv["text"])
                page_count = conv.get("page_count")
                q = score_content(
                    raw=dl["raw"],
                    text=readable,
                    content_type=dl.get("content_type") or "application/pdf",
                    representation="pdf",
                    page_count=page_count if isinstance(page_count, int) else None,
                )
                dl["quality"] = q
                dl["usable_chars"] = q.get("usable_chars")
                dl["quality_score"] = q.get("representation_score")
                dl["readable_text"] = readable
        dl["source"] = cand.get("source")
        dl["oa"] = cand.get("oa")
        downloaded.append(dl)
        chain_log.append(
            {
                "step": "download",
                "url": u[:100],
                "ok": True,
                "representation": dl.get("representation"),
                "usable_chars": dl.get("usable_chars"),
                "source": cand.get("source"),
            }
        )

    best = pick_best(downloaded)
    elapsed_ms = round((time.perf_counter() - t0) * 1000, 1)

    # Fallback: keep metadata if nothing better
    if not best:
        with sess._lock:
            sess.attempts += 1
            sess.failed += 1
            sess.metadata_only += 1
            sess.content_sizes.append(int(baseline.get("usable_chars") or 0))
            sess.richness_scores.append(float(baseline.get("representation_score") or 0))
            rec = {
                "document_id": document_id,
                "doi": doi,
                "result": "metadata_fallback",
                "baseline_chars": baseline.get("usable_chars"),
                "chain": chain_log,
                "elapsed_ms": elapsed_ms,
            }
            sess.records.append(rec)
        return {
            "ok": False,
            "skipped": False,
            "reason": "no_fulltext_candidate",
            "doi": doi,
            "baseline": baseline,
            "chain": chain_log,
            "elapsed_ms": elapsed_ms,
            "representation": "metadata",
        }

    best_rep = str(best.get("representation") or "unknown")
    best_chars = int(best.get("usable_chars") or 0)
    base_chars = int(baseline.get("usable_chars") or 0)
    base_rank = representation_rank(str(baseline.get("representation") or "metadata"))
    best_rank = representation_rank(best_rep)

    # Only accept if strictly richer than baseline — never demote readable mass
    too_thin = best_chars < 400 and best_rank < representation_rank("pdf")
    rank_not_better = best_rank < base_rank
    same_rank_no_gain = best_rank == base_rank and best_chars <= base_chars + 100
    lost_mass = best_chars < max(500, int(base_chars * 0.85)) and best_rank <= representation_rank(
        "html_fulltext"
    )
    if too_thin or rank_not_better or same_rank_no_gain or lost_mass:
        with sess._lock:
            sess.attempts += 1
            sess.metadata_only += 1
            sess.content_sizes.append(base_chars)
            sess.richness_scores.append(float(baseline.get("representation_score") or 0))
        return {
            "ok": False,
            "skipped": False,
            "reason": "candidate_not_richer",
            "doi": doi,
            "baseline": baseline,
            "best": {k: best.get(k) for k in ("url", "representation", "usable_chars", "source")},
            "chain": chain_log,
            "elapsed_ms": elapsed_ms,
            "representation": baseline.get("representation"),
        }

    readable = str(best.get("readable_text") or "")
    if not readable and best.get("raw"):
        conv = convert_to_readable(best["raw"], best_rep)
        readable = str(conv.get("text") or "")

    paths = persist_representation(
        raw=best["raw"],
        representation=best_rep,
        readable_text=readable,
        connector_id=connector_id,
        document_id=document_id,
        content_type=str(best.get("content_type") or ""),
        repo_root=root,
    )

    quality = best.get("quality") or score_content(
        raw=best["raw"],
        text=readable,
        content_type=str(best.get("content_type") or ""),
        representation=best_rep,
    )

    source = str(best.get("source") or "")
    with sess._lock:
        sess.attempts += 1
        sess.enriched += 1
        sess._bump_rep(best_rep, source)
        if doi and not is_metadata_like(best_rep, usable_chars=best_chars):
            sess.doi_fulltext += 1
        sess.content_sizes.append(int(quality.get("usable_chars") or best_chars))
        sess.richness_scores.append(float(quality.get("representation_score") or 0))
        sess.records.append(
            {
                "document_id": document_id,
                "doi": doi,
                "result": "enriched",
                "representation": best_rep,
                "source": source,
                "usable_chars": quality.get("usable_chars"),
                "url": best.get("url"),
                "elapsed_ms": elapsed_ms,
            }
        )

    return {
        "ok": True,
        "skipped": False,
        "doi": doi,
        "representation": best_rep,
        "source": source,
        "url": best.get("url"),
        "content_path": paths.get("content_path"),
        "text_path": paths.get("text_path"),
        "readable_text": readable,
        "quality": quality,
        "baseline": baseline,
        "chain": chain_log,
        "elapsed_ms": elapsed_ms,
        "content_type": best.get("content_type"),
        "bytes": best.get("bytes"),
        "oa": best.get("oa"),
    }


def apply_enrichment(doc: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    """Mutate document dict for extractors: content paths + large text_excerpt."""
    if result.get("skipped") and result.get("reason") == "already_rich":
        meta = dict(doc.get("metadata") or {})
        meta["fulltext"] = {
            "attempted": True,
            "result": "already_rich",
            "representation": result.get("representation"),
            "doi": result.get("doi"),
            "baseline": result.get("baseline"),
        }
        doc["metadata"] = meta
        return doc

    if not result.get("ok"):
        meta = dict(doc.get("metadata") or {})
        meta["fulltext"] = {
            "attempted": True,
            "result": result.get("reason") or "failed",
            "doi": result.get("doi"),
            "representation": result.get("representation") or "metadata",
            "chain": result.get("chain") or [],
            "baseline": result.get("baseline"),
        }
        doc["metadata"] = meta
        return doc

    meta = dict(doc.get("metadata") or {})
    readable = str(result.get("readable_text") or "")
    # Prefer text file as local_path for extractors; keep binary path in metadata
    text_path = result.get("text_path") or ""
    content_path = result.get("content_path") or ""
    if text_path and Path(text_path).exists():
        doc["local_path"] = text_path
    elif content_path:
        doc["local_path"] = content_path

    if readable:
        meta["text_excerpt"] = readable[:80000]
        meta["text_length"] = len(readable)
        meta["full_text"] = True
    meta["content_path"] = content_path
    meta["fulltext"] = {
        "attempted": True,
        "result": "enriched",
        "doi": result.get("doi"),
        "representation": result.get("representation"),
        "source": result.get("source"),
        "url": result.get("url"),
        "quality": result.get("quality"),
        "baseline": result.get("baseline"),
        "elapsed_ms": result.get("elapsed_ms"),
        "oa": result.get("oa"),
        "chain": result.get("chain") or [],
    }
    # content type
    rep = result.get("representation")
    if rep == "pdf":
        doc["content_type"] = "application/pdf"
    elif rep in {"html_fulltext", "html_thin"}:
        doc["content_type"] = "text/html"
    elif rep == "xml":
        doc["content_type"] = "application/xml"
    elif rep == "docx":
        doc["content_type"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    elif readable:
        doc["content_type"] = "text/plain"

    if result.get("bytes"):
        doc["bytes"] = int(result["bytes"])
    doc["notes"] = (
        str(doc.get("notes") or "")
        + f" | fulltext={result.get('representation')} via {result.get('source')}"
    ).strip(" |")
    doc["metadata"] = meta
    return doc


def enrich_document_dict(
    doc: dict[str, Any],
    *,
    session: FullTextSession | None = None,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Resolve + apply full-text enrichment on a document dict."""
    result = resolve_fulltext_for_document(doc, session=session, repo_root=repo_root)
    return apply_enrichment(doc, result)


def enrich_document_ref(doc_ref: Any, *, session: FullTextSession | None = None, repo_root: Path | None = None) -> Any:
    """Enrich a DocumentRef dataclass instance in place."""
    d = doc_ref.to_dict() if hasattr(doc_ref, "to_dict") else dict(doc_ref)
    enriched = enrich_document_dict(d, session=session, repo_root=repo_root)
    # write back fields
    for key in (
        "local_path",
        "content_type",
        "bytes",
        "notes",
        "metadata",
        "title",
    ):
        if key in enriched and hasattr(doc_ref, key):
            setattr(doc_ref, key, enriched[key])
    return doc_ref


def persist_session_stats(session: FullTextSession | None = None, *, repo_root: Path | None = None) -> Path:
    root = repo_root or find_repo_root()
    sess = session or _SESSION
    path = root / "automation" / "learning" / "state" / "fulltext_acquisition.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    snap = sess.snapshot()
    path.write_text(json.dumps(snap, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path
