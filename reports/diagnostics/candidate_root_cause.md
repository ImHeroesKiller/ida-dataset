# Candidate Root Cause

**Generated:** 2026-07-26T06:27:29+00:00
**Session:** `SESSION-20260726-F3D8B3`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000882`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260726-F3D8B3`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000882': 1, 'duplicate_id:SIG-000883': 1, 'duplicate_id:SIG-000881': 1, 'duplicate_id:SIG-000880': 1, 'duplicate_id:SIG-000884': 1}`
- `candidate CAND-008602DDAB28 entity_id=SIG-000882 reason=duplicate_id:SIG-000882 conf=0.88`
- `candidate CAND-E202186D791D entity_id=SIG-000883 reason=duplicate_id:SIG-000883 conf=0.9`
- `candidate CAND-D946ED378877 entity_id=SIG-000881 reason=duplicate_id:SIG-000881 conf=0.92`
- `candidate CAND-C0CBAD3ABE52 entity_id=SIG-000880 reason=duplicate_id:SIG-000880 conf=0.9`
- `candidate CAND-0B3629F52836 entity_id=SIG-000884 reason=duplicate_id:SIG-000884 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-008602DDAB28 | business_signal_library | 0.88 | False | duplicate_id:SIG-000882 | Rejected |
| CAND-E202186D791D | business_signal_library | 0.9 | False | duplicate_id:SIG-000883 | Rejected |
| CAND-D946ED378877 | business_signal_library | 0.92 | False | duplicate_id:SIG-000881 | Rejected |
| CAND-C0CBAD3ABE52 | business_signal_library | 0.9 | False | duplicate_id:SIG-000880 | Rejected |
| CAND-0B3629F52836 | business_signal_library | 0.92 | False | duplicate_id:SIG-000884 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000882` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
