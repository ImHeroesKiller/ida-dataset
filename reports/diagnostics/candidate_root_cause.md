# Candidate Root Cause

**Generated:** 2026-07-19T03:15:28+00:00
**Session:** `SESSION-20260719-E267C8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000484`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260719-E267C8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000484': 1, 'duplicate_id:SIG-000481': 1, 'duplicate_id:SIG-000483': 1, 'duplicate_id:SIG-000482': 1, 'duplicate_id:SIG-000480': 1}`
- `candidate CAND-1E62163EA8AF entity_id=SIG-000484 reason=duplicate_id:SIG-000484 conf=0.92`
- `candidate CAND-D4EC8AA7A549 entity_id=SIG-000481 reason=duplicate_id:SIG-000481 conf=0.92`
- `candidate CAND-8A81E489C6E8 entity_id=SIG-000483 reason=duplicate_id:SIG-000483 conf=0.9`
- `candidate CAND-9BF8CB4823E0 entity_id=SIG-000482 reason=duplicate_id:SIG-000482 conf=0.88`
- `candidate CAND-DA178F38C24B entity_id=SIG-000480 reason=duplicate_id:SIG-000480 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-1E62163EA8AF | business_signal_library | 0.92 | False | duplicate_id:SIG-000484 | Rejected |
| CAND-D4EC8AA7A549 | business_signal_library | 0.92 | False | duplicate_id:SIG-000481 | Rejected |
| CAND-8A81E489C6E8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000483 | Rejected |
| CAND-9BF8CB4823E0 | business_signal_library | 0.88 | False | duplicate_id:SIG-000482 | Rejected |
| CAND-DA178F38C24B | business_signal_library | 0.9 | False | duplicate_id:SIG-000480 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000484` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
