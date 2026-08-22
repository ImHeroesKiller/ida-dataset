# Candidate Root Cause

**Generated:** 2026-08-22T12:59:31+00:00
**Session:** `SESSION-20260822-29B5DA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001013`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-29B5DA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001013': 1, 'duplicate_id:SIG-001015': 1, 'duplicate_id:SIG-001012': 1, 'duplicate_id:SIG-001011': 1, 'duplicate_id:SIG-001014': 1}`
- `candidate CAND-3E3845F7E2CF entity_id=SIG-001013 reason=duplicate_id:SIG-001013 conf=0.9`
- `candidate CAND-3318E44EA9E2 entity_id=SIG-001015 reason=duplicate_id:SIG-001015 conf=0.9`
- `candidate CAND-4F18069FDC78 entity_id=SIG-001012 reason=duplicate_id:SIG-001012 conf=0.9`
- `candidate CAND-6BEB42196619 entity_id=SIG-001011 reason=duplicate_id:SIG-001011 conf=0.92`
- `candidate CAND-A473153962A6 entity_id=SIG-001014 reason=duplicate_id:SIG-001014 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3E3845F7E2CF | business_signal_library | 0.9 | False | duplicate_id:SIG-001013 | Rejected |
| CAND-3318E44EA9E2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001015 | Rejected |
| CAND-4F18069FDC78 | business_signal_library | 0.9 | False | duplicate_id:SIG-001012 | Rejected |
| CAND-6BEB42196619 | business_signal_library | 0.92 | False | duplicate_id:SIG-001011 | Rejected |
| CAND-A473153962A6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001014 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001013` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
