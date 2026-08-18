# Candidate Root Cause

**Generated:** 2026-08-18T03:10:36+00:00
**Session:** `SESSION-20260818-401D06`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000508`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-401D06`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000508': 1, 'duplicate_id:SIG-000507': 1, 'duplicate_id:SIG-000506': 1, 'duplicate_id:SIG-000510': 1, 'duplicate_id:SIG-000509': 1}`
- `candidate CAND-6B1721B83180 entity_id=SIG-000508 reason=duplicate_id:SIG-000508 conf=0.9`
- `candidate CAND-E4966DE7A084 entity_id=SIG-000507 reason=duplicate_id:SIG-000507 conf=0.9`
- `candidate CAND-F71392363979 entity_id=SIG-000506 reason=duplicate_id:SIG-000506 conf=0.92`
- `candidate CAND-6B1CA5ED03D1 entity_id=SIG-000510 reason=duplicate_id:SIG-000510 conf=0.9`
- `candidate CAND-52C47D2AFE23 entity_id=SIG-000509 reason=duplicate_id:SIG-000509 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6B1721B83180 | business_signal_library | 0.9 | False | duplicate_id:SIG-000508 | Rejected |
| CAND-E4966DE7A084 | business_signal_library | 0.9 | False | duplicate_id:SIG-000507 | Rejected |
| CAND-F71392363979 | business_signal_library | 0.92 | False | duplicate_id:SIG-000506 | Rejected |
| CAND-6B1CA5ED03D1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000510 | Rejected |
| CAND-52C47D2AFE23 | business_signal_library | 0.9 | False | duplicate_id:SIG-000509 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000508` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
