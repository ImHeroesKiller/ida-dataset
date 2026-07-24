# Candidate Root Cause

**Generated:** 2026-07-24T22:23:55+00:00
**Session:** `SESSION-20260724-CFF217`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000808`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260724-CFF217`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000808': 1, 'duplicate_id:SIG-000805': 1, 'duplicate_id:SIG-000807': 1, 'duplicate_id:SIG-000806': 1, 'duplicate_id:SIG-000809': 1}`
- `candidate CAND-AA25D67E5DC3 entity_id=SIG-000808 reason=duplicate_id:SIG-000808 conf=0.9`
- `candidate CAND-0365D8BD6EF6 entity_id=SIG-000805 reason=duplicate_id:SIG-000805 conf=0.9`
- `candidate CAND-EFB588E85D05 entity_id=SIG-000807 reason=duplicate_id:SIG-000807 conf=0.88`
- `candidate CAND-5383DBC8CC1C entity_id=SIG-000806 reason=duplicate_id:SIG-000806 conf=0.92`
- `candidate CAND-E00CAA810DCB entity_id=SIG-000809 reason=duplicate_id:SIG-000809 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-AA25D67E5DC3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000808 | Rejected |
| CAND-0365D8BD6EF6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000805 | Rejected |
| CAND-EFB588E85D05 | business_signal_library | 0.88 | False | duplicate_id:SIG-000807 | Rejected |
| CAND-5383DBC8CC1C | business_signal_library | 0.92 | False | duplicate_id:SIG-000806 | Rejected |
| CAND-E00CAA810DCB | business_signal_library | 0.92 | False | duplicate_id:SIG-000809 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000808` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
