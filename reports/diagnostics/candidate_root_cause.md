# Candidate Root Cause

**Generated:** 2026-07-16T15:58:14+00:00
**Session:** `SESSION-20260716-9A2F5B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000322`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260716-9A2F5B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000322': 1, 'duplicate_id:SIG-000323': 1, 'duplicate_id:SIG-000320': 1, 'duplicate_id:SIG-000321': 1, 'duplicate_id:SIG-000324': 1}`
- `candidate CAND-C72E82BC4FD3 entity_id=SIG-000322 reason=duplicate_id:SIG-000322 conf=0.88`
- `candidate CAND-2B658D291D7F entity_id=SIG-000323 reason=duplicate_id:SIG-000323 conf=0.9`
- `candidate CAND-C57C03CBCA78 entity_id=SIG-000320 reason=duplicate_id:SIG-000320 conf=0.9`
- `candidate CAND-24F9392D74E3 entity_id=SIG-000321 reason=duplicate_id:SIG-000321 conf=0.92`
- `candidate CAND-75967B9722AF entity_id=SIG-000324 reason=duplicate_id:SIG-000324 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C72E82BC4FD3 | business_signal_library | 0.88 | False | duplicate_id:SIG-000322 | Rejected |
| CAND-2B658D291D7F | business_signal_library | 0.9 | False | duplicate_id:SIG-000323 | Rejected |
| CAND-C57C03CBCA78 | business_signal_library | 0.9 | False | duplicate_id:SIG-000320 | Rejected |
| CAND-24F9392D74E3 | business_signal_library | 0.92 | False | duplicate_id:SIG-000321 | Rejected |
| CAND-75967B9722AF | business_signal_library | 0.92 | False | duplicate_id:SIG-000324 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000322` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
