# Candidate Root Cause

**Generated:** 2026-07-13T07:16:09+00:00
**Session:** `SESSION-20260713-D5C28B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000146`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260713-D5C28B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000146': 1, 'duplicate_id:SIG-000147': 1, 'duplicate_id:SIG-000145': 1, 'duplicate_id:SIG-000149': 1, 'duplicate_id:SIG-000148': 1}`
- `candidate CAND-AD44BECE8865 entity_id=SIG-000146 reason=duplicate_id:SIG-000146 conf=0.92`
- `candidate CAND-C62A2DF0F626 entity_id=SIG-000147 reason=duplicate_id:SIG-000147 conf=0.88`
- `candidate CAND-C62BD33D6670 entity_id=SIG-000145 reason=duplicate_id:SIG-000145 conf=0.9`
- `candidate CAND-FDC7B3642121 entity_id=SIG-000149 reason=duplicate_id:SIG-000149 conf=0.92`
- `candidate CAND-73BB26E893A8 entity_id=SIG-000148 reason=duplicate_id:SIG-000148 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-AD44BECE8865 | business_signal_library | 0.92 | False | duplicate_id:SIG-000146 | Rejected |
| CAND-C62A2DF0F626 | business_signal_library | 0.88 | False | duplicate_id:SIG-000147 | Rejected |
| CAND-C62BD33D6670 | business_signal_library | 0.9 | False | duplicate_id:SIG-000145 | Rejected |
| CAND-FDC7B3642121 | business_signal_library | 0.92 | False | duplicate_id:SIG-000149 | Rejected |
| CAND-73BB26E893A8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000148 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000146` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
