# Candidate Root Cause

**Generated:** 2026-08-21T14:55:40+00:00
**Session:** `SESSION-20260821-6A8A5A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000908`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-6A8A5A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000908': 1, 'duplicate_id:SIG-000906': 1, 'duplicate_id:SIG-000909': 1, 'duplicate_id:SIG-000910': 1, 'duplicate_id:SIG-000907': 1}`
- `candidate CAND-5543F71F63FF entity_id=SIG-000908 reason=duplicate_id:SIG-000908 conf=0.9`
- `candidate CAND-4E6097EBA33C entity_id=SIG-000906 reason=duplicate_id:SIG-000906 conf=0.92`
- `candidate CAND-CBE87EE5B85A entity_id=SIG-000909 reason=duplicate_id:SIG-000909 conf=0.9`
- `candidate CAND-BA5DFFE2162C entity_id=SIG-000910 reason=duplicate_id:SIG-000910 conf=0.9`
- `candidate CAND-4F18BC3FB4DC entity_id=SIG-000907 reason=duplicate_id:SIG-000907 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5543F71F63FF | business_signal_library | 0.9 | False | duplicate_id:SIG-000908 | Rejected |
| CAND-4E6097EBA33C | business_signal_library | 0.92 | False | duplicate_id:SIG-000906 | Rejected |
| CAND-CBE87EE5B85A | business_signal_library | 0.9 | False | duplicate_id:SIG-000909 | Rejected |
| CAND-BA5DFFE2162C | business_signal_library | 0.9 | False | duplicate_id:SIG-000910 | Rejected |
| CAND-4F18BC3FB4DC | business_signal_library | 0.9 | False | duplicate_id:SIG-000907 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000908` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
