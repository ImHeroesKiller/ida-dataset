"""PDF text extraction — never publish raw PDF; extract text + metadata only."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def extract_pdf(path: str | Path) -> dict[str, Any]:
    """Extract text and metadata from PDF. Tries PyMuPDF then pdfplumber."""
    p = Path(path)
    if not p.exists():
        return {"ok": False, "error": "file_not_found", "text": "", "metadata": {}}

    # Try PyMuPDF (fitz)
    try:
        import fitz  # type: ignore

        doc = fitz.open(str(p))
        texts: list[str] = []
        meta = dict(doc.metadata or {})
        for page in doc:
            texts.append(page.get_text("text") or "")
        doc.close()
        text = "\n".join(texts).strip()
        return {
            "ok": True,
            "backend": "pymupdf",
            "text": text[:200000],
            "metadata": {
                "title": meta.get("title") or "",
                "author": meta.get("author") or "",
                "subject": meta.get("subject") or "",
                "creationDate": meta.get("creationDate") or "",
                "modDate": meta.get("modDate") or "",
                "page_count": len(texts),
            },
        }
    except Exception as exc_fitz:  # noqa: BLE001
        fitz_err = str(exc_fitz)

    # Try pdfplumber
    try:
        import pdfplumber  # type: ignore

        texts = []
        meta = {}
        with pdfplumber.open(str(p)) as pdf:
            meta = dict(pdf.metadata or {})
            for page in pdf.pages:
                texts.append(page.extract_text() or "")
        text = "\n".join(texts).strip()
        return {
            "ok": True,
            "backend": "pdfplumber",
            "text": text[:200000],
            "metadata": {
                "title": meta.get("Title") or meta.get("title") or "",
                "author": meta.get("Author") or meta.get("author") or "",
                "page_count": len(texts),
            },
        }
    except Exception as exc_pl:  # noqa: BLE001
        return {
            "ok": False,
            "error": f"pdf_extract_failed: fitz={fitz_err}; pdfplumber={exc_pl}",
            "text": "",
            "metadata": {},
        }
