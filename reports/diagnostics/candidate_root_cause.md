# Candidate Root Cause

**Generated:** 2026-08-01T14:46:09+00:00
**Session:** `SESSION-20260801-8A43BC`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001213`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260801-8A43BC`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001213': 1, 'duplicate_id:SIG-001212': 1, 'duplicate_id:SIG-001214': 1, 'duplicate_id:SIG-001211': 1, 'duplicate_id:SIG-001210': 1}`
- `candidate CAND-9478F34581C7 entity_id=SIG-001213 reason=duplicate_id:SIG-001213 conf=0.9`
- `candidate CAND-D50A7FD7C37D entity_id=SIG-001212 reason=duplicate_id:SIG-001212 conf=0.88`
- `candidate CAND-0A575DF910FE entity_id=SIG-001214 reason=duplicate_id:SIG-001214 conf=0.92`
- `candidate CAND-5085550FE0EC entity_id=SIG-001211 reason=duplicate_id:SIG-001211 conf=0.92`
- `candidate CAND-F265D26BE90B entity_id=SIG-001210 reason=duplicate_id:SIG-001210 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-9478F34581C7 | business_signal_library | 0.9 | False | duplicate_id:SIG-001213 | Rejected |
| CAND-D50A7FD7C37D | business_signal_library | 0.88 | False | duplicate_id:SIG-001212 | Rejected |
| CAND-0A575DF910FE | business_signal_library | 0.92 | False | duplicate_id:SIG-001214 | Rejected |
| CAND-5085550FE0EC | business_signal_library | 0.92 | False | duplicate_id:SIG-001211 | Rejected |
| CAND-F265D26BE90B | business_signal_library | 0.9 | False | duplicate_id:SIG-001210 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001213` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
