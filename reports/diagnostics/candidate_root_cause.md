# Candidate Root Cause

**Generated:** 2026-08-20T04:11:12+00:00
**Session:** `SESSION-20260820-1EBBC9`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000743`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-1EBBC9`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000743': 1, 'duplicate_id:SIG-000745': 1, 'duplicate_id:SIG-000742': 1, 'duplicate_id:SIG-000741': 1, 'duplicate_id:SIG-000744': 1}`
- `candidate CAND-D55F42E19E42 entity_id=SIG-000743 reason=duplicate_id:SIG-000743 conf=0.9`
- `candidate CAND-EFA7EBA43D85 entity_id=SIG-000745 reason=duplicate_id:SIG-000745 conf=0.9`
- `candidate CAND-3C96D5B41992 entity_id=SIG-000742 reason=duplicate_id:SIG-000742 conf=0.9`
- `candidate CAND-6D42F3B92796 entity_id=SIG-000741 reason=duplicate_id:SIG-000741 conf=0.92`
- `candidate CAND-796D82D2EFE3 entity_id=SIG-000744 reason=duplicate_id:SIG-000744 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D55F42E19E42 | business_signal_library | 0.9 | False | duplicate_id:SIG-000743 | Rejected |
| CAND-EFA7EBA43D85 | business_signal_library | 0.9 | False | duplicate_id:SIG-000745 | Rejected |
| CAND-3C96D5B41992 | business_signal_library | 0.9 | False | duplicate_id:SIG-000742 | Rejected |
| CAND-6D42F3B92796 | business_signal_library | 0.92 | False | duplicate_id:SIG-000741 | Rejected |
| CAND-796D82D2EFE3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000744 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000743` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
