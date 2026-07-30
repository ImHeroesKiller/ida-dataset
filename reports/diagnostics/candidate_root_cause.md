# Candidate Root Cause

**Generated:** 2026-07-30T22:26:01+00:00
**Session:** `SESSION-20260730-7C9A45`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001127`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260730-7C9A45`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001127': 1, 'duplicate_id:SIG-001125': 1, 'duplicate_id:SIG-001129': 1, 'duplicate_id:SIG-001126': 1, 'duplicate_id:SIG-001128': 1}`
- `candidate CAND-231EE580A37B entity_id=SIG-001127 reason=duplicate_id:SIG-001127 conf=0.88`
- `candidate CAND-85B0F0D3208C entity_id=SIG-001125 reason=duplicate_id:SIG-001125 conf=0.9`
- `candidate CAND-12A8896C1572 entity_id=SIG-001129 reason=duplicate_id:SIG-001129 conf=0.92`
- `candidate CAND-86A88A945BB5 entity_id=SIG-001126 reason=duplicate_id:SIG-001126 conf=0.92`
- `candidate CAND-7E4BAF35DCAE entity_id=SIG-001128 reason=duplicate_id:SIG-001128 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-231EE580A37B | business_signal_library | 0.88 | False | duplicate_id:SIG-001127 | Rejected |
| CAND-85B0F0D3208C | business_signal_library | 0.9 | False | duplicate_id:SIG-001125 | Rejected |
| CAND-12A8896C1572 | business_signal_library | 0.92 | False | duplicate_id:SIG-001129 | Rejected |
| CAND-86A88A945BB5 | business_signal_library | 0.92 | False | duplicate_id:SIG-001126 | Rejected |
| CAND-7E4BAF35DCAE | business_signal_library | 0.9 | False | duplicate_id:SIG-001128 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001127` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
