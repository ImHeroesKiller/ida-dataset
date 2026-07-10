"""Connector / search / document / metadata cache layer."""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path
from typing import Any, Optional


class JsonFileCache:
    def __init__(self, root: Path, *, default_ttl: int = 86400) -> None:
        self.root = root
        self.default_ttl = default_ttl
        self.root.mkdir(parents=True, exist_ok=True)

    def _key_path(self, namespace: str, key: str) -> Path:
        digest = hashlib.sha256(f"{namespace}:{key}".encode("utf-8")).hexdigest()
        folder = self.root / namespace
        folder.mkdir(parents=True, exist_ok=True)
        return folder / f"{digest}.json"

    def get(self, namespace: str, key: str) -> Optional[Any]:
        path = self._key_path(namespace, key)
        if not path.exists():
            return None
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return None
        expires = float(payload.get("expires_at", 0))
        if expires and time.time() > expires:
            try:
                path.unlink()
            except OSError:
                pass
            return None
        return payload.get("value")

    def set(
        self,
        namespace: str,
        key: str,
        value: Any,
        *,
        ttl: Optional[int] = None,
    ) -> None:
        path = self._key_path(namespace, key)
        ttl_val = self.default_ttl if ttl is None else ttl
        payload = {
            "cached_at": time.time(),
            "expires_at": time.time() + ttl_val if ttl_val else 0,
            "value": value,
        }
        path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )

    def clear_namespace(self, namespace: str) -> int:
        folder = self.root / namespace
        if not folder.exists():
            return 0
        count = 0
        for path in folder.glob("*.json"):
            path.unlink(missing_ok=True)
            count += 1
        return count
