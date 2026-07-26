# Candidate Root Cause

**Generated:** 2026-07-26T03:19:07+00:00
**Session:** `SESSION-20260726-6FF8FC`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000878`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260726-6FF8FC`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000878': 1, 'duplicate_id:SIG-000879': 1, 'duplicate_id:SIG-000875': 1, 'duplicate_id:SIG-000876': 1, 'duplicate_id:SIG-000877': 1}`
- `candidate CAND-240516BB096B entity_id=SIG-000878 reason=duplicate_id:SIG-000878 conf=0.9`
- `candidate CAND-6AFE6F2DD8BC entity_id=SIG-000879 reason=duplicate_id:SIG-000879 conf=0.92`
- `candidate CAND-D0A5FD5AA38B entity_id=SIG-000875 reason=duplicate_id:SIG-000875 conf=0.9`
- `candidate CAND-399F47D7C9E8 entity_id=SIG-000876 reason=duplicate_id:SIG-000876 conf=0.92`
- `candidate CAND-9711F56BAE07 entity_id=SIG-000877 reason=duplicate_id:SIG-000877 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-240516BB096B | business_signal_library | 0.9 | False | duplicate_id:SIG-000878 | Rejected |
| CAND-6AFE6F2DD8BC | business_signal_library | 0.92 | False | duplicate_id:SIG-000879 | Rejected |
| CAND-D0A5FD5AA38B | business_signal_library | 0.9 | False | duplicate_id:SIG-000875 | Rejected |
| CAND-399F47D7C9E8 | business_signal_library | 0.92 | False | duplicate_id:SIG-000876 | Rejected |
| CAND-9711F56BAE07 | business_signal_library | 0.88 | False | duplicate_id:SIG-000877 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000878` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
