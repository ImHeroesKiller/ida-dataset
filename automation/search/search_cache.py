"""Search result cache facade."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

from automation.connectors.cache import JsonFileCache


class SearchCache:
    def __init__(self, root: Path, ttl: int = 86400):
        self.cache = JsonFileCache(root, default_ttl=ttl)

    def get(self, key: str) -> Optional[Any]:
        return self.cache.get("orchestrator_search", key)

    def set(self, key: str, value: Any, *, ttl: Optional[int] = None) -> None:
        self.cache.set("orchestrator_search", key, value, ttl=ttl)
