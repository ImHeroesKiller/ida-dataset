# Candidate Root Cause

**Generated:** 2026-08-20T22:48:04+00:00
**Session:** `SESSION-20260820-43265B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000836`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-43265B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000836': 1, 'duplicate_id:SIG-000839': 1, 'duplicate_id:SIG-000838': 1, 'duplicate_id:SIG-000840': 1, 'duplicate_id:SIG-000837': 1}`
- `candidate CAND-C48293109783 entity_id=SIG-000836 reason=duplicate_id:SIG-000836 conf=0.92`
- `candidate CAND-51EC3278D163 entity_id=SIG-000839 reason=duplicate_id:SIG-000839 conf=0.9`
- `candidate CAND-22D90A9C0C1E entity_id=SIG-000838 reason=duplicate_id:SIG-000838 conf=0.9`
- `candidate CAND-C254B1AB1F9F entity_id=SIG-000840 reason=duplicate_id:SIG-000840 conf=0.9`
- `candidate CAND-BF7083339D65 entity_id=SIG-000837 reason=duplicate_id:SIG-000837 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C48293109783 | business_signal_library | 0.92 | False | duplicate_id:SIG-000836 | Rejected |
| CAND-51EC3278D163 | business_signal_library | 0.9 | False | duplicate_id:SIG-000839 | Rejected |
| CAND-22D90A9C0C1E | business_signal_library | 0.9 | False | duplicate_id:SIG-000838 | Rejected |
| CAND-C254B1AB1F9F | business_signal_library | 0.9 | False | duplicate_id:SIG-000840 | Rejected |
| CAND-BF7083339D65 | business_signal_library | 0.9 | False | duplicate_id:SIG-000837 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000836` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
