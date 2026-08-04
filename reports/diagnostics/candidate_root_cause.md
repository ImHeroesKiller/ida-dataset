# Candidate Root Cause

**Generated:** 2026-08-04T18:49:13+00:00
**Session:** `SESSION-20260804-BC39B9`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001383`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260804-BC39B9`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001383': 1, 'duplicate_id:SIG-001380': 1, 'duplicate_id:SIG-001384': 1, 'duplicate_id:SIG-001381': 1, 'duplicate_id:SIG-001382': 1}`
- `candidate CAND-6A81A7CC6365 entity_id=SIG-001383 reason=duplicate_id:SIG-001383 conf=0.9`
- `candidate CAND-4501297B7E8D entity_id=SIG-001380 reason=duplicate_id:SIG-001380 conf=0.9`
- `candidate CAND-63634C7550BC entity_id=SIG-001384 reason=duplicate_id:SIG-001384 conf=0.92`
- `candidate CAND-EED3EF440BE5 entity_id=SIG-001381 reason=duplicate_id:SIG-001381 conf=0.92`
- `candidate CAND-CE9E8C0C48A4 entity_id=SIG-001382 reason=duplicate_id:SIG-001382 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6A81A7CC6365 | business_signal_library | 0.9 | False | duplicate_id:SIG-001383 | Rejected |
| CAND-4501297B7E8D | business_signal_library | 0.9 | False | duplicate_id:SIG-001380 | Rejected |
| CAND-63634C7550BC | business_signal_library | 0.92 | False | duplicate_id:SIG-001384 | Rejected |
| CAND-EED3EF440BE5 | business_signal_library | 0.92 | False | duplicate_id:SIG-001381 | Rejected |
| CAND-CE9E8C0C48A4 | business_signal_library | 0.88 | False | duplicate_id:SIG-001382 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001383` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
