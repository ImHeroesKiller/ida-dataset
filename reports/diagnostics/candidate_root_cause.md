# Candidate Root Cause

**Generated:** 2026-08-21T22:44:38+00:00
**Session:** `SESSION-20260821-093313`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000948`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-093313`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000948': 1, 'duplicate_id:SIG-000950': 1, 'duplicate_id:SIG-000949': 1, 'duplicate_id:SIG-000947': 1, 'duplicate_id:SIG-000946': 1}`
- `candidate CAND-4D33D40FFE41 entity_id=SIG-000948 reason=duplicate_id:SIG-000948 conf=0.9`
- `candidate CAND-1E04B18F7EC0 entity_id=SIG-000950 reason=duplicate_id:SIG-000950 conf=0.9`
- `candidate CAND-FCDC8FCC0535 entity_id=SIG-000949 reason=duplicate_id:SIG-000949 conf=0.9`
- `candidate CAND-521C77F641BC entity_id=SIG-000947 reason=duplicate_id:SIG-000947 conf=0.9`
- `candidate CAND-E3E33CD05DC2 entity_id=SIG-000946 reason=duplicate_id:SIG-000946 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4D33D40FFE41 | business_signal_library | 0.9 | False | duplicate_id:SIG-000948 | Rejected |
| CAND-1E04B18F7EC0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000950 | Rejected |
| CAND-FCDC8FCC0535 | business_signal_library | 0.9 | False | duplicate_id:SIG-000949 | Rejected |
| CAND-521C77F641BC | business_signal_library | 0.9 | False | duplicate_id:SIG-000947 | Rejected |
| CAND-E3E33CD05DC2 | business_signal_library | 0.92 | False | duplicate_id:SIG-000946 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000948` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
