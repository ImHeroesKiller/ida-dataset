"""Phase 1 placeholder connectors — dry-run only, no network I/O."""

from __future__ import annotations

from typing import Any, Optional, Type

from automation.connectors.base_connector import BaseConnector
from automation.connectors.types import DocumentRef, SearchQuery, SearchResult


class PlaceholderConnector(BaseConnector):
    """Shared implementation for architecture-only connectors."""

    def connect(self) -> dict[str, Any]:
        self._connected = True
        return {
            "ok": True,
            "connector_id": self.connector_id,
            "dry_run": self.dry_run(),
            "message": f"{self.name} connected (placeholder)",
        }

    def health(self) -> dict[str, Any]:
        return {
            "ok": self.is_enabled(),
            "status": "idle" if self.is_enabled() else "disabled",
            "message": "Phase 1 placeholder — no external probe",
        }

    def search(self, query: SearchQuery) -> list[SearchResult]:
        if not self.is_enabled():
            return []
        if not self._connected:
            self.connect()
        return self.placeholder_search(query)

    def fetch(self, url: str) -> dict[str, Any]:
        if not self.domain_allowed(url) and not url.startswith("file:"):
            raise PermissionError(f"domain_not_allowed:{url}")
        if not self.robots_txt_placeholder(url):
            raise PermissionError(f"robots_disallow:{url}")
        return {
            "ok": True,
            "url": url,
            "dry_run": True,
            "content": None,
            "message": "Phase 1 placeholder fetch — no network",
        }

    def download(self, url: str, dest: Optional[str] = None) -> DocumentRef:
        _ = dest
        if not self.domain_allowed(url) and not url.startswith("file:"):
            raise PermissionError(f"domain_not_allowed:{url}")
        return self.placeholder_document(url)

    def extract_metadata(self, payload: dict[str, Any]) -> dict[str, Any]:
        return {
            "title": payload.get("title") or payload.get("url") or "",
            "url": payload.get("url") or "",
            "connector_id": self.connector_id,
            "source_id": self.source_id,
            "dry_run": True,
        }

    def supported_formats(self) -> list[str]:
        return ["text/plain", "application/pdf", "text/html", "application/json"]

    def rate_limit(self) -> int:
        return int(self.config.get("rate_limit_per_minute") or 30)

    def cache_policy(self) -> dict[str, Any]:
        return {
            "enabled": bool(self.config.get("caching", True)),
            "ttl_seconds": int(self.config.get("cache_ttl_seconds") or 86400),
        }

    def trust_score(self) -> float:
        return float(self.config.get("trust_score") or 0.7)

    def shutdown(self) -> None:
        self._connected = False


def _cls(name: str, type_name: str) -> Type[PlaceholderConnector]:
    return type(
        name,
        (PlaceholderConnector,),
        {"name": name.replace("_", " "), "connector_type": type_name},
    )


CONNECTOR_CLASSES: dict[str, Type[BaseConnector]] = {
    "world_bank": _cls("WorldBankConnector", "government"),
    "bps_indonesia": _cls("BpsIndonesiaConnector", "government"),
    "oecd": _cls("OecdConnector", "research"),
    "sec_annual_reports": _cls("SecAnnualReportsConnector", "corporate"),
    "company_annual_reports": _cls("CompanyAnnualReportsConnector", "corporate"),
    "github": _cls("GitHubConnector", "repository"),
    "rss": _cls("RssConnector", "rss"),
    "generic_search": _cls("GenericSearchConnector", "search"),
    "generic_website": _cls("GenericWebsiteConnector", "documentation"),
    "local_files": _cls("LocalFilesConnector", "internal"),
    "pdf_repository": _cls("PdfRepositoryConnector", "repository"),
    "internal_dataset": _cls("InternalDatasetConnector", "internal"),
}
