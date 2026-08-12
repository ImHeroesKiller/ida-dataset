# Candidate Root Cause

**Generated:** 2026-08-12T18:18:22+00:00
**Session:** `SESSION-20260812-F6BB34`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001990`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260812-F6BB34`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001990': 1, 'duplicate_id:SIG-001994': 1, 'duplicate_id:SIG-001992': 1, 'duplicate_id:SIG-001991': 1, 'duplicate_id:SIG-001993': 1}`
- `candidate CAND-3A7B41C8BCA8 entity_id=SIG-001990 reason=duplicate_id:SIG-001990 conf=0.9`
- `candidate CAND-1F191025BB77 entity_id=SIG-001994 reason=duplicate_id:SIG-001994 conf=0.92`
- `candidate CAND-A6349870EBF5 entity_id=SIG-001992 reason=duplicate_id:SIG-001992 conf=0.88`
- `candidate CAND-D5180254D1FE entity_id=SIG-001991 reason=duplicate_id:SIG-001991 conf=0.92`
- `candidate CAND-150025835B2D entity_id=SIG-001993 reason=duplicate_id:SIG-001993 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3A7B41C8BCA8 | business_signal_library | 0.9 | False | duplicate_id:SIG-001990 | Rejected |
| CAND-1F191025BB77 | business_signal_library | 0.92 | False | duplicate_id:SIG-001994 | Rejected |
| CAND-A6349870EBF5 | business_signal_library | 0.88 | False | duplicate_id:SIG-001992 | Rejected |
| CAND-D5180254D1FE | business_signal_library | 0.92 | False | duplicate_id:SIG-001991 | Rejected |
| CAND-150025835B2D | business_signal_library | 0.9 | False | duplicate_id:SIG-001993 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001990` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
