# Candidate Root Cause

**Generated:** 2026-08-15T03:06:41+00:00
**Session:** `SESSION-20260815-276EBE`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000174`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-276EBE`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000174': 1, 'duplicate_id:SIG-000172': 1, 'duplicate_id:SIG-000175': 1, 'duplicate_id:SIG-000173': 1, 'duplicate_id:SIG-000171': 1}`
- `candidate CAND-4C14ACE9A8C0 entity_id=SIG-000174 reason=duplicate_id:SIG-000174 conf=0.9`
- `candidate CAND-EE9530DA6A21 entity_id=SIG-000172 reason=duplicate_id:SIG-000172 conf=0.9`
- `candidate CAND-6FC8BDB8B382 entity_id=SIG-000175 reason=duplicate_id:SIG-000175 conf=0.9`
- `candidate CAND-FB078486DE38 entity_id=SIG-000173 reason=duplicate_id:SIG-000173 conf=0.9`
- `candidate CAND-5D54CCE2DD57 entity_id=SIG-000171 reason=duplicate_id:SIG-000171 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4C14ACE9A8C0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000174 | Rejected |
| CAND-EE9530DA6A21 | business_signal_library | 0.9 | False | duplicate_id:SIG-000172 | Rejected |
| CAND-6FC8BDB8B382 | business_signal_library | 0.9 | False | duplicate_id:SIG-000175 | Rejected |
| CAND-FB078486DE38 | business_signal_library | 0.9 | False | duplicate_id:SIG-000173 | Rejected |
| CAND-5D54CCE2DD57 | business_signal_library | 0.92 | False | duplicate_id:SIG-000171 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000174` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
