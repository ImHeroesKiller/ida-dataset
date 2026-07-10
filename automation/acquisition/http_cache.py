"""HTTP conditional cache — ETag / Last-Modified / 304 Not Modified.

Minimizes bandwidth. Never fabricates content.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urlparse

from automation.lib.paths import find_repo_root


class HttpCache:
    """Persistent URL → validators + optional body metadata cache."""

    def __init__(self, repo_root: Path | None = None):
        self.repo_root = repo_root or find_repo_root()
        self.path = (
            self.repo_root
            / "automation"
            / "connectors"
            / "cache"
            / "http_cache.json"
        )
        self._data: dict[str, Any] = self._load()

    def _load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {"version": 1, "entries": {}, "stats": self._empty_stats()}
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            data.setdefault("entries", {})
            data.setdefault("stats", self._empty_stats())
            return data
        except Exception:  # noqa: BLE001
            return {"version": 1, "entries": {}, "stats": self._empty_stats()}

    @staticmethod
    def _empty_stats() -> dict[str, int]:
        return {
            "hits": 0,
            "misses": 0,
            "not_modified": 0,
            "stores": 0,
            "bytes_saved_est": 0,
        }

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(self._data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )

    def get_entry(self, url: str) -> Optional[dict[str, Any]]:
        return (self._data.get("entries") or {}).get(url)

    def conditional_headers(self, url: str) -> dict[str, str]:
        """Build If-None-Match / If-Modified-Since for a URL."""
        entry = self.get_entry(url)
        if not entry:
            return {}
        hdrs: dict[str, str] = {}
        etag = entry.get("etag")
        if etag:
            hdrs["If-None-Match"] = str(etag)
        last_mod = entry.get("last_modified")
        if last_mod:
            hdrs["If-Modified-Since"] = str(last_mod)
        return hdrs

    def store_response(
        self,
        url: str,
        *,
        status: int,
        headers: dict[str, Any],
        content_hash: str = "",
        bytes_len: int = 0,
        not_modified: bool = False,
    ) -> None:
        entries = self._data.setdefault("entries", {})
        stats = self._data.setdefault("stats", self._empty_stats())
        # normalize header keys
        h = {str(k).lower(): str(v) for k, v in (headers or {}).items()}
        prev = entries.get(url) or {}
        if not_modified:
            stats["not_modified"] = int(stats.get("not_modified") or 0) + 1
            stats["hits"] = int(stats.get("hits") or 0) + 1
            stats["bytes_saved_est"] = int(stats.get("bytes_saved_est") or 0) + int(
                prev.get("bytes") or 0
            )
            entries[url] = {
                **prev,
                "url": url,
                "last_checked": time.time(),
                "status": 304,
            }
        else:
            stats["misses"] = int(stats.get("misses") or 0) + 1
            stats["stores"] = int(stats.get("stores") or 0) + 1
            entries[url] = {
                "url": url,
                "host": (urlparse(url).hostname or ""),
                "etag": h.get("etag") or prev.get("etag") or "",
                "last_modified": h.get("last-modified") or prev.get("last_modified") or "",
                "cache_control": h.get("cache-control") or "",
                "expires": h.get("expires") or "",
                "content_hash": content_hash or prev.get("content_hash") or "",
                "bytes": bytes_len or prev.get("bytes") or 0,
                "status": status,
                "last_checked": time.time(),
                "last_fetched": time.time(),
            }
        self.save()

    def record_hit(self, *, bytes_saved: int = 0) -> None:
        stats = self._data.setdefault("stats", self._empty_stats())
        stats["hits"] = int(stats.get("hits") or 0) + 1
        stats["bytes_saved_est"] = int(stats.get("bytes_saved_est") or 0) + bytes_saved
        self.save()

    def stats(self) -> dict[str, Any]:
        return dict(self._data.get("stats") or self._empty_stats())
