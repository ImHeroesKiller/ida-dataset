"""Shared HTTP helpers for production connectors — cache-aware, rate-friendly."""

from __future__ import annotations

import gzip
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import zlib
from typing import Any, Optional

DEFAULT_UA = "IDA-Dataset-Factory/2.0 (+https://github.com/ImHeroesKiller/ida-dataset; research; respects rate limits)"


def http_get(
    url: str,
    *,
    headers: Optional[dict[str, str]] = None,
    timeout: float = 30.0,
    retries: int = 2,
    backoff: float = 1.0,
    use_cache: bool = False,
    http_cache: Any = None,
) -> dict[str, Any]:
    """GET url. Returns {ok, status, headers, text, json, raw, error, url, not_modified, retries_used}.

    When use_cache=True and http_cache is provided, conditional validators are applied
    and 304 responses are recorded as not_modified.
    """
    hdrs = {
        "User-Agent": DEFAULT_UA,
        "Accept": "application/json, text/html, application/xml, text/plain, application/pdf, */*",
        "Accept-Encoding": "gzip, deflate",
    }
    if headers:
        hdrs.update(headers)

    # merge cache validators if not already present
    if use_cache and http_cache is not None:
        for k, v in (http_cache.conditional_headers(url) or {}).items():
            hdrs.setdefault(k, v)

    last_err = ""
    retries_used = 0
    for attempt in range(max(1, retries + 1)):
        try:
            req = urllib.request.Request(url, headers=hdrs, method="GET")
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
                # decompress if needed
                encoding = (resp.headers.get("Content-Encoding") or "").lower()
                if encoding == "gzip" or raw[:2] == b"\x1f\x8b":
                    try:
                        raw = gzip.decompress(raw)
                    except Exception:  # noqa: BLE001
                        pass
                elif encoding == "deflate":
                    try:
                        raw = zlib.decompress(raw)
                    except Exception:  # noqa: BLE001
                        try:
                            raw = zlib.decompress(raw, -zlib.MAX_WBITS)
                        except Exception:  # noqa: BLE001
                            pass

                text = raw.decode("utf-8", errors="replace")
                ctype = (resp.headers.get("Content-Type") or "").split(";")[0].strip()
                status = getattr(resp, "status", 200)
                resp_headers = dict(resp.headers.items())
                parsed = None
                if "json" in ctype or text[:1] in "{[":
                    try:
                        parsed = json.loads(text)
                    except json.JSONDecodeError:
                        parsed = None

                import hashlib

                content_hash = hashlib.sha256(raw).hexdigest()
                if use_cache and http_cache is not None:
                    http_cache.store_response(
                        url,
                        status=status,
                        headers=resp_headers,
                        content_hash=content_hash,
                        bytes_len=len(raw),
                        not_modified=False,
                    )

                return {
                    "ok": True,
                    "status": status,
                    "headers": resp_headers,
                    "text": text,
                    "json": parsed,
                    "raw": raw,
                    "content_type": ctype,
                    "bytes": len(raw),
                    "url": url,
                    "error": None,
                    "not_modified": False,
                    "retries_used": retries_used,
                    "content_hash": content_hash,
                }
        except urllib.error.HTTPError as exc:
            last_err = f"HTTP {exc.code}: {exc.reason}"
            body = b""
            try:
                body = exc.read()
            except Exception:  # noqa: BLE001
                pass
            # 304 Not Modified
            if exc.code == 304:
                if use_cache and http_cache is not None:
                    http_cache.store_response(
                        url,
                        status=304,
                        headers=dict(exc.headers.items()) if exc.headers else {},
                        not_modified=True,
                    )
                return {
                    "ok": True,
                    "status": 304,
                    "headers": dict(exc.headers.items()) if exc.headers else {},
                    "text": "",
                    "json": None,
                    "raw": b"",
                    "content_type": "",
                    "bytes": 0,
                    "url": url,
                    "error": None,
                    "not_modified": True,
                    "retries_used": retries_used,
                }
            text_body = body.decode("utf-8", errors="replace")[:500] if body else ""
            if exc.code in (429, 500, 502, 503, 504) and attempt < retries:
                retries_used += 1
                time.sleep(backoff * (attempt + 1))
                continue
            return {
                "ok": False,
                "status": exc.code,
                "headers": dict(exc.headers.items()) if exc.headers else {},
                "text": text_body,
                "json": None,
                "raw": body,
                "content_type": "",
                "bytes": len(body),
                "url": url,
                "error": last_err,
                "not_modified": False,
                "retries_used": retries_used,
            }
        except Exception as exc:  # noqa: BLE001
            last_err = str(exc)
            if attempt < retries:
                retries_used += 1
                time.sleep(backoff * (attempt + 1))
                continue
            return {
                "ok": False,
                "status": 0,
                "headers": {},
                "text": "",
                "json": None,
                "raw": b"",
                "content_type": "",
                "bytes": 0,
                "url": url,
                "error": last_err,
                "not_modified": False,
                "retries_used": retries_used,
            }
    return {
        "ok": False,
        "status": 0,
        "headers": {},
        "text": "",
        "json": None,
        "raw": b"",
        "content_type": "",
        "bytes": 0,
        "url": url,
        "error": last_err or "request_failed",
        "not_modified": False,
        "retries_used": retries_used,
    }


def urlencode_query(params: dict[str, Any]) -> str:
    return urllib.parse.urlencode(
        {k: v for k, v in params.items() if v is not None and v != ""}
    )
