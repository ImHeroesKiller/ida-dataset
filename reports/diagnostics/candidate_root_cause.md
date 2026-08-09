# Candidate Root Cause

**Generated:** 2026-08-09T13:12:47+00:00
**Session:** `SESSION-20260809-35A0B9`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001721`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-35A0B9`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001721': 1, 'duplicate_id:SIG-001720': 1, 'duplicate_id:SIG-001724': 1, 'duplicate_id:SIG-001722': 1, 'duplicate_id:SIG-001723': 1}`
- `candidate CAND-26177332FE65 entity_id=SIG-001721 reason=duplicate_id:SIG-001721 conf=0.92`
- `candidate CAND-CADC4F5BD065 entity_id=SIG-001720 reason=duplicate_id:SIG-001720 conf=0.9`
- `candidate CAND-9AFEAF59BB81 entity_id=SIG-001724 reason=duplicate_id:SIG-001724 conf=0.92`
- `candidate CAND-49835F5B0625 entity_id=SIG-001722 reason=duplicate_id:SIG-001722 conf=0.88`
- `candidate CAND-D5E5D1C59F27 entity_id=SIG-001723 reason=duplicate_id:SIG-001723 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-26177332FE65 | business_signal_library | 0.92 | False | duplicate_id:SIG-001721 | Rejected |
| CAND-CADC4F5BD065 | business_signal_library | 0.9 | False | duplicate_id:SIG-001720 | Rejected |
| CAND-9AFEAF59BB81 | business_signal_library | 0.92 | False | duplicate_id:SIG-001724 | Rejected |
| CAND-49835F5B0625 | business_signal_library | 0.88 | False | duplicate_id:SIG-001722 | Rejected |
| CAND-D5E5D1C59F27 | business_signal_library | 0.9 | False | duplicate_id:SIG-001723 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001721` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
