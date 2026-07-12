# Candidate Root Cause

**Generated:** 2026-07-12T03:54:29+00:00
**Session:** `SESSION-20260712-A029B2`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000078`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260712-A029B2`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000078': 1, 'duplicate_id:SIG-000079': 1, 'duplicate_id:SIG-000077': 1, 'duplicate_id:SIG-000076': 1, 'duplicate_id:SIG-000075': 1}`
- `candidate CAND-6BD41A4E502D entity_id=SIG-000078 reason=duplicate_id:SIG-000078 conf=0.9`
- `candidate CAND-78CD1E950F6A entity_id=SIG-000079 reason=duplicate_id:SIG-000079 conf=0.92`
- `candidate CAND-EE40F5FABF8B entity_id=SIG-000077 reason=duplicate_id:SIG-000077 conf=0.88`
- `candidate CAND-12A11252EC39 entity_id=SIG-000076 reason=duplicate_id:SIG-000076 conf=0.92`
- `candidate CAND-A9ADBE2D3028 entity_id=SIG-000075 reason=duplicate_id:SIG-000075 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6BD41A4E502D | business_signal_library | 0.9 | False | duplicate_id:SIG-000078 | Rejected |
| CAND-78CD1E950F6A | business_signal_library | 0.92 | False | duplicate_id:SIG-000079 | Rejected |
| CAND-EE40F5FABF8B | business_signal_library | 0.88 | False | duplicate_id:SIG-000077 | Rejected |
| CAND-12A11252EC39 | business_signal_library | 0.92 | False | duplicate_id:SIG-000076 | Rejected |
| CAND-A9ADBE2D3028 | business_signal_library | 0.9 | False | duplicate_id:SIG-000075 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000078` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
