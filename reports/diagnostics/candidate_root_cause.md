# Candidate Root Cause

**Generated:** 2026-08-22T01:36:16+00:00
**Session:** `SESSION-20260822-6857F0`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000958`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-6857F0`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000958': 1, 'duplicate_id:SIG-000957': 1, 'duplicate_id:SIG-000959': 1, 'duplicate_id:SIG-000960': 1, 'duplicate_id:SIG-000956': 1}`
- `candidate CAND-FC9150DAD143 entity_id=SIG-000958 reason=duplicate_id:SIG-000958 conf=0.9`
- `candidate CAND-8642A3BD588F entity_id=SIG-000957 reason=duplicate_id:SIG-000957 conf=0.9`
- `candidate CAND-61ECEC3868AE entity_id=SIG-000959 reason=duplicate_id:SIG-000959 conf=0.9`
- `candidate CAND-EFCE7ACA1E28 entity_id=SIG-000960 reason=duplicate_id:SIG-000960 conf=0.9`
- `candidate CAND-37C204162B2F entity_id=SIG-000956 reason=duplicate_id:SIG-000956 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FC9150DAD143 | business_signal_library | 0.9 | False | duplicate_id:SIG-000958 | Rejected |
| CAND-8642A3BD588F | business_signal_library | 0.9 | False | duplicate_id:SIG-000957 | Rejected |
| CAND-61ECEC3868AE | business_signal_library | 0.9 | False | duplicate_id:SIG-000959 | Rejected |
| CAND-EFCE7ACA1E28 | business_signal_library | 0.9 | False | duplicate_id:SIG-000960 | Rejected |
| CAND-37C204162B2F | business_signal_library | 0.92 | False | duplicate_id:SIG-000956 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000958` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
