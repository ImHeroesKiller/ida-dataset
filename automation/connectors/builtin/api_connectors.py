"""Production API connectors — real network I/O, no fabricated results.

Each connector discovers and downloads documents from trusted open APIs.
Connectors never write domain datasets.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any, Optional

from automation.connectors.base_connector import BaseConnector
from automation.connectors.http_utils import DEFAULT_UA, http_get, urlencode_query
from automation.connectors.types import DocumentRef, SearchQuery, SearchResult, utc_now_iso


def _slug(s: str, n: int = 80) -> str:
    s = re.sub(r"\s+", " ", (s or "").strip())
    return s[:n]


class HttpApiConnector(BaseConnector):
    """Base for HTTP JSON API connectors."""

    def connect(self) -> dict[str, Any]:
        self._connected = True
        return {"ok": True, "connector_id": self.connector_id, "dry_run": self.dry_run()}

    def health(self) -> dict[str, Any]:
        if not self.is_enabled():
            return {"ok": False, "status": "disabled"}
        # lightweight probe
        base = (self.config.get("health_url") or self.config.get("api_endpoint") or "").strip()
        if not base:
            domains = self.allowed_domains()
            base = f"https://{domains[0]}" if domains else ""
        if not base or self.dry_run():
            return {
                "ok": True,
                "status": "idle" if self.dry_run() else "healthy",
                "message": "dry_run" if self.dry_run() else "no_health_probe",
            }
        res = http_get(base, timeout=min(15.0, float(self.config.get("timeout_seconds") or 30)))
        return {
            "ok": bool(res.get("ok")),
            "status": "healthy" if res.get("ok") else "error",
            "message": res.get("error") or f"HTTP {res.get('status')}",
            "http_status": res.get("status"),
        }

    def fetch(self, url: str) -> dict[str, Any]:
        if not self.domain_allowed(url):
            raise PermissionError(f"domain_not_allowed:{url}")
        if self.dry_run():
            return {"ok": True, "url": url, "dry_run": True, "content": None}
        return http_get(
            url,
            timeout=float(self.config.get("timeout_seconds") or 30),
            retries=int(self.config.get("retries") or 2),
            headers={"User-Agent": str(self.config.get("user_agent") or DEFAULT_UA)},
        )

    def download(self, url: str, dest: Optional[str] = None) -> DocumentRef:
        if not self.domain_allowed(url) and not url.startswith("file:"):
            raise PermissionError(f"domain_not_allowed:{url}")
        if self.dry_run():
            return self.placeholder_document(url)

        res = self.fetch(url)
        if not res.get("ok"):
            raise RuntimeError(res.get("error") or "download_failed")

        text = res.get("text") or ""
        raw = text.encode("utf-8")
        checksum = hashlib.sha256(raw).hexdigest()
        doc_id = f"DOC-{checksum[:12].upper()}"
        root = Path(self.config.get("_repo_root") or Path.cwd())
        store = root / "automation" / "raw_documents" / self.connector_id
        store.mkdir(parents=True, exist_ok=True)
        local = Path(dest) if dest else store / f"{doc_id}.txt"
        local.write_bytes(raw)

        ctype = res.get("content_type") or "text/plain"
        title = ""
        meta = res.get("json") if isinstance(res.get("json"), dict) else {}
        if isinstance(meta, dict):
            title = str(meta.get("title") or meta.get("display_title") or "")[:200]

        return DocumentRef.create(
            document_id=doc_id,
            connector_id=self.connector_id,
            source_id=self.source_id,
            trust_score=self.trust_score(),
            original_url=url,
            checksum=checksum,
            version="2.0",
            title=title or _slug(url, 100),
            content_type=ctype,
            local_path=str(local),
            status="incoming",
            dry_run=False,
            bytes=len(raw),
            notes="Acquired via HTTP connector",
            metadata={
                "http_status": res.get("status"),
                "snippet": text[:500],
                "acquired": True,
            },
            retrieved_at=utc_now_iso(),
        )

    def extract_metadata(self, payload: dict[str, Any]) -> dict[str, Any]:
        return {
            "title": payload.get("title") or "",
            "url": payload.get("url") or payload.get("original_url") or "",
            "connector_id": self.connector_id,
            "source_id": self.source_id,
            "dry_run": self.dry_run(),
        }

    def supported_formats(self) -> list[str]:
        return ["application/json", "text/html", "text/plain", "application/pdf"]

    def rate_limit(self) -> int:
        return int(self.config.get("rate_limit_per_minute") or 20)

    def cache_policy(self) -> dict[str, Any]:
        return {
            "enabled": bool(self.config.get("caching", True)),
            "ttl_seconds": int(self.config.get("cache_ttl_seconds") or 86400),
        }

    def trust_score(self) -> float:
        return float(self.config.get("trust_score") or 0.85)

    def shutdown(self) -> None:
        self._connected = False

    def search(self, query: SearchQuery) -> list[SearchResult]:
        raise NotImplementedError


class WorldBankConnector(HttpApiConnector):
    """World Bank Documents & Reports search API (public)."""

    name = "World Bank"
    connector_type = "government"

    def search(self, query: SearchQuery) -> list[SearchResult]:
        if not self.is_enabled():
            return []
        if not self._connected:
            self.connect()
        if self.dry_run():
            return self.placeholder_search(query)

        q = query.query or "Indonesia"
        # Prefer Indonesia-focused public WDS API
        api = (
            "https://search.worldbank.org/api/v2/wds?"
            + urlencode_query(
                {
                    "format": "json",
                    "qterm": q,
                    "fl": "docdt,count,display_title,abstracts,url,docty,lang",
                    "rows": min(query.limit, 10),
                    "os": 0,
                }
            )
        )
        res = http_get(api, timeout=float(self.config.get("timeout_seconds") or 30))
        if not res.get("ok") or not res.get("json"):
            # fallback documents endpoint style
            return []

        data = res["json"]
        docs = data.get("documents") or data.get("osr") or []
        if isinstance(docs, dict):
            docs = list(docs.values())
        out: list[SearchResult] = []
        for row in docs[: query.limit]:
            if not isinstance(row, dict):
                continue
            title = str(
                row.get("display_title")
                or row.get("title")
                or row.get("docdt")
                or "World Bank document"
            )
            url = str(
                row.get("url")
                or row.get("pdfurl")
                or row.get("guid")
                or f"https://documents.worldbank.org/search?q={q.replace(' ', '+')}"
            )
            if url and not url.startswith("http"):
                url = f"https://documents.worldbank.org{url}" if url.startswith("/") else url
            abstract = ""
            abs_field = row.get("abstracts") or row.get("abstract") or ""
            if isinstance(abs_field, dict):
                abstract = str(next(iter(abs_field.values()), ""))[:400]
            else:
                abstract = str(abs_field)[:400]
            out.append(
                SearchResult.create(
                    connector_id=self.connector_id,
                    source_id=self.source_id or "SRC-000004",
                    title=_slug(title, 200),
                    url=url,
                    snippet=abstract or f"World Bank document related to: {q}",
                    trust_score=self.trust_score(),
                    dry_run=False,
                    metadata={
                        "published_at": str(row.get("docdt") or row.get("publisheddate") or ""),
                        "doc_type": str(row.get("docty") or ""),
                        "language": str(row.get("lang") or ""),
                        "api": "worldbank_wds_v2",
                    },
                )
            )
        return out


class OpenAlexConnector(HttpApiConnector):
    """OpenAlex works API — open scholarly metadata."""

    name = "OpenAlex"
    connector_type = "research"

    def search(self, query: SearchQuery) -> list[SearchResult]:
        if not self.is_enabled():
            return []
        if not self._connected:
            self.connect()
        if self.dry_run():
            return self.placeholder_search(query)

        q = query.query or "Indonesia industry"
        api = (
            "https://api.openalex.org/works?"
            + urlencode_query(
                {
                    "search": q,
                    "per_page": min(query.limit, 10),
                    "mailto": self.config.get("mailto") or "ida-dataset@users.noreply.github.com",
                }
            )
        )
        res = http_get(api, timeout=float(self.config.get("timeout_seconds") or 30))
        if not res.get("ok") or not isinstance(res.get("json"), dict):
            return []
        results = (res["json"] or {}).get("results") or []
        out: list[SearchResult] = []
        for row in results[: query.limit]:
            title = str(row.get("display_name") or row.get("title") or "OpenAlex work")
            # Prefer OpenAlex id URL (in domain allow-list) for reliable download
            openalex_id = str(row.get("id") or "")
            loc = row.get("primary_location") or {}
            landing = str(loc.get("landing_page_url") or loc.get("pdf_url") or "")
            url = openalex_id or landing
            abstract = ""
            inv = row.get("abstract_inverted_index")
            if isinstance(inv, dict):
                # reconstruct simple abstract from inverted index
                positions: list[tuple[int, str]] = []
                for word, idxs in inv.items():
                    for i in idxs:
                        positions.append((int(i), str(word)))
                positions.sort()
                abstract = " ".join(w for _, w in positions)[:500]
            concepts = row.get("concepts") or []
            concept_names = [
                str(c.get("display_name"))
                for c in concepts[:8]
                if isinstance(c, dict) and c.get("display_name")
            ]
            out.append(
                SearchResult.create(
                    connector_id=self.connector_id,
                    source_id=self.source_id or "SRC-OPENALEX",
                    title=_slug(title, 200),
                    url=url or f"https://openalex.org/works?search={q.replace(' ', '+')}",
                    snippet=abstract or ", ".join(concept_names)[:400],
                    trust_score=self.trust_score(),
                    dry_run=False,
                    metadata={
                        "published_at": str(row.get("publication_date") or row.get("publication_year") or ""),
                        "concepts": concept_names,
                        "cited_by_count": row.get("cited_by_count"),
                        "api": "openalex_works",
                        "landing_page_url": landing,
                        "openalex_id": openalex_id,
                    },
                )
            )
        return out


class CrossrefConnector(HttpApiConnector):
    """Crossref works API — bibliographic metadata."""

    name = "Crossref"
    connector_type = "research"

    def search(self, query: SearchQuery) -> list[SearchResult]:
        if not self.is_enabled():
            return []
        if not self._connected:
            self.connect()
        if self.dry_run():
            return self.placeholder_search(query)

        q = query.query or "Indonesia industry"
        api = (
            "https://api.crossref.org/works?"
            + urlencode_query({"query": q, "rows": min(query.limit, 10)})
        )
        res = http_get(
            api,
            timeout=float(self.config.get("timeout_seconds") or 30),
            headers={
                "User-Agent": str(
                    self.config.get("user_agent")
                    or "IDA-Dataset-Factory/2.0 (mailto:ida-dataset@users.noreply.github.com)"
                )
            },
        )
        if not res.get("ok") or not isinstance(res.get("json"), dict):
            return []
        items = ((res["json"] or {}).get("message") or {}).get("items") or []
        out: list[SearchResult] = []
        for row in items[: query.limit]:
            titles = row.get("title") or []
            title = titles[0] if titles else "Crossref work"
            doi = str(row.get("DOI") or "")
            # Prefer Crossref API work URL (allow-listed) over publisher DOI landing pages
            api_url = (
                f"https://api.crossref.org/works/{doi}"
                if doi
                else "https://api.crossref.org/works"
            )
            abstract = re.sub(r"<[^>]+>", " ", str(row.get("abstract") or ""))[:400]
            container = row.get("container-title") or []
            out.append(
                SearchResult.create(
                    connector_id=self.connector_id,
                    source_id=self.source_id or "SRC-CROSSREF",
                    title=_slug(str(title), 200),
                    url=api_url,
                    snippet=abstract
                    or (container[0] if container else f"Crossref result for {q}")[:400],
                    trust_score=self.trust_score(),
                    dry_run=False,
                    metadata={
                        "published_at": str(
                            (row.get("published-print") or row.get("published-online") or {})
                            .get("date-parts", [[None]])[0][0]
                            or ""
                        ),
                        "DOI": doi,
                        "type": row.get("type"),
                        "api": "crossref_works",
                        "landing_url": str(row.get("URL") or ""),
                    },
                )
            )
        return out


class OecdConnector(HttpApiConnector):
    """OECD library search via public site JSON-ish fallback to HTML search results page metadata."""

    name = "OECD"
    connector_type = "research"

    def search(self, query: SearchQuery) -> list[SearchResult]:
        if not self.is_enabled():
            return []
        if not self._connected:
            self.connect()
        if self.dry_run():
            return self.placeholder_search(query)

        q = query.query or "Indonesia"
        # OECD library search page — extract links when API unavailable
        api = f"https://www.oecd.org/search/?q={q.replace(' ', '+')}&orderBy=mostRelevant"
        res = http_get(api, timeout=float(self.config.get("timeout_seconds") or 30))
        if not res.get("ok"):
            return []
        html = res.get("text") or ""
        # pull absolute oecd.org links with titles
        links = re.findall(
            r'href="(https://www\.oecd\.org/[^"#?]+)"[^>]*>([^<]{12,180})</a>',
            html,
            flags=re.I,
        )
        seen: set[str] = set()
        out: list[SearchResult] = []
        for url, title in links:
            u = url.split("?")[0]
            if u in seen:
                continue
            if any(x in u for x in ("/search", "/assets/", ".css", ".js", "/login")):
                continue
            seen.add(u)
            title = re.sub(r"\s+", " ", title).strip()
            out.append(
                SearchResult.create(
                    connector_id=self.connector_id,
                    source_id=self.source_id or "SRC-000005",
                    title=_slug(title, 200),
                    url=u,
                    snippet=f"OECD public page related to: {q}",
                    trust_score=self.trust_score(),
                    dry_run=False,
                    metadata={"api": "oecd_html_search", "published_at": ""},
                )
            )
            if len(out) >= query.limit:
                break
        return out


class AdbConnector(HttpApiConnector):
    """ADB publications search (HTML scrape of public search)."""

    name = "Asian Development Bank"
    connector_type = "research"

    def search(self, query: SearchQuery) -> list[SearchResult]:
        if not self.is_enabled():
            return []
        if not self._connected:
            self.connect()
        if self.dry_run():
            return self.placeholder_search(query)

        q = query.query or "Indonesia"
        api = f"https://www.adb.org/search?keywords={q.replace(' ', '+')}"
        res = http_get(api, timeout=float(self.config.get("timeout_seconds") or 30))
        if not res.get("ok"):
            return []
        html = res.get("text") or ""
        links = re.findall(
            r'href="(https://www\.adb\.org/(?:publications|news|projects)/[^"#]+)"[^>]*>([^<]{10,180})</a>',
            html,
            flags=re.I,
        )
        if not links:
            links = re.findall(
                r'href="(/publications/[^"#]+)"[^>]*>([^<]{10,180})</a>',
                html,
                flags=re.I,
            )
            links = [(f"https://www.adb.org{u}", t) for u, t in links]
        seen: set[str] = set()
        out: list[SearchResult] = []
        for url, title in links:
            u = url.split("?")[0]
            if u in seen:
                continue
            seen.add(u)
            out.append(
                SearchResult.create(
                    connector_id=self.connector_id,
                    source_id=self.source_id or "SRC-000006",
                    title=_slug(re.sub(r"\s+", " ", title).strip(), 200),
                    url=u,
                    snippet=f"ADB public content related to: {q}",
                    trust_score=self.trust_score(),
                    dry_run=False,
                    metadata={"api": "adb_html_search", "published_at": ""},
                )
            )
            if len(out) >= query.limit:
                break
        return out


class BpsConnector(HttpApiConnector):
    """BPS Indonesia public site search (HTML)."""

    name = "BPS Indonesia"
    connector_type = "government"

    def search(self, query: SearchQuery) -> list[SearchResult]:
        if not self.is_enabled():
            return []
        if not self._connected:
            self.connect()
        if self.dry_run():
            return self.placeholder_search(query)

        q = query.query or "industri"
        api = f"https://www.bps.go.id/id/search?keyword={q.replace(' ', '+')}"
        res = http_get(api, timeout=float(self.config.get("timeout_seconds") or 30))
        if not res.get("ok"):
            # alternate
            api2 = f"https://www.bps.go.id/en/search?keyword={q.replace(' ', '+')}"
            res = http_get(api2, timeout=float(self.config.get("timeout_seconds") or 30))
        if not res.get("ok"):
            return []
        html = res.get("text") or ""
        links = re.findall(
            r'href="(https://www\.bps\.go\.id/[^"#]+)"[^>]*>([^<]{10,180})</a>',
            html,
            flags=re.I,
        )
        if not links:
            links = re.findall(
                r'href="(/id/[^"#]+|/en/[^"#]+)"[^>]*>([^<]{10,180})</a>',
                html,
                flags=re.I,
            )
            links = [(f"https://www.bps.go.id{u}", t) for u, t in links]
        seen: set[str] = set()
        out: list[SearchResult] = []
        for url, title in links:
            u = url.split("?")[0]
            if u in seen or "/search" in u:
                continue
            seen.add(u)
            out.append(
                SearchResult.create(
                    connector_id=self.connector_id,
                    source_id=self.source_id or "SRC-000001",
                    title=_slug(re.sub(r"\s+", " ", title).strip(), 200),
                    url=u,
                    snippet=f"BPS public page related to: {q}",
                    trust_score=self.trust_score(),
                    dry_run=False,
                    metadata={"api": "bps_html_search", "published_at": ""},
                )
            )
            if len(out) >= query.limit:
                break
        return out


# Keep placeholders for remaining classes (interfaces ready)
from automation.connectors.builtin.stubs import PlaceholderConnector  # noqa: E402


class GenericWebsiteConnector(HttpApiConnector):
    """Generic HTML page fetch for allow-listed domains."""

    name = "Generic Website"
    connector_type = "documentation"

    def search(self, query: SearchQuery) -> list[SearchResult]:
        if not self.is_enabled():
            return []
        if self.dry_run():
            return self.placeholder_search(query)
        domains = self.allowed_domains()
        if not domains:
            return []
        base = f"https://{domains[0]}"
        q = query.query or ""
        url = f"{base}/?s={q.replace(' ', '+')}" if q else base
        res = http_get(url, timeout=float(self.config.get("timeout_seconds") or 30))
        if not res.get("ok"):
            return []
        return [
            SearchResult.create(
                connector_id=self.connector_id,
                source_id=self.source_id,
                title=f"{self.name}: {q or domains[0]}",
                url=url,
                snippet=(res.get("text") or "")[:300],
                trust_score=self.trust_score(),
                dry_run=False,
                metadata={"api": "generic_html", "published_at": ""},
            )
        ]


API_CONNECTOR_CLASSES: dict[str, type[BaseConnector]] = {
    "world_bank": WorldBankConnector,
    "bps_indonesia": BpsConnector,
    "oecd": OecdConnector,
    "adb": AdbConnector,
    "openalex": OpenAlexConnector,
    "crossref": CrossrefConnector,
    "generic_website": GenericWebsiteConnector,
    # remaining use placeholders until dedicated implementation
    "sec_annual_reports": PlaceholderConnector,
    "company_annual_reports": PlaceholderConnector,
    "github": PlaceholderConnector,
    "rss": PlaceholderConnector,
    "generic_search": PlaceholderConnector,
    "local_files": PlaceholderConnector,
    "pdf_repository": PlaceholderConnector,
    "internal_dataset": PlaceholderConnector,
    "kemenperin": GenericWebsiteConnector,
    "kemnaker": GenericWebsiteConnector,
    "lkpp": GenericWebsiteConnector,
    "oss_indonesia": GenericWebsiteConnector,
    "apindo": GenericWebsiteConnector,
    "kadin": GenericWebsiteConnector,
}
