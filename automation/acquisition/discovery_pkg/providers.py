"""Discovery provider adapters — discover URLs only; auto-disable without credentials."""

from __future__ import annotations

import json
import os
import time
from typing import Any, Optional
from urllib.parse import quote_plus, urlencode

from automation.acquisition.discovery import discover_urls
from automation.acquisition.discovery_pkg.base import BaseDiscoveryProvider
from automation.connectors.http_utils import http_get


def _item(url: str, title: str = "", snippet: str = "", provider_id: str = "", published_at: str = "") -> dict[str, Any]:
    return {
        "url": url,
        "title": (title or "")[:200],
        "snippet": (snippet or "")[:400],
        "published_at": published_at or "",
        "provider_id": provider_id,
        "discovery_only": True,
    }


class TrustedSiteProvider(BaseDiscoveryProvider):
    """Always-on: emits site-scoped query metadata (no external API)."""

    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        # This provider does not hit the network; layer uses its queries for other providers
        # and for connector site targeting.
        return []

    def health(self) -> dict[str, Any]:
        return {"ok": True, "status": "healthy", "message": "always_available"}


class GoogleCseProvider(BaseDiscoveryProvider):
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        key = os.environ.get("GOOGLE_SEARCH_API_KEY", "").strip()
        cx = os.environ.get("GOOGLE_SEARCH_ENGINE_ID", "").strip()
        if not key or not cx:
            return []
        params = {
            "key": key,
            "cx": cx,
            "q": query,
            "num": min(limit, 10),
        }
        url = f"{self.config.get('base_url')}?{urlencode(params)}"
        res = http_get(url, timeout=float(self.config.get("timeout") or 20), retries=1)
        if not res.get("ok") or not isinstance(res.get("json"), dict):
            return []
        out = []
        for item in (res["json"].get("items") or [])[:limit]:
            out.append(
                _item(
                    str(item.get("link") or ""),
                    str(item.get("title") or ""),
                    str(item.get("snippet") or ""),
                    self.provider_id,
                )
            )
        return [x for x in out if x["url"]]

    def health(self) -> dict[str, Any]:
        ok = bool(os.environ.get("GOOGLE_SEARCH_API_KEY") and os.environ.get("GOOGLE_SEARCH_ENGINE_ID"))
        return {"ok": ok, "status": "healthy" if ok else "offline", "message": "credentials" if ok else "missing_credentials"}


class BingProvider(BaseDiscoveryProvider):
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        key = os.environ.get("BING_SEARCH_API_KEY", "").strip()
        if not key:
            return []
        url = f"{self.config.get('base_url')}?{urlencode({'q': query, 'count': min(limit, 10)})}"
        res = http_get(
            url,
            headers={"Ocp-Apim-Subscription-Key": key},
            timeout=float(self.config.get("timeout") or 20),
            retries=1,
        )
        if not res.get("ok") or not isinstance(res.get("json"), dict):
            return []
        out = []
        for item in ((res["json"].get("webPages") or {}).get("value") or [])[:limit]:
            out.append(
                _item(
                    str(item.get("url") or ""),
                    str(item.get("name") or ""),
                    str(item.get("snippet") or ""),
                    self.provider_id,
                )
            )
        return [x for x in out if x["url"]]

    def health(self) -> dict[str, Any]:
        ok = bool(os.environ.get("BING_SEARCH_API_KEY"))
        return {"ok": ok, "status": "healthy" if ok else "offline", "message": "credentials" if ok else "missing_credentials"}


class BraveProvider(BaseDiscoveryProvider):
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        key = os.environ.get("BRAVE_SEARCH_API_KEY", "").strip()
        if not key:
            return []
        url = f"{self.config.get('base_url')}?{urlencode({'q': query, 'count': min(limit, 10)})}"
        res = http_get(
            url,
            headers={"X-Subscription-Token": key, "Accept": "application/json"},
            timeout=float(self.config.get("timeout") or 20),
            retries=1,
        )
        if not res.get("ok") or not isinstance(res.get("json"), dict):
            return []
        out = []
        for item in ((res["json"].get("web") or {}).get("results") or [])[:limit]:
            out.append(
                _item(
                    str(item.get("url") or ""),
                    str(item.get("title") or ""),
                    str(item.get("description") or ""),
                    self.provider_id,
                )
            )
        return [x for x in out if x["url"]]

    def health(self) -> dict[str, Any]:
        ok = bool(os.environ.get("BRAVE_SEARCH_API_KEY"))
        return {"ok": ok, "status": "healthy" if ok else "offline", "message": "credentials" if ok else "missing_credentials"}


class SerpApiProvider(BaseDiscoveryProvider):
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        key = os.environ.get("SERPAPI_API_KEY", "").strip()
        if not key:
            return []
        params = {"engine": "google", "q": query, "api_key": key, "num": min(limit, 10)}
        url = f"{self.config.get('base_url')}?{urlencode(params)}"
        res = http_get(url, timeout=float(self.config.get("timeout") or 25), retries=1)
        if not res.get("ok") or not isinstance(res.get("json"), dict):
            return []
        out = []
        for item in (res["json"].get("organic_results") or [])[:limit]:
            out.append(
                _item(
                    str(item.get("link") or ""),
                    str(item.get("title") or ""),
                    str(item.get("snippet") or ""),
                    self.provider_id,
                )
            )
        return [x for x in out if x["url"]]

    def health(self) -> dict[str, Any]:
        ok = bool(os.environ.get("SERPAPI_API_KEY"))
        return {"ok": ok, "status": "healthy" if ok else "offline", "message": "credentials" if ok else "missing_credentials"}


class TavilyProvider(BaseDiscoveryProvider):
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        key = os.environ.get("TAVILY_API_KEY", "").strip()
        if not key:
            return []
        # Tavily expects POST; use GET-compatible workaround via query if available
        # Prefer simple GET to search endpoint is not standard — use urllib POST
        import urllib.request

        payload = json.dumps(
            {"api_key": key, "query": query, "max_results": min(limit, 10), "include_answer": False}
        ).encode("utf-8")
        req = urllib.request.Request(
            str(self.config.get("base_url") or "https://api.tavily.com/search"),
            data=payload,
            headers={"Content-Type": "application/json", "User-Agent": "IDA-Dataset-Factory/2.0"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=float(self.config.get("timeout") or 25)) as resp:
                data = json.loads(resp.read().decode("utf-8", errors="replace"))
        except Exception:  # noqa: BLE001
            return []
        out = []
        for item in (data.get("results") or [])[:limit]:
            out.append(
                _item(
                    str(item.get("url") or ""),
                    str(item.get("title") or ""),
                    str(item.get("content") or "")[:400],
                    self.provider_id,
                )
            )
        return [x for x in out if x["url"]]

    def health(self) -> dict[str, Any]:
        ok = bool(os.environ.get("TAVILY_API_KEY"))
        return {"ok": ok, "status": "healthy" if ok else "offline", "message": "credentials" if ok else "missing_credentials"}


class YandexProvider(BaseDiscoveryProvider):
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        # Yandex XML typically needs user+key; without full config return empty
        key = os.environ.get("YANDEX_API_KEY", "").strip()
        if not key:
            return []
        # Minimal probe — many setups need user id; skip network if incomplete
        user = os.environ.get("YANDEX_USER", "").strip()
        if not user:
            return []
        params = {"user": user, "key": key, "query": query}
        url = f"{self.config.get('base_url')}?{urlencode(params)}"
        res = http_get(url, timeout=float(self.config.get("timeout") or 20), retries=1)
        if not res.get("ok"):
            return []
        # parse simple urls from XML
        import re

        links = re.findall(r"<url>(https?://[^<]+)</url>", res.get("text") or "", flags=re.I)
        return [_item(u, provider_id=self.provider_id) for u in links[:limit]]

    def health(self) -> dict[str, Any]:
        ok = bool(os.environ.get("YANDEX_API_KEY"))
        return {"ok": ok, "status": "healthy" if ok else "offline", "message": "credentials" if ok else "missing_credentials"}


class CommonCrawlProvider(BaseDiscoveryProvider):
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        if os.environ.get("COMMONCRAWL_ENABLED", "").strip() not in {"1", "true", "yes"}:
            return []
        # CDX API style — use query as domain or url pattern when site: present
        domain = ""
        if "site:" in query:
            part = query.split("site:", 1)[1].split()[0]
            domain = part.strip()
        if not domain:
            return []
        # Common Crawl index (example endpoint; may vary by crawl id)
        index_url = (
            f"https://index.commoncrawl.org/CC-MAIN-2024-10-index?"
            f"{urlencode({'url': f'*.{domain}/*', 'output': 'json', 'limit': min(limit, 20)})}"
        )
        res = http_get(index_url, timeout=float(self.config.get("timeout") or 30), retries=1)
        if not res.get("ok"):
            return []
        out = []
        for line in (res.get("text") or "").splitlines()[:limit]:
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            u = str(row.get("url") or "")
            if u:
                out.append(_item(u, provider_id=self.provider_id))
        return out

    def health(self) -> dict[str, Any]:
        ok = os.environ.get("COMMONCRAWL_ENABLED", "").strip() in {"1", "true", "yes"}
        return {"ok": ok, "status": "healthy" if ok else "offline", "message": "toggle" if ok else "disabled"}


class FeedProvider(BaseDiscoveryProvider):
    """RSS / Atom / Sitemap discovery from trusted source base URLs."""

    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        sources = kwargs.get("trusted_sources") or []
        api_type = str(self.config.get("api_type") or "rss")
        out: list[dict[str, Any]] = []
        for s in sources[:12]:
            base = str(s.get("base_url") or "")
            rss = s.get("rss_feed")
            kwargs_disc: dict[str, Any] = {"base_url": base, "limit": max(3, limit // 4)}
            if api_type == "rss":
                kwargs_disc["rss_feed"] = rss
            elif api_type == "atom":
                kwargs_disc["atom_feed"] = rss  # reuse if atom-like
            elif api_type == "sitemap":
                if base:
                    kwargs_disc["sitemap_url"] = base.rstrip("/") + "/sitemap.xml"
            try:
                found = discover_urls(**kwargs_disc)
            except Exception:  # noqa: BLE001
                found = []
            for item in found:
                out.append(
                    _item(
                        item.get("url", ""),
                        item.get("title", ""),
                        f"discovered via {api_type}",
                        self.provider_id,
                        item.get("published_at", ""),
                    )
                )
            if len(out) >= limit:
                break
        return out[:limit]

    def health(self) -> dict[str, Any]:
        return {"ok": True, "status": "healthy", "message": "feed_discovery"}


class OpenSearchProvider(BaseDiscoveryProvider):
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        # Optional: trusted sources may declare opensearch_url in notes/config later
        return []

    def health(self) -> dict[str, Any]:
        return {"ok": True, "status": "idle", "message": "optional"}


PROVIDER_CLASSES: dict[str, type[BaseDiscoveryProvider]] = {
    "google_cse": GoogleCseProvider,
    "bing": BingProvider,
    "brave": BraveProvider,
    "serpapi": SerpApiProvider,
    "tavily": TavilyProvider,
    "yandex": YandexProvider,
    "commoncrawl": CommonCrawlProvider,
    "rss": FeedProvider,
    "atom": FeedProvider,
    "sitemap": FeedProvider,
    "opensearch": OpenSearchProvider,
    "trusted_site": TrustedSiteProvider,
}


def build_provider(config: dict[str, Any]) -> Optional[BaseDiscoveryProvider]:
    api_type = str(config.get("api_type") or "")
    cls = PROVIDER_CLASSES.get(api_type)
    if not cls:
        return None
    return cls(config)
