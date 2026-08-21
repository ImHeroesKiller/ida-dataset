# Candidate Root Cause

**Generated:** 2026-08-21T11:46:15+00:00
**Session:** `SESSION-20260821-4DBFBD`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000895`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-4DBFBD`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000895': 1, 'duplicate_id:SIG-000893': 1, 'duplicate_id:SIG-000892': 1, 'duplicate_id:SIG-000894': 1, 'duplicate_id:SIG-000891': 1}`
- `candidate CAND-6323B751CE34 entity_id=SIG-000895 reason=duplicate_id:SIG-000895 conf=0.9`
- `candidate CAND-46BD04237113 entity_id=SIG-000893 reason=duplicate_id:SIG-000893 conf=0.9`
- `candidate CAND-39AAC5BFEA58 entity_id=SIG-000892 reason=duplicate_id:SIG-000892 conf=0.9`
- `candidate CAND-3A29FFDC311E entity_id=SIG-000894 reason=duplicate_id:SIG-000894 conf=0.9`
- `candidate CAND-FFED4946B7B4 entity_id=SIG-000891 reason=duplicate_id:SIG-000891 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6323B751CE34 | business_signal_library | 0.9 | False | duplicate_id:SIG-000895 | Rejected |
| CAND-46BD04237113 | business_signal_library | 0.9 | False | duplicate_id:SIG-000893 | Rejected |
| CAND-39AAC5BFEA58 | business_signal_library | 0.9 | False | duplicate_id:SIG-000892 | Rejected |
| CAND-3A29FFDC311E | business_signal_library | 0.9 | False | duplicate_id:SIG-000894 | Rejected |
| CAND-FFED4946B7B4 | business_signal_library | 0.92 | False | duplicate_id:SIG-000891 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000895` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
