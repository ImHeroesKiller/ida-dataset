# Candidate Root Cause

**Generated:** 2026-08-02T19:31:04+00:00
**Session:** `SESSION-20260802-155C66`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001280`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260802-155C66`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001280': 1, 'duplicate_id:SIG-001283': 1, 'duplicate_id:SIG-001281': 1, 'duplicate_id:SIG-001284': 1, 'duplicate_id:SIG-001282': 1}`
- `candidate CAND-BACA7AA8F9CA entity_id=SIG-001280 reason=duplicate_id:SIG-001280 conf=0.9`
- `candidate CAND-1A1170133AAC entity_id=SIG-001283 reason=duplicate_id:SIG-001283 conf=0.9`
- `candidate CAND-02F4CF246911 entity_id=SIG-001281 reason=duplicate_id:SIG-001281 conf=0.92`
- `candidate CAND-9826B4D5A997 entity_id=SIG-001284 reason=duplicate_id:SIG-001284 conf=0.92`
- `candidate CAND-8617BA898CA9 entity_id=SIG-001282 reason=duplicate_id:SIG-001282 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-BACA7AA8F9CA | business_signal_library | 0.9 | False | duplicate_id:SIG-001280 | Rejected |
| CAND-1A1170133AAC | business_signal_library | 0.9 | False | duplicate_id:SIG-001283 | Rejected |
| CAND-02F4CF246911 | business_signal_library | 0.92 | False | duplicate_id:SIG-001281 | Rejected |
| CAND-9826B4D5A997 | business_signal_library | 0.92 | False | duplicate_id:SIG-001284 | Rejected |
| CAND-8617BA898CA9 | business_signal_library | 0.88 | False | duplicate_id:SIG-001282 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001280` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
