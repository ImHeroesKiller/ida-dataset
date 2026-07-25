# Candidate Root Cause

**Generated:** 2026-07-25T08:33:27+00:00
**Session:** `SESSION-20260725-3C181C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000828`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260725-3C181C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000828': 1, 'duplicate_id:SIG-000825': 1, 'duplicate_id:SIG-000829': 1, 'duplicate_id:SIG-000826': 1, 'duplicate_id:SIG-000827': 1}`
- `candidate CAND-9263543014B1 entity_id=SIG-000828 reason=duplicate_id:SIG-000828 conf=0.9`
- `candidate CAND-7F87A94FD502 entity_id=SIG-000825 reason=duplicate_id:SIG-000825 conf=0.9`
- `candidate CAND-5C75B6C917F3 entity_id=SIG-000829 reason=duplicate_id:SIG-000829 conf=0.92`
- `candidate CAND-0650B4D169FE entity_id=SIG-000826 reason=duplicate_id:SIG-000826 conf=0.92`
- `candidate CAND-0663D055BF04 entity_id=SIG-000827 reason=duplicate_id:SIG-000827 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-9263543014B1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000828 | Rejected |
| CAND-7F87A94FD502 | business_signal_library | 0.9 | False | duplicate_id:SIG-000825 | Rejected |
| CAND-5C75B6C917F3 | business_signal_library | 0.92 | False | duplicate_id:SIG-000829 | Rejected |
| CAND-0650B4D169FE | business_signal_library | 0.92 | False | duplicate_id:SIG-000826 | Rejected |
| CAND-0663D055BF04 | business_signal_library | 0.88 | False | duplicate_id:SIG-000827 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000828` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
