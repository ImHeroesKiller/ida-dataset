# Candidate Root Cause

**Generated:** 2026-07-25T00:28:49+00:00
**Session:** `SESSION-20260725-824FFE`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000811`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260725-824FFE`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000811': 1, 'duplicate_id:SIG-000810': 1, 'duplicate_id:SIG-000813': 1, 'duplicate_id:SIG-000814': 1, 'duplicate_id:SIG-000812': 1}`
- `candidate CAND-11FBC1B3808A entity_id=SIG-000811 reason=duplicate_id:SIG-000811 conf=0.92`
- `candidate CAND-586058878DEC entity_id=SIG-000810 reason=duplicate_id:SIG-000810 conf=0.9`
- `candidate CAND-CBC33889E529 entity_id=SIG-000813 reason=duplicate_id:SIG-000813 conf=0.9`
- `candidate CAND-2F1E4FBB61FC entity_id=SIG-000814 reason=duplicate_id:SIG-000814 conf=0.92`
- `candidate CAND-EEBF1CA3A5F5 entity_id=SIG-000812 reason=duplicate_id:SIG-000812 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-11FBC1B3808A | business_signal_library | 0.92 | False | duplicate_id:SIG-000811 | Rejected |
| CAND-586058878DEC | business_signal_library | 0.9 | False | duplicate_id:SIG-000810 | Rejected |
| CAND-CBC33889E529 | business_signal_library | 0.9 | False | duplicate_id:SIG-000813 | Rejected |
| CAND-2F1E4FBB61FC | business_signal_library | 0.92 | False | duplicate_id:SIG-000814 | Rejected |
| CAND-EEBF1CA3A5F5 | business_signal_library | 0.88 | False | duplicate_id:SIG-000812 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000811` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
