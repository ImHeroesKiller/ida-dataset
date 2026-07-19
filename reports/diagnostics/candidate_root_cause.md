# Candidate Root Cause

**Generated:** 2026-07-19T12:24:52+00:00
**Session:** `SESSION-20260719-3651B8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000501`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260719-3651B8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000501': 1, 'duplicate_id:SIG-000502': 1, 'duplicate_id:SIG-000504': 1, 'duplicate_id:SIG-000503': 1, 'duplicate_id:SIG-000500': 1}`
- `candidate CAND-01C9C499D6D3 entity_id=SIG-000501 reason=duplicate_id:SIG-000501 conf=0.92`
- `candidate CAND-8B79E9842DCC entity_id=SIG-000502 reason=duplicate_id:SIG-000502 conf=0.88`
- `candidate CAND-EA5E12A62BCE entity_id=SIG-000504 reason=duplicate_id:SIG-000504 conf=0.92`
- `candidate CAND-701F428EFC2D entity_id=SIG-000503 reason=duplicate_id:SIG-000503 conf=0.9`
- `candidate CAND-D01E210BF501 entity_id=SIG-000500 reason=duplicate_id:SIG-000500 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-01C9C499D6D3 | business_signal_library | 0.92 | False | duplicate_id:SIG-000501 | Rejected |
| CAND-8B79E9842DCC | business_signal_library | 0.88 | False | duplicate_id:SIG-000502 | Rejected |
| CAND-EA5E12A62BCE | business_signal_library | 0.92 | False | duplicate_id:SIG-000504 | Rejected |
| CAND-701F428EFC2D | business_signal_library | 0.9 | False | duplicate_id:SIG-000503 | Rejected |
| CAND-D01E210BF501 | business_signal_library | 0.9 | False | duplicate_id:SIG-000500 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000501` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
