# Candidate Root Cause

**Generated:** 2026-07-27T16:01:31+00:00
**Session:** `SESSION-20260727-2D348B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000959`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260727-2D348B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000959': 1, 'duplicate_id:SIG-000955': 1, 'duplicate_id:SIG-000957': 1, 'duplicate_id:SIG-000958': 1, 'duplicate_id:SIG-000956': 1}`
- `candidate CAND-8F59F65371C3 entity_id=SIG-000959 reason=duplicate_id:SIG-000959 conf=0.92`
- `candidate CAND-374C37BA48E0 entity_id=SIG-000955 reason=duplicate_id:SIG-000955 conf=0.9`
- `candidate CAND-C449B4DE1466 entity_id=SIG-000957 reason=duplicate_id:SIG-000957 conf=0.88`
- `candidate CAND-1BC1D9E48E7E entity_id=SIG-000958 reason=duplicate_id:SIG-000958 conf=0.9`
- `candidate CAND-BF0D33164E52 entity_id=SIG-000956 reason=duplicate_id:SIG-000956 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-8F59F65371C3 | business_signal_library | 0.92 | False | duplicate_id:SIG-000959 | Rejected |
| CAND-374C37BA48E0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000955 | Rejected |
| CAND-C449B4DE1466 | business_signal_library | 0.88 | False | duplicate_id:SIG-000957 | Rejected |
| CAND-1BC1D9E48E7E | business_signal_library | 0.9 | False | duplicate_id:SIG-000958 | Rejected |
| CAND-BF0D33164E52 | business_signal_library | 0.92 | False | duplicate_id:SIG-000956 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000959` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
