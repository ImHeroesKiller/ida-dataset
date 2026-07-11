"""Open-access and repository full-text discovery — public legal sources only."""

from __future__ import annotations

import os
import re
from typing import Any, Optional
from urllib.parse import quote, urlencode

from automation.acquisition.fulltext.doi import crossref_mailto, extract_doi
from automation.connectors.http_utils import DEFAULT_UA, http_get


def _email() -> str:
    return (
        os.environ.get("UNPAYWALL_EMAIL")
        or os.environ.get("OPENALEX_EMAIL")
        or os.environ.get("CROSSREF_MAILTO")
        or "ida-dataset-factory@users.noreply.github.com"
    )


def discover_unpaywall(doi: str, *, timeout: float = 25.0) -> dict[str, Any]:
    """Unpaywall OA locations (requires email — polite pool)."""
    doi = (doi or "").strip()
    if not doi:
        return {"ok": False, "error": "empty_doi", "candidates": []}
    email = _email()
    url = f"https://api.unpaywall.org/v2/{quote(doi, safe='/')}?{urlencode({'email': email})}"
    res = http_get(url, headers={"User-Agent": f"{DEFAULT_UA}; mailto:{email}"}, timeout=timeout, retries=1)
    if not res.get("ok") or not isinstance(res.get("json"), dict):
        return {
            "ok": False,
            "error": res.get("error") or f"http_{res.get('status')}",
            "candidates": [],
            "http_status": res.get("status"),
        }
    data = res["json"]
    candidates: list[dict[str, Any]] = []
    best = data.get("best_oa_location") or {}
    locs = list(data.get("oa_locations") or [])
    if best and best not in locs:
        locs.insert(0, best)
    for loc in locs:
        if not isinstance(loc, dict):
            continue
        pdf = loc.get("url_for_pdf") or ""
        landing = loc.get("url_for_landing_page") or loc.get("url") or ""
        if pdf:
            candidates.append(
                {
                    "url": pdf,
                    "representation_hint": "pdf",
                    "source": "unpaywall",
                    "host_type": loc.get("host_type"),
                    "license": loc.get("license"),
                    "oa": True,
                }
            )
        if landing and landing != pdf:
            candidates.append(
                {
                    "url": landing,
                    "representation_hint": "html_fulltext",
                    "source": "unpaywall_landing",
                    "host_type": loc.get("host_type"),
                    "license": loc.get("license"),
                    "oa": True,
                }
            )
    return {
        "ok": True,
        "is_oa": bool(data.get("is_oa")),
        "oa_status": data.get("oa_status"),
        "journal_is_oa": data.get("journal_is_oa"),
        "candidates": candidates,
        "title": data.get("title") or "",
        "source": "unpaywall",
    }


def discover_openalex(doi: str | None = None, openalex_id: str | None = None, *, timeout: float = 25.0) -> dict[str, Any]:
    """OpenAlex work locations (PDF + landing)."""
    email = _email()
    if openalex_id:
        oid = openalex_id.replace("https://openalex.org/", "")
        api = f"https://api.openalex.org/works/{oid}"
    elif doi:
        api = f"https://api.openalex.org/works/https://doi.org/{quote(doi, safe='/')}"
    else:
        return {"ok": False, "error": "need_doi_or_id", "candidates": []}
    if email:
        api += f"?{urlencode({'mailto': email})}"
    res = http_get(api, headers={"User-Agent": f"{DEFAULT_UA}; mailto:{email}"}, timeout=timeout, retries=1)
    if not res.get("ok") or not isinstance(res.get("json"), dict):
        return {"ok": False, "error": res.get("error") or "openalex_failed", "candidates": []}
    data = res["json"]
    candidates: list[dict[str, Any]] = []
    primary = data.get("primary_location") or {}
    locations = list(data.get("locations") or [])
    if primary:
        locations.insert(0, primary)
    seen: set[str] = set()
    for loc in locations:
        if not isinstance(loc, dict):
            continue
        pdf = (loc.get("pdf_url") or "").strip()
        landing = (loc.get("landing_page_url") or "").strip()
        source = ((loc.get("source") or {}) if isinstance(loc.get("source"), dict) else {})
        src_name = source.get("display_name") or "openalex"
        for u, hint in ((pdf, "pdf"), (landing, "html_fulltext")):
            if not u or u in seen:
                continue
            seen.add(u)
            candidates.append(
                {
                    "url": u,
                    "representation_hint": hint,
                    "source": f"openalex:{src_name}",
                    "oa": bool(loc.get("is_oa")),
                    "license": loc.get("license"),
                }
            )
    # abstract reconstruction
    abstract = ""
    inv = data.get("abstract_inverted_index")
    if isinstance(inv, dict) and inv:
        try:
            positions: list[tuple[int, str]] = []
            for word, idxs in inv.items():
                for i in idxs:
                    positions.append((int(i), str(word)))
            positions.sort()
            abstract = " ".join(w for _, w in positions)
        except Exception:  # noqa: BLE001
            abstract = ""
    return {
        "ok": True,
        "candidates": candidates,
        "title": data.get("title") or data.get("display_name") or "",
        "doi": extract_doi(data.get("doi"), doi),
        "openalex_id": data.get("id"),
        "abstract": abstract[:4000],
        "is_oa": data.get("open_access", {}).get("is_oa")
        if isinstance(data.get("open_access"), dict)
        else None,
        "source": "openalex",
    }


def discover_pubmed_central(doi: str, *, timeout: float = 20.0) -> dict[str, Any]:
    """Europe PMC full-text links when available."""
    doi = (doi or "").strip()
    if not doi:
        return {"ok": False, "candidates": []}
    q = urlencode({"query": f'DOI:"{doi}"', "format": "json", "pageSize": "3", "resultType": "core"})
    api = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?{q}"
    res = http_get(api, timeout=timeout, retries=1)
    if not res.get("ok") or not isinstance(res.get("json"), dict):
        return {"ok": False, "error": res.get("error"), "candidates": []}
    results = ((res["json"].get("resultList") or {}).get("result")) or []
    candidates: list[dict[str, Any]] = []
    for row in results:
        if not isinstance(row, dict):
            continue
        pmcid = row.get("pmcid") or ""
        if pmcid:
            candidates.append(
                {
                    "url": f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/pdf/",
                    "representation_hint": "pdf",
                    "source": "pmc",
                    "oa": True,
                }
            )
            candidates.append(
                {
                    "url": f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/",
                    "representation_hint": "html_fulltext",
                    "source": "pmc_html",
                    "oa": True,
                }
            )
            # Europe PMC XML
            candidates.append(
                {
                    "url": f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML",
                    "representation_hint": "xml",
                    "source": "europepmc_xml",
                    "oa": True,
                }
            )
        ft = row.get("fullTextUrlList") or {}
        for item in (ft.get("fullTextUrl") or []) if isinstance(ft, dict) else []:
            if isinstance(item, dict) and item.get("url"):
                hint = "pdf" if str(item.get("documentStyle") or "").lower() == "pdf" else "html_fulltext"
                candidates.append(
                    {
                        "url": item["url"],
                        "representation_hint": hint,
                        "source": "europepmc",
                        "oa": True,
                    }
                )
    return {"ok": True, "candidates": candidates, "source": "europepmc"}


def discover_arxiv(doi: str | None = None, title: str = "", *, timeout: float = 20.0) -> dict[str, Any]:
    """arXiv API by DOI or title."""
    if doi:
        q = f'doi:"{doi}"'
    elif title:
        q = f'ti:"{title[:120]}"'
    else:
        return {"ok": False, "candidates": []}
    api = "http://export.arxiv.org/api/query?" + urlencode({"search_query": q, "start": 0, "max_results": 3})
    res = http_get(api, timeout=timeout, retries=1)
    if not res.get("ok"):
        return {"ok": False, "error": res.get("error"), "candidates": []}
    text = res.get("text") or ""
    candidates: list[dict[str, Any]] = []
    for m in re.finditer(r"<id>(https?://arxiv\.org/abs/[^<]+)</id>", text):
        abs_url = m.group(1)
        pdf_url = abs_url.replace("/abs/", "/pdf/") + ".pdf"
        candidates.append({"url": pdf_url, "representation_hint": "pdf", "source": "arxiv", "oa": True})
        candidates.append({"url": abs_url, "representation_hint": "html_fulltext", "source": "arxiv_abs", "oa": True})
    return {"ok": bool(candidates), "candidates": candidates, "source": "arxiv"}


def discover_semantic_scholar(doi: str, *, timeout: float = 20.0) -> dict[str, Any]:
    """Semantic Scholar paper OA PDF if present."""
    doi = (doi or "").strip()
    if not doi:
        return {"ok": False, "candidates": []}
    api = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{quote(doi, safe='/')}?fields=title,openAccessPdf,url,externalIds"
    res = http_get(api, timeout=timeout, retries=1)
    if not res.get("ok") or not isinstance(res.get("json"), dict):
        return {"ok": False, "error": res.get("error"), "candidates": []}
    data = res["json"]
    candidates: list[dict[str, Any]] = []
    oa = data.get("openAccessPdf") or {}
    if isinstance(oa, dict) and oa.get("url"):
        candidates.append(
            {
                "url": oa["url"],
                "representation_hint": "pdf",
                "source": "semantic_scholar",
                "oa": True,
            }
        )
    if data.get("url"):
        candidates.append(
            {
                "url": data["url"],
                "representation_hint": "html_fulltext",
                "source": "semantic_scholar_page",
                "oa": True,
            }
        )
    return {"ok": True, "candidates": candidates, "title": data.get("title") or "", "source": "semantic_scholar"}


def discover_core(doi: str, *, timeout: float = 20.0) -> dict[str, Any]:
    """CORE API v3 open access (optional CORE_API_KEY for higher limits)."""
    doi = (doi or "").strip()
    if not doi:
        return {"ok": False, "candidates": []}
    key = os.environ.get("CORE_API_KEY", "").strip()
    # Public search endpoint
    q = 'doi:"' + doi + '"'
    api = "https://api.core.ac.uk/v3/search/works?" + urlencode({"q": q, "limit": 3})
    headers = {"User-Agent": DEFAULT_UA}
    if key:
        headers["Authorization"] = f"Bearer {key}"
    res = http_get(api, headers=headers, timeout=timeout, retries=1)
    if not res.get("ok") or not isinstance(res.get("json"), dict):
        return {"ok": False, "error": res.get("error"), "candidates": []}
    candidates: list[dict[str, Any]] = []
    for row in res["json"].get("results") or []:
        if not isinstance(row, dict):
            continue
        for u in (row.get("downloadUrl"), row.get("sourceFulltextUrls"), row.get("links")):
            if isinstance(u, str) and u.startswith("http"):
                hint = "pdf" if ".pdf" in u.lower() else "html_fulltext"
                candidates.append({"url": u, "representation_hint": hint, "source": "core", "oa": True})
            elif isinstance(u, list):
                for item in u:
                    if isinstance(item, str) and item.startswith("http"):
                        hint = "pdf" if ".pdf" in item.lower() else "html_fulltext"
                        candidates.append({"url": item, "representation_hint": hint, "source": "core", "oa": True})
                    elif isinstance(item, dict) and item.get("url"):
                        candidates.append(
                            {
                                "url": item["url"],
                                "representation_hint": "html_fulltext",
                                "source": "core",
                                "oa": True,
                            }
                        )
    return {"ok": True, "candidates": candidates, "source": "core"}


def discover_zenodo(doi: str, *, timeout: float = 20.0) -> dict[str, Any]:
    """Zenodo records by DOI."""
    doi = (doi or "").strip()
    if not doi:
        return {"ok": False, "candidates": []}
    api = "https://zenodo.org/api/records?" + urlencode({"q": f'doi:"{doi}"', "size": 3})
    res = http_get(api, timeout=timeout, retries=1)
    if not res.get("ok") or not isinstance(res.get("json"), dict):
        return {"ok": False, "candidates": []}
    candidates: list[dict[str, Any]] = []
    for hit in res["json"].get("hits", {}).get("hits") or []:
        files = ((hit.get("files") or []) if isinstance(hit, dict) else [])
        for f in files:
            if not isinstance(f, dict):
                continue
            link = (f.get("links") or {}).get("self") or (f.get("links") or {}).get("download")
            if link:
                key = str(f.get("key") or "").lower()
                hint = "pdf" if key.endswith(".pdf") else ("xml" if key.endswith(".xml") else "txt")
                candidates.append({"url": link, "representation_hint": hint, "source": "zenodo", "oa": True})
    return {"ok": True, "candidates": candidates, "source": "zenodo"}


def collect_oa_candidates(
    *,
    doi: str | None,
    title: str = "",
    openalex_id: str | None = None,
    crossref_links: list[dict[str, Any]] | None = None,
    landing_page: str | None = None,
) -> list[dict[str, Any]]:
    """Aggregate OA/repository candidates (deduped by URL)."""
    out: list[dict[str, Any]] = []
    seen: set[str] = set()

    def add_many(items: list[dict[str, Any]]) -> None:
        for it in items:
            u = str(it.get("url") or "").strip()
            if not u or not u.startswith("http") or u in seen:
                continue
            seen.add(u)
            out.append(it)

    if crossref_links:
        for link in crossref_links:
            u = str(link.get("url") or "").strip()
            if not u:
                continue
            ct = str(link.get("content_type") or "").lower()
            hint = "pdf" if "pdf" in ct else ("xml" if "xml" in ct else "html_fulltext")
            add_many(
                [
                    {
                        "url": u,
                        "representation_hint": hint,
                        "source": link.get("source") or "crossref_link",
                        "oa": True,
                    }
                ]
            )

    if landing_page and landing_page.startswith("http"):
        add_many(
            [
                {
                    "url": landing_page,
                    "representation_hint": "html_fulltext",
                    "source": "publisher_landing",
                    "oa": False,
                }
            ]
        )

    if doi:
        # Tier 1: high-yield OA + bibliographic locations
        tier1 = (
            lambda: discover_unpaywall(doi),
            lambda: discover_openalex(doi=doi, openalex_id=openalex_id),
            lambda: discover_pubmed_central(doi),
        )
        # Tier 2: secondary repositories (only if still sparse)
        tier2 = (
            lambda: discover_semantic_scholar(doi),
            lambda: discover_arxiv(doi=doi, title=title),
            lambda: discover_core(doi),
            lambda: discover_zenodo(doi),
        )
        for fn in tier1:
            try:
                r = fn()
                add_many(list(r.get("candidates") or []))
            except Exception:  # noqa: BLE001
                continue
        pdf_n = sum(1 for c in out if c.get("representation_hint") == "pdf")
        if pdf_n < 1 or len(out) < 3:
            for fn in tier2:
                try:
                    r = fn()
                    add_many(list(r.get("candidates") or []))
                except Exception:  # noqa: BLE001
                    continue
                if sum(1 for c in out if c.get("representation_hint") == "pdf") >= 2:
                    break
    elif openalex_id:
        try:
            r = discover_openalex(openalex_id=openalex_id)
            add_many(list(r.get("candidates") or []))
        except Exception:  # noqa: BLE001
            pass

    # Prefer PDFs earlier in list for download order (ranking still final)
    out.sort(key=lambda c: 0 if c.get("representation_hint") == "pdf" else 1)
    return out
