# Candidate Root Cause

**Generated:** 2026-08-14T16:07:54+00:00
**Session:** `SESSION-20260814-9F677C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000125`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-9F677C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000125': 1, 'duplicate_id:SIG-000122': 1, 'duplicate_id:SIG-000123': 1, 'duplicate_id:SIG-000124': 1, 'duplicate_id:SIG-000121': 1}`
- `candidate CAND-8B32AE44A8EB entity_id=SIG-000125 reason=duplicate_id:SIG-000125 conf=0.9`
- `candidate CAND-0AB3E03DC966 entity_id=SIG-000122 reason=duplicate_id:SIG-000122 conf=0.9`
- `candidate CAND-55C4D984819F entity_id=SIG-000123 reason=duplicate_id:SIG-000123 conf=0.9`
- `candidate CAND-352EC65AC914 entity_id=SIG-000124 reason=duplicate_id:SIG-000124 conf=0.9`
- `candidate CAND-9833B5B4D891 entity_id=SIG-000121 reason=duplicate_id:SIG-000121 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-8B32AE44A8EB | business_signal_library | 0.9 | False | duplicate_id:SIG-000125 | Rejected |
| CAND-0AB3E03DC966 | business_signal_library | 0.9 | False | duplicate_id:SIG-000122 | Rejected |
| CAND-55C4D984819F | business_signal_library | 0.9 | False | duplicate_id:SIG-000123 | Rejected |
| CAND-352EC65AC914 | business_signal_library | 0.9 | False | duplicate_id:SIG-000124 | Rejected |
| CAND-9833B5B4D891 | business_signal_library | 0.92 | False | duplicate_id:SIG-000121 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000125` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
