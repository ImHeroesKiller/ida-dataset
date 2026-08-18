# Candidate Root Cause

**Generated:** 2026-08-18T16:43:35+00:00
**Session:** `SESSION-20260818-227F02`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000576`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-227F02`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000576': 1, 'duplicate_id:SIG-000577': 1, 'duplicate_id:SIG-000580': 1, 'duplicate_id:SIG-000579': 1, 'duplicate_id:SIG-000578': 1}`
- `candidate CAND-959FEFA15B8A entity_id=SIG-000576 reason=duplicate_id:SIG-000576 conf=0.92`
- `candidate CAND-E39840BC3482 entity_id=SIG-000577 reason=duplicate_id:SIG-000577 conf=0.9`
- `candidate CAND-AABC6F2E965C entity_id=SIG-000580 reason=duplicate_id:SIG-000580 conf=0.9`
- `candidate CAND-C0439A294DBF entity_id=SIG-000579 reason=duplicate_id:SIG-000579 conf=0.9`
- `candidate CAND-F970346FF906 entity_id=SIG-000578 reason=duplicate_id:SIG-000578 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-959FEFA15B8A | business_signal_library | 0.92 | False | duplicate_id:SIG-000576 | Rejected |
| CAND-E39840BC3482 | business_signal_library | 0.9 | False | duplicate_id:SIG-000577 | Rejected |
| CAND-AABC6F2E965C | business_signal_library | 0.9 | False | duplicate_id:SIG-000580 | Rejected |
| CAND-C0439A294DBF | business_signal_library | 0.9 | False | duplicate_id:SIG-000579 | Rejected |
| CAND-F970346FF906 | business_signal_library | 0.9 | False | duplicate_id:SIG-000578 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000576` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
