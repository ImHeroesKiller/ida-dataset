# Candidate Root Cause

**Generated:** 2026-07-14T11:07:44+00:00
**Session:** `SESSION-20260714-B330A0`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000199`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260714-B330A0`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000199': 1, 'duplicate_id:SIG-000196': 1, 'duplicate_id:SIG-000197': 1, 'duplicate_id:SIG-000195': 1, 'duplicate_id:SIG-000198': 1}`
- `candidate CAND-FDFC3B1B6F81 entity_id=SIG-000199 reason=duplicate_id:SIG-000199 conf=0.88`
- `candidate CAND-92743443C38C entity_id=SIG-000196 reason=duplicate_id:SIG-000196 conf=0.88`
- `candidate CAND-FEB750B16EF9 entity_id=SIG-000197 reason=duplicate_id:SIG-000197 conf=0.92`
- `candidate CAND-D2DBCB55F879 entity_id=SIG-000195 reason=duplicate_id:SIG-000195 conf=0.9`
- `candidate CAND-A951CC1F5172 entity_id=SIG-000198 reason=duplicate_id:SIG-000198 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FDFC3B1B6F81 | business_signal_library | 0.88 | False | duplicate_id:SIG-000199 | Rejected |
| CAND-92743443C38C | business_signal_library | 0.88 | False | duplicate_id:SIG-000196 | Rejected |
| CAND-FEB750B16EF9 | business_signal_library | 0.92 | False | duplicate_id:SIG-000197 | Rejected |
| CAND-D2DBCB55F879 | business_signal_library | 0.9 | False | duplicate_id:SIG-000195 | Rejected |
| CAND-A951CC1F5172 | business_signal_library | 0.9 | False | duplicate_id:SIG-000198 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000199` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
