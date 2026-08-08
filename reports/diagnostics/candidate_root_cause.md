# Candidate Root Cause

**Generated:** 2026-08-08T10:53:19+00:00
**Session:** `SESSION-20260808-B2782F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001609`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-B2782F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001609': 1, 'duplicate_id:SIG-001607': 1, 'duplicate_id:SIG-001608': 1, 'duplicate_id:SIG-001606': 1, 'duplicate_id:SIG-001605': 1}`
- `candidate CAND-95C4FE73A692 entity_id=SIG-001609 reason=duplicate_id:SIG-001609 conf=0.92`
- `candidate CAND-E54F84B804EE entity_id=SIG-001607 reason=duplicate_id:SIG-001607 conf=0.88`
- `candidate CAND-3AD9A8305968 entity_id=SIG-001608 reason=duplicate_id:SIG-001608 conf=0.9`
- `candidate CAND-FAE53EC70D9F entity_id=SIG-001606 reason=duplicate_id:SIG-001606 conf=0.92`
- `candidate CAND-F63660754218 entity_id=SIG-001605 reason=duplicate_id:SIG-001605 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-95C4FE73A692 | business_signal_library | 0.92 | False | duplicate_id:SIG-001609 | Rejected |
| CAND-E54F84B804EE | business_signal_library | 0.88 | False | duplicate_id:SIG-001607 | Rejected |
| CAND-3AD9A8305968 | business_signal_library | 0.9 | False | duplicate_id:SIG-001608 | Rejected |
| CAND-FAE53EC70D9F | business_signal_library | 0.92 | False | duplicate_id:SIG-001606 | Rejected |
| CAND-F63660754218 | business_signal_library | 0.9 | False | duplicate_id:SIG-001605 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001609` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
