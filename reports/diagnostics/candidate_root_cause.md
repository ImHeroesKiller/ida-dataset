# Candidate Root Cause

**Generated:** 2026-07-15T20:34:42+00:00
**Session:** `SESSION-20260715-BBC621`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000277`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260715-BBC621`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000277': 1, 'duplicate_id:SIG-000276': 1, 'duplicate_id:SIG-000279': 1, 'duplicate_id:SIG-000278': 1, 'duplicate_id:SIG-000275': 1}`
- `candidate CAND-73669B722259 entity_id=SIG-000277 reason=duplicate_id:SIG-000277 conf=0.88`
- `candidate CAND-D70296C73563 entity_id=SIG-000276 reason=duplicate_id:SIG-000276 conf=0.92`
- `candidate CAND-8B5C4E38E467 entity_id=SIG-000279 reason=duplicate_id:SIG-000279 conf=0.9`
- `candidate CAND-8F934284A5BD entity_id=SIG-000278 reason=duplicate_id:SIG-000278 conf=0.85`
- `candidate CAND-3840D11A0592 entity_id=SIG-000275 reason=duplicate_id:SIG-000275 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-73669B722259 | business_signal_library | 0.88 | False | duplicate_id:SIG-000277 | Rejected |
| CAND-D70296C73563 | business_signal_library | 0.92 | False | duplicate_id:SIG-000276 | Rejected |
| CAND-8B5C4E38E467 | business_signal_library | 0.9 | False | duplicate_id:SIG-000279 | Rejected |
| CAND-8F934284A5BD | business_signal_library | 0.85 | False | duplicate_id:SIG-000278 | Rejected |
| CAND-3840D11A0592 | business_signal_library | 0.9 | False | duplicate_id:SIG-000275 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000277` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
