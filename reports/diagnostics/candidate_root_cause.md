# Candidate Root Cause

**Generated:** 2026-07-23T14:26:35+00:00
**Session:** `SESSION-20260723-2A5ED4`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000734`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260723-2A5ED4`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000734': 1, 'duplicate_id:SIG-000731': 1, 'duplicate_id:SIG-000732': 1, 'duplicate_id:SIG-000730': 1, 'duplicate_id:SIG-000733': 1}`
- `candidate CAND-FC205AEE74FF entity_id=SIG-000734 reason=duplicate_id:SIG-000734 conf=0.92`
- `candidate CAND-CEF0DCFFFE5A entity_id=SIG-000731 reason=duplicate_id:SIG-000731 conf=0.92`
- `candidate CAND-AFEFA89960CB entity_id=SIG-000732 reason=duplicate_id:SIG-000732 conf=0.88`
- `candidate CAND-FCD81F301C98 entity_id=SIG-000730 reason=duplicate_id:SIG-000730 conf=0.9`
- `candidate CAND-45665A708295 entity_id=SIG-000733 reason=duplicate_id:SIG-000733 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FC205AEE74FF | business_signal_library | 0.92 | False | duplicate_id:SIG-000734 | Rejected |
| CAND-CEF0DCFFFE5A | business_signal_library | 0.92 | False | duplicate_id:SIG-000731 | Rejected |
| CAND-AFEFA89960CB | business_signal_library | 0.88 | False | duplicate_id:SIG-000732 | Rejected |
| CAND-FCD81F301C98 | business_signal_library | 0.9 | False | duplicate_id:SIG-000730 | Rejected |
| CAND-45665A708295 | business_signal_library | 0.9 | False | duplicate_id:SIG-000733 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000734` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
