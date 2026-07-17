# Candidate Root Cause

**Generated:** 2026-07-17T15:33:31+00:00
**Session:** `SESSION-20260717-211594`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000381`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260717-211594`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000381': 1, 'duplicate_id:SIG-000383': 1, 'duplicate_id:SIG-000382': 1, 'duplicate_id:SIG-000384': 1, 'duplicate_id:SIG-000380': 1}`
- `candidate CAND-8CA6977D8E36 entity_id=SIG-000381 reason=duplicate_id:SIG-000381 conf=0.92`
- `candidate CAND-FE6F4FFF3A05 entity_id=SIG-000383 reason=duplicate_id:SIG-000383 conf=0.92`
- `candidate CAND-20BF7B4CAADE entity_id=SIG-000382 reason=duplicate_id:SIG-000382 conf=0.9`
- `candidate CAND-9330E3DAEA96 entity_id=SIG-000384 reason=duplicate_id:SIG-000384 conf=0.9`
- `candidate CAND-EE41532A5E80 entity_id=SIG-000380 reason=duplicate_id:SIG-000380 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-8CA6977D8E36 | business_signal_library | 0.92 | False | duplicate_id:SIG-000381 | Rejected |
| CAND-FE6F4FFF3A05 | business_signal_library | 0.92 | False | duplicate_id:SIG-000383 | Rejected |
| CAND-20BF7B4CAADE | business_signal_library | 0.9 | False | duplicate_id:SIG-000382 | Rejected |
| CAND-9330E3DAEA96 | business_signal_library | 0.9 | False | duplicate_id:SIG-000384 | Rejected |
| CAND-EE41532A5E80 | business_signal_library | 0.9 | False | duplicate_id:SIG-000380 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000381` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
