# Candidate Root Cause

**Generated:** 2026-07-13T13:45:09+00:00
**Session:** `SESSION-20260713-A895CA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000161`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260713-A895CA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000161': 1, 'duplicate_id:SIG-000164': 1, 'duplicate_id:SIG-000160': 1, 'duplicate_id:SIG-000163': 1, 'duplicate_id:SIG-000162': 1}`
- `candidate CAND-F506A22E6A15 entity_id=SIG-000161 reason=duplicate_id:SIG-000161 conf=0.92`
- `candidate CAND-71206E4BDC33 entity_id=SIG-000164 reason=duplicate_id:SIG-000164 conf=0.92`
- `candidate CAND-04C8722B440C entity_id=SIG-000160 reason=duplicate_id:SIG-000160 conf=0.9`
- `candidate CAND-DB5683E3C3C2 entity_id=SIG-000163 reason=duplicate_id:SIG-000163 conf=0.9`
- `candidate CAND-CAC48C02E0C4 entity_id=SIG-000162 reason=duplicate_id:SIG-000162 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F506A22E6A15 | business_signal_library | 0.92 | False | duplicate_id:SIG-000161 | Rejected |
| CAND-71206E4BDC33 | business_signal_library | 0.92 | False | duplicate_id:SIG-000164 | Rejected |
| CAND-04C8722B440C | business_signal_library | 0.9 | False | duplicate_id:SIG-000160 | Rejected |
| CAND-DB5683E3C3C2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000163 | Rejected |
| CAND-CAC48C02E0C4 | business_signal_library | 0.88 | False | duplicate_id:SIG-000162 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000161` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
