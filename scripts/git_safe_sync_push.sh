#!/usr/bin/env bash
# Safe git synchronize + push for factory production workflows.
# Never force-push. Never overwrite remote history.
# CRITICAL: Does NOT write into the git worktree during fetch/rebase/push
# (diagnostics go to $TMPDIR / RUNNER_TEMP only) so the tree cannot go dirty mid-sync.
#
# Usage: scripts/git_safe_sync_push.sh [remote] [branch]
# Exit: 0 success | 1 failed | 2 env error

set -euo pipefail

REMOTE="${1:-origin}"
BRANCH="${2:-${GITHUB_REF_NAME:-$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo main)}}"
MAX_RETRIES="${GIT_SAFE_PUSH_RETRIES:-3}"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

RECOVERY_USED="NO"
REBASE_OK="NO"
PUSHED="NO"
STASHED="NO"
ATTEMPT=1
DIAG_DIR="${RUNNER_TEMP:-${TMPDIR:-/tmp}}/ida-git-diag-$$"
mkdir -p "${DIAG_DIR}"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "git_safe_sync_push: not a git repository" >&2
  exit 2
fi

echo "git_safe_sync_push: remote=${REMOTE} branch=${BRANCH}"
echo "git_safe_sync_push: diagnostics_dir=${DIAG_DIR}"
git config --local push.default simple || true
git config --local pull.rebase true || true

if [[ "${FORCE_PUSH:-}" == "true" ]]; then
  echo "git_safe_sync_push: FORCE_PUSH refused by factory policy" >&2
  exit 1
fi

diag_snapshot() {
  local name="$1"
  local f="${DIAG_DIR}/${name}.txt"
  {
    echo "=== ${name} $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
    echo "--- status --porcelain=v1 ---"
    git status --porcelain=v1 || true
    echo "--- diff --name-only ---"
    git diff --name-only || true
    echo "--- diff --stat ---"
    git diff --stat || true
    echo "--- status ---"
    git status || true
  } >"${f}"
  # Also print to job log (required diagnostics)
  cat "${f}"
}

print_telemetry() {
  local clean="YES"
  local dirty
  dirty="$(git status --porcelain=v1 --untracked-files=no 2>/dev/null || true)"
  if [[ -n "${dirty}" ]]; then
    clean="NO"
  fi
  cat <<EOF

======================
Git Working Tree
CLEAN
${clean}
$(if [[ "${clean}" != "YES" ]]; then echo "${dirty}"; fi)
======================
Commits
Pushed
${PUSHED}
======================
Rebase
Success
${REBASE_OK}
======================
Push retries
${ATTEMPT}/${MAX_RETRIES}
======================
Recovery
Used
${RECOVERY_USED}
======================
EOF
  # Optional: copy summary to reports only AFTER push completes (may dirty tree post-success)
  if [[ "${PUSHED}" == "YES" || "${clean}" == "YES" ]]; then
    mkdir -p reports/reliability
    {
      echo "# Push Recovery Report"
      echo ""
      echo "- time: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
      echo "- pushed: ${PUSHED}"
      echo "- rebase_ok: ${REBASE_OK}"
      echo "- recovery_used: ${RECOVERY_USED}"
      echo "- attempts: ${ATTEMPT}/${MAX_RETRIES}"
      echo "- clean_tracked: ${clean}"
      echo "- diagnostics_dir: ${DIAG_DIR}"
      echo ""
    } > reports/reliability/push_recovery_report.md 2>/dev/null || true
  fi
}

verify_clean_tracked() {
  local label="$1"
  diag_snapshot "verify_${label}"
  local dirty
  dirty="$(git status --porcelain=v1 --untracked-files=no 2>/dev/null || true)"
  if [[ -n "${dirty}" ]]; then
    echo "DIRTY tracked worktree (${label}):"
    echo "${dirty}"
    echo "Dirty files:"
    echo "${dirty}"
    return 1
  fi
  if ! git diff --exit-code >/dev/null 2>&1; then
    echo "DIRTY: unstaged tracked diff (${label})"
    git diff --name-only || true
    git diff --stat || true
    return 1
  fi
  if ! git diff --cached --exit-code >/dev/null 2>&1; then
    echo "DIRTY: staged diff (${label})"
    git diff --cached --name-only || true
    return 1
  fi
  echo "CLEAN tracked worktree (${label})"
  return 0
}

auto_finalize_once() {
  echo "→ automatic finalize commit for dirty tree"
  RECOVERY_USED="YES"
  git add -A -- \
    reports/ \
    automation/sessions/ \
    automation/learning/state/ \
    automation/queue/ \
    domains/ \
    scripts/ \
    automation/ci/ \
    automation/lib/git_safe.py \
    .github/workflows/ \
    2>/dev/null || true
  # stage remaining tracked dirt
  while IFS= read -r line; do
    [[ -z "${line}" ]] && continue
    path="${line:3}"
    git add -- "${path}" 2>/dev/null || true
  done < <(git status --porcelain=v1 --untracked-files=no 2>/dev/null || true)

  if git diff --cached --quiet 2>/dev/null; then
    echo "→ nothing to finalize-commit"
    return 1
  fi
  git commit -m "chore(ci): finalize generated artifacts" || return 1
  return 0
}

sync_once() {
  diag_snapshot "worktree_before_sync"

  # Must be clean before fetch/rebase
  if ! verify_clean_tracked "before_fetch"; then
    echo "→ dirty before fetch — one automatic finalize commit"
    if auto_finalize_once; then
      if ! verify_clean_tracked "after_finalize"; then
        echo "git_safe_sync_push: still dirty after finalize — abort" >&2
        git status --porcelain=v1 >&2 || true
        return 1
      fi
    else
      echo "git_safe_sync_push: cannot finalize dirty tree — abort" >&2
      git status --porcelain=v1 >&2 || true
      return 1
    fi
  fi

  echo "→ fetch ${REMOTE}"
  git fetch "${REMOTE}" --prune
  diag_snapshot "worktree_after_fetch"

  # Fetch must not dirty the tree; if it did, surface filenames
  if ! verify_clean_tracked "after_fetch"; then
    echo "→ worktree became dirty during fetch — culprit files above"
    if auto_finalize_once && verify_clean_tracked "after_fetch_finalize"; then
      echo "→ recovered with finalize commit"
    else
      echo "git_safe_sync_push: dirty during fetch and cannot recover" >&2
      return 1
    fi
  fi

  if ! git rev-parse --verify "${REMOTE}/${BRANCH}" >/dev/null 2>&1; then
    echo "→ remote branch missing; will push new branch"
    REBASE_OK="YES"
    return 0
  fi

  diag_snapshot "worktree_before_rebase"
  echo "→ status before pull --rebase"
  git status || true

  if ! verify_clean_tracked "before_rebase"; then
    echo "git_safe_sync_push: dirty before rebase after recovery attempt" >&2
    return 1
  fi

  echo "→ pull --rebase ${REMOTE} ${BRANCH}"
  if git pull --rebase "${REMOTE}" "${BRANCH}"; then
    echo "→ rebase complete (or already up-to-date)"
    REBASE_OK="YES"
  else
    echo "git_safe_sync_push: rebase conflict — aborting rebase safely" >&2
    git rebase --abort 2>/dev/null || true
    REBASE_OK="NO"
    return 1
  fi

  if ! verify_clean_tracked "after_rebase"; then
    echo "→ dirty after rebase — one finalize attempt"
    if auto_finalize_once && verify_clean_tracked "after_rebase_finalize"; then
      :
    else
      echo "git_safe_sync_push: dirty after rebase" >&2
      git status --porcelain=v1 >&2 || true
      return 1
    fi
  fi

  return 0
}

ATTEMPT=1
while [[ "${ATTEMPT}" -le "${MAX_RETRIES}" ]]; do
  echo "git_safe_sync_push: attempt ${ATTEMPT}/${MAX_RETRIES}"
  if ! sync_once; then
    echo "git_safe_sync_push: sync failed on attempt ${ATTEMPT}" >&2
    ATTEMPT=$((ATTEMPT + 1))
    sleep $((ATTEMPT * 2))
    continue
  fi

  if git rev-parse --verify "${REMOTE}/${BRANCH}" >/dev/null 2>&1; then
    LOCAL=$(git rev-parse HEAD)
    REMOTE_SHA=$(git rev-parse "${REMOTE}/${BRANCH}")
    if [[ "${LOCAL}" == "${REMOTE_SHA}" ]]; then
      echo "git_safe_sync_push: already up-to-date with ${REMOTE}/${BRANCH}"
      PUSHED="NO"
      print_telemetry
      exit 0
    fi
  fi

  echo "→ push ${REMOTE} HEAD:${BRANCH}"
  if git push "${REMOTE}" "HEAD:${BRANCH}"; then
    echo "git_safe_sync_push: push ok"
    PUSHED="YES"
    print_telemetry
    exit 0
  fi

  echo "git_safe_sync_push: push rejected — will re-sync and retry" >&2
  RECOVERY_USED="YES"
  ATTEMPT=$((ATTEMPT + 1))
  sleep $((ATTEMPT * 2))
done

echo "git_safe_sync_push: FAILED after ${MAX_RETRIES} attempts (safe abort; local history preserved)" >&2
print_telemetry
exit 1
