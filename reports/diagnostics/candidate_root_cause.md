# Candidate Root Cause

**Generated:** 2026-07-26T19:34:01+00:00
**Session:** `SESSION-20260726-F9FE08`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000916`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260726-F9FE08`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000916': 1, 'duplicate_id:SIG-000917': 1, 'duplicate_id:SIG-000919': 1, 'duplicate_id:SIG-000918': 1, 'duplicate_id:SIG-000915': 1}`
- `candidate CAND-3CC9381EC8BC entity_id=SIG-000916 reason=duplicate_id:SIG-000916 conf=0.92`
- `candidate CAND-DF670D4949C8 entity_id=SIG-000917 reason=duplicate_id:SIG-000917 conf=0.88`
- `candidate CAND-636E9C02F1EC entity_id=SIG-000919 reason=duplicate_id:SIG-000919 conf=0.92`
- `candidate CAND-9625EC63103C entity_id=SIG-000918 reason=duplicate_id:SIG-000918 conf=0.9`
- `candidate CAND-D21814F879B6 entity_id=SIG-000915 reason=duplicate_id:SIG-000915 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3CC9381EC8BC | business_signal_library | 0.92 | False | duplicate_id:SIG-000916 | Rejected |
| CAND-DF670D4949C8 | business_signal_library | 0.88 | False | duplicate_id:SIG-000917 | Rejected |
| CAND-636E9C02F1EC | business_signal_library | 0.92 | False | duplicate_id:SIG-000919 | Rejected |
| CAND-9625EC63103C | business_signal_library | 0.9 | False | duplicate_id:SIG-000918 | Rejected |
| CAND-D21814F879B6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000915 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000916` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
