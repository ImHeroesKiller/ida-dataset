# Self-Healing Report

**Generated:** 2026-07-10T15:51:42.662478+00:00  
**Rule:** Document recovery only — no architecture redesign  

---

## Failure → recovery matrix

| Failure mode | Detected by | Recovery path today | Automatic? | Gap? |
|--------------|-------------|---------------------|------------|------|
| Workflow failure (step exit ≠0) | GHA job failure | Next cron/schedule re-runs; artifacts uploaded with `if: always()` | Partial | No auto-rerun beyond GHA retry UI |
| Temporary source outage | Connector errors / empty docs | Next session retries sources; throttle helpers | Yes (next session) | No multi-source failover orchestration beyond selector |
| Partial extraction failure | Validator / runtime | Failed candidates not published; session continues | Yes | — |
| Empty document set | live_runtime | Session completes without publish; journal notes | Yes | Rows=0 is success-ish — may mask starvation |
| Duplicate detection | Validator / dedupe | Reject duplicate; append skipped | Yes | — |
| Validation failure (conf/schema) | Validator / DPS gates | Reject; knowledge_rejected counters | Yes | — |
| Git push conflict | `git push` failure in learn/publish | **Manual** re-run / human rebase | **No** | **YES — missing automatic rebase/retry** |
| GitHub Actions retry | Platform | Re-run failed jobs manually or from UI | Partial | No workflow-level `strategy.fail-fast` custom retry loop |
| Interrupted production session | Runner cancel | Incomplete session file may remain; next schedule new session_id | Partial | No resume-mid-session checkpoint consumer |
| Publish blocked (no approved) | publish_ci exit 4 | Next day publish; learn may auto-approve path | Partial | Depends on review queue state |
| Branch protection blocking bot push | push rejected | Human adjust permissions / PAT | No | **Config dependency outside code** |

---

## What works well

1. **Append-only publisher** never overwrites history.  
2. **Confidence threshold 0.80** rejects bad rows.  
3. **Trusted source requirement** in policies.  
4. **Session isolation** via new SESSION ids.  
5. **Artifact upload always()** preserves forensics after failure.  
6. **Hourly schedule** naturally retries acquisition.

---

## Missing recovery paths (report only)

1. **Push non-fast-forward auto-heal** (fetch/rebase/retry).  
2. **Mid-session resume** after runner kill.  
3. **Export retry chain** after successful publish.  
4. **Starvation alert** when N consecutive sessions add 0 rows.  
5. **Concurrent learn serialization**.

These are **operational gaps**, not invitations to redesign the factory architecture.

---

## Verdict

Self-healing is **adequate for acquisition rejects and empty docs**, **inadequate for git contention**.  
Overnight risk concentrates on **repository write conflicts**, not schema corruption.
