# Candidate Root Cause

**Generated:** 2026-08-19T10:49:40+00:00
**Session:** `SESSION-20260819-3D25B0`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000661`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-3D25B0`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000661': 1, 'duplicate_id:SIG-000665': 1, 'duplicate_id:SIG-000663': 1, 'duplicate_id:SIG-000662': 1, 'duplicate_id:SIG-000664': 1}`
- `candidate CAND-2A4E62723F14 entity_id=SIG-000661 reason=duplicate_id:SIG-000661 conf=0.92`
- `candidate CAND-6D5BC54620FA entity_id=SIG-000665 reason=duplicate_id:SIG-000665 conf=0.9`
- `candidate CAND-FE7974DB6155 entity_id=SIG-000663 reason=duplicate_id:SIG-000663 conf=0.9`
- `candidate CAND-0DF6BAEC3528 entity_id=SIG-000662 reason=duplicate_id:SIG-000662 conf=0.9`
- `candidate CAND-44F8730B4350 entity_id=SIG-000664 reason=duplicate_id:SIG-000664 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2A4E62723F14 | business_signal_library | 0.92 | False | duplicate_id:SIG-000661 | Rejected |
| CAND-6D5BC54620FA | business_signal_library | 0.9 | False | duplicate_id:SIG-000665 | Rejected |
| CAND-FE7974DB6155 | business_signal_library | 0.9 | False | duplicate_id:SIG-000663 | Rejected |
| CAND-0DF6BAEC3528 | business_signal_library | 0.9 | False | duplicate_id:SIG-000662 | Rejected |
| CAND-44F8730B4350 | business_signal_library | 0.9 | False | duplicate_id:SIG-000664 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000661` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
