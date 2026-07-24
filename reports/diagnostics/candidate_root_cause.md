# Candidate Root Cause

**Generated:** 2026-07-24T20:44:23+00:00
**Session:** `SESSION-20260724-E1C5D4`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000803`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260724-E1C5D4`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000803': 1, 'duplicate_id:SIG-000800': 1, 'duplicate_id:SIG-000804': 1, 'duplicate_id:SIG-000802': 1, 'duplicate_id:SIG-000801': 1}`
- `candidate CAND-98FBB998BA73 entity_id=SIG-000803 reason=duplicate_id:SIG-000803 conf=0.9`
- `candidate CAND-A86A926433FD entity_id=SIG-000800 reason=duplicate_id:SIG-000800 conf=0.9`
- `candidate CAND-DEB7D30E35F6 entity_id=SIG-000804 reason=duplicate_id:SIG-000804 conf=0.92`
- `candidate CAND-557B5BDE109C entity_id=SIG-000802 reason=duplicate_id:SIG-000802 conf=0.88`
- `candidate CAND-E3DF63E1D8B9 entity_id=SIG-000801 reason=duplicate_id:SIG-000801 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-98FBB998BA73 | business_signal_library | 0.9 | False | duplicate_id:SIG-000803 | Rejected |
| CAND-A86A926433FD | business_signal_library | 0.9 | False | duplicate_id:SIG-000800 | Rejected |
| CAND-DEB7D30E35F6 | business_signal_library | 0.92 | False | duplicate_id:SIG-000804 | Rejected |
| CAND-557B5BDE109C | business_signal_library | 0.88 | False | duplicate_id:SIG-000802 | Rejected |
| CAND-E3DF63E1D8B9 | business_signal_library | 0.92 | False | duplicate_id:SIG-000801 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000803` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
