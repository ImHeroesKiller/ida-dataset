# Candidate Root Cause

**Generated:** 2026-07-24T07:50:40+00:00
**Session:** `SESSION-20260724-A6E0FB`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000765`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260724-A6E0FB`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000765': 1, 'duplicate_id:SIG-000767': 1, 'duplicate_id:SIG-000769': 1, 'duplicate_id:SIG-000768': 1, 'duplicate_id:SIG-000766': 1}`
- `candidate CAND-781254B10699 entity_id=SIG-000765 reason=duplicate_id:SIG-000765 conf=0.9`
- `candidate CAND-205FC73272E1 entity_id=SIG-000767 reason=duplicate_id:SIG-000767 conf=0.88`
- `candidate CAND-A009EEB91DFD entity_id=SIG-000769 reason=duplicate_id:SIG-000769 conf=0.92`
- `candidate CAND-198B91772F8C entity_id=SIG-000768 reason=duplicate_id:SIG-000768 conf=0.9`
- `candidate CAND-337EBAF69D68 entity_id=SIG-000766 reason=duplicate_id:SIG-000766 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-781254B10699 | business_signal_library | 0.9 | False | duplicate_id:SIG-000765 | Rejected |
| CAND-205FC73272E1 | business_signal_library | 0.88 | False | duplicate_id:SIG-000767 | Rejected |
| CAND-A009EEB91DFD | business_signal_library | 0.92 | False | duplicate_id:SIG-000769 | Rejected |
| CAND-198B91772F8C | business_signal_library | 0.9 | False | duplicate_id:SIG-000768 | Rejected |
| CAND-337EBAF69D68 | business_signal_library | 0.92 | False | duplicate_id:SIG-000766 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000765` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
