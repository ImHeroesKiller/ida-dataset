# Candidate Root Cause

**Generated:** 2026-08-11T02:11:37+00:00
**Session:** `SESSION-20260811-E43338`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001863`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260811-E43338`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001863': 1, 'duplicate_id:SIG-001864': 1, 'duplicate_id:SIG-001861': 1, 'duplicate_id:SIG-001862': 1, 'duplicate_id:SIG-001860': 1}`
- `candidate CAND-87BDB91702DD entity_id=SIG-001863 reason=duplicate_id:SIG-001863 conf=0.9`
- `candidate CAND-981125BCDEF4 entity_id=SIG-001864 reason=duplicate_id:SIG-001864 conf=0.92`
- `candidate CAND-E9BF1B826645 entity_id=SIG-001861 reason=duplicate_id:SIG-001861 conf=0.92`
- `candidate CAND-F164579474AF entity_id=SIG-001862 reason=duplicate_id:SIG-001862 conf=0.88`
- `candidate CAND-C556A19D07E7 entity_id=SIG-001860 reason=duplicate_id:SIG-001860 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-87BDB91702DD | business_signal_library | 0.9 | False | duplicate_id:SIG-001863 | Rejected |
| CAND-981125BCDEF4 | business_signal_library | 0.92 | False | duplicate_id:SIG-001864 | Rejected |
| CAND-E9BF1B826645 | business_signal_library | 0.92 | False | duplicate_id:SIG-001861 | Rejected |
| CAND-F164579474AF | business_signal_library | 0.88 | False | duplicate_id:SIG-001862 | Rejected |
| CAND-C556A19D07E7 | business_signal_library | 0.9 | False | duplicate_id:SIG-001860 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001863` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
