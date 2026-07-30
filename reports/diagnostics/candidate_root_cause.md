# Candidate Root Cause

**Generated:** 2026-07-30T04:17:00+00:00
**Session:** `SESSION-20260730-FD283B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001083`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260730-FD283B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001083': 1, 'duplicate_id:SIG-001082': 1, 'duplicate_id:SIG-001080': 1, 'duplicate_id:SIG-001081': 1, 'duplicate_id:SIG-001084': 1}`
- `candidate CAND-95E0B1AE0822 entity_id=SIG-001083 reason=duplicate_id:SIG-001083 conf=0.9`
- `candidate CAND-4B55EE94475D entity_id=SIG-001082 reason=duplicate_id:SIG-001082 conf=0.88`
- `candidate CAND-5547F0DAB831 entity_id=SIG-001080 reason=duplicate_id:SIG-001080 conf=0.9`
- `candidate CAND-7117FE436E68 entity_id=SIG-001081 reason=duplicate_id:SIG-001081 conf=0.92`
- `candidate CAND-16FA184C7C77 entity_id=SIG-001084 reason=duplicate_id:SIG-001084 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-95E0B1AE0822 | business_signal_library | 0.9 | False | duplicate_id:SIG-001083 | Rejected |
| CAND-4B55EE94475D | business_signal_library | 0.88 | False | duplicate_id:SIG-001082 | Rejected |
| CAND-5547F0DAB831 | business_signal_library | 0.9 | False | duplicate_id:SIG-001080 | Rejected |
| CAND-7117FE436E68 | business_signal_library | 0.92 | False | duplicate_id:SIG-001081 | Rejected |
| CAND-16FA184C7C77 | business_signal_library | 0.92 | False | duplicate_id:SIG-001084 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001083` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
