# Candidate Root Cause

**Generated:** 2026-07-17T17:34:11+00:00
**Session:** `SESSION-20260717-AA6BB2`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000387`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260717-AA6BB2`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000387': 1, 'duplicate_id:SIG-000385': 1, 'duplicate_id:SIG-000386': 1, 'duplicate_id:SIG-000389': 1, 'duplicate_id:SIG-000388': 1}`
- `candidate CAND-EDC748B87239 entity_id=SIG-000387 reason=duplicate_id:SIG-000387 conf=0.88`
- `candidate CAND-9A012B9E46C4 entity_id=SIG-000385 reason=duplicate_id:SIG-000385 conf=0.9`
- `candidate CAND-2DEB20E9B147 entity_id=SIG-000386 reason=duplicate_id:SIG-000386 conf=0.92`
- `candidate CAND-4ADF466CED68 entity_id=SIG-000389 reason=duplicate_id:SIG-000389 conf=0.92`
- `candidate CAND-5F1E3DC05B02 entity_id=SIG-000388 reason=duplicate_id:SIG-000388 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-EDC748B87239 | business_signal_library | 0.88 | False | duplicate_id:SIG-000387 | Rejected |
| CAND-9A012B9E46C4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000385 | Rejected |
| CAND-2DEB20E9B147 | business_signal_library | 0.92 | False | duplicate_id:SIG-000386 | Rejected |
| CAND-4ADF466CED68 | business_signal_library | 0.92 | False | duplicate_id:SIG-000389 | Rejected |
| CAND-5F1E3DC05B02 | business_signal_library | 0.9 | False | duplicate_id:SIG-000388 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000387` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
