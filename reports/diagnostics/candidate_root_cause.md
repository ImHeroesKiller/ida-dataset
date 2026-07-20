# Candidate Root Cause

**Generated:** 2026-07-20T07:07:26+00:00
**Session:** `SESSION-20260720-058E82`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000559`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260720-058E82`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000559': 1, 'duplicate_id:SIG-000558': 1, 'duplicate_id:SIG-000556': 1, 'duplicate_id:SIG-000557': 1, 'duplicate_id:SIG-000555': 1}`
- `candidate CAND-5119FEE307DA entity_id=SIG-000559 reason=duplicate_id:SIG-000559 conf=0.92`
- `candidate CAND-10EA9B64F31F entity_id=SIG-000558 reason=duplicate_id:SIG-000558 conf=0.9`
- `candidate CAND-22ABAD21B6AF entity_id=SIG-000556 reason=duplicate_id:SIG-000556 conf=0.92`
- `candidate CAND-DCD063C2D2A6 entity_id=SIG-000557 reason=duplicate_id:SIG-000557 conf=0.88`
- `candidate CAND-F963A64EE8E6 entity_id=SIG-000555 reason=duplicate_id:SIG-000555 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5119FEE307DA | business_signal_library | 0.92 | False | duplicate_id:SIG-000559 | Rejected |
| CAND-10EA9B64F31F | business_signal_library | 0.9 | False | duplicate_id:SIG-000558 | Rejected |
| CAND-22ABAD21B6AF | business_signal_library | 0.92 | False | duplicate_id:SIG-000556 | Rejected |
| CAND-DCD063C2D2A6 | business_signal_library | 0.88 | False | duplicate_id:SIG-000557 | Rejected |
| CAND-F963A64EE8E6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000555 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000559` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
