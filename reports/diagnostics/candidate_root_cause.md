# Candidate Root Cause

**Generated:** 2026-07-31T23:21:55+00:00
**Session:** `SESSION-20260731-09AA69`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001183`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260731-09AA69`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001183': 1, 'duplicate_id:SIG-001180': 1, 'duplicate_id:SIG-001182': 1, 'duplicate_id:SIG-001184': 1, 'duplicate_id:SIG-001181': 1}`
- `candidate CAND-0A7542E276F1 entity_id=SIG-001183 reason=duplicate_id:SIG-001183 conf=0.88`
- `candidate CAND-DE80ABA82006 entity_id=SIG-001180 reason=duplicate_id:SIG-001180 conf=0.9`
- `candidate CAND-955A2387C8EF entity_id=SIG-001182 reason=duplicate_id:SIG-001182 conf=0.9`
- `candidate CAND-71793D1412F9 entity_id=SIG-001184 reason=duplicate_id:SIG-001184 conf=0.9`
- `candidate CAND-06004B549E29 entity_id=SIG-001181 reason=duplicate_id:SIG-001181 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0A7542E276F1 | business_signal_library | 0.88 | False | duplicate_id:SIG-001183 | Rejected |
| CAND-DE80ABA82006 | business_signal_library | 0.9 | False | duplicate_id:SIG-001180 | Rejected |
| CAND-955A2387C8EF | business_signal_library | 0.9 | False | duplicate_id:SIG-001182 | Rejected |
| CAND-71793D1412F9 | business_signal_library | 0.9 | False | duplicate_id:SIG-001184 | Rejected |
| CAND-06004B549E29 | business_signal_library | 0.88 | False | duplicate_id:SIG-001181 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001183` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
