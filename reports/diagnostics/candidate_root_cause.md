# Candidate Root Cause

**Generated:** 2026-08-23T15:43:00+00:00
**Session:** `SESSION-20260823-D0670F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001139`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-D0670F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001139': 1, 'duplicate_id:SIG-001137': 1, 'duplicate_id:SIG-001138': 1, 'duplicate_id:SIG-001140': 1, 'duplicate_id:SIG-001136': 1}`
- `candidate CAND-07ACA3827BD9 entity_id=SIG-001139 reason=duplicate_id:SIG-001139 conf=0.9`
- `candidate CAND-F5A5544E7E67 entity_id=SIG-001137 reason=duplicate_id:SIG-001137 conf=0.9`
- `candidate CAND-F50E83FE4967 entity_id=SIG-001138 reason=duplicate_id:SIG-001138 conf=0.9`
- `candidate CAND-BD0BB2C49A27 entity_id=SIG-001140 reason=duplicate_id:SIG-001140 conf=0.9`
- `candidate CAND-8E10B3A5E4CE entity_id=SIG-001136 reason=duplicate_id:SIG-001136 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-07ACA3827BD9 | business_signal_library | 0.9 | False | duplicate_id:SIG-001139 | Rejected |
| CAND-F5A5544E7E67 | business_signal_library | 0.9 | False | duplicate_id:SIG-001137 | Rejected |
| CAND-F50E83FE4967 | business_signal_library | 0.9 | False | duplicate_id:SIG-001138 | Rejected |
| CAND-BD0BB2C49A27 | business_signal_library | 0.9 | False | duplicate_id:SIG-001140 | Rejected |
| CAND-8E10B3A5E4CE | business_signal_library | 0.92 | False | duplicate_id:SIG-001136 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001139` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
