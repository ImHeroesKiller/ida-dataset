#!/usr/bin/env bash
# Safe git synchronize + push for factory production workflows.
# Never force-push. Never overwrite remote history.
#
# Atomic production expects: all writers finished → single commit → clean tree → sync → push.
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
BRANCH="${2:-${GITHUB_REF_NAME:-$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo main)}}"
MAX_RETRIES="${GIT_SAFE_PUSH_RETRIES:-3}"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

RECOVERY_USED="NO"
REBASE_OK="NO"
PUSHED="NO"
STASHED="NO"
ATTEMPT=1
TRACE_DIR="reports/reliability"
mkdir -p "${TRACE_DIR}"
TRACE_MD="${TRACE_DIR}/git_worktree_trace.md"
PUSH_MD="${TRACE_DIR}/push_recovery_report.md"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "git_safe_sync_push: not a git repository" >&2
  exit 2
fi

if [[ ! -f "${TRACE_MD}" ]]; then
  cat > "${TRACE_MD}" <<'EOF'
# Git Working Tree Trace

Snapshots around git sync/push. Dirty trees after commit indicate post-commit writers.

EOF
fi

echo "git_safe_sync_push: remote=${REMOTE} branch=${BRANCH}"
git config --local push.default simple || true
git config --local pull.rebase true || true

if [[ "${FORCE_PUSH:-}" == "true" ]]; then
  echo "git_safe_sync_push: FORCE_PUSH refused by factory policy" >&2
  exit 1
fi

log_trace() {
  local stage="$1"
  {
    echo ""
    echo "## ${stage}"
    echo ""
    echo "- **time:** $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    if [[ -n "$(git status --porcelain 2>/dev/null || true)" ]]; then
      echo "- **dirty:** YES"
      echo ""
      echo '```'
      git status --porcelain || true
      echo '```'
    else
      echo "- **dirty:** NO (clean)"
    fi
    echo ""
  } >> "${TRACE_MD}"
}

print_telemetry() {
  local clean="YES"
  local dirty
  dirty="$(git status --porcelain 2>/dev/null || true)"
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
  cat > "${PUSH_MD}" <<EOF
# Push Recovery Report

- time: $(date -u +%Y-%m-%dT%H:%M:%SZ)
- pushed: ${PUSHED}
- rebase_ok: ${REBASE_OK}
- recovery_used: ${RECOVERY_USED}
- attempts: ${ATTEMPT}/${MAX_RETRIES}
- clean: ${clean}

EOF
}

verify_clean() {
  local label="$1"
  log_trace "verify_clean:${label}"
  local dirty
  dirty="$(git status --porcelain 2>/dev/null || true)"
  if [[ -n "${dirty}" ]]; then
    echo "DIRTY working tree (${label}):"
    echo "${dirty}"
    echo "Dirty files:"
    echo "${dirty}"
    return 1
  fi
  if ! git diff --exit-code >/dev/null 2>&1; then
    echo "DIRTY: unstaged diff present (${label})"
    git diff --stat || true
    return 1
  fi
  if ! git diff --cached --exit-code >/dev/null 2>&1; then
    echo "DIRTY: staged diff present (${label})"
    git diff --cached --stat || true
    return 1
  fi
  echo "CLEAN working tree (${label})"
  return 0
}

resolve_generated_conflicts() {
  local conflicts
  conflicts="$(git diff --name-only --diff-filter=U 2>/dev/null || true)"
  if [[ -z "${conflicts}" ]]; then
    return 0
  fi
  echo "→ resolving generated-file conflicts (prefer ours for reports/runtime state)"
  while IFS= read -r f; do
    [[ -z "${f}" ]] && continue
    case "${f}" in
      reports/*|automation/learning/state/*|automation/sessions/*|automation/connectors/cache/*)
        git checkout --ours -- "${f}" 2>/dev/null || true
        git add -- "${f}" 2>/dev/null || true
        echo "  resolved(ours): ${f}"
        ;;
      *)
        echo "  unresolvable non-generated conflict: ${f}" >&2
        return 1
        ;;
    esac
  done <<< "${conflicts}"
  return 0
}

sync_once() {
  log_trace "before_fetch"
  echo "→ fetch ${REMOTE}"
  git fetch "${REMOTE}" --prune

  if ! git rev-parse --verify "${REMOTE}/${BRANCH}" >/dev/null 2>&1; then
    echo "→ remote branch missing; will push new branch"
    REBASE_OK="YES"
    return 0
  fi

  log_trace "before_rebase"

  if ! verify_clean "pre_rebase"; then
    echo "→ working tree dirty — stashing (include untracked) for safe rebase"
    RECOVERY_USED="YES"
    STASHED="YES"
    git stash push --include-untracked -m "factory-safe-sync-$(date -u +%Y%m%dT%H%M%SZ)" || true
    log_trace "after_stash"
  fi

  echo "→ pull --rebase ${REMOTE} ${BRANCH}"
  if git pull --rebase "${REMOTE}" "${BRANCH}"; then
    echo "→ rebase complete (or already up-to-date)"
    REBASE_OK="YES"
  else
    echo "git_safe_sync_push: rebase conflict — aborting rebase safely" >&2
    git rebase --abort 2>/dev/null || true
    REBASE_OK="NO"
    if [[ "${STASHED}" == "YES" ]]; then
      git stash pop || true
      STASHED="NO"
    fi
    return 1
  fi

  if [[ "${STASHED}" == "YES" ]]; then
    echo "→ stash pop"
    set +e
    git stash pop
    pop_rc=$?
    set -e
    if [[ "${pop_rc}" -ne 0 ]]; then
      RECOVERY_USED="YES"
      if resolve_generated_conflicts; then
        git add -A reports/ automation/learning/state/ automation/sessions/ 2>/dev/null || true
        echo "→ stash pop conflicts resolved for generated paths"
      else
        echo "git_safe_sync_push: stash pop left unresolvable conflicts" >&2
        return 1
      fi
    fi
    STASHED="NO"
    log_trace "after_stash_pop"
  fi

  if ! verify_clean "post_rebase"; then
    echo "→ auto-staging residual factory artifacts"
    git add \
      reports/reliability/ \
      reports/learning/ \
      reports/production/ \
      reports/discovery/ \
      reports/performance/ \
      reports/manufacturing/ \
      reports/quality/ \
      automation/learning/state/ \
      automation/sessions/ \
      automation/queue/ \
      domains/ \
      2>/dev/null || true
    if ! git diff --cached --quiet 2>/dev/null; then
      git commit -m "chore(ci): capture residual factory artifacts after safe rebase" || true
      RECOVERY_USED="YES"
    fi
    if ! verify_clean "post_auto_commit"; then
      echo "→ residual dirt remains; stashing for push of local commits only"
      git stash push --include-untracked -m "factory-pre-push-residual" || true
      STASHED="YES"
      RECOVERY_USED="YES"
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
      if [[ "${STASHED}" == "YES" ]]; then
        git stash pop || true
        STASHED="NO"
      fi
      print_telemetry
      exit 0
    fi
  fi

  log_trace "before_push"
  if git push "${REMOTE}" "HEAD:${BRANCH}"; then
    echo "git_safe_sync_push: push ok"
    PUSHED="YES"
    if [[ "${STASHED}" == "YES" ]]; then
      git stash pop || true
      STASHED="NO"
    fi
    log_trace "after_push"
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
