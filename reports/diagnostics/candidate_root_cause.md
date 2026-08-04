# Candidate Root Cause

**Generated:** 2026-08-04T00:25:34+00:00
**Session:** `SESSION-20260804-B5A0E3`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001349`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260804-B5A0E3`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001349': 1, 'duplicate_id:SIG-001347': 1, 'duplicate_id:SIG-001346': 1, 'duplicate_id:SIG-001345': 1, 'duplicate_id:SIG-001348': 1}`
- `candidate CAND-4ECB6AB85E95 entity_id=SIG-001349 reason=duplicate_id:SIG-001349 conf=0.92`
- `candidate CAND-B599C3EDCBD0 entity_id=SIG-001347 reason=duplicate_id:SIG-001347 conf=0.88`
- `candidate CAND-ACB5FB4C3B72 entity_id=SIG-001346 reason=duplicate_id:SIG-001346 conf=0.92`
- `candidate CAND-06C20DB8962F entity_id=SIG-001345 reason=duplicate_id:SIG-001345 conf=0.9`
- `candidate CAND-1CC4EFBF8AF4 entity_id=SIG-001348 reason=duplicate_id:SIG-001348 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4ECB6AB85E95 | business_signal_library | 0.92 | False | duplicate_id:SIG-001349 | Rejected |
| CAND-B599C3EDCBD0 | business_signal_library | 0.88 | False | duplicate_id:SIG-001347 | Rejected |
| CAND-ACB5FB4C3B72 | business_signal_library | 0.92 | False | duplicate_id:SIG-001346 | Rejected |
| CAND-06C20DB8962F | business_signal_library | 0.9 | False | duplicate_id:SIG-001345 | Rejected |
| CAND-1CC4EFBF8AF4 | business_signal_library | 0.9 | False | duplicate_id:SIG-001348 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001349` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
