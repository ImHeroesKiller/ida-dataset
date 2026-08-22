# Candidate Root Cause

**Generated:** 2026-08-22T22:41:43+00:00
**Session:** `SESSION-20260822-560A8F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001064`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-560A8F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001064': 1, 'duplicate_id:SIG-001063': 1, 'duplicate_id:SIG-001065': 1, 'duplicate_id:SIG-001062': 1, 'duplicate_id:SIG-001061': 1}`
- `candidate CAND-5B666465B337 entity_id=SIG-001064 reason=duplicate_id:SIG-001064 conf=0.9`
- `candidate CAND-47083254B265 entity_id=SIG-001063 reason=duplicate_id:SIG-001063 conf=0.9`
- `candidate CAND-4775A1046F79 entity_id=SIG-001065 reason=duplicate_id:SIG-001065 conf=0.9`
- `candidate CAND-622597F2B1A6 entity_id=SIG-001062 reason=duplicate_id:SIG-001062 conf=0.9`
- `candidate CAND-4699FB3BE952 entity_id=SIG-001061 reason=duplicate_id:SIG-001061 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5B666465B337 | business_signal_library | 0.9 | False | duplicate_id:SIG-001064 | Rejected |
| CAND-47083254B265 | business_signal_library | 0.9 | False | duplicate_id:SIG-001063 | Rejected |
| CAND-4775A1046F79 | business_signal_library | 0.9 | False | duplicate_id:SIG-001065 | Rejected |
| CAND-622597F2B1A6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001062 | Rejected |
| CAND-4699FB3BE952 | business_signal_library | 0.92 | False | duplicate_id:SIG-001061 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001064` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
