# Candidate Root Cause

**Generated:** 2026-07-27T05:02:00+00:00
**Session:** `SESSION-20260727-A02275`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000938`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260727-A02275`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000938': 1, 'duplicate_id:SIG-000937': 1, 'duplicate_id:SIG-000935': 1, 'duplicate_id:SIG-000939': 1, 'duplicate_id:SIG-000936': 1}`
- `candidate CAND-FBD5988F66E0 entity_id=SIG-000938 reason=duplicate_id:SIG-000938 conf=0.9`
- `candidate CAND-A8F49D645E04 entity_id=SIG-000937 reason=duplicate_id:SIG-000937 conf=0.88`
- `candidate CAND-4447C65D1CF6 entity_id=SIG-000935 reason=duplicate_id:SIG-000935 conf=0.9`
- `candidate CAND-65101315B605 entity_id=SIG-000939 reason=duplicate_id:SIG-000939 conf=0.92`
- `candidate CAND-4D9A979368CF entity_id=SIG-000936 reason=duplicate_id:SIG-000936 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FBD5988F66E0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000938 | Rejected |
| CAND-A8F49D645E04 | business_signal_library | 0.88 | False | duplicate_id:SIG-000937 | Rejected |
| CAND-4447C65D1CF6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000935 | Rejected |
| CAND-65101315B605 | business_signal_library | 0.92 | False | duplicate_id:SIG-000939 | Rejected |
| CAND-4D9A979368CF | business_signal_library | 0.92 | False | duplicate_id:SIG-000936 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000938` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
