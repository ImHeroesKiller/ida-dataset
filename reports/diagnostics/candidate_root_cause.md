# Candidate Root Cause

**Generated:** 2026-08-05T04:30:31+00:00
**Session:** `SESSION-20260805-63349F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001402`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260805-63349F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001402': 1, 'duplicate_id:SIG-001403': 1, 'duplicate_id:SIG-001400': 1, 'duplicate_id:SIG-001404': 1, 'duplicate_id:SIG-001401': 1}`
- `candidate CAND-A7838EA40D1E entity_id=SIG-001402 reason=duplicate_id:SIG-001402 conf=0.88`
- `candidate CAND-FA20A4B6C529 entity_id=SIG-001403 reason=duplicate_id:SIG-001403 conf=0.9`
- `candidate CAND-B95FA6720EDC entity_id=SIG-001400 reason=duplicate_id:SIG-001400 conf=0.9`
- `candidate CAND-B8B42FE84E5C entity_id=SIG-001404 reason=duplicate_id:SIG-001404 conf=0.92`
- `candidate CAND-1A55F534E713 entity_id=SIG-001401 reason=duplicate_id:SIG-001401 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A7838EA40D1E | business_signal_library | 0.88 | False | duplicate_id:SIG-001402 | Rejected |
| CAND-FA20A4B6C529 | business_signal_library | 0.9 | False | duplicate_id:SIG-001403 | Rejected |
| CAND-B95FA6720EDC | business_signal_library | 0.9 | False | duplicate_id:SIG-001400 | Rejected |
| CAND-B8B42FE84E5C | business_signal_library | 0.92 | False | duplicate_id:SIG-001404 | Rejected |
| CAND-1A55F534E713 | business_signal_library | 0.92 | False | duplicate_id:SIG-001401 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001402` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
