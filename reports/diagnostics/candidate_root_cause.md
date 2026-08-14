# Candidate Root Cause

**Generated:** 2026-08-14T20:46:11+00:00
**Session:** `SESSION-20260814-8A298D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000148`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-8A298D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000148': 1, 'duplicate_id:SIG-000146': 1, 'duplicate_id:SIG-000149': 1, 'duplicate_id:SIG-000150': 1, 'duplicate_id:SIG-000147': 1}`
- `candidate CAND-4001BAB87189 entity_id=SIG-000148 reason=duplicate_id:SIG-000148 conf=0.9`
- `candidate CAND-3C6A6D4B0BE8 entity_id=SIG-000146 reason=duplicate_id:SIG-000146 conf=0.92`
- `candidate CAND-3A29092154A5 entity_id=SIG-000149 reason=duplicate_id:SIG-000149 conf=0.9`
- `candidate CAND-AE53CA4C8F31 entity_id=SIG-000150 reason=duplicate_id:SIG-000150 conf=0.9`
- `candidate CAND-3108069C3A26 entity_id=SIG-000147 reason=duplicate_id:SIG-000147 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4001BAB87189 | business_signal_library | 0.9 | False | duplicate_id:SIG-000148 | Rejected |
| CAND-3C6A6D4B0BE8 | business_signal_library | 0.92 | False | duplicate_id:SIG-000146 | Rejected |
| CAND-3A29092154A5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000149 | Rejected |
| CAND-AE53CA4C8F31 | business_signal_library | 0.9 | False | duplicate_id:SIG-000150 | Rejected |
| CAND-3108069C3A26 | business_signal_library | 0.9 | False | duplicate_id:SIG-000147 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000148` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
