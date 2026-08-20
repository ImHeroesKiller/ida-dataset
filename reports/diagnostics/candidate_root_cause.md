# Candidate Root Cause

**Generated:** 2026-08-20T21:47:21+00:00
**Session:** `SESSION-20260820-232D8C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000832`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-232D8C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000832': 1, 'duplicate_id:SIG-000835': 1, 'duplicate_id:SIG-000834': 1, 'duplicate_id:SIG-000833': 1, 'duplicate_id:SIG-000831': 1}`
- `candidate CAND-639CAB5B7B18 entity_id=SIG-000832 reason=duplicate_id:SIG-000832 conf=0.9`
- `candidate CAND-BF14ABE7C79E entity_id=SIG-000835 reason=duplicate_id:SIG-000835 conf=0.9`
- `candidate CAND-86865F14A3F0 entity_id=SIG-000834 reason=duplicate_id:SIG-000834 conf=0.9`
- `candidate CAND-BAFB8094FCEC entity_id=SIG-000833 reason=duplicate_id:SIG-000833 conf=0.9`
- `candidate CAND-EDA8F851B637 entity_id=SIG-000831 reason=duplicate_id:SIG-000831 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-639CAB5B7B18 | business_signal_library | 0.9 | False | duplicate_id:SIG-000832 | Rejected |
| CAND-BF14ABE7C79E | business_signal_library | 0.9 | False | duplicate_id:SIG-000835 | Rejected |
| CAND-86865F14A3F0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000834 | Rejected |
| CAND-BAFB8094FCEC | business_signal_library | 0.9 | False | duplicate_id:SIG-000833 | Rejected |
| CAND-EDA8F851B637 | business_signal_library | 0.92 | False | duplicate_id:SIG-000831 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000832` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
