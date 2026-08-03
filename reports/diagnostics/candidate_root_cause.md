# Candidate Root Cause

**Generated:** 2026-08-03T20:46:47+00:00
**Session:** `SESSION-20260803-11E67E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001339`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260803-11E67E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001339': 1, 'duplicate_id:SIG-001338': 1, 'duplicate_id:SIG-001337': 1, 'duplicate_id:SIG-001336': 1, 'duplicate_id:SIG-001335': 1}`
- `candidate CAND-E14FE9EE8913 entity_id=SIG-001339 reason=duplicate_id:SIG-001339 conf=0.92`
- `candidate CAND-1CF81C5879AF entity_id=SIG-001338 reason=duplicate_id:SIG-001338 conf=0.9`
- `candidate CAND-E8ED3ABFE0D8 entity_id=SIG-001337 reason=duplicate_id:SIG-001337 conf=0.88`
- `candidate CAND-90F582D64FEB entity_id=SIG-001336 reason=duplicate_id:SIG-001336 conf=0.92`
- `candidate CAND-18DA13DB0E67 entity_id=SIG-001335 reason=duplicate_id:SIG-001335 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E14FE9EE8913 | business_signal_library | 0.92 | False | duplicate_id:SIG-001339 | Rejected |
| CAND-1CF81C5879AF | business_signal_library | 0.9 | False | duplicate_id:SIG-001338 | Rejected |
| CAND-E8ED3ABFE0D8 | business_signal_library | 0.88 | False | duplicate_id:SIG-001337 | Rejected |
| CAND-90F582D64FEB | business_signal_library | 0.92 | False | duplicate_id:SIG-001336 | Rejected |
| CAND-18DA13DB0E67 | business_signal_library | 0.9 | False | duplicate_id:SIG-001335 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001339` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
