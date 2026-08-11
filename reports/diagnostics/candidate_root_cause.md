# Candidate Root Cause

**Generated:** 2026-08-11T21:10:12+00:00
**Session:** `SESSION-20260811-94AACE`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001920`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260811-94AACE`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001920': 1, 'duplicate_id:SIG-001923': 1, 'duplicate_id:SIG-001921': 1, 'duplicate_id:SIG-001924': 1, 'duplicate_id:SIG-001922': 1}`
- `candidate CAND-0FDBB0F7555F entity_id=SIG-001920 reason=duplicate_id:SIG-001920 conf=0.9`
- `candidate CAND-F13167DC0072 entity_id=SIG-001923 reason=duplicate_id:SIG-001923 conf=0.9`
- `candidate CAND-31B233865B9E entity_id=SIG-001921 reason=duplicate_id:SIG-001921 conf=0.92`
- `candidate CAND-98E862F0E8C1 entity_id=SIG-001924 reason=duplicate_id:SIG-001924 conf=0.92`
- `candidate CAND-6F5F34D72DAF entity_id=SIG-001922 reason=duplicate_id:SIG-001922 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0FDBB0F7555F | business_signal_library | 0.9 | False | duplicate_id:SIG-001920 | Rejected |
| CAND-F13167DC0072 | business_signal_library | 0.9 | False | duplicate_id:SIG-001923 | Rejected |
| CAND-31B233865B9E | business_signal_library | 0.92 | False | duplicate_id:SIG-001921 | Rejected |
| CAND-98E862F0E8C1 | business_signal_library | 0.92 | False | duplicate_id:SIG-001924 | Rejected |
| CAND-6F5F34D72DAF | business_signal_library | 0.88 | False | duplicate_id:SIG-001922 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001920` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
