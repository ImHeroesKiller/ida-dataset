# Candidate Root Cause

**Generated:** 2026-08-10T23:54:18+00:00
**Session:** `SESSION-20260810-991354`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001859`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-991354`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001859': 1, 'duplicate_id:SIG-001857': 1, 'duplicate_id:SIG-001856': 1, 'duplicate_id:SIG-001855': 1, 'duplicate_id:SIG-001858': 1}`
- `candidate CAND-9A784BF09801 entity_id=SIG-001859 reason=duplicate_id:SIG-001859 conf=0.9`
- `candidate CAND-C53B60D042E2 entity_id=SIG-001857 reason=duplicate_id:SIG-001857 conf=0.9`
- `candidate CAND-B84A819E5B83 entity_id=SIG-001856 reason=duplicate_id:SIG-001856 conf=0.92`
- `candidate CAND-3CBCB1B1103F entity_id=SIG-001855 reason=duplicate_id:SIG-001855 conf=0.9`
- `candidate CAND-CD3814078EB2 entity_id=SIG-001858 reason=duplicate_id:SIG-001858 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-9A784BF09801 | business_signal_library | 0.9 | False | duplicate_id:SIG-001859 | Rejected |
| CAND-C53B60D042E2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001857 | Rejected |
| CAND-B84A819E5B83 | business_signal_library | 0.92 | False | duplicate_id:SIG-001856 | Rejected |
| CAND-3CBCB1B1103F | business_signal_library | 0.9 | False | duplicate_id:SIG-001855 | Rejected |
| CAND-CD3814078EB2 | business_signal_library | 0.92 | False | duplicate_id:SIG-001858 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001859` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
