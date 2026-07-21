# Candidate Root Cause

**Generated:** 2026-07-21T06:49:04+00:00
**Session:** `SESSION-20260721-EB846A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000606`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260721-EB846A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000606': 1, 'duplicate_id:SIG-000609': 1, 'duplicate_id:SIG-000607': 1, 'duplicate_id:SIG-000608': 1, 'duplicate_id:SIG-000605': 1}`
- `candidate CAND-0CC170594F30 entity_id=SIG-000606 reason=duplicate_id:SIG-000606 conf=0.92`
- `candidate CAND-12B6F2A0931A entity_id=SIG-000609 reason=duplicate_id:SIG-000609 conf=0.92`
- `candidate CAND-FB7F5DA0FF08 entity_id=SIG-000607 reason=duplicate_id:SIG-000607 conf=0.88`
- `candidate CAND-AFA7B7079494 entity_id=SIG-000608 reason=duplicate_id:SIG-000608 conf=0.9`
- `candidate CAND-74A11C6688C8 entity_id=SIG-000605 reason=duplicate_id:SIG-000605 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0CC170594F30 | business_signal_library | 0.92 | False | duplicate_id:SIG-000606 | Rejected |
| CAND-12B6F2A0931A | business_signal_library | 0.92 | False | duplicate_id:SIG-000609 | Rejected |
| CAND-FB7F5DA0FF08 | business_signal_library | 0.88 | False | duplicate_id:SIG-000607 | Rejected |
| CAND-AFA7B7079494 | business_signal_library | 0.9 | False | duplicate_id:SIG-000608 | Rejected |
| CAND-74A11C6688C8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000605 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000606` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
