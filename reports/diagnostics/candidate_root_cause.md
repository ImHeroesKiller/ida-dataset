# Candidate Root Cause

**Generated:** 2026-08-24T05:05:15+00:00
**Session:** `SESSION-20260824-EA5764`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001193`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260824-EA5764`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001193': 1, 'duplicate_id:SIG-001195': 1, 'duplicate_id:SIG-001191': 1, 'duplicate_id:SIG-001194': 1, 'duplicate_id:SIG-001192': 1}`
- `candidate CAND-610C298AE7E7 entity_id=SIG-001193 reason=duplicate_id:SIG-001193 conf=0.9`
- `candidate CAND-4816E858B208 entity_id=SIG-001195 reason=duplicate_id:SIG-001195 conf=0.9`
- `candidate CAND-9FD21F44F5A1 entity_id=SIG-001191 reason=duplicate_id:SIG-001191 conf=0.92`
- `candidate CAND-30EA792E9972 entity_id=SIG-001194 reason=duplicate_id:SIG-001194 conf=0.9`
- `candidate CAND-D51B86F2D296 entity_id=SIG-001192 reason=duplicate_id:SIG-001192 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-610C298AE7E7 | business_signal_library | 0.9 | False | duplicate_id:SIG-001193 | Rejected |
| CAND-4816E858B208 | business_signal_library | 0.9 | False | duplicate_id:SIG-001195 | Rejected |
| CAND-9FD21F44F5A1 | business_signal_library | 0.92 | False | duplicate_id:SIG-001191 | Rejected |
| CAND-30EA792E9972 | business_signal_library | 0.9 | False | duplicate_id:SIG-001194 | Rejected |
| CAND-D51B86F2D296 | business_signal_library | 0.9 | False | duplicate_id:SIG-001192 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001193` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
