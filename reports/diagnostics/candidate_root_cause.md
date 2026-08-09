# Candidate Root Cause

**Generated:** 2026-08-09T14:57:38+00:00
**Session:** `SESSION-20260809-CEA637`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001730`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-CEA637`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001730': 1, 'duplicate_id:SIG-001733': 1, 'duplicate_id:SIG-001732': 1, 'duplicate_id:SIG-001731': 1, 'duplicate_id:SIG-001734': 1}`
- `candidate CAND-A792EA59440A entity_id=SIG-001730 reason=duplicate_id:SIG-001730 conf=0.9`
- `candidate CAND-F024906BAAA1 entity_id=SIG-001733 reason=duplicate_id:SIG-001733 conf=0.9`
- `candidate CAND-2BED15DB2BB0 entity_id=SIG-001732 reason=duplicate_id:SIG-001732 conf=0.88`
- `candidate CAND-BCBF129A18DA entity_id=SIG-001731 reason=duplicate_id:SIG-001731 conf=0.92`
- `candidate CAND-33BE9465DDD9 entity_id=SIG-001734 reason=duplicate_id:SIG-001734 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A792EA59440A | business_signal_library | 0.9 | False | duplicate_id:SIG-001730 | Rejected |
| CAND-F024906BAAA1 | business_signal_library | 0.9 | False | duplicate_id:SIG-001733 | Rejected |
| CAND-2BED15DB2BB0 | business_signal_library | 0.88 | False | duplicate_id:SIG-001732 | Rejected |
| CAND-BCBF129A18DA | business_signal_library | 0.92 | False | duplicate_id:SIG-001731 | Rejected |
| CAND-33BE9465DDD9 | business_signal_library | 0.92 | False | duplicate_id:SIG-001734 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001730` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
