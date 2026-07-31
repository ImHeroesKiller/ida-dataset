# Candidate Root Cause

**Generated:** 2026-07-31T08:09:52+00:00
**Session:** `SESSION-20260731-BF82F5`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001141`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260731-BF82F5`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001141': 1, 'duplicate_id:SIG-001143': 1, 'duplicate_id:SIG-001140': 1, 'duplicate_id:SIG-001142': 1, 'duplicate_id:SIG-001144': 1}`
- `candidate CAND-97B0305B3B41 entity_id=SIG-001141 reason=duplicate_id:SIG-001141 conf=0.92`
- `candidate CAND-BAB8AB77DB96 entity_id=SIG-001143 reason=duplicate_id:SIG-001143 conf=0.9`
- `candidate CAND-923F478BF92C entity_id=SIG-001140 reason=duplicate_id:SIG-001140 conf=0.9`
- `candidate CAND-3A367082BB46 entity_id=SIG-001142 reason=duplicate_id:SIG-001142 conf=0.88`
- `candidate CAND-45DC9CE65588 entity_id=SIG-001144 reason=duplicate_id:SIG-001144 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-97B0305B3B41 | business_signal_library | 0.92 | False | duplicate_id:SIG-001141 | Rejected |
| CAND-BAB8AB77DB96 | business_signal_library | 0.9 | False | duplicate_id:SIG-001143 | Rejected |
| CAND-923F478BF92C | business_signal_library | 0.9 | False | duplicate_id:SIG-001140 | Rejected |
| CAND-3A367082BB46 | business_signal_library | 0.88 | False | duplicate_id:SIG-001142 | Rejected |
| CAND-45DC9CE65588 | business_signal_library | 0.92 | False | duplicate_id:SIG-001144 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001141` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
