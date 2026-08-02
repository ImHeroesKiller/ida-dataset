# Candidate Root Cause

**Generated:** 2026-08-02T22:18:17+00:00
**Session:** `SESSION-20260802-334F21`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001290`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260802-334F21`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001290': 1, 'duplicate_id:SIG-001294': 1, 'duplicate_id:SIG-001292': 1, 'duplicate_id:SIG-001293': 1, 'duplicate_id:SIG-001291': 1}`
- `candidate CAND-A379C54534AF entity_id=SIG-001290 reason=duplicate_id:SIG-001290 conf=0.9`
- `candidate CAND-FC85E1D75E42 entity_id=SIG-001294 reason=duplicate_id:SIG-001294 conf=0.92`
- `candidate CAND-2BE8D974B9FB entity_id=SIG-001292 reason=duplicate_id:SIG-001292 conf=0.88`
- `candidate CAND-F08E90E0FED3 entity_id=SIG-001293 reason=duplicate_id:SIG-001293 conf=0.9`
- `candidate CAND-751AFB9E5AA9 entity_id=SIG-001291 reason=duplicate_id:SIG-001291 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A379C54534AF | business_signal_library | 0.9 | False | duplicate_id:SIG-001290 | Rejected |
| CAND-FC85E1D75E42 | business_signal_library | 0.92 | False | duplicate_id:SIG-001294 | Rejected |
| CAND-2BE8D974B9FB | business_signal_library | 0.88 | False | duplicate_id:SIG-001292 | Rejected |
| CAND-F08E90E0FED3 | business_signal_library | 0.9 | False | duplicate_id:SIG-001293 | Rejected |
| CAND-751AFB9E5AA9 | business_signal_library | 0.92 | False | duplicate_id:SIG-001291 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001290` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
