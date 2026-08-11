# Candidate Root Cause

**Generated:** 2026-08-11T13:26:22+00:00
**Session:** `SESSION-20260811-0B4817`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001896`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260811-0B4817`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001896': 1, 'duplicate_id:SIG-001898': 1, 'duplicate_id:SIG-001895': 1, 'duplicate_id:SIG-001899': 1, 'duplicate_id:SIG-001897': 1}`
- `candidate CAND-95C9AC16C72E entity_id=SIG-001896 reason=duplicate_id:SIG-001896 conf=0.92`
- `candidate CAND-0D08C6267E34 entity_id=SIG-001898 reason=duplicate_id:SIG-001898 conf=0.9`
- `candidate CAND-7511F41090D5 entity_id=SIG-001895 reason=duplicate_id:SIG-001895 conf=0.9`
- `candidate CAND-94C6C4C02E22 entity_id=SIG-001899 reason=duplicate_id:SIG-001899 conf=0.92`
- `candidate CAND-A3A59D70010E entity_id=SIG-001897 reason=duplicate_id:SIG-001897 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-95C9AC16C72E | business_signal_library | 0.92 | False | duplicate_id:SIG-001896 | Rejected |
| CAND-0D08C6267E34 | business_signal_library | 0.9 | False | duplicate_id:SIG-001898 | Rejected |
| CAND-7511F41090D5 | business_signal_library | 0.9 | False | duplicate_id:SIG-001895 | Rejected |
| CAND-94C6C4C02E22 | business_signal_library | 0.92 | False | duplicate_id:SIG-001899 | Rejected |
| CAND-A3A59D70010E | business_signal_library | 0.88 | False | duplicate_id:SIG-001897 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001896` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
