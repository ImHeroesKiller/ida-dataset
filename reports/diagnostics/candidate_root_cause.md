# Candidate Root Cause

**Generated:** 2026-08-14T23:36:51+00:00
**Session:** `SESSION-20260814-8ED1C5`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000164`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-8ED1C5`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000164': 1, 'duplicate_id:SIG-000161': 1, 'duplicate_id:SIG-000165': 1, 'duplicate_id:SIG-000162': 1, 'duplicate_id:SIG-000163': 1}`
- `candidate CAND-50168A60D0BF entity_id=SIG-000164 reason=duplicate_id:SIG-000164 conf=0.9`
- `candidate CAND-5B7101C9A6ED entity_id=SIG-000161 reason=duplicate_id:SIG-000161 conf=0.92`
- `candidate CAND-FC63F8A8F318 entity_id=SIG-000165 reason=duplicate_id:SIG-000165 conf=0.9`
- `candidate CAND-53E5EB59F8D3 entity_id=SIG-000162 reason=duplicate_id:SIG-000162 conf=0.9`
- `candidate CAND-65A713DD4FC3 entity_id=SIG-000163 reason=duplicate_id:SIG-000163 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-50168A60D0BF | business_signal_library | 0.9 | False | duplicate_id:SIG-000164 | Rejected |
| CAND-5B7101C9A6ED | business_signal_library | 0.92 | False | duplicate_id:SIG-000161 | Rejected |
| CAND-FC63F8A8F318 | business_signal_library | 0.9 | False | duplicate_id:SIG-000165 | Rejected |
| CAND-53E5EB59F8D3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000162 | Rejected |
| CAND-65A713DD4FC3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000163 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000164` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
