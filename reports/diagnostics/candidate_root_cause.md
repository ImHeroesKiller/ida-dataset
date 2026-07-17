# Candidate Root Cause

**Generated:** 2026-07-17T12:15:10+00:00
**Session:** `SESSION-20260717-907A03`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000371`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260717-907A03`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000371': 1, 'duplicate_id:SIG-000374': 1, 'duplicate_id:SIG-000370': 1, 'duplicate_id:SIG-000373': 1, 'duplicate_id:SIG-000372': 1}`
- `candidate CAND-9819CBD6F48B entity_id=SIG-000371 reason=duplicate_id:SIG-000371 conf=0.92`
- `candidate CAND-77B1F26BB6AE entity_id=SIG-000374 reason=duplicate_id:SIG-000374 conf=0.92`
- `candidate CAND-2BD7862F1812 entity_id=SIG-000370 reason=duplicate_id:SIG-000370 conf=0.9`
- `candidate CAND-E0AA2401D8DC entity_id=SIG-000373 reason=duplicate_id:SIG-000373 conf=0.9`
- `candidate CAND-AAA89471219C entity_id=SIG-000372 reason=duplicate_id:SIG-000372 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-9819CBD6F48B | business_signal_library | 0.92 | False | duplicate_id:SIG-000371 | Rejected |
| CAND-77B1F26BB6AE | business_signal_library | 0.92 | False | duplicate_id:SIG-000374 | Rejected |
| CAND-2BD7862F1812 | business_signal_library | 0.9 | False | duplicate_id:SIG-000370 | Rejected |
| CAND-E0AA2401D8DC | business_signal_library | 0.9 | False | duplicate_id:SIG-000373 | Rejected |
| CAND-AAA89471219C | business_signal_library | 0.88 | False | duplicate_id:SIG-000372 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000371` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
