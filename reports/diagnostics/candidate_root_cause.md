# Candidate Root Cause

**Generated:** 2026-08-16T15:37:45+00:00
**Session:** `SESSION-20260816-B453FD`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000350`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-B453FD`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000350': 1, 'duplicate_id:SIG-000349': 1, 'duplicate_id:SIG-000347': 1, 'duplicate_id:SIG-000348': 1, 'duplicate_id:SIG-000346': 1}`
- `candidate CAND-F0B92AD56FD4 entity_id=SIG-000350 reason=duplicate_id:SIG-000350 conf=0.9`
- `candidate CAND-D26E8A86AD7B entity_id=SIG-000349 reason=duplicate_id:SIG-000349 conf=0.9`
- `candidate CAND-D87723788918 entity_id=SIG-000347 reason=duplicate_id:SIG-000347 conf=0.9`
- `candidate CAND-C75B1E64798E entity_id=SIG-000348 reason=duplicate_id:SIG-000348 conf=0.9`
- `candidate CAND-A202C72EF376 entity_id=SIG-000346 reason=duplicate_id:SIG-000346 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F0B92AD56FD4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000350 | Rejected |
| CAND-D26E8A86AD7B | business_signal_library | 0.9 | False | duplicate_id:SIG-000349 | Rejected |
| CAND-D87723788918 | business_signal_library | 0.9 | False | duplicate_id:SIG-000347 | Rejected |
| CAND-C75B1E64798E | business_signal_library | 0.9 | False | duplicate_id:SIG-000348 | Rejected |
| CAND-A202C72EF376 | business_signal_library | 0.92 | False | duplicate_id:SIG-000346 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000350` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
