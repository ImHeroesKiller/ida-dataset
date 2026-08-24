# Candidate Root Cause

**Generated:** 2026-08-24T14:11:57+00:00
**Session:** `SESSION-20260824-51FFEE`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001234`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260824-51FFEE`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001234': 1, 'duplicate_id:SIG-001233': 1, 'duplicate_id:SIG-001231': 1, 'duplicate_id:SIG-001232': 1, 'duplicate_id:SIG-001235': 1}`
- `candidate CAND-391B6756D29E entity_id=SIG-001234 reason=duplicate_id:SIG-001234 conf=0.9`
- `candidate CAND-4940E0ED6B5A entity_id=SIG-001233 reason=duplicate_id:SIG-001233 conf=0.9`
- `candidate CAND-3E7DDCCB7BE7 entity_id=SIG-001231 reason=duplicate_id:SIG-001231 conf=0.92`
- `candidate CAND-F15A6699ED8A entity_id=SIG-001232 reason=duplicate_id:SIG-001232 conf=0.9`
- `candidate CAND-646D79E19837 entity_id=SIG-001235 reason=duplicate_id:SIG-001235 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-391B6756D29E | business_signal_library | 0.9 | False | duplicate_id:SIG-001234 | Rejected |
| CAND-4940E0ED6B5A | business_signal_library | 0.9 | False | duplicate_id:SIG-001233 | Rejected |
| CAND-3E7DDCCB7BE7 | business_signal_library | 0.92 | False | duplicate_id:SIG-001231 | Rejected |
| CAND-F15A6699ED8A | business_signal_library | 0.9 | False | duplicate_id:SIG-001232 | Rejected |
| CAND-646D79E19837 | business_signal_library | 0.9 | False | duplicate_id:SIG-001235 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001234` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
