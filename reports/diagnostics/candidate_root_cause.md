# Candidate Root Cause

**Generated:** 2026-08-20T07:07:23+00:00
**Session:** `SESSION-20260820-4C5085`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000760`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-4C5085`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000760': 1, 'duplicate_id:SIG-000759': 1, 'duplicate_id:SIG-000757': 1, 'duplicate_id:SIG-000756': 1, 'duplicate_id:SIG-000758': 1}`
- `candidate CAND-D95306EA2F69 entity_id=SIG-000760 reason=duplicate_id:SIG-000760 conf=0.9`
- `candidate CAND-8F39FF073FF4 entity_id=SIG-000759 reason=duplicate_id:SIG-000759 conf=0.9`
- `candidate CAND-1E932FA99338 entity_id=SIG-000757 reason=duplicate_id:SIG-000757 conf=0.9`
- `candidate CAND-129215F45395 entity_id=SIG-000756 reason=duplicate_id:SIG-000756 conf=0.92`
- `candidate CAND-4312D14BA0DE entity_id=SIG-000758 reason=duplicate_id:SIG-000758 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D95306EA2F69 | business_signal_library | 0.9 | False | duplicate_id:SIG-000760 | Rejected |
| CAND-8F39FF073FF4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000759 | Rejected |
| CAND-1E932FA99338 | business_signal_library | 0.9 | False | duplicate_id:SIG-000757 | Rejected |
| CAND-129215F45395 | business_signal_library | 0.92 | False | duplicate_id:SIG-000756 | Rejected |
| CAND-4312D14BA0DE | business_signal_library | 0.9 | False | duplicate_id:SIG-000758 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000760` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
