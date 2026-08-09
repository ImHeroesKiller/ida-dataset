# Candidate Root Cause

**Generated:** 2026-08-09T11:48:47+00:00
**Session:** `SESSION-20260809-8A08C6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001715`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-8A08C6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001715': 1, 'duplicate_id:SIG-001719': 1, 'duplicate_id:SIG-001716': 1, 'duplicate_id:SIG-001717': 1, 'duplicate_id:SIG-001718': 1}`
- `candidate CAND-FFF47DB3BA02 entity_id=SIG-001715 reason=duplicate_id:SIG-001715 conf=0.9`
- `candidate CAND-4BE04656387B entity_id=SIG-001719 reason=duplicate_id:SIG-001719 conf=0.92`
- `candidate CAND-03170FC19D60 entity_id=SIG-001716 reason=duplicate_id:SIG-001716 conf=0.92`
- `candidate CAND-3262030D6420 entity_id=SIG-001717 reason=duplicate_id:SIG-001717 conf=0.88`
- `candidate CAND-F57EB22B2B05 entity_id=SIG-001718 reason=duplicate_id:SIG-001718 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FFF47DB3BA02 | business_signal_library | 0.9 | False | duplicate_id:SIG-001715 | Rejected |
| CAND-4BE04656387B | business_signal_library | 0.92 | False | duplicate_id:SIG-001719 | Rejected |
| CAND-03170FC19D60 | business_signal_library | 0.92 | False | duplicate_id:SIG-001716 | Rejected |
| CAND-3262030D6420 | business_signal_library | 0.88 | False | duplicate_id:SIG-001717 | Rejected |
| CAND-F57EB22B2B05 | business_signal_library | 0.9 | False | duplicate_id:SIG-001718 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001715` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
