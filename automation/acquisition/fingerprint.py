"""Document fingerprints — skip already-processed content.

SHA256 content fingerprint + URL fingerprint store.
"""

from __future__ import annotations

import hashlib
import json
import re
import time
from pathlib import Path
from typing import Any, Optional

from automation.lib.paths import find_repo_root


def sha256_text(text: str) -> str:
    return hashlib.sha256((text or "").encode("utf-8", errors="replace")).hexdigest()


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw or b"").hexdigest()


def normalize_for_fingerprint(text: str) -> str:
    """Light normalization for content fingerprint (not semantic invention)."""
    t = text or ""
    t = re.sub(r"\s+", " ", t).strip().lower()
    return t


def content_fingerprint(text: str) -> str:
    return sha256_text(normalize_for_fingerprint(text))


def url_fingerprint(url: str) -> str:
    u = (url or "").strip().lower().split("#")[0]
    return sha256_text(u)


class FingerprintStore:
    """Persistent seen-document store for incremental acquisition."""

    def __init__(self, repo_root: Path | None = None):
        self.repo_root = repo_root or find_repo_root()
        self.path = (
            self.repo_root
            / "automation"
            / "connectors"
            / "cache"
            / "document_fingerprints.json"
        )
        self._data = self._load()

    def _load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {"version": 1, "by_hash": {}, "by_url": {}, "stats": {"skips": 0, "adds": 0}}
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            data.setdefault("by_hash", {})
            data.setdefault("by_url", {})
            data.setdefault("stats", {"skips": 0, "adds": 0})
            return data
        except Exception:  # noqa: BLE001
            return {"version": 1, "by_hash": {}, "by_url": {}, "stats": {"skips": 0, "adds": 0}}

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(self._data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )

    def seen_url(self, url: str) -> bool:
        return url_fingerprint(url) in (self._data.get("by_url") or {})

    def seen_hash(self, content_hash: str) -> bool:
        return bool(content_hash) and content_hash in (self._data.get("by_hash") or {})

    def should_skip(
        self,
        *,
        url: str = "",
        content_hash: str = "",
        text: str = "",
    ) -> tuple[bool, str]:
        """Return (skip, reason)."""
        if content_hash and self.seen_hash(content_hash):
            self._bump_skip()
            return True, "duplicate_content_hash"
        if text:
            fp = content_fingerprint(text)
            if self.seen_hash(fp):
                self._bump_skip()
                return True, "duplicate_content_fingerprint"
        if url and self.seen_url(url):
            # URL seen before — skip re-download unless content changed
            entry = (self._data.get("by_url") or {}).get(url_fingerprint(url)) or {}
            if content_hash and entry.get("content_hash") == content_hash:
                self._bump_skip()
                return True, "unchanged_url_content"
            if not content_hash and not text:
                # known URL with no new content proof — treat as candidate for conditional GET
                return False, "known_url_need_validate"
        return False, ""

    def remember(
        self,
        *,
        url: str,
        content_hash: str,
        document_id: str = "",
        connector_id: str = "",
        bytes_len: int = 0,
    ) -> None:
        now = time.time()
        ufp = url_fingerprint(url) if url else ""
        if content_hash:
            self._data.setdefault("by_hash", {})[content_hash] = {
                "document_id": document_id,
                "url": url,
                "connector_id": connector_id,
                "bytes": bytes_len,
                "seen_at": now,
            }
        if ufp:
            self._data.setdefault("by_url", {})[ufp] = {
                "url": url,
                "content_hash": content_hash,
                "document_id": document_id,
                "connector_id": connector_id,
                "seen_at": now,
            }
        stats = self._data.setdefault("stats", {"skips": 0, "adds": 0})
        stats["adds"] = int(stats.get("adds") or 0) + 1
        self.save()

    def _bump_skip(self) -> None:
        stats = self._data.setdefault("stats", {"skips": 0, "adds": 0})
        stats["skips"] = int(stats.get("skips") or 0) + 1

    def stats(self) -> dict[str, Any]:
        return {
            **(self._data.get("stats") or {}),
            "unique_hashes": len(self._data.get("by_hash") or {}),
            "unique_urls": len(self._data.get("by_url") or {}),
        }
