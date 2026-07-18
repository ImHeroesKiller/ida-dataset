# Candidate Root Cause

**Generated:** 2026-07-18T13:39:22+00:00
**Session:** `SESSION-20260718-29377B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000438`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260718-29377B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000438': 1, 'duplicate_id:SIG-000435': 1, 'duplicate_id:SIG-000439': 1, 'duplicate_id:SIG-000437': 1, 'duplicate_id:SIG-000436': 1}`
- `candidate CAND-1EC3689B65BE entity_id=SIG-000438 reason=duplicate_id:SIG-000438 conf=0.9`
- `candidate CAND-30C8864AD342 entity_id=SIG-000435 reason=duplicate_id:SIG-000435 conf=0.9`
- `candidate CAND-E1304F6EE41E entity_id=SIG-000439 reason=duplicate_id:SIG-000439 conf=0.92`
- `candidate CAND-20210E3916D7 entity_id=SIG-000437 reason=duplicate_id:SIG-000437 conf=0.88`
- `candidate CAND-DFF82AD29449 entity_id=SIG-000436 reason=duplicate_id:SIG-000436 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-1EC3689B65BE | business_signal_library | 0.9 | False | duplicate_id:SIG-000438 | Rejected |
| CAND-30C8864AD342 | business_signal_library | 0.9 | False | duplicate_id:SIG-000435 | Rejected |
| CAND-E1304F6EE41E | business_signal_library | 0.92 | False | duplicate_id:SIG-000439 | Rejected |
| CAND-20210E3916D7 | business_signal_library | 0.88 | False | duplicate_id:SIG-000437 | Rejected |
| CAND-DFF82AD29449 | business_signal_library | 0.92 | False | duplicate_id:SIG-000436 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000438` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
