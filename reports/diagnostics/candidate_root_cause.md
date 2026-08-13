# Candidate Root Cause

**Generated:** 2026-08-13T10:20:05+00:00
**Session:** `SESSION-20260813-1DB3D1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000021`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260813-1DB3D1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000021': 1, 'duplicate_id:SIG-000022': 1, 'duplicate_id:SIG-000025': 1, 'duplicate_id:SIG-000024': 1, 'duplicate_id:SIG-000023': 1}`
- `candidate CAND-4D4352DAB1C2 entity_id=SIG-000021 reason=duplicate_id:SIG-000021 conf=0.92`
- `candidate CAND-55C52E295607 entity_id=SIG-000022 reason=duplicate_id:SIG-000022 conf=0.9`
- `candidate CAND-607FE02AF3CB entity_id=SIG-000025 reason=duplicate_id:SIG-000025 conf=0.9`
- `candidate CAND-1B0719A8A324 entity_id=SIG-000024 reason=duplicate_id:SIG-000024 conf=0.9`
- `candidate CAND-0A9BAAE9F53A entity_id=SIG-000023 reason=duplicate_id:SIG-000023 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4D4352DAB1C2 | business_signal_library | 0.92 | False | duplicate_id:SIG-000021 | Rejected |
| CAND-55C52E295607 | business_signal_library | 0.9 | False | duplicate_id:SIG-000022 | Rejected |
| CAND-607FE02AF3CB | business_signal_library | 0.9 | False | duplicate_id:SIG-000025 | Rejected |
| CAND-1B0719A8A324 | business_signal_library | 0.9 | False | duplicate_id:SIG-000024 | Rejected |
| CAND-0A9BAAE9F53A | business_signal_library | 0.9 | False | duplicate_id:SIG-000023 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000021` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
