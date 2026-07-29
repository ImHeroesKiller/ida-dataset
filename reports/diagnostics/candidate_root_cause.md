# Candidate Root Cause

**Generated:** 2026-07-29T12:20:20+00:00
**Session:** `SESSION-20260729-A3F699`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001048`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260729-A3F699`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001048': 1, 'duplicate_id:SIG-001047': 1, 'duplicate_id:SIG-001045': 1, 'duplicate_id:SIG-001049': 1, 'duplicate_id:SIG-001046': 1}`
- `candidate CAND-DA757E4692C7 entity_id=SIG-001048 reason=duplicate_id:SIG-001048 conf=0.9`
- `candidate CAND-32138B4D7EF0 entity_id=SIG-001047 reason=duplicate_id:SIG-001047 conf=0.88`
- `candidate CAND-2C2F1CA504AE entity_id=SIG-001045 reason=duplicate_id:SIG-001045 conf=0.9`
- `candidate CAND-03BE5E645536 entity_id=SIG-001049 reason=duplicate_id:SIG-001049 conf=0.92`
- `candidate CAND-CBD480FE438A entity_id=SIG-001046 reason=duplicate_id:SIG-001046 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DA757E4692C7 | business_signal_library | 0.9 | False | duplicate_id:SIG-001048 | Rejected |
| CAND-32138B4D7EF0 | business_signal_library | 0.88 | False | duplicate_id:SIG-001047 | Rejected |
| CAND-2C2F1CA504AE | business_signal_library | 0.9 | False | duplicate_id:SIG-001045 | Rejected |
| CAND-03BE5E645536 | business_signal_library | 0.92 | False | duplicate_id:SIG-001049 | Rejected |
| CAND-CBD480FE438A | business_signal_library | 0.92 | False | duplicate_id:SIG-001046 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001048` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
