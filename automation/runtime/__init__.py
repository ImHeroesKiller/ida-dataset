"""Runtime lifecycle, lock, diagnostics, and structured error logging.

Stabilization layer only — no new learning engines.
"""

from .lifecycle import (
    RuntimeLifecycle,
    RuntimeState,
    acquire_lock,
    release_lock,
    read_lock,
    read_status,
    write_status,
    is_process_alive,
)

__all__ = [
    "RuntimeLifecycle",
    "RuntimeState",
    "acquire_lock",
    "release_lock",
    "read_lock",
    "read_status",
    "write_status",
    "is_process_alive",
]
