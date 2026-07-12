# Candidate Root Cause

**Generated:** 2026-07-12T07:33:56+00:00
**Session:** `SESSION-20260712-37CE0D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `none`

**dry_run publisher gate:** `True`

## How many candidates?

- Total analyzed: **4**
- Integrity blocked: **0**
- Blocked by primary reason: **0**

## What evidence proves it?

- `session_id=SESSION-20260712-37CE0D`
- `dry_run=True`
- `candidates_analyzed=4`
- `integrity_blocked=0`
- `top_family=none count=0`
- `family_histogram={}`
- `reason_histogram={}`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A9BDDA0A288F | industry_library | 0.8375 | True | ok | Skipped |
| CAND-7032256FDB1F | industry_library | 0.92 | True | ok | Skipped |
| CAND-D898D6A1DF9D | industry_library | 0.92 | True | ok | Skipped |
| CAND-A4F2A2B3D784 | industry_library | 0.92 | True | ok | Skipped |

## Could production continue if that rule were satisfied?

If rule/condition `none` were satisfied for 0/4 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=True).

No recommendation is made. Statement is conditional evidence only.
