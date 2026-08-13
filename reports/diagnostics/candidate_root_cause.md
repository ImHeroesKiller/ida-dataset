# Candidate Root Cause

**Generated:** 2026-08-13T22:56:58+00:00
**Session:** `SESSION-20260813-1F6838`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000067`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260813-1F6838`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000067': 1, 'duplicate_id:SIG-000066': 1, 'duplicate_id:SIG-000069': 1, 'duplicate_id:SIG-000068': 1, 'duplicate_id:SIG-000070': 1}`
- `candidate CAND-4A3D6D0C5DAB entity_id=SIG-000067 reason=duplicate_id:SIG-000067 conf=0.9`
- `candidate CAND-B885955D647D entity_id=SIG-000066 reason=duplicate_id:SIG-000066 conf=0.92`
- `candidate CAND-E74E62421DED entity_id=SIG-000069 reason=duplicate_id:SIG-000069 conf=0.9`
- `candidate CAND-F75F3C1F4503 entity_id=SIG-000068 reason=duplicate_id:SIG-000068 conf=0.9`
- `candidate CAND-AAEA826020D6 entity_id=SIG-000070 reason=duplicate_id:SIG-000070 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4A3D6D0C5DAB | business_signal_library | 0.9 | False | duplicate_id:SIG-000067 | Rejected |
| CAND-B885955D647D | business_signal_library | 0.92 | False | duplicate_id:SIG-000066 | Rejected |
| CAND-E74E62421DED | business_signal_library | 0.9 | False | duplicate_id:SIG-000069 | Rejected |
| CAND-F75F3C1F4503 | business_signal_library | 0.9 | False | duplicate_id:SIG-000068 | Rejected |
| CAND-AAEA826020D6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000070 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000067` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
