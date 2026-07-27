# Candidate Root Cause

**Generated:** 2026-07-27T12:44:10+00:00
**Session:** `SESSION-20260727-0F4B21`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000952`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260727-0F4B21`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000952': 1, 'duplicate_id:SIG-000954': 1, 'duplicate_id:SIG-000951': 1, 'duplicate_id:SIG-000950': 1, 'duplicate_id:SIG-000953': 1}`
- `candidate CAND-989C75827272 entity_id=SIG-000952 reason=duplicate_id:SIG-000952 conf=0.88`
- `candidate CAND-9F369C541BE6 entity_id=SIG-000954 reason=duplicate_id:SIG-000954 conf=0.92`
- `candidate CAND-BAC271049FB4 entity_id=SIG-000951 reason=duplicate_id:SIG-000951 conf=0.92`
- `candidate CAND-E9CD4F316DD7 entity_id=SIG-000950 reason=duplicate_id:SIG-000950 conf=0.9`
- `candidate CAND-0A43474D50A8 entity_id=SIG-000953 reason=duplicate_id:SIG-000953 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-989C75827272 | business_signal_library | 0.88 | False | duplicate_id:SIG-000952 | Rejected |
| CAND-9F369C541BE6 | business_signal_library | 0.92 | False | duplicate_id:SIG-000954 | Rejected |
| CAND-BAC271049FB4 | business_signal_library | 0.92 | False | duplicate_id:SIG-000951 | Rejected |
| CAND-E9CD4F316DD7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000950 | Rejected |
| CAND-0A43474D50A8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000953 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000952` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
