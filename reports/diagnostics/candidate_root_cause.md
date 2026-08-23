# Candidate Root Cause

**Generated:** 2026-08-23T19:41:29+00:00
**Session:** `SESSION-20260823-EF8C3E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001159`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-EF8C3E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001159': 1, 'duplicate_id:SIG-001158': 1, 'duplicate_id:SIG-001156': 1, 'duplicate_id:SIG-001157': 1, 'duplicate_id:SIG-001160': 1}`
- `candidate CAND-67897A95FE97 entity_id=SIG-001159 reason=duplicate_id:SIG-001159 conf=0.9`
- `candidate CAND-60FFA530CE1E entity_id=SIG-001158 reason=duplicate_id:SIG-001158 conf=0.9`
- `candidate CAND-554A0DA62349 entity_id=SIG-001156 reason=duplicate_id:SIG-001156 conf=0.92`
- `candidate CAND-C8FC5A2FEC7C entity_id=SIG-001157 reason=duplicate_id:SIG-001157 conf=0.9`
- `candidate CAND-1B9016357C96 entity_id=SIG-001160 reason=duplicate_id:SIG-001160 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-67897A95FE97 | business_signal_library | 0.9 | False | duplicate_id:SIG-001159 | Rejected |
| CAND-60FFA530CE1E | business_signal_library | 0.9 | False | duplicate_id:SIG-001158 | Rejected |
| CAND-554A0DA62349 | business_signal_library | 0.92 | False | duplicate_id:SIG-001156 | Rejected |
| CAND-C8FC5A2FEC7C | business_signal_library | 0.9 | False | duplicate_id:SIG-001157 | Rejected |
| CAND-1B9016357C96 | business_signal_library | 0.9 | False | duplicate_id:SIG-001160 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001159` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
