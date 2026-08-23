# Candidate Root Cause

**Generated:** 2026-08-23T13:00:08+00:00
**Session:** `SESSION-20260823-1E00EB`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001123`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-1E00EB`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001123': 1, 'duplicate_id:SIG-001121': 1, 'duplicate_id:SIG-001124': 1, 'duplicate_id:SIG-001125': 1, 'duplicate_id:SIG-001122': 1}`
- `candidate CAND-DB73C7CBE34B entity_id=SIG-001123 reason=duplicate_id:SIG-001123 conf=0.9`
- `candidate CAND-5200DB2C9A23 entity_id=SIG-001121 reason=duplicate_id:SIG-001121 conf=0.92`
- `candidate CAND-2ABC5CE9ED51 entity_id=SIG-001124 reason=duplicate_id:SIG-001124 conf=0.9`
- `candidate CAND-EB0586B8867F entity_id=SIG-001125 reason=duplicate_id:SIG-001125 conf=0.9`
- `candidate CAND-680D30B06D4A entity_id=SIG-001122 reason=duplicate_id:SIG-001122 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DB73C7CBE34B | business_signal_library | 0.9 | False | duplicate_id:SIG-001123 | Rejected |
| CAND-5200DB2C9A23 | business_signal_library | 0.92 | False | duplicate_id:SIG-001121 | Rejected |
| CAND-2ABC5CE9ED51 | business_signal_library | 0.9 | False | duplicate_id:SIG-001124 | Rejected |
| CAND-EB0586B8867F | business_signal_library | 0.9 | False | duplicate_id:SIG-001125 | Rejected |
| CAND-680D30B06D4A | business_signal_library | 0.9 | False | duplicate_id:SIG-001122 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001123` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
