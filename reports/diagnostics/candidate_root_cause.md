# Candidate Root Cause

**Generated:** 2026-08-14T20:04:36+00:00
**Session:** `SESSION-20260814-DECB25`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000143`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-DECB25`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000143': 1, 'duplicate_id:SIG-000141': 1, 'duplicate_id:SIG-000144': 1, 'duplicate_id:SIG-000145': 1, 'duplicate_id:SIG-000142': 1}`
- `candidate CAND-46EE860AC4C1 entity_id=SIG-000143 reason=duplicate_id:SIG-000143 conf=0.9`
- `candidate CAND-30FEC094AB73 entity_id=SIG-000141 reason=duplicate_id:SIG-000141 conf=0.92`
- `candidate CAND-7E57A556A008 entity_id=SIG-000144 reason=duplicate_id:SIG-000144 conf=0.9`
- `candidate CAND-22831FAFAC35 entity_id=SIG-000145 reason=duplicate_id:SIG-000145 conf=0.9`
- `candidate CAND-C005EB46E1BA entity_id=SIG-000142 reason=duplicate_id:SIG-000142 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-46EE860AC4C1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000143 | Rejected |
| CAND-30FEC094AB73 | business_signal_library | 0.92 | False | duplicate_id:SIG-000141 | Rejected |
| CAND-7E57A556A008 | business_signal_library | 0.9 | False | duplicate_id:SIG-000144 | Rejected |
| CAND-22831FAFAC35 | business_signal_library | 0.9 | False | duplicate_id:SIG-000145 | Rejected |
| CAND-C005EB46E1BA | business_signal_library | 0.9 | False | duplicate_id:SIG-000142 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000143` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
