# Candidate Root Cause

**Generated:** 2026-07-11T08:50:31+00:00
**Session:** `SESSION-20260711-6BC023`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000026`

**dry_run publisher gate:** `True`

## How many candidates?

- Total analyzed: **3**
- Integrity blocked: **3**
- Blocked by primary reason: **3**

## What evidence proves it?

- `session_id=SESSION-20260711-6BC023`
- `dry_run=True`
- `candidates_analyzed=3`
- `integrity_blocked=3`
- `top_family=duplicate_id count=3`
- `family_histogram={'duplicate_id': 3}`
- `reason_histogram={'duplicate_id:SIG-000026': 1, 'duplicate_id:SIG-000027': 1, 'duplicate_id:SIG-000025': 1}`
- `candidate CAND-F04B1DEAECD0 entity_id=SIG-000026 reason=duplicate_id:SIG-000026 conf=0.88`
- `candidate CAND-D03DE2F0A439 entity_id=SIG-000027 reason=duplicate_id:SIG-000027 conf=0.9`
- `candidate CAND-7528E4183942 entity_id=SIG-000025 reason=duplicate_id:SIG-000025 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F04B1DEAECD0 | business_signal_library | 0.88 | False | duplicate_id:SIG-000026 | Skipped |
| CAND-D03DE2F0A439 | business_signal_library | 0.9 | False | duplicate_id:SIG-000027 | Skipped |
| CAND-7528E4183942 | business_signal_library | 0.92 | False | duplicate_id:SIG-000025 | Skipped |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000026` were satisfied for 3/3 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=True).

No recommendation is made. Statement is conditional evidence only.
