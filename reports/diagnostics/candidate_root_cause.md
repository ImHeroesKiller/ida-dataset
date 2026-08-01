# Candidate Root Cause

**Generated:** 2026-08-01T22:21:31+00:00
**Session:** `SESSION-20260801-17AD18`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001234`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260801-17AD18`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001234': 1, 'duplicate_id:SIG-001232': 1, 'duplicate_id:SIG-001230': 1, 'duplicate_id:SIG-001233': 1, 'duplicate_id:SIG-001231': 1}`
- `candidate CAND-B34BD716C68C entity_id=SIG-001234 reason=duplicate_id:SIG-001234 conf=0.92`
- `candidate CAND-31834BDF6ED8 entity_id=SIG-001232 reason=duplicate_id:SIG-001232 conf=0.88`
- `candidate CAND-BF8059258BAF entity_id=SIG-001230 reason=duplicate_id:SIG-001230 conf=0.9`
- `candidate CAND-306BD1BDD079 entity_id=SIG-001233 reason=duplicate_id:SIG-001233 conf=0.9`
- `candidate CAND-7DC7B1FF711C entity_id=SIG-001231 reason=duplicate_id:SIG-001231 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B34BD716C68C | business_signal_library | 0.92 | False | duplicate_id:SIG-001234 | Rejected |
| CAND-31834BDF6ED8 | business_signal_library | 0.88 | False | duplicate_id:SIG-001232 | Rejected |
| CAND-BF8059258BAF | business_signal_library | 0.9 | False | duplicate_id:SIG-001230 | Rejected |
| CAND-306BD1BDD079 | business_signal_library | 0.9 | False | duplicate_id:SIG-001233 | Rejected |
| CAND-7DC7B1FF711C | business_signal_library | 0.92 | False | duplicate_id:SIG-001231 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001234` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
