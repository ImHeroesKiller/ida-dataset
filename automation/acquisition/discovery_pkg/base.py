"""Base discovery provider interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseDiscoveryProvider(ABC):
    """Discover candidate URLs only — never extract knowledge."""

    def __init__(self, config: dict[str, Any]):
        self.config = config
        self.provider_id = str(config.get("id") or "DISC-UNKNOWN")
        self.name = str(config.get("name") or self.provider_id)

    @abstractmethod
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        """Return list of {url, title, snippet, published_at, provider_id}."""

    @abstractmethod
    def health(self) -> dict[str, Any]:
        ...

    def quota(self) -> dict[str, Any]:
        return {
            "daily_quota": int(self.config.get("daily_quota") or 0),
            "rate_limit": int(self.config.get("rate_limit") or 0),
            "cost_per_request": float(self.config.get("cost_per_request") or 0),
        }

    def metadata(self) -> dict[str, Any]:
        return {
            "id": self.provider_id,
            "name": self.name,
            "api_type": self.config.get("api_type"),
            "supports_site_filter": bool(self.config.get("supports_site_filter")),
            "supports_date_filter": bool(self.config.get("supports_date_filter")),
            "supports_language_filter": bool(self.config.get("supports_language_filter")),
            "supports_country_filter": bool(self.config.get("supports_country_filter")),
            "priority": self.config.get("priority"),
            "enabled": self.config.get("enabled"),
            "credentials_available": self.config.get("credentials_available"),
            "status": self.config.get("status"),
            "health": self.config.get("health"),
        }
