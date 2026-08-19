# Candidate Root Cause

**Generated:** 2026-08-19T18:56:57+00:00
**Session:** `SESSION-20260819-F0DFD8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000705`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-F0DFD8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000705': 1, 'duplicate_id:SIG-000703': 1, 'duplicate_id:SIG-000704': 1, 'duplicate_id:SIG-000702': 1, 'duplicate_id:SIG-000701': 1}`
- `candidate CAND-009A894CA81D entity_id=SIG-000705 reason=duplicate_id:SIG-000705 conf=0.9`
- `candidate CAND-4F9148B765B3 entity_id=SIG-000703 reason=duplicate_id:SIG-000703 conf=0.9`
- `candidate CAND-4DF006559A27 entity_id=SIG-000704 reason=duplicate_id:SIG-000704 conf=0.9`
- `candidate CAND-5C82D08E2536 entity_id=SIG-000702 reason=duplicate_id:SIG-000702 conf=0.9`
- `candidate CAND-4FA9B2EFED4B entity_id=SIG-000701 reason=duplicate_id:SIG-000701 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-009A894CA81D | business_signal_library | 0.9 | False | duplicate_id:SIG-000705 | Rejected |
| CAND-4F9148B765B3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000703 | Rejected |
| CAND-4DF006559A27 | business_signal_library | 0.9 | False | duplicate_id:SIG-000704 | Rejected |
| CAND-5C82D08E2536 | business_signal_library | 0.9 | False | duplicate_id:SIG-000702 | Rejected |
| CAND-4FA9B2EFED4B | business_signal_library | 0.92 | False | duplicate_id:SIG-000701 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000705` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
