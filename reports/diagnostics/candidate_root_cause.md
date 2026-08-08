# Candidate Root Cause

**Generated:** 2026-08-08T23:49:04+00:00
**Session:** `SESSION-20260808-2DE03D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001673`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-2DE03D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001673': 1, 'duplicate_id:SIG-001674': 1, 'duplicate_id:SIG-001671': 1, 'duplicate_id:SIG-001670': 1, 'duplicate_id:SIG-001672': 1}`
- `candidate CAND-7BDD4ABADCA0 entity_id=SIG-001673 reason=duplicate_id:SIG-001673 conf=0.9`
- `candidate CAND-3E3FE8C51F39 entity_id=SIG-001674 reason=duplicate_id:SIG-001674 conf=0.92`
- `candidate CAND-5F7113DBFF2E entity_id=SIG-001671 reason=duplicate_id:SIG-001671 conf=0.92`
- `candidate CAND-9A3A230B1C88 entity_id=SIG-001670 reason=duplicate_id:SIG-001670 conf=0.9`
- `candidate CAND-CD966623F161 entity_id=SIG-001672 reason=duplicate_id:SIG-001672 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7BDD4ABADCA0 | business_signal_library | 0.9 | False | duplicate_id:SIG-001673 | Rejected |
| CAND-3E3FE8C51F39 | business_signal_library | 0.92 | False | duplicate_id:SIG-001674 | Rejected |
| CAND-5F7113DBFF2E | business_signal_library | 0.92 | False | duplicate_id:SIG-001671 | Rejected |
| CAND-9A3A230B1C88 | business_signal_library | 0.9 | False | duplicate_id:SIG-001670 | Rejected |
| CAND-CD966623F161 | business_signal_library | 0.88 | False | duplicate_id:SIG-001672 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001673` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
