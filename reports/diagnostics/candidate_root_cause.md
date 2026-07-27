# Candidate Root Cause

**Generated:** 2026-07-27T18:02:22+00:00
**Session:** `SESSION-20260727-42D654`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000960`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260727-42D654`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000960': 1, 'duplicate_id:SIG-000963': 1, 'duplicate_id:SIG-000961': 1, 'duplicate_id:SIG-000964': 1, 'duplicate_id:SIG-000962': 1}`
- `candidate CAND-440CFACCFA9D entity_id=SIG-000960 reason=duplicate_id:SIG-000960 conf=0.9`
- `candidate CAND-159BDD00BC69 entity_id=SIG-000963 reason=duplicate_id:SIG-000963 conf=0.9`
- `candidate CAND-9715855190F9 entity_id=SIG-000961 reason=duplicate_id:SIG-000961 conf=0.92`
- `candidate CAND-7C236670EB08 entity_id=SIG-000964 reason=duplicate_id:SIG-000964 conf=0.92`
- `candidate CAND-50191FC44EB7 entity_id=SIG-000962 reason=duplicate_id:SIG-000962 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-440CFACCFA9D | business_signal_library | 0.9 | False | duplicate_id:SIG-000960 | Rejected |
| CAND-159BDD00BC69 | business_signal_library | 0.9 | False | duplicate_id:SIG-000963 | Rejected |
| CAND-9715855190F9 | business_signal_library | 0.92 | False | duplicate_id:SIG-000961 | Rejected |
| CAND-7C236670EB08 | business_signal_library | 0.92 | False | duplicate_id:SIG-000964 | Rejected |
| CAND-50191FC44EB7 | business_signal_library | 0.88 | False | duplicate_id:SIG-000962 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000960` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
