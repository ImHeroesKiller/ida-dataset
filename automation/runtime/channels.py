"""Separated runtime log channels.

Channels: system, learning, runtime, errors, publish, review, telemetry

Every log line includes: session_id, correlation_id, timestamp, duration, module
"""

from __future__ import annotations

import json
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from automation.lib.paths import find_repo_root
from automation.runtime.lifecycle import logs_dir

CHANNELS = (
    "system",
    "learning",
    "runtime",
    "errors",
    "publish",
    "review",
    "telemetry",
)

_lock = threading.Lock()
_context: dict[str, Any] = {
    "session_id": None,
    "correlation_id": None,
}


def set_context(*, session_id: str | None = None, correlation_id: str | None = None) -> None:
    with _lock:
        if session_id is not None:
            _context["session_id"] = session_id
        if correlation_id is not None:
            _context["correlation_id"] = correlation_id


def clear_context() -> None:
    with _lock:
        _context["session_id"] = None
        _context["correlation_id"] = None


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def log(
    channel: str,
    message: str,
    *,
    module: str = "runtime",
    level: str = "INFO",
    duration_ms: float | None = None,
    session_id: str | None = None,
    correlation_id: str | None = None,
    meta: dict[str, Any] | None = None,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    if channel not in CHANNELS:
        channel = "runtime"
    root = repo_root or find_repo_root()
    with _lock:
        sid = session_id if session_id is not None else _context.get("session_id")
        cid = correlation_id if correlation_id is not None else _context.get("correlation_id")

    row = {
        "timestamp": utc_now_iso(),
        "channel": channel,
        "level": level,
        "module": module,
        "message": message,
        "session_id": sid,
        "correlation_id": cid,
        "duration_ms": duration_ms,
        "meta": meta or {},
    }
    path = logs_dir(root) / f"{channel}.jsonl"
    with _lock:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


class timed:
    """Context manager that logs duration to a channel on exit."""

    def __init__(
        self,
        channel: str,
        message: str,
        *,
        module: str = "runtime",
        **kwargs: Any,
    ) -> None:
        self.channel = channel
        self.message = message
        self.module = module
        self.kwargs = kwargs
        self._t0 = 0.0

    def __enter__(self) -> "timed":
        self._t0 = time.time()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:  # type: ignore[no-untyped-def]
        duration = round((time.time() - self._t0) * 1000, 1)
        level = "ERROR" if exc else "INFO"
        msg = self.message if not exc else f"{self.message} failed: {exc}"
        log(
            self.channel,
            msg,
            module=self.module,
            level=level,
            duration_ms=duration,
            **self.kwargs,
        )


def read_channel(
    channel: str,
    *,
    limit: int = 100,
    session_id: str | None = None,
    correlation_id: str | None = None,
    repo_root: Path | None = None,
) -> list[dict[str, Any]]:
    if channel not in CHANNELS and channel != "all":
        return []
    root = repo_root or find_repo_root()
    base = logs_dir(root)
    files: list[Path]
    if channel == "all":
        files = [base / f"{c}.jsonl" for c in CHANNELS]
    else:
        files = [base / f"{channel}.jsonl"]

    rows: list[dict[str, Any]] = []
    for path in files:
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if session_id and row.get("session_id") != session_id:
                continue
            if correlation_id and row.get("correlation_id") != correlation_id:
                continue
            rows.append(row)
    rows.sort(key=lambda r: str(r.get("timestamp") or ""), reverse=True)
    return rows[:limit]
