#!/usr/bin/env python3
"""Certify clean git worktree before rebase/push.

Loops: refresh index → status → stage factory paths → finalize commit
until clean or max rounds exceeded.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


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


def porcelain(root: Path, *, untracked: str = "all") -> list[str]:
    args = ["status", "--porcelain=v1"]
    if untracked == "no":
        args.append("--untracked-files=no")
    r = git(root, *args)
    return [ln for ln in (r.stdout or "").splitlines() if ln.strip()]


def dump_diag(root: Path, name: str) -> Path:
    out = root / "reports" / "reliability" / name
    out.parent.mkdir(parents=True, exist_ok=True)
    status = git(root, "status", "--porcelain=v1")
    names = git(root, "diff", "--name-only")
    stat = git(root, "diff", "--stat")
    cached_names = git(root, "diff", "--cached", "--name-only")
    body = [
        f"# {name}",
        "",
        f"- **time:** {_utc()}",
        "",
        "## git status --porcelain=v1",
        "",
        "```",
        (status.stdout or "").rstrip() or "(empty)",
        "```",
        "",
        "## git diff --name-only",
        "",
        "```",
        (names.stdout or "").rstrip() or "(empty)",
        "```",
        "",
        "## git diff --stat",
        "",
        "```",
        (stat.stdout or "").rstrip() or "(empty)",
        "```",
        "",
        "## git diff --cached --name-only",
        "",
        "```",
        (cached_names.stdout or "").rstrip() or "(empty)",
        "```",
        "",
    ]
    out.write_text("\n".join(body), encoding="utf-8", newline="\n")
    print(out.read_text(encoding="utf-8"))
    return out


def stage_factory(root: Path, *, dry_run: bool) -> None:
    paths = [
        "automation/sessions/",
        "automation/learning/state/",
        "automation/queue/",
        "automation/missions/",
        "reports/",
        "scripts/",
        "automation/ci/",
        "automation/lib/git_safe.py",
        ".github/workflows/",
    ]
    for p in paths:
        git(root, "add", "-A", "--", p)
    if not dry_run:
        git(root, "add", "-A", "--", "domains/")
    # Stage remaining tracked modifications
    st = porcelain(root)
    for ln in st:
        path = ln[3:].strip() if len(ln) > 3 else ""
        if not path:
            continue
        if ln.startswith("??"):
            if path.startswith(
                (
                    "automation/connectors/cache/",
                    "automation/raw_documents/",
                    "automation/documents/",
                    "node_modules/",
                    ".next/",
                )
            ):
                continue
        git(root, "add", "--", path)


def certify(
    root: Path,
    *,
    dry_run: bool = False,
    max_rounds: int = 5,
    commit_message: str = "chore(ci): finalize generated artifacts",
) -> int:
    git(root, "update-index", "--refresh")
    dump_diag(root, "worktree_before_certify.md")
    commits_made = 0

    for round_i in range(1, max_rounds + 1):
        git(root, "update-index", "--refresh")
        dirty = porcelain(root)
        # Ignore pure untracked cache dirs
        meaningful = []
        for ln in dirty:
            path = ln[3:].strip() if len(ln) > 3 else ln
            if ln.startswith("??") and path.startswith(
                (
                    "automation/connectors/cache/",
                    "automation/raw_documents/",
                    "automation/documents/",
                    "node_modules/",
                    ".next/",
                )
            ):
                continue
            meaningful.append(ln)

        if not meaningful:
            # Also require no unstaged/staged diffs on tracked files
            if (
                git(root, "diff", "--exit-code").returncode == 0
                and git(root, "diff", "--cached", "--exit-code").returncode == 0
            ):
                dump_diag(root, "worktree_certified_clean.md")
                print(f"CERTIFIED_CLEAN round={round_i}")
                print(f"COMMITS_MADE={commits_made}")
                return 0

        print(f"DIRTY round={round_i}:")
        for ln in meaningful:
            print(f"  {ln}")

        stage_factory(root, dry_run=dry_run)
        if git(root, "diff", "--cached", "--quiet").returncode != 0:
            msg = commit_message if round_i == 1 else f"{commit_message} (round {round_i})"
            c = git(root, "commit", "-m", msg)
            print(c.stdout or "")
            print(c.stderr or "", file=sys.stderr)
            if c.returncode == 0:
                commits_made += 1
            else:
                print("commit failed", file=sys.stderr)
        else:
            print("nothing staged after git add")

    dump_diag(root, "worktree_certify_failed.md")
    dirty = porcelain(root)
    print("ABORT: worktree cannot become clean")
    print("Modified/untracked remaining:")
    for ln in dirty:
        print(f"  {ln}")
    print(f"COMMITS_MADE={commits_made}")
    return 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--repo-root", default=".")
    p.add_argument("--dry-run-session", action="store_true")
    p.add_argument("--max-rounds", type=int, default=5)
    p.add_argument(
        "--message",
        default="chore(ci): finalize generated artifacts",
    )
    args = p.parse_args(argv)
    root = Path(args.repo_root).resolve()
    return certify(
        root,
        dry_run=args.dry_run_session,
        max_rounds=args.max_rounds,
        commit_message=args.message,
    )


if __name__ == "__main__":
    raise SystemExit(main())
