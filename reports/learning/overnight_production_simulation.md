# Overnight Production Simulation (12 hours unattended)

**Generated:** 2026-07-10T15:51:42.662478+00:00  
**Window:** 12 consecutive hours (UTC)  
**Assumptions:** learn.yml hourly active; quality @07:00 and publish @08:00 fire if window includes them; no human pushes; default Industry mission  

---

## Estimated activity

| Metric | Low | Mid (expected) | High (optimistic) |
|--------|----:|---------------:|------------------:|
| Learning sessions | 10 | 12 | 13 |
| Rows added (all datasets) | 0 | 12 | 50 |
| Exports generated | 0 | 0 | 1–2 if manually chained |
| New reports (session/review/publish) | 10 | 14 | 18 |
| Git commits (`chore(learning)` etc.) | 0–3 | 8 | 12 |
| Storage growth | ~2 MB | ~6.2 MB | ~20–40 MB |
| External source HTTP calls | ~48 | ~96 | ~192 |
| GitHub Actions minutes | ~29 | ~58 | ~87 |

**Policy caps:** `max_rows_per_day: 200`, `max_updates_per_day: 50` (policies.yaml).  
**Publisher env cap:** `max_publish_rows: 200` (production.yaml).

---

## Expected coverage impact

At mid estimate (~12 rows), product coverage moves **marginally** (e.g. industry 50→~55 of 250).  
Overnight will **not** complete product targets — it sustains continuous acquisition.

---

## Bottlenecks & risks

| Risk | Likelihood | Impact | Notes |
|------|------------|--------|-------|
| Git push non-fast-forward | Medium | High | Concurrent learn or human push |
| Empty document set | High | Medium | Connectors often dry/thin → 0 rows, session still "ok" |
| Trusted source rate limits / downtime | Medium | Medium | BPS/WB/etc. timeouts → reject/skip |
| Duplicate detection | Medium | Low | Correct DPS behavior; reduces rows added |
| Validation / confidence reject | Medium | Low | conf &lt; 0.80 rejected |
| Merge conflicts on journal/state | Medium | Medium | learning_journal.jsonl hot file |
| Review wait / publish blocked | Medium | Medium | review_required + empty approved queue |
| GHA minutes quota | Low | High | Depends on org plan |
| Repository growth (sessions/reports) | High | Low | Expected; monitor |
| Orphan creation | Medium | Medium | If FKs weak on new rows |
| Rate limits on source sites | Medium | Medium | robots/throttle helpers exist |

---

## Safe execution intervals (recommendations)

| Setting | Current | Safer overnight |
|---------|---------|-----------------|
| Learn cron | Hourly | Keep hourly **or** every 2h if push races observed |
| Concurrency | None | `concurrency: learn` queue |
| Push | bare push | fetch + rebase + retry ×3 |
| Export | manual | Daily after publish 08:30 UTC (optional) |
| Mission | Industry default | Explicit dispatch if Batch-009 desired |

---

## Simulation conclusion

Unattended operation will likely produce **session artifacts + occasional knowledge rows**, not a full batch factory run.  
**Safe for continuous learning maintenance** if push-conflict risk accepted.  
**Not safe to assume** multi-batch coverage explosion or guaranteed export refresh.
