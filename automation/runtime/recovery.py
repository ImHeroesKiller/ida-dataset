"""Automatic recovery policy for recoverable runtime failures.

Recoverable: temporary IO, connector, queue failures (limited retries).
Unrecoverable: stop safely and notify dashboard — never silent continue.
"""

from __future__ import annotations

import time
from typing import Any, Callable, TypeVar

from automation.runtime.channels import log
from automation.runtime.errors import classify_recoverable, record_failure

T = TypeVar("T")

DEFAULT_MAX_ATTEMPTS = 3
DEFAULT_BACKOFF_SECONDS = (0.5, 1.5, 3.0)


def run_with_recovery(
    fn: Callable[[], T],
    *,
    component: str,
    session_id: str | None = None,
    correlation_id: str | None = None,
    max_attempts: int = DEFAULT_MAX_ATTEMPTS,
    backoff: tuple[float, ...] = DEFAULT_BACKOFF_SECONDS,
    on_unrecoverable: Callable[[dict[str, Any]], None] | None = None,
    repo_root: Any = None,
) -> T:
    """Execute fn with limited retries for recoverable failures only."""
    last_exc: BaseException | None = None
    attempts = max(1, max_attempts)
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001
            last_exc = exc
            recoverable = classify_recoverable(exc, component=component)
            record = record_failure(
                component=component,
                exception=exc,
                session_id=session_id,
                correlation_id=correlation_id,
                recovery_action="auto_retry" if recoverable and attempt < attempts else "stop_and_notify",
                meta={"attempt": attempt, "max_attempts": attempts},
                update_status=not recoverable or attempt >= attempts,
                repo_root=repo_root,
            )
            log(
                "errors",
                f"{component} attempt {attempt}/{attempts}: {exc}",
                module="recovery",
                level="WARNING" if recoverable else "ERROR",
                session_id=session_id,
                correlation_id=correlation_id,
                meta={"recoverable": recoverable, "attempt": attempt},
                repo_root=repo_root,
            )
            if not recoverable or attempt >= attempts:
                if on_unrecoverable:
                    on_unrecoverable(record)
                raise
            delay = backoff[min(attempt - 1, len(backoff) - 1)]
            time.sleep(delay)
    assert last_exc is not None
    raise last_exc
