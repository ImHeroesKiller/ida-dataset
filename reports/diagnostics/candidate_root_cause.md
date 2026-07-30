# Candidate Root Cause

**Generated:** 2026-07-30T09:50:21+00:00
**Session:** `SESSION-20260730-3157FA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001098`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260730-3157FA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001098': 1, 'duplicate_id:SIG-001099': 1, 'duplicate_id:SIG-001095': 1, 'duplicate_id:SIG-001096': 1, 'duplicate_id:SIG-001097': 1}`
- `candidate CAND-A329B8F1D6E8 entity_id=SIG-001098 reason=duplicate_id:SIG-001098 conf=0.9`
- `candidate CAND-CD54174CA374 entity_id=SIG-001099 reason=duplicate_id:SIG-001099 conf=0.92`
- `candidate CAND-FCAD01A78B58 entity_id=SIG-001095 reason=duplicate_id:SIG-001095 conf=0.9`
- `candidate CAND-3B9B5B920998 entity_id=SIG-001096 reason=duplicate_id:SIG-001096 conf=0.92`
- `candidate CAND-61D55E381D5D entity_id=SIG-001097 reason=duplicate_id:SIG-001097 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A329B8F1D6E8 | business_signal_library | 0.9 | False | duplicate_id:SIG-001098 | Rejected |
| CAND-CD54174CA374 | business_signal_library | 0.92 | False | duplicate_id:SIG-001099 | Rejected |
| CAND-FCAD01A78B58 | business_signal_library | 0.9 | False | duplicate_id:SIG-001095 | Rejected |
| CAND-3B9B5B920998 | business_signal_library | 0.92 | False | duplicate_id:SIG-001096 | Rejected |
| CAND-61D55E381D5D | business_signal_library | 0.88 | False | duplicate_id:SIG-001097 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001098` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
