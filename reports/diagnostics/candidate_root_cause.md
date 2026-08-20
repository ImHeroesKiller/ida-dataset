# Candidate Root Cause

**Generated:** 2026-08-20T11:46:41+00:00
**Session:** `SESSION-20260820-AB30BD`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000785`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-AB30BD`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000785': 1, 'duplicate_id:SIG-000782': 1, 'duplicate_id:SIG-000784': 1, 'duplicate_id:SIG-000783': 1, 'duplicate_id:SIG-000781': 1}`
- `candidate CAND-2E522EC11AC8 entity_id=SIG-000785 reason=duplicate_id:SIG-000785 conf=0.9`
- `candidate CAND-130D4E2A69D6 entity_id=SIG-000782 reason=duplicate_id:SIG-000782 conf=0.9`
- `candidate CAND-7D6F7D76E2A8 entity_id=SIG-000784 reason=duplicate_id:SIG-000784 conf=0.9`
- `candidate CAND-4824D102E2C8 entity_id=SIG-000783 reason=duplicate_id:SIG-000783 conf=0.9`
- `candidate CAND-3A52788B8202 entity_id=SIG-000781 reason=duplicate_id:SIG-000781 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2E522EC11AC8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000785 | Rejected |
| CAND-130D4E2A69D6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000782 | Rejected |
| CAND-7D6F7D76E2A8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000784 | Rejected |
| CAND-4824D102E2C8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000783 | Rejected |
| CAND-3A52788B8202 | business_signal_library | 0.92 | False | duplicate_id:SIG-000781 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000785` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
