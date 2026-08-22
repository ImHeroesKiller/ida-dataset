# Candidate Root Cause

**Generated:** 2026-08-22T07:00:33+00:00
**Session:** `SESSION-20260822-BE1CC1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000981`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-BE1CC1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000981': 1, 'duplicate_id:SIG-000984': 1, 'duplicate_id:SIG-000983': 1, 'duplicate_id:SIG-000982': 1, 'duplicate_id:SIG-000985': 1}`
- `candidate CAND-2D884DBC439D entity_id=SIG-000981 reason=duplicate_id:SIG-000981 conf=0.92`
- `candidate CAND-D3AD38576331 entity_id=SIG-000984 reason=duplicate_id:SIG-000984 conf=0.9`
- `candidate CAND-EE0FEE5E74C0 entity_id=SIG-000983 reason=duplicate_id:SIG-000983 conf=0.9`
- `candidate CAND-A29F07F1A6BA entity_id=SIG-000982 reason=duplicate_id:SIG-000982 conf=0.9`
- `candidate CAND-BF16324E850F entity_id=SIG-000985 reason=duplicate_id:SIG-000985 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2D884DBC439D | business_signal_library | 0.92 | False | duplicate_id:SIG-000981 | Rejected |
| CAND-D3AD38576331 | business_signal_library | 0.9 | False | duplicate_id:SIG-000984 | Rejected |
| CAND-EE0FEE5E74C0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000983 | Rejected |
| CAND-A29F07F1A6BA | business_signal_library | 0.9 | False | duplicate_id:SIG-000982 | Rejected |
| CAND-BF16324E850F | business_signal_library | 0.9 | False | duplicate_id:SIG-000985 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000981` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
