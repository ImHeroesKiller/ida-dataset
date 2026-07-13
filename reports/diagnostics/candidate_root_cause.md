# Candidate Root Cause

**Generated:** 2026-07-13T10:49:35+00:00
**Session:** `SESSION-20260713-39EDF7`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000157`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260713-39EDF7`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000157': 1, 'duplicate_id:SIG-000155': 1, 'duplicate_id:SIG-000158': 1, 'duplicate_id:SIG-000159': 1, 'duplicate_id:SIG-000156': 1}`
- `candidate CAND-4760F5ECD2A7 entity_id=SIG-000157 reason=duplicate_id:SIG-000157 conf=0.88`
- `candidate CAND-51F8478D42C8 entity_id=SIG-000155 reason=duplicate_id:SIG-000155 conf=0.9`
- `candidate CAND-EA06333A2083 entity_id=SIG-000158 reason=duplicate_id:SIG-000158 conf=0.9`
- `candidate CAND-3862E05B462B entity_id=SIG-000159 reason=duplicate_id:SIG-000159 conf=0.92`
- `candidate CAND-97C42C3C1DBD entity_id=SIG-000156 reason=duplicate_id:SIG-000156 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4760F5ECD2A7 | business_signal_library | 0.88 | False | duplicate_id:SIG-000157 | Rejected |
| CAND-51F8478D42C8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000155 | Rejected |
| CAND-EA06333A2083 | business_signal_library | 0.9 | False | duplicate_id:SIG-000158 | Rejected |
| CAND-3862E05B462B | business_signal_library | 0.92 | False | duplicate_id:SIG-000159 | Rejected |
| CAND-97C42C3C1DBD | business_signal_library | 0.92 | False | duplicate_id:SIG-000156 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000157` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
