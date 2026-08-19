# Candidate Root Cause

**Generated:** 2026-08-19T01:36:29+00:00
**Session:** `SESSION-20260819-84359B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000618`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-84359B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000618': 1, 'duplicate_id:SIG-000619': 1, 'duplicate_id:SIG-000616': 1, 'duplicate_id:SIG-000620': 1, 'duplicate_id:SIG-000617': 1}`
- `candidate CAND-BA57BDDBE3F8 entity_id=SIG-000618 reason=duplicate_id:SIG-000618 conf=0.9`
- `candidate CAND-3CBF9398DCBC entity_id=SIG-000619 reason=duplicate_id:SIG-000619 conf=0.9`
- `candidate CAND-169AD6C981DE entity_id=SIG-000616 reason=duplicate_id:SIG-000616 conf=0.92`
- `candidate CAND-0BF3E63296CB entity_id=SIG-000620 reason=duplicate_id:SIG-000620 conf=0.9`
- `candidate CAND-6FB8E6977951 entity_id=SIG-000617 reason=duplicate_id:SIG-000617 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-BA57BDDBE3F8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000618 | Rejected |
| CAND-3CBF9398DCBC | business_signal_library | 0.9 | False | duplicate_id:SIG-000619 | Rejected |
| CAND-169AD6C981DE | business_signal_library | 0.92 | False | duplicate_id:SIG-000616 | Rejected |
| CAND-0BF3E63296CB | business_signal_library | 0.9 | False | duplicate_id:SIG-000620 | Rejected |
| CAND-6FB8E6977951 | business_signal_library | 0.9 | False | duplicate_id:SIG-000617 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000618` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
