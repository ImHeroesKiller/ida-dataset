# Candidate Root Cause

**Generated:** 2026-08-01T20:27:42+00:00
**Session:** `SESSION-20260801-BFACDF`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001227`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260801-BFACDF`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001227': 1, 'duplicate_id:SIG-001228': 1, 'duplicate_id:SIG-001229': 1, 'duplicate_id:SIG-001225': 1, 'duplicate_id:SIG-001226': 1}`
- `candidate CAND-AE0D7E8F9891 entity_id=SIG-001227 reason=duplicate_id:SIG-001227 conf=0.88`
- `candidate CAND-B177876F6A07 entity_id=SIG-001228 reason=duplicate_id:SIG-001228 conf=0.9`
- `candidate CAND-CEEEA4BF9668 entity_id=SIG-001229 reason=duplicate_id:SIG-001229 conf=0.92`
- `candidate CAND-4D07CA53FAE6 entity_id=SIG-001225 reason=duplicate_id:SIG-001225 conf=0.9`
- `candidate CAND-F4EAA1CACCA3 entity_id=SIG-001226 reason=duplicate_id:SIG-001226 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-AE0D7E8F9891 | business_signal_library | 0.88 | False | duplicate_id:SIG-001227 | Rejected |
| CAND-B177876F6A07 | business_signal_library | 0.9 | False | duplicate_id:SIG-001228 | Rejected |
| CAND-CEEEA4BF9668 | business_signal_library | 0.92 | False | duplicate_id:SIG-001229 | Rejected |
| CAND-4D07CA53FAE6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001225 | Rejected |
| CAND-F4EAA1CACCA3 | business_signal_library | 0.92 | False | duplicate_id:SIG-001226 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001227` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
