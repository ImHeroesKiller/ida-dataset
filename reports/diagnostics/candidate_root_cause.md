# Candidate Root Cause

**Generated:** 2026-08-08T15:50:07+00:00
**Session:** `SESSION-20260808-B626D9`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001632`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-B626D9`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001632': 1, 'duplicate_id:SIG-001631': 1, 'duplicate_id:SIG-001630': 1, 'duplicate_id:SIG-001633': 1, 'duplicate_id:SIG-001634': 1}`
- `candidate CAND-6AECE3D3686B entity_id=SIG-001632 reason=duplicate_id:SIG-001632 conf=0.9`
- `candidate CAND-B623A3644BA3 entity_id=SIG-001631 reason=duplicate_id:SIG-001631 conf=0.92`
- `candidate CAND-A88774C2D0CD entity_id=SIG-001630 reason=duplicate_id:SIG-001630 conf=0.9`
- `candidate CAND-B5AC4EEBB0A9 entity_id=SIG-001633 reason=duplicate_id:SIG-001633 conf=0.92`
- `candidate CAND-1DBCD08404B4 entity_id=SIG-001634 reason=duplicate_id:SIG-001634 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6AECE3D3686B | business_signal_library | 0.9 | False | duplicate_id:SIG-001632 | Rejected |
| CAND-B623A3644BA3 | business_signal_library | 0.92 | False | duplicate_id:SIG-001631 | Rejected |
| CAND-A88774C2D0CD | business_signal_library | 0.9 | False | duplicate_id:SIG-001630 | Rejected |
| CAND-B5AC4EEBB0A9 | business_signal_library | 0.92 | False | duplicate_id:SIG-001633 | Rejected |
| CAND-1DBCD08404B4 | business_signal_library | 0.9 | False | duplicate_id:SIG-001634 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001632` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
