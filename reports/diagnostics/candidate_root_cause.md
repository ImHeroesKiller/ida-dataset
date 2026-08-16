# Candidate Root Cause

**Generated:** 2026-08-16T04:51:33+00:00
**Session:** `SESSION-20260816-627EB1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000291`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-627EB1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000291': 1, 'duplicate_id:SIG-000294': 1, 'duplicate_id:SIG-000292': 1, 'duplicate_id:SIG-000293': 1, 'duplicate_id:SIG-000295': 1}`
- `candidate CAND-633760A27FC7 entity_id=SIG-000291 reason=duplicate_id:SIG-000291 conf=0.92`
- `candidate CAND-96C59BEE58B3 entity_id=SIG-000294 reason=duplicate_id:SIG-000294 conf=0.9`
- `candidate CAND-503A3CAF2B20 entity_id=SIG-000292 reason=duplicate_id:SIG-000292 conf=0.9`
- `candidate CAND-E226A7292454 entity_id=SIG-000293 reason=duplicate_id:SIG-000293 conf=0.9`
- `candidate CAND-0E37D9DD4947 entity_id=SIG-000295 reason=duplicate_id:SIG-000295 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-633760A27FC7 | business_signal_library | 0.92 | False | duplicate_id:SIG-000291 | Rejected |
| CAND-96C59BEE58B3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000294 | Rejected |
| CAND-503A3CAF2B20 | business_signal_library | 0.9 | False | duplicate_id:SIG-000292 | Rejected |
| CAND-E226A7292454 | business_signal_library | 0.9 | False | duplicate_id:SIG-000293 | Rejected |
| CAND-0E37D9DD4947 | business_signal_library | 0.9 | False | duplicate_id:SIG-000295 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000291` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
