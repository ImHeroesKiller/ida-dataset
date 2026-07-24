# Candidate Root Cause

**Generated:** 2026-07-24T12:46:40+00:00
**Session:** `SESSION-20260724-A7B211`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000782`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260724-A7B211`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000782': 1, 'duplicate_id:SIG-000780': 1, 'duplicate_id:SIG-000781': 1, 'duplicate_id:SIG-000783': 1, 'duplicate_id:SIG-000784': 1}`
- `candidate CAND-933A90BBC5B6 entity_id=SIG-000782 reason=duplicate_id:SIG-000782 conf=0.88`
- `candidate CAND-960A53783439 entity_id=SIG-000780 reason=duplicate_id:SIG-000780 conf=0.9`
- `candidate CAND-DE536DA5179F entity_id=SIG-000781 reason=duplicate_id:SIG-000781 conf=0.92`
- `candidate CAND-5CD8F47309E6 entity_id=SIG-000783 reason=duplicate_id:SIG-000783 conf=0.9`
- `candidate CAND-1F8A2D33ACAD entity_id=SIG-000784 reason=duplicate_id:SIG-000784 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-933A90BBC5B6 | business_signal_library | 0.88 | False | duplicate_id:SIG-000782 | Rejected |
| CAND-960A53783439 | business_signal_library | 0.9 | False | duplicate_id:SIG-000780 | Rejected |
| CAND-DE536DA5179F | business_signal_library | 0.92 | False | duplicate_id:SIG-000781 | Rejected |
| CAND-5CD8F47309E6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000783 | Rejected |
| CAND-1F8A2D33ACAD | business_signal_library | 0.92 | False | duplicate_id:SIG-000784 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000782` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
