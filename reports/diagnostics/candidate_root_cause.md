# Candidate Root Cause

**Generated:** 2026-08-15T19:34:27+00:00
**Session:** `SESSION-20260815-DA6CAD`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000257`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-DA6CAD`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000257': 1, 'duplicate_id:SIG-000256': 1, 'duplicate_id:SIG-000260': 1, 'duplicate_id:SIG-000259': 1, 'duplicate_id:SIG-000258': 1}`
- `candidate CAND-05EFE4E98A84 entity_id=SIG-000257 reason=duplicate_id:SIG-000257 conf=0.9`
- `candidate CAND-7B72015D2B0F entity_id=SIG-000256 reason=duplicate_id:SIG-000256 conf=0.92`
- `candidate CAND-FECAB88CBAB0 entity_id=SIG-000260 reason=duplicate_id:SIG-000260 conf=0.9`
- `candidate CAND-B7637AFDEC48 entity_id=SIG-000259 reason=duplicate_id:SIG-000259 conf=0.9`
- `candidate CAND-4EB74EBB67E6 entity_id=SIG-000258 reason=duplicate_id:SIG-000258 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-05EFE4E98A84 | business_signal_library | 0.9 | False | duplicate_id:SIG-000257 | Rejected |
| CAND-7B72015D2B0F | business_signal_library | 0.92 | False | duplicate_id:SIG-000256 | Rejected |
| CAND-FECAB88CBAB0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000260 | Rejected |
| CAND-B7637AFDEC48 | business_signal_library | 0.9 | False | duplicate_id:SIG-000259 | Rejected |
| CAND-4EB74EBB67E6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000258 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000257` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
