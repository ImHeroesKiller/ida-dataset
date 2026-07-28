# Candidate Root Cause

**Generated:** 2026-07-28T02:59:20+00:00
**Session:** `SESSION-20260728-6F8F94`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000980`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260728-6F8F94`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000980': 1, 'duplicate_id:SIG-000983': 1, 'duplicate_id:SIG-000982': 1, 'duplicate_id:SIG-000981': 1, 'duplicate_id:SIG-000984': 1}`
- `candidate CAND-A0F43FB5B469 entity_id=SIG-000980 reason=duplicate_id:SIG-000980 conf=0.9`
- `candidate CAND-A8DC4938F56F entity_id=SIG-000983 reason=duplicate_id:SIG-000983 conf=0.9`
- `candidate CAND-DBA6EF2FBD52 entity_id=SIG-000982 reason=duplicate_id:SIG-000982 conf=0.88`
- `candidate CAND-29E0C835FA8D entity_id=SIG-000981 reason=duplicate_id:SIG-000981 conf=0.92`
- `candidate CAND-A57D11D39C45 entity_id=SIG-000984 reason=duplicate_id:SIG-000984 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A0F43FB5B469 | business_signal_library | 0.9 | False | duplicate_id:SIG-000980 | Rejected |
| CAND-A8DC4938F56F | business_signal_library | 0.9 | False | duplicate_id:SIG-000983 | Rejected |
| CAND-DBA6EF2FBD52 | business_signal_library | 0.88 | False | duplicate_id:SIG-000982 | Rejected |
| CAND-29E0C835FA8D | business_signal_library | 0.92 | False | duplicate_id:SIG-000981 | Rejected |
| CAND-A57D11D39C45 | business_signal_library | 0.92 | False | duplicate_id:SIG-000984 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000980` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
