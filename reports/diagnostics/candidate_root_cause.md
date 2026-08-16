# Candidate Root Cause

**Generated:** 2026-08-16T01:38:24+00:00
**Session:** `SESSION-20260816-98B41A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000283`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-98B41A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000283': 1, 'duplicate_id:SIG-000285': 1, 'duplicate_id:SIG-000284': 1, 'duplicate_id:SIG-000281': 1, 'duplicate_id:SIG-000282': 1}`
- `candidate CAND-5C0B9D8D3787 entity_id=SIG-000283 reason=duplicate_id:SIG-000283 conf=0.9`
- `candidate CAND-76AD47CD240B entity_id=SIG-000285 reason=duplicate_id:SIG-000285 conf=0.9`
- `candidate CAND-05DB78FE030E entity_id=SIG-000284 reason=duplicate_id:SIG-000284 conf=0.9`
- `candidate CAND-1041BC8F363F entity_id=SIG-000281 reason=duplicate_id:SIG-000281 conf=0.92`
- `candidate CAND-50A094A611B6 entity_id=SIG-000282 reason=duplicate_id:SIG-000282 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5C0B9D8D3787 | business_signal_library | 0.9 | False | duplicate_id:SIG-000283 | Rejected |
| CAND-76AD47CD240B | business_signal_library | 0.9 | False | duplicate_id:SIG-000285 | Rejected |
| CAND-05DB78FE030E | business_signal_library | 0.9 | False | duplicate_id:SIG-000284 | Rejected |
| CAND-1041BC8F363F | business_signal_library | 0.92 | False | duplicate_id:SIG-000281 | Rejected |
| CAND-50A094A611B6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000282 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000283` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
