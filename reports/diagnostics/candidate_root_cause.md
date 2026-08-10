# Candidate Root Cause

**Generated:** 2026-08-10T13:29:54+00:00
**Session:** `SESSION-20260810-16A186`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001812`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-16A186`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001812': 1, 'duplicate_id:SIG-001810': 1, 'duplicate_id:SIG-001814': 1, 'duplicate_id:SIG-001813': 1, 'duplicate_id:SIG-001811': 1}`
- `candidate CAND-6FA61BBDC952 entity_id=SIG-001812 reason=duplicate_id:SIG-001812 conf=0.88`
- `candidate CAND-0AEB3ED5CC1E entity_id=SIG-001810 reason=duplicate_id:SIG-001810 conf=0.9`
- `candidate CAND-A4D0BB502530 entity_id=SIG-001814 reason=duplicate_id:SIG-001814 conf=0.92`
- `candidate CAND-6ED1C8EC42EA entity_id=SIG-001813 reason=duplicate_id:SIG-001813 conf=0.9`
- `candidate CAND-FA46B09444F0 entity_id=SIG-001811 reason=duplicate_id:SIG-001811 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6FA61BBDC952 | business_signal_library | 0.88 | False | duplicate_id:SIG-001812 | Rejected |
| CAND-0AEB3ED5CC1E | business_signal_library | 0.9 | False | duplicate_id:SIG-001810 | Rejected |
| CAND-A4D0BB502530 | business_signal_library | 0.92 | False | duplicate_id:SIG-001814 | Rejected |
| CAND-6ED1C8EC42EA | business_signal_library | 0.9 | False | duplicate_id:SIG-001813 | Rejected |
| CAND-FA46B09444F0 | business_signal_library | 0.92 | False | duplicate_id:SIG-001811 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001812` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
