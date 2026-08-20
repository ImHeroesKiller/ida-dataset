# Candidate Root Cause

**Generated:** 2026-08-20T04:56:52+00:00
**Session:** `SESSION-20260820-DE77AA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000750`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-DE77AA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000750': 1, 'duplicate_id:SIG-000746': 1, 'duplicate_id:SIG-000747': 1, 'duplicate_id:SIG-000748': 1, 'duplicate_id:SIG-000749': 1}`
- `candidate CAND-3D44533D05C8 entity_id=SIG-000750 reason=duplicate_id:SIG-000750 conf=0.9`
- `candidate CAND-F3538717BF79 entity_id=SIG-000746 reason=duplicate_id:SIG-000746 conf=0.92`
- `candidate CAND-4DE94EB1B61F entity_id=SIG-000747 reason=duplicate_id:SIG-000747 conf=0.9`
- `candidate CAND-650D73A4FC1A entity_id=SIG-000748 reason=duplicate_id:SIG-000748 conf=0.9`
- `candidate CAND-1139D3F1622D entity_id=SIG-000749 reason=duplicate_id:SIG-000749 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3D44533D05C8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000750 | Rejected |
| CAND-F3538717BF79 | business_signal_library | 0.92 | False | duplicate_id:SIG-000746 | Rejected |
| CAND-4DE94EB1B61F | business_signal_library | 0.9 | False | duplicate_id:SIG-000747 | Rejected |
| CAND-650D73A4FC1A | business_signal_library | 0.9 | False | duplicate_id:SIG-000748 | Rejected |
| CAND-1139D3F1622D | business_signal_library | 0.9 | False | duplicate_id:SIG-000749 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000750` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
