# Candidate Root Cause

**Generated:** 2026-07-21T12:05:35+00:00
**Session:** `SESSION-20260721-2133E0`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000624`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260721-2133E0`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000624': 1, 'duplicate_id:SIG-000620': 1, 'duplicate_id:SIG-000622': 1, 'duplicate_id:SIG-000623': 1, 'duplicate_id:SIG-000621': 1}`
- `candidate CAND-454CD09B3E12 entity_id=SIG-000624 reason=duplicate_id:SIG-000624 conf=0.92`
- `candidate CAND-D4FB46BF2999 entity_id=SIG-000620 reason=duplicate_id:SIG-000620 conf=0.9`
- `candidate CAND-9B3CDA8AF2A3 entity_id=SIG-000622 reason=duplicate_id:SIG-000622 conf=0.88`
- `candidate CAND-FCB10EBB079C entity_id=SIG-000623 reason=duplicate_id:SIG-000623 conf=0.9`
- `candidate CAND-382EA3B43AC9 entity_id=SIG-000621 reason=duplicate_id:SIG-000621 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-454CD09B3E12 | business_signal_library | 0.92 | False | duplicate_id:SIG-000624 | Rejected |
| CAND-D4FB46BF2999 | business_signal_library | 0.9 | False | duplicate_id:SIG-000620 | Rejected |
| CAND-9B3CDA8AF2A3 | business_signal_library | 0.88 | False | duplicate_id:SIG-000622 | Rejected |
| CAND-FCB10EBB079C | business_signal_library | 0.9 | False | duplicate_id:SIG-000623 | Rejected |
| CAND-382EA3B43AC9 | business_signal_library | 0.92 | False | duplicate_id:SIG-000621 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000624` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
