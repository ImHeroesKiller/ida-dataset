# Candidate Root Cause

**Generated:** 2026-08-07T04:08:49+00:00
**Session:** `SESSION-20260807-5AD7D9`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001483`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-5AD7D9`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001483': 1, 'duplicate_id:SIG-001481': 1, 'duplicate_id:SIG-001484': 1, 'duplicate_id:SIG-001480': 1, 'duplicate_id:SIG-001482': 1}`
- `candidate CAND-DA3DE215CADE entity_id=SIG-001483 reason=duplicate_id:SIG-001483 conf=0.9`
- `candidate CAND-98AC028EE035 entity_id=SIG-001481 reason=duplicate_id:SIG-001481 conf=0.92`
- `candidate CAND-BA4D39DC6C6F entity_id=SIG-001484 reason=duplicate_id:SIG-001484 conf=0.92`
- `candidate CAND-AABDB9BF5F17 entity_id=SIG-001480 reason=duplicate_id:SIG-001480 conf=0.9`
- `candidate CAND-B1BBEF3285C4 entity_id=SIG-001482 reason=duplicate_id:SIG-001482 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DA3DE215CADE | business_signal_library | 0.9 | False | duplicate_id:SIG-001483 | Rejected |
| CAND-98AC028EE035 | business_signal_library | 0.92 | False | duplicate_id:SIG-001481 | Rejected |
| CAND-BA4D39DC6C6F | business_signal_library | 0.92 | False | duplicate_id:SIG-001484 | Rejected |
| CAND-AABDB9BF5F17 | business_signal_library | 0.9 | False | duplicate_id:SIG-001480 | Rejected |
| CAND-B1BBEF3285C4 | business_signal_library | 0.88 | False | duplicate_id:SIG-001482 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001483` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
