# Candidate Root Cause

**Generated:** 2026-08-06T08:53:18+00:00
**Session:** `SESSION-20260806-4551A6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001460`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260806-4551A6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001460': 1, 'duplicate_id:SIG-001463': 1, 'duplicate_id:SIG-001462': 1, 'duplicate_id:SIG-001464': 1, 'duplicate_id:SIG-001461': 1}`
- `candidate CAND-0B8ED759F449 entity_id=SIG-001460 reason=duplicate_id:SIG-001460 conf=0.9`
- `candidate CAND-EABF9CF3BFDA entity_id=SIG-001463 reason=duplicate_id:SIG-001463 conf=0.9`
- `candidate CAND-59D1FD64A043 entity_id=SIG-001462 reason=duplicate_id:SIG-001462 conf=0.88`
- `candidate CAND-DB3D24883E84 entity_id=SIG-001464 reason=duplicate_id:SIG-001464 conf=0.92`
- `candidate CAND-569C475F1CF7 entity_id=SIG-001461 reason=duplicate_id:SIG-001461 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0B8ED759F449 | business_signal_library | 0.9 | False | duplicate_id:SIG-001460 | Rejected |
| CAND-EABF9CF3BFDA | business_signal_library | 0.9 | False | duplicate_id:SIG-001463 | Rejected |
| CAND-59D1FD64A043 | business_signal_library | 0.88 | False | duplicate_id:SIG-001462 | Rejected |
| CAND-DB3D24883E84 | business_signal_library | 0.92 | False | duplicate_id:SIG-001464 | Rejected |
| CAND-569C475F1CF7 | business_signal_library | 0.92 | False | duplicate_id:SIG-001461 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001460` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
