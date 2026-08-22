# Candidate Root Cause

**Generated:** 2026-08-22T07:51:07+00:00
**Session:** `SESSION-20260822-D28163`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000987`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-D28163`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000987': 1, 'duplicate_id:SIG-000990': 1, 'duplicate_id:SIG-000986': 1, 'duplicate_id:SIG-000989': 1, 'duplicate_id:SIG-000988': 1}`
- `candidate CAND-EF7870D41C0C entity_id=SIG-000987 reason=duplicate_id:SIG-000987 conf=0.9`
- `candidate CAND-8C6AEBAD4DDE entity_id=SIG-000990 reason=duplicate_id:SIG-000990 conf=0.9`
- `candidate CAND-73EA71E277F2 entity_id=SIG-000986 reason=duplicate_id:SIG-000986 conf=0.92`
- `candidate CAND-EF52A6EFD15E entity_id=SIG-000989 reason=duplicate_id:SIG-000989 conf=0.9`
- `candidate CAND-31AC56C78126 entity_id=SIG-000988 reason=duplicate_id:SIG-000988 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-EF7870D41C0C | business_signal_library | 0.9 | False | duplicate_id:SIG-000987 | Rejected |
| CAND-8C6AEBAD4DDE | business_signal_library | 0.9 | False | duplicate_id:SIG-000990 | Rejected |
| CAND-73EA71E277F2 | business_signal_library | 0.92 | False | duplicate_id:SIG-000986 | Rejected |
| CAND-EF52A6EFD15E | business_signal_library | 0.9 | False | duplicate_id:SIG-000989 | Rejected |
| CAND-31AC56C78126 | business_signal_library | 0.9 | False | duplicate_id:SIG-000988 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000987` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
