# Candidate Root Cause

**Generated:** 2026-07-12T16:25:30+00:00
**Session:** `SESSION-20260712-EED5D2`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000113`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260712-EED5D2`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000113': 1, 'duplicate_id:SIG-000111': 1, 'duplicate_id:SIG-000114': 1, 'duplicate_id:SIG-000112': 1, 'duplicate_id:SIG-000110': 1}`
- `candidate CAND-D1136EB30F69 entity_id=SIG-000113 reason=duplicate_id:SIG-000113 conf=0.9`
- `candidate CAND-667E71ADDC64 entity_id=SIG-000111 reason=duplicate_id:SIG-000111 conf=0.92`
- `candidate CAND-BFB2ED06EB21 entity_id=SIG-000114 reason=duplicate_id:SIG-000114 conf=0.92`
- `candidate CAND-285C75536837 entity_id=SIG-000112 reason=duplicate_id:SIG-000112 conf=0.88`
- `candidate CAND-BBE91DE4D22D entity_id=SIG-000110 reason=duplicate_id:SIG-000110 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D1136EB30F69 | business_signal_library | 0.9 | False | duplicate_id:SIG-000113 | Rejected |
| CAND-667E71ADDC64 | business_signal_library | 0.92 | False | duplicate_id:SIG-000111 | Rejected |
| CAND-BFB2ED06EB21 | business_signal_library | 0.92 | False | duplicate_id:SIG-000114 | Rejected |
| CAND-285C75536837 | business_signal_library | 0.88 | False | duplicate_id:SIG-000112 | Rejected |
| CAND-BBE91DE4D22D | business_signal_library | 0.9 | False | duplicate_id:SIG-000110 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000113` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
