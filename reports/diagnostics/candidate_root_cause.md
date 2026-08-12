# Candidate Root Cause

**Generated:** 2026-08-12T22:07:10+00:00
**Session:** `SESSION-20260812-E39200`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-002006`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260812-E39200`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-002006': 1, 'duplicate_id:SIG-002005': 1, 'duplicate_id:SIG-002008': 1, 'duplicate_id:SIG-002009': 1, 'duplicate_id:SIG-002007': 1}`
- `candidate CAND-404FE3AE6B1C entity_id=SIG-002006 reason=duplicate_id:SIG-002006 conf=0.92`
- `candidate CAND-AD7197898232 entity_id=SIG-002005 reason=duplicate_id:SIG-002005 conf=0.9`
- `candidate CAND-23E2BAD1843B entity_id=SIG-002008 reason=duplicate_id:SIG-002008 conf=0.9`
- `candidate CAND-0A4759612CCB entity_id=SIG-002009 reason=duplicate_id:SIG-002009 conf=0.92`
- `candidate CAND-E5B93681AE5D entity_id=SIG-002007 reason=duplicate_id:SIG-002007 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-404FE3AE6B1C | business_signal_library | 0.92 | False | duplicate_id:SIG-002006 | Rejected |
| CAND-AD7197898232 | business_signal_library | 0.9 | False | duplicate_id:SIG-002005 | Rejected |
| CAND-23E2BAD1843B | business_signal_library | 0.9 | False | duplicate_id:SIG-002008 | Rejected |
| CAND-0A4759612CCB | business_signal_library | 0.92 | False | duplicate_id:SIG-002009 | Rejected |
| CAND-E5B93681AE5D | business_signal_library | 0.88 | False | duplicate_id:SIG-002007 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-002006` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
