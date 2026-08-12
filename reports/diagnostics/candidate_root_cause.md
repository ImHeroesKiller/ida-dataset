# Candidate Root Cause

**Generated:** 2026-08-12T08:37:18+00:00
**Session:** `SESSION-20260812-04DE3C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001963`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260812-04DE3C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001963': 1, 'duplicate_id:SIG-001964': 1, 'duplicate_id:SIG-001962': 1, 'duplicate_id:SIG-001960': 1, 'duplicate_id:SIG-001961': 1}`
- `candidate CAND-94A6838C4D52 entity_id=SIG-001963 reason=duplicate_id:SIG-001963 conf=0.92`
- `candidate CAND-3EB74B177C8A entity_id=SIG-001964 reason=duplicate_id:SIG-001964 conf=0.9`
- `candidate CAND-F456975D940B entity_id=SIG-001962 reason=duplicate_id:SIG-001962 conf=0.9`
- `candidate CAND-B45DE3F1A2AE entity_id=SIG-001960 reason=duplicate_id:SIG-001960 conf=0.9`
- `candidate CAND-B5A8DFB7CD43 entity_id=SIG-001961 reason=duplicate_id:SIG-001961 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-94A6838C4D52 | business_signal_library | 0.92 | False | duplicate_id:SIG-001963 | Rejected |
| CAND-3EB74B177C8A | business_signal_library | 0.9 | False | duplicate_id:SIG-001964 | Rejected |
| CAND-F456975D940B | business_signal_library | 0.9 | False | duplicate_id:SIG-001962 | Rejected |
| CAND-B45DE3F1A2AE | business_signal_library | 0.9 | False | duplicate_id:SIG-001960 | Rejected |
| CAND-B5A8DFB7CD43 | business_signal_library | 0.92 | False | duplicate_id:SIG-001961 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001963` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
