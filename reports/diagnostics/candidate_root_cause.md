# Candidate Root Cause

**Generated:** 2026-07-30T06:53:56+00:00
**Session:** `SESSION-20260730-F4B912`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001085`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260730-F4B912`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001085': 1, 'duplicate_id:SIG-001086': 1, 'duplicate_id:SIG-001088': 1, 'duplicate_id:SIG-001089': 1, 'duplicate_id:SIG-001087': 1}`
- `candidate CAND-2DE462363531 entity_id=SIG-001085 reason=duplicate_id:SIG-001085 conf=0.9`
- `candidate CAND-A3B904375DB2 entity_id=SIG-001086 reason=duplicate_id:SIG-001086 conf=0.92`
- `candidate CAND-4600437B8E14 entity_id=SIG-001088 reason=duplicate_id:SIG-001088 conf=0.9`
- `candidate CAND-99F8095A9383 entity_id=SIG-001089 reason=duplicate_id:SIG-001089 conf=0.92`
- `candidate CAND-F61E5D586FC2 entity_id=SIG-001087 reason=duplicate_id:SIG-001087 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2DE462363531 | business_signal_library | 0.9 | False | duplicate_id:SIG-001085 | Rejected |
| CAND-A3B904375DB2 | business_signal_library | 0.92 | False | duplicate_id:SIG-001086 | Rejected |
| CAND-4600437B8E14 | business_signal_library | 0.9 | False | duplicate_id:SIG-001088 | Rejected |
| CAND-99F8095A9383 | business_signal_library | 0.92 | False | duplicate_id:SIG-001089 | Rejected |
| CAND-F61E5D586FC2 | business_signal_library | 0.88 | False | duplicate_id:SIG-001087 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001085` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
