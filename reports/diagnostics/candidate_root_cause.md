# Candidate Root Cause

**Generated:** 2026-08-11T19:33:04+00:00
**Session:** `SESSION-20260811-CF1167`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001916`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260811-CF1167`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001916': 1, 'duplicate_id:SIG-001919': 1, 'duplicate_id:SIG-001918': 1, 'duplicate_id:SIG-001915': 1, 'duplicate_id:SIG-001917': 1}`
- `candidate CAND-42901719CBF1 entity_id=SIG-001916 reason=duplicate_id:SIG-001916 conf=0.92`
- `candidate CAND-2F7A6E09A084 entity_id=SIG-001919 reason=duplicate_id:SIG-001919 conf=0.92`
- `candidate CAND-E43B43B61D97 entity_id=SIG-001918 reason=duplicate_id:SIG-001918 conf=0.9`
- `candidate CAND-60CCC94982C1 entity_id=SIG-001915 reason=duplicate_id:SIG-001915 conf=0.9`
- `candidate CAND-DD427B4D6675 entity_id=SIG-001917 reason=duplicate_id:SIG-001917 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-42901719CBF1 | business_signal_library | 0.92 | False | duplicate_id:SIG-001916 | Rejected |
| CAND-2F7A6E09A084 | business_signal_library | 0.92 | False | duplicate_id:SIG-001919 | Rejected |
| CAND-E43B43B61D97 | business_signal_library | 0.9 | False | duplicate_id:SIG-001918 | Rejected |
| CAND-60CCC94982C1 | business_signal_library | 0.9 | False | duplicate_id:SIG-001915 | Rejected |
| CAND-DD427B4D6675 | business_signal_library | 0.88 | False | duplicate_id:SIG-001917 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001916` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
