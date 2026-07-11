# Candidate Root Cause

**Generated:** 2026-07-11T12:22:38+00:00
**Session:** `SESSION-20260711-B8F6DE`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `none`

**dry_run publisher gate:** `True`

## How many candidates?

- Total analyzed: **2**
- Integrity blocked: **0**
- Blocked by primary reason: **0**

## What evidence proves it?

- `session_id=SESSION-20260711-B8F6DE`
- `dry_run=True`
- `candidates_analyzed=2`
- `integrity_blocked=0`
- `top_family=none count=0`
- `family_histogram={}`
- `reason_histogram={}`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-AB39F9418E9D | industry_library | 0.92 | True | ok | Skipped |
| CAND-113BEDD08F27 | industry_library | 0.92 | True | ok | Skipped |

## Could production continue if that rule were satisfied?

If rule/condition `none` were satisfied for 0/2 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=True).

No recommendation is made. Statement is conditional evidence only.
