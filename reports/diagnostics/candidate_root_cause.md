# Candidate Root Cause

**Generated:** 2026-08-21T20:45:46+00:00
**Session:** `SESSION-20260821-575416`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000936`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-575416`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000936': 1, 'duplicate_id:SIG-000938': 1, 'duplicate_id:SIG-000937': 1, 'duplicate_id:SIG-000939': 1, 'duplicate_id:SIG-000940': 1}`
- `candidate CAND-DA8C56632BDE entity_id=SIG-000936 reason=duplicate_id:SIG-000936 conf=0.92`
- `candidate CAND-96C87663E0EF entity_id=SIG-000938 reason=duplicate_id:SIG-000938 conf=0.9`
- `candidate CAND-3E81876BDA10 entity_id=SIG-000937 reason=duplicate_id:SIG-000937 conf=0.9`
- `candidate CAND-D19211091D19 entity_id=SIG-000939 reason=duplicate_id:SIG-000939 conf=0.9`
- `candidate CAND-7A934755FA94 entity_id=SIG-000940 reason=duplicate_id:SIG-000940 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DA8C56632BDE | business_signal_library | 0.92 | False | duplicate_id:SIG-000936 | Rejected |
| CAND-96C87663E0EF | business_signal_library | 0.9 | False | duplicate_id:SIG-000938 | Rejected |
| CAND-3E81876BDA10 | business_signal_library | 0.9 | False | duplicate_id:SIG-000937 | Rejected |
| CAND-D19211091D19 | business_signal_library | 0.9 | False | duplicate_id:SIG-000939 | Rejected |
| CAND-7A934755FA94 | business_signal_library | 0.9 | False | duplicate_id:SIG-000940 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000936` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
