# Candidate Root Cause

**Generated:** 2026-08-21T09:00:17+00:00
**Session:** `SESSION-20260821-D0722D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000877`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-D0722D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000877': 1, 'duplicate_id:SIG-000880': 1, 'duplicate_id:SIG-000876': 1, 'duplicate_id:SIG-000879': 1, 'duplicate_id:SIG-000878': 1}`
- `candidate CAND-545BA9784C1F entity_id=SIG-000877 reason=duplicate_id:SIG-000877 conf=0.9`
- `candidate CAND-B87DA823D5BF entity_id=SIG-000880 reason=duplicate_id:SIG-000880 conf=0.9`
- `candidate CAND-0218272BEE61 entity_id=SIG-000876 reason=duplicate_id:SIG-000876 conf=0.92`
- `candidate CAND-53EB1111D68F entity_id=SIG-000879 reason=duplicate_id:SIG-000879 conf=0.9`
- `candidate CAND-184991D4CF5C entity_id=SIG-000878 reason=duplicate_id:SIG-000878 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-545BA9784C1F | business_signal_library | 0.9 | False | duplicate_id:SIG-000877 | Rejected |
| CAND-B87DA823D5BF | business_signal_library | 0.9 | False | duplicate_id:SIG-000880 | Rejected |
| CAND-0218272BEE61 | business_signal_library | 0.92 | False | duplicate_id:SIG-000876 | Rejected |
| CAND-53EB1111D68F | business_signal_library | 0.9 | False | duplicate_id:SIG-000879 | Rejected |
| CAND-184991D4CF5C | business_signal_library | 0.9 | False | duplicate_id:SIG-000878 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000877` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
