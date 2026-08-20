# Candidate Root Cause

**Generated:** 2026-08-20T13:10:13+00:00
**Session:** `SESSION-20260820-CF0EF8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000786`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-CF0EF8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000786': 1, 'duplicate_id:SIG-000789': 1, 'duplicate_id:SIG-000788': 1, 'duplicate_id:SIG-000790': 1, 'duplicate_id:SIG-000787': 1}`
- `candidate CAND-5E4F40E40100 entity_id=SIG-000786 reason=duplicate_id:SIG-000786 conf=0.92`
- `candidate CAND-9C4B78A88B58 entity_id=SIG-000789 reason=duplicate_id:SIG-000789 conf=0.9`
- `candidate CAND-F2B8B1F709E7 entity_id=SIG-000788 reason=duplicate_id:SIG-000788 conf=0.9`
- `candidate CAND-0273446AAE50 entity_id=SIG-000790 reason=duplicate_id:SIG-000790 conf=0.9`
- `candidate CAND-1FE8693D23BA entity_id=SIG-000787 reason=duplicate_id:SIG-000787 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5E4F40E40100 | business_signal_library | 0.92 | False | duplicate_id:SIG-000786 | Rejected |
| CAND-9C4B78A88B58 | business_signal_library | 0.9 | False | duplicate_id:SIG-000789 | Rejected |
| CAND-F2B8B1F709E7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000788 | Rejected |
| CAND-0273446AAE50 | business_signal_library | 0.9 | False | duplicate_id:SIG-000790 | Rejected |
| CAND-1FE8693D23BA | business_signal_library | 0.9 | False | duplicate_id:SIG-000787 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000786` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
