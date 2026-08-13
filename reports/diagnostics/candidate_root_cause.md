# Candidate Root Cause

**Generated:** 2026-08-13T05:06:27+00:00
**Session:** `SESSION-20260813-B27E4D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000001`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260813-B27E4D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000001': 1, 'duplicate_id:SIG-000005': 1, 'duplicate_id:SIG-000003': 1, 'duplicate_id:SIG-000002': 1, 'duplicate_id:SIG-000004': 1}`
- `candidate CAND-49372E3A2CEB entity_id=SIG-000001 reason=duplicate_id:SIG-000001 conf=0.9`
- `candidate CAND-368A590D2F9F entity_id=SIG-000005 reason=duplicate_id:SIG-000005 conf=0.9`
- `candidate CAND-AC0DACBFE498 entity_id=SIG-000003 reason=duplicate_id:SIG-000003 conf=0.9`
- `candidate CAND-73E5699E5B09 entity_id=SIG-000002 reason=duplicate_id:SIG-000002 conf=0.92`
- `candidate CAND-087D9A7AD2FE entity_id=SIG-000004 reason=duplicate_id:SIG-000004 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-49372E3A2CEB | business_signal_library | 0.9 | False | duplicate_id:SIG-000001 | Rejected |
| CAND-368A590D2F9F | business_signal_library | 0.9 | False | duplicate_id:SIG-000005 | Rejected |
| CAND-AC0DACBFE498 | business_signal_library | 0.9 | False | duplicate_id:SIG-000003 | Rejected |
| CAND-73E5699E5B09 | business_signal_library | 0.92 | False | duplicate_id:SIG-000002 | Rejected |
| CAND-087D9A7AD2FE | business_signal_library | 0.9 | False | duplicate_id:SIG-000004 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000001` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
