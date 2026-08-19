# Candidate Root Cause

**Generated:** 2026-08-19T17:47:36+00:00
**Session:** `SESSION-20260819-857487`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000696`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-857487`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000696': 1, 'duplicate_id:SIG-000697': 1, 'duplicate_id:SIG-000698': 1, 'duplicate_id:SIG-000700': 1, 'duplicate_id:SIG-000699': 1}`
- `candidate CAND-3215D7EB271D entity_id=SIG-000696 reason=duplicate_id:SIG-000696 conf=0.92`
- `candidate CAND-E07DE23E943A entity_id=SIG-000697 reason=duplicate_id:SIG-000697 conf=0.9`
- `candidate CAND-C43DCD0DDB7B entity_id=SIG-000698 reason=duplicate_id:SIG-000698 conf=0.9`
- `candidate CAND-9680120AEFD2 entity_id=SIG-000700 reason=duplicate_id:SIG-000700 conf=0.9`
- `candidate CAND-6226A60734EC entity_id=SIG-000699 reason=duplicate_id:SIG-000699 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3215D7EB271D | business_signal_library | 0.92 | False | duplicate_id:SIG-000696 | Rejected |
| CAND-E07DE23E943A | business_signal_library | 0.9 | False | duplicate_id:SIG-000697 | Rejected |
| CAND-C43DCD0DDB7B | business_signal_library | 0.9 | False | duplicate_id:SIG-000698 | Rejected |
| CAND-9680120AEFD2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000700 | Rejected |
| CAND-6226A60734EC | business_signal_library | 0.9 | False | duplicate_id:SIG-000699 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000696` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
