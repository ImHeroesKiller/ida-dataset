# Candidate Root Cause

**Generated:** 2026-08-07T07:34:17+00:00
**Session:** `SESSION-20260807-4535E4`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001490`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-4535E4`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001490': 1, 'duplicate_id:SIG-001494': 1, 'duplicate_id:SIG-001492': 1, 'duplicate_id:SIG-001491': 1, 'duplicate_id:SIG-001493': 1}`
- `candidate CAND-D28980DE51E9 entity_id=SIG-001490 reason=duplicate_id:SIG-001490 conf=0.9`
- `candidate CAND-7C306AFC5ED4 entity_id=SIG-001494 reason=duplicate_id:SIG-001494 conf=0.92`
- `candidate CAND-C05120C55104 entity_id=SIG-001492 reason=duplicate_id:SIG-001492 conf=0.88`
- `candidate CAND-323C33E9E289 entity_id=SIG-001491 reason=duplicate_id:SIG-001491 conf=0.92`
- `candidate CAND-BC61B5F55483 entity_id=SIG-001493 reason=duplicate_id:SIG-001493 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D28980DE51E9 | business_signal_library | 0.9 | False | duplicate_id:SIG-001490 | Rejected |
| CAND-7C306AFC5ED4 | business_signal_library | 0.92 | False | duplicate_id:SIG-001494 | Rejected |
| CAND-C05120C55104 | business_signal_library | 0.88 | False | duplicate_id:SIG-001492 | Rejected |
| CAND-323C33E9E289 | business_signal_library | 0.92 | False | duplicate_id:SIG-001491 | Rejected |
| CAND-BC61B5F55483 | business_signal_library | 0.9 | False | duplicate_id:SIG-001493 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001490` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
