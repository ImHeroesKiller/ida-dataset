"""Shared HTTP helpers for production connectors — rate-friendly, no fabrication."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Optional

DEFAULT_UA = "IDA-Dataset-Factory/2.0 (+https://github.com/ImHeroesKiller/ida-dataset; research; respects rate limits)"


def http_get(
    url: str,
    *,
    headers: Optional[dict[str, str]] = None,
    timeout: float = 30.0,
    retries: int = 2,
    backoff: float = 1.0,
) -> dict[str, Any]:
    """GET url. Returns {ok, status, headers, text, json, error, url}."""
    hdrs = {
        "User-Agent": DEFAULT_UA,
        "Accept": "application/json, text/html, application/xml, text/plain, */*",
    }
    if headers:
        hdrs.update(headers)

    last_err = ""
    for attempt in range(max(1, retries + 1)):
        try:
            req = urllib.request.Request(url, headers=hdrs, method="GET")
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
                text = raw.decode("utf-8", errors="replace")
                ctype = (resp.headers.get("Content-Type") or "").split(";")[0].strip()
                parsed = None
                if "json" in ctype or text[:1] in "{[":
                    try:
                        parsed = json.loads(text)
                    except json.JSONDecodeError:
                        parsed = None
                return {
                    "ok": True,
                    "status": getattr(resp, "status", 200),
                    "headers": dict(resp.headers.items()),
                    "text": text,
                    "json": parsed,
                    "content_type": ctype,
                    "bytes": len(raw),
                    "url": url,
                    "error": None,
                }
        except urllib.error.HTTPError as exc:
            last_err = f"HTTP {exc.code}: {exc.reason}"
            body = ""
            try:
                body = exc.read().decode("utf-8", errors="replace")[:500]
            except Exception:  # noqa: BLE001
                pass
            if exc.code in (429, 500, 502, 503, 504) and attempt < retries:
                time.sleep(backoff * (attempt + 1))
                continue
            return {
                "ok": False,
                "status": exc.code,
                "headers": {},
                "text": body,
                "json": None,
                "content_type": "",
                "bytes": 0,
                "url": url,
                "error": last_err,
            }
        except Exception as exc:  # noqa: BLE001
            last_err = str(exc)
            if attempt < retries:
                time.sleep(backoff * (attempt + 1))
                continue
            return {
                "ok": False,
                "status": 0,
                "headers": {},
                "text": "",
                "json": None,
                "content_type": "",
                "bytes": 0,
                "url": url,
                "error": last_err,
            }
    return {
        "ok": False,
        "status": 0,
        "headers": {},
        "text": "",
        "json": None,
        "content_type": "",
        "bytes": 0,
        "url": url,
        "error": last_err or "request_failed",
    }


def urlencode_query(params: dict[str, Any]) -> str:
    return urllib.parse.urlencode(
        {k: v for k, v in params.items() if v is not None and v != ""}
    )
