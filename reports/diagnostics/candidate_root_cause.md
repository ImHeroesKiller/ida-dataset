# Candidate Root Cause

**Generated:** 2026-08-23T09:47:52+00:00
**Session:** `SESSION-20260823-DD71D7`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001109`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-DD71D7`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001109': 1, 'duplicate_id:SIG-001106': 1, 'duplicate_id:SIG-001110': 1, 'duplicate_id:SIG-001108': 1, 'duplicate_id:SIG-001107': 1}`
- `candidate CAND-1CE670113672 entity_id=SIG-001109 reason=duplicate_id:SIG-001109 conf=0.9`
- `candidate CAND-89CC5216C4F8 entity_id=SIG-001106 reason=duplicate_id:SIG-001106 conf=0.92`
- `candidate CAND-2E486E4D7BD6 entity_id=SIG-001110 reason=duplicate_id:SIG-001110 conf=0.9`
- `candidate CAND-14B22BDD6862 entity_id=SIG-001108 reason=duplicate_id:SIG-001108 conf=0.9`
- `candidate CAND-818485DDE2FD entity_id=SIG-001107 reason=duplicate_id:SIG-001107 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-1CE670113672 | business_signal_library | 0.9 | False | duplicate_id:SIG-001109 | Rejected |
| CAND-89CC5216C4F8 | business_signal_library | 0.92 | False | duplicate_id:SIG-001106 | Rejected |
| CAND-2E486E4D7BD6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001110 | Rejected |
| CAND-14B22BDD6862 | business_signal_library | 0.9 | False | duplicate_id:SIG-001108 | Rejected |
| CAND-818485DDE2FD | business_signal_library | 0.9 | False | duplicate_id:SIG-001107 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001109` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
