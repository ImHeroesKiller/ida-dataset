# Candidate Root Cause

**Generated:** 2026-08-17T08:11:33+00:00
**Session:** `SESSION-20260817-EA5CE0`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000417`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-EA5CE0`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000417': 1, 'duplicate_id:SIG-000416': 1, 'duplicate_id:SIG-000420': 1, 'duplicate_id:SIG-000418': 1, 'duplicate_id:SIG-000419': 1}`
- `candidate CAND-D27606BF0501 entity_id=SIG-000417 reason=duplicate_id:SIG-000417 conf=0.9`
- `candidate CAND-8A505386F251 entity_id=SIG-000416 reason=duplicate_id:SIG-000416 conf=0.92`
- `candidate CAND-EEA2E51AFD4C entity_id=SIG-000420 reason=duplicate_id:SIG-000420 conf=0.9`
- `candidate CAND-A382708BF971 entity_id=SIG-000418 reason=duplicate_id:SIG-000418 conf=0.9`
- `candidate CAND-B3CC7A4548CA entity_id=SIG-000419 reason=duplicate_id:SIG-000419 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D27606BF0501 | business_signal_library | 0.9 | False | duplicate_id:SIG-000417 | Rejected |
| CAND-8A505386F251 | business_signal_library | 0.92 | False | duplicate_id:SIG-000416 | Rejected |
| CAND-EEA2E51AFD4C | business_signal_library | 0.9 | False | duplicate_id:SIG-000420 | Rejected |
| CAND-A382708BF971 | business_signal_library | 0.9 | False | duplicate_id:SIG-000418 | Rejected |
| CAND-B3CC7A4548CA | business_signal_library | 0.9 | False | duplicate_id:SIG-000419 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000417` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
