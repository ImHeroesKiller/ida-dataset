# Candidate Root Cause

**Generated:** 2026-08-19T16:52:15+00:00
**Session:** `SESSION-20260819-47C28F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000694`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-47C28F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000694': 1, 'duplicate_id:SIG-000695': 1, 'duplicate_id:SIG-000691': 1, 'duplicate_id:SIG-000692': 1, 'duplicate_id:SIG-000693': 1}`
- `candidate CAND-0FC6CB6E6A22 entity_id=SIG-000694 reason=duplicate_id:SIG-000694 conf=0.9`
- `candidate CAND-DC024AF70361 entity_id=SIG-000695 reason=duplicate_id:SIG-000695 conf=0.9`
- `candidate CAND-091D4F5097E6 entity_id=SIG-000691 reason=duplicate_id:SIG-000691 conf=0.92`
- `candidate CAND-BA4EEE593B04 entity_id=SIG-000692 reason=duplicate_id:SIG-000692 conf=0.9`
- `candidate CAND-6773EC1FF777 entity_id=SIG-000693 reason=duplicate_id:SIG-000693 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0FC6CB6E6A22 | business_signal_library | 0.9 | False | duplicate_id:SIG-000694 | Rejected |
| CAND-DC024AF70361 | business_signal_library | 0.9 | False | duplicate_id:SIG-000695 | Rejected |
| CAND-091D4F5097E6 | business_signal_library | 0.92 | False | duplicate_id:SIG-000691 | Rejected |
| CAND-BA4EEE593B04 | business_signal_library | 0.9 | False | duplicate_id:SIG-000692 | Rejected |
| CAND-6773EC1FF777 | business_signal_library | 0.9 | False | duplicate_id:SIG-000693 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000694` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
