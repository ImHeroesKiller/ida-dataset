# Candidate Root Cause

**Generated:** 2026-08-17T14:43:04+00:00
**Session:** `SESSION-20260817-6C339D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000455`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-6C339D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000455': 1, 'duplicate_id:SIG-000454': 1, 'duplicate_id:SIG-000451': 1, 'duplicate_id:SIG-000453': 1, 'duplicate_id:SIG-000452': 1}`
- `candidate CAND-7047A8737067 entity_id=SIG-000455 reason=duplicate_id:SIG-000455 conf=0.9`
- `candidate CAND-7E6BBCDA6D1C entity_id=SIG-000454 reason=duplicate_id:SIG-000454 conf=0.9`
- `candidate CAND-EDAF740A2DC6 entity_id=SIG-000451 reason=duplicate_id:SIG-000451 conf=0.92`
- `candidate CAND-4892BFB52828 entity_id=SIG-000453 reason=duplicate_id:SIG-000453 conf=0.9`
- `candidate CAND-D9944FC66E18 entity_id=SIG-000452 reason=duplicate_id:SIG-000452 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7047A8737067 | business_signal_library | 0.9 | False | duplicate_id:SIG-000455 | Rejected |
| CAND-7E6BBCDA6D1C | business_signal_library | 0.9 | False | duplicate_id:SIG-000454 | Rejected |
| CAND-EDAF740A2DC6 | business_signal_library | 0.92 | False | duplicate_id:SIG-000451 | Rejected |
| CAND-4892BFB52828 | business_signal_library | 0.9 | False | duplicate_id:SIG-000453 | Rejected |
| CAND-D9944FC66E18 | business_signal_library | 0.9 | False | duplicate_id:SIG-000452 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000455` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
