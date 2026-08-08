# Candidate Root Cause

**Generated:** 2026-08-08T11:49:22+00:00
**Session:** `SESSION-20260808-02017E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001613`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-02017E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001613': 1, 'duplicate_id:SIG-001614': 1, 'duplicate_id:SIG-001610': 1, 'duplicate_id:SIG-001611': 1, 'duplicate_id:SIG-001612': 1}`
- `candidate CAND-D40E74990A59 entity_id=SIG-001613 reason=duplicate_id:SIG-001613 conf=0.9`
- `candidate CAND-08EE430AA88D entity_id=SIG-001614 reason=duplicate_id:SIG-001614 conf=0.92`
- `candidate CAND-FB70BE987DA8 entity_id=SIG-001610 reason=duplicate_id:SIG-001610 conf=0.9`
- `candidate CAND-B14E47EEC9F6 entity_id=SIG-001611 reason=duplicate_id:SIG-001611 conf=0.92`
- `candidate CAND-429E50FDEF23 entity_id=SIG-001612 reason=duplicate_id:SIG-001612 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D40E74990A59 | business_signal_library | 0.9 | False | duplicate_id:SIG-001613 | Rejected |
| CAND-08EE430AA88D | business_signal_library | 0.92 | False | duplicate_id:SIG-001614 | Rejected |
| CAND-FB70BE987DA8 | business_signal_library | 0.9 | False | duplicate_id:SIG-001610 | Rejected |
| CAND-B14E47EEC9F6 | business_signal_library | 0.92 | False | duplicate_id:SIG-001611 | Rejected |
| CAND-429E50FDEF23 | business_signal_library | 0.88 | False | duplicate_id:SIG-001612 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001613` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
