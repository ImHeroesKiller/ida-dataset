"""Learning session storage — GitHub Actions execution model.

Sessions are the durable unit of learning. Every GHA (or local) learning run
writes one JSON file under:

  automation/sessions/YYYY-MM-DD/SESSION-xxxxx.json

The dashboard on Vercel reads these files (and GitHub Actions run status).
No long-lived Python runtime is required.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional
from uuid import uuid4

from automation.lib.paths import find_repo_root

SESSION_ID_RE = re.compile(r"^SESSION-[A-Z0-9-]+$", re.IGNORECASE)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sessions_root(repo_root: Path | None = None) -> Path:
    root = repo_root or find_repo_root()
    path = root / "automation" / "sessions"
    path.mkdir(parents=True, exist_ok=True)
    return path


def new_session_id(when: datetime | None = None) -> str:
    """SESSION-{YYYYMMDD}-{6hex} — matches automation/sessions layout."""
    ts = when or datetime.now(timezone.utc)
    day = ts.strftime("%Y%m%d")
    return f"SESSION-{day}-{uuid4().hex[:6].upper()}"


def session_day_dir(session_id: str, repo_root: Path | None = None) -> Path:
    """Resolve YYYY-MM-DD directory from session id or today."""
    root = sessions_root(repo_root)
    m = re.search(r"SESSION-(\d{8})-", session_id, re.IGNORECASE)
    if m:
        raw = m.group(1)
        day = f"{raw[0:4]}-{raw[4:6]}-{raw[6:8]}"
    else:
        day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = root / day
    path.mkdir(parents=True, exist_ok=True)
    return path


def session_path(session_id: str, repo_root: Path | None = None) -> Path:
    return session_day_dir(session_id, repo_root) / f"{session_id}.json"


def empty_session(
    *,
    session_id: str | None = None,
    mission: str | None = None,
    instruction: str | None = None,
    trigger: str = "manual",
    dry_run: bool = True,
    environment: str = "development",
    github: dict[str, Any] | None = None,
) -> dict[str, Any]:
    sid = session_id or new_session_id()
    return {
        "session_id": sid,
        "start_time": utc_now_iso(),
        "end_time": None,
        "duration_seconds": None,
        "knowledge_added": 0,
        "knowledge_updated": 0,
        "knowledge_rejected": 0,
        "mission": mission or instruction or "Continuous learning tick",
        "instruction": instruction or mission or "Continuous learning tick",
        "status": "running",
        "errors": [],
        "summary": "Learning session starting",
        "trigger": trigger,
        "dry_run": dry_run,
        "environment": environment,
        "planner_output": None,
        "connector_output": None,
        "knowledge_delta": None,
        "publish_summary": None,
        "telemetry": {},
        "logs": [],
        "events": [],
        "github": github or {},
        "execution_model": "github_actions",
        "architecture": [
            "Scheduler",
            "Planner",
            "Policy",
            "Connector Manager",
            "Pipeline",
            "Review",
            "Publisher",
            "Telemetry",
        ],
    }


def save_session(session: dict[str, Any], repo_root: Path | None = None) -> Path:
    sid = str(session.get("session_id") or new_session_id())
    session["session_id"] = sid
    path = session_path(sid, repo_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(
        json.dumps(session, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    tmp.replace(path)
    return path


def load_session(session_id: str, repo_root: Path | None = None) -> dict[str, Any] | None:
    path = session_path(session_id, repo_root)
    if not path.exists():
        # Search all day dirs
        root = sessions_root(repo_root)
        if root.exists():
            for found in root.rglob(f"{session_id}.json"):
                path = found
                break
        if not path.exists():
            return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def finalize_session(
    session: dict[str, Any],
    *,
    status: str,
    summary: str | None = None,
    errors: list[Any] | None = None,
    repo_root: Path | None = None,
) -> Path:
    end = utc_now_iso()
    session["end_time"] = end
    session["status"] = status
    if summary is not None:
        session["summary"] = summary
    if errors:
        existing = list(session.get("errors") or [])
        existing.extend(errors)
        session["errors"] = existing
    start = session.get("start_time")
    if start:
        try:
            t0 = datetime.fromisoformat(str(start).replace("Z", "+00:00"))
            t1 = datetime.fromisoformat(end.replace("Z", "+00:00"))
            session["duration_seconds"] = round((t1 - t0).total_seconds(), 3)
        except ValueError:
            session["duration_seconds"] = None
    return save_session(session, repo_root)


def append_event(
    session: dict[str, Any],
    verb: str,
    detail: str,
    **kwargs: Any,
) -> dict[str, Any]:
    """Append a journal-style event into the session (for replay)."""
    events = list(session.get("events") or [])
    logs = list(session.get("logs") or [])
    seq = len(events) + 1
    row = {
        "seq": seq,
        "ts": utc_now_iso(),
        "verb": verb,
        "detail": detail,
        "stage": kwargs.get("stage", "learning"),
        "status": kwargs.get("status", "progress"),
        "dataset": kwargs.get("dataset"),
        "mission_id": kwargs.get("mission_id") or session.get("mission_id"),
        "session_id": session.get("session_id"),
        "progress": kwargs.get("progress"),
        "current_task": kwargs.get("current_task") or detail,
        "current_entity": kwargs.get("current_entity"),
        "current_document": kwargs.get("current_document"),
        "current_source": kwargs.get("current_source"),
        "current_relationship": kwargs.get("current_relationship"),
        "confidence": kwargs.get("confidence"),
        "duration_ms": kwargs.get("duration_ms"),
        "meta": kwargs.get("meta") or {},
    }
    events.append(row)
    logs.append(f"[{row['ts']}] {verb}: {detail}")
    session["events"] = events
    session["logs"] = logs
    return row


def list_sessions(
    repo_root: Path | None = None,
    *,
    limit: int = 200,
) -> list[dict[str, Any]]:
    root = sessions_root(repo_root)
    if not root.exists():
        return []
    files = sorted(root.rglob("SESSION-*.json"), reverse=True)
    out: list[dict[str, Any]] = []
    for path in files[: limit * 2]:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        out.append(
            {
                "session_id": data.get("session_id") or path.stem,
                "path": str(path.relative_to(find_repo_root() if repo_root is None else repo_root)),
                "start_time": data.get("start_time"),
                "end_time": data.get("end_time"),
                "duration_seconds": data.get("duration_seconds"),
                "status": data.get("status"),
                "mission": data.get("mission"),
                "knowledge_added": data.get("knowledge_added", 0),
                "knowledge_updated": data.get("knowledge_updated", 0),
                "knowledge_rejected": data.get("knowledge_rejected", 0),
                "summary": data.get("summary"),
                "trigger": data.get("trigger"),
                "dry_run": data.get("dry_run"),
                "events": len(data.get("events") or []),
                "github": data.get("github") or {},
            }
        )
        if len(out) >= limit:
            break
    out.sort(key=lambda s: str(s.get("start_time") or ""), reverse=True)
    return out


def history_stats(sessions: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate learning history: today / week / month / totals."""
    now = datetime.now(timezone.utc)
    today = now.date()

    def parse_day(s: dict[str, Any]) -> Optional[datetime]:
        raw = s.get("start_time")
        if not raw:
            return None
        try:
            return datetime.fromisoformat(str(raw).replace("Z", "+00:00"))
        except ValueError:
            return None

    def in_range(s: dict[str, Any], days: int) -> bool:
        dt = parse_day(s)
        if not dt:
            return False
        return (now - dt).days < days and dt.date() <= today

    def is_today(s: dict[str, Any]) -> bool:
        dt = parse_day(s)
        return bool(dt and dt.date() == today)

    all_s = sessions
    today_s = [s for s in all_s if is_today(s)]
    week_s = [s for s in all_s if in_range(s, 7)]
    month_s = [s for s in all_s if in_range(s, 30)]

    def bucket(items: list[dict[str, Any]]) -> dict[str, Any]:
        total = len(items)
        success = sum(1 for s in items if str(s.get("status")) in {"completed", "success"})
        failed = sum(1 for s in items if str(s.get("status")) in {"failed", "error"})
        durations = [
            float(s["duration_seconds"])
            for s in items
            if s.get("duration_seconds") is not None
        ]
        added = [int(s.get("knowledge_added") or 0) for s in items]
        return {
            "sessions": total,
            "success": success,
            "failed": failed,
            "success_rate": round((success / total) * 100, 1) if total else 0.0,
            "knowledge_added": sum(added),
            "knowledge_updated": sum(int(s.get("knowledge_updated") or 0) for s in items),
            "knowledge_rejected": sum(int(s.get("knowledge_rejected") or 0) for s in items),
            "avg_duration_seconds": round(sum(durations) / len(durations), 2)
            if durations
            else 0.0,
            "avg_knowledge_added": round(sum(added) / len(added), 2) if added else 0.0,
        }

    return {
        "today": bucket(today_s),
        "this_week": bucket(week_s),
        "this_month": bucket(month_s),
        "total": bucket(all_s),
        "knowledge_growth": {
            "added": sum(int(s.get("knowledge_added") or 0) for s in all_s),
            "updated": sum(int(s.get("knowledge_updated") or 0) for s in all_s),
            "rejected": sum(int(s.get("knowledge_rejected") or 0) for s in all_s),
        },
    }
