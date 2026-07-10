#!/usr/bin/env python3
"""Git working-tree snapshots for production reliability.

IMPORTANT: When --ephemeral is set, writes only under /tmp (or RUNNER_TEMP)
so this tracer cannot dirty the git worktree after commit.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=str(root),
        capture_output=True,
        text=True,
        check=False,
    )


def porcelain(root: Path) -> list[str]:
    r = git(root, "status", "--porcelain=v1")
    return [ln for ln in (r.stdout or "").splitlines() if ln.strip()]


def append_trace(
    root: Path,
    stage: str,
    *,
    ephemeral: bool = False,
) -> dict[str, Any]:
    lines = porcelain(root)
    status = git(root, "status", "--porcelain=v1")
    names = git(root, "diff", "--name-only")
    stat = git(root, "diff", "--stat")

    block = [
        f"## {stage}",
        "",
        f"- **time:** {_utc()}",
        f"- **dirty_count:** {len(lines)}",
        "",
        "### status --porcelain=v1",
        "",
        "```",
        (status.stdout or "").rstrip() or "(empty)",
        "```",
        "",
        "### diff --name-only",
        "",
        "```",
        (names.stdout or "").rstrip() or "(empty)",
        "```",
        "",
        "### diff --stat",
        "",
        "```",
        (stat.stdout or "").rstrip() or "(empty)",
        "```",
        "",
    ]
    text = "\n".join(block)

    # Always print to CI log
    print(text)

    if ephemeral:
        base = Path(os.environ.get("RUNNER_TEMP") or os.environ.get("TMPDIR") or "/tmp")
        out = base / "ida-worktree-trace.md"
        with out.open("a", encoding="utf-8", newline="\n") as f:
            f.write(text + "\n")
        return {"stage": stage, "dirty": bool(lines), "count": len(lines), "path": str(out)}

    report = root / "reports" / "reliability" / "git_worktree_trace.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    if not report.exists():
        report.write_text(
            "# Git Working Tree Trace\n\n"
            "Snapshots after each production stage.\n\n",
            encoding="utf-8",
            newline="\n",
        )
    with report.open("a", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    return {
        "stage": stage,
        "dirty": bool(lines),
        "count": len(lines),
        "files": lines,
        "path": str(report),
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Record git worktree snapshot")
    p.add_argument("--stage", required=True)
    p.add_argument("--fail-if-dirty", action="store_true")
    p.add_argument(
        "--ephemeral",
        action="store_true",
        help="Write only under TMPDIR/RUNNER_TEMP (safe after git commit)",
    )
    p.add_argument("--repo-root", default=".")
    args = p.parse_args(argv)
    root = Path(args.repo_root).resolve()
    snap = append_trace(root, args.stage, ephemeral=args.ephemeral)
    if args.fail_if_dirty and snap["dirty"]:
        # Only fail on tracked dirt
        tracked = porcelain(root)
        tracked = [
            ln
            for ln in tracked
            if not ln.startswith("??")
            or not any(
                ln[3:].startswith(p)
                for p in (
                    "automation/connectors/cache/",
                    "automation/raw_documents/",
                    "automation/documents/",
                )
            )
        ]
        # re-check tracked-only
        r = git(root, "status", "--porcelain=v1", "--untracked-files=no")
        tracked_lines = [ln for ln in (r.stdout or "").splitlines() if ln.strip()]
        if tracked_lines:
            print("DIRTY working tree (tracked):")
            for f in tracked_lines:
                print(f"  {f}")
            return 1
    print(f"stage={args.stage} dirty={snap['dirty']} count={snap['count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
