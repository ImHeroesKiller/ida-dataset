# Candidate Root Cause

**Generated:** 2026-07-17T04:28:00+00:00
**Session:** `SESSION-20260717-E6744F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000354`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260717-E6744F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000354': 1, 'duplicate_id:SIG-000350': 1, 'duplicate_id:SIG-000353': 1, 'duplicate_id:SIG-000351': 1, 'duplicate_id:SIG-000352': 1}`
- `candidate CAND-A30DC3F2212D entity_id=SIG-000354 reason=duplicate_id:SIG-000354 conf=0.88`
- `candidate CAND-119F638DF0A7 entity_id=SIG-000350 reason=duplicate_id:SIG-000350 conf=0.9`
- `candidate CAND-D71DFF3E376A entity_id=SIG-000353 reason=duplicate_id:SIG-000353 conf=0.9`
- `candidate CAND-E13B13782F7A entity_id=SIG-000351 reason=duplicate_id:SIG-000351 conf=0.88`
- `candidate CAND-2868F8C0DE7B entity_id=SIG-000352 reason=duplicate_id:SIG-000352 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A30DC3F2212D | business_signal_library | 0.88 | False | duplicate_id:SIG-000354 | Rejected |
| CAND-119F638DF0A7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000350 | Rejected |
| CAND-D71DFF3E376A | business_signal_library | 0.9 | False | duplicate_id:SIG-000353 | Rejected |
| CAND-E13B13782F7A | business_signal_library | 0.88 | False | duplicate_id:SIG-000351 | Rejected |
| CAND-2868F8C0DE7B | business_signal_library | 0.92 | False | duplicate_id:SIG-000352 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000354` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
