# Candidate Root Cause

**Generated:** 2026-08-15T18:43:08+00:00
**Session:** `SESSION-20260815-F5F5B1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000253`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-F5F5B1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000253': 1, 'duplicate_id:SIG-000254': 1, 'duplicate_id:SIG-000252': 1, 'duplicate_id:SIG-000255': 1, 'duplicate_id:SIG-000251': 1}`
- `candidate CAND-68AE8F4EC205 entity_id=SIG-000253 reason=duplicate_id:SIG-000253 conf=0.9`
- `candidate CAND-8B3FFC58D8C1 entity_id=SIG-000254 reason=duplicate_id:SIG-000254 conf=0.9`
- `candidate CAND-FA5AD7F70835 entity_id=SIG-000252 reason=duplicate_id:SIG-000252 conf=0.9`
- `candidate CAND-0D06ADE5459D entity_id=SIG-000255 reason=duplicate_id:SIG-000255 conf=0.9`
- `candidate CAND-B2ADD55D3507 entity_id=SIG-000251 reason=duplicate_id:SIG-000251 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-68AE8F4EC205 | business_signal_library | 0.9 | False | duplicate_id:SIG-000253 | Rejected |
| CAND-8B3FFC58D8C1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000254 | Rejected |
| CAND-FA5AD7F70835 | business_signal_library | 0.9 | False | duplicate_id:SIG-000252 | Rejected |
| CAND-0D06ADE5459D | business_signal_library | 0.9 | False | duplicate_id:SIG-000255 | Rejected |
| CAND-B2ADD55D3507 | business_signal_library | 0.92 | False | duplicate_id:SIG-000251 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000253` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
