# Candidate Root Cause

**Generated:** 2026-08-15T20:36:55+00:00
**Session:** `SESSION-20260815-F34A47`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000264`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-F34A47`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000264': 1, 'duplicate_id:SIG-000263': 1, 'duplicate_id:SIG-000265': 1, 'duplicate_id:SIG-000261': 1, 'duplicate_id:SIG-000262': 1}`
- `candidate CAND-34DEF7CF7233 entity_id=SIG-000264 reason=duplicate_id:SIG-000264 conf=0.9`
- `candidate CAND-10759A26B5DE entity_id=SIG-000263 reason=duplicate_id:SIG-000263 conf=0.9`
- `candidate CAND-D614D478A9FC entity_id=SIG-000265 reason=duplicate_id:SIG-000265 conf=0.9`
- `candidate CAND-02F8F7F55912 entity_id=SIG-000261 reason=duplicate_id:SIG-000261 conf=0.92`
- `candidate CAND-0435C8284D1B entity_id=SIG-000262 reason=duplicate_id:SIG-000262 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-34DEF7CF7233 | business_signal_library | 0.9 | False | duplicate_id:SIG-000264 | Rejected |
| CAND-10759A26B5DE | business_signal_library | 0.9 | False | duplicate_id:SIG-000263 | Rejected |
| CAND-D614D478A9FC | business_signal_library | 0.9 | False | duplicate_id:SIG-000265 | Rejected |
| CAND-02F8F7F55912 | business_signal_library | 0.92 | False | duplicate_id:SIG-000261 | Rejected |
| CAND-0435C8284D1B | business_signal_library | 0.9 | False | duplicate_id:SIG-000262 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000264` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
