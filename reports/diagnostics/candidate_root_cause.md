# Candidate Root Cause

**Generated:** 2026-08-09T22:53:58+00:00
**Session:** `SESSION-20260809-EDD07E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001771`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-EDD07E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001771': 1, 'duplicate_id:SIG-001774': 1, 'duplicate_id:SIG-001770': 1, 'duplicate_id:SIG-001772': 1, 'duplicate_id:SIG-001773': 1}`
- `candidate CAND-8329E1F744FA entity_id=SIG-001771 reason=duplicate_id:SIG-001771 conf=0.92`
- `candidate CAND-23E4829C0DE9 entity_id=SIG-001774 reason=duplicate_id:SIG-001774 conf=0.92`
- `candidate CAND-068AE516BB69 entity_id=SIG-001770 reason=duplicate_id:SIG-001770 conf=0.9`
- `candidate CAND-7B2E6CFACD5A entity_id=SIG-001772 reason=duplicate_id:SIG-001772 conf=0.88`
- `candidate CAND-CC42BCAED22C entity_id=SIG-001773 reason=duplicate_id:SIG-001773 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-8329E1F744FA | business_signal_library | 0.92 | False | duplicate_id:SIG-001771 | Rejected |
| CAND-23E4829C0DE9 | business_signal_library | 0.92 | False | duplicate_id:SIG-001774 | Rejected |
| CAND-068AE516BB69 | business_signal_library | 0.9 | False | duplicate_id:SIG-001770 | Rejected |
| CAND-7B2E6CFACD5A | business_signal_library | 0.88 | False | duplicate_id:SIG-001772 | Rejected |
| CAND-CC42BCAED22C | business_signal_library | 0.9 | False | duplicate_id:SIG-001773 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001771` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
