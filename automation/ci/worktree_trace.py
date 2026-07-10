#!/usr/bin/env python3
"""Git working-tree snapshots for production reliability.

Usage:
  python automation/ci/worktree_trace.py --stage acquire
  python automation/ci/worktree_trace.py --stage pre_rebase --fail-if-dirty
"""

from __future__ import annotations

import argparse
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
    r = git(root, "status", "--porcelain")
    lines = [ln for ln in (r.stdout or "").splitlines() if ln.strip()]
    return lines


def classify(lines: list[str]) -> dict[str, list[str]]:
    modified: list[str] = []
    deleted: list[str] = []
    untracked: list[str] = []
    staged: list[str] = []
    other: list[str] = []
    for ln in lines:
        code = ln[:2]
        path = ln[3:].strip() if len(ln) > 3 else ln
        if code == "??":
            untracked.append(path)
        elif "D" in code:
            deleted.append(path)
        elif code.strip() and code[0] != " ":
            staged.append(path)
            if "M" in code or "A" in code:
                modified.append(path)
        elif "M" in code:
            modified.append(path)
        else:
            other.append(path)
    return {
        "modified": modified,
        "deleted": deleted,
        "untracked": untracked,
        "staged": staged,
        "other": other,
        "all": lines,
    }


def append_trace(
    root: Path,
    stage: str,
    *,
    extra: str = "",
) -> dict[str, Any]:
    lines = porcelain(root)
    parts = classify(lines)
    report = root / "reports" / "reliability" / "git_worktree_trace.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    if not report.exists():
        report.write_text(
            "# Git Working Tree Trace\n\n"
            "Snapshots after each production stage. Dirty files after commit indicate post-commit writers.\n\n",
            encoding="utf-8",
            newline="\n",
        )
    block = [
        f"## {stage}",
        "",
        f"- **time:** {_utc()}",
        f"- **dirty_count:** {len(lines)}",
        f"- **modified:** {len(parts['modified'])}",
        f"- **deleted:** {len(parts['deleted'])}",
        f"- **untracked:** {len(parts['untracked'])}",
        f"- **staged:** {len(parts['staged'])}",
        "",
    ]
    if lines:
        block.append("```")
        block.extend(lines[:200])
        if len(lines) > 200:
            block.append(f"... ({len(lines) - 200} more)")
        block.append("```")
    else:
        block.append("_clean_")
    if extra:
        block += ["", extra, ""]
    block.append("")
    with report.open("a", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(block))
    return {
        "stage": stage,
        "dirty": bool(lines),
        "count": len(lines),
        "files": lines,
        **{k: v for k, v in parts.items() if k != "all"},
    }


def is_clean(root: Path) -> tuple[bool, list[str]]:
    lines = porcelain(root)
    # Also check unstaged and staged diffs
    d1 = git(root, "diff", "--exit-code")
    d2 = git(root, "diff", "--cached", "--exit-code")
    clean = not lines and d1.returncode == 0 and d2.returncode == 0
    return clean, lines


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Record git worktree snapshot")
    p.add_argument("--stage", required=True)
    p.add_argument("--fail-if-dirty", action="store_true")
    p.add_argument("--repo-root", default=".")
    args = p.parse_args(argv)
    root = Path(args.repo_root).resolve()
    snap = append_trace(root, args.stage)
    if args.fail_if_dirty and snap["dirty"]:
        print("DIRTY working tree:")
        for f in snap["files"]:
            print(f"  {f}")
        return 1
    print(
        f"stage={args.stage} dirty={snap['dirty']} count={snap['count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
