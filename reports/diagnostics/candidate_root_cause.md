# Candidate Root Cause

**Generated:** 2026-08-07T17:19:41+00:00
**Session:** `SESSION-20260807-C87376`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001529`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-C87376`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001529': 1, 'duplicate_id:SIG-001527': 1, 'duplicate_id:SIG-001528': 1, 'duplicate_id:SIG-001526': 1, 'duplicate_id:SIG-001525': 1}`
- `candidate CAND-245F7A48D068 entity_id=SIG-001529 reason=duplicate_id:SIG-001529 conf=0.92`
- `candidate CAND-5D56584D68AD entity_id=SIG-001527 reason=duplicate_id:SIG-001527 conf=0.88`
- `candidate CAND-94BF23D67141 entity_id=SIG-001528 reason=duplicate_id:SIG-001528 conf=0.9`
- `candidate CAND-B8E1A02F4173 entity_id=SIG-001526 reason=duplicate_id:SIG-001526 conf=0.92`
- `candidate CAND-A63B0ECE7465 entity_id=SIG-001525 reason=duplicate_id:SIG-001525 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-245F7A48D068 | business_signal_library | 0.92 | False | duplicate_id:SIG-001529 | Rejected |
| CAND-5D56584D68AD | business_signal_library | 0.88 | False | duplicate_id:SIG-001527 | Rejected |
| CAND-94BF23D67141 | business_signal_library | 0.9 | False | duplicate_id:SIG-001528 | Rejected |
| CAND-B8E1A02F4173 | business_signal_library | 0.92 | False | duplicate_id:SIG-001526 | Rejected |
| CAND-A63B0ECE7465 | business_signal_library | 0.9 | False | duplicate_id:SIG-001525 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001529` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
