"""Discovery query/URL cache — avoid repeating searches."""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path
from typing import Any, Optional

from automation.lib.paths import find_repo_root


class DiscoveryCache:
    def __init__(self, repo_root: Path | None = None, ttl_seconds: int = 86400):
        self.repo_root = repo_root or find_repo_root()
        self.ttl = ttl_seconds
        self.path = (
            self.repo_root
            / "automation"
            / "connectors"
            / "cache"
            / "discovery_cache.json"
        )
        self._data = self._load()

    def _load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {"queries": {}, "urls": {}, "stats": {"hits": 0, "misses": 0, "stores": 0}}
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            data.setdefault("queries", {})
            data.setdefault("urls", {})
            data.setdefault("stats", {"hits": 0, "misses": 0, "stores": 0})
            return data
        except Exception:  # noqa: BLE001
            return {"queries": {}, "urls": {}, "stats": {"hits": 0, "misses": 0, "stores": 0}}

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(self._data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )

    @staticmethod
    def _key(provider_id: str, query: str) -> str:
        raw = f"{provider_id}|{query}".encode("utf-8")
        return hashlib.sha256(raw).hexdigest()

    def get_query(self, provider_id: str, query: str) -> Optional[list[dict[str, Any]]]:
        k = self._key(provider_id, query)
        entry = (self._data.get("queries") or {}).get(k)
        if not entry:
            self._data["stats"]["misses"] = int(self._data["stats"].get("misses") or 0) + 1
            return None
        if time.time() - float(entry.get("ts") or 0) > self.ttl:
            self._data["stats"]["misses"] = int(self._data["stats"].get("misses") or 0) + 1
            return None
        self._data["stats"]["hits"] = int(self._data["stats"].get("hits") or 0) + 1
        return list(entry.get("results") or [])

    def set_query(
        self, provider_id: str, query: str, results: list[dict[str, Any]]
    ) -> None:
        k = self._key(provider_id, query)
        self._data.setdefault("queries", {})[k] = {
            "provider_id": provider_id,
            "query": query,
            "ts": time.time(),
            "results": results[:50],
        }
        self._data["stats"]["stores"] = int(self._data["stats"].get("stores") or 0) + 1
        # url index
        for r in results:
            url = str(r.get("url") or "")
            if url:
                self._data.setdefault("urls", {})[url.lower()] = {
                    "provider_id": provider_id,
                    "ts": time.time(),
                    "title": r.get("title"),
                }
        self.save()

    def stats(self) -> dict[str, Any]:
        return {
            **(self._data.get("stats") or {}),
            "cached_queries": len(self._data.get("queries") or {}),
            "cached_urls": len(self._data.get("urls") or {}),
        }
