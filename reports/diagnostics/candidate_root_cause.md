# Candidate Root Cause

**Generated:** 2026-08-16T11:36:26+00:00
**Session:** `SESSION-20260816-A22948`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000329`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-A22948`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000329': 1, 'duplicate_id:SIG-000330': 1, 'duplicate_id:SIG-000327': 1, 'duplicate_id:SIG-000326': 1, 'duplicate_id:SIG-000328': 1}`
- `candidate CAND-D1D2A8D3603C entity_id=SIG-000329 reason=duplicate_id:SIG-000329 conf=0.9`
- `candidate CAND-F149D068BDAC entity_id=SIG-000330 reason=duplicate_id:SIG-000330 conf=0.9`
- `candidate CAND-DF8C98EC1479 entity_id=SIG-000327 reason=duplicate_id:SIG-000327 conf=0.9`
- `candidate CAND-E4CB3C9DA54F entity_id=SIG-000326 reason=duplicate_id:SIG-000326 conf=0.92`
- `candidate CAND-DF0586184C7F entity_id=SIG-000328 reason=duplicate_id:SIG-000328 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D1D2A8D3603C | business_signal_library | 0.9 | False | duplicate_id:SIG-000329 | Rejected |
| CAND-F149D068BDAC | business_signal_library | 0.9 | False | duplicate_id:SIG-000330 | Rejected |
| CAND-DF8C98EC1479 | business_signal_library | 0.9 | False | duplicate_id:SIG-000327 | Rejected |
| CAND-E4CB3C9DA54F | business_signal_library | 0.92 | False | duplicate_id:SIG-000326 | Rejected |
| CAND-DF0586184C7F | business_signal_library | 0.9 | False | duplicate_id:SIG-000328 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000329` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
