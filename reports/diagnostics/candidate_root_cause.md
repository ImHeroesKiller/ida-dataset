# Candidate Root Cause

**Generated:** 2026-08-23T10:43:36+00:00
**Session:** `SESSION-20260823-092161`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001111`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-092161`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001111': 1, 'duplicate_id:SIG-001112': 1, 'duplicate_id:SIG-001113': 1, 'duplicate_id:SIG-001114': 1, 'duplicate_id:SIG-001115': 1}`
- `candidate CAND-4F14C6EA9AB5 entity_id=SIG-001111 reason=duplicate_id:SIG-001111 conf=0.92`
- `candidate CAND-30D0D3BA0BE7 entity_id=SIG-001112 reason=duplicate_id:SIG-001112 conf=0.9`
- `candidate CAND-9F6D7D02F3CE entity_id=SIG-001113 reason=duplicate_id:SIG-001113 conf=0.9`
- `candidate CAND-CE804A82D09B entity_id=SIG-001114 reason=duplicate_id:SIG-001114 conf=0.9`
- `candidate CAND-04742D9EB879 entity_id=SIG-001115 reason=duplicate_id:SIG-001115 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4F14C6EA9AB5 | business_signal_library | 0.92 | False | duplicate_id:SIG-001111 | Rejected |
| CAND-30D0D3BA0BE7 | business_signal_library | 0.9 | False | duplicate_id:SIG-001112 | Rejected |
| CAND-9F6D7D02F3CE | business_signal_library | 0.9 | False | duplicate_id:SIG-001113 | Rejected |
| CAND-CE804A82D09B | business_signal_library | 0.9 | False | duplicate_id:SIG-001114 | Rejected |
| CAND-04742D9EB879 | business_signal_library | 0.9 | False | duplicate_id:SIG-001115 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001111` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
