#!/usr/bin/env bash
# Vercel Ignored Build Step.
# Exit 0 = skip this deployment. Exit 1 = proceed with build.
#
# Learning sessions commit only automation/sessions + reports/learning.
# Redeploying the Next.js app for those commits rotates chunk hashes and
# causes intermittent ChunkLoadError / 404 for open browser tabs.
#
# Skip the build when the commit touches ONLY non-app knowledge artifacts.

set -euo pipefail

# Always build production promotions / force redeploys.
if [[ "${VERCEL_FORCE_NO_BUILD:-}" == "1" ]]; then
  echo "[vercel-ignore] force skip"
  exit 0
fi

# First deploy / missing git history → always build.
if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
  echo "[vercel-ignore] no HEAD — build"
  exit 1
fi

# Prefer previous successful deployment SHA when available.
PREV="${VERCEL_GIT_PREVIOUS_SHA:-}"
if [[ -z "$PREV" ]] || ! git cat-file -e "${PREV}^{commit}" 2>/dev/null; then
  if git rev-parse --verify HEAD^ >/dev/null 2>&1; then
    PREV="$(git rev-parse HEAD^)"
  else
    echo "[vercel-ignore] no previous commit — build"
    exit 1
  fi
fi

CHANGED="$(git diff --name-only "$PREV" HEAD 2>/dev/null || true)"
if [[ -z "$CHANGED" ]]; then
  echo "[vercel-ignore] empty diff — skip"
  exit 0
fi

# Paths that do NOT require a frontend redeploy.
# Everything else forces a build.
is_skip_only=1
while IFS= read -r file; do
  [[ -z "$file" ]] && continue
  case "$file" in
    automation/sessions/*|automation/sessions) ;;
    automation/learning/state/*|automation/learning/state) ;;
    automation/queue/*|automation/queue) ;;
    automation/review/*|automation/review) ;;
    automation/scheduler/state/*|automation/scheduler/state) ;;
    automation/missions/missions/*|automation/missions/history/*|automation/missions/contracts/*|automation/missions/attachments/*) ;;
    reports/learning/*|reports/learning|reports/publish/*|reports/review/*|reports/planner/*|reports/validation/*) ;;
    domains/*|domains) ;;
    relationships/*|relationships) ;;
    metadata/*|metadata) ;;
    exports/*|exports) ;;
    *.md|docs/*|docs|CHANGELOG.md|LICENSE|VERSION) ;;
    .github/workflows/*|.github/*) ;;
    *)
      is_skip_only=0
      echo "[vercel-ignore] app-relevant change: $file"
      ;;
  esac
done <<< "$CHANGED"

if [[ "$is_skip_only" -eq 1 ]]; then
  echo "[vercel-ignore] only knowledge/session artifacts changed — skip deploy"
  exit 0
fi

echo "[vercel-ignore] application or config changed — build"
exit 1
