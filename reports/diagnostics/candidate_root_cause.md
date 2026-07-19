# Candidate Root Cause

**Generated:** 2026-07-19T23:12:58+00:00
**Session:** `SESSION-20260719-DBC1B8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000543`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260719-DBC1B8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000543': 1, 'duplicate_id:SIG-000541': 1, 'duplicate_id:SIG-000542': 1, 'duplicate_id:SIG-000540': 1, 'duplicate_id:SIG-000544': 1}`
- `candidate CAND-6AD491B800C0 entity_id=SIG-000543 reason=duplicate_id:SIG-000543 conf=0.92`
- `candidate CAND-F7F4061832FC entity_id=SIG-000541 reason=duplicate_id:SIG-000541 conf=0.92`
- `candidate CAND-2BF9D3ACB76E entity_id=SIG-000542 reason=duplicate_id:SIG-000542 conf=0.9`
- `candidate CAND-179A5443622E entity_id=SIG-000540 reason=duplicate_id:SIG-000540 conf=0.9`
- `candidate CAND-D19921F0B55B entity_id=SIG-000544 reason=duplicate_id:SIG-000544 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6AD491B800C0 | business_signal_library | 0.92 | False | duplicate_id:SIG-000543 | Rejected |
| CAND-F7F4061832FC | business_signal_library | 0.92 | False | duplicate_id:SIG-000541 | Rejected |
| CAND-2BF9D3ACB76E | business_signal_library | 0.9 | False | duplicate_id:SIG-000542 | Rejected |
| CAND-179A5443622E | business_signal_library | 0.9 | False | duplicate_id:SIG-000540 | Rejected |
| CAND-D19921F0B55B | business_signal_library | 0.9 | False | duplicate_id:SIG-000544 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000543` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
