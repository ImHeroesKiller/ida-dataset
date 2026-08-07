# Candidate Root Cause

**Generated:** 2026-08-07T20:12:48+00:00
**Session:** `SESSION-20260807-330F48`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001543`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-330F48`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001543': 1, 'duplicate_id:SIG-001540': 1, 'duplicate_id:SIG-001542': 1, 'duplicate_id:SIG-001541': 1, 'duplicate_id:SIG-001544': 1}`
- `candidate CAND-AF7EB49B1D7E entity_id=SIG-001543 reason=duplicate_id:SIG-001543 conf=0.9`
- `candidate CAND-91F423DCC978 entity_id=SIG-001540 reason=duplicate_id:SIG-001540 conf=0.9`
- `candidate CAND-C41E80DE7239 entity_id=SIG-001542 reason=duplicate_id:SIG-001542 conf=0.88`
- `candidate CAND-A9B1C8D461F5 entity_id=SIG-001541 reason=duplicate_id:SIG-001541 conf=0.92`
- `candidate CAND-1EAE23D4FFF5 entity_id=SIG-001544 reason=duplicate_id:SIG-001544 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-AF7EB49B1D7E | business_signal_library | 0.9 | False | duplicate_id:SIG-001543 | Rejected |
| CAND-91F423DCC978 | business_signal_library | 0.9 | False | duplicate_id:SIG-001540 | Rejected |
| CAND-C41E80DE7239 | business_signal_library | 0.88 | False | duplicate_id:SIG-001542 | Rejected |
| CAND-A9B1C8D461F5 | business_signal_library | 0.92 | False | duplicate_id:SIG-001541 | Rejected |
| CAND-1EAE23D4FFF5 | business_signal_library | 0.92 | False | duplicate_id:SIG-001544 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001543` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
