# Candidate Root Cause

**Generated:** 2026-07-21T08:57:38+00:00
**Session:** `SESSION-20260721-3CD3CE`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000614`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260721-3CD3CE`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000614': 1, 'duplicate_id:SIG-000613': 1, 'duplicate_id:SIG-000612': 1, 'duplicate_id:SIG-000611': 1, 'duplicate_id:SIG-000610': 1}`
- `candidate CAND-8AAD6AE805BB entity_id=SIG-000614 reason=duplicate_id:SIG-000614 conf=0.92`
- `candidate CAND-7916F282A65A entity_id=SIG-000613 reason=duplicate_id:SIG-000613 conf=0.9`
- `candidate CAND-4F4C0907B3FF entity_id=SIG-000612 reason=duplicate_id:SIG-000612 conf=0.88`
- `candidate CAND-5E9AB7056F2F entity_id=SIG-000611 reason=duplicate_id:SIG-000611 conf=0.92`
- `candidate CAND-411FAA6F5720 entity_id=SIG-000610 reason=duplicate_id:SIG-000610 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-8AAD6AE805BB | business_signal_library | 0.92 | False | duplicate_id:SIG-000614 | Rejected |
| CAND-7916F282A65A | business_signal_library | 0.9 | False | duplicate_id:SIG-000613 | Rejected |
| CAND-4F4C0907B3FF | business_signal_library | 0.88 | False | duplicate_id:SIG-000612 | Rejected |
| CAND-5E9AB7056F2F | business_signal_library | 0.92 | False | duplicate_id:SIG-000611 | Rejected |
| CAND-411FAA6F5720 | business_signal_library | 0.9 | False | duplicate_id:SIG-000610 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000614` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
