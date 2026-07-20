# Candidate Root Cause

**Generated:** 2026-07-20T03:21:46+00:00
**Session:** `SESSION-20260720-E61DA3`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000546`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260720-E61DA3`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000546': 1, 'duplicate_id:SIG-000547': 1, 'duplicate_id:SIG-000548': 1, 'duplicate_id:SIG-000549': 1, 'duplicate_id:SIG-000545': 1}`
- `candidate CAND-7513975967DE entity_id=SIG-000546 reason=duplicate_id:SIG-000546 conf=0.92`
- `candidate CAND-3C0642AB6103 entity_id=SIG-000547 reason=duplicate_id:SIG-000547 conf=0.88`
- `candidate CAND-EEEF1E23AE67 entity_id=SIG-000548 reason=duplicate_id:SIG-000548 conf=0.9`
- `candidate CAND-B18B9B2F30B2 entity_id=SIG-000549 reason=duplicate_id:SIG-000549 conf=0.92`
- `candidate CAND-B5591DF1FC55 entity_id=SIG-000545 reason=duplicate_id:SIG-000545 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7513975967DE | business_signal_library | 0.92 | False | duplicate_id:SIG-000546 | Rejected |
| CAND-3C0642AB6103 | business_signal_library | 0.88 | False | duplicate_id:SIG-000547 | Rejected |
| CAND-EEEF1E23AE67 | business_signal_library | 0.9 | False | duplicate_id:SIG-000548 | Rejected |
| CAND-B18B9B2F30B2 | business_signal_library | 0.92 | False | duplicate_id:SIG-000549 | Rejected |
| CAND-B5591DF1FC55 | business_signal_library | 0.9 | False | duplicate_id:SIG-000545 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000546` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
