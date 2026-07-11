"""Representation ranking — richest available document body wins."""

from __future__ import annotations

from typing import Any

# Higher = better. Metadata is last.
REPRESENTATION_RANK: dict[str, int] = {
    "html_fulltext": 100,
    "pdf": 90,
    "xml": 80,
    "epub": 70,
    "docx": 60,
    "txt": 50,
    "markdown": 45,
    "html_thin": 30,
    "abstract": 20,
    "metadata_json": 10,
    "metadata": 5,
    "unknown": 0,
    "failed": 0,
    "blocked": 0,
}


def representation_rank(kind: str) -> int:
    return int(REPRESENTATION_RANK.get(str(kind or "unknown"), 0))


def classify_bytes(raw: bytes, content_type: str = "", url: str = "") -> str:
    """Classify representation from content-type and magic bytes."""
    ct = (content_type or "").lower()
    url_l = (url or "").lower()
    head = raw[:16] if raw else b""

    if head.startswith(b"%PDF") or "pdf" in ct or url_l.endswith(".pdf"):
        return "pdf"
    if head.startswith(b"PK") and ("word" in ct or url_l.endswith(".docx") or "officedocument" in ct):
        return "docx"
    if "epub" in ct or url_l.endswith(".epub"):
        return "epub"
    if "xml" in ct or head.startswith(b"<?xml") or (head.startswith(b"<") and b"xmlns" in raw[:500]):
        if b"<html" in raw[:500].lower() or b"<!doctype html" in raw[:200].lower():
            return "html_fulltext"
        return "xml"
    if "json" in ct or (raw[:1] in (b"{", b"[") and b'"' in raw[:200]):
        return "metadata_json"
    if "markdown" in ct or url_l.endswith(".md"):
        return "markdown"
    if "text/plain" in ct or url_l.endswith(".txt"):
        return "txt"
    if "html" in ct or b"<html" in raw[:500].lower() or b"<!doctype html" in raw[:200].lower():
        # thin vs full decided later by quality
        return "html_fulltext"
    return "unknown"


def is_metadata_like(kind: str, *, usable_chars: int = 0) -> bool:
    if kind in {"metadata", "metadata_json", "abstract"}:
        return True
    if kind == "html_thin":
        return True
    if kind in {"html_fulltext", "txt"} and usable_chars < 400:
        return True
    return False


def pick_best(candidates: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Pick highest-ranked successful candidate; break ties by usable_chars then bytes."""
    ok = [c for c in candidates if c.get("ok") and c.get("raw") is not None]
    if not ok:
        return None

    def key(c: dict[str, Any]) -> tuple:
        kind = str(c.get("representation") or "unknown")
        # demote thin html
        if kind == "html_fulltext" and int(c.get("usable_chars") or 0) < 400:
            kind = "html_thin"
            c = {**c, "representation": kind}
        return (
            representation_rank(kind),
            int(c.get("usable_chars") or 0),
            int(c.get("bytes") or 0),
            float(c.get("quality_score") or 0),
        )

    return max(ok, key=key)
