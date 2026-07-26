# Candidate Root Cause

**Generated:** 2026-07-26T21:21:52+00:00
**Session:** `SESSION-20260726-4F113E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000924`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260726-4F113E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000924': 1, 'duplicate_id:SIG-000921': 1, 'duplicate_id:SIG-000922': 1, 'duplicate_id:SIG-000920': 1, 'duplicate_id:SIG-000923': 1}`
- `candidate CAND-926B41A73525 entity_id=SIG-000924 reason=duplicate_id:SIG-000924 conf=0.92`
- `candidate CAND-82BC7A2538C5 entity_id=SIG-000921 reason=duplicate_id:SIG-000921 conf=0.92`
- `candidate CAND-5674784BC955 entity_id=SIG-000922 reason=duplicate_id:SIG-000922 conf=0.88`
- `candidate CAND-7AAFEC033B1F entity_id=SIG-000920 reason=duplicate_id:SIG-000920 conf=0.9`
- `candidate CAND-60293767341E entity_id=SIG-000923 reason=duplicate_id:SIG-000923 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-926B41A73525 | business_signal_library | 0.92 | False | duplicate_id:SIG-000924 | Rejected |
| CAND-82BC7A2538C5 | business_signal_library | 0.92 | False | duplicate_id:SIG-000921 | Rejected |
| CAND-5674784BC955 | business_signal_library | 0.88 | False | duplicate_id:SIG-000922 | Rejected |
| CAND-7AAFEC033B1F | business_signal_library | 0.9 | False | duplicate_id:SIG-000920 | Rejected |
| CAND-60293767341E | business_signal_library | 0.9 | False | duplicate_id:SIG-000923 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000924` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
