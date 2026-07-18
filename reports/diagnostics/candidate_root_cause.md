# Candidate Root Cause

**Generated:** 2026-07-18T21:14:15+00:00
**Session:** `SESSION-20260718-DBD2FC`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000460`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260718-DBD2FC`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000460': 1, 'duplicate_id:SIG-000464': 1, 'duplicate_id:SIG-000463': 1, 'duplicate_id:SIG-000461': 1, 'duplicate_id:SIG-000462': 1}`
- `candidate CAND-77A8A95AA981 entity_id=SIG-000460 reason=duplicate_id:SIG-000460 conf=0.9`
- `candidate CAND-F875844848F8 entity_id=SIG-000464 reason=duplicate_id:SIG-000464 conf=0.92`
- `candidate CAND-62051F904511 entity_id=SIG-000463 reason=duplicate_id:SIG-000463 conf=0.9`
- `candidate CAND-085FE9DFF31D entity_id=SIG-000461 reason=duplicate_id:SIG-000461 conf=0.92`
- `candidate CAND-EA3D26E0A5D1 entity_id=SIG-000462 reason=duplicate_id:SIG-000462 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-77A8A95AA981 | business_signal_library | 0.9 | False | duplicate_id:SIG-000460 | Rejected |
| CAND-F875844848F8 | business_signal_library | 0.92 | False | duplicate_id:SIG-000464 | Rejected |
| CAND-62051F904511 | business_signal_library | 0.9 | False | duplicate_id:SIG-000463 | Rejected |
| CAND-085FE9DFF31D | business_signal_library | 0.92 | False | duplicate_id:SIG-000461 | Rejected |
| CAND-EA3D26E0A5D1 | business_signal_library | 0.88 | False | duplicate_id:SIG-000462 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000460` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
