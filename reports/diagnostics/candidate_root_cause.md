# Candidate Root Cause

**Generated:** 2026-08-24T05:57:33+00:00
**Session:** `SESSION-20260824-38C5B9`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001198`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260824-38C5B9`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001198': 1, 'duplicate_id:SIG-001199': 1, 'duplicate_id:SIG-001197': 1, 'duplicate_id:SIG-001196': 1, 'duplicate_id:SIG-001200': 1}`
- `candidate CAND-7995FBF33B05 entity_id=SIG-001198 reason=duplicate_id:SIG-001198 conf=0.9`
- `candidate CAND-829938F97550 entity_id=SIG-001199 reason=duplicate_id:SIG-001199 conf=0.9`
- `candidate CAND-0649651BE6B3 entity_id=SIG-001197 reason=duplicate_id:SIG-001197 conf=0.9`
- `candidate CAND-8A1C13A623CE entity_id=SIG-001196 reason=duplicate_id:SIG-001196 conf=0.92`
- `candidate CAND-37317598AA1A entity_id=SIG-001200 reason=duplicate_id:SIG-001200 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7995FBF33B05 | business_signal_library | 0.9 | False | duplicate_id:SIG-001198 | Rejected |
| CAND-829938F97550 | business_signal_library | 0.9 | False | duplicate_id:SIG-001199 | Rejected |
| CAND-0649651BE6B3 | business_signal_library | 0.9 | False | duplicate_id:SIG-001197 | Rejected |
| CAND-8A1C13A623CE | business_signal_library | 0.92 | False | duplicate_id:SIG-001196 | Rejected |
| CAND-37317598AA1A | business_signal_library | 0.9 | False | duplicate_id:SIG-001200 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001198` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
