# Candidate Root Cause

**Generated:** 2026-08-18T23:35:54+00:00
**Session:** `SESSION-20260818-BD91DA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000614`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-BD91DA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000614': 1, 'duplicate_id:SIG-000613': 1, 'duplicate_id:SIG-000612': 1, 'duplicate_id:SIG-000611': 1, 'duplicate_id:SIG-000615': 1}`
- `candidate CAND-31C85BAB2107 entity_id=SIG-000614 reason=duplicate_id:SIG-000614 conf=0.9`
- `candidate CAND-C603090421A7 entity_id=SIG-000613 reason=duplicate_id:SIG-000613 conf=0.9`
- `candidate CAND-86F16D2B60F4 entity_id=SIG-000612 reason=duplicate_id:SIG-000612 conf=0.9`
- `candidate CAND-DCB10809329B entity_id=SIG-000611 reason=duplicate_id:SIG-000611 conf=0.92`
- `candidate CAND-AFF8804ABEE0 entity_id=SIG-000615 reason=duplicate_id:SIG-000615 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-31C85BAB2107 | business_signal_library | 0.9 | False | duplicate_id:SIG-000614 | Rejected |
| CAND-C603090421A7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000613 | Rejected |
| CAND-86F16D2B60F4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000612 | Rejected |
| CAND-DCB10809329B | business_signal_library | 0.92 | False | duplicate_id:SIG-000611 | Rejected |
| CAND-AFF8804ABEE0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000615 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000614` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
