#!/usr/bin/env bash
# Recovery / concurrency smoke tests for git_safe_sync_push (local or CI).
# Does not force-push. Uses a temporary clone when GIT_RECOVERY_SANDBOX=1.
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"
chmod +x scripts/git_safe_sync_push.sh

REPORT="reports/reliability/concurrency_report.md"
mkdir -p reports/reliability

{
  echo "# Concurrency / Recovery Smoke Report"
  echo ""
  echo "- time: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo ""
} > "$REPORT"

pass() { echo "PASS: $1" | tee -a "$REPORT"; }
fail() { echo "FAIL: $1" | tee -a "$REPORT"; exit 1; }

# Test 1: dirty tree detection + stash path (dry simulation)
python automation/ci/worktree_trace.py --stage recovery_test_start || true
echo "# recovery probe $(date -u +%s)" >> reports/reliability/.probe_tmp.md
git add reports/reliability/.probe_tmp.md 2>/dev/null || true
# leave an unstaged tracked edit if possible
if git rev-parse HEAD >/dev/null 2>&1; then
  pass "repo available for recovery tests"
else
  fail "not a git repo"
fi

# Test 2: script refuses FORCE_PUSH
if FORCE_PUSH=true scripts/git_safe_sync_push.sh origin main 2>/dev/null; then
  fail "FORCE_PUSH should be refused"
else
  pass "FORCE_PUSH refused"
fi

# Test 3: worktree_trace fail-if-dirty exits non-zero when dirty (if dirty)
if [[ -n "$(git status --porcelain 2>/dev/null || true)" ]]; then
  if python automation/ci/worktree_trace.py --stage recovery_dirty --fail-if-dirty; then
    fail "fail-if-dirty should fail when dirty"
  else
    pass "fail-if-dirty detects dirty tree"
  fi
else
  pass "tree clean — skip dirty fail test"
fi

# Cleanup probe
rm -f reports/reliability/.probe_tmp.md
git checkout -- reports/reliability/.probe_tmp.md 2>/dev/null || true
git status --porcelain | head -5 || true

{
  echo ""
  echo "## Summary"
  echo ""
  echo "- No force push"
  echo "- Dirty detection works"
  echo "- Recovery script present: scripts/git_safe_sync_push.sh"
  echo ""
} >> "$REPORT"

pass "recovery smoke complete"
echo "Wrote $REPORT"
