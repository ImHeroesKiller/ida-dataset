# Candidate Root Cause

**Generated:** 2026-08-10T04:22:59+00:00
**Session:** `SESSION-20260810-45FAAB`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001785`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-45FAAB`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001785': 1, 'duplicate_id:SIG-001787': 1, 'duplicate_id:SIG-001786': 1, 'duplicate_id:SIG-001789': 1, 'duplicate_id:SIG-001788': 1}`
- `candidate CAND-98A53C852A59 entity_id=SIG-001785 reason=duplicate_id:SIG-001785 conf=0.9`
- `candidate CAND-78FBC3F094B5 entity_id=SIG-001787 reason=duplicate_id:SIG-001787 conf=0.88`
- `candidate CAND-CD33AA4FA6B6 entity_id=SIG-001786 reason=duplicate_id:SIG-001786 conf=0.92`
- `candidate CAND-355D43E6575C entity_id=SIG-001789 reason=duplicate_id:SIG-001789 conf=0.92`
- `candidate CAND-8FBC9A9D6813 entity_id=SIG-001788 reason=duplicate_id:SIG-001788 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-98A53C852A59 | business_signal_library | 0.9 | False | duplicate_id:SIG-001785 | Rejected |
| CAND-78FBC3F094B5 | business_signal_library | 0.88 | False | duplicate_id:SIG-001787 | Rejected |
| CAND-CD33AA4FA6B6 | business_signal_library | 0.92 | False | duplicate_id:SIG-001786 | Rejected |
| CAND-355D43E6575C | business_signal_library | 0.92 | False | duplicate_id:SIG-001789 | Rejected |
| CAND-8FBC9A9D6813 | business_signal_library | 0.9 | False | duplicate_id:SIG-001788 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001785` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
