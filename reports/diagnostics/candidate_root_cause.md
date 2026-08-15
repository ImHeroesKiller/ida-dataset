# Candidate Root Cause

**Generated:** 2026-08-15T05:39:02+00:00
**Session:** `SESSION-20260815-7E8F04`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000187`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-7E8F04`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000187': 1, 'duplicate_id:SIG-000189': 1, 'duplicate_id:SIG-000188': 1, 'duplicate_id:SIG-000186': 1, 'duplicate_id:SIG-000190': 1}`
- `candidate CAND-FFD93695BC3C entity_id=SIG-000187 reason=duplicate_id:SIG-000187 conf=0.9`
- `candidate CAND-8F76666CA87C entity_id=SIG-000189 reason=duplicate_id:SIG-000189 conf=0.9`
- `candidate CAND-4CCFC941B303 entity_id=SIG-000188 reason=duplicate_id:SIG-000188 conf=0.9`
- `candidate CAND-27995E64D39C entity_id=SIG-000186 reason=duplicate_id:SIG-000186 conf=0.92`
- `candidate CAND-D53E09BEC5C5 entity_id=SIG-000190 reason=duplicate_id:SIG-000190 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FFD93695BC3C | business_signal_library | 0.9 | False | duplicate_id:SIG-000187 | Rejected |
| CAND-8F76666CA87C | business_signal_library | 0.9 | False | duplicate_id:SIG-000189 | Rejected |
| CAND-4CCFC941B303 | business_signal_library | 0.9 | False | duplicate_id:SIG-000188 | Rejected |
| CAND-27995E64D39C | business_signal_library | 0.92 | False | duplicate_id:SIG-000186 | Rejected |
| CAND-D53E09BEC5C5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000190 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000187` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
