# Candidate Root Cause

**Generated:** 2026-08-15T10:37:01+00:00
**Session:** `SESSION-20260815-19A91C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000211`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-19A91C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000211': 1, 'duplicate_id:SIG-000213': 1, 'duplicate_id:SIG-000212': 1, 'duplicate_id:SIG-000215': 1, 'duplicate_id:SIG-000214': 1}`
- `candidate CAND-9BDEC75B316C entity_id=SIG-000211 reason=duplicate_id:SIG-000211 conf=0.92`
- `candidate CAND-E1101C1C6C93 entity_id=SIG-000213 reason=duplicate_id:SIG-000213 conf=0.9`
- `candidate CAND-A1A237638773 entity_id=SIG-000212 reason=duplicate_id:SIG-000212 conf=0.9`
- `candidate CAND-A9AA975AEBC9 entity_id=SIG-000215 reason=duplicate_id:SIG-000215 conf=0.9`
- `candidate CAND-99B60BC20496 entity_id=SIG-000214 reason=duplicate_id:SIG-000214 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-9BDEC75B316C | business_signal_library | 0.92 | False | duplicate_id:SIG-000211 | Rejected |
| CAND-E1101C1C6C93 | business_signal_library | 0.9 | False | duplicate_id:SIG-000213 | Rejected |
| CAND-A1A237638773 | business_signal_library | 0.9 | False | duplicate_id:SIG-000212 | Rejected |
| CAND-A9AA975AEBC9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000215 | Rejected |
| CAND-99B60BC20496 | business_signal_library | 0.9 | False | duplicate_id:SIG-000214 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000211` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
