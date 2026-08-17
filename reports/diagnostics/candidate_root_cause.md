# Candidate Root Cause

**Generated:** 2026-08-17T23:37:58+00:00
**Session:** `SESSION-20260817-3E4D7D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000500`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-3E4D7D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000500': 1, 'duplicate_id:SIG-000496': 1, 'duplicate_id:SIG-000498': 1, 'duplicate_id:SIG-000499': 1, 'duplicate_id:SIG-000497': 1}`
- `candidate CAND-B261E2876715 entity_id=SIG-000500 reason=duplicate_id:SIG-000500 conf=0.9`
- `candidate CAND-77A2539554E7 entity_id=SIG-000496 reason=duplicate_id:SIG-000496 conf=0.92`
- `candidate CAND-B19C574ABADB entity_id=SIG-000498 reason=duplicate_id:SIG-000498 conf=0.9`
- `candidate CAND-1F62EDD2D6EB entity_id=SIG-000499 reason=duplicate_id:SIG-000499 conf=0.9`
- `candidate CAND-36DB67905D85 entity_id=SIG-000497 reason=duplicate_id:SIG-000497 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B261E2876715 | business_signal_library | 0.9 | False | duplicate_id:SIG-000500 | Rejected |
| CAND-77A2539554E7 | business_signal_library | 0.92 | False | duplicate_id:SIG-000496 | Rejected |
| CAND-B19C574ABADB | business_signal_library | 0.9 | False | duplicate_id:SIG-000498 | Rejected |
| CAND-1F62EDD2D6EB | business_signal_library | 0.9 | False | duplicate_id:SIG-000499 | Rejected |
| CAND-36DB67905D85 | business_signal_library | 0.9 | False | duplicate_id:SIG-000497 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000500` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
