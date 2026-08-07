# Candidate Root Cause

**Generated:** 2026-08-07T11:12:47+00:00
**Session:** `SESSION-20260807-70EC88`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001504`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-70EC88`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001504': 1, 'duplicate_id:SIG-001500': 1, 'duplicate_id:SIG-001501': 1, 'duplicate_id:SIG-001503': 1, 'duplicate_id:SIG-001502': 1}`
- `candidate CAND-E89C58EE7794 entity_id=SIG-001504 reason=duplicate_id:SIG-001504 conf=0.92`
- `candidate CAND-854CA0CCBB5C entity_id=SIG-001500 reason=duplicate_id:SIG-001500 conf=0.9`
- `candidate CAND-ACBB4E4F8429 entity_id=SIG-001501 reason=duplicate_id:SIG-001501 conf=0.92`
- `candidate CAND-EA43C3495F7A entity_id=SIG-001503 reason=duplicate_id:SIG-001503 conf=0.9`
- `candidate CAND-3FBE76C31685 entity_id=SIG-001502 reason=duplicate_id:SIG-001502 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E89C58EE7794 | business_signal_library | 0.92 | False | duplicate_id:SIG-001504 | Rejected |
| CAND-854CA0CCBB5C | business_signal_library | 0.9 | False | duplicate_id:SIG-001500 | Rejected |
| CAND-ACBB4E4F8429 | business_signal_library | 0.92 | False | duplicate_id:SIG-001501 | Rejected |
| CAND-EA43C3495F7A | business_signal_library | 0.9 | False | duplicate_id:SIG-001503 | Rejected |
| CAND-3FBE76C31685 | business_signal_library | 0.88 | False | duplicate_id:SIG-001502 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001504` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
