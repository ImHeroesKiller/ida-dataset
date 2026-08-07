# Candidate Root Cause

**Generated:** 2026-08-07T00:59:35+00:00
**Session:** `SESSION-20260807-F274B6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001477`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-F274B6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001477': 1, 'duplicate_id:SIG-001478': 1, 'duplicate_id:SIG-001476': 1, 'duplicate_id:SIG-001475': 1, 'duplicate_id:SIG-001479': 1}`
- `candidate CAND-EF70DE0904BA entity_id=SIG-001477 reason=duplicate_id:SIG-001477 conf=0.88`
- `candidate CAND-729195FF90B9 entity_id=SIG-001478 reason=duplicate_id:SIG-001478 conf=0.9`
- `candidate CAND-17F90AE0F811 entity_id=SIG-001476 reason=duplicate_id:SIG-001476 conf=0.92`
- `candidate CAND-554111BC19A0 entity_id=SIG-001475 reason=duplicate_id:SIG-001475 conf=0.9`
- `candidate CAND-F3591862CE96 entity_id=SIG-001479 reason=duplicate_id:SIG-001479 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-EF70DE0904BA | business_signal_library | 0.88 | False | duplicate_id:SIG-001477 | Rejected |
| CAND-729195FF90B9 | business_signal_library | 0.9 | False | duplicate_id:SIG-001478 | Rejected |
| CAND-17F90AE0F811 | business_signal_library | 0.92 | False | duplicate_id:SIG-001476 | Rejected |
| CAND-554111BC19A0 | business_signal_library | 0.9 | False | duplicate_id:SIG-001475 | Rejected |
| CAND-F3591862CE96 | business_signal_library | 0.92 | False | duplicate_id:SIG-001479 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001477` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
