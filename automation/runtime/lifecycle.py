"""Runtime lifecycle state machine and exclusive lock.

States:
  Idle → Starting → Running → Stopping → Stopped → Failed

Only one runtime instance may hold the lock at a time.
Never raise setMaxListeners-style workarounds — fix ownership instead.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Optional
from uuid import uuid4

from automation.lib.paths import find_repo_root

VALID_TRANSITIONS: dict[str, set[str]] = {
    "idle": {"starting", "failed"},
    "starting": {"running", "failed", "stopping", "stopped"},
    "running": {"stopping", "failed", "stopped"},
    "stopping": {"stopped", "failed"},
    "stopped": {"idle", "starting"},
    "failed": {"idle", "starting"},
}


class RuntimeState(str, Enum):
    IDLE = "idle"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def runtime_dir(repo_root: Path | None = None) -> Path:
    root = repo_root or find_repo_root()
    path = root / "automation" / "runtime"
    path.mkdir(parents=True, exist_ok=True)
    return path


def state_dir(repo_root: Path | None = None) -> Path:
    path = runtime_dir(repo_root) / "state"
    path.mkdir(parents=True, exist_ok=True)
    return path


def logs_dir(repo_root: Path | None = None) -> Path:
    path = runtime_dir(repo_root) / "logs"
    path.mkdir(parents=True, exist_ok=True)
    return path


def lock_path(repo_root: Path | None = None) -> Path:
    return state_dir(repo_root) / "runtime.lock.json"


def status_path(repo_root: Path | None = None) -> Path:
    return state_dir(repo_root) / "runtime.status.json"


def is_process_alive(pid: int | None) -> bool:
    if not pid or pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        # Process exists but we cannot signal it — treat as alive
        return True
    except OSError:
        return False
    return True


def _atomic_write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + f".tmp.{os.getpid()}")
    tmp.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    tmp.replace(path)


def read_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def read_lock(repo_root: Path | None = None) -> dict[str, Any] | None:
    return read_json(lock_path(repo_root))


def read_status(repo_root: Path | None = None) -> dict[str, Any]:
    data = read_json(status_path(repo_root))
    if data:
        return data
    return {
        "status": RuntimeState.IDLE.value,
        "session_id": None,
        "correlation_id": None,
        "pid": None,
        "started_at": None,
        "stopped_at": None,
        "current_stage": None,
        "current_task": None,
        "documents_processed": 0,
        "knowledge_candidates": 0,
        "uptime_seconds": 0,
        "last_error": None,
        "health": default_health(),
    }


def default_health() -> dict[str, str]:
    return {
        "runtime": "healthy",
        "scheduler": "healthy",
        "connector": "healthy",
        "queue": "healthy",
        "sse": "healthy",
        "publisher": "healthy",
    }


def write_status(data: dict[str, Any], repo_root: Path | None = None) -> dict[str, Any]:
    path = status_path(repo_root)
    existing = read_status(repo_root)
    merged = {**existing, **data, "updated_at": utc_now_iso()}
    if merged.get("started_at") and merged.get("status") in {
        RuntimeState.RUNNING.value,
        RuntimeState.STARTING.value,
    }:
        try:
            started = datetime.fromisoformat(str(merged["started_at"]).replace("Z", "+00:00"))
            merged["uptime_seconds"] = max(
                0, int((datetime.now(timezone.utc) - started).total_seconds())
            )
        except (TypeError, ValueError):
            pass
    _atomic_write(path, merged)
    return merged


def release_lock(
    *,
    session_id: str | None = None,
    correlation_id: str | None = None,
    force: bool = False,
    repo_root: Path | None = None,
) -> bool:
    """Release lock if we own it (or force). Returns True if released."""
    path = lock_path(repo_root)
    current = read_lock(repo_root)
    if not current:
        return True
    if not force:
        if session_id and current.get("session_id") and current["session_id"] != session_id:
            return False
        if correlation_id and current.get("correlation_id") and current["correlation_id"] != correlation_id:
            return False
        holder_pid = current.get("pid")
        if holder_pid and holder_pid != os.getpid() and is_process_alive(int(holder_pid)):
            return False
    try:
        path.unlink(missing_ok=True)
    except OSError:
        return False
    return True


def reclaim_stale_lock(repo_root: Path | None = None) -> bool:
    """If lock holder is dead, clear lock and mark status failed/idle."""
    current = read_lock(repo_root)
    if not current:
        return False
    pid = current.get("pid")
    if pid and is_process_alive(int(pid)):
        return False
    release_lock(force=True, repo_root=repo_root)
    status = read_status(repo_root)
    if status.get("status") in {
        RuntimeState.STARTING.value,
        RuntimeState.RUNNING.value,
        RuntimeState.STOPPING.value,
    }:
        write_status(
            {
                "status": RuntimeState.FAILED.value,
                "stopped_at": utc_now_iso(),
                "last_error": {
                    "timestamp": utc_now_iso(),
                    "component": "runtime.lock",
                    "exception": "StaleLock",
                    "message": (
                        f"Runtime lock held by dead process pid={pid}; "
                        "reclaimed. Previous session may have crashed."
                    ),
                    "recovery_action": "restart_runtime",
                    "session_id": current.get("session_id"),
                    "correlation_id": current.get("correlation_id"),
                },
                "pid": None,
            },
            repo_root=repo_root,
        )
    return True


@dataclass
class LockAcquisition:
    ok: bool
    correlation_id: str
    session_id: str | None = None
    reason: str | None = None
    component: str = "runtime.lock"
    recovery_action: str | None = None
    existing: dict[str, Any] | None = None


def acquire_lock(
    *,
    session_id: str,
    correlation_id: str | None = None,
    instruction: str | None = None,
    allow_reclaim: bool = True,
    repo_root: Path | None = None,
) -> LockAcquisition:
    """Acquire exclusive runtime lock. Fails if another live instance holds it."""
    cid = correlation_id or f"CORR-{uuid4().hex[:12].upper()}"
    if allow_reclaim:
        reclaim_stale_lock(repo_root)

    path = lock_path(repo_root)
    current = read_lock(repo_root)
    if current:
        pid = current.get("pid")
        if pid and is_process_alive(int(pid)):
            return LockAcquisition(
                ok=False,
                correlation_id=cid,
                session_id=session_id,
                reason=(
                    f"Runtime already held by pid={pid} "
                    f"session={current.get('session_id')} "
                    f"status={current.get('status')}"
                ),
                recovery_action="wait_or_stop_existing_runtime",
                existing=current,
            )
        # stale
        release_lock(force=True, repo_root=repo_root)

    payload = {
        "pid": os.getpid(),
        "session_id": session_id,
        "correlation_id": cid,
        "status": RuntimeState.STARTING.value,
        "instruction": instruction,
        "acquired_at": utc_now_iso(),
        "host": os.uname().nodename if hasattr(os, "uname") else "unknown",
    }
    # O_EXCL style: write only if missing
    try:
        fd = os.open(str(path), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    except FileExistsError:
        existing = read_lock(repo_root)
        return LockAcquisition(
            ok=False,
            correlation_id=cid,
            session_id=session_id,
            reason="Concurrent lock acquisition race",
            recovery_action="retry_start_once",
            existing=existing,
        )
    except OSError as exc:
        return LockAcquisition(
            ok=False,
            correlation_id=cid,
            session_id=session_id,
            reason=f"Filesystem lock error: {exc}",
            recovery_action="check_permissions_and_disk",
        )

    write_status(
        {
            "status": RuntimeState.STARTING.value,
            "session_id": session_id,
            "correlation_id": cid,
            "pid": os.getpid(),
            "started_at": utc_now_iso(),
            "stopped_at": None,
            "instruction": instruction,
            "current_stage": "startup",
            "current_task": "Acquiring runtime lock",
            "documents_processed": 0,
            "knowledge_candidates": 0,
            "uptime_seconds": 0,
            "last_error": None,
            "health": default_health(),
        },
        repo_root=repo_root,
    )
    return LockAcquisition(
        ok=True,
        correlation_id=cid,
        session_id=session_id,
    )


class RuntimeLifecycle:
    """Owns state transitions for a single live session."""

    def __init__(
        self,
        *,
        session_id: str,
        correlation_id: str,
        repo_root: Path | None = None,
        instruction: str | None = None,
    ) -> None:
        self.session_id = session_id
        self.correlation_id = correlation_id
        self.repo_root = repo_root or find_repo_root()
        self.instruction = instruction
        self._state = RuntimeState.IDLE
        self.started_at: str | None = None
        self.documents_processed = 0
        self.knowledge_candidates = 0

    @property
    def state(self) -> RuntimeState:
        return self._state

    def transition(
        self,
        new_state: RuntimeState,
        *,
        stage: str | None = None,
        task: str | None = None,
        error: dict[str, Any] | None = None,
        health: dict[str, str] | None = None,
        **extra: Any,
    ) -> dict[str, Any]:
        allowed = VALID_TRANSITIONS.get(self._state.value, set())
        # Allow same-state refresh while running
        if new_state != self._state and new_state.value not in allowed:
            # Force-safe transitions for crash recovery
            if new_state in {RuntimeState.FAILED, RuntimeState.STOPPED}:
                pass
            else:
                raise ValueError(
                    f"Invalid lifecycle transition {self._state.value} → {new_state.value}"
                )
        self._state = new_state
        if new_state == RuntimeState.STARTING and not self.started_at:
            self.started_at = utc_now_iso()

        # Update lock status field if we own it
        lock = read_lock(self.repo_root)
        if lock and lock.get("session_id") == self.session_id:
            lock["status"] = new_state.value
            lock["updated_at"] = utc_now_iso()
            _atomic_write(lock_path(self.repo_root), lock)

        payload: dict[str, Any] = {
            "status": new_state.value,
            "session_id": self.session_id,
            "correlation_id": self.correlation_id,
            "pid": os.getpid(),
            "started_at": self.started_at,
            "instruction": self.instruction,
            "documents_processed": self.documents_processed,
            "knowledge_candidates": self.knowledge_candidates,
            **extra,
        }
        if stage is not None:
            payload["current_stage"] = stage
        if task is not None:
            payload["current_task"] = task
        if health is not None:
            payload["health"] = {**default_health(), **health}
        if error is not None:
            payload["last_error"] = error
        if new_state in {RuntimeState.STOPPED, RuntimeState.FAILED, RuntimeState.IDLE}:
            payload["stopped_at"] = utc_now_iso()
        return write_status(payload, repo_root=self.repo_root)

    def mark_progress(
        self,
        *,
        stage: str | None = None,
        task: str | None = None,
        documents_processed: int | None = None,
        knowledge_candidates: int | None = None,
        health: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        if documents_processed is not None:
            self.documents_processed = documents_processed
        if knowledge_candidates is not None:
            self.knowledge_candidates = knowledge_candidates
        if self._state == RuntimeState.STARTING:
            return self.transition(
                RuntimeState.RUNNING,
                stage=stage,
                task=task,
                health=health,
            )
        if self._state != RuntimeState.RUNNING:
            return read_status(self.repo_root)
        return write_status(
            {
                "status": RuntimeState.RUNNING.value,
                "session_id": self.session_id,
                "correlation_id": self.correlation_id,
                "pid": os.getpid(),
                "started_at": self.started_at,
                "current_stage": stage,
                "current_task": task,
                "documents_processed": self.documents_processed,
                "knowledge_candidates": self.knowledge_candidates,
                **({"health": {**default_health(), **health}} if health else {}),
            },
            repo_root=self.repo_root,
        )

    def release(self, *, force: bool = False) -> None:
        release_lock(
            session_id=self.session_id,
            correlation_id=self.correlation_id,
            force=force,
            repo_root=self.repo_root,
        )
