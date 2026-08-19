# Candidate Root Cause

**Generated:** 2026-08-19T23:42:28+00:00
**Session:** `SESSION-20260819-2E981E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000728`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-2E981E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000728': 1, 'duplicate_id:SIG-000730': 1, 'duplicate_id:SIG-000726': 1, 'duplicate_id:SIG-000727': 1, 'duplicate_id:SIG-000729': 1}`
- `candidate CAND-49B88F06F840 entity_id=SIG-000728 reason=duplicate_id:SIG-000728 conf=0.9`
- `candidate CAND-303EF501096C entity_id=SIG-000730 reason=duplicate_id:SIG-000730 conf=0.9`
- `candidate CAND-FAC1FFCCF606 entity_id=SIG-000726 reason=duplicate_id:SIG-000726 conf=0.92`
- `candidate CAND-3E81B06E22AA entity_id=SIG-000727 reason=duplicate_id:SIG-000727 conf=0.9`
- `candidate CAND-32E653FE16C2 entity_id=SIG-000729 reason=duplicate_id:SIG-000729 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-49B88F06F840 | business_signal_library | 0.9 | False | duplicate_id:SIG-000728 | Rejected |
| CAND-303EF501096C | business_signal_library | 0.9 | False | duplicate_id:SIG-000730 | Rejected |
| CAND-FAC1FFCCF606 | business_signal_library | 0.92 | False | duplicate_id:SIG-000726 | Rejected |
| CAND-3E81B06E22AA | business_signal_library | 0.9 | False | duplicate_id:SIG-000727 | Rejected |
| CAND-32E653FE16C2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000729 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000728` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
