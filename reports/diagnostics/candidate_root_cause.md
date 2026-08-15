# Candidate Root Cause

**Generated:** 2026-08-15T23:35:07+00:00
**Session:** `SESSION-20260815-B91A9F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000280`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-B91A9F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000280': 1, 'duplicate_id:SIG-000279': 1, 'duplicate_id:SIG-000278': 1, 'duplicate_id:SIG-000276': 1, 'duplicate_id:SIG-000277': 1}`
- `candidate CAND-918D8F4B01E7 entity_id=SIG-000280 reason=duplicate_id:SIG-000280 conf=0.9`
- `candidate CAND-368C0A43F0B8 entity_id=SIG-000279 reason=duplicate_id:SIG-000279 conf=0.9`
- `candidate CAND-EAED15573BC9 entity_id=SIG-000278 reason=duplicate_id:SIG-000278 conf=0.9`
- `candidate CAND-74E4D8703D76 entity_id=SIG-000276 reason=duplicate_id:SIG-000276 conf=0.92`
- `candidate CAND-3D02E50BE94F entity_id=SIG-000277 reason=duplicate_id:SIG-000277 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-918D8F4B01E7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000280 | Rejected |
| CAND-368C0A43F0B8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000279 | Rejected |
| CAND-EAED15573BC9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000278 | Rejected |
| CAND-74E4D8703D76 | business_signal_library | 0.92 | False | duplicate_id:SIG-000276 | Rejected |
| CAND-3D02E50BE94F | business_signal_library | 0.9 | False | duplicate_id:SIG-000277 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000280` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
