# Candidate Root Cause

**Generated:** 2026-07-19T22:12:19+00:00
**Session:** `SESSION-20260719-CB4819`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000539`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260719-CB4819`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000539': 1, 'duplicate_id:SIG-000536': 1, 'duplicate_id:SIG-000535': 1, 'duplicate_id:SIG-000538': 1, 'duplicate_id:SIG-000537': 1}`
- `candidate CAND-BB67DB089F3A entity_id=SIG-000539 reason=duplicate_id:SIG-000539 conf=0.92`
- `candidate CAND-815DE05CD973 entity_id=SIG-000536 reason=duplicate_id:SIG-000536 conf=0.92`
- `candidate CAND-D14748A24E6A entity_id=SIG-000535 reason=duplicate_id:SIG-000535 conf=0.9`
- `candidate CAND-555AD85E9AFF entity_id=SIG-000538 reason=duplicate_id:SIG-000538 conf=0.9`
- `candidate CAND-0CFAF6BB2EA8 entity_id=SIG-000537 reason=duplicate_id:SIG-000537 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-BB67DB089F3A | business_signal_library | 0.92 | False | duplicate_id:SIG-000539 | Rejected |
| CAND-815DE05CD973 | business_signal_library | 0.92 | False | duplicate_id:SIG-000536 | Rejected |
| CAND-D14748A24E6A | business_signal_library | 0.9 | False | duplicate_id:SIG-000535 | Rejected |
| CAND-555AD85E9AFF | business_signal_library | 0.9 | False | duplicate_id:SIG-000538 | Rejected |
| CAND-0CFAF6BB2EA8 | business_signal_library | 0.88 | False | duplicate_id:SIG-000537 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000539` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
