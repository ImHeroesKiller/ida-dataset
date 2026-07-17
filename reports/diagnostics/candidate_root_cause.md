# Candidate Root Cause

**Generated:** 2026-07-17T22:18:51+00:00
**Session:** `SESSION-20260717-C19B96`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000402`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260717-C19B96`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000402': 1, 'duplicate_id:SIG-000404': 1, 'duplicate_id:SIG-000403': 1, 'duplicate_id:SIG-000400': 1, 'duplicate_id:SIG-000401': 1}`
- `candidate CAND-DD9E09C76D0C entity_id=SIG-000402 reason=duplicate_id:SIG-000402 conf=0.88`
- `candidate CAND-6C374DA6CA3E entity_id=SIG-000404 reason=duplicate_id:SIG-000404 conf=0.92`
- `candidate CAND-F60D0AE64828 entity_id=SIG-000403 reason=duplicate_id:SIG-000403 conf=0.9`
- `candidate CAND-E384340A9097 entity_id=SIG-000400 reason=duplicate_id:SIG-000400 conf=0.9`
- `candidate CAND-94789E909F53 entity_id=SIG-000401 reason=duplicate_id:SIG-000401 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DD9E09C76D0C | business_signal_library | 0.88 | False | duplicate_id:SIG-000402 | Rejected |
| CAND-6C374DA6CA3E | business_signal_library | 0.92 | False | duplicate_id:SIG-000404 | Rejected |
| CAND-F60D0AE64828 | business_signal_library | 0.9 | False | duplicate_id:SIG-000403 | Rejected |
| CAND-E384340A9097 | business_signal_library | 0.9 | False | duplicate_id:SIG-000400 | Rejected |
| CAND-94789E909F53 | business_signal_library | 0.92 | False | duplicate_id:SIG-000401 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000402` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
