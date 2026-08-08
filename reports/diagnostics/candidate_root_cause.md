# Candidate Root Cause

**Generated:** 2026-08-08T08:15:04+00:00
**Session:** `SESSION-20260808-51992C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001594`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-51992C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001594': 1, 'duplicate_id:SIG-001591': 1, 'duplicate_id:SIG-001592': 1, 'duplicate_id:SIG-001593': 1, 'duplicate_id:SIG-001590': 1}`
- `candidate CAND-896A3F163EA0 entity_id=SIG-001594 reason=duplicate_id:SIG-001594 conf=0.9`
- `candidate CAND-00719BD18825 entity_id=SIG-001591 reason=duplicate_id:SIG-001591 conf=0.92`
- `candidate CAND-332BACE1F641 entity_id=SIG-001592 reason=duplicate_id:SIG-001592 conf=0.9`
- `candidate CAND-1A190230402A entity_id=SIG-001593 reason=duplicate_id:SIG-001593 conf=0.92`
- `candidate CAND-A6FDD4EA3E10 entity_id=SIG-001590 reason=duplicate_id:SIG-001590 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-896A3F163EA0 | business_signal_library | 0.9 | False | duplicate_id:SIG-001594 | Rejected |
| CAND-00719BD18825 | business_signal_library | 0.92 | False | duplicate_id:SIG-001591 | Rejected |
| CAND-332BACE1F641 | business_signal_library | 0.9 | False | duplicate_id:SIG-001592 | Rejected |
| CAND-1A190230402A | business_signal_library | 0.92 | False | duplicate_id:SIG-001593 | Rejected |
| CAND-A6FDD4EA3E10 | business_signal_library | 0.9 | False | duplicate_id:SIG-001590 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001594` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
