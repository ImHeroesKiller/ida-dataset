# Candidate Root Cause

**Generated:** 2026-08-07T15:20:16+00:00
**Session:** `SESSION-20260807-44CC29`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001515`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-44CC29`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001515': 1, 'duplicate_id:SIG-001517': 1, 'duplicate_id:SIG-001519': 1, 'duplicate_id:SIG-001516': 1, 'duplicate_id:SIG-001518': 1}`
- `candidate CAND-9A0E34B03E60 entity_id=SIG-001515 reason=duplicate_id:SIG-001515 conf=0.9`
- `candidate CAND-5DA8CA5A604D entity_id=SIG-001517 reason=duplicate_id:SIG-001517 conf=0.88`
- `candidate CAND-F6D4C7C28D5C entity_id=SIG-001519 reason=duplicate_id:SIG-001519 conf=0.92`
- `candidate CAND-A439EF1B02FE entity_id=SIG-001516 reason=duplicate_id:SIG-001516 conf=0.92`
- `candidate CAND-71B402E26622 entity_id=SIG-001518 reason=duplicate_id:SIG-001518 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-9A0E34B03E60 | business_signal_library | 0.9 | False | duplicate_id:SIG-001515 | Rejected |
| CAND-5DA8CA5A604D | business_signal_library | 0.88 | False | duplicate_id:SIG-001517 | Rejected |
| CAND-F6D4C7C28D5C | business_signal_library | 0.92 | False | duplicate_id:SIG-001519 | Rejected |
| CAND-A439EF1B02FE | business_signal_library | 0.92 | False | duplicate_id:SIG-001516 | Rejected |
| CAND-71B402E26622 | business_signal_library | 0.9 | False | duplicate_id:SIG-001518 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001515` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
