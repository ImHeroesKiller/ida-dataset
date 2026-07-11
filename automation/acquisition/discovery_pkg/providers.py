"""Discovery provider adapters — discover URLs only.

Providers never become knowledge sources. Missing credentials → empty results
with MISCONFIGURED status reported by the registry (never silent disable).
Provider page-size caps only where the upstream API requires them.
"""

from __future__ import annotations

import json
import os
import time
from typing import Any, Optional
from urllib.parse import urlencode

from automation.acquisition.discovery import discover_urls
from automation.acquisition.discovery_pkg.base import BaseDiscoveryProvider
from automation.connectors.http_utils import http_get


def _item(
    url: str,
    title: str = "",
    snippet: str = "",
    provider_id: str = "",
    published_at: str = "",
) -> dict[str, Any]:
    return {
        "url": url,
        "title": (title or "")[:200],
        "snippet": (snippet or "")[:400],
        "published_at": published_at or "",
        "provider_id": provider_id,
        "discovery_only": True,
    }


def _provider_page_cap(api_type: str, limit: int) -> int:
    """Only API-native maxima — not arbitrary session document caps."""
    caps = {
        "google_cse": 10,  # Google CSE hard max per request
        "bing": 50,
        "brave": 20,
        "serpapi": 20,
        "tavily": 20,
        "yandex": 50,
        "commoncrawl": 100,
        "rss": 500,
        "atom": 500,
        "sitemap": 500,
    }
    cap = caps.get(api_type, 20)
    return max(1, min(int(limit or cap), cap))


def probe_tavily_connectivity() -> dict[str, Any]:
    """Explicit Tavily connectivity check with evidence (no secrets logged)."""
    key = os.environ.get("TAVILY_API_KEY", "").strip()
    if not key:
        return {
            "probed": False,
            "ok": False,
            "status": "MISCONFIGURED",
            "message": "TAVILY_API_KEY missing",
            "latency_ms": None,
        }
    import urllib.request

    payload = json.dumps(
        {
            "api_key": key,
            "query": "site:worldbank.org indonesia",
            "max_results": 1,
            "include_answer": False,
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        "https://api.tavily.com/search",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "IDA-Dataset-Factory/2.0",
        },
        method="POST",
    )
    t0 = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            code = getattr(resp, "status", 200) or 200
        latency = round((time.perf_counter() - t0) * 1000, 1)
        data = json.loads(body) if body else {}
        n = len(data.get("results") or [])
        return {
            "probed": True,
            "ok": code == 200,
            "status": "ACTIVE" if code == 200 else "ERROR",
            "message": f"http_{code}_results_{n}",
            "latency_ms": latency,
            "http_status": code,
            "result_count": n,
        }
    except Exception as exc:  # noqa: BLE001
        latency = round((time.perf_counter() - t0) * 1000, 1)
        return {
            "probed": True,
            "ok": False,
            "status": "ERROR",
            "message": f"connectivity_failed:{type(exc).__name__}",
            "latency_ms": latency,
        }


class TrustedSiteProvider(BaseDiscoveryProvider):
    """Always-on: emits site-scoped query metadata (no external API)."""

    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        return []

    def health(self) -> dict[str, Any]:
        return {"ok": True, "status": "healthy", "message": "always_available"}


class GoogleCseProvider(BaseDiscoveryProvider):
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        key = os.environ.get("GOOGLE_SEARCH_API_KEY", "").strip()
        cx = os.environ.get("GOOGLE_SEARCH_ENGINE_ID", "").strip()
        if not key or not cx:
            return []
        num = _provider_page_cap("google_cse", limit)
        params = {"key": key, "cx": cx, "q": query, "num": num}
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
        ok = bool(
            os.environ.get("GOOGLE_SEARCH_API_KEY")
            and os.environ.get("GOOGLE_SEARCH_ENGINE_ID")
        )
        return {
            "ok": ok,
            "status": "healthy" if ok else "offline",
            "message": "credentials" if ok else "missing_credentials",
        }


class BingProvider(BaseDiscoveryProvider):
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        key = os.environ.get("BING_SEARCH_API_KEY", "").strip()
        if not key:
            return []
        count = _provider_page_cap("bing", limit)
        url = f"{self.config.get('base_url')}?{urlencode({'q': query, 'count': count})}"
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
        return {
            "ok": ok,
            "status": "healthy" if ok else "offline",
            "message": "credentials" if ok else "missing_credentials",
        }


class BraveProvider(BaseDiscoveryProvider):
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        key = os.environ.get("BRAVE_SEARCH_API_KEY", "").strip()
        if not key:
            return []
        count = _provider_page_cap("brave", limit)
        url = f"{self.config.get('base_url')}?{urlencode({'q': query, 'count': count})}"
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
        return {
            "ok": ok,
            "status": "healthy" if ok else "offline",
            "message": "credentials" if ok else "missing_credentials",
        }


class SerpApiProvider(BaseDiscoveryProvider):
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        key = os.environ.get("SERPAPI_API_KEY", "").strip()
        if not key:
            return []
        num = _provider_page_cap("serpapi", limit)
        params = {"engine": "google", "q": query, "api_key": key, "num": num}
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
        return {
            "ok": ok,
            "status": "healthy" if ok else "offline",
            "message": "credentials" if ok else "missing_credentials",
        }


class TavilyProvider(BaseDiscoveryProvider):
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        key = os.environ.get("TAVILY_API_KEY", "").strip()
        if not key:
            return []
        import urllib.request

        max_results = _provider_page_cap("tavily", limit)
        payload = json.dumps(
            {
                "api_key": key,
                "query": query,
                "max_results": max_results,
                "include_answer": False,
            }
        ).encode("utf-8")
        req = urllib.request.Request(
            str(self.config.get("base_url") or "https://api.tavily.com/search"),
            data=payload,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "IDA-Dataset-Factory/2.0",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(
                req, timeout=float(self.config.get("timeout") or 25)
            ) as resp:
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
        return {
            "ok": ok,
            "status": "healthy" if ok else "offline",
            "message": "credentials" if ok else "missing_credentials",
        }


class YandexProvider(BaseDiscoveryProvider):
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        key = os.environ.get("YANDEX_API_KEY", "").strip()
        user = os.environ.get("YANDEX_USER", "").strip()
        if not key or not user:
            return []
        params = {"user": user, "key": key, "query": query}
        url = f"{self.config.get('base_url')}?{urlencode(params)}"
        res = http_get(url, timeout=float(self.config.get("timeout") or 20), retries=1)
        if not res.get("ok"):
            return []
        import re

        links = re.findall(
            r"<url>(https?://[^<]+)</url>", res.get("text") or "", flags=re.I
        )
        return [_item(u, provider_id=self.provider_id) for u in links[:limit]]

    def health(self) -> dict[str, Any]:
        ok = bool(
            os.environ.get("YANDEX_API_KEY") and os.environ.get("YANDEX_USER")
        )
        return {
            "ok": ok,
            "status": "healthy" if ok else "offline",
            "message": "credentials" if ok else "missing_credentials",
        }


class CommonCrawlProvider(BaseDiscoveryProvider):
    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        # Default ON; explicit disable only
        if os.environ.get("COMMONCRAWL_ENABLED", "1").strip().lower() in {
            "0",
            "false",
            "no",
            "off",
        }:
            return []
        domain = ""
        if "site:" in query:
            part = query.split("site:", 1)[1].split()[0]
            domain = part.strip()
        if not domain:
            return []
        page = _provider_page_cap("commoncrawl", limit)
        index_url = (
            f"https://index.commoncrawl.org/CC-MAIN-2024-10-index?"
            f"{urlencode({'url': f'*.{domain}/*', 'output': 'json', 'limit': page})}"
        )
        res = http_get(
            index_url, timeout=float(self.config.get("timeout") or 30), retries=1
        )
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
        disabled = os.environ.get("COMMONCRAWL_ENABLED", "1").strip().lower() in {
            "0",
            "false",
            "no",
            "off",
        }
        ok = not disabled
        return {
            "ok": ok,
            "status": "healthy" if ok else "offline",
            "message": "toggle" if ok else "disabled",
        }


class FeedProvider(BaseDiscoveryProvider):
    """RSS / Atom / Sitemap discovery from trusted source base URLs."""

    def discover(self, query: str, *, limit: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        sources = kwargs.get("trusted_sources") or []
        api_type = str(self.config.get("api_type") or "rss")
        # source_budget: how many trusted sources to probe (adaptive, not fixed 12)
        source_budget = int(kwargs.get("source_budget") or len(sources) or 0)
        if source_budget <= 0:
            source_budget = len(sources)
        out: list[dict[str, Any]] = []
        per_source = max(3, int(limit / max(1, min(source_budget, len(sources) or 1))))
        for s in sources[:source_budget]:
            base = str(s.get("base_url") or "")
            rss = s.get("rss_feed")
            kwargs_disc: dict[str, Any] = {
                "base_url": base,
                "limit": per_source,
            }
            if api_type == "rss":
                kwargs_disc["rss_feed"] = rss
            elif api_type == "atom":
                kwargs_disc["atom_feed"] = rss
            elif api_type == "sitemap":
                if base:
                    kwargs_disc["sitemap_url"] = base.rstrip("/") + "/sitemap.xml"
            try:
                # Short timeouts keep multi-source feed harvest within runtime budget
                kwargs_disc["timeout"] = float(
                    kwargs.get("timeout") or self.config.get("timeout") or 8.0
                )
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
