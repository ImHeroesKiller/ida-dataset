# Candidate Root Cause

**Generated:** 2026-08-05T09:01:42+00:00
**Session:** `SESSION-20260805-64B07B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001410`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260805-64B07B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001410': 1, 'duplicate_id:SIG-001413': 1, 'duplicate_id:SIG-001411': 1, 'duplicate_id:SIG-001414': 1, 'duplicate_id:SIG-001412': 1}`
- `candidate CAND-304EDF67B498 entity_id=SIG-001410 reason=duplicate_id:SIG-001410 conf=0.9`
- `candidate CAND-47CFCCB0A15E entity_id=SIG-001413 reason=duplicate_id:SIG-001413 conf=0.9`
- `candidate CAND-499A54B429D9 entity_id=SIG-001411 reason=duplicate_id:SIG-001411 conf=0.92`
- `candidate CAND-899AF713A46F entity_id=SIG-001414 reason=duplicate_id:SIG-001414 conf=0.92`
- `candidate CAND-E4B100CD5C21 entity_id=SIG-001412 reason=duplicate_id:SIG-001412 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-304EDF67B498 | business_signal_library | 0.9 | False | duplicate_id:SIG-001410 | Rejected |
| CAND-47CFCCB0A15E | business_signal_library | 0.9 | False | duplicate_id:SIG-001413 | Rejected |
| CAND-499A54B429D9 | business_signal_library | 0.92 | False | duplicate_id:SIG-001411 | Rejected |
| CAND-899AF713A46F | business_signal_library | 0.92 | False | duplicate_id:SIG-001414 | Rejected |
| CAND-E4B100CD5C21 | business_signal_library | 0.88 | False | duplicate_id:SIG-001412 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001410` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
