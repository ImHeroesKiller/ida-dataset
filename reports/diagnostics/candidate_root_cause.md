# Candidate Root Cause

**Generated:** 2026-08-02T17:25:10+00:00
**Session:** `SESSION-20260802-0F3A84`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001275`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260802-0F3A84`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001275': 1, 'duplicate_id:SIG-001276': 1, 'duplicate_id:SIG-001277': 1, 'duplicate_id:SIG-001279': 1, 'duplicate_id:SIG-001278': 1}`
- `candidate CAND-843F0C2B1EAE entity_id=SIG-001275 reason=duplicate_id:SIG-001275 conf=0.9`
- `candidate CAND-D4E3AB9B0FDC entity_id=SIG-001276 reason=duplicate_id:SIG-001276 conf=0.92`
- `candidate CAND-B1FFFE112A73 entity_id=SIG-001277 reason=duplicate_id:SIG-001277 conf=0.88`
- `candidate CAND-BA2C57D00319 entity_id=SIG-001279 reason=duplicate_id:SIG-001279 conf=0.92`
- `candidate CAND-227762168480 entity_id=SIG-001278 reason=duplicate_id:SIG-001278 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-843F0C2B1EAE | business_signal_library | 0.9 | False | duplicate_id:SIG-001275 | Rejected |
| CAND-D4E3AB9B0FDC | business_signal_library | 0.92 | False | duplicate_id:SIG-001276 | Rejected |
| CAND-B1FFFE112A73 | business_signal_library | 0.88 | False | duplicate_id:SIG-001277 | Rejected |
| CAND-BA2C57D00319 | business_signal_library | 0.92 | False | duplicate_id:SIG-001279 | Rejected |
| CAND-227762168480 | business_signal_library | 0.9 | False | duplicate_id:SIG-001278 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001275` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
