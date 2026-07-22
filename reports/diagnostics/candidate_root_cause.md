# Candidate Root Cause

**Generated:** 2026-07-22T07:53:32+00:00
**Session:** `SESSION-20260722-1DD63C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000667`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260722-1DD63C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000667': 1, 'duplicate_id:SIG-000666': 1, 'duplicate_id:SIG-000668': 1, 'duplicate_id:SIG-000669': 1, 'duplicate_id:SIG-000665': 1}`
- `candidate CAND-0D9BC5BA4A17 entity_id=SIG-000667 reason=duplicate_id:SIG-000667 conf=0.88`
- `candidate CAND-1704E2993E48 entity_id=SIG-000666 reason=duplicate_id:SIG-000666 conf=0.92`
- `candidate CAND-A47DAF18B917 entity_id=SIG-000668 reason=duplicate_id:SIG-000668 conf=0.9`
- `candidate CAND-24EB6CFB982D entity_id=SIG-000669 reason=duplicate_id:SIG-000669 conf=0.92`
- `candidate CAND-F6B93D60A3A9 entity_id=SIG-000665 reason=duplicate_id:SIG-000665 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0D9BC5BA4A17 | business_signal_library | 0.88 | False | duplicate_id:SIG-000667 | Rejected |
| CAND-1704E2993E48 | business_signal_library | 0.92 | False | duplicate_id:SIG-000666 | Rejected |
| CAND-A47DAF18B917 | business_signal_library | 0.9 | False | duplicate_id:SIG-000668 | Rejected |
| CAND-24EB6CFB982D | business_signal_library | 0.92 | False | duplicate_id:SIG-000669 | Rejected |
| CAND-F6B93D60A3A9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000665 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000667` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
