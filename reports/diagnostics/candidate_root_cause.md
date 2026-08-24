# Candidate Root Cause

**Generated:** 2026-08-24T13:11:42+00:00
**Session:** `SESSION-20260824-8E6ED1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001226`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260824-8E6ED1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001226': 1, 'duplicate_id:SIG-001229': 1, 'duplicate_id:SIG-001228': 1, 'duplicate_id:SIG-001227': 1, 'duplicate_id:SIG-001230': 1}`
- `candidate CAND-25AB1669A5B4 entity_id=SIG-001226 reason=duplicate_id:SIG-001226 conf=0.92`
- `candidate CAND-4A646C5C30E6 entity_id=SIG-001229 reason=duplicate_id:SIG-001229 conf=0.9`
- `candidate CAND-4F328416BCE5 entity_id=SIG-001228 reason=duplicate_id:SIG-001228 conf=0.9`
- `candidate CAND-4613F5A3B2C6 entity_id=SIG-001227 reason=duplicate_id:SIG-001227 conf=0.9`
- `candidate CAND-2A1895F7F312 entity_id=SIG-001230 reason=duplicate_id:SIG-001230 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-25AB1669A5B4 | business_signal_library | 0.92 | False | duplicate_id:SIG-001226 | Rejected |
| CAND-4A646C5C30E6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001229 | Rejected |
| CAND-4F328416BCE5 | business_signal_library | 0.9 | False | duplicate_id:SIG-001228 | Rejected |
| CAND-4613F5A3B2C6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001227 | Rejected |
| CAND-2A1895F7F312 | business_signal_library | 0.9 | False | duplicate_id:SIG-001230 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001226` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
