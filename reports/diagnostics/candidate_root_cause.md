# Candidate Root Cause

**Generated:** 2026-07-19T14:05:58+00:00
**Session:** `SESSION-20260719-DE79D3`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000505`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260719-DE79D3`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000505': 1, 'duplicate_id:SIG-000506': 1, 'duplicate_id:SIG-000508': 1, 'duplicate_id:SIG-000509': 1, 'duplicate_id:SIG-000507': 1}`
- `candidate CAND-A476E3F9EE84 entity_id=SIG-000505 reason=duplicate_id:SIG-000505 conf=0.9`
- `candidate CAND-AF16021D6EDA entity_id=SIG-000506 reason=duplicate_id:SIG-000506 conf=0.92`
- `candidate CAND-F83063C02249 entity_id=SIG-000508 reason=duplicate_id:SIG-000508 conf=0.9`
- `candidate CAND-953F121DE47F entity_id=SIG-000509 reason=duplicate_id:SIG-000509 conf=0.92`
- `candidate CAND-2BD17A0F64E3 entity_id=SIG-000507 reason=duplicate_id:SIG-000507 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A476E3F9EE84 | business_signal_library | 0.9 | False | duplicate_id:SIG-000505 | Rejected |
| CAND-AF16021D6EDA | business_signal_library | 0.92 | False | duplicate_id:SIG-000506 | Rejected |
| CAND-F83063C02249 | business_signal_library | 0.9 | False | duplicate_id:SIG-000508 | Rejected |
| CAND-953F121DE47F | business_signal_library | 0.92 | False | duplicate_id:SIG-000509 | Rejected |
| CAND-2BD17A0F64E3 | business_signal_library | 0.88 | False | duplicate_id:SIG-000507 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000505` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
