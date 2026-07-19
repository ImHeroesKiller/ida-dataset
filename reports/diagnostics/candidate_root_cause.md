# Candidate Root Cause

**Generated:** 2026-07-19T06:16:10+00:00
**Session:** `SESSION-20260719-593A11`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000488`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260719-593A11`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000488': 1, 'duplicate_id:SIG-000485': 1, 'duplicate_id:SIG-000486': 1, 'duplicate_id:SIG-000489': 1, 'duplicate_id:SIG-000487': 1}`
- `candidate CAND-B564E2825394 entity_id=SIG-000488 reason=duplicate_id:SIG-000488 conf=0.9`
- `candidate CAND-E74A354F8DAC entity_id=SIG-000485 reason=duplicate_id:SIG-000485 conf=0.9`
- `candidate CAND-DD72282F42F1 entity_id=SIG-000486 reason=duplicate_id:SIG-000486 conf=0.92`
- `candidate CAND-687D00C3C11E entity_id=SIG-000489 reason=duplicate_id:SIG-000489 conf=0.92`
- `candidate CAND-5001D8D1FE75 entity_id=SIG-000487 reason=duplicate_id:SIG-000487 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B564E2825394 | business_signal_library | 0.9 | False | duplicate_id:SIG-000488 | Rejected |
| CAND-E74A354F8DAC | business_signal_library | 0.9 | False | duplicate_id:SIG-000485 | Rejected |
| CAND-DD72282F42F1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000486 | Rejected |
| CAND-687D00C3C11E | business_signal_library | 0.92 | False | duplicate_id:SIG-000489 | Rejected |
| CAND-5001D8D1FE75 | business_signal_library | 0.88 | False | duplicate_id:SIG-000487 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000488` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
