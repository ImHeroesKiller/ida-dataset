# Candidate Root Cause

**Generated:** 2026-08-10T05:59:37+00:00
**Session:** `SESSION-20260810-4D48AF`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001790`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-4D48AF`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001790': 1, 'duplicate_id:SIG-001791': 1, 'duplicate_id:SIG-001794': 1, 'duplicate_id:SIG-001792': 1, 'duplicate_id:SIG-001793': 1}`
- `candidate CAND-91A4A71643D6 entity_id=SIG-001790 reason=duplicate_id:SIG-001790 conf=0.9`
- `candidate CAND-FA719B0519B2 entity_id=SIG-001791 reason=duplicate_id:SIG-001791 conf=0.92`
- `candidate CAND-03AA8293C400 entity_id=SIG-001794 reason=duplicate_id:SIG-001794 conf=0.92`
- `candidate CAND-FCFE11F2E433 entity_id=SIG-001792 reason=duplicate_id:SIG-001792 conf=0.88`
- `candidate CAND-AAE1D34D1C8F entity_id=SIG-001793 reason=duplicate_id:SIG-001793 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-91A4A71643D6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001790 | Rejected |
| CAND-FA719B0519B2 | business_signal_library | 0.92 | False | duplicate_id:SIG-001791 | Rejected |
| CAND-03AA8293C400 | business_signal_library | 0.92 | False | duplicate_id:SIG-001794 | Rejected |
| CAND-FCFE11F2E433 | business_signal_library | 0.88 | False | duplicate_id:SIG-001792 | Rejected |
| CAND-AAE1D34D1C8F | business_signal_library | 0.9 | False | duplicate_id:SIG-001793 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001790` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
