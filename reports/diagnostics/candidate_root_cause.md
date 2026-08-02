# Candidate Root Cause

**Generated:** 2026-08-02T21:15:34+00:00
**Session:** `SESSION-20260802-11E7F8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001288`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260802-11E7F8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001288': 1, 'duplicate_id:SIG-001285': 1, 'duplicate_id:SIG-001289': 1, 'duplicate_id:SIG-001287': 1, 'duplicate_id:SIG-001286': 1}`
- `candidate CAND-D9302C322320 entity_id=SIG-001288 reason=duplicate_id:SIG-001288 conf=0.9`
- `candidate CAND-E9677CBEF596 entity_id=SIG-001285 reason=duplicate_id:SIG-001285 conf=0.9`
- `candidate CAND-70B4047D3F43 entity_id=SIG-001289 reason=duplicate_id:SIG-001289 conf=0.92`
- `candidate CAND-FF331A1B2492 entity_id=SIG-001287 reason=duplicate_id:SIG-001287 conf=0.88`
- `candidate CAND-7C9A4B32C22D entity_id=SIG-001286 reason=duplicate_id:SIG-001286 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D9302C322320 | business_signal_library | 0.9 | False | duplicate_id:SIG-001288 | Rejected |
| CAND-E9677CBEF596 | business_signal_library | 0.9 | False | duplicate_id:SIG-001285 | Rejected |
| CAND-70B4047D3F43 | business_signal_library | 0.92 | False | duplicate_id:SIG-001289 | Rejected |
| CAND-FF331A1B2492 | business_signal_library | 0.88 | False | duplicate_id:SIG-001287 | Rejected |
| CAND-7C9A4B32C22D | business_signal_library | 0.92 | False | duplicate_id:SIG-001286 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001288` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
