# Candidate Root Cause

**Generated:** 2026-08-20T19:52:00+00:00
**Session:** `SESSION-20260820-37B2EB`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000821`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-37B2EB`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000821': 1, 'duplicate_id:SIG-000824': 1, 'duplicate_id:SIG-000823': 1, 'duplicate_id:SIG-000825': 1, 'duplicate_id:SIG-000822': 1}`
- `candidate CAND-E9E509F8782A entity_id=SIG-000821 reason=duplicate_id:SIG-000821 conf=0.92`
- `candidate CAND-1AF770101A50 entity_id=SIG-000824 reason=duplicate_id:SIG-000824 conf=0.9`
- `candidate CAND-F315EA3BAFB3 entity_id=SIG-000823 reason=duplicate_id:SIG-000823 conf=0.9`
- `candidate CAND-2E51BF497BBC entity_id=SIG-000825 reason=duplicate_id:SIG-000825 conf=0.9`
- `candidate CAND-FC22B96D4B0B entity_id=SIG-000822 reason=duplicate_id:SIG-000822 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E9E509F8782A | business_signal_library | 0.92 | False | duplicate_id:SIG-000821 | Rejected |
| CAND-1AF770101A50 | business_signal_library | 0.9 | False | duplicate_id:SIG-000824 | Rejected |
| CAND-F315EA3BAFB3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000823 | Rejected |
| CAND-2E51BF497BBC | business_signal_library | 0.9 | False | duplicate_id:SIG-000825 | Rejected |
| CAND-FC22B96D4B0B | business_signal_library | 0.9 | False | duplicate_id:SIG-000822 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000821` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
