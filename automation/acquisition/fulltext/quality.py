"""Content quality / richness scoring for acquired representations."""

from __future__ import annotations

import re
from typing import Any

from automation.acquisition.fulltext.ranking import representation_rank


def strip_html(raw: str) -> str:
    t = re.sub(r"(?is)<script[^>]*>.*?</script>", " ", raw or "")
    t = re.sub(r"(?is)<style[^>]*>.*?</style>", " ", t)
    t = re.sub(r"(?is)<noscript[^>]*>.*?</noscript>", " ", t)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"&\w+;", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def usable_text_from_raw(raw: bytes, content_type: str = "", representation: str = "") -> str:
    if not raw:
        return ""
    rep = representation or ""
    ct = (content_type or "").lower()
    if rep == "pdf" or raw[:4] == b"%PDF":
        # binary — text extracted separately
        return ""
    try:
        text = raw.decode("utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        text = raw.decode("latin-1", errors="replace")
    if rep in {"html_fulltext", "html_thin"} or "html" in ct or text.lstrip().lower().startswith(
        ("<!doctype", "<html")
    ):
        return strip_html(text)
    if rep == "metadata_json" or "json" in ct or text.lstrip()[:1] in "{[":
        # extract string leaves
        import json

        try:
            data = json.loads(text)
        except Exception:  # noqa: BLE001
            return strip_html(text)[:5000]
        strings: list[str] = []

        def walk(o: Any, depth: int = 0) -> None:
            if depth > 14:
                return
            if isinstance(o, str) and len(o) > 2:
                strings.append(o)
            elif isinstance(o, dict):
                for v in o.values():
                    walk(v, depth + 1)
            elif isinstance(o, list):
                for i in o[:100]:
                    walk(i, depth + 1)

        walk(data)
        joined = re.sub(r"<[^>]+>", " ", " ".join(strings))
        return re.sub(r"\s+", " ", joined).strip()
    if rep == "xml" or "xml" in ct:
        return strip_html(text)
    return text


def score_content(
    *,
    raw: bytes | None = None,
    text: str = "",
    content_type: str = "",
    representation: str = "",
    page_count: int | None = None,
) -> dict[str, Any]:
    """Compute richness metrics and a 0–100 representation score."""
    raw = raw or b""
    usable = text or usable_text_from_raw(raw, content_type, representation)
    chars = len(usable)
    words = len(usable.split()) if usable else 0
    paras = max(1, usable.count(". ") // 2) if usable else 0
    tables = len(re.findall(r"(?i)<table|\btable\b", usable + (raw[:20000].decode("utf-8", errors="replace") if raw else "")))
    refs = len(re.findall(r"(?i)\breferences\b|doi:|https?://doi\.org", usable))
    figures = len(re.findall(r"(?i)\bfigure\b|\bfig\.\s*\d|<img\b", usable + (raw[:10000].decode("utf-8", errors="replace") if raw else "")))
    captions = len(re.findall(r"(?i)caption", usable))
    # knowledge density proxy: unique mid-length tokens / 100 words
    tokens = [t.lower() for t in re.findall(r"[A-Za-z][A-Za-z0-9\-]{3,}", usable)]
    uniq = len(set(tokens))
    density = round((uniq / max(1, words)) * 100, 3) if words else 0.0

    rep = representation or "unknown"
    if rep == "html_fulltext" and chars < 400:
        rep = "html_thin"

    base = representation_rank(rep)
    # scale by content mass
    mass = min(40.0, (chars / 500.0) * 8.0)  # up to +40
    struct = min(15.0, tables * 2 + refs * 0.5 + figures * 1.0)
    score = min(100.0, base * 0.45 + mass + struct + min(10.0, density / 5.0))

    return {
        "representation": rep,
        "content_length": chars,
        "words": words,
        "paragraphs": paras,
        "tables": tables,
        "references": refs,
        "figures": figures,
        "captions": captions,
        "pages": page_count,
        "readable_text": chars,
        "knowledge_density": density,
        "representation_score": round(score, 2),
        "usable_chars": chars,
        "bytes": len(raw),
    }
