# Candidate Root Cause

**Generated:** 2026-07-11T18:55:52+00:00
**Session:** `SESSION-20260711-9942B1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `none`

**dry_run publisher gate:** `True`

## How many candidates?

- Total analyzed: **4**
- Integrity blocked: **0**
- Blocked by primary reason: **0**

## What evidence proves it?

- `session_id=SESSION-20260711-9942B1`
- `dry_run=True`
- `candidates_analyzed=4`
- `integrity_blocked=0`
- `top_family=none count=0`
- `family_histogram={}`
- `reason_histogram={}`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-AAC974FAABFD | industry_library | 0.8375 | True | ok | Skipped |
| CAND-AF5EE372F987 | industry_library | 0.92 | True | ok | Skipped |
| CAND-0273F818BCE5 | industry_library | 0.92 | True | ok | Skipped |
| CAND-C16E21791B67 | industry_library | 0.92 | True | ok | Skipped |

## Could production continue if that rule were satisfied?

If rule/condition `none` were satisfied for 0/4 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=True).

No recommendation is made. Statement is conditional evidence only.
