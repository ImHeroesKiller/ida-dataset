# Candidate Root Cause

**Generated:** 2026-08-09T21:59:33+00:00
**Session:** `SESSION-20260809-397A01`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001767`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-397A01`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001767': 1, 'duplicate_id:SIG-001766': 1, 'duplicate_id:SIG-001769': 1, 'duplicate_id:SIG-001765': 1, 'duplicate_id:SIG-001768': 1}`
- `candidate CAND-73C270B097D3 entity_id=SIG-001767 reason=duplicate_id:SIG-001767 conf=0.88`
- `candidate CAND-2AEC27C5EC2D entity_id=SIG-001766 reason=duplicate_id:SIG-001766 conf=0.92`
- `candidate CAND-03AC52A853CF entity_id=SIG-001769 reason=duplicate_id:SIG-001769 conf=0.92`
- `candidate CAND-C868C26FB497 entity_id=SIG-001765 reason=duplicate_id:SIG-001765 conf=0.9`
- `candidate CAND-A2F66793FD8F entity_id=SIG-001768 reason=duplicate_id:SIG-001768 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-73C270B097D3 | business_signal_library | 0.88 | False | duplicate_id:SIG-001767 | Rejected |
| CAND-2AEC27C5EC2D | business_signal_library | 0.92 | False | duplicate_id:SIG-001766 | Rejected |
| CAND-03AC52A853CF | business_signal_library | 0.92 | False | duplicate_id:SIG-001769 | Rejected |
| CAND-C868C26FB497 | business_signal_library | 0.9 | False | duplicate_id:SIG-001765 | Rejected |
| CAND-A2F66793FD8F | business_signal_library | 0.9 | False | duplicate_id:SIG-001768 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001767` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
