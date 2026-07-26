# Candidate Root Cause

**Generated:** 2026-07-26T22:26:46+00:00
**Session:** `SESSION-20260726-6E6706`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000926`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260726-6E6706`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000926': 1, 'duplicate_id:SIG-000925': 1, 'duplicate_id:SIG-000927': 1, 'duplicate_id:SIG-000928': 1, 'duplicate_id:SIG-000929': 1}`
- `candidate CAND-104AF4579E4C entity_id=SIG-000926 reason=duplicate_id:SIG-000926 conf=0.92`
- `candidate CAND-A257547E04BE entity_id=SIG-000925 reason=duplicate_id:SIG-000925 conf=0.9`
- `candidate CAND-524CDDD829E6 entity_id=SIG-000927 reason=duplicate_id:SIG-000927 conf=0.88`
- `candidate CAND-4A36CD5699E6 entity_id=SIG-000928 reason=duplicate_id:SIG-000928 conf=0.9`
- `candidate CAND-B48D7B32E36C entity_id=SIG-000929 reason=duplicate_id:SIG-000929 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-104AF4579E4C | business_signal_library | 0.92 | False | duplicate_id:SIG-000926 | Rejected |
| CAND-A257547E04BE | business_signal_library | 0.9 | False | duplicate_id:SIG-000925 | Rejected |
| CAND-524CDDD829E6 | business_signal_library | 0.88 | False | duplicate_id:SIG-000927 | Rejected |
| CAND-4A36CD5699E6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000928 | Rejected |
| CAND-B48D7B32E36C | business_signal_library | 0.92 | False | duplicate_id:SIG-000929 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000926` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
