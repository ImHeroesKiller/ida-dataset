# Candidate Root Cause

**Generated:** 2026-08-03T13:57:42+00:00
**Session:** `SESSION-20260803-956D54`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001322`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260803-956D54`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001322': 1, 'duplicate_id:SIG-001324': 1, 'duplicate_id:SIG-001323': 1, 'duplicate_id:SIG-001321': 1, 'duplicate_id:SIG-001320': 1}`
- `candidate CAND-75ED9055DD93 entity_id=SIG-001322 reason=duplicate_id:SIG-001322 conf=0.88`
- `candidate CAND-ECC61854792D entity_id=SIG-001324 reason=duplicate_id:SIG-001324 conf=0.92`
- `candidate CAND-50208A20DE36 entity_id=SIG-001323 reason=duplicate_id:SIG-001323 conf=0.9`
- `candidate CAND-C90475C4A43F entity_id=SIG-001321 reason=duplicate_id:SIG-001321 conf=0.92`
- `candidate CAND-FF587B3E303F entity_id=SIG-001320 reason=duplicate_id:SIG-001320 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-75ED9055DD93 | business_signal_library | 0.88 | False | duplicate_id:SIG-001322 | Rejected |
| CAND-ECC61854792D | business_signal_library | 0.92 | False | duplicate_id:SIG-001324 | Rejected |
| CAND-50208A20DE36 | business_signal_library | 0.9 | False | duplicate_id:SIG-001323 | Rejected |
| CAND-C90475C4A43F | business_signal_library | 0.92 | False | duplicate_id:SIG-001321 | Rejected |
| CAND-FF587B3E303F | business_signal_library | 0.9 | False | duplicate_id:SIG-001320 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001322` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
