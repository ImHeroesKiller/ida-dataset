# Candidate Root Cause

**Generated:** 2026-08-19T08:58:03+00:00
**Session:** `SESSION-20260819-05D02D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000653`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-05D02D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000653': 1, 'duplicate_id:SIG-000652': 1, 'duplicate_id:SIG-000655': 1, 'duplicate_id:SIG-000654': 1, 'duplicate_id:SIG-000651': 1}`
- `candidate CAND-2FB063AC2CFB entity_id=SIG-000653 reason=duplicate_id:SIG-000653 conf=0.9`
- `candidate CAND-9FA59F41601F entity_id=SIG-000652 reason=duplicate_id:SIG-000652 conf=0.9`
- `candidate CAND-4D7C73DC9A1A entity_id=SIG-000655 reason=duplicate_id:SIG-000655 conf=0.9`
- `candidate CAND-A15824E2552C entity_id=SIG-000654 reason=duplicate_id:SIG-000654 conf=0.9`
- `candidate CAND-0E5C8630C4F3 entity_id=SIG-000651 reason=duplicate_id:SIG-000651 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2FB063AC2CFB | business_signal_library | 0.9 | False | duplicate_id:SIG-000653 | Rejected |
| CAND-9FA59F41601F | business_signal_library | 0.9 | False | duplicate_id:SIG-000652 | Rejected |
| CAND-4D7C73DC9A1A | business_signal_library | 0.9 | False | duplicate_id:SIG-000655 | Rejected |
| CAND-A15824E2552C | business_signal_library | 0.9 | False | duplicate_id:SIG-000654 | Rejected |
| CAND-0E5C8630C4F3 | business_signal_library | 0.92 | False | duplicate_id:SIG-000651 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000653` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
