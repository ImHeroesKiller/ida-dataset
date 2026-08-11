# Candidate Root Cause

**Generated:** 2026-08-11T16:25:20+00:00
**Session:** `SESSION-20260811-4E5A2B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001906`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260811-4E5A2B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001906': 1, 'duplicate_id:SIG-001909': 1, 'duplicate_id:SIG-001908': 1, 'duplicate_id:SIG-001905': 1, 'duplicate_id:SIG-001907': 1}`
- `candidate CAND-5EF1B06B3907 entity_id=SIG-001906 reason=duplicate_id:SIG-001906 conf=0.92`
- `candidate CAND-19E23356FE15 entity_id=SIG-001909 reason=duplicate_id:SIG-001909 conf=0.92`
- `candidate CAND-8C1AEDF5E714 entity_id=SIG-001908 reason=duplicate_id:SIG-001908 conf=0.9`
- `candidate CAND-D4D5D6B0FF58 entity_id=SIG-001905 reason=duplicate_id:SIG-001905 conf=0.9`
- `candidate CAND-ED344A1D9A4F entity_id=SIG-001907 reason=duplicate_id:SIG-001907 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5EF1B06B3907 | business_signal_library | 0.92 | False | duplicate_id:SIG-001906 | Rejected |
| CAND-19E23356FE15 | business_signal_library | 0.92 | False | duplicate_id:SIG-001909 | Rejected |
| CAND-8C1AEDF5E714 | business_signal_library | 0.9 | False | duplicate_id:SIG-001908 | Rejected |
| CAND-D4D5D6B0FF58 | business_signal_library | 0.9 | False | duplicate_id:SIG-001905 | Rejected |
| CAND-ED344A1D9A4F | business_signal_library | 0.88 | False | duplicate_id:SIG-001907 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001906` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
