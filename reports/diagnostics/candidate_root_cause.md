# Candidate Root Cause

**Generated:** 2026-07-18T22:14:01+00:00
**Session:** `SESSION-20260718-062A24`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000469`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260718-062A24`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000469': 1, 'duplicate_id:SIG-000465': 1, 'duplicate_id:SIG-000467': 1, 'duplicate_id:SIG-000466': 1, 'duplicate_id:SIG-000468': 1}`
- `candidate CAND-F5A82C597F45 entity_id=SIG-000469 reason=duplicate_id:SIG-000469 conf=0.92`
- `candidate CAND-9FAFF8D842A5 entity_id=SIG-000465 reason=duplicate_id:SIG-000465 conf=0.9`
- `candidate CAND-67D1020D67BA entity_id=SIG-000467 reason=duplicate_id:SIG-000467 conf=0.88`
- `candidate CAND-8B96638C998B entity_id=SIG-000466 reason=duplicate_id:SIG-000466 conf=0.92`
- `candidate CAND-29C8C08F7663 entity_id=SIG-000468 reason=duplicate_id:SIG-000468 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F5A82C597F45 | business_signal_library | 0.92 | False | duplicate_id:SIG-000469 | Rejected |
| CAND-9FAFF8D842A5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000465 | Rejected |
| CAND-67D1020D67BA | business_signal_library | 0.88 | False | duplicate_id:SIG-000467 | Rejected |
| CAND-8B96638C998B | business_signal_library | 0.92 | False | duplicate_id:SIG-000466 | Rejected |
| CAND-29C8C08F7663 | business_signal_library | 0.9 | False | duplicate_id:SIG-000468 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000469` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
