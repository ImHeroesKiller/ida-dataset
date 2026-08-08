# Candidate Root Cause

**Generated:** 2026-08-08T13:09:25+00:00
**Session:** `SESSION-20260808-D544DF`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001617`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-D544DF`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001617': 1, 'duplicate_id:SIG-001618': 1, 'duplicate_id:SIG-001616': 1, 'duplicate_id:SIG-001615': 1, 'duplicate_id:SIG-001619': 1}`
- `candidate CAND-B9312C706295 entity_id=SIG-001617 reason=duplicate_id:SIG-001617 conf=0.88`
- `candidate CAND-A746275E5DDD entity_id=SIG-001618 reason=duplicate_id:SIG-001618 conf=0.9`
- `candidate CAND-CE0F2F664786 entity_id=SIG-001616 reason=duplicate_id:SIG-001616 conf=0.92`
- `candidate CAND-62BCE049BFEC entity_id=SIG-001615 reason=duplicate_id:SIG-001615 conf=0.9`
- `candidate CAND-9F52E6140531 entity_id=SIG-001619 reason=duplicate_id:SIG-001619 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B9312C706295 | business_signal_library | 0.88 | False | duplicate_id:SIG-001617 | Rejected |
| CAND-A746275E5DDD | business_signal_library | 0.9 | False | duplicate_id:SIG-001618 | Rejected |
| CAND-CE0F2F664786 | business_signal_library | 0.92 | False | duplicate_id:SIG-001616 | Rejected |
| CAND-62BCE049BFEC | business_signal_library | 0.9 | False | duplicate_id:SIG-001615 | Rejected |
| CAND-9F52E6140531 | business_signal_library | 0.92 | False | duplicate_id:SIG-001619 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001617` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
