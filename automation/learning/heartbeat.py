"""Scheduler / production heartbeat — observe-only production telemetry.

Updates on each production learning cycle. Does not redesign the scheduler.
Persists to automation/learning/state/scheduler_heartbeat.json (existing state dir).
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Optional

from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root

# Production status surface (matches ops dashboard vocabulary)
STATUS_RUNNING = "Running"
STATUS_IDLE = "Idle"
STATUS_PUBLISHING = "Publishing"
STATUS_FAILED = "Failed"

_STATE_REL = Path("automation") / "learning" / "state" / "scheduler_heartbeat.json"


def heartbeat_path(repo_root: Path | None = None) -> Path:
    root = repo_root or find_repo_root()
    return root / _STATE_REL


def _empty() -> dict[str, Any]:
    return {
        "version": "1.0",
        "status": STATUS_IDLE,
        "last_heartbeat": None,
        "last_success": None,
        "last_failure": None,
        "current_job": None,
        "job_id": None,
        "dataset": None,
        "mission_id": None,
        "session_id": None,
        "job_started_at": None,
        "job_duration_seconds": None,
        "last_error": None,
        "cycle_count": 0,
        "success_count": 0,
        "failure_count": 0,
        "updated_at": None,
    }


def load_heartbeat(repo_root: Path | None = None) -> dict[str, Any]:
    path = heartbeat_path(repo_root)
    if not path.exists():
        return _empty()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return _empty()
        base = _empty()
        base.update(data)
        return base
    except Exception:  # noqa: BLE001
        return _empty()


def _save(data: dict[str, Any], repo_root: Path | None = None) -> Path:
    path = heartbeat_path(repo_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    data["updated_at"] = utc_now_iso()
    data["last_heartbeat"] = data["updated_at"]
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return path


def pulse(
    *,
    status: str,
    current_job: str | None = None,
    job_id: str | None = None,
    dataset: str | None = None,
    mission_id: str | None = None,
    session_id: str | None = None,
    error: str | None = None,
    job_started_at: str | None = None,
    mark_success: bool = False,
    mark_failure: bool = False,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Update heartbeat snapshot (one production cycle step)."""
    data = load_heartbeat(repo_root)
    now = utc_now_iso()
    data["status"] = status
    data["last_heartbeat"] = now
    data["cycle_count"] = int(data.get("cycle_count") or 0) + 1

    if current_job is not None:
        data["current_job"] = current_job
    if job_id is not None:
        data["job_id"] = job_id
    if dataset is not None:
        data["dataset"] = dataset
    if mission_id is not None:
        data["mission_id"] = mission_id
    if session_id is not None:
        data["session_id"] = session_id
    if job_started_at is not None:
        data["job_started_at"] = job_started_at

    # Duration from job start when available
    started = data.get("job_started_at")
    if started:
        try:
            from datetime import datetime

            t0 = datetime.fromisoformat(str(started).replace("Z", "+00:00"))
            t1 = datetime.fromisoformat(now.replace("Z", "+00:00"))
            data["job_duration_seconds"] = round(max(0.0, (t1 - t0).total_seconds()), 3)
        except Exception:  # noqa: BLE001
            pass

    if mark_success:
        data["last_success"] = now
        data["success_count"] = int(data.get("success_count") or 0) + 1
        data["last_error"] = None
        data["status"] = STATUS_IDLE
        data["current_job"] = None
    if mark_failure:
        data["last_failure"] = now
        data["failure_count"] = int(data.get("failure_count") or 0) + 1
        data["last_error"] = (error or "production_failed")[:500]
        data["status"] = STATUS_FAILED
    elif error:
        data["last_error"] = str(error)[:500]

    _save(data, repo_root)
    return data


def cycle_start(
    *,
    job: str,
    job_id: str = "",
    dataset: str = "",
    mission_id: str = "",
    session_id: str = "",
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Heartbeat at the start of a production cycle → Running."""
    return pulse(
        status=STATUS_RUNNING,
        current_job=job,
        job_id=job_id or None,
        dataset=dataset or None,
        mission_id=mission_id or None,
        session_id=session_id or None,
        job_started_at=utc_now_iso(),
        repo_root=repo_root,
    )


def cycle_publishing(
    *,
    job: str | None = None,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Heartbeat while rows are being published → Publishing."""
    data = load_heartbeat(repo_root)
    return pulse(
        status=STATUS_PUBLISHING,
        current_job=job if job is not None else data.get("current_job"),
        job_id=data.get("job_id"),
        dataset=data.get("dataset"),
        mission_id=data.get("mission_id"),
        session_id=data.get("session_id"),
        job_started_at=data.get("job_started_at"),
        repo_root=repo_root,
    )


def cycle_success(
    *,
    repo_root: Path | None = None,
    summary: str = "",
) -> dict[str, Any]:
    """Heartbeat at successful cycle end → Idle + last_success."""
    data = load_heartbeat(repo_root)
    return pulse(
        status=STATUS_IDLE,
        current_job=summary or data.get("current_job"),
        job_id=data.get("job_id"),
        dataset=data.get("dataset"),
        mission_id=data.get("mission_id"),
        session_id=data.get("session_id"),
        job_started_at=data.get("job_started_at"),
        mark_success=True,
        repo_root=repo_root,
    )


def cycle_failure(
    *,
    error: str,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Heartbeat at failed cycle end → Failed + last_failure."""
    data = load_heartbeat(repo_root)
    return pulse(
        status=STATUS_FAILED,
        current_job=data.get("current_job"),
        job_id=data.get("job_id"),
        dataset=data.get("dataset"),
        mission_id=data.get("mission_id"),
        session_id=data.get("session_id"),
        job_started_at=data.get("job_started_at"),
        error=error,
        mark_failure=True,
        repo_root=repo_root,
    )


def snapshot(repo_root: Path | None = None) -> dict[str, Any]:
    """Read-only snapshot for APIs / dashboard (no mutation)."""
    data = load_heartbeat(repo_root)
    # If no recent heartbeat and status was Running, surface as Idle for observability
    return {
        "status": data.get("status") or STATUS_IDLE,
        "last_heartbeat": data.get("last_heartbeat"),
        "last_success": data.get("last_success"),
        "last_failure": data.get("last_failure"),
        "current_job": data.get("current_job"),
        "job_id": data.get("job_id"),
        "dataset": data.get("dataset"),
        "mission_id": data.get("mission_id"),
        "session_id": data.get("session_id"),
        "job_started_at": data.get("job_started_at"),
        "job_duration_seconds": data.get("job_duration_seconds"),
        "last_error": data.get("last_error"),
        "cycle_count": data.get("cycle_count") or 0,
        "success_count": data.get("success_count") or 0,
        "failure_count": data.get("failure_count") or 0,
        "updated_at": data.get("updated_at"),
    }
