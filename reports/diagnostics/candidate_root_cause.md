# Candidate Root Cause

**Generated:** 2026-07-16T17:34:21+00:00
**Session:** `SESSION-20260716-A9BE59`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000328`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260716-A9BE59`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000328': 1, 'duplicate_id:SIG-000325': 1, 'duplicate_id:SIG-000327': 1, 'duplicate_id:SIG-000326': 1, 'duplicate_id:SIG-000329': 1}`
- `candidate CAND-917892FD9116 entity_id=SIG-000328 reason=duplicate_id:SIG-000328 conf=0.9`
- `candidate CAND-E71EB8159183 entity_id=SIG-000325 reason=duplicate_id:SIG-000325 conf=0.9`
- `candidate CAND-1532953B3748 entity_id=SIG-000327 reason=duplicate_id:SIG-000327 conf=0.92`
- `candidate CAND-F9E630E7797D entity_id=SIG-000326 reason=duplicate_id:SIG-000326 conf=0.88`
- `candidate CAND-CA293BEE26A5 entity_id=SIG-000329 reason=duplicate_id:SIG-000329 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-917892FD9116 | business_signal_library | 0.9 | False | duplicate_id:SIG-000328 | Rejected |
| CAND-E71EB8159183 | business_signal_library | 0.9 | False | duplicate_id:SIG-000325 | Rejected |
| CAND-1532953B3748 | business_signal_library | 0.92 | False | duplicate_id:SIG-000327 | Rejected |
| CAND-F9E630E7797D | business_signal_library | 0.88 | False | duplicate_id:SIG-000326 | Rejected |
| CAND-CA293BEE26A5 | business_signal_library | 0.88 | False | duplicate_id:SIG-000329 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000328` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
