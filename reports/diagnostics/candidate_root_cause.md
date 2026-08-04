# Candidate Root Cause

**Generated:** 2026-08-04T20:44:08+00:00
**Session:** `SESSION-20260804-B1ABCD`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001389`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260804-B1ABCD`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001389': 1, 'duplicate_id:SIG-001386': 1, 'duplicate_id:SIG-001387': 1, 'duplicate_id:SIG-001388': 1, 'duplicate_id:SIG-001385': 1}`
- `candidate CAND-A771CD7A80C5 entity_id=SIG-001389 reason=duplicate_id:SIG-001389 conf=0.92`
- `candidate CAND-5B70EF808670 entity_id=SIG-001386 reason=duplicate_id:SIG-001386 conf=0.92`
- `candidate CAND-31255D4527BC entity_id=SIG-001387 reason=duplicate_id:SIG-001387 conf=0.88`
- `candidate CAND-AA57B44AE581 entity_id=SIG-001388 reason=duplicate_id:SIG-001388 conf=0.9`
- `candidate CAND-A92D6F79FB99 entity_id=SIG-001385 reason=duplicate_id:SIG-001385 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A771CD7A80C5 | business_signal_library | 0.92 | False | duplicate_id:SIG-001389 | Rejected |
| CAND-5B70EF808670 | business_signal_library | 0.92 | False | duplicate_id:SIG-001386 | Rejected |
| CAND-31255D4527BC | business_signal_library | 0.88 | False | duplicate_id:SIG-001387 | Rejected |
| CAND-AA57B44AE581 | business_signal_library | 0.9 | False | duplicate_id:SIG-001388 | Rejected |
| CAND-A92D6F79FB99 | business_signal_library | 0.9 | False | duplicate_id:SIG-001385 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001389` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
