# Candidate Root Cause

**Generated:** 2026-08-16T14:38:47+00:00
**Session:** `SESSION-20260816-F653D7`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000342`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-F653D7`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000342': 1, 'duplicate_id:SIG-000345': 1, 'duplicate_id:SIG-000343': 1, 'duplicate_id:SIG-000341': 1, 'duplicate_id:SIG-000344': 1}`
- `candidate CAND-F9CBCCE9E9B3 entity_id=SIG-000342 reason=duplicate_id:SIG-000342 conf=0.9`
- `candidate CAND-FE71476023C0 entity_id=SIG-000345 reason=duplicate_id:SIG-000345 conf=0.9`
- `candidate CAND-4A113AF4A9F2 entity_id=SIG-000343 reason=duplicate_id:SIG-000343 conf=0.9`
- `candidate CAND-E20EDEE68693 entity_id=SIG-000341 reason=duplicate_id:SIG-000341 conf=0.92`
- `candidate CAND-15D189A74CA2 entity_id=SIG-000344 reason=duplicate_id:SIG-000344 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F9CBCCE9E9B3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000342 | Rejected |
| CAND-FE71476023C0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000345 | Rejected |
| CAND-4A113AF4A9F2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000343 | Rejected |
| CAND-E20EDEE68693 | business_signal_library | 0.92 | False | duplicate_id:SIG-000341 | Rejected |
| CAND-15D189A74CA2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000344 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000342` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
