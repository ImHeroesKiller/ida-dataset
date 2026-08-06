# Candidate Root Cause

**Generated:** 2026-08-06T06:11:12+00:00
**Session:** `SESSION-20260806-0975DC`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001458`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260806-0975DC`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001458': 1, 'duplicate_id:SIG-001459': 1, 'duplicate_id:SIG-001455': 1, 'duplicate_id:SIG-001456': 1, 'duplicate_id:SIG-001457': 1}`
- `candidate CAND-CE1D72D83CE7 entity_id=SIG-001458 reason=duplicate_id:SIG-001458 conf=0.9`
- `candidate CAND-B05D3C825907 entity_id=SIG-001459 reason=duplicate_id:SIG-001459 conf=0.92`
- `candidate CAND-3E2284FE2C8E entity_id=SIG-001455 reason=duplicate_id:SIG-001455 conf=0.9`
- `candidate CAND-2D5247C562F4 entity_id=SIG-001456 reason=duplicate_id:SIG-001456 conf=0.92`
- `candidate CAND-0F9A662A5F08 entity_id=SIG-001457 reason=duplicate_id:SIG-001457 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-CE1D72D83CE7 | business_signal_library | 0.9 | False | duplicate_id:SIG-001458 | Rejected |
| CAND-B05D3C825907 | business_signal_library | 0.92 | False | duplicate_id:SIG-001459 | Rejected |
| CAND-3E2284FE2C8E | business_signal_library | 0.9 | False | duplicate_id:SIG-001455 | Rejected |
| CAND-2D5247C562F4 | business_signal_library | 0.92 | False | duplicate_id:SIG-001456 | Rejected |
| CAND-0F9A662A5F08 | business_signal_library | 0.88 | False | duplicate_id:SIG-001457 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001458` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
