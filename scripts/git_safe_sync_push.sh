#!/usr/bin/env bash
# Safe git synchronize + push for factory production workflows.
# Never force-push. Never overwrite remote history. Abort on unresolvable conflict.
#
# Usage:
#   scripts/git_safe_sync_push.sh [remote] [branch]
#
# Exit codes:
#   0  success (pushed or nothing to push)
#   1  conflict / push failed after retries (safe abort)
#   2  usage / environment error

set -euo pipefail

REMOTE="${1:-origin}"
BRANCH="${2:-${GITHUB_REF_NAME:-$(git rev-parse --abbrev-ref HEAD)}}"
MAX_RETRIES="${GIT_SAFE_PUSH_RETRIES:-3}"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "git_safe_sync_push: not a git repository" >&2
  exit 2
fi

echo "git_safe_sync_push: remote=${REMOTE} branch=${BRANCH}"

# Ensure we never force-push
git config --local push.default simple || true

sync_once() {
  echo "→ fetch ${REMOTE}"
  git fetch "${REMOTE}" --prune

  # If remote branch does not exist yet, first push is allowed
  if ! git rev-parse --verify "${REMOTE}/${BRANCH}" >/dev/null 2>&1; then
    echo "→ remote branch missing; will push new branch"
    return 0
  fi

  # Prefer rebase onto remote tip (preserves linear history without overwrite)
  echo "→ pull --rebase ${REMOTE} ${BRANCH}"
  if git pull --rebase "${REMOTE}" "${BRANCH}"; then
    echo "→ rebase complete (or already up-to-date)"
    return 0
  fi

  # Rebase conflict: abort safely, never leave partial rebase
  echo "git_safe_sync_push: rebase conflict — aborting rebase safely" >&2
  git rebase --abort 2>/dev/null || true
  return 1
}

push_once() {
  # Refuse force flags even if env tries
  if [[ "${FORCE_PUSH:-}" == "true" ]]; then
    echo "git_safe_sync_push: FORCE_PUSH refused by factory policy" >&2
    return 1
  fi
  git push "${REMOTE}" "HEAD:${BRANCH}"
}

attempt=1
while [[ "${attempt}" -le "${MAX_RETRIES}" ]]; do
  echo "git_safe_sync_push: attempt ${attempt}/${MAX_RETRIES}"
  if ! sync_once; then
    echo "git_safe_sync_push: sync failed on attempt ${attempt}" >&2
    attempt=$((attempt + 1))
    sleep $((attempt * 2))
    continue
  fi

  # Nothing ahead? still try push (no-op if up to date)
  if git rev-parse --verify "${REMOTE}/${BRANCH}" >/dev/null 2>&1; then
    LOCAL=$(git rev-parse HEAD)
    REMOTE_SHA=$(git rev-parse "${REMOTE}/${BRANCH}")
    if [[ "${LOCAL}" == "${REMOTE_SHA}" ]]; then
      echo "git_safe_sync_push: already up-to-date with ${REMOTE}/${BRANCH}"
      exit 0
    fi
  fi

  if push_once; then
    echo "git_safe_sync_push: push ok"
    exit 0
  fi

  echo "git_safe_sync_push: push rejected — will re-sync and retry" >&2
  attempt=$((attempt + 1))
  sleep $((attempt * 2))
done

echo "git_safe_sync_push: FAILED after ${MAX_RETRIES} attempts (safe abort; local history preserved)" >&2
exit 1
