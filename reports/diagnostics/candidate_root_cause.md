# Candidate Root Cause

**Generated:** 2026-08-24T10:55:59+00:00
**Session:** `SESSION-20260824-27860E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001220`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260824-27860E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001220': 1, 'duplicate_id:SIG-001219': 1, 'duplicate_id:SIG-001218': 1, 'duplicate_id:SIG-001216': 1, 'duplicate_id:SIG-001217': 1}`
- `candidate CAND-33E17A2DED84 entity_id=SIG-001220 reason=duplicate_id:SIG-001220 conf=0.9`
- `candidate CAND-4D612DDBADF4 entity_id=SIG-001219 reason=duplicate_id:SIG-001219 conf=0.9`
- `candidate CAND-F866E4894FB4 entity_id=SIG-001218 reason=duplicate_id:SIG-001218 conf=0.9`
- `candidate CAND-1B8C86D852F4 entity_id=SIG-001216 reason=duplicate_id:SIG-001216 conf=0.92`
- `candidate CAND-039287A82056 entity_id=SIG-001217 reason=duplicate_id:SIG-001217 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-33E17A2DED84 | business_signal_library | 0.9 | False | duplicate_id:SIG-001220 | Rejected |
| CAND-4D612DDBADF4 | business_signal_library | 0.9 | False | duplicate_id:SIG-001219 | Rejected |
| CAND-F866E4894FB4 | business_signal_library | 0.9 | False | duplicate_id:SIG-001218 | Rejected |
| CAND-1B8C86D852F4 | business_signal_library | 0.92 | False | duplicate_id:SIG-001216 | Rejected |
| CAND-039287A82056 | business_signal_library | 0.9 | False | duplicate_id:SIG-001217 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001220` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
