# Candidate Root Cause

**Generated:** 2026-08-19T04:07:39+00:00
**Session:** `SESSION-20260819-E6E122`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000630`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-E6E122`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000630': 1, 'duplicate_id:SIG-000627': 1, 'duplicate_id:SIG-000628': 1, 'duplicate_id:SIG-000629': 1, 'duplicate_id:SIG-000626': 1}`
- `candidate CAND-19869B9201AE entity_id=SIG-000630 reason=duplicate_id:SIG-000630 conf=0.9`
- `candidate CAND-8DE01918E869 entity_id=SIG-000627 reason=duplicate_id:SIG-000627 conf=0.9`
- `candidate CAND-1C14E19638F3 entity_id=SIG-000628 reason=duplicate_id:SIG-000628 conf=0.9`
- `candidate CAND-6128F9526514 entity_id=SIG-000629 reason=duplicate_id:SIG-000629 conf=0.9`
- `candidate CAND-7AFE279A4129 entity_id=SIG-000626 reason=duplicate_id:SIG-000626 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-19869B9201AE | business_signal_library | 0.9 | False | duplicate_id:SIG-000630 | Rejected |
| CAND-8DE01918E869 | business_signal_library | 0.9 | False | duplicate_id:SIG-000627 | Rejected |
| CAND-1C14E19638F3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000628 | Rejected |
| CAND-6128F9526514 | business_signal_library | 0.9 | False | duplicate_id:SIG-000629 | Rejected |
| CAND-7AFE279A4129 | business_signal_library | 0.92 | False | duplicate_id:SIG-000626 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000630` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
