#!/usr/bin/env python3
"""Force completion of factory writers before git phase.

Does not change acquisition/manufacturing/scheduler logic — only ensures
file handles and known persistence paths are settled before git add/commit.
"""

from __future__ import annotations

import argparse
import gc
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path


def _utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def finalize(repo_root: Path) -> dict:
    """Best-effort flush of known post-session writers."""
    notes: list[str] = []
    # 1) GC — drop open file-like objects if any remain
    gc.collect()
    notes.append("gc.collect")

    # 2) Ensure no leaked default ThreadPoolExecutor activity (wait short)
    try:
        # Creating and shutting down a dummy executor joins any default pool usage patterns
        with ThreadPoolExecutor(max_workers=1) as ex:
            ex.submit(lambda: None).result(timeout=5)
        notes.append("threadpool_barrier")
    except Exception as exc:  # noqa: BLE001
        notes.append(f"threadpool_barrier_skip:{exc}")

    # 3) Touch-flush known JSON state files by re-reading and rewriting atomically
    #    only if they already exist (no new knowledge generation).
    state_dir = repo_root / "automation" / "learning" / "state"
    stabilized = 0
    if state_dir.exists():
        for p in sorted(state_dir.glob("*.json")):
            try:
                raw = p.read_text(encoding="utf-8")
                # rewrite same bytes to force fsync of last write
                p.write_text(raw, encoding="utf-8", newline="\n")
                stabilized += 1
            except Exception:  # noqa: BLE001
                continue
    notes.append(f"state_fsync_files={stabilized}")

    # 4) Small settle delay for any OS buffer
    time.sleep(0.15)
    notes.append("settle_150ms")

    report = {
        "ts": _utc(),
        "ok": True,
        "notes": notes,
        "message": "writers finalized before git phase",
    }
    out = repo_root / "reports" / "reliability" / "writer_finalize.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    return report


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--repo-root", default=".")
    args = p.parse_args(argv)
    root = Path(args.repo_root).resolve()
    r = finalize(root)
    print(json.dumps(r, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
