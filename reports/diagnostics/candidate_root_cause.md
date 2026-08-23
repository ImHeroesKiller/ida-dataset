# Candidate Root Cause

**Generated:** 2026-08-23T14:43:00+00:00
**Session:** `SESSION-20260823-F2D7A9`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001134`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-F2D7A9`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001134': 1, 'duplicate_id:SIG-001133': 1, 'duplicate_id:SIG-001131': 1, 'duplicate_id:SIG-001135': 1, 'duplicate_id:SIG-001132': 1}`
- `candidate CAND-574D6BE7BEDC entity_id=SIG-001134 reason=duplicate_id:SIG-001134 conf=0.9`
- `candidate CAND-F8FDF1C69A08 entity_id=SIG-001133 reason=duplicate_id:SIG-001133 conf=0.9`
- `candidate CAND-EF3EEF08FBEA entity_id=SIG-001131 reason=duplicate_id:SIG-001131 conf=0.92`
- `candidate CAND-51A788830F67 entity_id=SIG-001135 reason=duplicate_id:SIG-001135 conf=0.9`
- `candidate CAND-017F44966819 entity_id=SIG-001132 reason=duplicate_id:SIG-001132 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-574D6BE7BEDC | business_signal_library | 0.9 | False | duplicate_id:SIG-001134 | Rejected |
| CAND-F8FDF1C69A08 | business_signal_library | 0.9 | False | duplicate_id:SIG-001133 | Rejected |
| CAND-EF3EEF08FBEA | business_signal_library | 0.92 | False | duplicate_id:SIG-001131 | Rejected |
| CAND-51A788830F67 | business_signal_library | 0.9 | False | duplicate_id:SIG-001135 | Rejected |
| CAND-017F44966819 | business_signal_library | 0.9 | False | duplicate_id:SIG-001132 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001134` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
