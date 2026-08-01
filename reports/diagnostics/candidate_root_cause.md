# Candidate Root Cause

**Generated:** 2026-08-01T18:20:31+00:00
**Session:** `SESSION-20260801-D5E489`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001221`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260801-D5E489`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001221': 1, 'duplicate_id:SIG-001220': 1, 'duplicate_id:SIG-001222': 1, 'duplicate_id:SIG-001223': 1, 'duplicate_id:SIG-001224': 1}`
- `candidate CAND-FA77FD8E086E entity_id=SIG-001221 reason=duplicate_id:SIG-001221 conf=0.92`
- `candidate CAND-544F0ED9A6C4 entity_id=SIG-001220 reason=duplicate_id:SIG-001220 conf=0.9`
- `candidate CAND-1236F090CCC8 entity_id=SIG-001222 reason=duplicate_id:SIG-001222 conf=0.88`
- `candidate CAND-BC59406A3176 entity_id=SIG-001223 reason=duplicate_id:SIG-001223 conf=0.9`
- `candidate CAND-988C43EE8A86 entity_id=SIG-001224 reason=duplicate_id:SIG-001224 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FA77FD8E086E | business_signal_library | 0.92 | False | duplicate_id:SIG-001221 | Rejected |
| CAND-544F0ED9A6C4 | business_signal_library | 0.9 | False | duplicate_id:SIG-001220 | Rejected |
| CAND-1236F090CCC8 | business_signal_library | 0.88 | False | duplicate_id:SIG-001222 | Rejected |
| CAND-BC59406A3176 | business_signal_library | 0.9 | False | duplicate_id:SIG-001223 | Rejected |
| CAND-988C43EE8A86 | business_signal_library | 0.92 | False | duplicate_id:SIG-001224 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001221` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
