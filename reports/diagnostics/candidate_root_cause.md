# Candidate Root Cause

**Generated:** 2026-08-23T18:49:47+00:00
**Session:** `SESSION-20260823-23AAAB`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001151`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-23AAAB`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001151': 1, 'duplicate_id:SIG-001155': 1, 'duplicate_id:SIG-001153': 1, 'duplicate_id:SIG-001152': 1, 'duplicate_id:SIG-001154': 1}`
- `candidate CAND-B844179475B2 entity_id=SIG-001151 reason=duplicate_id:SIG-001151 conf=0.92`
- `candidate CAND-4F3C89A7430E entity_id=SIG-001155 reason=duplicate_id:SIG-001155 conf=0.9`
- `candidate CAND-EB53B5CC2DE2 entity_id=SIG-001153 reason=duplicate_id:SIG-001153 conf=0.9`
- `candidate CAND-68AF3FF6778A entity_id=SIG-001152 reason=duplicate_id:SIG-001152 conf=0.9`
- `candidate CAND-4B047DB0B171 entity_id=SIG-001154 reason=duplicate_id:SIG-001154 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B844179475B2 | business_signal_library | 0.92 | False | duplicate_id:SIG-001151 | Rejected |
| CAND-4F3C89A7430E | business_signal_library | 0.9 | False | duplicate_id:SIG-001155 | Rejected |
| CAND-EB53B5CC2DE2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001153 | Rejected |
| CAND-68AF3FF6778A | business_signal_library | 0.9 | False | duplicate_id:SIG-001152 | Rejected |
| CAND-4B047DB0B171 | business_signal_library | 0.9 | False | duplicate_id:SIG-001154 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001151` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
