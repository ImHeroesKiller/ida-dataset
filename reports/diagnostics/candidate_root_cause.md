# Candidate Root Cause

**Generated:** 2026-08-19T22:53:38+00:00
**Session:** `SESSION-20260819-8924E1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000722`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-8924E1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000722': 1, 'duplicate_id:SIG-000724': 1, 'duplicate_id:SIG-000725': 1, 'duplicate_id:SIG-000723': 1, 'duplicate_id:SIG-000721': 1}`
- `candidate CAND-33CDCABF9175 entity_id=SIG-000722 reason=duplicate_id:SIG-000722 conf=0.9`
- `candidate CAND-B5AFD094DA8D entity_id=SIG-000724 reason=duplicate_id:SIG-000724 conf=0.9`
- `candidate CAND-B1264DC9A82F entity_id=SIG-000725 reason=duplicate_id:SIG-000725 conf=0.9`
- `candidate CAND-B8440B3EFB34 entity_id=SIG-000723 reason=duplicate_id:SIG-000723 conf=0.9`
- `candidate CAND-0EC4AB4F08BE entity_id=SIG-000721 reason=duplicate_id:SIG-000721 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-33CDCABF9175 | business_signal_library | 0.9 | False | duplicate_id:SIG-000722 | Rejected |
| CAND-B5AFD094DA8D | business_signal_library | 0.9 | False | duplicate_id:SIG-000724 | Rejected |
| CAND-B1264DC9A82F | business_signal_library | 0.9 | False | duplicate_id:SIG-000725 | Rejected |
| CAND-B8440B3EFB34 | business_signal_library | 0.9 | False | duplicate_id:SIG-000723 | Rejected |
| CAND-0EC4AB4F08BE | business_signal_library | 0.92 | False | duplicate_id:SIG-000721 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000722` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
