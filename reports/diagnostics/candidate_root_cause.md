# Candidate Root Cause

**Generated:** 2026-08-10T19:27:50+00:00
**Session:** `SESSION-20260810-5EC7A1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001833`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-5EC7A1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001833': 1, 'duplicate_id:SIG-001831': 1, 'duplicate_id:SIG-001832': 1, 'duplicate_id:SIG-001834': 1, 'duplicate_id:SIG-001830': 1}`
- `candidate CAND-DAC5560D993D entity_id=SIG-001833 reason=duplicate_id:SIG-001833 conf=0.9`
- `candidate CAND-7995885ED0B7 entity_id=SIG-001831 reason=duplicate_id:SIG-001831 conf=0.92`
- `candidate CAND-61E83C6ECECF entity_id=SIG-001832 reason=duplicate_id:SIG-001832 conf=0.88`
- `candidate CAND-0541E9534910 entity_id=SIG-001834 reason=duplicate_id:SIG-001834 conf=0.92`
- `candidate CAND-F71AD1B81456 entity_id=SIG-001830 reason=duplicate_id:SIG-001830 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DAC5560D993D | business_signal_library | 0.9 | False | duplicate_id:SIG-001833 | Rejected |
| CAND-7995885ED0B7 | business_signal_library | 0.92 | False | duplicate_id:SIG-001831 | Rejected |
| CAND-61E83C6ECECF | business_signal_library | 0.88 | False | duplicate_id:SIG-001832 | Rejected |
| CAND-0541E9534910 | business_signal_library | 0.92 | False | duplicate_id:SIG-001834 | Rejected |
| CAND-F71AD1B81456 | business_signal_library | 0.9 | False | duplicate_id:SIG-001830 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001833` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
