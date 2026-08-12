# Candidate Root Cause

**Generated:** 2026-08-12T16:23:51+00:00
**Session:** `SESSION-20260812-A6804C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001986`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260812-A6804C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001986': 1, 'duplicate_id:SIG-001987': 1, 'duplicate_id:SIG-001989': 1, 'duplicate_id:SIG-001988': 1, 'duplicate_id:SIG-001985': 1}`
- `candidate CAND-0ED8A638D2E4 entity_id=SIG-001986 reason=duplicate_id:SIG-001986 conf=0.92`
- `candidate CAND-065348A727CE entity_id=SIG-001987 reason=duplicate_id:SIG-001987 conf=0.88`
- `candidate CAND-AA348B1AC4A3 entity_id=SIG-001989 reason=duplicate_id:SIG-001989 conf=0.92`
- `candidate CAND-EAA3E290DC4B entity_id=SIG-001988 reason=duplicate_id:SIG-001988 conf=0.9`
- `candidate CAND-3191B0E3914C entity_id=SIG-001985 reason=duplicate_id:SIG-001985 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0ED8A638D2E4 | business_signal_library | 0.92 | False | duplicate_id:SIG-001986 | Rejected |
| CAND-065348A727CE | business_signal_library | 0.88 | False | duplicate_id:SIG-001987 | Rejected |
| CAND-AA348B1AC4A3 | business_signal_library | 0.92 | False | duplicate_id:SIG-001989 | Rejected |
| CAND-EAA3E290DC4B | business_signal_library | 0.9 | False | duplicate_id:SIG-001988 | Rejected |
| CAND-3191B0E3914C | business_signal_library | 0.9 | False | duplicate_id:SIG-001985 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001986` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
