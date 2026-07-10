"""Factory capacity — rows/hour, throughput, growth velocity."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from automation.lib.paths import find_repo_root


def _parse_ts(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except ValueError:
        return None


def collect_capacity(repo_root: Path | None = None) -> dict[str, Any]:
    root = repo_root or find_repo_root()
    sessions_root = root / "automation" / "sessions"
    now = datetime.now(timezone.utc)

    sessions: list[dict[str, Any]] = []
    if sessions_root.exists():
        for day in sorted(sessions_root.iterdir(), reverse=True):
            if not day.is_dir():
                continue
            for f in day.glob("SESSION-*.json"):
                try:
                    sessions.append(json.loads(f.read_text(encoding="utf-8")))
                except Exception:  # noqa: BLE001
                    continue
            if len(sessions) > 200:
                break

    def window_rows(hours: float) -> tuple[int, int]:
        cutoff = now.timestamp() - hours * 3600
        added = 0
        n = 0
        for s in sessions:
            ts = _parse_ts(s.get("end_time") or s.get("start_time"))
            if not ts:
                continue
            if ts.timestamp() >= cutoff:
                added += int(s.get("knowledge_added") or 0)
                n += 1
        return added, n

    rows_1h, sess_1h = window_rows(1)
    rows_24h, sess_24h = window_rows(24)
    rows_7d, sess_7d = window_rows(24 * 7)
    rows_30d, sess_30d = window_rows(24 * 30)

    # From last acquisition performance snapshot
    thr = {}
    try:
        p = root / "automation" / "learning" / "state" / "acquisition_performance.json"
        if p.exists():
            thr = (json.loads(p.read_text(encoding="utf-8")) or {}).get("throughput") or {}
    except Exception:  # noqa: BLE001
        pass

    rows_per_hour = float(thr.get("rows_per_hour") or (rows_24h / 24.0 if rows_24h else 0))
    docs_per_hour = float(thr.get("documents_per_hour") or 0)

    return {
        "rows_last_hour": rows_1h,
        "rows_today_approx": rows_24h,
        "rows_this_week": rows_7d,
        "rows_this_month": rows_30d,
        "sessions_last_hour": sess_1h,
        "sessions_24h": sess_24h,
        "sessions_7d": sess_7d,
        "sessions_30d": sess_30d,
        "rows_per_hour": round(rows_per_hour, 2),
        "rows_per_day": round(rows_per_hour * 24, 2),
        "rows_per_week": round(rows_per_hour * 24 * 7, 2),
        "rows_per_month": round(rows_per_hour * 24 * 30, 2),
        "documents_per_hour": round(docs_per_hour, 2),
        "candidates_per_hour": round(docs_per_hour * 0.75, 2),  # observed ratio proxy
        "validation_throughput": "integrity_guard_inline",
        "publish_throughput": "append_only_csv",
        "connector_throughput": thr,
        "mission_throughput_sessions_24h": sess_24h,
        "growth_velocity_rows_per_day": round(rows_7d / 7.0, 2) if rows_7d else 0.0,
    }
