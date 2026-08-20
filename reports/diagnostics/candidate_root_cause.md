# Candidate Root Cause

**Generated:** 2026-08-20T16:55:49+00:00
**Session:** `SESSION-20260820-ACDD2B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000806`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-ACDD2B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000806': 1, 'duplicate_id:SIG-000808': 1, 'duplicate_id:SIG-000807': 1, 'duplicate_id:SIG-000809': 1, 'duplicate_id:SIG-000810': 1}`
- `candidate CAND-C55582A0571A entity_id=SIG-000806 reason=duplicate_id:SIG-000806 conf=0.92`
- `candidate CAND-F51A5DAE5796 entity_id=SIG-000808 reason=duplicate_id:SIG-000808 conf=0.9`
- `candidate CAND-EEB792004EEC entity_id=SIG-000807 reason=duplicate_id:SIG-000807 conf=0.9`
- `candidate CAND-2FC80669F06E entity_id=SIG-000809 reason=duplicate_id:SIG-000809 conf=0.9`
- `candidate CAND-8AD584CC4F4C entity_id=SIG-000810 reason=duplicate_id:SIG-000810 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C55582A0571A | business_signal_library | 0.92 | False | duplicate_id:SIG-000806 | Rejected |
| CAND-F51A5DAE5796 | business_signal_library | 0.9 | False | duplicate_id:SIG-000808 | Rejected |
| CAND-EEB792004EEC | business_signal_library | 0.9 | False | duplicate_id:SIG-000807 | Rejected |
| CAND-2FC80669F06E | business_signal_library | 0.9 | False | duplicate_id:SIG-000809 | Rejected |
| CAND-8AD584CC4F4C | business_signal_library | 0.9 | False | duplicate_id:SIG-000810 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000806` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
