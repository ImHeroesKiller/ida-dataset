# Candidate Root Cause

**Generated:** 2026-08-16T23:35:40+00:00
**Session:** `SESSION-20260816-E2A371`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000390`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-E2A371`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000390': 1, 'duplicate_id:SIG-000389': 1, 'duplicate_id:SIG-000388': 1, 'duplicate_id:SIG-000387': 1, 'duplicate_id:SIG-000386': 1}`
- `candidate CAND-4B0CC88468EC entity_id=SIG-000390 reason=duplicate_id:SIG-000390 conf=0.9`
- `candidate CAND-672F06BBEB83 entity_id=SIG-000389 reason=duplicate_id:SIG-000389 conf=0.9`
- `candidate CAND-27F24F21E84A entity_id=SIG-000388 reason=duplicate_id:SIG-000388 conf=0.9`
- `candidate CAND-4F1E2BD9A668 entity_id=SIG-000387 reason=duplicate_id:SIG-000387 conf=0.9`
- `candidate CAND-4C1E3A8EF762 entity_id=SIG-000386 reason=duplicate_id:SIG-000386 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4B0CC88468EC | business_signal_library | 0.9 | False | duplicate_id:SIG-000390 | Rejected |
| CAND-672F06BBEB83 | business_signal_library | 0.9 | False | duplicate_id:SIG-000389 | Rejected |
| CAND-27F24F21E84A | business_signal_library | 0.9 | False | duplicate_id:SIG-000388 | Rejected |
| CAND-4F1E2BD9A668 | business_signal_library | 0.9 | False | duplicate_id:SIG-000387 | Rejected |
| CAND-4C1E3A8EF762 | business_signal_library | 0.92 | False | duplicate_id:SIG-000386 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000390` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
