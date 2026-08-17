# Candidate Root Cause

**Generated:** 2026-08-17T22:40:11+00:00
**Session:** `SESSION-20260817-961D26`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000491`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-961D26`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000491': 1, 'duplicate_id:SIG-000495': 1, 'duplicate_id:SIG-000492': 1, 'duplicate_id:SIG-000494': 1, 'duplicate_id:SIG-000493': 1}`
- `candidate CAND-89D5606D368D entity_id=SIG-000491 reason=duplicate_id:SIG-000491 conf=0.92`
- `candidate CAND-E5E526D12E4F entity_id=SIG-000495 reason=duplicate_id:SIG-000495 conf=0.9`
- `candidate CAND-E7F7A21524EC entity_id=SIG-000492 reason=duplicate_id:SIG-000492 conf=0.9`
- `candidate CAND-7E6C56E1B25B entity_id=SIG-000494 reason=duplicate_id:SIG-000494 conf=0.9`
- `candidate CAND-7DD7533AB1DF entity_id=SIG-000493 reason=duplicate_id:SIG-000493 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-89D5606D368D | business_signal_library | 0.92 | False | duplicate_id:SIG-000491 | Rejected |
| CAND-E5E526D12E4F | business_signal_library | 0.9 | False | duplicate_id:SIG-000495 | Rejected |
| CAND-E7F7A21524EC | business_signal_library | 0.9 | False | duplicate_id:SIG-000492 | Rejected |
| CAND-7E6C56E1B25B | business_signal_library | 0.9 | False | duplicate_id:SIG-000494 | Rejected |
| CAND-7DD7533AB1DF | business_signal_library | 0.9 | False | duplicate_id:SIG-000493 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000491` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
