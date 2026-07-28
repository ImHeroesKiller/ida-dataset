# Candidate Root Cause

**Generated:** 2026-07-28T17:01:42+00:00
**Session:** `SESSION-20260728-131EF2`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001004`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260728-131EF2`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001004': 1, 'duplicate_id:SIG-001000': 1, 'duplicate_id:SIG-001002': 1, 'duplicate_id:SIG-001001': 1, 'duplicate_id:SIG-001003': 1}`
- `candidate CAND-53CB65AD6435 entity_id=SIG-001004 reason=duplicate_id:SIG-001004 conf=0.92`
- `candidate CAND-3AFCD470AF00 entity_id=SIG-001000 reason=duplicate_id:SIG-001000 conf=0.9`
- `candidate CAND-10E983F8BBBE entity_id=SIG-001002 reason=duplicate_id:SIG-001002 conf=0.88`
- `candidate CAND-7180F62E835E entity_id=SIG-001001 reason=duplicate_id:SIG-001001 conf=0.92`
- `candidate CAND-B5F3EF427E25 entity_id=SIG-001003 reason=duplicate_id:SIG-001003 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-53CB65AD6435 | business_signal_library | 0.92 | False | duplicate_id:SIG-001004 | Rejected |
| CAND-3AFCD470AF00 | business_signal_library | 0.9 | False | duplicate_id:SIG-001000 | Rejected |
| CAND-10E983F8BBBE | business_signal_library | 0.88 | False | duplicate_id:SIG-001002 | Rejected |
| CAND-7180F62E835E | business_signal_library | 0.92 | False | duplicate_id:SIG-001001 | Rejected |
| CAND-B5F3EF427E25 | business_signal_library | 0.9 | False | duplicate_id:SIG-001003 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001004` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
