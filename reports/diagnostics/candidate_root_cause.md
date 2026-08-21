# Candidate Root Cause

**Generated:** 2026-08-21T23:43:38+00:00
**Session:** `SESSION-20260821-295467`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000951`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-295467`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000951': 1, 'duplicate_id:SIG-000952': 1, 'duplicate_id:SIG-000954': 1, 'duplicate_id:SIG-000953': 1, 'duplicate_id:SIG-000955': 1}`
- `candidate CAND-07AB21F8D997 entity_id=SIG-000951 reason=duplicate_id:SIG-000951 conf=0.92`
- `candidate CAND-B16B2E04394A entity_id=SIG-000952 reason=duplicate_id:SIG-000952 conf=0.9`
- `candidate CAND-6B7A751DDB0F entity_id=SIG-000954 reason=duplicate_id:SIG-000954 conf=0.9`
- `candidate CAND-831B03389F9A entity_id=SIG-000953 reason=duplicate_id:SIG-000953 conf=0.9`
- `candidate CAND-4CA269D981F7 entity_id=SIG-000955 reason=duplicate_id:SIG-000955 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-07AB21F8D997 | business_signal_library | 0.92 | False | duplicate_id:SIG-000951 | Rejected |
| CAND-B16B2E04394A | business_signal_library | 0.9 | False | duplicate_id:SIG-000952 | Rejected |
| CAND-6B7A751DDB0F | business_signal_library | 0.9 | False | duplicate_id:SIG-000954 | Rejected |
| CAND-831B03389F9A | business_signal_library | 0.9 | False | duplicate_id:SIG-000953 | Rejected |
| CAND-4CA269D981F7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000955 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000951` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
