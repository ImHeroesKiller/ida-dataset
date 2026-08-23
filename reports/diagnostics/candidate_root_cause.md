# Candidate Root Cause

**Generated:** 2026-08-23T07:01:38+00:00
**Session:** `SESSION-20260823-F6ADF2`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001091`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-F6ADF2`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001091': 1, 'duplicate_id:SIG-001094': 1, 'duplicate_id:SIG-001095': 1, 'duplicate_id:SIG-001092': 1, 'duplicate_id:SIG-001093': 1}`
- `candidate CAND-29E882E9755E entity_id=SIG-001091 reason=duplicate_id:SIG-001091 conf=0.92`
- `candidate CAND-F2AE79D3721B entity_id=SIG-001094 reason=duplicate_id:SIG-001094 conf=0.9`
- `candidate CAND-948E73466C8B entity_id=SIG-001095 reason=duplicate_id:SIG-001095 conf=0.9`
- `candidate CAND-BE3D5C0CDD63 entity_id=SIG-001092 reason=duplicate_id:SIG-001092 conf=0.9`
- `candidate CAND-E45E53F29DCD entity_id=SIG-001093 reason=duplicate_id:SIG-001093 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-29E882E9755E | business_signal_library | 0.92 | False | duplicate_id:SIG-001091 | Rejected |
| CAND-F2AE79D3721B | business_signal_library | 0.9 | False | duplicate_id:SIG-001094 | Rejected |
| CAND-948E73466C8B | business_signal_library | 0.9 | False | duplicate_id:SIG-001095 | Rejected |
| CAND-BE3D5C0CDD63 | business_signal_library | 0.9 | False | duplicate_id:SIG-001092 | Rejected |
| CAND-E45E53F29DCD | business_signal_library | 0.9 | False | duplicate_id:SIG-001093 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001091` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
