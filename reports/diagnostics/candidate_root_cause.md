# Candidate Root Cause

**Generated:** 2026-08-09T09:09:11+00:00
**Session:** `SESSION-20260809-0CEB67`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001704`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-0CEB67`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001704': 1, 'duplicate_id:SIG-001701': 1, 'duplicate_id:SIG-001702': 1, 'duplicate_id:SIG-001700': 1, 'duplicate_id:SIG-001703': 1}`
- `candidate CAND-6AB4FFF89B2C entity_id=SIG-001704 reason=duplicate_id:SIG-001704 conf=0.92`
- `candidate CAND-6C6291A637C2 entity_id=SIG-001701 reason=duplicate_id:SIG-001701 conf=0.92`
- `candidate CAND-D55528D3BDAA entity_id=SIG-001702 reason=duplicate_id:SIG-001702 conf=0.88`
- `candidate CAND-35B8C33BDDE0 entity_id=SIG-001700 reason=duplicate_id:SIG-001700 conf=0.9`
- `candidate CAND-819AEC781AEB entity_id=SIG-001703 reason=duplicate_id:SIG-001703 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6AB4FFF89B2C | business_signal_library | 0.92 | False | duplicate_id:SIG-001704 | Rejected |
| CAND-6C6291A637C2 | business_signal_library | 0.92 | False | duplicate_id:SIG-001701 | Rejected |
| CAND-D55528D3BDAA | business_signal_library | 0.88 | False | duplicate_id:SIG-001702 | Rejected |
| CAND-35B8C33BDDE0 | business_signal_library | 0.9 | False | duplicate_id:SIG-001700 | Rejected |
| CAND-819AEC781AEB | business_signal_library | 0.9 | False | duplicate_id:SIG-001703 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001704` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
