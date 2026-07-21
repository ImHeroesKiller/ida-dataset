# Candidate Root Cause

**Generated:** 2026-07-21T21:32:45+00:00
**Session:** `SESSION-20260721-DD0E7C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000649`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260721-DD0E7C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000649': 1, 'duplicate_id:SIG-000645': 1, 'duplicate_id:SIG-000647': 1, 'duplicate_id:SIG-000648': 1, 'duplicate_id:SIG-000646': 1}`
- `candidate CAND-C63617407EB1 entity_id=SIG-000649 reason=duplicate_id:SIG-000649 conf=0.92`
- `candidate CAND-901276AD644E entity_id=SIG-000645 reason=duplicate_id:SIG-000645 conf=0.9`
- `candidate CAND-AE1159449DE5 entity_id=SIG-000647 reason=duplicate_id:SIG-000647 conf=0.88`
- `candidate CAND-56CA8B2F47F1 entity_id=SIG-000648 reason=duplicate_id:SIG-000648 conf=0.9`
- `candidate CAND-40D3158FE987 entity_id=SIG-000646 reason=duplicate_id:SIG-000646 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C63617407EB1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000649 | Rejected |
| CAND-901276AD644E | business_signal_library | 0.9 | False | duplicate_id:SIG-000645 | Rejected |
| CAND-AE1159449DE5 | business_signal_library | 0.88 | False | duplicate_id:SIG-000647 | Rejected |
| CAND-56CA8B2F47F1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000648 | Rejected |
| CAND-40D3158FE987 | business_signal_library | 0.92 | False | duplicate_id:SIG-000646 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000649` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
