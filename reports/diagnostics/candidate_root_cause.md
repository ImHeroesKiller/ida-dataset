# Candidate Root Cause

**Generated:** 2026-07-19T08:47:41+00:00
**Session:** `SESSION-20260719-0CF9E7`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000494`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260719-0CF9E7`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000494': 1, 'duplicate_id:SIG-000492': 1, 'duplicate_id:SIG-000493': 1, 'duplicate_id:SIG-000491': 1, 'duplicate_id:SIG-000490': 1}`
- `candidate CAND-EC6152B3AD42 entity_id=SIG-000494 reason=duplicate_id:SIG-000494 conf=0.92`
- `candidate CAND-3F19FC05333C entity_id=SIG-000492 reason=duplicate_id:SIG-000492 conf=0.88`
- `candidate CAND-73111C497C1C entity_id=SIG-000493 reason=duplicate_id:SIG-000493 conf=0.9`
- `candidate CAND-DCBED297C6A8 entity_id=SIG-000491 reason=duplicate_id:SIG-000491 conf=0.92`
- `candidate CAND-7E46922F9995 entity_id=SIG-000490 reason=duplicate_id:SIG-000490 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-EC6152B3AD42 | business_signal_library | 0.92 | False | duplicate_id:SIG-000494 | Rejected |
| CAND-3F19FC05333C | business_signal_library | 0.88 | False | duplicate_id:SIG-000492 | Rejected |
| CAND-73111C497C1C | business_signal_library | 0.9 | False | duplicate_id:SIG-000493 | Rejected |
| CAND-DCBED297C6A8 | business_signal_library | 0.92 | False | duplicate_id:SIG-000491 | Rejected |
| CAND-7E46922F9995 | business_signal_library | 0.9 | False | duplicate_id:SIG-000490 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000494` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
