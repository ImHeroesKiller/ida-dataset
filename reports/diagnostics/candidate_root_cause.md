# Candidate Root Cause

**Generated:** 2026-08-18T10:44:30+00:00
**Session:** `SESSION-20260818-F1F1DE`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000547`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-F1F1DE`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000547': 1, 'duplicate_id:SIG-000548': 1, 'duplicate_id:SIG-000549': 1, 'duplicate_id:SIG-000550': 1, 'duplicate_id:SIG-000546': 1}`
- `candidate CAND-2599302EEC6A entity_id=SIG-000547 reason=duplicate_id:SIG-000547 conf=0.9`
- `candidate CAND-918359B012B8 entity_id=SIG-000548 reason=duplicate_id:SIG-000548 conf=0.9`
- `candidate CAND-497B37901874 entity_id=SIG-000549 reason=duplicate_id:SIG-000549 conf=0.9`
- `candidate CAND-FE2184C6E8F8 entity_id=SIG-000550 reason=duplicate_id:SIG-000550 conf=0.9`
- `candidate CAND-F40B5D64DEE5 entity_id=SIG-000546 reason=duplicate_id:SIG-000546 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2599302EEC6A | business_signal_library | 0.9 | False | duplicate_id:SIG-000547 | Rejected |
| CAND-918359B012B8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000548 | Rejected |
| CAND-497B37901874 | business_signal_library | 0.9 | False | duplicate_id:SIG-000549 | Rejected |
| CAND-FE2184C6E8F8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000550 | Rejected |
| CAND-F40B5D64DEE5 | business_signal_library | 0.92 | False | duplicate_id:SIG-000546 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000547` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
