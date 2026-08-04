# Candidate Root Cause

**Generated:** 2026-08-04T22:32:14+00:00
**Session:** `SESSION-20260804-51D277`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001392`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260804-51D277`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001392': 1, 'duplicate_id:SIG-001394': 1, 'duplicate_id:SIG-001393': 1, 'duplicate_id:SIG-001391': 1, 'duplicate_id:SIG-001390': 1}`
- `candidate CAND-D821562676F1 entity_id=SIG-001392 reason=duplicate_id:SIG-001392 conf=0.88`
- `candidate CAND-8815FAF4065E entity_id=SIG-001394 reason=duplicate_id:SIG-001394 conf=0.92`
- `candidate CAND-F9C9F462E156 entity_id=SIG-001393 reason=duplicate_id:SIG-001393 conf=0.9`
- `candidate CAND-6887DBD14BE1 entity_id=SIG-001391 reason=duplicate_id:SIG-001391 conf=0.92`
- `candidate CAND-B549AEAE5919 entity_id=SIG-001390 reason=duplicate_id:SIG-001390 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D821562676F1 | business_signal_library | 0.88 | False | duplicate_id:SIG-001392 | Rejected |
| CAND-8815FAF4065E | business_signal_library | 0.92 | False | duplicate_id:SIG-001394 | Rejected |
| CAND-F9C9F462E156 | business_signal_library | 0.9 | False | duplicate_id:SIG-001393 | Rejected |
| CAND-6887DBD14BE1 | business_signal_library | 0.92 | False | duplicate_id:SIG-001391 | Rejected |
| CAND-B549AEAE5919 | business_signal_library | 0.9 | False | duplicate_id:SIG-001390 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001392` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
