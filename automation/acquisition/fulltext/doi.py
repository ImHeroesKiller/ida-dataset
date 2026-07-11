"""DOI extraction and Crossref-based resolution."""

from __future__ import annotations

import os
import re
from typing import Any, Optional
from urllib.parse import quote, unquote, urlparse

from automation.connectors.http_utils import DEFAULT_UA, http_get

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>\]\}]+", re.I)


def extract_doi(*sources: Any) -> Optional[str]:
    """Extract first DOI from URLs, JSON blobs, or free text."""
    for src in sources:
        if src is None:
            continue
        if isinstance(src, dict):
            for key in ("DOI", "doi", "DOI_URL", "doi_url"):
                if src.get(key):
                    found = extract_doi(str(src.get(key)))
                    if found:
                        return found
            # nested message (Crossref)
            msg = src.get("message")
            if isinstance(msg, dict):
                found = extract_doi(msg)
                if found:
                    return found
            # scan stringified subset
            blob = str(src)[:8000]
            m = DOI_RE.search(blob)
            if m:
                return _clean_doi(m.group(0))
            continue
        text = str(src)
        # doi.org URL
        if "doi.org/" in text.lower():
            part = text.lower().split("doi.org/", 1)[1]
            part = part.split("?", 1)[0].split("#", 1)[0]
            return _clean_doi(unquote(part))
        m = DOI_RE.search(text)
        if m:
            return _clean_doi(m.group(0))
    return None


def _clean_doi(doi: str) -> str:
    d = (doi or "").strip().rstrip(".,;)}]")
    d = d.replace("https://doi.org/", "").replace("http://doi.org/", "")
    return d


def crossref_mailto() -> str:
    return (
        os.environ.get("CROSSREF_MAILTO")
        or os.environ.get("OPENALEX_EMAIL")
        or os.environ.get("UNPAYWALL_EMAIL")
        or "ida-dataset-factory@users.noreply.github.com"
    )


def resolve_crossref(doi: str, *, timeout: float = 25.0) -> dict[str, Any]:
    """Resolve DOI via Crossref works API → landing page + link assets."""
    doi = _clean_doi(doi)
    if not doi:
        return {"ok": False, "error": "empty_doi", "doi": doi}
    url = f"https://api.crossref.org/works/{quote(doi, safe='/')}"
    headers = {
        "User-Agent": f"{DEFAULT_UA}; mailto:{crossref_mailto()}",
        "Accept": "application/json",
    }
    res = http_get(url, headers=headers, timeout=timeout, retries=2)
    if not res.get("ok") or not isinstance(res.get("json"), dict):
        return {
            "ok": False,
            "error": res.get("error") or "crossref_failed",
            "doi": doi,
            "http_status": res.get("status"),
        }
    msg = (res["json"] or {}).get("message") or {}
    if not isinstance(msg, dict):
        return {"ok": False, "error": "crossref_bad_payload", "doi": doi}

    title = msg.get("title")
    if isinstance(title, list):
        title = title[0] if title else ""
    resource = msg.get("resource") or {}
    primary = (resource.get("primary") or {}).get("URL") if isinstance(resource, dict) else None
    landing = (
        primary
        or msg.get("URL")
        or f"https://doi.org/{doi}"
    )

    links: list[dict[str, Any]] = []
    for link in msg.get("link") or []:
        if not isinstance(link, dict):
            continue
        links.append(
            {
                "url": link.get("URL"),
                "content_type": link.get("content-type") or link.get("content_type"),
                "intended": link.get("intended-application"),
                "source": "crossref_link",
            }
        )

    # license / OA hints
    license_urls = []
    for lic in msg.get("license") or []:
        if isinstance(lic, dict) and lic.get("URL"):
            license_urls.append(str(lic["URL"]))

    abstract = msg.get("abstract") or ""
    if abstract:
        abstract = re.sub(r"<[^>]+>", " ", str(abstract))
        abstract = re.sub(r"\s+", " ", abstract).strip()

    return {
        "ok": True,
        "doi": doi,
        "title": str(title or "")[:300],
        "landing_page": landing,
        "publisher": msg.get("publisher") or "",
        "container_title": (msg.get("container-title") or [""])[0]
        if isinstance(msg.get("container-title"), list)
        else msg.get("container-title") or "",
        "links": links,
        "license_urls": license_urls,
        "abstract": abstract[:4000],
        "type": msg.get("type") or "",
        "is_referenced_by_count": msg.get("is-referenced-by-count"),
        "raw_message_keys": list(msg.keys())[:40],
        "source": "crossref",
    }


def resolve_doi_org(doi: str, *, timeout: float = 20.0) -> dict[str, Any]:
    """Follow doi.org to final landing URL (no full body)."""
    doi = _clean_doi(doi)
    url = f"https://doi.org/{quote(doi, safe='/')}"
    res = http_get(
        url,
        headers={"User-Agent": DEFAULT_UA, "Accept": "text/html,application/xhtml+xml"},
        timeout=timeout,
        retries=1,
    )
    final = res.get("url") or url
    # urllib may not expose final URL after redirect in all cases
    return {
        "ok": bool(res.get("ok")),
        "doi": doi,
        "landing_page": final,
        "http_status": res.get("status"),
        "content_type": res.get("content_type"),
        "error": res.get("error"),
        "source": "doi.org",
    }


def host_of(url: str) -> str:
    try:
        return (urlparse(url).hostname or "").lower()
    except Exception:  # noqa: BLE001
        return ""
