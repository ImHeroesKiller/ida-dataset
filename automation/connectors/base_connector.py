"""Base connector interface — every connector must implement these methods."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional
from urllib.parse import urlparse

from .types import DocumentRef, SearchQuery, SearchResult, utc_now_iso


class BaseConnector(ABC):
    """Controlled knowledge acquisition connector.

    Connectors only acquire documents/metadata.
    They never write domain datasets and never extract knowledge.
    """

    connector_id: str = "CONN-UNKNOWN"
    name: str = "Unknown"
    connector_type: str = "future"
    source_id: str = ""

    def __init__(self, config: dict[str, Any]):
        self.config = config
        self.connector_id = str(config.get("connector_id", self.connector_id))
        self.name = str(config.get("name", self.name))
        self.connector_type = str(config.get("type", self.connector_type))
        self.source_id = str(config.get("source_id", self.source_id))
        self._connected = False

    # ---- mandatory interface ----
    @abstractmethod
    def connect(self) -> dict[str, Any]:
        ...

    @abstractmethod
    def health(self) -> dict[str, Any]:
        ...

    @abstractmethod
    def search(self, query: SearchQuery) -> list[SearchResult]:
        ...

    @abstractmethod
    def fetch(self, url: str) -> dict[str, Any]:
        ...

    @abstractmethod
    def download(self, url: str, dest: Optional[str] = None) -> DocumentRef:
        ...

    @abstractmethod
    def extract_metadata(self, payload: dict[str, Any]) -> dict[str, Any]:
        ...

    @abstractmethod
    def supported_formats(self) -> list[str]:
        ...

    @abstractmethod
    def rate_limit(self) -> int:
        ...

    @abstractmethod
    def cache_policy(self) -> dict[str, Any]:
        ...

    @abstractmethod
    def trust_score(self) -> float:
        ...

    @abstractmethod
    def shutdown(self) -> None:
        ...

    # ---- shared helpers ----
    def is_enabled(self) -> bool:
        return bool(self.config.get("enabled", False))

    def dry_run(self) -> bool:
        return bool(self.config.get("dry_run", True))

    def allowed_domains(self) -> list[str]:
        return list(self.config.get("allowed_domains") or [])

    def blocked_domains(self) -> list[str]:
        return list(self.config.get("blocked_domains") or [])

    def domain_allowed(self, url: str) -> bool:
        host = (urlparse(url).hostname or "").lower()
        if host.startswith("www."):
            host = host[4:]
        if not host and url.startswith("file:"):
            return True

        def _norm(d: str) -> str:
            d = (d or "").lower()
            return d[4:] if d.startswith("www.") else d

        blocked = {_norm(d) for d in self.blocked_domains()}
        if host in blocked or any(host.endswith("." + b) for b in blocked):
            return False
        allowed = {_norm(d) for d in self.allowed_domains()}
        if not allowed:
            # empty allow-list: only internal/local style connectors may proceed
            return self.connector_type in {"internal", "rss"} or url.startswith("file:")
        return host in allowed or any(host.endswith("." + a) for a in allowed)

    def robots_txt_placeholder(self, url: str) -> bool:
        """Placeholder robots.txt respect — always True in Phase 1 architecture."""
        _ = url
        return True

    def placeholder_search(self, query: SearchQuery) -> list[SearchResult]:
        """Architecture-only search result (no network)."""
        domains = self.allowed_domains()
        base = f"https://{domains[0]}" if domains else "https://example.invalid"
        return [
            SearchResult.create(
                connector_id=self.connector_id,
                source_id=self.source_id,
                title=f"[dry-run] {self.name}: {query.query}",
                url=f"{base}/search?q={query.query.replace(' ', '+')}",
                snippet="Phase 1 placeholder result — no external fetch performed.",
                trust_score=self.trust_score(),
                dry_run=True,
                metadata={"phase": "1", "connector": self.name},
            )
        ]

    def placeholder_document(self, url: str, *, mission_id: str | None = None) -> DocumentRef:
        return DocumentRef.create(
            connector_id=self.connector_id,
            source_id=self.source_id,
            trust_score=self.trust_score(),
            original_url=url,
            checksum="dry-run-no-content",
            version="0.0.0-phase1",
            title=f"[dry-run] {self.name}",
            content_type="text/plain",
            status="incoming",
            dry_run=True,
            mission_id=mission_id,
            bytes=0,
            notes="Phase 1 placeholder document — no binary downloaded.",
            metadata={"phase": "1"},
            retrieved_at=utc_now_iso(),
        )
