# Candidate Root Cause

**Generated:** 2026-07-18T08:13:24+00:00
**Session:** `SESSION-20260718-505C3B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000423`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260718-505C3B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000423': 1, 'duplicate_id:SIG-000420': 1, 'duplicate_id:SIG-000421': 1, 'duplicate_id:SIG-000424': 1, 'duplicate_id:SIG-000422': 1}`
- `candidate CAND-712CC33095B1 entity_id=SIG-000423 reason=duplicate_id:SIG-000423 conf=0.9`
- `candidate CAND-1ADCE73E2E31 entity_id=SIG-000420 reason=duplicate_id:SIG-000420 conf=0.9`
- `candidate CAND-C0269D7DF623 entity_id=SIG-000421 reason=duplicate_id:SIG-000421 conf=0.92`
- `candidate CAND-5E8C5ACAE520 entity_id=SIG-000424 reason=duplicate_id:SIG-000424 conf=0.92`
- `candidate CAND-3F87E8FB6B36 entity_id=SIG-000422 reason=duplicate_id:SIG-000422 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-712CC33095B1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000423 | Rejected |
| CAND-1ADCE73E2E31 | business_signal_library | 0.9 | False | duplicate_id:SIG-000420 | Rejected |
| CAND-C0269D7DF623 | business_signal_library | 0.92 | False | duplicate_id:SIG-000421 | Rejected |
| CAND-5E8C5ACAE520 | business_signal_library | 0.92 | False | duplicate_id:SIG-000424 | Rejected |
| CAND-3F87E8FB6B36 | business_signal_library | 0.88 | False | duplicate_id:SIG-000422 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000423` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
