# Candidate Root Cause

**Generated:** 2026-07-11T10:24:16+00:00
**Session:** `SESSION-20260711-C6CDF9`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000035`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260711-C6CDF9`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000035': 1, 'duplicate_id:SIG-000039': 1, 'duplicate_id:SIG-000038': 1, 'duplicate_id:SIG-000036': 1, 'duplicate_id:SIG-000037': 1}`
- `candidate CAND-C591A3211145 entity_id=SIG-000035 reason=duplicate_id:SIG-000035 conf=0.9`
- `candidate CAND-E1A9E882A02E entity_id=SIG-000039 reason=duplicate_id:SIG-000039 conf=0.92`
- `candidate CAND-821C4A7AAAEB entity_id=SIG-000038 reason=duplicate_id:SIG-000038 conf=0.9`
- `candidate CAND-825DCF302C31 entity_id=SIG-000036 reason=duplicate_id:SIG-000036 conf=0.92`
- `candidate CAND-33AB2719B8BC entity_id=SIG-000037 reason=duplicate_id:SIG-000037 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C591A3211145 | business_signal_library | 0.9 | False | duplicate_id:SIG-000035 | Rejected |
| CAND-E1A9E882A02E | business_signal_library | 0.92 | False | duplicate_id:SIG-000039 | Rejected |
| CAND-821C4A7AAAEB | business_signal_library | 0.9 | False | duplicate_id:SIG-000038 | Rejected |
| CAND-825DCF302C31 | business_signal_library | 0.92 | False | duplicate_id:SIG-000036 | Rejected |
| CAND-33AB2719B8BC | business_signal_library | 0.88 | False | duplicate_id:SIG-000037 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000035` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
