# Candidate Root Cause

**Generated:** 2026-08-07T06:00:03+00:00
**Session:** `SESSION-20260807-1A8F4F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001488`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-1A8F4F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001488': 1, 'duplicate_id:SIG-001486': 1, 'duplicate_id:SIG-001485': 1, 'duplicate_id:SIG-001487': 1, 'duplicate_id:SIG-001489': 1}`
- `candidate CAND-3BEFA05AFD89 entity_id=SIG-001488 reason=duplicate_id:SIG-001488 conf=0.9`
- `candidate CAND-BA250567348B entity_id=SIG-001486 reason=duplicate_id:SIG-001486 conf=0.92`
- `candidate CAND-A1BB6AD11B32 entity_id=SIG-001485 reason=duplicate_id:SIG-001485 conf=0.9`
- `candidate CAND-099D9DF66EDC entity_id=SIG-001487 reason=duplicate_id:SIG-001487 conf=0.88`
- `candidate CAND-47AD6A9B5F03 entity_id=SIG-001489 reason=duplicate_id:SIG-001489 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3BEFA05AFD89 | business_signal_library | 0.9 | False | duplicate_id:SIG-001488 | Rejected |
| CAND-BA250567348B | business_signal_library | 0.92 | False | duplicate_id:SIG-001486 | Rejected |
| CAND-A1BB6AD11B32 | business_signal_library | 0.9 | False | duplicate_id:SIG-001485 | Rejected |
| CAND-099D9DF66EDC | business_signal_library | 0.88 | False | duplicate_id:SIG-001487 | Rejected |
| CAND-47AD6A9B5F03 | business_signal_library | 0.92 | False | duplicate_id:SIG-001489 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001488` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
