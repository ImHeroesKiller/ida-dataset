# Candidate Root Cause

**Generated:** 2026-08-13T15:12:45+00:00
**Session:** `SESSION-20260813-966463`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000037`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260813-966463`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000037': 1, 'duplicate_id:SIG-000036': 1, 'duplicate_id:SIG-000038': 1, 'duplicate_id:SIG-000040': 1, 'duplicate_id:SIG-000039': 1}`
- `candidate CAND-1112D769007D entity_id=SIG-000037 reason=duplicate_id:SIG-000037 conf=0.9`
- `candidate CAND-75C00D70B2B2 entity_id=SIG-000036 reason=duplicate_id:SIG-000036 conf=0.92`
- `candidate CAND-494FBA3577BA entity_id=SIG-000038 reason=duplicate_id:SIG-000038 conf=0.9`
- `candidate CAND-E17834D59BA0 entity_id=SIG-000040 reason=duplicate_id:SIG-000040 conf=0.9`
- `candidate CAND-E22521BAC641 entity_id=SIG-000039 reason=duplicate_id:SIG-000039 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-1112D769007D | business_signal_library | 0.9 | False | duplicate_id:SIG-000037 | Rejected |
| CAND-75C00D70B2B2 | business_signal_library | 0.92 | False | duplicate_id:SIG-000036 | Rejected |
| CAND-494FBA3577BA | business_signal_library | 0.9 | False | duplicate_id:SIG-000038 | Rejected |
| CAND-E17834D59BA0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000040 | Rejected |
| CAND-E22521BAC641 | business_signal_library | 0.9 | False | duplicate_id:SIG-000039 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000037` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
