# Candidate Root Cause

**Generated:** 2026-08-05T07:59:24+00:00
**Session:** `SESSION-20260805-F44054`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001409`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260805-F44054`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001409': 1, 'duplicate_id:SIG-001406': 1, 'duplicate_id:SIG-001407': 1, 'duplicate_id:SIG-001408': 1, 'duplicate_id:SIG-001405': 1}`
- `candidate CAND-6403743BE5CB entity_id=SIG-001409 reason=duplicate_id:SIG-001409 conf=0.92`
- `candidate CAND-EDA7ECA20F36 entity_id=SIG-001406 reason=duplicate_id:SIG-001406 conf=0.92`
- `candidate CAND-5D692CFD9EC7 entity_id=SIG-001407 reason=duplicate_id:SIG-001407 conf=0.88`
- `candidate CAND-C5FEE30564F4 entity_id=SIG-001408 reason=duplicate_id:SIG-001408 conf=0.9`
- `candidate CAND-974CF3ECACDB entity_id=SIG-001405 reason=duplicate_id:SIG-001405 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6403743BE5CB | business_signal_library | 0.92 | False | duplicate_id:SIG-001409 | Rejected |
| CAND-EDA7ECA20F36 | business_signal_library | 0.92 | False | duplicate_id:SIG-001406 | Rejected |
| CAND-5D692CFD9EC7 | business_signal_library | 0.88 | False | duplicate_id:SIG-001407 | Rejected |
| CAND-C5FEE30564F4 | business_signal_library | 0.9 | False | duplicate_id:SIG-001408 | Rejected |
| CAND-974CF3ECACDB | business_signal_library | 0.9 | False | duplicate_id:SIG-001405 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001409` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
