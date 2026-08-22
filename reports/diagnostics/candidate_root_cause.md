# Candidate Root Cause

**Generated:** 2026-08-22T15:40:19+00:00
**Session:** `SESSION-20260822-FE63E5`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001027`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-FE63E5`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001027': 1, 'duplicate_id:SIG-001028': 1, 'duplicate_id:SIG-001026': 1, 'duplicate_id:SIG-001029': 1, 'duplicate_id:SIG-001030': 1}`
- `candidate CAND-BD38E685CE8E entity_id=SIG-001027 reason=duplicate_id:SIG-001027 conf=0.9`
- `candidate CAND-BC051DE91082 entity_id=SIG-001028 reason=duplicate_id:SIG-001028 conf=0.9`
- `candidate CAND-FB6CE0153A7E entity_id=SIG-001026 reason=duplicate_id:SIG-001026 conf=0.92`
- `candidate CAND-C98EB5F5C1D8 entity_id=SIG-001029 reason=duplicate_id:SIG-001029 conf=0.9`
- `candidate CAND-EAFE96CCB1F6 entity_id=SIG-001030 reason=duplicate_id:SIG-001030 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-BD38E685CE8E | business_signal_library | 0.9 | False | duplicate_id:SIG-001027 | Rejected |
| CAND-BC051DE91082 | business_signal_library | 0.9 | False | duplicate_id:SIG-001028 | Rejected |
| CAND-FB6CE0153A7E | business_signal_library | 0.92 | False | duplicate_id:SIG-001026 | Rejected |
| CAND-C98EB5F5C1D8 | business_signal_library | 0.9 | False | duplicate_id:SIG-001029 | Rejected |
| CAND-EAFE96CCB1F6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001030 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001027` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
