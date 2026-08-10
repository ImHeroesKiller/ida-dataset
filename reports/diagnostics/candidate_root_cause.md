# Candidate Root Cause

**Generated:** 2026-08-10T18:10:55+00:00
**Session:** `SESSION-20260810-789390`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001829`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-789390`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001829': 1, 'duplicate_id:SIG-001828': 1, 'duplicate_id:SIG-001827': 1, 'duplicate_id:SIG-001826': 1, 'duplicate_id:SIG-001825': 1}`
- `candidate CAND-782DBED75ED6 entity_id=SIG-001829 reason=duplicate_id:SIG-001829 conf=0.92`
- `candidate CAND-A5E76FE29947 entity_id=SIG-001828 reason=duplicate_id:SIG-001828 conf=0.9`
- `candidate CAND-1A794ED0AE85 entity_id=SIG-001827 reason=duplicate_id:SIG-001827 conf=0.88`
- `candidate CAND-CB21912CEEC7 entity_id=SIG-001826 reason=duplicate_id:SIG-001826 conf=0.92`
- `candidate CAND-2C1DA711BB5E entity_id=SIG-001825 reason=duplicate_id:SIG-001825 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-782DBED75ED6 | business_signal_library | 0.92 | False | duplicate_id:SIG-001829 | Rejected |
| CAND-A5E76FE29947 | business_signal_library | 0.9 | False | duplicate_id:SIG-001828 | Rejected |
| CAND-1A794ED0AE85 | business_signal_library | 0.88 | False | duplicate_id:SIG-001827 | Rejected |
| CAND-CB21912CEEC7 | business_signal_library | 0.92 | False | duplicate_id:SIG-001826 | Rejected |
| CAND-2C1DA711BB5E | business_signal_library | 0.9 | False | duplicate_id:SIG-001825 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001829` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
