# Candidate Root Cause

**Generated:** 2026-08-13T16:19:02+00:00
**Session:** `SESSION-20260813-AA629B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000041`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260813-AA629B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000041': 1, 'duplicate_id:SIG-000044': 1, 'duplicate_id:SIG-000042': 1, 'duplicate_id:SIG-000043': 1, 'duplicate_id:SIG-000045': 1}`
- `candidate CAND-DC9ED724F886 entity_id=SIG-000041 reason=duplicate_id:SIG-000041 conf=0.92`
- `candidate CAND-0141D4462067 entity_id=SIG-000044 reason=duplicate_id:SIG-000044 conf=0.9`
- `candidate CAND-83E6F6025C06 entity_id=SIG-000042 reason=duplicate_id:SIG-000042 conf=0.9`
- `candidate CAND-949485E6FC46 entity_id=SIG-000043 reason=duplicate_id:SIG-000043 conf=0.9`
- `candidate CAND-B8DF777C8E79 entity_id=SIG-000045 reason=duplicate_id:SIG-000045 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DC9ED724F886 | business_signal_library | 0.92 | False | duplicate_id:SIG-000041 | Rejected |
| CAND-0141D4462067 | business_signal_library | 0.9 | False | duplicate_id:SIG-000044 | Rejected |
| CAND-83E6F6025C06 | business_signal_library | 0.9 | False | duplicate_id:SIG-000042 | Rejected |
| CAND-949485E6FC46 | business_signal_library | 0.9 | False | duplicate_id:SIG-000043 | Rejected |
| CAND-B8DF777C8E79 | business_signal_library | 0.9 | False | duplicate_id:SIG-000045 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000041` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
