"""Safe git synchronize + push helpers for factory CI (no force-push)."""

from __future__ import annotations

import subprocess
import time
from pathlib import Path
from typing import Any


def git_run(root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=str(root),
        capture_output=True,
        text=True,
        check=False,
    )


def is_worktree_clean(root: Path) -> tuple[bool, list[str]]:
    st = git_run(root, ["status", "--porcelain"])
    lines = [ln for ln in (st.stdout or "").splitlines() if ln.strip()]
    d1 = git_run(root, ["diff", "--exit-code"])
    d2 = git_run(root, ["diff", "--cached", "--exit-code"])
    clean = not lines and d1.returncode == 0 and d2.returncode == 0
    return clean, lines


def safe_sync_and_push(
    root: Path,
    *,
    remote: str = "origin",
    branch: str | None = None,
    max_retries: int = 3,
) -> dict[str, Any]:
    """Delegate to scripts/git_safe_sync_push.sh (canonical implementation)."""
    root = Path(root)
    script = root / "scripts" / "git_safe_sync_push.sh"
    if not branch:
        br = git_run(root, ["rev-parse", "--abbrev-ref", "HEAD"])
        branch = (br.stdout or "main").strip() or "main"

    if script.exists():
        proc = subprocess.run(
            ["bash", str(script), remote, branch],
            cwd=str(root),
            capture_output=True,
            text=True,
            check=False,
            env={
                **dict(**{k: v for k, v in __import__("os").environ.items()}),
                "GIT_SAFE_PUSH_RETRIES": str(max_retries),
            },
        )
        return {
            "ok": proc.returncode == 0,
            "pushed": "push ok" in (proc.stdout or ""),
            "returncode": proc.returncode,
            "stdout": proc.stdout or "",
            "stderr": proc.stderr or "",
            "branch": branch,
            "messages": [ln for ln in (proc.stdout or "").splitlines() if ln.strip()],
        }

    # Fallback pure-Python path (no force-push)
    messages: list[str] = []
    for attempt in range(1, max_retries + 1):
        messages.append(f"attempt={attempt}")
        clean, dirty = is_worktree_clean(root)
        if not clean:
            messages.append(f"dirty_pre_rebase:{dirty[:20]}")
            git_run(
                root,
                [
                    "stash",
                    "push",
                    "--include-untracked",
                    "-m",
                    f"factory-safe-sync-{attempt}",
                ],
            )
            messages.append("stashed")

        fetch = git_run(root, ["fetch", remote, "--prune"])
        if fetch.returncode != 0:
            messages.append(f"fetch_failed: {(fetch.stderr or fetch.stdout or '').strip()}")
            time.sleep(attempt * 2)
            continue

        has_remote = (
            git_run(root, ["rev-parse", "--verify", f"{remote}/{branch}"]).returncode
            == 0
        )
        if has_remote:
            pull = git_run(root, ["pull", "--rebase", remote, branch])
            if pull.returncode != 0:
                git_run(root, ["rebase", "--abort"])
                messages.append(
                    f"rebase_conflict_aborted: {(pull.stderr or pull.stdout or '').strip()}"
                )
                time.sleep(attempt * 2)
                continue
            messages.append("rebase_ok_or_uptodate")

            local = git_run(root, ["rev-parse", "HEAD"]).stdout.strip()
            remote_sha = git_run(
                root, ["rev-parse", f"{remote}/{branch}"]
            ).stdout.strip()
            if local and remote_sha and local == remote_sha:
                git_run(root, ["stash", "pop"])
                return {
                    "ok": True,
                    "pushed": False,
                    "already_up_to_date": True,
                    "messages": messages,
                    "branch": branch,
                }

        push = git_run(root, ["push", remote, f"HEAD:{branch}"])
        git_run(root, ["stash", "pop"])
        if push.returncode == 0:
            messages.append("push_ok")
            return {
                "ok": True,
                "pushed": True,
                "already_up_to_date": False,
                "messages": messages,
                "branch": branch,
            }
        messages.append(f"push_failed: {(push.stderr or push.stdout or '').strip()}")
        time.sleep(attempt * 2)

    return {
        "ok": False,
        "pushed": False,
        "already_up_to_date": False,
        "messages": messages,
        "branch": branch,
        "error": "safe_push_exhausted_retries",
    }
