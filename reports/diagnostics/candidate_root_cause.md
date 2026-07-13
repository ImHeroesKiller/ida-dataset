# Candidate Root Cause

**Generated:** 2026-07-13T09:58:07+00:00
**Session:** `SESSION-20260713-758858`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000154`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260713-758858`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000154': 1, 'duplicate_id:SIG-000153': 1, 'duplicate_id:SIG-000151': 1, 'duplicate_id:SIG-000150': 1, 'duplicate_id:SIG-000152': 1}`
- `candidate CAND-E81B6B05ED28 entity_id=SIG-000154 reason=duplicate_id:SIG-000154 conf=0.92`
- `candidate CAND-6C12166FC30D entity_id=SIG-000153 reason=duplicate_id:SIG-000153 conf=0.9`
- `candidate CAND-CC9A741E8084 entity_id=SIG-000151 reason=duplicate_id:SIG-000151 conf=0.92`
- `candidate CAND-76343B2A3D5C entity_id=SIG-000150 reason=duplicate_id:SIG-000150 conf=0.9`
- `candidate CAND-C44310DE0529 entity_id=SIG-000152 reason=duplicate_id:SIG-000152 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E81B6B05ED28 | business_signal_library | 0.92 | False | duplicate_id:SIG-000154 | Rejected |
| CAND-6C12166FC30D | business_signal_library | 0.9 | False | duplicate_id:SIG-000153 | Rejected |
| CAND-CC9A741E8084 | business_signal_library | 0.92 | False | duplicate_id:SIG-000151 | Rejected |
| CAND-76343B2A3D5C | business_signal_library | 0.9 | False | duplicate_id:SIG-000150 | Rejected |
| CAND-C44310DE0529 | business_signal_library | 0.88 | False | duplicate_id:SIG-000152 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000154` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
