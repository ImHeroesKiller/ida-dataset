# Candidate Root Cause

**Generated:** 2026-07-21T03:51:41+00:00
**Session:** `SESSION-20260721-162842`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000602`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260721-162842`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000602': 1, 'duplicate_id:SIG-000600': 1, 'duplicate_id:SIG-000603': 1, 'duplicate_id:SIG-000601': 1, 'duplicate_id:SIG-000604': 1}`
- `candidate CAND-D6BF476AD258 entity_id=SIG-000602 reason=duplicate_id:SIG-000602 conf=0.88`
- `candidate CAND-25CE106451D7 entity_id=SIG-000600 reason=duplicate_id:SIG-000600 conf=0.9`
- `candidate CAND-3086D356D42B entity_id=SIG-000603 reason=duplicate_id:SIG-000603 conf=0.9`
- `candidate CAND-BBEBF5D8A30E entity_id=SIG-000601 reason=duplicate_id:SIG-000601 conf=0.92`
- `candidate CAND-A229EE3759AE entity_id=SIG-000604 reason=duplicate_id:SIG-000604 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D6BF476AD258 | business_signal_library | 0.88 | False | duplicate_id:SIG-000602 | Rejected |
| CAND-25CE106451D7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000600 | Rejected |
| CAND-3086D356D42B | business_signal_library | 0.9 | False | duplicate_id:SIG-000603 | Rejected |
| CAND-BBEBF5D8A30E | business_signal_library | 0.92 | False | duplicate_id:SIG-000601 | Rejected |
| CAND-A229EE3759AE | business_signal_library | 0.92 | False | duplicate_id:SIG-000604 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000602` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
