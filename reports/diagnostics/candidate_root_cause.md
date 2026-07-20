# Candidate Root Cause

**Generated:** 2026-07-20T20:41:09+00:00
**Session:** `SESSION-20260720-AB7A57`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000586`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260720-AB7A57`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000586': 1, 'duplicate_id:SIG-000589': 1, 'duplicate_id:SIG-000588': 1, 'duplicate_id:SIG-000587': 1, 'duplicate_id:SIG-000585': 1}`
- `candidate CAND-64C5597AAF3F entity_id=SIG-000586 reason=duplicate_id:SIG-000586 conf=0.92`
- `candidate CAND-FB2746CADD61 entity_id=SIG-000589 reason=duplicate_id:SIG-000589 conf=0.92`
- `candidate CAND-FF12F3FA61F9 entity_id=SIG-000588 reason=duplicate_id:SIG-000588 conf=0.9`
- `candidate CAND-929405BD5BDC entity_id=SIG-000587 reason=duplicate_id:SIG-000587 conf=0.88`
- `candidate CAND-C2E9337BAB97 entity_id=SIG-000585 reason=duplicate_id:SIG-000585 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-64C5597AAF3F | business_signal_library | 0.92 | False | duplicate_id:SIG-000586 | Rejected |
| CAND-FB2746CADD61 | business_signal_library | 0.92 | False | duplicate_id:SIG-000589 | Rejected |
| CAND-FF12F3FA61F9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000588 | Rejected |
| CAND-929405BD5BDC | business_signal_library | 0.88 | False | duplicate_id:SIG-000587 | Rejected |
| CAND-C2E9337BAB97 | business_signal_library | 0.9 | False | duplicate_id:SIG-000585 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000586` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
