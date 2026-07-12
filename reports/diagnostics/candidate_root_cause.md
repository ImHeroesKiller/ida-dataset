# Candidate Root Cause

**Generated:** 2026-07-12T22:13:08+00:00
**Session:** `SESSION-20260712-48FEED`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000129`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260712-48FEED`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000129': 1, 'duplicate_id:SIG-000125': 1, 'duplicate_id:SIG-000128': 1, 'duplicate_id:SIG-000127': 1, 'duplicate_id:SIG-000126': 1}`
- `candidate CAND-3CAB5ADD289C entity_id=SIG-000129 reason=duplicate_id:SIG-000129 conf=0.92`
- `candidate CAND-2197EDE3A8EA entity_id=SIG-000125 reason=duplicate_id:SIG-000125 conf=0.9`
- `candidate CAND-7F1962DF5802 entity_id=SIG-000128 reason=duplicate_id:SIG-000128 conf=0.9`
- `candidate CAND-517A5C4003E4 entity_id=SIG-000127 reason=duplicate_id:SIG-000127 conf=0.88`
- `candidate CAND-90EE229F9B6E entity_id=SIG-000126 reason=duplicate_id:SIG-000126 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3CAB5ADD289C | business_signal_library | 0.92 | False | duplicate_id:SIG-000129 | Rejected |
| CAND-2197EDE3A8EA | business_signal_library | 0.9 | False | duplicate_id:SIG-000125 | Rejected |
| CAND-7F1962DF5802 | business_signal_library | 0.9 | False | duplicate_id:SIG-000128 | Rejected |
| CAND-517A5C4003E4 | business_signal_library | 0.88 | False | duplicate_id:SIG-000127 | Rejected |
| CAND-90EE229F9B6E | business_signal_library | 0.92 | False | duplicate_id:SIG-000126 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000129` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
