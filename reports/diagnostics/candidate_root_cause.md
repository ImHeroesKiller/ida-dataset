# Candidate Root Cause

**Generated:** 2026-07-29T19:38:38+00:00
**Session:** `SESSION-20260729-9757A5`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001061`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260729-9757A5`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001061': 1, 'duplicate_id:SIG-001063': 1, 'duplicate_id:SIG-001060': 1, 'duplicate_id:SIG-001062': 1, 'duplicate_id:SIG-001064': 1}`
- `candidate CAND-09CAD66AD0BD entity_id=SIG-001061 reason=duplicate_id:SIG-001061 conf=0.92`
- `candidate CAND-2766DB5E6811 entity_id=SIG-001063 reason=duplicate_id:SIG-001063 conf=0.9`
- `candidate CAND-9A3AA4758A26 entity_id=SIG-001060 reason=duplicate_id:SIG-001060 conf=0.9`
- `candidate CAND-17C9204C021E entity_id=SIG-001062 reason=duplicate_id:SIG-001062 conf=0.88`
- `candidate CAND-B07615F66A7A entity_id=SIG-001064 reason=duplicate_id:SIG-001064 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-09CAD66AD0BD | business_signal_library | 0.92 | False | duplicate_id:SIG-001061 | Rejected |
| CAND-2766DB5E6811 | business_signal_library | 0.9 | False | duplicate_id:SIG-001063 | Rejected |
| CAND-9A3AA4758A26 | business_signal_library | 0.9 | False | duplicate_id:SIG-001060 | Rejected |
| CAND-17C9204C021E | business_signal_library | 0.88 | False | duplicate_id:SIG-001062 | Rejected |
| CAND-B07615F66A7A | business_signal_library | 0.92 | False | duplicate_id:SIG-001064 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001061` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
