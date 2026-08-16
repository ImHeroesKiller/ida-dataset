# Candidate Root Cause

**Generated:** 2026-08-16T18:45:37+00:00
**Session:** `SESSION-20260816-EC17F0`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000365`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-EC17F0`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000365': 1, 'duplicate_id:SIG-000362': 1, 'duplicate_id:SIG-000363': 1, 'duplicate_id:SIG-000364': 1, 'duplicate_id:SIG-000361': 1}`
- `candidate CAND-5BB36E9B897A entity_id=SIG-000365 reason=duplicate_id:SIG-000365 conf=0.9`
- `candidate CAND-D383A5022E66 entity_id=SIG-000362 reason=duplicate_id:SIG-000362 conf=0.9`
- `candidate CAND-F9DBF09376D3 entity_id=SIG-000363 reason=duplicate_id:SIG-000363 conf=0.9`
- `candidate CAND-29910E5FDBDF entity_id=SIG-000364 reason=duplicate_id:SIG-000364 conf=0.9`
- `candidate CAND-228F9051A01C entity_id=SIG-000361 reason=duplicate_id:SIG-000361 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5BB36E9B897A | business_signal_library | 0.9 | False | duplicate_id:SIG-000365 | Rejected |
| CAND-D383A5022E66 | business_signal_library | 0.9 | False | duplicate_id:SIG-000362 | Rejected |
| CAND-F9DBF09376D3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000363 | Rejected |
| CAND-29910E5FDBDF | business_signal_library | 0.9 | False | duplicate_id:SIG-000364 | Rejected |
| CAND-228F9051A01C | business_signal_library | 0.92 | False | duplicate_id:SIG-000361 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000365` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
