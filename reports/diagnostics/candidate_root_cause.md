# Candidate Root Cause

**Generated:** 2026-08-21T09:56:24+00:00
**Session:** `SESSION-20260821-8FF67F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000881`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-8FF67F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000881': 1, 'duplicate_id:SIG-000885': 1, 'duplicate_id:SIG-000883': 1, 'duplicate_id:SIG-000884': 1, 'duplicate_id:SIG-000882': 1}`
- `candidate CAND-71A539207046 entity_id=SIG-000881 reason=duplicate_id:SIG-000881 conf=0.92`
- `candidate CAND-F8DA2000B587 entity_id=SIG-000885 reason=duplicate_id:SIG-000885 conf=0.9`
- `candidate CAND-5BE677D65175 entity_id=SIG-000883 reason=duplicate_id:SIG-000883 conf=0.9`
- `candidate CAND-1D44AF6C4606 entity_id=SIG-000884 reason=duplicate_id:SIG-000884 conf=0.9`
- `candidate CAND-7AF171DB9981 entity_id=SIG-000882 reason=duplicate_id:SIG-000882 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-71A539207046 | business_signal_library | 0.92 | False | duplicate_id:SIG-000881 | Rejected |
| CAND-F8DA2000B587 | business_signal_library | 0.9 | False | duplicate_id:SIG-000885 | Rejected |
| CAND-5BE677D65175 | business_signal_library | 0.9 | False | duplicate_id:SIG-000883 | Rejected |
| CAND-1D44AF6C4606 | business_signal_library | 0.9 | False | duplicate_id:SIG-000884 | Rejected |
| CAND-7AF171DB9981 | business_signal_library | 0.9 | False | duplicate_id:SIG-000882 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000881` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
