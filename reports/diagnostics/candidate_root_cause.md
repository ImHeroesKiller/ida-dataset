# Candidate Root Cause

**Generated:** 2026-08-19T04:53:31+00:00
**Session:** `SESSION-20260819-7D4F4E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000632`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-7D4F4E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000632': 1, 'duplicate_id:SIG-000631': 1, 'duplicate_id:SIG-000634': 1, 'duplicate_id:SIG-000633': 1, 'duplicate_id:SIG-000635': 1}`
- `candidate CAND-6B23F4B80639 entity_id=SIG-000632 reason=duplicate_id:SIG-000632 conf=0.9`
- `candidate CAND-14FC812912B9 entity_id=SIG-000631 reason=duplicate_id:SIG-000631 conf=0.92`
- `candidate CAND-5764B652E14E entity_id=SIG-000634 reason=duplicate_id:SIG-000634 conf=0.9`
- `candidate CAND-6A0CF7DA3E2D entity_id=SIG-000633 reason=duplicate_id:SIG-000633 conf=0.9`
- `candidate CAND-F171D967E9BC entity_id=SIG-000635 reason=duplicate_id:SIG-000635 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6B23F4B80639 | business_signal_library | 0.9 | False | duplicate_id:SIG-000632 | Rejected |
| CAND-14FC812912B9 | business_signal_library | 0.92 | False | duplicate_id:SIG-000631 | Rejected |
| CAND-5764B652E14E | business_signal_library | 0.9 | False | duplicate_id:SIG-000634 | Rejected |
| CAND-6A0CF7DA3E2D | business_signal_library | 0.9 | False | duplicate_id:SIG-000633 | Rejected |
| CAND-F171D967E9BC | business_signal_library | 0.9 | False | duplicate_id:SIG-000635 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000632` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
