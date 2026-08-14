# Candidate Root Cause

**Generated:** 2026-08-14T13:20:53+00:00
**Session:** `SESSION-20260814-D7AC92`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000114`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-D7AC92`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000114': 1, 'duplicate_id:SIG-000111': 1, 'duplicate_id:SIG-000113': 1, 'duplicate_id:SIG-000112': 1, 'duplicate_id:SIG-000115': 1}`
- `candidate CAND-F6AF98DC1B2A entity_id=SIG-000114 reason=duplicate_id:SIG-000114 conf=0.9`
- `candidate CAND-A54FF35E5975 entity_id=SIG-000111 reason=duplicate_id:SIG-000111 conf=0.92`
- `candidate CAND-DC6A45E00464 entity_id=SIG-000113 reason=duplicate_id:SIG-000113 conf=0.9`
- `candidate CAND-DC43EDFB01D1 entity_id=SIG-000112 reason=duplicate_id:SIG-000112 conf=0.9`
- `candidate CAND-0531D4274D4F entity_id=SIG-000115 reason=duplicate_id:SIG-000115 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F6AF98DC1B2A | business_signal_library | 0.9 | False | duplicate_id:SIG-000114 | Rejected |
| CAND-A54FF35E5975 | business_signal_library | 0.92 | False | duplicate_id:SIG-000111 | Rejected |
| CAND-DC6A45E00464 | business_signal_library | 0.9 | False | duplicate_id:SIG-000113 | Rejected |
| CAND-DC43EDFB01D1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000112 | Rejected |
| CAND-0531D4274D4F | business_signal_library | 0.9 | False | duplicate_id:SIG-000115 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000114` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
