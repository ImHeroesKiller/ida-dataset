# Candidate Root Cause

**Generated:** 2026-08-15T11:31:59+00:00
**Session:** `SESSION-20260815-92D26E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000217`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-92D26E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000217': 1, 'duplicate_id:SIG-000219': 1, 'duplicate_id:SIG-000218': 1, 'duplicate_id:SIG-000220': 1, 'duplicate_id:SIG-000216': 1}`
- `candidate CAND-644A22B0F0BA entity_id=SIG-000217 reason=duplicate_id:SIG-000217 conf=0.9`
- `candidate CAND-EC393753F8E9 entity_id=SIG-000219 reason=duplicate_id:SIG-000219 conf=0.9`
- `candidate CAND-CBEE9B4BC4EC entity_id=SIG-000218 reason=duplicate_id:SIG-000218 conf=0.9`
- `candidate CAND-2C3D7CB7CE54 entity_id=SIG-000220 reason=duplicate_id:SIG-000220 conf=0.9`
- `candidate CAND-0ED87BEFC4BE entity_id=SIG-000216 reason=duplicate_id:SIG-000216 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-644A22B0F0BA | business_signal_library | 0.9 | False | duplicate_id:SIG-000217 | Rejected |
| CAND-EC393753F8E9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000219 | Rejected |
| CAND-CBEE9B4BC4EC | business_signal_library | 0.9 | False | duplicate_id:SIG-000218 | Rejected |
| CAND-2C3D7CB7CE54 | business_signal_library | 0.9 | False | duplicate_id:SIG-000220 | Rejected |
| CAND-0ED87BEFC4BE | business_signal_library | 0.92 | False | duplicate_id:SIG-000216 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000217` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
