# Candidate Root Cause

**Generated:** 2026-08-10T02:16:12+00:00
**Session:** `SESSION-20260810-C77E2C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001784`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-C77E2C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001784': 1, 'duplicate_id:SIG-001780': 1, 'duplicate_id:SIG-001782': 1, 'duplicate_id:SIG-001783': 1, 'duplicate_id:SIG-001781': 1}`
- `candidate CAND-FB9DC5413A53 entity_id=SIG-001784 reason=duplicate_id:SIG-001784 conf=0.92`
- `candidate CAND-CC707C44B95C entity_id=SIG-001780 reason=duplicate_id:SIG-001780 conf=0.9`
- `candidate CAND-A543CFE48318 entity_id=SIG-001782 reason=duplicate_id:SIG-001782 conf=0.88`
- `candidate CAND-CBE5037666F1 entity_id=SIG-001783 reason=duplicate_id:SIG-001783 conf=0.9`
- `candidate CAND-4AFD3D27AF5F entity_id=SIG-001781 reason=duplicate_id:SIG-001781 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FB9DC5413A53 | business_signal_library | 0.92 | False | duplicate_id:SIG-001784 | Rejected |
| CAND-CC707C44B95C | business_signal_library | 0.9 | False | duplicate_id:SIG-001780 | Rejected |
| CAND-A543CFE48318 | business_signal_library | 0.88 | False | duplicate_id:SIG-001782 | Rejected |
| CAND-CBE5037666F1 | business_signal_library | 0.9 | False | duplicate_id:SIG-001783 | Rejected |
| CAND-4AFD3D27AF5F | business_signal_library | 0.92 | False | duplicate_id:SIG-001781 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001784` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
