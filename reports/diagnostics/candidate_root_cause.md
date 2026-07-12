# Candidate Root Cause

**Generated:** 2026-07-12T21:12:09+00:00
**Session:** `SESSION-20260712-486C14`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000123`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260712-486C14`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000123': 1, 'duplicate_id:SIG-000122': 1, 'duplicate_id:SIG-000124': 1, 'duplicate_id:SIG-000120': 1, 'duplicate_id:SIG-000121': 1}`
- `candidate CAND-D287F8CA1590 entity_id=SIG-000123 reason=duplicate_id:SIG-000123 conf=0.92`
- `candidate CAND-90A95C9CFC01 entity_id=SIG-000122 reason=duplicate_id:SIG-000122 conf=0.9`
- `candidate CAND-2D415744DAE8 entity_id=SIG-000124 reason=duplicate_id:SIG-000124 conf=0.85`
- `candidate CAND-A3843ADEFBA8 entity_id=SIG-000120 reason=duplicate_id:SIG-000120 conf=0.9`
- `candidate CAND-3954E52A3898 entity_id=SIG-000121 reason=duplicate_id:SIG-000121 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D287F8CA1590 | business_signal_library | 0.92 | False | duplicate_id:SIG-000123 | Rejected |
| CAND-90A95C9CFC01 | business_signal_library | 0.9 | False | duplicate_id:SIG-000122 | Rejected |
| CAND-2D415744DAE8 | business_signal_library | 0.85 | False | duplicate_id:SIG-000124 | Rejected |
| CAND-A3843ADEFBA8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000120 | Rejected |
| CAND-3954E52A3898 | business_signal_library | 0.92 | False | duplicate_id:SIG-000121 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000123` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
