# Candidate Root Cause

**Generated:** 2026-08-14T07:54:02+00:00
**Session:** `SESSION-20260814-181E14`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000095`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-181E14`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000095': 1, 'duplicate_id:SIG-000094': 1, 'duplicate_id:SIG-000091': 1, 'duplicate_id:SIG-000092': 1, 'duplicate_id:SIG-000093': 1}`
- `candidate CAND-D7A6D8E0325C entity_id=SIG-000095 reason=duplicate_id:SIG-000095 conf=0.9`
- `candidate CAND-A62C5DFA8238 entity_id=SIG-000094 reason=duplicate_id:SIG-000094 conf=0.9`
- `candidate CAND-2CA63AF06C1C entity_id=SIG-000091 reason=duplicate_id:SIG-000091 conf=0.92`
- `candidate CAND-17F2F0BEDF0F entity_id=SIG-000092 reason=duplicate_id:SIG-000092 conf=0.9`
- `candidate CAND-B52E5707B7AC entity_id=SIG-000093 reason=duplicate_id:SIG-000093 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D7A6D8E0325C | business_signal_library | 0.9 | False | duplicate_id:SIG-000095 | Rejected |
| CAND-A62C5DFA8238 | business_signal_library | 0.9 | False | duplicate_id:SIG-000094 | Rejected |
| CAND-2CA63AF06C1C | business_signal_library | 0.92 | False | duplicate_id:SIG-000091 | Rejected |
| CAND-17F2F0BEDF0F | business_signal_library | 0.9 | False | duplicate_id:SIG-000092 | Rejected |
| CAND-B52E5707B7AC | business_signal_library | 0.9 | False | duplicate_id:SIG-000093 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000095` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
