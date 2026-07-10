# Workflow Audit — GitHub Actions

**Generated:** 2026-07-10T15:51:42.662478+00:00  
**Workflows present:** validate, learn, quality, publish, export  
**Not present:** planner.yml, review.yml (review covered by quality.yml)

---

## Inventory

### validate.yml

| Field | Value |
|-------|-------|
| Status | PASS with warnings |
| Triggers | push (main/staging/develop), pull_request, workflow_dispatch |
| Cron | none |
| Permissions | contents: read |
| Secrets | none required |
| Artifacts | validation-reports |
| Failure handling | exit codes 0-4 enforced; repo-health node job |
| Retry | GHA default (no custom) |

**Warnings:**
- dry_run defaults true on push — validation reports only
- fail_on_warning production config may fail on soft issues

### learn.yml

| Field | Value |
|-------|-------|
| Status | PASS with HIGH warnings |
| Triggers | schedule hourly + daily 06:00 UTC, workflow_dispatch |
| Cron | 0 * * * *; 0 6 * * * |
| Permissions | contents: write, actions: read |
| Secrets | GITHUB_TOKEN (implicit) |
| Artifacts | learning-session-* |
| Failure handling | exit code enforced after commit step (always() commit) |
| Retry | GHA default only; push no rebase retry |

**Warnings:**
- CRITICAL: git push without pull --rebase
- No concurrency group — overlapping hourlies possible
- Default mission Industry-centric
- Scheduled dry_run=false — real mutations on main
- Commits even if learn exit non-zero (always() && commit_session)

### quality.yml

| Field | Value |
|-------|-------|
| Status | PASS with warnings |
| Triggers | schedule daily 07:00 UTC, workflow_dispatch |
| Cron | 0 7 * * * |
| Permissions | contents: read |
| Secrets | none |
| Artifacts | review-reports |
| Failure handling | exit code enforced |
| Retry | GHA default |

**Warnings:**
- contents:read — cannot commit review into repo
- schedule dry_run defaults true on dispatch

### publish.yml

| Field | Value |
|-------|-------|
| Status | PASS with warnings |
| Triggers | schedule daily 08:00 UTC, workflow_dispatch |
| Cron | 0 8 * * * |
| Permissions | contents: write |
| Secrets | GITHUB_TOKEN |
| Artifacts | publish-reports |
| Failure handling | exit 0-4; publisher_blocked when no approved candidates |
| Retry | GHA default |

**Warnings:**
- review_required may block scheduled publish (exit 4)
- Scheduled forces dry_run=false commit+push
- Same push race risk if concurrent with learn

### export.yml

| Field | Value |
|-------|-------|
| Status | PASS for manual; GAP for autonomous export |
| Triggers | workflow_dispatch, workflow_call |
| Cron | none |
| Permissions | contents: write |
| Secrets | GITHUB_TOKEN |
| Artifacts | factory-exports |
| Failure handling | SystemExit if packager not ok |
| Retry | GHA default |

**Warnings:**
- NOT scheduled overnight
- defaults to industry_library export only in step


---

## Cross-cutting findings

| Topic | Assessment |
|-------|------------|
| Branch protection compatibility | production.yaml documents PR requirements; GHA bot pushes directly to main via contents:write — ensure repo settings allow Actions to push or workflows will fail push |
| Secrets | No custom API secrets required for baseline connectors; GITHUB_TOKEN only |
| Exit codes | validate/publish document 0–4; learn 0 success / 1 failure / 2 config |
| Artifacts | Uploaded with if-no-files-found: warn |
| Schedule timezone | UTC |
| Overnight chain | learn hourly → quality 07:00 → publish 08:00 (export not in chain) |

---

## Critical warnings (must acknowledge before unattended night)

1. **learn.yml push race** — no pull --rebase  
2. **No concurrency group** on learn  
3. **policies.review_required / publishing_enabled** may limit pipeline publish volume  
4. **export.yml not scheduled**  
5. **Default learn mission = Industry**, not Batch-009  

---

## Verdict

Workflows are **operational for continuous industry learning** with known push/conflict risk.  
They are **not fully certified** for unattended multi-writer, multi-batch factory production without mitigations above.
