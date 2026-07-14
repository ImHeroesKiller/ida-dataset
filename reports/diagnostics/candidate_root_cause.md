# Candidate Root Cause

**Generated:** 2026-07-14T08:30:25+00:00
**Session:** `SESSION-20260714-44B6AA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000193`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260714-44B6AA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000193': 1, 'duplicate_id:SIG-000194': 1, 'duplicate_id:SIG-000192': 1, 'duplicate_id:SIG-000190': 1, 'duplicate_id:SIG-000191': 1}`
- `candidate CAND-83AB144D8A36 entity_id=SIG-000193 reason=duplicate_id:SIG-000193 conf=0.85`
- `candidate CAND-99B9C198D907 entity_id=SIG-000194 reason=duplicate_id:SIG-000194 conf=0.9`
- `candidate CAND-A12FE9F04895 entity_id=SIG-000192 reason=duplicate_id:SIG-000192 conf=0.92`
- `candidate CAND-A86881EB3F00 entity_id=SIG-000190 reason=duplicate_id:SIG-000190 conf=0.9`
- `candidate CAND-5CED4DEC7D21 entity_id=SIG-000191 reason=duplicate_id:SIG-000191 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-83AB144D8A36 | business_signal_library | 0.85 | False | duplicate_id:SIG-000193 | Rejected |
| CAND-99B9C198D907 | business_signal_library | 0.9 | False | duplicate_id:SIG-000194 | Rejected |
| CAND-A12FE9F04895 | business_signal_library | 0.92 | False | duplicate_id:SIG-000192 | Rejected |
| CAND-A86881EB3F00 | business_signal_library | 0.9 | False | duplicate_id:SIG-000190 | Rejected |
| CAND-5CED4DEC7D21 | business_signal_library | 0.88 | False | duplicate_id:SIG-000191 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000193` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
