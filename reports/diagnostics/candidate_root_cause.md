# Candidate Root Cause

**Generated:** 2026-08-24T10:08:23+00:00
**Session:** `SESSION-20260824-20615C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001211`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260824-20615C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001211': 1, 'duplicate_id:SIG-001215': 1, 'duplicate_id:SIG-001212': 1, 'duplicate_id:SIG-001213': 1, 'duplicate_id:SIG-001214': 1}`
- `candidate CAND-089DAA0A6612 entity_id=SIG-001211 reason=duplicate_id:SIG-001211 conf=0.92`
- `candidate CAND-79C7D156092E entity_id=SIG-001215 reason=duplicate_id:SIG-001215 conf=0.9`
- `candidate CAND-CF373C52DC15 entity_id=SIG-001212 reason=duplicate_id:SIG-001212 conf=0.9`
- `candidate CAND-0B1F6CCFADF6 entity_id=SIG-001213 reason=duplicate_id:SIG-001213 conf=0.9`
- `candidate CAND-B0BFDB3FDB22 entity_id=SIG-001214 reason=duplicate_id:SIG-001214 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-089DAA0A6612 | business_signal_library | 0.92 | False | duplicate_id:SIG-001211 | Rejected |
| CAND-79C7D156092E | business_signal_library | 0.9 | False | duplicate_id:SIG-001215 | Rejected |
| CAND-CF373C52DC15 | business_signal_library | 0.9 | False | duplicate_id:SIG-001212 | Rejected |
| CAND-0B1F6CCFADF6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001213 | Rejected |
| CAND-B0BFDB3FDB22 | business_signal_library | 0.9 | False | duplicate_id:SIG-001214 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001211` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
