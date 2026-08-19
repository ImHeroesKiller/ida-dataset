# Candidate Root Cause

**Generated:** 2026-08-19T13:10:06+00:00
**Session:** `SESSION-20260819-38D089`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000675`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-38D089`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000675': 1, 'duplicate_id:SIG-000673': 1, 'duplicate_id:SIG-000672': 1, 'duplicate_id:SIG-000671': 1, 'duplicate_id:SIG-000674': 1}`
- `candidate CAND-99CB4AFB1C52 entity_id=SIG-000675 reason=duplicate_id:SIG-000675 conf=0.9`
- `candidate CAND-87E7FF6F65C9 entity_id=SIG-000673 reason=duplicate_id:SIG-000673 conf=0.9`
- `candidate CAND-6EE736BCEFA1 entity_id=SIG-000672 reason=duplicate_id:SIG-000672 conf=0.9`
- `candidate CAND-8C72BD7CA0AE entity_id=SIG-000671 reason=duplicate_id:SIG-000671 conf=0.92`
- `candidate CAND-87701479CDE7 entity_id=SIG-000674 reason=duplicate_id:SIG-000674 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-99CB4AFB1C52 | business_signal_library | 0.9 | False | duplicate_id:SIG-000675 | Rejected |
| CAND-87E7FF6F65C9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000673 | Rejected |
| CAND-6EE736BCEFA1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000672 | Rejected |
| CAND-8C72BD7CA0AE | business_signal_library | 0.92 | False | duplicate_id:SIG-000671 | Rejected |
| CAND-87701479CDE7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000674 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000675` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
