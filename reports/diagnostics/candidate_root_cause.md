# Candidate Root Cause

**Generated:** 2026-08-12T19:31:48+00:00
**Session:** `SESSION-20260812-12DF4F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001999`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260812-12DF4F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001999': 1, 'duplicate_id:SIG-001995': 1, 'duplicate_id:SIG-001998': 1, 'duplicate_id:SIG-001996': 1, 'duplicate_id:SIG-001997': 1}`
- `candidate CAND-B51615D8244D entity_id=SIG-001999 reason=duplicate_id:SIG-001999 conf=0.92`
- `candidate CAND-4A69D513267D entity_id=SIG-001995 reason=duplicate_id:SIG-001995 conf=0.9`
- `candidate CAND-5FB676CBAEDF entity_id=SIG-001998 reason=duplicate_id:SIG-001998 conf=0.9`
- `candidate CAND-CACFCDB392AC entity_id=SIG-001996 reason=duplicate_id:SIG-001996 conf=0.92`
- `candidate CAND-79C8DD601C89 entity_id=SIG-001997 reason=duplicate_id:SIG-001997 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B51615D8244D | business_signal_library | 0.92 | False | duplicate_id:SIG-001999 | Rejected |
| CAND-4A69D513267D | business_signal_library | 0.9 | False | duplicate_id:SIG-001995 | Rejected |
| CAND-5FB676CBAEDF | business_signal_library | 0.9 | False | duplicate_id:SIG-001998 | Rejected |
| CAND-CACFCDB392AC | business_signal_library | 0.92 | False | duplicate_id:SIG-001996 | Rejected |
| CAND-79C8DD601C89 | business_signal_library | 0.88 | False | duplicate_id:SIG-001997 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001999` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
