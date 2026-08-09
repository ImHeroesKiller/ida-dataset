# Candidate Root Cause

**Generated:** 2026-08-09T16:57:01+00:00
**Session:** `SESSION-20260809-F0E2AF`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001743`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-F0E2AF`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001743': 1, 'duplicate_id:SIG-001742': 1, 'duplicate_id:SIG-001740': 1, 'duplicate_id:SIG-001744': 1, 'duplicate_id:SIG-001741': 1}`
- `candidate CAND-2A771375FD96 entity_id=SIG-001743 reason=duplicate_id:SIG-001743 conf=0.9`
- `candidate CAND-40351E14956F entity_id=SIG-001742 reason=duplicate_id:SIG-001742 conf=0.88`
- `candidate CAND-8138D05BED19 entity_id=SIG-001740 reason=duplicate_id:SIG-001740 conf=0.9`
- `candidate CAND-D2F48A9278F0 entity_id=SIG-001744 reason=duplicate_id:SIG-001744 conf=0.92`
- `candidate CAND-E12CA40A4952 entity_id=SIG-001741 reason=duplicate_id:SIG-001741 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2A771375FD96 | business_signal_library | 0.9 | False | duplicate_id:SIG-001743 | Rejected |
| CAND-40351E14956F | business_signal_library | 0.88 | False | duplicate_id:SIG-001742 | Rejected |
| CAND-8138D05BED19 | business_signal_library | 0.9 | False | duplicate_id:SIG-001740 | Rejected |
| CAND-D2F48A9278F0 | business_signal_library | 0.92 | False | duplicate_id:SIG-001744 | Rejected |
| CAND-E12CA40A4952 | business_signal_library | 0.92 | False | duplicate_id:SIG-001741 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001743` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
