# Candidate Root Cause

**Generated:** 2026-08-17T21:41:27+00:00
**Session:** `SESSION-20260817-32E753`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000489`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-32E753`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000489': 1, 'duplicate_id:SIG-000488': 1, 'duplicate_id:SIG-000486': 1, 'duplicate_id:SIG-000490': 1, 'duplicate_id:SIG-000487': 1}`
- `candidate CAND-FE797E03BE7B entity_id=SIG-000489 reason=duplicate_id:SIG-000489 conf=0.9`
- `candidate CAND-3CE2DBCCF6B7 entity_id=SIG-000488 reason=duplicate_id:SIG-000488 conf=0.9`
- `candidate CAND-A5580FB78E49 entity_id=SIG-000486 reason=duplicate_id:SIG-000486 conf=0.92`
- `candidate CAND-DD81301824F0 entity_id=SIG-000490 reason=duplicate_id:SIG-000490 conf=0.9`
- `candidate CAND-FCD109E65BD8 entity_id=SIG-000487 reason=duplicate_id:SIG-000487 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FE797E03BE7B | business_signal_library | 0.9 | False | duplicate_id:SIG-000489 | Rejected |
| CAND-3CE2DBCCF6B7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000488 | Rejected |
| CAND-A5580FB78E49 | business_signal_library | 0.92 | False | duplicate_id:SIG-000486 | Rejected |
| CAND-DD81301824F0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000490 | Rejected |
| CAND-FCD109E65BD8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000487 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000489` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
