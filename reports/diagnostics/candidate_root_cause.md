# Candidate Root Cause

**Generated:** 2026-08-23T01:43:47+00:00
**Session:** `SESSION-20260823-42EB8C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001073`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-42EB8C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001073': 1, 'duplicate_id:SIG-001072': 1, 'duplicate_id:SIG-001075': 1, 'duplicate_id:SIG-001074': 1, 'duplicate_id:SIG-001071': 1}`
- `candidate CAND-415C5402A871 entity_id=SIG-001073 reason=duplicate_id:SIG-001073 conf=0.9`
- `candidate CAND-1185F8E14E7B entity_id=SIG-001072 reason=duplicate_id:SIG-001072 conf=0.9`
- `candidate CAND-79F02F3102EC entity_id=SIG-001075 reason=duplicate_id:SIG-001075 conf=0.9`
- `candidate CAND-794FA3B8695A entity_id=SIG-001074 reason=duplicate_id:SIG-001074 conf=0.9`
- `candidate CAND-F601293A232F entity_id=SIG-001071 reason=duplicate_id:SIG-001071 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-415C5402A871 | business_signal_library | 0.9 | False | duplicate_id:SIG-001073 | Rejected |
| CAND-1185F8E14E7B | business_signal_library | 0.9 | False | duplicate_id:SIG-001072 | Rejected |
| CAND-79F02F3102EC | business_signal_library | 0.9 | False | duplicate_id:SIG-001075 | Rejected |
| CAND-794FA3B8695A | business_signal_library | 0.9 | False | duplicate_id:SIG-001074 | Rejected |
| CAND-F601293A232F | business_signal_library | 0.92 | False | duplicate_id:SIG-001071 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001073` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
