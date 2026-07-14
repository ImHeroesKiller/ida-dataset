# Candidate Root Cause

**Generated:** 2026-07-14T22:20:20+00:00
**Session:** `SESSION-20260714-F5E0EA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000228`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260714-F5E0EA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000228': 1, 'duplicate_id:SIG-000229': 1, 'duplicate_id:SIG-000225': 1, 'duplicate_id:SIG-000227': 1, 'duplicate_id:SIG-000226': 1}`
- `candidate CAND-6A86A762D174 entity_id=SIG-000228 reason=duplicate_id:SIG-000228 conf=0.85`
- `candidate CAND-2B893D76402E entity_id=SIG-000229 reason=duplicate_id:SIG-000229 conf=0.9`
- `candidate CAND-9F2FD6E9E5D6 entity_id=SIG-000225 reason=duplicate_id:SIG-000225 conf=0.85`
- `candidate CAND-574B2781AD02 entity_id=SIG-000227 reason=duplicate_id:SIG-000227 conf=0.92`
- `candidate CAND-213C11B13B85 entity_id=SIG-000226 reason=duplicate_id:SIG-000226 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6A86A762D174 | business_signal_library | 0.85 | False | duplicate_id:SIG-000228 | Rejected |
| CAND-2B893D76402E | business_signal_library | 0.9 | False | duplicate_id:SIG-000229 | Rejected |
| CAND-9F2FD6E9E5D6 | business_signal_library | 0.85 | False | duplicate_id:SIG-000225 | Rejected |
| CAND-574B2781AD02 | business_signal_library | 0.92 | False | duplicate_id:SIG-000227 | Rejected |
| CAND-213C11B13B85 | business_signal_library | 0.9 | False | duplicate_id:SIG-000226 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000228` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
