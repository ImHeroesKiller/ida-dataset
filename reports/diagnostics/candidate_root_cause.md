# Candidate Root Cause

**Generated:** 2026-07-23T18:33:22+00:00
**Session:** `SESSION-20260723-0CFFBF`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000741`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260723-0CFFBF`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000741': 1, 'duplicate_id:SIG-000740': 1, 'duplicate_id:SIG-000742': 1, 'duplicate_id:SIG-000744': 1, 'duplicate_id:SIG-000743': 1}`
- `candidate CAND-250C74F2EEBB entity_id=SIG-000741 reason=duplicate_id:SIG-000741 conf=0.92`
- `candidate CAND-D6678FE6776D entity_id=SIG-000740 reason=duplicate_id:SIG-000740 conf=0.9`
- `candidate CAND-825E598F936A entity_id=SIG-000742 reason=duplicate_id:SIG-000742 conf=0.88`
- `candidate CAND-8D478EAD28B6 entity_id=SIG-000744 reason=duplicate_id:SIG-000744 conf=0.92`
- `candidate CAND-C1F9121CCB1E entity_id=SIG-000743 reason=duplicate_id:SIG-000743 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-250C74F2EEBB | business_signal_library | 0.92 | False | duplicate_id:SIG-000741 | Rejected |
| CAND-D6678FE6776D | business_signal_library | 0.9 | False | duplicate_id:SIG-000740 | Rejected |
| CAND-825E598F936A | business_signal_library | 0.88 | False | duplicate_id:SIG-000742 | Rejected |
| CAND-8D478EAD28B6 | business_signal_library | 0.92 | False | duplicate_id:SIG-000744 | Rejected |
| CAND-C1F9121CCB1E | business_signal_library | 0.9 | False | duplicate_id:SIG-000743 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000741` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
