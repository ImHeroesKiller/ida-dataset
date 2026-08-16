# Candidate Root Cause

**Generated:** 2026-08-16T06:55:49+00:00
**Session:** `SESSION-20260816-5E2619`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000302`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-5E2619`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000302': 1, 'duplicate_id:SIG-000304': 1, 'duplicate_id:SIG-000301': 1, 'duplicate_id:SIG-000305': 1, 'duplicate_id:SIG-000303': 1}`
- `candidate CAND-EB21F85DE178 entity_id=SIG-000302 reason=duplicate_id:SIG-000302 conf=0.9`
- `candidate CAND-9BA03CFCD4F2 entity_id=SIG-000304 reason=duplicate_id:SIG-000304 conf=0.9`
- `candidate CAND-7775F30F43CE entity_id=SIG-000301 reason=duplicate_id:SIG-000301 conf=0.92`
- `candidate CAND-0FA6A769843E entity_id=SIG-000305 reason=duplicate_id:SIG-000305 conf=0.9`
- `candidate CAND-682799A4AE72 entity_id=SIG-000303 reason=duplicate_id:SIG-000303 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-EB21F85DE178 | business_signal_library | 0.9 | False | duplicate_id:SIG-000302 | Rejected |
| CAND-9BA03CFCD4F2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000304 | Rejected |
| CAND-7775F30F43CE | business_signal_library | 0.92 | False | duplicate_id:SIG-000301 | Rejected |
| CAND-0FA6A769843E | business_signal_library | 0.9 | False | duplicate_id:SIG-000305 | Rejected |
| CAND-682799A4AE72 | business_signal_library | 0.9 | False | duplicate_id:SIG-000303 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000302` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
