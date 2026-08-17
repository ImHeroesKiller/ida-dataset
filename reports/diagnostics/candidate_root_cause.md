# Candidate Root Cause

**Generated:** 2026-08-17T10:47:28+00:00
**Session:** `SESSION-20260817-7FC508`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000431`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-7FC508`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000431': 1, 'duplicate_id:SIG-000432': 1, 'duplicate_id:SIG-000435': 1, 'duplicate_id:SIG-000434': 1, 'duplicate_id:SIG-000433': 1}`
- `candidate CAND-90E8B4C03187 entity_id=SIG-000431 reason=duplicate_id:SIG-000431 conf=0.92`
- `candidate CAND-553805CCF843 entity_id=SIG-000432 reason=duplicate_id:SIG-000432 conf=0.9`
- `candidate CAND-244553DC2B67 entity_id=SIG-000435 reason=duplicate_id:SIG-000435 conf=0.9`
- `candidate CAND-110B12140330 entity_id=SIG-000434 reason=duplicate_id:SIG-000434 conf=0.9`
- `candidate CAND-073CC628103F entity_id=SIG-000433 reason=duplicate_id:SIG-000433 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-90E8B4C03187 | business_signal_library | 0.92 | False | duplicate_id:SIG-000431 | Rejected |
| CAND-553805CCF843 | business_signal_library | 0.9 | False | duplicate_id:SIG-000432 | Rejected |
| CAND-244553DC2B67 | business_signal_library | 0.9 | False | duplicate_id:SIG-000435 | Rejected |
| CAND-110B12140330 | business_signal_library | 0.9 | False | duplicate_id:SIG-000434 | Rejected |
| CAND-073CC628103F | business_signal_library | 0.9 | False | duplicate_id:SIG-000433 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000431` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
