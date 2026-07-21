# Candidate Root Cause

**Generated:** 2026-07-21T14:15:49+00:00
**Session:** `SESSION-20260721-3555C3`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000625`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260721-3555C3`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000625': 1, 'duplicate_id:SIG-000629': 1, 'duplicate_id:SIG-000628': 1, 'duplicate_id:SIG-000626': 1, 'duplicate_id:SIG-000627': 1}`
- `candidate CAND-7BDD893959CA entity_id=SIG-000625 reason=duplicate_id:SIG-000625 conf=0.9`
- `candidate CAND-C45620304406 entity_id=SIG-000629 reason=duplicate_id:SIG-000629 conf=0.92`
- `candidate CAND-119AF429DAFE entity_id=SIG-000628 reason=duplicate_id:SIG-000628 conf=0.9`
- `candidate CAND-DE89E5E6CC75 entity_id=SIG-000626 reason=duplicate_id:SIG-000626 conf=0.92`
- `candidate CAND-938DED9BD2E6 entity_id=SIG-000627 reason=duplicate_id:SIG-000627 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7BDD893959CA | business_signal_library | 0.9 | False | duplicate_id:SIG-000625 | Rejected |
| CAND-C45620304406 | business_signal_library | 0.92 | False | duplicate_id:SIG-000629 | Rejected |
| CAND-119AF429DAFE | business_signal_library | 0.9 | False | duplicate_id:SIG-000628 | Rejected |
| CAND-DE89E5E6CC75 | business_signal_library | 0.92 | False | duplicate_id:SIG-000626 | Rejected |
| CAND-938DED9BD2E6 | business_signal_library | 0.88 | False | duplicate_id:SIG-000627 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000625` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
