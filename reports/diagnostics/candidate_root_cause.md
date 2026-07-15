# Candidate Root Cause

**Generated:** 2026-07-15T15:15:34+00:00
**Session:** `SESSION-20260715-C4FFA3`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000260`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260715-C4FFA3`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000260': 1, 'duplicate_id:SIG-000262': 1, 'duplicate_id:SIG-000261': 1, 'duplicate_id:SIG-000263': 1, 'duplicate_id:SIG-000264': 1}`
- `candidate CAND-78770980F2D2 entity_id=SIG-000260 reason=duplicate_id:SIG-000260 conf=0.9`
- `candidate CAND-863F475DAEAF entity_id=SIG-000262 reason=duplicate_id:SIG-000262 conf=0.92`
- `candidate CAND-F6BAA6A0BDAF entity_id=SIG-000261 reason=duplicate_id:SIG-000261 conf=0.88`
- `candidate CAND-40B652407BCD entity_id=SIG-000263 reason=duplicate_id:SIG-000263 conf=0.85`
- `candidate CAND-79CC7526A1D1 entity_id=SIG-000264 reason=duplicate_id:SIG-000264 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-78770980F2D2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000260 | Rejected |
| CAND-863F475DAEAF | business_signal_library | 0.92 | False | duplicate_id:SIG-000262 | Rejected |
| CAND-F6BAA6A0BDAF | business_signal_library | 0.88 | False | duplicate_id:SIG-000261 | Rejected |
| CAND-40B652407BCD | business_signal_library | 0.85 | False | duplicate_id:SIG-000263 | Rejected |
| CAND-79CC7526A1D1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000264 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000260` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
