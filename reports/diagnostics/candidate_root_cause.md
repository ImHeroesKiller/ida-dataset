# Candidate Root Cause

**Generated:** 2026-08-21T19:45:15+00:00
**Session:** `SESSION-20260821-07C58A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000935`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-07C58A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000935': 1, 'duplicate_id:SIG-000931': 1, 'duplicate_id:SIG-000932': 1, 'duplicate_id:SIG-000934': 1, 'duplicate_id:SIG-000933': 1}`
- `candidate CAND-56304B224769 entity_id=SIG-000935 reason=duplicate_id:SIG-000935 conf=0.9`
- `candidate CAND-8B05497A92A0 entity_id=SIG-000931 reason=duplicate_id:SIG-000931 conf=0.92`
- `candidate CAND-CE523362EAFE entity_id=SIG-000932 reason=duplicate_id:SIG-000932 conf=0.9`
- `candidate CAND-4BF18E10C2D3 entity_id=SIG-000934 reason=duplicate_id:SIG-000934 conf=0.9`
- `candidate CAND-3D58CB6F0ED7 entity_id=SIG-000933 reason=duplicate_id:SIG-000933 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-56304B224769 | business_signal_library | 0.9 | False | duplicate_id:SIG-000935 | Rejected |
| CAND-8B05497A92A0 | business_signal_library | 0.92 | False | duplicate_id:SIG-000931 | Rejected |
| CAND-CE523362EAFE | business_signal_library | 0.9 | False | duplicate_id:SIG-000932 | Rejected |
| CAND-4BF18E10C2D3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000934 | Rejected |
| CAND-3D58CB6F0ED7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000933 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000935` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
