# Candidate Root Cause

**Generated:** 2026-07-12T09:23:07+00:00
**Session:** `SESSION-20260712-6D9F98`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000091`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260712-6D9F98`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000091': 1, 'duplicate_id:SIG-000094': 1, 'duplicate_id:SIG-000090': 1, 'duplicate_id:SIG-000093': 1, 'duplicate_id:SIG-000092': 1}`
- `candidate CAND-153880E3AA52 entity_id=SIG-000091 reason=duplicate_id:SIG-000091 conf=0.92`
- `candidate CAND-C5625A7A6429 entity_id=SIG-000094 reason=duplicate_id:SIG-000094 conf=0.92`
- `candidate CAND-0D27D86BDE8A entity_id=SIG-000090 reason=duplicate_id:SIG-000090 conf=0.9`
- `candidate CAND-06D3CD95EE5D entity_id=SIG-000093 reason=duplicate_id:SIG-000093 conf=0.9`
- `candidate CAND-D1FB4715F0BE entity_id=SIG-000092 reason=duplicate_id:SIG-000092 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-153880E3AA52 | business_signal_library | 0.92 | False | duplicate_id:SIG-000091 | Rejected |
| CAND-C5625A7A6429 | business_signal_library | 0.92 | False | duplicate_id:SIG-000094 | Rejected |
| CAND-0D27D86BDE8A | business_signal_library | 0.9 | False | duplicate_id:SIG-000090 | Rejected |
| CAND-06D3CD95EE5D | business_signal_library | 0.9 | False | duplicate_id:SIG-000093 | Rejected |
| CAND-D1FB4715F0BE | business_signal_library | 0.88 | False | duplicate_id:SIG-000092 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000091` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
