# Candidate Root Cause

**Generated:** 2026-07-29T00:17:24+00:00
**Session:** `SESSION-20260728-861443`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001023`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260728-861443`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001023': 1, 'duplicate_id:SIG-001020': 1, 'duplicate_id:SIG-001024': 1, 'duplicate_id:SIG-001021': 1, 'duplicate_id:SIG-001022': 1}`
- `candidate CAND-89EB6CD8A59E entity_id=SIG-001023 reason=duplicate_id:SIG-001023 conf=0.9`
- `candidate CAND-B2A01D49D0BC entity_id=SIG-001020 reason=duplicate_id:SIG-001020 conf=0.9`
- `candidate CAND-9D6FB2D0B6F7 entity_id=SIG-001024 reason=duplicate_id:SIG-001024 conf=0.92`
- `candidate CAND-46B3EAF4AAA9 entity_id=SIG-001021 reason=duplicate_id:SIG-001021 conf=0.92`
- `candidate CAND-F46FD5C469A7 entity_id=SIG-001022 reason=duplicate_id:SIG-001022 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-89EB6CD8A59E | business_signal_library | 0.9 | False | duplicate_id:SIG-001023 | Rejected |
| CAND-B2A01D49D0BC | business_signal_library | 0.9 | False | duplicate_id:SIG-001020 | Rejected |
| CAND-9D6FB2D0B6F7 | business_signal_library | 0.92 | False | duplicate_id:SIG-001024 | Rejected |
| CAND-46B3EAF4AAA9 | business_signal_library | 0.92 | False | duplicate_id:SIG-001021 | Rejected |
| CAND-F46FD5C469A7 | business_signal_library | 0.88 | False | duplicate_id:SIG-001022 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001023` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
