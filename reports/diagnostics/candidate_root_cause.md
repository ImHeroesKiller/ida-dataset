# Candidate Root Cause

**Generated:** 2026-08-18T06:58:41+00:00
**Session:** `SESSION-20260818-08ED9A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000526`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-08ED9A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000526': 1, 'duplicate_id:SIG-000530': 1, 'duplicate_id:SIG-000529': 1, 'duplicate_id:SIG-000528': 1, 'duplicate_id:SIG-000527': 1}`
- `candidate CAND-954A0701CD61 entity_id=SIG-000526 reason=duplicate_id:SIG-000526 conf=0.92`
- `candidate CAND-4CA87695AF86 entity_id=SIG-000530 reason=duplicate_id:SIG-000530 conf=0.9`
- `candidate CAND-4DF619E76A40 entity_id=SIG-000529 reason=duplicate_id:SIG-000529 conf=0.9`
- `candidate CAND-AF29DF3CFBBB entity_id=SIG-000528 reason=duplicate_id:SIG-000528 conf=0.9`
- `candidate CAND-4F59E0088558 entity_id=SIG-000527 reason=duplicate_id:SIG-000527 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-954A0701CD61 | business_signal_library | 0.92 | False | duplicate_id:SIG-000526 | Rejected |
| CAND-4CA87695AF86 | business_signal_library | 0.9 | False | duplicate_id:SIG-000530 | Rejected |
| CAND-4DF619E76A40 | business_signal_library | 0.9 | False | duplicate_id:SIG-000529 | Rejected |
| CAND-AF29DF3CFBBB | business_signal_library | 0.9 | False | duplicate_id:SIG-000528 | Rejected |
| CAND-4F59E0088558 | business_signal_library | 0.9 | False | duplicate_id:SIG-000527 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000526` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
