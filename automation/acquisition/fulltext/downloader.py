"""Multi-format full-text downloader with light conversion to readable text."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any, Optional

from automation.acquisition.fulltext.quality import score_content, strip_html, usable_text_from_raw
from automation.acquisition.fulltext.ranking import classify_bytes
from automation.connectors.http_utils import DEFAULT_UA, http_get
from automation.lib.paths import find_repo_root


def download_url(
    url: str,
    *,
    timeout: float = 35.0,
    retries: int = 1,
    accept: str | None = None,
) -> dict[str, Any]:
    """Download URL without connector domain allowlist (legal public OA/publisher)."""
    url = (url or "").strip()
    if not url.startswith("http"):
        return {"ok": False, "error": "invalid_url", "url": url}
    headers = {
        "User-Agent": DEFAULT_UA,
        "Accept": accept
        or "application/pdf,text/html,application/xhtml+xml,application/xml,text/xml,text/plain,application/json,*/*",
    }
    res = http_get(url, headers=headers, timeout=timeout, retries=retries)
    if not res.get("ok"):
        status = res.get("status")
        err = str(res.get("error") or "")
        kind = "failed"
        if status in {401, 403} or "403" in err or "401" in err:
            kind = "blocked"
        elif status in {301, 302, 303, 307, 308}:
            kind = "redirect"
        return {
            "ok": False,
            "error": res.get("error") or f"http_{status}",
            "url": url,
            "http_status": status,
            "failure_kind": kind,
        }

    raw: bytes = res.get("raw") or (res.get("text") or "").encode("utf-8", errors="replace")
    ctype = res.get("content_type") or ""
    rep = classify_bytes(raw, ctype, url)

    # Detect login/captcha/js shells early
    text_head = ""
    try:
        text_head = raw[:12000].decode("utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        text_head = ""
    low = text_head.lower()
    if rep in {"html_fulltext", "unknown"} and (
        "captcha" in low
        or "cloudflare" in low
        or "enable javascript" in low
        or ("log in" in low and "password" in low and len(strip_html(text_head)) < 400)
    ):
        return {
            "ok": False,
            "error": "blocked_or_shell",
            "url": url,
            "http_status": res.get("status"),
            "failure_kind": "blocked",
            "representation": rep,
        }

    page_count = None
    readable = ""
    if rep == "pdf":
        # persist temp then extract
        pass
    else:
        readable = usable_text_from_raw(raw, ctype, rep)

    quality = score_content(
        raw=raw,
        text=readable,
        content_type=ctype,
        representation=rep,
        page_count=page_count,
    )
    rep = quality.get("representation") or rep

    return {
        "ok": True,
        "url": url,
        "raw": raw,
        "text": res.get("text") or "",
        "readable_text": readable,
        "content_type": ctype,
        "http_status": res.get("status"),
        "bytes": len(raw),
        "representation": rep,
        "quality": quality,
        "usable_chars": quality.get("usable_chars") or 0,
        "quality_score": quality.get("representation_score") or 0,
        "failure_kind": None,
    }


def convert_to_readable(raw: bytes, representation: str, *, path: Path | None = None) -> dict[str, Any]:
    """Convert binary/text body to readable text for existing extractors."""
    if representation == "pdf":
        # write temp if needed
        tmp = path
        if tmp is None or not tmp.exists():
            root = find_repo_root()
            tmp_dir = root / "automation" / "raw_documents" / "_fulltext_tmp"
            tmp_dir.mkdir(parents=True, exist_ok=True)
            h = hashlib.sha256(raw).hexdigest()[:16]
            tmp = tmp_dir / f"{h}.pdf"
            tmp.write_bytes(raw)
        try:
            from automation.acquisition.pdf_extract import extract_pdf

            pdf = extract_pdf(tmp)
            if pdf.get("ok") and pdf.get("text"):
                return {
                    "ok": True,
                    "text": str(pdf["text"]),
                    "page_count": (pdf.get("metadata") or {}).get("page_count"),
                    "backend": pdf.get("backend"),
                }
            return {"ok": False, "text": "", "error": pdf.get("error")}
        except Exception as exc:  # noqa: BLE001
            return {"ok": False, "text": "", "error": str(exc)}

    if representation == "docx":
        # minimal: unzip document.xml if python-docx unavailable
        try:
            import zipfile
            import io

            with zipfile.ZipFile(io.BytesIO(raw)) as zf:
                xml = zf.read("word/document.xml").decode("utf-8", errors="replace")
            text = re.sub(r"</w:p>", "\n", xml)
            text = re.sub(r"<[^>]+>", "", text)
            text = re.sub(r"\s+\n", "\n", text)
            return {"ok": True, "text": text.strip()}
        except Exception as exc:  # noqa: BLE001
            return {"ok": False, "text": "", "error": str(exc)}

    readable = usable_text_from_raw(raw, representation=representation)
    return {"ok": bool(readable), "text": readable}


def persist_representation(
    *,
    raw: bytes,
    representation: str,
    readable_text: str,
    connector_id: str,
    document_id: str,
    content_type: str = "",
    repo_root: Path | None = None,
) -> dict[str, str]:
    """Write content + readable text under raw_documents/<connector>/fulltext/."""
    root = repo_root or find_repo_root()
    store = root / "automation" / "raw_documents" / (connector_id or "FULLTEXT") / "fulltext"
    store.mkdir(parents=True, exist_ok=True)
    ext_map = {
        "pdf": ".pdf",
        "html_fulltext": ".html",
        "html_thin": ".html",
        "xml": ".xml",
        "docx": ".docx",
        "txt": ".txt",
        "markdown": ".md",
        "metadata_json": ".json",
        "epub": ".epub",
    }
    ext = ext_map.get(representation, ".bin")
    content_path = store / f"{document_id}{ext}"
    content_path.write_bytes(raw)
    text_path = store / f"{document_id}.txt"
    if readable_text:
        text_path.write_text(readable_text, encoding="utf-8", newline="\n")
    elif representation == "pdf":
        conv = convert_to_readable(raw, "pdf", path=content_path)
        if conv.get("text"):
            text_path.write_text(str(conv["text"]), encoding="utf-8", newline="\n")
            readable_text = str(conv["text"])
    return {
        "content_path": str(content_path),
        "text_path": str(text_path) if text_path.exists() else "",
        "readable_text": readable_text,
    }
