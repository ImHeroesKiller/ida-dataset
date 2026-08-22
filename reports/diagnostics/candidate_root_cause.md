# Candidate Root Cause

**Generated:** 2026-08-22T21:41:16+00:00
**Session:** `SESSION-20260822-4FF7C0`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001059`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-4FF7C0`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001059': 1, 'duplicate_id:SIG-001060': 1, 'duplicate_id:SIG-001058': 1, 'duplicate_id:SIG-001056': 1, 'duplicate_id:SIG-001057': 1}`
- `candidate CAND-04D64C5F6075 entity_id=SIG-001059 reason=duplicate_id:SIG-001059 conf=0.9`
- `candidate CAND-1D074CECCCBE entity_id=SIG-001060 reason=duplicate_id:SIG-001060 conf=0.9`
- `candidate CAND-025F07416C2E entity_id=SIG-001058 reason=duplicate_id:SIG-001058 conf=0.9`
- `candidate CAND-23BFF505D2F7 entity_id=SIG-001056 reason=duplicate_id:SIG-001056 conf=0.92`
- `candidate CAND-BAD293EE7204 entity_id=SIG-001057 reason=duplicate_id:SIG-001057 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-04D64C5F6075 | business_signal_library | 0.9 | False | duplicate_id:SIG-001059 | Rejected |
| CAND-1D074CECCCBE | business_signal_library | 0.9 | False | duplicate_id:SIG-001060 | Rejected |
| CAND-025F07416C2E | business_signal_library | 0.9 | False | duplicate_id:SIG-001058 | Rejected |
| CAND-23BFF505D2F7 | business_signal_library | 0.92 | False | duplicate_id:SIG-001056 | Rejected |
| CAND-BAD293EE7204 | business_signal_library | 0.9 | False | duplicate_id:SIG-001057 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001059` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
