# Candidate Root Cause

**Generated:** 2026-08-23T20:43:02+00:00
**Session:** `SESSION-20260823-B446EC`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001161`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-B446EC`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001161': 1, 'duplicate_id:SIG-001162': 1, 'duplicate_id:SIG-001163': 1, 'duplicate_id:SIG-001165': 1, 'duplicate_id:SIG-001164': 1}`
- `candidate CAND-DC39B89B5525 entity_id=SIG-001161 reason=duplicate_id:SIG-001161 conf=0.92`
- `candidate CAND-5DFE3B02F533 entity_id=SIG-001162 reason=duplicate_id:SIG-001162 conf=0.9`
- `candidate CAND-0831460B1DD6 entity_id=SIG-001163 reason=duplicate_id:SIG-001163 conf=0.9`
- `candidate CAND-098871ED13F3 entity_id=SIG-001165 reason=duplicate_id:SIG-001165 conf=0.9`
- `candidate CAND-35BEA2604EC8 entity_id=SIG-001164 reason=duplicate_id:SIG-001164 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DC39B89B5525 | business_signal_library | 0.92 | False | duplicate_id:SIG-001161 | Rejected |
| CAND-5DFE3B02F533 | business_signal_library | 0.9 | False | duplicate_id:SIG-001162 | Rejected |
| CAND-0831460B1DD6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001163 | Rejected |
| CAND-098871ED13F3 | business_signal_library | 0.9 | False | duplicate_id:SIG-001165 | Rejected |
| CAND-35BEA2604EC8 | business_signal_library | 0.9 | False | duplicate_id:SIG-001164 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001161` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
