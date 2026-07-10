#!/usr/bin/env python3
"""Stress / stability tests for live runtime lock, lifecycle, recovery.

Run:
  python3 -m automation.runtime.tests.test_runtime_stability
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import threading
import time
import traceback
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from automation.runtime.channels import log, read_channel, set_context, clear_context
from automation.runtime.errors import classify_recoverable, record_failure
from automation.runtime.lifecycle import (
    RuntimeLifecycle,
    RuntimeState,
    acquire_lock,
    is_process_alive,
    read_lock,
    read_status,
    reclaim_stale_lock,
    release_lock,
    write_status,
)
from automation.runtime.recovery import run_with_recovery


class Results:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.errors: list[str] = []

    def ok(self, name: str) -> None:
        self.passed += 1
        print(f"  PASS  {name}")

    def fail(self, name: str, msg: str) -> None:
        self.failed += 1
        self.errors.append(f"{name}: {msg}")
        print(f"  FAIL  {name}: {msg}")


def _tmp_root() -> Path:
    d = Path(tempfile.mkdtemp(prefix="ida-runtime-test-"))
    (d / "VERSION").write_text("0.0.0-test\n", encoding="utf-8")
    (d / "domains").mkdir()
    return d


def test_lock_exclusive(r: Results) -> None:
    root = _tmp_root()
    a = acquire_lock(session_id="SES-A", correlation_id="CORR-A", repo_root=root)
    if not a.ok:
        r.fail("lock_exclusive_first", a.reason or "first acquire failed")
        return
    r.ok("lock_exclusive_first")

    b = acquire_lock(session_id="SES-B", correlation_id="CORR-B", repo_root=root)
    if b.ok:
        r.fail("lock_exclusive_second", "second acquire should fail while first holds")
    else:
        r.ok("lock_exclusive_second")

    release_lock(session_id="SES-A", correlation_id="CORR-A", repo_root=root)
    c = acquire_lock(session_id="SES-C", correlation_id="CORR-C", repo_root=root)
    if c.ok:
        r.ok("lock_release_and_reacquire")
    else:
        r.fail("lock_release_and_reacquire", c.reason or "reacquire failed")
    release_lock(force=True, repo_root=root)


def test_stale_lock_reclaim(r: Results) -> None:
    root = _tmp_root()
    lock_file = root / "automation" / "runtime" / "state" / "runtime.lock.json"
    lock_file.parent.mkdir(parents=True, exist_ok=True)
    lock_file.write_text(
        json.dumps(
            {
                "pid": 99999999,
                "session_id": "SES-DEAD",
                "correlation_id": "CORR-DEAD",
                "status": "running",
            }
        ),
        encoding="utf-8",
    )
    write_status(
        {"status": "running", "session_id": "SES-DEAD", "pid": 99999999},
        repo_root=root,
    )
    reclaimed = reclaim_stale_lock(repo_root=root)
    if not reclaimed:
        r.fail("stale_lock_reclaim", "expected reclaim of dead pid")
        return
    if read_lock(repo_root=root) is not None:
        r.fail("stale_lock_reclaim", "lock file still present")
        return
    r.ok("stale_lock_reclaim")


def test_lifecycle_transitions(r: Results) -> None:
    root = _tmp_root()
    lock = acquire_lock(session_id="SES-L", correlation_id="CORR-L", repo_root=root)
    if not lock.ok:
        r.fail("lifecycle_start", lock.reason or "lock failed")
        return
    lc = RuntimeLifecycle(
        session_id="SES-L",
        correlation_id="CORR-L",
        repo_root=root,
        instruction="test",
    )
    try:
        lc.transition(RuntimeState.STARTING, stage="startup", task="boot")
        lc.transition(RuntimeState.RUNNING, stage="mission", task="work")
        lc.mark_progress(stage="pipeline", task="read", documents_processed=2)
        lc.transition(RuntimeState.STOPPING, stage="complete", task="wind down")
        lc.transition(RuntimeState.STOPPED, stage="complete", task="done")
        st = read_status(repo_root=root)
        if st.get("status") != "stopped":
            r.fail("lifecycle_transitions", f"status={st.get('status')}")
        elif st.get("documents_processed") != 2:
            r.fail("lifecycle_transitions", f"docs={st.get('documents_processed')}")
        else:
            r.ok("lifecycle_transitions")
    except Exception as exc:  # noqa: BLE001
        r.fail("lifecycle_transitions", str(exc))
    finally:
        lc.release(force=True)


def test_invalid_transition_blocked(r: Results) -> None:
    root = _tmp_root()
    lc = RuntimeLifecycle(
        session_id="SES-X", correlation_id="CORR-X", repo_root=root
    )
    try:
        lc.transition(RuntimeState.RUNNING)
        r.fail("invalid_transition", "should have raised")
    except ValueError:
        r.ok("invalid_transition")
    except Exception as exc:  # noqa: BLE001
        r.fail("invalid_transition", f"wrong exception {exc}")


def test_error_record_shape(r: Results) -> None:
    root = _tmp_root()
    rec = record_failure(
        component="test.component",
        exception=RuntimeError("boom"),
        session_id="SES-E",
        correlation_id="CORR-E",
        recovery_action="stop_and_notify",
        repo_root=root,
    )
    required = {
        "timestamp",
        "component",
        "exception",
        "stack_trace",
        "correlation_id",
        "session_id",
        "recovery_action",
    }
    missing = required - set(rec.keys())
    if missing:
        r.fail("error_record_shape", f"missing {missing}")
    else:
        r.ok("error_record_shape")
    log_dir = root / "automation" / "runtime" / "logs"
    if not any(log_dir.glob("error_*.json")):
        r.fail("error_record_file", "no error_*.json written")
    else:
        r.ok("error_record_file")


def test_channel_logging(r: Results) -> None:
    root = _tmp_root()
    set_context(session_id="SES-C", correlation_id="CORR-C")
    try:
        log(
            "runtime",
            "hello channel",
            module="test",
            duration_ms=12.5,
            repo_root=root,
        )
        rows = read_channel("runtime", limit=5, repo_root=root)
        if not rows:
            r.fail("channel_logging", "no rows")
            return
        row = rows[0]
        for key in ("timestamp", "session_id", "correlation_id", "module", "duration_ms"):
            if key not in row:
                r.fail("channel_logging", f"missing {key}")
                return
        r.ok("channel_logging")
    finally:
        clear_context()


def test_recovery_retry_then_succeed(r: Results) -> None:
    root = _tmp_root()
    state = {"n": 0}

    def flaky() -> str:
        state["n"] += 1
        if state["n"] < 3:
            raise OSError("temporary io")
        return "ok"

    out = run_with_recovery(
        flaky,
        component="queue.io",
        session_id="SES-R",
        correlation_id="CORR-R",
        max_attempts=3,
        backoff=(0.01, 0.01, 0.01),
        repo_root=root,
    )
    if out == "ok" and state["n"] == 3:
        r.ok("recovery_retry_then_succeed")
    else:
        r.fail("recovery_retry_then_succeed", f"out={out} n={state['n']}")


def test_recovery_unrecoverable_no_retry(r: Results) -> None:
    root = _tmp_root()
    state = {"n": 0}

    def bad() -> None:
        state["n"] += 1
        raise ImportError("missing module")

    try:
        run_with_recovery(
            bad,
            component="runtime.import",
            session_id="SES-U",
            correlation_id="CORR-U",
            max_attempts=5,
            backoff=(0.01,),
            repo_root=root,
        )
        r.fail("recovery_unrecoverable", "should have raised")
    except ImportError:
        if state["n"] == 1:
            r.ok("recovery_unrecoverable")
        else:
            r.fail("recovery_unrecoverable", f"retried {state['n']} times")


def test_classify_recoverable(r: Results) -> None:
    if not classify_recoverable(OSError("x"), component="queue"):
        r.fail("classify_oserror", "OSError should be recoverable")
    else:
        r.ok("classify_oserror")
    if classify_recoverable(ImportError("x"), component="runtime"):
        r.fail("classify_import", "ImportError should be unrecoverable")
    else:
        r.ok("classify_import")


def test_concurrent_lock_attempts(r: Results) -> None:
    root = _tmp_root()
    winners: list[str] = []
    barrier = threading.Barrier(8)

    def worker(i: int) -> None:
        barrier.wait()
        acq = acquire_lock(
            session_id=f"SES-{i}",
            correlation_id=f"CORR-{i}",
            repo_root=root,
        )
        if acq.ok:
            winners.append(f"SES-{i}")
            time.sleep(0.05)
            release_lock(session_id=f"SES-{i}", correlation_id=f"CORR-{i}", repo_root=root)

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    if len(winners) >= 1:
        r.ok("concurrent_lock_attempts")
    else:
        r.fail("concurrent_lock_attempts", f"winners={winners}")


def test_process_alive_self(r: Results) -> None:
    if is_process_alive(os.getpid()):
        r.ok("process_alive_self")
    else:
        r.fail("process_alive_self", "self pid not alive?")
    if is_process_alive(99999999):
        r.fail("process_dead", "fake pid should be dead")
    else:
        r.ok("process_dead")


def test_no_duplicate_lock_file_after_release(r: Results) -> None:
    root = _tmp_root()
    for i in range(5):
        acq = acquire_lock(
            session_id=f"SES-R{i}",
            correlation_id=f"CORR-R{i}",
            repo_root=root,
        )
        if not acq.ok:
            r.fail("repeat_start_stop", f"iter {i}: {acq.reason}")
            return
        release_lock(
            session_id=f"SES-R{i}",
            correlation_id=f"CORR-R{i}",
            repo_root=root,
        )
    if read_lock(repo_root=root) is None:
        r.ok("repeat_start_stop")
    else:
        r.fail("repeat_start_stop", "lock remains after release cycle")


def main() -> int:
    print("Runtime stability tests")
    print("=" * 50)
    r = Results()
    tests = [
        test_lock_exclusive,
        test_stale_lock_reclaim,
        test_lifecycle_transitions,
        test_invalid_transition_blocked,
        test_error_record_shape,
        test_channel_logging,
        test_recovery_retry_then_succeed,
        test_recovery_unrecoverable_no_retry,
        test_classify_recoverable,
        test_concurrent_lock_attempts,
        test_process_alive_self,
        test_no_duplicate_lock_file_after_release,
    ]
    for fn in tests:
        try:
            fn(r)
        except Exception:  # noqa: BLE001
            r.fail(fn.__name__, traceback.format_exc())
    print("=" * 50)
    print(f"Passed: {r.passed}  Failed: {r.failed}")
    if r.errors:
        print("Failures:")
        for e in r.errors:
            print(f"  - {e}")
    return 0 if r.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
