# Candidate Root Cause

**Generated:** 2026-08-17T01:35:34+00:00
**Session:** `SESSION-20260817-022DF5`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000393`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-022DF5`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000393': 1, 'duplicate_id:SIG-000394': 1, 'duplicate_id:SIG-000392': 1, 'duplicate_id:SIG-000391': 1, 'duplicate_id:SIG-000395': 1}`
- `candidate CAND-6710DB37BF70 entity_id=SIG-000393 reason=duplicate_id:SIG-000393 conf=0.9`
- `candidate CAND-C6078FE1CC09 entity_id=SIG-000394 reason=duplicate_id:SIG-000394 conf=0.9`
- `candidate CAND-DD42F7D7C13A entity_id=SIG-000392 reason=duplicate_id:SIG-000392 conf=0.9`
- `candidate CAND-EFBEB6E184B1 entity_id=SIG-000391 reason=duplicate_id:SIG-000391 conf=0.92`
- `candidate CAND-10E599C7683B entity_id=SIG-000395 reason=duplicate_id:SIG-000395 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6710DB37BF70 | business_signal_library | 0.9 | False | duplicate_id:SIG-000393 | Rejected |
| CAND-C6078FE1CC09 | business_signal_library | 0.9 | False | duplicate_id:SIG-000394 | Rejected |
| CAND-DD42F7D7C13A | business_signal_library | 0.9 | False | duplicate_id:SIG-000392 | Rejected |
| CAND-EFBEB6E184B1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000391 | Rejected |
| CAND-10E599C7683B | business_signal_library | 0.9 | False | duplicate_id:SIG-000395 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000393` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
