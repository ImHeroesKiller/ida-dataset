# Candidate Root Cause

**Generated:** 2026-08-12T12:07:20+00:00
**Session:** `SESSION-20260812-1107FB`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001972`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260812-1107FB`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001972': 1, 'duplicate_id:SIG-001971': 1, 'duplicate_id:SIG-001973': 1, 'duplicate_id:SIG-001974': 1, 'duplicate_id:SIG-001970': 1}`
- `candidate CAND-03A008CFE344 entity_id=SIG-001972 reason=duplicate_id:SIG-001972 conf=0.88`
- `candidate CAND-2BF9385FFD27 entity_id=SIG-001971 reason=duplicate_id:SIG-001971 conf=0.92`
- `candidate CAND-F8C46B12F748 entity_id=SIG-001973 reason=duplicate_id:SIG-001973 conf=0.9`
- `candidate CAND-0378EBFD8170 entity_id=SIG-001974 reason=duplicate_id:SIG-001974 conf=0.92`
- `candidate CAND-14EA8599D487 entity_id=SIG-001970 reason=duplicate_id:SIG-001970 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-03A008CFE344 | business_signal_library | 0.88 | False | duplicate_id:SIG-001972 | Rejected |
| CAND-2BF9385FFD27 | business_signal_library | 0.92 | False | duplicate_id:SIG-001971 | Rejected |
| CAND-F8C46B12F748 | business_signal_library | 0.9 | False | duplicate_id:SIG-001973 | Rejected |
| CAND-0378EBFD8170 | business_signal_library | 0.92 | False | duplicate_id:SIG-001974 | Rejected |
| CAND-14EA8599D487 | business_signal_library | 0.9 | False | duplicate_id:SIG-001970 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001972` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
