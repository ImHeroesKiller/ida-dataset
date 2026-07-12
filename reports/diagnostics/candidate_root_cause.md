# Candidate Root Cause

**Generated:** 2026-07-12T06:54:49+00:00
**Session:** `SESSION-20260712-878E73`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000082`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260712-878E73`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000082': 1, 'duplicate_id:SIG-000083': 1, 'duplicate_id:SIG-000081': 1, 'duplicate_id:SIG-000080': 1, 'duplicate_id:SIG-000084': 1}`
- `candidate CAND-B01FF3661621 entity_id=SIG-000082 reason=duplicate_id:SIG-000082 conf=0.88`
- `candidate CAND-DBA61E770828 entity_id=SIG-000083 reason=duplicate_id:SIG-000083 conf=0.9`
- `candidate CAND-3E27E3F8FA68 entity_id=SIG-000081 reason=duplicate_id:SIG-000081 conf=0.92`
- `candidate CAND-1B872BD3F954 entity_id=SIG-000080 reason=duplicate_id:SIG-000080 conf=0.9`
- `candidate CAND-9FE40C8ECC48 entity_id=SIG-000084 reason=duplicate_id:SIG-000084 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B01FF3661621 | business_signal_library | 0.88 | False | duplicate_id:SIG-000082 | Rejected |
| CAND-DBA61E770828 | business_signal_library | 0.9 | False | duplicate_id:SIG-000083 | Rejected |
| CAND-3E27E3F8FA68 | business_signal_library | 0.92 | False | duplicate_id:SIG-000081 | Rejected |
| CAND-1B872BD3F954 | business_signal_library | 0.9 | False | duplicate_id:SIG-000080 | Rejected |
| CAND-9FE40C8ECC48 | business_signal_library | 0.92 | False | duplicate_id:SIG-000084 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000082` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
