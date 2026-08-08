# Candidate Root Cause

**Generated:** 2026-08-08T05:23:21+00:00
**Session:** `SESSION-20260808-7A0726`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001579`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-7A0726`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001579': 1, 'duplicate_id:SIG-001577': 1, 'duplicate_id:SIG-001576': 1, 'duplicate_id:SIG-001575': 1, 'duplicate_id:SIG-001578': 1}`
- `candidate CAND-201F735BFD28 entity_id=SIG-001579 reason=duplicate_id:SIG-001579 conf=0.92`
- `candidate CAND-F58F06D78586 entity_id=SIG-001577 reason=duplicate_id:SIG-001577 conf=0.88`
- `candidate CAND-CF4DD487B376 entity_id=SIG-001576 reason=duplicate_id:SIG-001576 conf=0.92`
- `candidate CAND-C5A96BD4ABC0 entity_id=SIG-001575 reason=duplicate_id:SIG-001575 conf=0.9`
- `candidate CAND-3D33CFBC63CF entity_id=SIG-001578 reason=duplicate_id:SIG-001578 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-201F735BFD28 | business_signal_library | 0.92 | False | duplicate_id:SIG-001579 | Rejected |
| CAND-F58F06D78586 | business_signal_library | 0.88 | False | duplicate_id:SIG-001577 | Rejected |
| CAND-CF4DD487B376 | business_signal_library | 0.92 | False | duplicate_id:SIG-001576 | Rejected |
| CAND-C5A96BD4ABC0 | business_signal_library | 0.9 | False | duplicate_id:SIG-001575 | Rejected |
| CAND-3D33CFBC63CF | business_signal_library | 0.9 | False | duplicate_id:SIG-001578 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001579` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
