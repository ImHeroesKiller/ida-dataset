# Candidate Root Cause

**Generated:** 2026-08-22T19:41:42+00:00
**Session:** `SESSION-20260822-82B52E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001046`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-82B52E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001046': 1, 'duplicate_id:SIG-001047': 1, 'duplicate_id:SIG-001048': 1, 'duplicate_id:SIG-001050': 1, 'duplicate_id:SIG-001049': 1}`
- `candidate CAND-AE57B5C2A7C7 entity_id=SIG-001046 reason=duplicate_id:SIG-001046 conf=0.92`
- `candidate CAND-9D483E25900A entity_id=SIG-001047 reason=duplicate_id:SIG-001047 conf=0.9`
- `candidate CAND-A6F5C877C719 entity_id=SIG-001048 reason=duplicate_id:SIG-001048 conf=0.9`
- `candidate CAND-990541EDA925 entity_id=SIG-001050 reason=duplicate_id:SIG-001050 conf=0.9`
- `candidate CAND-6C6DE091236F entity_id=SIG-001049 reason=duplicate_id:SIG-001049 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-AE57B5C2A7C7 | business_signal_library | 0.92 | False | duplicate_id:SIG-001046 | Rejected |
| CAND-9D483E25900A | business_signal_library | 0.9 | False | duplicate_id:SIG-001047 | Rejected |
| CAND-A6F5C877C719 | business_signal_library | 0.9 | False | duplicate_id:SIG-001048 | Rejected |
| CAND-990541EDA925 | business_signal_library | 0.9 | False | duplicate_id:SIG-001050 | Rejected |
| CAND-6C6DE091236F | business_signal_library | 0.9 | False | duplicate_id:SIG-001049 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001046` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
