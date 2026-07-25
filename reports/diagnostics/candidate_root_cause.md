# Candidate Root Cause

**Generated:** 2026-07-25T11:36:25+00:00
**Session:** `SESSION-20260725-EE5C3E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000835`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260725-EE5C3E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000835': 1, 'duplicate_id:SIG-000837': 1, 'duplicate_id:SIG-000838': 1, 'duplicate_id:SIG-000839': 1, 'duplicate_id:SIG-000836': 1}`
- `candidate CAND-D53DDDA1A510 entity_id=SIG-000835 reason=duplicate_id:SIG-000835 conf=0.9`
- `candidate CAND-EC84A08FE90F entity_id=SIG-000837 reason=duplicate_id:SIG-000837 conf=0.88`
- `candidate CAND-51E08EFC9DB3 entity_id=SIG-000838 reason=duplicate_id:SIG-000838 conf=0.9`
- `candidate CAND-740673B86969 entity_id=SIG-000839 reason=duplicate_id:SIG-000839 conf=0.92`
- `candidate CAND-697EC003427E entity_id=SIG-000836 reason=duplicate_id:SIG-000836 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D53DDDA1A510 | business_signal_library | 0.9 | False | duplicate_id:SIG-000835 | Rejected |
| CAND-EC84A08FE90F | business_signal_library | 0.88 | False | duplicate_id:SIG-000837 | Rejected |
| CAND-51E08EFC9DB3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000838 | Rejected |
| CAND-740673B86969 | business_signal_library | 0.92 | False | duplicate_id:SIG-000839 | Rejected |
| CAND-697EC003427E | business_signal_library | 0.92 | False | duplicate_id:SIG-000836 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000835` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
