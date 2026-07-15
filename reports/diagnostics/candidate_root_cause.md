# Candidate Root Cause

**Generated:** 2026-07-15T03:02:01+00:00
**Session:** `SESSION-20260715-D0B11B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000238`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260715-D0B11B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000238': 1, 'duplicate_id:SIG-000235': 1, 'duplicate_id:SIG-000239': 1, 'duplicate_id:SIG-000237': 1, 'duplicate_id:SIG-000236': 1}`
- `candidate CAND-CDF033653832 entity_id=SIG-000238 reason=duplicate_id:SIG-000238 conf=0.85`
- `candidate CAND-8BDDC31129B6 entity_id=SIG-000235 reason=duplicate_id:SIG-000235 conf=0.9`
- `candidate CAND-C6A1D7676555 entity_id=SIG-000239 reason=duplicate_id:SIG-000239 conf=0.9`
- `candidate CAND-6E5663346717 entity_id=SIG-000237 reason=duplicate_id:SIG-000237 conf=0.92`
- `candidate CAND-DB2A8FC5CD05 entity_id=SIG-000236 reason=duplicate_id:SIG-000236 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-CDF033653832 | business_signal_library | 0.85 | False | duplicate_id:SIG-000238 | Rejected |
| CAND-8BDDC31129B6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000235 | Rejected |
| CAND-C6A1D7676555 | business_signal_library | 0.9 | False | duplicate_id:SIG-000239 | Rejected |
| CAND-6E5663346717 | business_signal_library | 0.92 | False | duplicate_id:SIG-000237 | Rejected |
| CAND-DB2A8FC5CD05 | business_signal_library | 0.88 | False | duplicate_id:SIG-000236 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000238` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
