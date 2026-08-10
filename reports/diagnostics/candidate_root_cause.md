# Candidate Root Cause

**Generated:** 2026-08-10T22:56:54+00:00
**Session:** `SESSION-20260810-983065`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001850`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-983065`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001850': 1, 'duplicate_id:SIG-001851': 1, 'duplicate_id:SIG-001852': 1, 'duplicate_id:SIG-001853': 1, 'duplicate_id:SIG-001854': 1}`
- `candidate CAND-97FB15320376 entity_id=SIG-001850 reason=duplicate_id:SIG-001850 conf=0.9`
- `candidate CAND-905938FDF065 entity_id=SIG-001851 reason=duplicate_id:SIG-001851 conf=0.92`
- `candidate CAND-773BAEACC717 entity_id=SIG-001852 reason=duplicate_id:SIG-001852 conf=0.88`
- `candidate CAND-3AB1F02FFD84 entity_id=SIG-001853 reason=duplicate_id:SIG-001853 conf=0.9`
- `candidate CAND-6E947C0A971C entity_id=SIG-001854 reason=duplicate_id:SIG-001854 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-97FB15320376 | business_signal_library | 0.9 | False | duplicate_id:SIG-001850 | Rejected |
| CAND-905938FDF065 | business_signal_library | 0.92 | False | duplicate_id:SIG-001851 | Rejected |
| CAND-773BAEACC717 | business_signal_library | 0.88 | False | duplicate_id:SIG-001852 | Rejected |
| CAND-3AB1F02FFD84 | business_signal_library | 0.9 | False | duplicate_id:SIG-001853 | Rejected |
| CAND-6E947C0A971C | business_signal_library | 0.92 | False | duplicate_id:SIG-001854 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001850` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
