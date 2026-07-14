# Candidate Root Cause

**Generated:** 2026-07-14T12:36:51+00:00
**Session:** `SESSION-20260714-488CF7`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000204`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260714-488CF7`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000204': 1, 'duplicate_id:SIG-000202': 1, 'duplicate_id:SIG-000201': 1, 'duplicate_id:SIG-000200': 1, 'duplicate_id:SIG-000203': 1}`
- `candidate CAND-040342C45487 entity_id=SIG-000204 reason=duplicate_id:SIG-000204 conf=0.9`
- `candidate CAND-301A4106B6B9 entity_id=SIG-000202 reason=duplicate_id:SIG-000202 conf=0.92`
- `candidate CAND-983C177356D3 entity_id=SIG-000201 reason=duplicate_id:SIG-000201 conf=0.88`
- `candidate CAND-27282FC4815B entity_id=SIG-000200 reason=duplicate_id:SIG-000200 conf=0.9`
- `candidate CAND-67456BA8F0F6 entity_id=SIG-000203 reason=duplicate_id:SIG-000203 conf=0.85`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-040342C45487 | business_signal_library | 0.9 | False | duplicate_id:SIG-000204 | Rejected |
| CAND-301A4106B6B9 | business_signal_library | 0.92 | False | duplicate_id:SIG-000202 | Rejected |
| CAND-983C177356D3 | business_signal_library | 0.88 | False | duplicate_id:SIG-000201 | Rejected |
| CAND-27282FC4815B | business_signal_library | 0.9 | False | duplicate_id:SIG-000200 | Rejected |
| CAND-67456BA8F0F6 | business_signal_library | 0.85 | False | duplicate_id:SIG-000203 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000204` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
