# Candidate Root Cause

**Generated:** 2026-08-18T09:03:07+00:00
**Session:** `SESSION-20260818-D61D3C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000539`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-D61D3C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000539': 1, 'duplicate_id:SIG-000537': 1, 'duplicate_id:SIG-000538': 1, 'duplicate_id:SIG-000540': 1, 'duplicate_id:SIG-000536': 1}`
- `candidate CAND-7C45D0DA47C4 entity_id=SIG-000539 reason=duplicate_id:SIG-000539 conf=0.9`
- `candidate CAND-46DBE0B695BD entity_id=SIG-000537 reason=duplicate_id:SIG-000537 conf=0.9`
- `candidate CAND-02B818D381CE entity_id=SIG-000538 reason=duplicate_id:SIG-000538 conf=0.9`
- `candidate CAND-2B73D1E4A36F entity_id=SIG-000540 reason=duplicate_id:SIG-000540 conf=0.9`
- `candidate CAND-1611BBA58A91 entity_id=SIG-000536 reason=duplicate_id:SIG-000536 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7C45D0DA47C4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000539 | Rejected |
| CAND-46DBE0B695BD | business_signal_library | 0.9 | False | duplicate_id:SIG-000537 | Rejected |
| CAND-02B818D381CE | business_signal_library | 0.9 | False | duplicate_id:SIG-000538 | Rejected |
| CAND-2B73D1E4A36F | business_signal_library | 0.9 | False | duplicate_id:SIG-000540 | Rejected |
| CAND-1611BBA58A91 | business_signal_library | 0.92 | False | duplicate_id:SIG-000536 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000539` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
