# Candidate Root Cause

**Generated:** 2026-08-18T13:03:20+00:00
**Session:** `SESSION-20260818-EBF067`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000559`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-EBF067`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000559': 1, 'duplicate_id:SIG-000556': 1, 'duplicate_id:SIG-000558': 1, 'duplicate_id:SIG-000557': 1, 'duplicate_id:SIG-000560': 1}`
- `candidate CAND-BB6EBFBBEBCE entity_id=SIG-000559 reason=duplicate_id:SIG-000559 conf=0.9`
- `candidate CAND-72B595D748C1 entity_id=SIG-000556 reason=duplicate_id:SIG-000556 conf=0.92`
- `candidate CAND-3510CD789122 entity_id=SIG-000558 reason=duplicate_id:SIG-000558 conf=0.9`
- `candidate CAND-3E4FCF9DA6F3 entity_id=SIG-000557 reason=duplicate_id:SIG-000557 conf=0.9`
- `candidate CAND-33A3465046CF entity_id=SIG-000560 reason=duplicate_id:SIG-000560 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-BB6EBFBBEBCE | business_signal_library | 0.9 | False | duplicate_id:SIG-000559 | Rejected |
| CAND-72B595D748C1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000556 | Rejected |
| CAND-3510CD789122 | business_signal_library | 0.9 | False | duplicate_id:SIG-000558 | Rejected |
| CAND-3E4FCF9DA6F3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000557 | Rejected |
| CAND-33A3465046CF | business_signal_library | 0.9 | False | duplicate_id:SIG-000560 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000559` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
