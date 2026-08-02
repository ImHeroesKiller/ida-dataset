# Candidate Root Cause

**Generated:** 2026-08-02T13:42:55+00:00
**Session:** `SESSION-20260802-FB6DD6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001267`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260802-FB6DD6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001267': 1, 'duplicate_id:SIG-001266': 1, 'duplicate_id:SIG-001268': 1, 'duplicate_id:SIG-001269': 1, 'duplicate_id:SIG-001265': 1}`
- `candidate CAND-2ECB9D2CC83E entity_id=SIG-001267 reason=duplicate_id:SIG-001267 conf=0.88`
- `candidate CAND-8C6701305469 entity_id=SIG-001266 reason=duplicate_id:SIG-001266 conf=0.92`
- `candidate CAND-08457F44E1BD entity_id=SIG-001268 reason=duplicate_id:SIG-001268 conf=0.9`
- `candidate CAND-D7BDB9ED651D entity_id=SIG-001269 reason=duplicate_id:SIG-001269 conf=0.92`
- `candidate CAND-131E88D60222 entity_id=SIG-001265 reason=duplicate_id:SIG-001265 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2ECB9D2CC83E | business_signal_library | 0.88 | False | duplicate_id:SIG-001267 | Rejected |
| CAND-8C6701305469 | business_signal_library | 0.92 | False | duplicate_id:SIG-001266 | Rejected |
| CAND-08457F44E1BD | business_signal_library | 0.9 | False | duplicate_id:SIG-001268 | Rejected |
| CAND-D7BDB9ED651D | business_signal_library | 0.92 | False | duplicate_id:SIG-001269 | Rejected |
| CAND-131E88D60222 | business_signal_library | 0.9 | False | duplicate_id:SIG-001265 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001267` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
