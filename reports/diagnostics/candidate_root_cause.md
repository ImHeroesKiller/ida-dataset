# Candidate Root Cause

**Generated:** 2026-07-23T16:50:05+00:00
**Session:** `SESSION-20260723-56CA16`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000738`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260723-56CA16`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000738': 1, 'duplicate_id:SIG-000737': 1, 'duplicate_id:SIG-000739': 1, 'duplicate_id:SIG-000736': 1, 'duplicate_id:SIG-000735': 1}`
- `candidate CAND-4CBDBB10F335 entity_id=SIG-000738 reason=duplicate_id:SIG-000738 conf=0.9`
- `candidate CAND-1F5B7DB43814 entity_id=SIG-000737 reason=duplicate_id:SIG-000737 conf=0.88`
- `candidate CAND-E9D1CB39CC79 entity_id=SIG-000739 reason=duplicate_id:SIG-000739 conf=0.92`
- `candidate CAND-26025A91BD5F entity_id=SIG-000736 reason=duplicate_id:SIG-000736 conf=0.92`
- `candidate CAND-72F7F90FBCF2 entity_id=SIG-000735 reason=duplicate_id:SIG-000735 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4CBDBB10F335 | business_signal_library | 0.9 | False | duplicate_id:SIG-000738 | Rejected |
| CAND-1F5B7DB43814 | business_signal_library | 0.88 | False | duplicate_id:SIG-000737 | Rejected |
| CAND-E9D1CB39CC79 | business_signal_library | 0.92 | False | duplicate_id:SIG-000739 | Rejected |
| CAND-26025A91BD5F | business_signal_library | 0.92 | False | duplicate_id:SIG-000736 | Rejected |
| CAND-72F7F90FBCF2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000735 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000738` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
