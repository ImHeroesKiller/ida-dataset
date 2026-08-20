# Candidate Root Cause

**Generated:** 2026-08-20T23:45:19+00:00
**Session:** `SESSION-20260820-45C865`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000841`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-45C865`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000841': 1, 'duplicate_id:SIG-000845': 1, 'duplicate_id:SIG-000843': 1, 'duplicate_id:SIG-000842': 1, 'duplicate_id:SIG-000844': 1}`
- `candidate CAND-D81DB495AA16 entity_id=SIG-000841 reason=duplicate_id:SIG-000841 conf=0.92`
- `candidate CAND-5559ACD99FAA entity_id=SIG-000845 reason=duplicate_id:SIG-000845 conf=0.9`
- `candidate CAND-80BED8619FCE entity_id=SIG-000843 reason=duplicate_id:SIG-000843 conf=0.9`
- `candidate CAND-36BAA6CECFF5 entity_id=SIG-000842 reason=duplicate_id:SIG-000842 conf=0.9`
- `candidate CAND-2C87AF62EFFC entity_id=SIG-000844 reason=duplicate_id:SIG-000844 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D81DB495AA16 | business_signal_library | 0.92 | False | duplicate_id:SIG-000841 | Rejected |
| CAND-5559ACD99FAA | business_signal_library | 0.9 | False | duplicate_id:SIG-000845 | Rejected |
| CAND-80BED8619FCE | business_signal_library | 0.9 | False | duplicate_id:SIG-000843 | Rejected |
| CAND-36BAA6CECFF5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000842 | Rejected |
| CAND-2C87AF62EFFC | business_signal_library | 0.9 | False | duplicate_id:SIG-000844 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000841` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
