# Candidate Root Cause

**Generated:** 2026-08-17T09:57:21+00:00
**Session:** `SESSION-20260817-8534D2`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000429`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-8534D2`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000429': 1, 'duplicate_id:SIG-000426': 1, 'duplicate_id:SIG-000430': 1, 'duplicate_id:SIG-000428': 1, 'duplicate_id:SIG-000427': 1}`
- `candidate CAND-EB11F5B07543 entity_id=SIG-000429 reason=duplicate_id:SIG-000429 conf=0.9`
- `candidate CAND-D05540678A59 entity_id=SIG-000426 reason=duplicate_id:SIG-000426 conf=0.92`
- `candidate CAND-A0D7DB64B158 entity_id=SIG-000430 reason=duplicate_id:SIG-000430 conf=0.9`
- `candidate CAND-F3FBC553FB66 entity_id=SIG-000428 reason=duplicate_id:SIG-000428 conf=0.9`
- `candidate CAND-6B936E0FFAED entity_id=SIG-000427 reason=duplicate_id:SIG-000427 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-EB11F5B07543 | business_signal_library | 0.9 | False | duplicate_id:SIG-000429 | Rejected |
| CAND-D05540678A59 | business_signal_library | 0.92 | False | duplicate_id:SIG-000426 | Rejected |
| CAND-A0D7DB64B158 | business_signal_library | 0.9 | False | duplicate_id:SIG-000430 | Rejected |
| CAND-F3FBC553FB66 | business_signal_library | 0.9 | False | duplicate_id:SIG-000428 | Rejected |
| CAND-6B936E0FFAED | business_signal_library | 0.9 | False | duplicate_id:SIG-000427 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000429` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
