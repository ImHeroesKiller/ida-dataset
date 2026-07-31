# Candidate Root Cause

**Generated:** 2026-07-31T21:24:23+00:00
**Session:** `SESSION-20260731-39673C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001177`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260731-39673C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001177': 1, 'duplicate_id:SIG-001175': 1, 'duplicate_id:SIG-001179': 1, 'duplicate_id:SIG-001176': 1, 'duplicate_id:SIG-001178': 1}`
- `candidate CAND-68689EECA43E entity_id=SIG-001177 reason=duplicate_id:SIG-001177 conf=0.88`
- `candidate CAND-53ADC6594452 entity_id=SIG-001175 reason=duplicate_id:SIG-001175 conf=0.9`
- `candidate CAND-C4FE92B14F33 entity_id=SIG-001179 reason=duplicate_id:SIG-001179 conf=0.92`
- `candidate CAND-C0837F756E01 entity_id=SIG-001176 reason=duplicate_id:SIG-001176 conf=0.92`
- `candidate CAND-A2AAC6AEA742 entity_id=SIG-001178 reason=duplicate_id:SIG-001178 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-68689EECA43E | business_signal_library | 0.88 | False | duplicate_id:SIG-001177 | Rejected |
| CAND-53ADC6594452 | business_signal_library | 0.9 | False | duplicate_id:SIG-001175 | Rejected |
| CAND-C4FE92B14F33 | business_signal_library | 0.92 | False | duplicate_id:SIG-001179 | Rejected |
| CAND-C0837F756E01 | business_signal_library | 0.92 | False | duplicate_id:SIG-001176 | Rejected |
| CAND-A2AAC6AEA742 | business_signal_library | 0.9 | False | duplicate_id:SIG-001178 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001177` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
