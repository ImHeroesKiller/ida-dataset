# Candidate Root Cause

**Generated:** 2026-08-22T13:51:22+00:00
**Session:** `SESSION-20260822-0E030C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001017`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-0E030C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001017': 1, 'duplicate_id:SIG-001016': 1, 'duplicate_id:SIG-001020': 1, 'duplicate_id:SIG-001018': 1, 'duplicate_id:SIG-001019': 1}`
- `candidate CAND-E01867C95A35 entity_id=SIG-001017 reason=duplicate_id:SIG-001017 conf=0.9`
- `candidate CAND-220D32C9267F entity_id=SIG-001016 reason=duplicate_id:SIG-001016 conf=0.92`
- `candidate CAND-368BB1B82962 entity_id=SIG-001020 reason=duplicate_id:SIG-001020 conf=0.9`
- `candidate CAND-4F7A64AC7226 entity_id=SIG-001018 reason=duplicate_id:SIG-001018 conf=0.9`
- `candidate CAND-CD3AF35A7D6A entity_id=SIG-001019 reason=duplicate_id:SIG-001019 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E01867C95A35 | business_signal_library | 0.9 | False | duplicate_id:SIG-001017 | Rejected |
| CAND-220D32C9267F | business_signal_library | 0.92 | False | duplicate_id:SIG-001016 | Rejected |
| CAND-368BB1B82962 | business_signal_library | 0.9 | False | duplicate_id:SIG-001020 | Rejected |
| CAND-4F7A64AC7226 | business_signal_library | 0.9 | False | duplicate_id:SIG-001018 | Rejected |
| CAND-CD3AF35A7D6A | business_signal_library | 0.9 | False | duplicate_id:SIG-001019 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001017` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
