# Candidate Root Cause

**Generated:** 2026-07-29T21:15:28+00:00
**Session:** `SESSION-20260729-FA286B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001069`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260729-FA286B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001069': 1, 'duplicate_id:SIG-001068': 1, 'duplicate_id:SIG-001066': 1, 'duplicate_id:SIG-001067': 1, 'duplicate_id:SIG-001065': 1}`
- `candidate CAND-CBE734629757 entity_id=SIG-001069 reason=duplicate_id:SIG-001069 conf=0.92`
- `candidate CAND-72A60B889C92 entity_id=SIG-001068 reason=duplicate_id:SIG-001068 conf=0.9`
- `candidate CAND-85CFE8DEAAE4 entity_id=SIG-001066 reason=duplicate_id:SIG-001066 conf=0.92`
- `candidate CAND-EA9B4B11BBB0 entity_id=SIG-001067 reason=duplicate_id:SIG-001067 conf=0.88`
- `candidate CAND-1E596C520387 entity_id=SIG-001065 reason=duplicate_id:SIG-001065 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-CBE734629757 | business_signal_library | 0.92 | False | duplicate_id:SIG-001069 | Rejected |
| CAND-72A60B889C92 | business_signal_library | 0.9 | False | duplicate_id:SIG-001068 | Rejected |
| CAND-85CFE8DEAAE4 | business_signal_library | 0.92 | False | duplicate_id:SIG-001066 | Rejected |
| CAND-EA9B4B11BBB0 | business_signal_library | 0.88 | False | duplicate_id:SIG-001067 | Rejected |
| CAND-1E596C520387 | business_signal_library | 0.9 | False | duplicate_id:SIG-001065 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001069` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
