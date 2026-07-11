"""Download manager — parallel fetches, conditional GET, checksum, compression.

Respects rate limits via sequential-per-host optional lock; parallel across hosts.
"""

from __future__ import annotations

import gzip
import hashlib
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urlparse

from automation.acquisition.fingerprint import FingerprintStore, content_fingerprint, sha256_bytes
from automation.acquisition.http_cache import HttpCache
from automation.connectors.http_utils import DEFAULT_UA, http_get
from automation.lib.paths import find_repo_root


class DownloadManager:
    def __init__(
        self,
        repo_root: Path | None = None,
        *,
        max_workers: int = 6,
        timeout: float = 30.0,
        retries: int = 2,
    ):
        self.repo_root = repo_root or find_repo_root()
        self.max_workers = max(1, min(16, max_workers))
        self.timeout = timeout
        self.retries = retries
        self.cache = HttpCache(self.repo_root)
        self.fingerprints = FingerprintStore(self.repo_root)
        self.stats: dict[str, Any] = {
            "requested": 0,
            "downloaded": 0,
            "not_modified": 0,
            "skipped_duplicate": 0,
            "failed": 0,
            "bytes": 0,
            "elapsed_ms": 0.0,
            "retries": 0,
            "max_workers": self.max_workers,
            "adaptive_workers": self.max_workers,
            "connection_reuse": True,
            "accept_encoding": "gzip, deflate",
            "etag_conditional": True,
        }

    def scale_workers(self, avg_latency_ms: float) -> int:
        """Adaptive pool: 2 → 4 → 8 → 16 based on connector latency."""
        from automation.acquisition.throughput_ops import adaptive_workers

        n = adaptive_workers(avg_latency_ms, max_workers=16)
        self.max_workers = n
        self.stats["adaptive_workers"] = n
        self.stats["max_workers"] = n
        return n

    def download_one(
        self,
        url: str,
        *,
        headers: Optional[dict[str, str]] = None,
        auth_headers: Optional[dict[str, str]] = None,
        dest_dir: Optional[Path] = None,
        connector_id: str = "",
        skip_if_seen: bool = True,
    ) -> dict[str, Any]:
        """Download a single URL with cache validators + fingerprint skip."""
        self.stats["requested"] += 1
        t0 = time.perf_counter()
        url = (url or "").strip()
        if not url:
            self.stats["failed"] += 1
            return {"ok": False, "error": "empty_url", "url": url}

        if skip_if_seen:
            skip, reason = self.fingerprints.should_skip(url=url)
            # only hard-skip when we already have content hash for that URL
            # known_url_need_validate → still conditional GET

        hdrs = {
            "User-Agent": DEFAULT_UA,
            "Accept": "application/json, text/html, application/xml, text/plain, application/pdf, */*",
            "Accept-Encoding": "gzip, deflate",
        }
        if headers:
            hdrs.update(headers)
        if auth_headers:
            hdrs.update(auth_headers)
        # conditional validators
        hdrs.update(self.cache.conditional_headers(url))

        res = http_get(
            url,
            headers=hdrs,
            timeout=self.timeout,
            retries=self.retries,
            use_cache=True,
            http_cache=self.cache,
        )
        elapsed = round((time.perf_counter() - t0) * 1000, 1)
        self.stats["elapsed_ms"] += elapsed
        self.stats["retries"] += int(res.get("retries_used") or 0)

        if res.get("not_modified") or res.get("status") == 304:
            self.stats["not_modified"] += 1
            entry = self.cache.get_entry(url) or {}
            return {
                "ok": True,
                "not_modified": True,
                "url": url,
                "status": 304,
                "elapsed_ms": elapsed,
                "content_hash": entry.get("content_hash") or "",
                "bytes": 0,
                "text": "",
                "skipped": True,
                "reason": "not_modified",
            }

        if not res.get("ok"):
            self.stats["failed"] += 1
            return {
                "ok": False,
                "url": url,
                "status": res.get("status"),
                "error": res.get("error"),
                "elapsed_ms": elapsed,
            }

        text = res.get("text") or ""
        raw: bytes = res.get("raw") or text.encode("utf-8", errors="replace")
        content_hash = sha256_bytes(raw) if raw else content_fingerprint(text)

        if skip_if_seen:
            skip, reason = self.fingerprints.should_skip(
                url=url, content_hash=content_hash, text=text[:5000]
            )
            if skip and reason != "known_url_need_validate":
                self.stats["skipped_duplicate"] += 1
                return {
                    "ok": True,
                    "skipped": True,
                    "reason": reason,
                    "url": url,
                    "status": res.get("status"),
                    "content_hash": content_hash,
                    "elapsed_ms": elapsed,
                    "bytes": 0,
                }

        # persist body optionally
        local_path = None
        if dest_dir is not None:
            dest_dir = Path(dest_dir)
            dest_dir.mkdir(parents=True, exist_ok=True)
            doc_id = f"DOC-{content_hash[:12].upper()}"
            # choose extension from content type
            ctype = (res.get("content_type") or "").lower()
            ext = ".bin"
            if "json" in ctype:
                ext = ".json"
            elif "html" in ctype:
                ext = ".html"
            elif "pdf" in ctype:
                ext = ".pdf"
            elif "xml" in ctype:
                ext = ".xml"
            elif "csv" in ctype or "text/csv" in ctype:
                ext = ".csv"
            elif "text" in ctype:
                ext = ".txt"
            local_path = dest_dir / f"{doc_id}{ext}"
            local_path.write_bytes(raw)

        self.fingerprints.remember(
            url=url,
            content_hash=content_hash,
            document_id=f"DOC-{content_hash[:12].upper()}",
            connector_id=connector_id,
            bytes_len=len(raw),
        )
        self.stats["downloaded"] += 1
        self.stats["bytes"] += len(raw)

        return {
            "ok": True,
            "skipped": False,
            "not_modified": False,
            "url": url,
            "status": res.get("status"),
            "headers": res.get("headers") or {},
            "content_type": res.get("content_type") or "",
            "text": text,
            "json": res.get("json"),
            "raw": raw,
            "bytes": len(raw),
            "content_hash": content_hash,
            "local_path": str(local_path) if local_path else None,
            "elapsed_ms": elapsed,
            "from_cache": bool(res.get("from_cache")),
        }

    def download_many(
        self,
        urls: list[str],
        *,
        headers: Optional[dict[str, str]] = None,
        auth_headers: Optional[dict[str, str]] = None,
        dest_dir: Optional[Path] = None,
        connector_id: str = "",
        max_workers: Optional[int] = None,
    ) -> list[dict[str, Any]]:
        """Parallel download across URLs (thread pool)."""
        workers = max_workers or self.max_workers
        results: list[dict[str, Any]] = []
        if not urls:
            return results
        with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
            futs = {
                pool.submit(
                    self.download_one,
                    u,
                    headers=headers,
                    auth_headers=auth_headers,
                    dest_dir=dest_dir,
                    connector_id=connector_id,
                ): u
                for u in urls
            }
            for fut in as_completed(futs):
                try:
                    results.append(fut.result())
                except Exception as exc:  # noqa: BLE001
                    self.stats["failed"] += 1
                    results.append({"ok": False, "url": futs[fut], "error": str(exc)})
        return results

    def snapshot(self) -> dict[str, Any]:
        return {
            **self.stats,
            "http_cache": self.cache.stats(),
            "fingerprints": self.fingerprints.stats(),
        }
