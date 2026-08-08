# Candidate Root Cause

**Generated:** 2026-08-08T19:00:42+00:00
**Session:** `SESSION-20260808-258FEF`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001645`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-258FEF`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001645': 1, 'duplicate_id:SIG-001649': 1, 'duplicate_id:SIG-001646': 1, 'duplicate_id:SIG-001648': 1, 'duplicate_id:SIG-001647': 1}`
- `candidate CAND-DB267D65B039 entity_id=SIG-001645 reason=duplicate_id:SIG-001645 conf=0.9`
- `candidate CAND-679D5359EF45 entity_id=SIG-001649 reason=duplicate_id:SIG-001649 conf=0.92`
- `candidate CAND-E0B6E3BC28B1 entity_id=SIG-001646 reason=duplicate_id:SIG-001646 conf=0.92`
- `candidate CAND-D0DC108B89C9 entity_id=SIG-001648 reason=duplicate_id:SIG-001648 conf=0.9`
- `candidate CAND-0DE0829B70FB entity_id=SIG-001647 reason=duplicate_id:SIG-001647 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DB267D65B039 | business_signal_library | 0.9 | False | duplicate_id:SIG-001645 | Rejected |
| CAND-679D5359EF45 | business_signal_library | 0.92 | False | duplicate_id:SIG-001649 | Rejected |
| CAND-E0B6E3BC28B1 | business_signal_library | 0.92 | False | duplicate_id:SIG-001646 | Rejected |
| CAND-D0DC108B89C9 | business_signal_library | 0.9 | False | duplicate_id:SIG-001648 | Rejected |
| CAND-0DE0829B70FB | business_signal_library | 0.88 | False | duplicate_id:SIG-001647 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001645` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
