# Candidate Root Cause

**Generated:** 2026-08-09T07:18:34+00:00
**Session:** `SESSION-20260809-46F743`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001691`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-46F743`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001691': 1, 'duplicate_id:SIG-001693': 1, 'duplicate_id:SIG-001694': 1, 'duplicate_id:SIG-001690': 1, 'duplicate_id:SIG-001692': 1}`
- `candidate CAND-5CC04BFB79A6 entity_id=SIG-001691 reason=duplicate_id:SIG-001691 conf=0.92`
- `candidate CAND-155A9103831C entity_id=SIG-001693 reason=duplicate_id:SIG-001693 conf=0.9`
- `candidate CAND-5369928AC6D1 entity_id=SIG-001694 reason=duplicate_id:SIG-001694 conf=0.92`
- `candidate CAND-8A52F5D6A109 entity_id=SIG-001690 reason=duplicate_id:SIG-001690 conf=0.9`
- `candidate CAND-36EFC9BC123A entity_id=SIG-001692 reason=duplicate_id:SIG-001692 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5CC04BFB79A6 | business_signal_library | 0.92 | False | duplicate_id:SIG-001691 | Rejected |
| CAND-155A9103831C | business_signal_library | 0.9 | False | duplicate_id:SIG-001693 | Rejected |
| CAND-5369928AC6D1 | business_signal_library | 0.92 | False | duplicate_id:SIG-001694 | Rejected |
| CAND-8A52F5D6A109 | business_signal_library | 0.9 | False | duplicate_id:SIG-001690 | Rejected |
| CAND-36EFC9BC123A | business_signal_library | 0.88 | False | duplicate_id:SIG-001692 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001691` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
