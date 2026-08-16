# Candidate Root Cause

**Generated:** 2026-08-16T20:35:32+00:00
**Session:** `SESSION-20260816-BE2107`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000374`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-BE2107`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000374': 1, 'duplicate_id:SIG-000373': 1, 'duplicate_id:SIG-000371': 1, 'duplicate_id:SIG-000375': 1, 'duplicate_id:SIG-000372': 1}`
- `candidate CAND-A0167FBC3D27 entity_id=SIG-000374 reason=duplicate_id:SIG-000374 conf=0.9`
- `candidate CAND-E6B8D79533AF entity_id=SIG-000373 reason=duplicate_id:SIG-000373 conf=0.9`
- `candidate CAND-789D8A0CD6DC entity_id=SIG-000371 reason=duplicate_id:SIG-000371 conf=0.92`
- `candidate CAND-5DEFB0C104DB entity_id=SIG-000375 reason=duplicate_id:SIG-000375 conf=0.9`
- `candidate CAND-D51A2630612C entity_id=SIG-000372 reason=duplicate_id:SIG-000372 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A0167FBC3D27 | business_signal_library | 0.9 | False | duplicate_id:SIG-000374 | Rejected |
| CAND-E6B8D79533AF | business_signal_library | 0.9 | False | duplicate_id:SIG-000373 | Rejected |
| CAND-789D8A0CD6DC | business_signal_library | 0.92 | False | duplicate_id:SIG-000371 | Rejected |
| CAND-5DEFB0C104DB | business_signal_library | 0.9 | False | duplicate_id:SIG-000375 | Rejected |
| CAND-D51A2630612C | business_signal_library | 0.9 | False | duplicate_id:SIG-000372 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000374` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
