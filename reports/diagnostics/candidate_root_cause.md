# Candidate Root Cause

**Generated:** 2026-07-24T17:08:06+00:00
**Session:** `SESSION-20260724-3FA9F8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000794`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260724-3FA9F8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000794': 1, 'duplicate_id:SIG-000792': 1, 'duplicate_id:SIG-000791': 1, 'duplicate_id:SIG-000793': 1, 'duplicate_id:SIG-000790': 1}`
- `candidate CAND-22F09775A3D5 entity_id=SIG-000794 reason=duplicate_id:SIG-000794 conf=0.92`
- `candidate CAND-0E8D50B8E517 entity_id=SIG-000792 reason=duplicate_id:SIG-000792 conf=0.88`
- `candidate CAND-01602D8ADD0A entity_id=SIG-000791 reason=duplicate_id:SIG-000791 conf=0.92`
- `candidate CAND-5BBCE3A5C6A4 entity_id=SIG-000793 reason=duplicate_id:SIG-000793 conf=0.9`
- `candidate CAND-AABD1FF0AE76 entity_id=SIG-000790 reason=duplicate_id:SIG-000790 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-22F09775A3D5 | business_signal_library | 0.92 | False | duplicate_id:SIG-000794 | Rejected |
| CAND-0E8D50B8E517 | business_signal_library | 0.88 | False | duplicate_id:SIG-000792 | Rejected |
| CAND-01602D8ADD0A | business_signal_library | 0.92 | False | duplicate_id:SIG-000791 | Rejected |
| CAND-5BBCE3A5C6A4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000793 | Rejected |
| CAND-AABD1FF0AE76 | business_signal_library | 0.9 | False | duplicate_id:SIG-000790 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000794` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
