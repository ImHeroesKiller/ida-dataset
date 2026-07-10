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


def safe_sync_and_push(
    root: Path,
    *,
    remote: str = "origin",
    branch: str | None = None,
    max_retries: int = 3,
) -> dict[str, Any]:
    """Fetch, rebase onto remote, push with retries. Never force-push.

    On unresolvable conflict: abort rebase and return ok=False.
    Local commits are preserved.
    """
    root = Path(root)
    if not branch:
        br = git_run(root, ["rev-parse", "--abbrev-ref", "HEAD"])
        branch = (br.stdout or "main").strip() or "main"

    messages: list[str] = []
    for attempt in range(1, max_retries + 1):
        messages.append(f"attempt={attempt}")
        fetch = git_run(root, ["fetch", remote, "--prune"])
        if fetch.returncode != 0:
            messages.append(f"fetch_failed: {(fetch.stderr or fetch.stdout or '').strip()}")
            time.sleep(attempt * 2)
            continue

        # remote branch may not exist
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
                return {
                    "ok": True,
                    "pushed": False,
                    "already_up_to_date": True,
                    "messages": messages,
                    "branch": branch,
                }

        push = git_run(root, ["push", remote, f"HEAD:{branch}"])
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
