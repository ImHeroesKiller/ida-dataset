# Candidate Root Cause

**Generated:** 2026-07-29T09:09:36+00:00
**Session:** `SESSION-20260729-1751BA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001038`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260729-1751BA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001038': 1, 'duplicate_id:SIG-001039': 1, 'duplicate_id:SIG-001036': 1, 'duplicate_id:SIG-001037': 1, 'duplicate_id:SIG-001035': 1}`
- `candidate CAND-5AC593752965 entity_id=SIG-001038 reason=duplicate_id:SIG-001038 conf=0.9`
- `candidate CAND-91E0EBA3E646 entity_id=SIG-001039 reason=duplicate_id:SIG-001039 conf=0.92`
- `candidate CAND-4571B1F0ED5E entity_id=SIG-001036 reason=duplicate_id:SIG-001036 conf=0.92`
- `candidate CAND-7D73F2DE14A0 entity_id=SIG-001037 reason=duplicate_id:SIG-001037 conf=0.88`
- `candidate CAND-0A497AA82D72 entity_id=SIG-001035 reason=duplicate_id:SIG-001035 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5AC593752965 | business_signal_library | 0.9 | False | duplicate_id:SIG-001038 | Rejected |
| CAND-91E0EBA3E646 | business_signal_library | 0.92 | False | duplicate_id:SIG-001039 | Rejected |
| CAND-4571B1F0ED5E | business_signal_library | 0.92 | False | duplicate_id:SIG-001036 | Rejected |
| CAND-7D73F2DE14A0 | business_signal_library | 0.88 | False | duplicate_id:SIG-001037 | Rejected |
| CAND-0A497AA82D72 | business_signal_library | 0.9 | False | duplicate_id:SIG-001035 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001038` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
