# Candidate Root Cause

**Generated:** 2026-08-18T20:37:59+00:00
**Session:** `SESSION-20260818-FD6BA6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000598`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-FD6BA6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000598': 1, 'duplicate_id:SIG-000600': 1, 'duplicate_id:SIG-000599': 1, 'duplicate_id:SIG-000596': 1, 'duplicate_id:SIG-000597': 1}`
- `candidate CAND-172541DF4BF1 entity_id=SIG-000598 reason=duplicate_id:SIG-000598 conf=0.9`
- `candidate CAND-50CCB6204CF8 entity_id=SIG-000600 reason=duplicate_id:SIG-000600 conf=0.9`
- `candidate CAND-5579B11B91D4 entity_id=SIG-000599 reason=duplicate_id:SIG-000599 conf=0.9`
- `candidate CAND-34DE723773F9 entity_id=SIG-000596 reason=duplicate_id:SIG-000596 conf=0.92`
- `candidate CAND-021324DE79E0 entity_id=SIG-000597 reason=duplicate_id:SIG-000597 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-172541DF4BF1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000598 | Rejected |
| CAND-50CCB6204CF8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000600 | Rejected |
| CAND-5579B11B91D4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000599 | Rejected |
| CAND-34DE723773F9 | business_signal_library | 0.92 | False | duplicate_id:SIG-000596 | Rejected |
| CAND-021324DE79E0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000597 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000598` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
